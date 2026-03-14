import os
import json
import re
import glob
import html

SITE_BASE_URL = os.environ.get('SITE_BASE_URL', 'https://blog.kapy.ca').rstrip('/')


def extract_metadata(filepath):
    title = ""
    summary = ""
    first_paragraph = ""

    if not os.path.exists(filepath):
        return title, summary, first_paragraph

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title (first # heading)
    match_title = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match_title:
        title = match_title.group(1).strip()

    # Extract first meaningful paragraph
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
        if line.startswith('[!['):
            continue
        if line.startswith('**GitHub**') or line.startswith('**Stars**'):
            continue

        clean_line = re.sub(r'[*_~`]', '', line)
        clean_line = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_line)
        clean_line = clean_line.strip()

        first_paragraph = clean_line
        summary = clean_line[:150] + '...' if len(clean_line) > 150 else clean_line
        break

    return title, summary, first_paragraph


def render_preview_page(article):
    article_id = article['id']
    slug = article['slug']
    title = article['zh']['title'] or article['en']['title'] or slug
    summary = article['zh']['summary'] or article['en']['summary'] or ''
    first_p = article['zh'].get('first_paragraph') or article['en'].get('first_paragraph') or summary

    share_url = f"{SITE_BASE_URL}/p/{article_id}_{slug}.html"
    read_url = f"{SITE_BASE_URL}/?article={article_id}"

    title_e = html.escape(title)
    summary_e = html.escape(summary)
    first_p_e = html.escape(first_p)
    share_url_e = html.escape(share_url)
    read_url_e = html.escape(read_url)

    return f"""<!doctype html>
<html lang=\"zh-CN\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>{title_e} | External Brain</title>
  <meta name=\"description\" content=\"{summary_e}\" />

  <meta property=\"og:type\" content=\"article\" />
  <meta property=\"og:site_name\" content=\"External Brain\" />
  <meta property=\"og:title\" content=\"{title_e}\" />
  <meta property=\"og:description\" content=\"{summary_e}\" />
  <meta property=\"og:url\" content=\"{share_url_e}\" />

  <meta name=\"twitter:card\" content=\"summary\" />
  <meta name=\"twitter:title\" content=\"{title_e}\" />
  <meta name=\"twitter:description\" content=\"{summary_e}\" />
  <link rel=\"canonical\" href=\"{share_url_e}\" />

  <style>
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, Arial, sans-serif;
      background: #f5f5f7;
      color: #1f2937;
    }}
    .wrap {{
      max-width: 760px;
      margin: 0 auto;
      padding: 28px 20px 40px;
    }}
    .card {{
      background: #fff;
      border-radius: 14px;
      padding: 24px;
      box-shadow: 0 8px 24px rgba(0,0,0,.08);
    }}
    h1 {{ margin: 0 0 14px; font-size: 28px; line-height: 1.28; }}
    .summary {{ color: #4b5563; margin: 0 0 10px; }}
    .firstp {{ color: #374151; margin: 0 0 22px; }}
    .actions {{ display:flex; gap:10px; flex-wrap:wrap; }}
    .btn {{
      display:inline-block;
      text-decoration:none;
      border-radius:10px;
      padding:10px 14px;
      font-weight:600;
      border:1px solid #d1d5db;
      color:#111827;
      background:#fff;
    }}
    .btn.primary {{ border-color:#007aff; background:#007aff; color:#fff; }}
  </style>
</head>
<body>
  <div class=\"wrap\">
    <div class=\"card\">
      <h1>{title_e}</h1>
      <p class=\"summary\">{summary_e}</p>
      <p class=\"firstp\">{first_p_e}</p>
      <div class=\"actions\">
        <a class=\"btn primary\" href=\"{read_url_e}\">在阅读页打开全文</a>
        <a class=\"btn\" href=\"{SITE_BASE_URL}/\">返回首页</a>
      </div>
    </div>
  </div>
</body>
</html>
"""


def generate_preview_pages(sorted_articles):
    out_dir = 'p'
    os.makedirs(out_dir, exist_ok=True)

    # clear stale generated html (safe because this dir is fully generated)
    for existing in glob.glob(os.path.join(out_dir, '*.html')):
      try:
        os.remove(existing)
      except OSError:
        pass

    for article in sorted_articles:
        filename = f"{article['id']}_{article['slug']}.html"
        path = os.path.join(out_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(render_preview_page(article))


def main():
    files = glob.glob('*_*.cleaned.md')

    # Group by prefix N
    articles = {}
    for f in files:
        if f.endswith('.zh.md'):
            continue

        match = re.match(r'^(\d+)_([^/]+)\.cleaned\.md$', f)
        if match:
            num = int(match.group(1))
            slug = match.group(2)

            en_file = f
            zh_file = f"{num}_{slug}.cleaned.zh.md"

            en_title, en_summary, en_first_paragraph = extract_metadata(en_file)
            zh_title, zh_summary, zh_first_paragraph = extract_metadata(zh_file)

            if not zh_title:
                zh_title = en_title
            if not zh_summary:
                zh_summary = en_summary
            if not zh_first_paragraph:
                zh_first_paragraph = en_first_paragraph

            articles[num] = {
                "id": num,
                "slug": slug,
                "en": {
                    "title": en_title,
                    "summary": en_summary,
                    "first_paragraph": en_first_paragraph,
                    "file": en_file
                },
                "zh": {
                    "title": zh_title,
                    "summary": zh_summary,
                    "first_paragraph": zh_first_paragraph,
                    "file": zh_file if os.path.exists(zh_file) else en_file
                }
            }

    # Sort descending by ID
    sorted_articles = [articles[k] for k in sorted(articles.keys(), reverse=True)]

    with open('articles.json', 'w', encoding='utf-8') as f:
        json.dump(sorted_articles, f, ensure_ascii=False, indent=2)

    generate_preview_pages(sorted_articles)

    print(f"Generated articles.json with {len(sorted_articles)} articles.")
    print(f"Generated {len(sorted_articles)} preview pages under /p")


if __name__ == '__main__':
    main()
