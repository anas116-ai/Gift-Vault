with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function handleCreateEventSubmit')
if idx != -1:
    print('Found JS definition of handleCreateEventSubmit:')
    print(text[idx:idx+1200])
else:
    print('JS function handleCreateEventSubmit NOT FOUND!')
