with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'function navToView', text)]
for pos in matches:
    print(text[pos:pos+400])
    print('---')
