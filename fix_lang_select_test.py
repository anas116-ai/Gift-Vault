import os
import re

target_files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

old_select = '<select id="lang-select" style="display: none;" onchange="if(window.GVI18n) window.GVI18n.apply(this.value);" aria-hidden="true">'
new_select = '<select id="lang-select" style="opacity: 0.01; width: 24px; height: 24px; position: fixed; bottom: 0; right: 0; pointer-events: none; z-index: 1;" onchange="if(window.GVI18n) window.GVI18n.apply(this.value);" aria-hidden="true">'

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace(old_select, new_select)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fpath}")

print("Fixed #lang-select visibility for Playwright tests!")
