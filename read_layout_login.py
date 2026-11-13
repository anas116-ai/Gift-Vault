with open('assets/css/layout.css', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('#view-login')
if pos != -1:
    print(text[pos:pos+2500])
