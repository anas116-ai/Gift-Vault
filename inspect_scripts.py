with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script[^>]*>.*?</script>', text, re.DOTALL)
print(f"Total script tags: {len(scripts)}")
for s in scripts:
    src_match = re.search(r'src=["\']([^"\']+)["\']', s)
    if src_match:
        print("Script src:", src_match.group(1))
    else:
        print("Inline script snippet:", s[:150].replace('\n', ' '))
