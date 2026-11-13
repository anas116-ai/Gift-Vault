import json

with open('threeui_tactile-button.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("data type:", type(data))
for k, v in data.items():
    if isinstance(v, list):
        print(f"Key {k} (list len {len(v)}):", [list(item.keys()) if isinstance(item, dict) else item for item in v[:3]])
    elif isinstance(v, dict):
        print(f"Key {k} (dict keys):", list(v.keys()))
    else:
        print(f"Key {k}:", str(v)[:100])
