target_files = [
    r'c:\Project\Gift Valut\web_preview\index.html',
    r'c:\Project\Gift Valut\web_preview\desktop.html',
    r'c:\Project\Gift Valut\web_preview\mobile.html',
    r'c:\Project\Gift Valut\build\web\index.html',
    r'c:\Project\Gift Valut\web\index.html'
]

csp_tags = '''  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' 'unsafe-inline' https: data: blob:; img-src 'self' https: data: blob:; font-src 'self' https://fonts.gstatic.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;">'''

for p in target_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'http-equiv="Content-Security-Policy"' not in c:
        c = c.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">', '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + csp_tags)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Added CSP to {p}")

print("Done!")
