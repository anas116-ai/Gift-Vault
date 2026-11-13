with open('index.html', encoding='utf-8') as f:
    c = f.read()

s = c.find('class="login-edge-right"')
e = c.find('</main>', s)
print(c[s:e])
