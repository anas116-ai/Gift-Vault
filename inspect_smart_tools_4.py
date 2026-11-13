with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Smart Tools for Every Celebration')
if pos != -1:
    print(text[pos+4000:pos+6500])
