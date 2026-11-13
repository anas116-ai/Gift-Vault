with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Check table alignment
print("--- TABLE HEADERS ---")
ths = re.findall(r'<th[^>]*>(.*?)</th>', text)
for t in ths:
    print("TH:", t.strip())

# Check media queries content
print("\n--- MEDIA QUERIES ---")
mqs = re.findall(r'@media\s*\([^)]+\)\s*\{([^}]+(?:\{[^}]+\}[^}]+)*)\}', text)
for i, mq in enumerate(mqs):
    print(f"MQ {i}: length {len(mq)}")
    print(mq[:400])

# Check floating back
print("\n--- FLOATING BACK ---")
fb = re.search(r'\.app-floating-back[^{]*\{[^}]+\}', text)
if fb:
    print(fb.group(0))

# Check munshi grid
print("\n--- MUNSHI ENTRY ---")
mg = re.search(r'\.munshi-entry-card[^{]*\{[^}]+\}', text)
if mg:
    print(mg.group(0))
