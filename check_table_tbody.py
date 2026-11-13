with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="ledger-tbody"')
if idx != -1:
    print('Found ledger-tbody:')
    print(text[idx-50:idx+800])
else:
    print('ledger-tbody not found')

idx2 = text.find('id="recent-tbody"')
if idx2 != -1:
    print('\nFound recent-tbody:')
    print(text[idx2-50:idx2+400])
