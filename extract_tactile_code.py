import json, os

with open('threeui_tactile-button.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for f in data.get('files', []):
    path = f.get('path', '')
    code = f.get('code', '')
    print(f"Path: {path}, bytes: {len(code)}")
    basename = os.path.basename(path)
    with open('extracted_' + basename, 'w', encoding='utf-8') as out:
        out.write(code)
    print(f"Saved extracted_{basename}")
