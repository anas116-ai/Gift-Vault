with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<section' in l and i < 300:
        print(f"Line {i}: {l.strip()}")
