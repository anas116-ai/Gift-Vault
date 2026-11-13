with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        l = line.strip()
        if 'id="pane-' in l:
            print(f'{i}: {l[:100]}')
        if 'class="ws-tab-btn' in l:
            print(f'{i}: {l[:100]}')
        if 'id="view-' in l:
            print(f'{i}: {l[:100]}')
