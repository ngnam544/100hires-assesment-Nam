import argparse
import json
import os
import re
import time
import random
from playwright.sync_api import sync_playwright



def human_scroll(page):
    scroll_steps = random.randint(3, 5)
    for _ in range(scroll_steps):
        scroll_amount = random.randint(300, 700)
        page.mouse.wheel(0, scroll_amount)
        time.sleep(random.uniform(0.5, 1.5))

AUTH_STATE_FILE = "auth_state.json"
EXPERTS_FILE = "experts_list.json"
POST_SCROLLS = 10
PROFILE_SCROLLS = 3
NAVIGATION_RETRIES = 2

AUTH_BLOCK_MARKERS = [
    "Join LinkedIn",
    "Already on Linkedin? Sign in",
    "Already on LinkedIn? Sign in",
    "Email or phone",
    "Password (6+ characters)",
    "LinkedIn is better on the app",
    "Your account has been temporarily restricted",
    "unusually high volume of LinkedIn profile data",
    "Your restriction will be lifted",
]

ELLIPSIS = "\u2026"
BULLET = "\u2022"


class AuthBlockedError(Exception):
    pass


def parse_posts(raw_text, expert_name):
    posts = []
    current_post = []
    state = "SEARCHING_FOR_POST"

    header_lines = []
    is_quote_repost = False
    is_pure_repost = False

    lines = raw_text.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            if state == "IN_CONTENT" and current_post and current_post[-1] != "":
                current_post.append("")
            continue

        if re.match(r"^Feed post number \d+", line):
            if current_post and not is_pure_repost and not is_quote_repost:
                while current_post and current_post[-1] == "":
                    current_post.pop()
                if current_post:
                    posts.append("\n".join(current_post))

            current_post = []
            header_lines = []
            is_quote_repost = False
            is_pure_repost = False
            state = "SKIPPING_HEADER"
            continue

        if state == "SKIPPING_HEADER":
            header_lines.append(line)
            if has_timestamp(line):
                header_text = "\n".join(header_lines).lower()
                activity_phrases = [
                    "reposted this",
                    "likes this",
                    "commented on",
                    "replied to",
                    "celebrates this",
                    "supports this",
                    "loves this",
                    "finds this",
                    "was mentioned in",
                    "shared this",
                ]

                if any(phrase in header_text for phrase in activity_phrases):
                    is_pure_repost = True
                else:
                    author_name = header_lines[0].lower() if header_lines else ""
                    name_parts = author_name.split()
                    if name_parts and not any(len(part) >= 3 and part in expert_name.lower() for part in name_parts):
                        is_pure_repost = True

                state = "WAITING_FOR_CONTENT_START"
            continue

        if state == "WAITING_FOR_CONTENT_START":
            if line == "Follow":
                continue
            state = "IN_CONTENT"
            current_post.append(line)
            continue

        if state == "IN_CONTENT":
            stop_phrases = [
                f"{ELLIPSIS}more",
                "...more",
                f"{ELLIPSIS} see more",
                "â€¦more",
                "â€¦ see more",
                "Activate to view larger image,",
                "Activate to view larger image",
                "Like",
                "Comment",
                "Repost",
                "Send",
                "Share",
            ]
            if line in stop_phrases or re.match(r"^\d+$", line) or re.match(r"^\d+\s+(comments|reposts|likes)$", line):
                state = "SEARCHING_FOR_POST"
                continue

            if has_timestamp(line):
                is_quote_repost = True

            current_post.append(line)

    if current_post and not is_pure_repost and not is_quote_repost:
        while current_post and current_post[-1] == "":
            current_post.pop()
        if current_post:
            posts.append("\n".join(current_post))

    return posts


def has_timestamp(line):
    return (
        "ago \u2022" in line
        or "ago â€¢" in line
        or re.match(r"^\d+\s+(days|weeks|months|years|hours|minutes)\s+ago", line)
    )


