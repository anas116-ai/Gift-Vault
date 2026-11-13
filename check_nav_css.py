with open('assets/css/layout.css', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('header-glass')
if pos != -1:
    print(text[pos-50:pos+800])
else:
    print("header-glass not found in layout.css")
