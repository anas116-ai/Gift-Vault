import shutil
import re

with open('assets/js/shader-buttons.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace any guard that skips btn-hero-signin or btn-ref1-primary
code = re.sub(r'if \(!btn \|\| btn\.id === [^;]+;', 'if (!btn) return;', code)

with open('assets/js/shader-buttons.js', 'w', encoding='utf-8') as f:
    f.write(code)

for dst in ['web_preview/assets/js/shader-buttons.js', 'build/web/assets/js/shader-buttons.js', 'web/assets/js/shader-buttons.js']:
    shutil.copyfile('assets/js/shader-buttons.js', dst)
    print(f'Synchronized {dst}')
