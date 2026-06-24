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
            if line in ["Follow", "hashtag"]:
                continue
            state = "IN_CONTENT"
            current_post.append(line)
            continue

        if state == "IN_CONTENT":
            stop_phrases = [
                f"{ELLIPSIS}more",
                "...more",
                f"{ELLIPSIS} see more",
                "…more",
                "… see more",
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

            if line == "hashtag":
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
        or "ago •" in line
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
        "…more",
        "… see more",
        "Activate to view larger image,",
        "Activate to view larger image",
        "Connect",
        "Message",
        "Save",
        "Activity",
        "hashtag",
        "Profile enhanced with Premium",
        "Contact info",
        "Accessibility",
        "Talent Solutions",
        "Community Guidelines",
        "Careers",
        "Marketing Solutions",
        "Privacy & Terms",
        "Ad Choices",
        "Advertising",
        "Sales Solutions",
        "Safety Center",
        "Questions?",
        "Visit our Help Center.",
        "Manage your account and privacy",
        "Go to your Settings.",
        "Recommendation transparency",
        "Learn more about Recommended Content.",
        "Select language",
        "Ø§Ù„Ø¹Ø±Ø¨ÙŠØ© (Arabic)",
        "à¦¬à¦¾à¦‚à¦²à¦¾ (Bangla)",
        "ÄŒeÅ¡tina (Czech)",
        "Dansk (Danish)",
        "Deutsch (German)",
        "Î•Î»Î»Î·Î½Î¹ÎºÎ¬ (Greek)",
        "English (English)",
        "Español (Spanish)",
        "ÙØ§Ø±Ø³ÛŒ (Persian)",
        "Suomi (Finnish)",
        "Français (French)",
        "à¤¹à¤¿à¤‚à¤¦à¥€ (Hindi)",
        "Magyar (Hungarian)",
        "Bahasa Indonesia (Indonesian)",
        "Italiano (Italian)",
        "×¢×‘×¨×™×ª (Hebrew)",
        "æ—¥æœ¬èªž (Japanese)",
        "í•œêµ­ì–´ (Korean)",
        "à¤®à¤°à¤¾à¤ à¥€ (Marathi)",
        "Bahasa Malaysia (Malay)",
        "Nederlands (Dutch)",
        "Norsk (Norwegian)",
        "à¨ªà©°à¨œà¨¾à¨¬à©€ (Punjabi)",
        "Polski (Polish)",
        "Português (Portuguese)",
        "Română (Romanian)",
        "Ð ÑƒÑÑÐºÐ¸Ð¹ (Russian)",
        "Svenska (Swedish)",
        "à°¤à±†à°²à±à°—à± (Telugu)",
        "à¸ à¸²à¸©à¸²à¹„à¸—à¸¢ (Thai)",
        "Tagalog (Tagalog)",
        "Türkçe (Turkish)",
        "Ð£ÐºÑ€Ð°Ñ—Ð½ÑÑŒÐºÐ° (Ukrainian)",
        "Tiáº¿ng Viá»‡t (Vietnamese)",
        "ç®€ä½“ä¸­æ–‡ (Chinese (Simplified))",
        "æ­£é«”ä¸­æ–‡ (Chinese (Traditional))",
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
    if re.match(r"^\d+[mhdwy]\s*(\u2022|•)", line):
        return True
    if re.match(r"^\d+\s+(days|weeks|months|years)\s+ago", line):
        return True
    if any(marker in line for marker in ["\u2022 3rd", "\u2022 2nd", "\u2022 1st", "• 3rd", "• 2nd", "• 1st"]):
        return True
    if "Verified" in line:
        return True
    return False


def clean_text_block(text, username, title="Unknown"):
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()

        # Stop completely when we hit footer elements or right rail
        if "Accessibility" == stripped or "Select language" == stripped:
            break
        if stripped.startswith("People who follow "):
            break
        if "People you may know" in stripped:
            break
        if "Others named " in stripped:
            break

        if title == "Main Profile & About":
            if stripped in ["Featured", "Activity", "Experience", "Education", "Licenses & certifications", "Skills", "Recommendations", "Volunteering"]:
                break

        # Ignore noisy lines defined in is_noise_line
        if is_noise_line(line, username):
            continue

        # Ignore UI artifacts (reactions, comments, alone dot)
        if stripped == "·" or stripped == "•" or stripped == "\u2022":
            continue
        if ", number of reactions" in stripped:
            continue
        if "comments ·" in stripped and "reposts" in stripped:
            continue

        # Append lines, preserving natural blank lines
        if stripped:
            cleaned.append(stripped)
        else:
            # Only add a blank line if the previous line wasn't blank
            if cleaned and cleaned[-1] != "":
                cleaned.append("")

    # Final pass to ensure no double blanks and clean edges
    final_text = "\n".join(cleaned).strip()
    return final_text

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
    if page.locator("div.scaffold-layout__main").count() > 0:
        return page.locator("div.scaffold-layout__main").inner_text()
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
    details_content = f"# 🧑‍💼 Detailed Profile: {username}\n\n"
    sections = [
        ("Main Profile & About", f"https://www.linkedin.com/in/{username}/"),
        ("Experience", f"https://www.linkedin.com/in/{username}/details/experience/"),
        ("Recommendations (Received)", f"https://www.linkedin.com/in/{username}/details/recommendations/?detailScreenTabIndex=0"),
    ]

    section_statuses = {}
    errors = []

    for title, url in sections:
        print(f"  -> Scraping {title}")
        status, raw, error = navigate_and_extract(page, url, scrolls=PROFILE_SCROLLS)
        section_statuses[title] = status
        if status == "ok":
            cleaned_text = clean_text_block(raw, username, title)
            if cleaned_text:
                details_content += f"==================================================\n"
                details_content += f"## 📌 {title}\n"
                details_content += f"==================================================\n\n"
                details_content += f"{cleaned_text}\n\n"
        elif status == "auth_blocked":
            raise AuthBlockedError(f"LinkedIn login/session blocked while scraping {title} for {username}. Run --login again.")
        else:
            errors.append(f"{title}: {error}")
            details_content += f"## {title}\nERROR: {error}\n\n"

    details_path = os.path.join("research", "other", f"{username}_details.md")
    with open(details_path, "w", encoding="utf-8") as f:
        f.write(details_content)

    return section_statuses, False, errors


def scrape(single_user=None):
    if not os.path.exists(AUTH_STATE_FILE):
        print("Please run with --login first.")
        return

    if single_user:
        usernames = [single_user]
    else:
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
    parser.add_argument("--user", type=str, help="Scrape a single specific username")
    args = parser.parse_args()

    if args.login:
        login()
    elif args.scrape or args.user:
        scrape(single_user=args.user)
    else:
        print("Please specify --login, --scrape, or --user <username>")
