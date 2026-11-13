with open('assets/css/layout.css', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'login', text, re.IGNORECASE)]
print("Total matches of 'login' in layout.css:", len(matches))
if matches:
    pos = matches[0]
    print("Around first match:\n", text[max(0, pos-100):pos+400])