def is_noise_line(line, username):
    line = line.strip()
    if not line:
        return False

    noise_exact = [
        "All activity",
        "Posts",
        "Comments",
        "Videos",
        "Images",
        "More",
        "Follow",
        "Like",
        "Comment",
        "Repost",
        "Send",
        "Share",
        f"{ELLIPSIS}more",
        "...more",
        f"{ELLIPSIS} see more",
        "â€¦more",
        "â€¦ see more",
        "Activate to view larger image,",
        "Activate to view larger image",
        "Connect",
        "Message",
        "Save",
        "Activity",
    ]
    if line in noise_exact:
        return True
    if line.lower() == username.lower():
        return True
    if re.match(r"^\d+$", line):
        return True
    if re.match(r"^\d+\s+(comments|reposts|likes|reactions|followers|connections)$", line, re.IGNORECASE):
        return True
    if re.match(r"^Loaded \d+ Posts", line):
        return True
    if re.match(r"^Feed post number \d+", line):
        return True
    if re.match(r"^\d+[mhdwy]\s*(\u2022|â€¢)", line):
        return True
    if re.match(r"^\d+\s+(days|weeks|months|years)\s+ago", line):
        return True
    if any(marker in line for marker in ["\u2022 3rd", "\u2022 2nd", "\u2022 1st", "â€¢ 3rd", "â€¢ 2nd", "â€¢ 1st"]):
        return True
    if "Verified" in line:
        return True
    return False


def clean_text_block(text, username):
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        if line.startswith("#"):
            cleaned.append(f"\n{line.strip()}\n")
            continue
        if is_noise_line(line, username):
            continue
        stripped = line.strip()
        if stripped:
            if cleaned and cleaned[-1] != "" and not cleaned[-1].startswith("#"):
                cleaned.append("")
            cleaned.append(stripped)
            cleaned.append("")

    final_cleaned = []
    for line in cleaned:
        if line == "" and (not final_cleaned or final_cleaned[-1] == ""):
            continue
        final_cleaned.append(line)
    return "\n".join(final_cleaned).strip()


def login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.linkedin.com/login")
        print("Please log in to LinkedIn in the browser window.")
        input("Press Enter here in the console AFTER you have successfully logged in...")
        context.storage_state(path=AUTH_STATE_FILE)
        browser.close()


def get_main_text(page):
    if page.locator("main").count() > 0:
        return page.locator("main").inner_text()
    return page.inner_text("body")


def is_auth_blocked(text, page):
    if "/login" in page.url or "/signup" in page.url:
        return True
    return any(marker in text for marker in AUTH_BLOCK_MARKERS)


def navigate_and_extract(page, url, scrolls=PROFILE_SCROLLS, timeout=20000):
    last_error = None
    for attempt in range(1, NAVIGATION_RETRIES + 1):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=timeout)
            time.sleep(2)
            for _ in range(scrolls):
                human_scroll(page)

            text = get_main_text(page)
            if is_auth_blocked(text, page):
                return "auth_blocked", text, None
            return "ok", text, None
        except Exception as e:
            last_error = e
            print(f"    Attempt {attempt}/{NAVIGATION_RETRIES} failed for {url}: {e}")
            time.sleep(2)
    return "error", "", last_error


def write_status_file(path, title, message):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{message}\n")


def scrape_posts(page, username):
    posts_path = os.path.join("research", "linkedin-posts", f"{username}_posts.md")
    posts_url = f"https://www.linkedin.com/in/{username}/recent-activity/all/"
    status, raw_text, error = navigate_and_extract(page, posts_url, scrolls=0)

    if status == "auth_blocked":
        raise AuthBlockedError(f"LinkedIn login/session blocked while opening posts for {username}. Run --login again.")
    if status == "error":
        write_status_file(posts_path, f"Posts for {username}", f"ERROR: {error}")
        return 0, False, error

    all_posts = []
    seen_posts = set()

    for _ in range(POST_SCROLLS):
        raw_text = get_main_text(page)
        if is_auth_blocked(raw_text, page):
            raise AuthBlockedError(f"LinkedIn login/session blocked while scrolling posts for {username}. Run --login again.")

        parsed_batch = parse_posts(raw_text, username)
        for post in parsed_batch:
            if post not in seen_posts:
                seen_posts.add(post)
                all_posts.append(post)
                if len(all_posts) == 20:
                    break
                    
        if len(all_posts) == 20:
            break

        human_scroll(page)

    posts_content = f"# 🗂️ Cleaned Posts for {username} (Found {len(all_posts)})\n\n"
    for i, post in enumerate(all_posts, 1):
        posts_content += f"### 📝 Post {i}\n────────────────────────────────────────\n{post}\n\n\n"

    with open(posts_path, "w", encoding="utf-8") as f:
        f.write(posts_content)

    return len(all_posts), False, None


