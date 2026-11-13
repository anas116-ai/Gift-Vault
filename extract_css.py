with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
css_start = text.find('<style>') + len('<style>')
css_end = text.find('</style>')
css = text[css_start:css_end]

print("Total CSS lines:", len(css.splitlines()))

# Print all selectors
selectors = re.findall(r'([^{]+)\{', css)
print("Total CSS rules:", len(selectors))
for s in selectors[:25]:
    print("Rule:", s.strip())
