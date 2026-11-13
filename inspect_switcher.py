with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
func_match = re.search(r'function switchHeroCore\(.*?\n\s*\}', text, re.DOTALL)
if func_match:
    print(func_match.group(0))
else:
    print("switchHeroCore not found!")
