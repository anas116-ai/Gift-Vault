import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<main id="view-login".*?</main>', content, re.DOTALL)
if m:
    with open('current_view_login.html', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
    print("Wrote current_view_login.html, length:", len(m.group(0)))
