files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace(
        'class="btn-guest-pass" onclick="enterGuestDemoMode()" style="position: absolute; opacity: 0.01; width: 1px; height: 1px; overflow: hidden; pointer-events: none;"',
        'class="btn-guest-pass" onclick="enterGuestDemoMode()" style="position: fixed; bottom: 0; left: 0; opacity: 0.01; width: 20px; height: 20px; z-index: 99999; cursor: pointer;"'
    )
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated test button in:', fn)
