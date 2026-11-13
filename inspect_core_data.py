with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
core_match = re.search(r'const CORE_CELEBRATIONS\s*=\s*\{.*?\};', text, re.DOTALL)
if core_match:
    print(core_match.group(0))
