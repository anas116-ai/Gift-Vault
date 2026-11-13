with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
header_match = re.search(r'<header class="header-glass no-print">.*?</header>', text, re.DOTALL)
if header_match:
    print(header_match.group(0))
