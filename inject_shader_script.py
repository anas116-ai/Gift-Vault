files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'shader-buttons.js' not in c:
        target = '<script src="assets/js/app.js"></script>'
        replacement = '<script src="assets/js/app.js"></script>\n  <script src="assets/js/shader-buttons.js"></script>'
        c = c.replace(target, replacement)
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
        print('Injected into:', fn)
    else:
        print('Already in:', fn)
