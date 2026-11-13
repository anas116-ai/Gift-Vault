import re

with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

card_matches = re.findall(r'class="([^"]*card[^"]*)"', c)
print("Unique card classes found:")
for cm in sorted(set(card_matches)):
    print(" -", cm)

# Let's inspect snippet of features
feat_idx = c.find('id="features"')
if feat_idx != -1:
    print("\n--- Features snippet ---")
    print(c[feat_idx:feat_idx+1200])

# Let's inspect snippet of celebrations
cult_idx = c.find('id="culture"')
if cult_idx != -1:
    print("\n--- Culture snippet ---")
    print(c[cult_idx:cult_idx+1200])
