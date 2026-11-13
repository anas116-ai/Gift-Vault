with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'function [a-zA-Z0-9_]*Event[a-zA-Z0-9_]*\([^\)]*\)', text)
print('Event functions:', matches)

idx = text.find('handleCreateEventSubmit')
if idx != -1:
    print('Found handleCreateEventSubmit:')
    print(text[idx:idx+1000])
else:
    print('handleCreateEventSubmit NOT FOUND!')
