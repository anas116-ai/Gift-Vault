with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
start = text.find('id="modal-create-event"')
if start != -1:
    end = text.find('</form>', start)
    print(text[start-20:end+20])
else:
    print("modal-create-event not found")
