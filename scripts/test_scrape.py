import os
import time
from playwright.sync_api import sync_playwright

def test_scrape():
    username = "ericakuhl"
    print(f"Testing scrape for {username}...")
    
    os.makedirs("research", exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="auth_state.json")
        page = context.new_page()
        
        url = f"https://www.linkedin.com/in/{username}/recent-activity/all/"
        print(f"Navigating to {url}")
        page.goto(url, wait_until="domcontentloaded")
        time.sleep(3)
        
        # Scroll exactly 4 times (each scroll usually loads 5-10 posts)
        for i in range(4):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            
        main_locator = page.locator("main")
        if main_locator.count() > 0:
            raw_text = main_locator.inner_text()
        else:
            raw_text = page.inner_text("body")
            
        out_path = f"research/{username}_raw_test.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(raw_text)
            
        print(f"Saved raw text to {out_path}")
        browser.close()

if __name__ == "__main__":
    test_scrape()
