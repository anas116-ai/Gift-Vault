with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('function handleMunshiSubmit(e) {')
idx2 = text.find('function testSoundboxAnnouncement(', idx1)

print(f"idx1: {idx1}, idx2: {idx2}")
print("Between idx1 and idx2 length:", idx2 - idx1)
print(text[idx1:idx1+200])
print("...")
print(text[idx2-100:idx2])
