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

def extract_safe(page, url):
    try:
        print(f"  -> Navigating to {url}")
        page.goto(url, wait_until="domcontentloaded", timeout=20000)
        time.sleep(3) # Wait for content to render
        
        # Scroll down a few times to trigger lazy loading
        for _ in range(3):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            
        # Try to get the main element
        main_locator = page.locator("main")
        if main_locator.count() > 0:
            return main_locator.inner_text()
        return page.inner_text("body")
    except Exception as e:
        print(f"  -> Error extracting {url}: {e}")
        return f"Error: {e}"

def scrape():
    if not os.path.exists("auth_state.json"):
        print("Please run with --login first.")
        return
        
    with open("experts_list.json", "r") as f:
        usernames = json.load(f)
        
    os.makedirs(os.path.join("research", "linkedin-posts"), exist_ok=True)
    os.makedirs(os.path.join("research", "other"), exist_ok=True)
    
    with sync_playwright() as p:
        # Using headless=False is safer against bot detection, though it pops up a window
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="auth_state.json")
        page = context.new_page()
        
        for username in usernames:
            print(f"\nScraping {username}...")
            
            # 1. Main Profile (Includes About, headline, etc.)
            profile_text = extract_safe(page, f"https://www.linkedin.com/in/{username}/")
            
            # 2. Experience
            experience_text = extract_safe(page, f"https://www.linkedin.com/in/{username}/details/experience/")
            
            # 3. Recommendations
            recommendations_text = extract_safe(page, f"https://www.linkedin.com/in/{username}/details/recommendations/")
            
            # 4. Featured
            featured_text = extract_safe(page, f"https://www.linkedin.com/in/{username}/details/featured/")
            
            # 5. Posts (Shares)
            posts_text = extract_safe(page, f"https://www.linkedin.com/in/{username}/recent-activity/all/")
            
            # Save Profile Data
            md_content = f"# Profile: {username}\n\n"
            md_content += f"## Main Profile & About\n{profile_text}\n\n"
            md_content += f"## Experience\n{experience_text}\n\n"
            md_content += f"## Recommendations\n{recommendations_text}\n\n"
            
            with open(os.path.join("research", "other", f"{username}_profile.md"), "w", encoding="utf-8") as f:
                f.write(md_content)
                
            # Save Featured Data
            with open(os.path.join("research", "other", f"{username}_featured.md"), "w", encoding="utf-8") as f:
                f.write(f"# Featured for {username}\n\n{featured_text}")
                
            # Save Posts Data
            with open(os.path.join("research", "linkedin-posts", f"{username}_posts.md"), "w", encoding="utf-8") as f:
                f.write(f"# Recent Posts for {username}\n\n{posts_text}")
                
            # Sleep between profiles to mimic human behavior
            time.sleep(5)

        browser.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--login", action="store_true", help="Log in and save state")
    parser.add_argument("--scrape", action="store_true", help="Scrape profiles")
    args = parser.parse_args()
    
    if args.login:
        login()
    elif args.scrape:
        scrape()
    else:
        print("Please specify --login or --scrape")
