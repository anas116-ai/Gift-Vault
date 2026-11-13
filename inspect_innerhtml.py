with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '.innerHTML' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")
