import os
import json
import re
import glob

def extract_metadata(filepath):
    title = ""
    summary = ""
    if not os.path.exists(filepath):
        return title, summary

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title (first # heading)
    match_title = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match_title:
        title = match_title.group(1).strip()
    
    # Extract Summary (first paragraph that is not a heading, quote, image, or link wrapper)
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('#'):
            continue
        if line.startswith('>'):
            continue
        if line.startswith('!['):
            continue
        if line.startswith('[!['): # Filter out image links like [![Image 1...
            continue
        if line.startswith('**GitHub**') or line.startswith('**Stars**'):
            continue
            
        # Optional: strip simple markdown characters from summary for cleaner text
        clean_line = re.sub(r'[*_~`]', '', line)
        clean_line = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_line) # remove link URLs but keep text
        
        summary = clean_line[:150] + '...' if len(clean_line) > 150 else clean_line
        break

    return title, summary

def main():
    repo_dir = '.'
    files = glob.glob('*_*.cleaned.md')
    
    # Group by prefix N
    articles = {}
    for f in files:
        # Ignore zh files in this pass, we will look them up
        if f.endswith('.zh.md'):
            continue
            
        match = re.match(r'^(\d+)_([^/]+)\.cleaned\.md$', f)
        if match:
            num = int(match.group(1))
            slug = match.group(2)
            
            en_file = f
            zh_file = f"{num}_{slug}.cleaned.zh.md"
            
            en_title, en_summary = extract_metadata(en_file)
            zh_title, zh_summary = extract_metadata(zh_file)
            
            if not zh_title:
                zh_title = en_title
            if not zh_summary:
                zh_summary = en_summary
                
            articles[num] = {
                "id": num,
                "slug": slug,
                "en": {
                    "title": en_title,
                    "summary": en_summary,
                    "file": en_file
                },
                "zh": {
                    "title": zh_title,
                    "summary": zh_summary,
                    "file": zh_file if os.path.exists(zh_file) else en_file
                }
            }
            
    # Sort descending by ID
    sorted_articles = [articles[k] for k in sorted(articles.keys(), reverse=True)]
    
    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_articles, f, ensure_ascii=False, indent=2)

    print(f"Generated articles.json with {len(sorted_articles)} articles.")

if __name__ == '__main__':
    main()