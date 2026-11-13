with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Smart Tools for Every Celebration')
if pos != -1:
    print(text[pos-200:pos+2500])
else:
    print("Not found by title")
