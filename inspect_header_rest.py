with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
header_match = re.search(r'<header[^>]*>.*?</header>', text, re.DOTALL)
if header_match:
    print(header_match.group(0)[1500:])
