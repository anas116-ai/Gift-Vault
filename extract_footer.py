import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<footer class="footer-master.*?</footer\s*>', content, re.DOTALL)
if m:
    print("Found footer, length:", len(m.group(0)))
    with open('current_footer.html', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
else:
    print("Footer not found")
