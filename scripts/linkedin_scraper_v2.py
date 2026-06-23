import json
import time
import os
import argparse
from playwright.sync_api import sync_playwright

def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.linkedin.com/login")
        print("="*60)
        print("Please log in to LinkedIn in the browser window.")
        print("="*60)
        input("Press Enter here in the console AFTER you have successfully logged in and the feed has loaded...")
        context.storage_state(path="auth_state.json")
        print("Authentication state saved to auth_state.json")
        browser.close()

def extract_meaningful_text_from_json(obj, min_length=25):
    """Recursively search JSON for 'text' fields that contain actual content."""
    texts = []
    if isinstance(obj, dict):
        if "text" in obj and isinstance(obj["text"], str):
            val = obj["text"].strip()
            # Filter out URNs, JSON strings, and short UI elements
            if (len(val) >= min_length and 
                not val.startswith("urn:li:") and 
                not val.startswith("http") and
                "{" not in val):
                texts.append(val)
        for k, v in obj.items():
            texts.extend(extract_meaningful_text_from_json(v, min_length))
    elif isinstance(obj, list):
        for item in obj:
            texts.extend(extract_meaningful_text_from_json(item, min_length))
    return texts

class LinkedInInterceptor:
    def __init__(self):
        self.current_section_texts = []

    def handle_response(self, response):
        try:
            url = response.url
            # LinkedIn uses graphql and voyager/api for data fetching
            if ("graphql" in url or "voyager/api" in url) and response.request.method != "OPTIONS":
                content_type = response.headers.get("content-type", "")
                if "json" in content_type:
                    data = response.json()
                    texts = extract_meaningful_text_from_json(data)
                    self.current_section_texts.extend(texts)
        except Exception:
            pass

    def clear(self):
        self.current_section_texts = []

    def get_unique_texts(self):
        # Remove exact duplicates while preserving order
        seen = set()
        result = []
        for text in self.current_section_texts:
            if text not in seen:
                seen.add(text)
                result.append(text)
        return result

def scrape_section(page, interceptor, url):
    interceptor.clear()
    print(f"  -> Navigating to {url}")
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=20000)
        time.sleep(3) # Wait for initial API calls
        
        # Scroll to trigger pagination API calls
        for _ in range(4):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)
            
    except Exception as e:
        print(f"  -> Error navigating: {e}")
        
    texts = interceptor.get_unique_texts()
    return "\n\n".join(texts) if texts else "*No detailed text found in JSON API. Page might be empty or restricted.*"

def scrape():
    if not os.path.exists("auth_state.json"):
        print("Please run with --login first.")
        return
        
    with open("experts_list.json", "r") as f:
        usernames = json.load(f)
        
    os.makedirs(os.path.join("research", "linkedin-posts"), exist_ok=True)
    os.makedirs(os.path.join("research", "other"), exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="auth_state.json")
        page = context.new_page()
        
        interceptor = LinkedInInterceptor()
        page.on("response", interceptor.handle_response)
        
        for username in usernames:
            print(f"\nScraping V2 {username}...")
            
            # 1. Main Profile (About & Top Card)
            profile_text = scrape_section(page, interceptor, f"https://www.linkedin.com/in/{username}/")
            
            # 2. Experience
            experience_text = scrape_section(page, interceptor, f"https://www.linkedin.com/in/{username}/details/experience/")
            
            # 3. Recommendations (Received tab)
            recommendations_text = scrape_section(page, interceptor, f"https://www.linkedin.com/in/{username}/details/recommendations/?detailScreenTabIndex=0")
            
            # 4. Featured
            featured_text = scrape_section(page, interceptor, f"https://www.linkedin.com/in/{username}/details/featured/")
            
            # 5. Posts (All Activity)
            posts_text = scrape_section(page, interceptor, f"https://www.linkedin.com/in/{username}/recent-activity/all/")
            
            # Save Profile Data
            md_content = f"# Detailed Profile: {username}\n\n"
            md_content += f"## Main Profile & About\n{profile_text}\n\n"
            md_content += f"## Experience\n{experience_text}\n\n"
            md_content += f"## Featured\n{featured_text}\n\n"
            md_content += f"## Recommendations (Received)\n{recommendations_text}\n\n"
            
            with open(os.path.join("research", "other", f"{username}_details.md"), "w", encoding="utf-8") as f:
                f.write(md_content)
                
            # Save Posts Data
            with open(os.path.join("research", "linkedin-posts", f"{username}_posts.md"), "w", encoding="utf-8") as f:
                f.write(f"# Recent Posts for {username}\n\n{posts_text}")
                
            time.sleep(5)

        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--login", action="store_true", help="Log in and save state")
    parser.add_argument("--scrape", action="store_true", help="Scrape profiles V2")
    args = parser.parse_args()
    
    if args.login:
        login()
    elif args.scrape:
        scrape()
    else:
        print("Please specify --login or --scrape")
