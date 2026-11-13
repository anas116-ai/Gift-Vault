with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'let [a-zA-Z0-9_]+|const [a-zA-Z0-9_]+', text)
print("Variables in script (first 30):")
print(matches[10:40])

idx = text.find('const INITIAL_LEDGER')
if idx == -1:
    idx = text.find('SAMPLE_LEDGER')
if idx == -1:
    idx = text.find('currentTotalBlessings')

if idx != -1:
    print("\nState block preview:")
    print(text[idx-50:idx+600])
