import re
import urllib.request

with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

urls = re.findall(r'src="([^"]+)"', text)
print(f"Total src attributes found: {len(urls)}")
for u in urls:
    if u.startswith('http'):
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, timeout=5)
            print(f"HTTP {res.status} OK: {u[:80]}")
        except Exception as e:
            print(f"ERROR on {u}: {e}")
    else:
        print(f"Local/Data URI: {u[:50]}")
