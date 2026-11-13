import json

with open('threeui_tactile-button.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for f in data.get('files', []):
    name = f.get('name') or f.get('path') or ''
    content = f.get('content', '')
    print(f"File: {name}, length: {len(content)}")
    if 'nexus-tactile.html' in name or 'threeui.css' in name:
        with open('extracted_' + os.path.basename(name), 'w', encoding='utf-8') as out:
            out.write(content)
        print(f"Wrote extracted_{os.path.basename(name)}")
