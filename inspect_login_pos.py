with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="view-login"')
if pos != -1:
    print("Found view-login at pos:", pos)
    print(text[pos-20:pos+300])
