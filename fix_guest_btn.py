with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('onclick="enterGuestDemo()"', 'onclick="enterGuestDemoMode()"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

import shutil
for t in ['web_preview/index.html', 'build/web/index.html', 'web/index.html']:
    shutil.copyfile('index.html', t)
    print(f"Synced to {t}")
