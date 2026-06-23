import os
import re
import glob

def is_noise_line(line, username):
    line = line.strip()
    if not line:
        return False # We handle empty lines separately
        
    noise_exact = [
        "All activity", "Posts", "Comments", "Videos", "Images", "More", 
        "Follow", "Like", "Comment", "Repost", "Send", "…more", "...more", "… see more",
        "Activate to view larger image,", "Activate to view larger image",
        "Connect", "Message", "Save", "Share", "Activity"
    ]
    if line in noise_exact:
        return True
        
    if line.lower() == username.lower():
        return True
        
    if re.match(r'^\d+$', line):
        return True
    if re.match(r'^\d+\s+(comments|reposts|likes|reactions|followers|connections)$', line, re.IGNORECASE):
        return True
    if re.match(r'^Loaded \d+ Posts', line):
        return True
    if re.match(r'^Feed post number \d+', line):
        return True
        
    if re.match(r'^\d+[mhdwy]\s*•', line):
        return True
    if re.match(r'^\d+\s+(days|weeks|months|years)\s+ago', line):
        return True
        
    if "• 3rd" in line or "• 2nd" in line or "• 1st" in line:
        return True
        
    # Remove URL links that are raw text noise if needed, but let's keep them for now.
    return False

def clean_text_block(text, username):
    lines = text.split('\n')
    cleaned = []
    
    for line in lines:
        if line.startswith('#'):
            cleaned.append(f"\n{line.strip()}\n")
            continue
            
        if is_noise_line(line, username):
            continue
            
        stripped = line.strip()
        if stripped:
            # Add a blank line before new paragraphs if it doesn't exist
            if cleaned and cleaned[-1] != "" and not cleaned[-1].startswith("#"):
                # If the line looks like a UI header, add space
                cleaned.append("")
            cleaned.append(stripped)
            cleaned.append("") # Force a blank line after every sentence/paragraph for readability

    # Remove consecutive blank lines
    final_cleaned = []
    for line in cleaned:
        if line == "" and (not final_cleaned or final_cleaned[-1] == ""):
            continue
        final_cleaned.append(line)
        
    return "\n".join(final_cleaned).strip()

def process_posts():
    files = glob.glob("research/linkedin-posts/*_posts.md")
    for filepath in files:
        filename = os.path.basename(filepath)
        username = filename.split('_')[0]
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        cleaned_content = clean_text_block(content, username)
        
        # Add visual dividers between posts
        # Heuristic: when we see the username or a new post structure, we can add '---'
        # For simplicity, since we forced newlines, it's already much more readable.
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
    print(f"Cleaned {len(files)} post files.")

def process_other():
    # Gather all usernames from the profile files
    profile_files = glob.glob("research/other/*_profile.md")
    usernames = [os.path.basename(f).split('_')[0] for f in profile_files]
    
    for username in usernames:
        profile_path = f"research/other/{username}_profile.md"
        featured_path = f"research/other/{username}_featured.md"
        
        merged_content = f"# Detailed Profile: {username}\n\n"
        
        if os.path.exists(profile_path):
            with open(profile_path, 'r', encoding='utf-8') as f:
                merged_content += f.read() + "\n\n"
            os.remove(profile_path)
            
        if os.path.exists(featured_path):
            with open(featured_path, 'r', encoding='utf-8') as f:
                merged_content += f.read() + "\n\n"
            os.remove(featured_path)
            
        cleaned_content = clean_text_block(merged_content, username)
        
        out_path = f"research/other/{username}_details.md"
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
            
    print(f"Merged and cleaned data for {len(usernames)} users into author_details files.")

def main():
    print("Formatting posts...")
    process_posts()
    
    print("Consolidating and formatting profiles...")
    process_other()
    
    print("Done!")

if __name__ == "__main__":
    main()
