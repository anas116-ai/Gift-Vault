import os

files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']
for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('src="assets/images/giftvault_login_showcase_final.jpg"', 'src="assets/images/giftvault_showcase_16k_master.jpg"')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated image src in:', fn)
