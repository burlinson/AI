Perfect — Option 2 is the “scan everything automatically” route, and it’s exactly the kind of structured, high‑leverage workflow you like. Let’s build you a clean, repeatable script that:
- Crawls your entire Jekyll repo
- Scans every .md and .html file
- Extracts all links
- Outputs a clean CSV or Markdown table you can paste anywhere
- Shows link text, URL, and which file it came from
This gives you a full inventory of every link across your consulting blog.
Below is the polished version you can run locally.

🧰 Your Local Link‑Extraction Script (Python)
This script works on any Jekyll site, including Beautiful Jekyll.
1. Save this as extract_links.py in your repo root
import os
import re
import csv

# Regex for Markdown links: [text](url)
md_link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

# Regex for HTML links: <a href="url">text</a>
html_link_pattern = re.compile(r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.IGNORECASE)

output = []

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".md") or file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

                # Markdown links
                for text, url in md_link_pattern.findall(content):
                    output.append([file, text.strip(), url.strip()])

                # HTML links
                for url, text in html_link_pattern.findall(content):
                    output.append([file, text.strip(), url.strip()])

# Write to CSV
with open("all_links.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["file", "text", "url"])
    writer.writerows(output)

print("Done! Links saved to all_links.csv")



▶️ 2. Run it
From your repo folder:
python3 extract_links.py


This generates:
all_links.csv


You can open it in Excel, Numbers, Google Sheets, or convert it to Markdown.

📄 3. What the output looks like
Example:
|  |  |  | 
|  |  |  | 
|  |  |  | 
|  |  |  | 


This gives you a complete inventory of every link across your site.

⭐ Why this is the best option for you
- Zero manual scanning
- Works across all posts, pages, includes, layouts
- Lets you quickly identify duplicates, broken links, or missing references
- Perfect for building your _data/links.yml later if you want global link management
- Repeatable anytime you add more content

If you want, I can also:
- Add detection for image links
- Output a Markdown table instead of CSV
- Automatically generate a _data/links.yml from the results
- Add deduplication so each URL appears only once
Just tell me how far you want to take this.
