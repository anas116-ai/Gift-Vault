with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function handleMunshiSubmit')
print('Index:', idx)
print(text[idx:idx+300])
