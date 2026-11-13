with open('assets/js/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('navToView')
if pos != -1:
    print("Found navToView in app.js:")
    print(text[pos:pos+600])
else:
    print("Not in app.js")
