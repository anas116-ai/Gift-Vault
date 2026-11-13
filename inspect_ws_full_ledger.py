with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="ws-full-ledger-body"')
if idx != -1:
    print(text[idx-50:idx+1200])
