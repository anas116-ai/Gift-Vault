import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<main id="view-login".*?</main>', content, re.DOTALL)
if m:
    print("Found view-login, span:", m.span())
    print("First 400 chars:\n", m.group(0)[:400])
else:
    print("Not found")
