with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        l = line.strip()
        if 'id=' in l and 'modal' in l.lower():
            print(f'{i}: {l[:110]}')
        elif 'function open' in l or 'function switch' in l or 'function show' in l:
            print(f'{i}: {l[:110]}')
