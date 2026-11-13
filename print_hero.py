with open('index.html', encoding='utf-8') as f:
    c = f.read()

s = c.find('id="hero"')
if s == -1: s = c.find('hero-cinematic')
e = c.find('</section>', s)
print(c[s:e+10])
