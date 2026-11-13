with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
root_match = re.search(r':root\s*\{([^}]+)\}', text)
if root_match:
    print("CSS Variables:")
    for line in root_match.group(1).strip().split('\n'):
        if line.strip():
            print("  ", line.strip())

# Check how often each palette hex code appears in text:
palette = ['CAFF0A', 'F8333C', '036D19', '000411', 'DCE2CC', 'E5D0D5', 'A7D2B7', '8E99CC']
print("\nColor occurrence counts in HTML/CSS:")
for p in palette:
    count_upper = text.count(f"#{p}")
    count_lower = text.count(f"#{p.lower()}")
    print(f"#{p}: {count_upper + count_lower} times")
