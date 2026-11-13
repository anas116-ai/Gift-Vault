with open('web_preview/index.html', encoding='utf-8') as f:
    text = f.read()
import re
for m in re.finditer(r'id=["\']modal-[a-zA-Z0-9_\-]+["\']', text):
    line_no = text[:m.start()].count('\n') + 1
    print(f'Line {line_no}: {m.group(0)}')
