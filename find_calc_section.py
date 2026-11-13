with open('web_preview/index.html', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'id=["\']calculator-section["\']', text)
if m:
    idx = m.start()
    line_no = text[:idx].count('\n') + 1
    print(f'calculator-section at line {line_no}')
    print(text[idx-100:idx+300])
else:
    print('calculator-section NOT FOUND')
