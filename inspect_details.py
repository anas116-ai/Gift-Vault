with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for tab in ['tab-expenses', 'tab-reciprocity', 'tab-reports', 'tab-settings']:
    m = re.search(r'id=["\']' + tab + r'["\'](.*?)(?=(id=["\']tab-|<div id=["\']modal|</main>))', text, re.DOTALL)
    if m:
        print(f"================ {tab} ================")
        print(m.group(1))