def scrape_profile_details(page, username):
    details_content = f"# Detailed Profile: {username}\n\n"
    sections = [
        ("Main Profile & About", f"https://www.linkedin.com/in/{username}/"),
        ("Experience", f"https://www.linkedin.com/in/{username}/details/experience/"),
        ("Featured", f"https://www.linkedin.com/in/{username}/details/featured/"),
        ("Recommendations (Received)", f"https://www.linkedin.com/in/{username}/details/recommendations/?detailScreenTabIndex=0"),
    ]

    section_statuses = {}
    errors = []

    for title, url in sections:
        print(f"  -> Scraping {title}")
        status, raw, error = navigate_and_extract(page, url, scrolls=PROFILE_SCROLLS)
        section_statuses[title] = status
        if status == "ok":
            cleaned = clean_text_block(raw, username)
            details_content += f"## {title}\n{cleaned}\n\n"
        elif status == "auth_blocked":
            raise AuthBlockedError(f"LinkedIn login/session blocked while scraping {title} for {username}. Run --login again.")
        else:
            errors.append(f"{title}: {error}")
            details_content += f"## {title}\nERROR: {error}\n\n"

    details_path = os.path.join("research", "other", f"{username}_details.md")
    with open(details_path, "w", encoding="utf-8") as f:
        f.write(details_content)

    return section_statuses, False, errors


def scrape():
    if not os.path.exists(AUTH_STATE_FILE):
        print("Please run with --login first.")
        return

    with open(EXPERTS_FILE, "r", encoding="utf-8") as f:
        usernames = json.load(f)

    os.makedirs(os.path.join("research", "linkedin-posts"), exist_ok=True)
    os.makedirs(os.path.join("research", "other"), exist_ok=True)

    run_report = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=AUTH_STATE_FILE)
        page = context.new_page()

        try:
            for username in usernames:
                print(f"\nScraping V3 {username}...")
                print("  -> Scraping Posts")
                posts_found, posts_auth_blocked, posts_error = scrape_posts(page, username)

                section_statuses, details_auth_blocked, detail_errors = scrape_profile_details(page, username)
                errors = detail_errors[:]
                if posts_error:
                    errors.append(f"Posts: {posts_error}")

                run_report.append({
                    "username": username,
                    "posts_found": posts_found,
                    "auth_blocked": posts_auth_blocked or details_auth_blocked,
                    "sections": section_statuses,
                    "errors": errors,
                })

                time.sleep(3)
        except AuthBlockedError as e:
            print(f"\nSTOPPED: {e}")
            print("No auth-blocked output was written for the current profile.")
            raise SystemExit(1)
        finally:
            browser.close()

    print("\nScrape summary")
    print("=" * 60)
    for item in run_report:
        section_status = ", ".join(f"{name}={status}" for name, status in item["sections"].items())
        auth_note = " AUTH_BLOCKED" if item["auth_blocked"] else ""
        print(f"{item['username']}: posts={item['posts_found']}; {section_status}{auth_note}")
        for error in item["errors"]:
            print(f"  - {error}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--login", action="store_true")
    parser.add_argument("--scrape", action="store_true")
    args = parser.parse_args()

    if args.login:
        login()
    elif args.scrape:
        scrape()
    else:
        print("Please specify --login or --scrape")
