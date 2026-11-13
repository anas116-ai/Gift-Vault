with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Print lines with section tags or major containers
for idx, line in enumerate(lines):
    if '<section' in line or '<nav' in line or 'id="view-' in line or 'class="hero' in line or 'class="feature' in line:
        print(f"L{idx+1}: {line.strip()[:100]}")
