import os, re

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.js') or f.endswith('.html'):
            p = os.path.join(root, f)
            try:
                content = open(p, encoding='utf-8').read()
                if 'navToView' in content:
                    m = re.search(r'function\s+navToView[^{]*\{[^}]*\}', content)
                    if m:
                        print(f"In {p}: {m.group(0)}")
            except Exception:
                pass
