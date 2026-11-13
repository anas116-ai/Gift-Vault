with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
tabs = ['tab-overview', 'tab-entry', 'tab-ledger', 'tab-expenses', 'tab-reciprocity', 'tab-soundbox', 'tab-reports', 'tab-settings']
for tab in tabs:
    m = re.search(r'id=["\']' + tab + r'["\'](.*?)(?=(id=["\']tab-|<div id=["\']modal|</main>))', text, re.DOTALL)
    if m:
        content = m.group(1)
        print(f"=== {tab} ===")
        print(f"Length: {len(content)} chars")
        # print first 500 chars
        print(content[:300].strip())
