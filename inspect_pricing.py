with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="pricing"')
print(c[idx:idx+1500])
