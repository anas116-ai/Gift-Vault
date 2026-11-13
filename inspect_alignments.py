with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for sec in ['hero-section', 'features-section', 'comparison-section', 'faq-section']:
    m = re.search(r'<section[^>]*id=["\']' + sec + r'["\'][^>]*>(.*?)</section>', text, re.DOTALL)
    if m:
        c = m.group(1).strip()
        print(f"=== {sec} (len {len(c)}) ===")
        lines = [l.strip() for l in c.split('\n') if l.strip()]
        for l in lines[:10]:
            print("  ", l[:110])
