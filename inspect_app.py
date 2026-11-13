import re

with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Views found:', re.findall(r'id="view-[^"]+"', text))
print('Sections found:', re.findall(r'<section[^>]*id="([^"]+)"', text))
