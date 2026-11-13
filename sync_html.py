import shutil

targets = ['web_preview/index.html', 'build/web/index.html', 'web/index.html']
for t in targets:
    shutil.copyfile('index.html', t)
    print(f"Copied index.html to {t}")
