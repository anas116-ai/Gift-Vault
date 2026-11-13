with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
elements = [
    'ws-tabs-bar',
    'mode-selector-grid',
    'quick-amounts-grid',
    'ledger-table',
    'modal-backdrop',
    'modal-card',
    'modal-dialog',
    'events-cards-grid',
    'showcase-card'
]

for el in elements:
    m = re.search(r'\.' + el + r'[^{]*\{[^}]+\}', text)
    if m:
        print(f"=== {el} ===")
        print(m.group(0))
    else:
        print(f"⚠️ {el} NOT FOUND in CSS")
