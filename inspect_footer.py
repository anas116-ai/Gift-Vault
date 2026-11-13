with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('footer-master')
if pos != -1:
    print(text[pos-50:pos+2500])
else:
    pos2 = text.find('<footer')
    if pos2 != -1:
        print(text[pos2:pos2+2500])
    else:
        print("No footer found")
