with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'navToView', text)]
print("Total occurrences of navToView in index.html:", len(matches))
for pos in matches[:8]:
    line_start = text.rfind('\n', 0, pos)
    line_end = text.find('\n', pos)
    print(text[line_start:line_end].strip())
