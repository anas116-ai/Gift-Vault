import json

with open('threeui_tactile-button.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Keys:", data.keys())
if 'files' in data:
    print("Files:", [f.get('name') or f.get('path') for f in data['files']])
    for f in data['files']:
        name = f.get('name') or f.get('path') or ''
        print(f"\n--- {name} ---")
        content = f.get('content', '')
        print(content[:600])
