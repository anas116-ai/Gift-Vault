with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('navTo(')
if pos != -1:
    print(text[pos-50:pos+800])
