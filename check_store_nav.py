with open('assets/js/core/store.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('navToView')
if pos != -1:
    print("Found navToView in store.js:")
    print(text[pos:pos+500])
else:
    print("Not in store.js")
