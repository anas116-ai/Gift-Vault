with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'<div class="hero-grid">(.*?)<!-- END HERO GRID -->', text, re.DOTALL)
if not m:
    m = re.search(r'<div class="hero-grid">(.*?)</section>', text, re.DOTALL)

if m:
    print(m.group(1)[1200:])
