import re

with open('web_preview/mobile.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('IDs in mobile.html:', [m for m in re.findall(r'id="([^"]+)"', text)])
