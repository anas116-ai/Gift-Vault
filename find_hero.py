with open('index.html', encoding='utf-8') as f:
    c = f.read()

s = c.find('Family Vault')
while s != -1:
    print('Found at', s)
    print(c[s-100:s+200])
    print('='*50)
    s = c.find('Family Vault', s+100)
