with open('index.html', encoding='utf-8') as f:
    c = f.read()

import re
s_hero = c.find('id="hero"')
if s_hero == -1: s_hero = c.find('hero-cinematic')
e_hero = c.find('</section>', s_hero)
hero_txt = c[s_hero:e_hero]

print('Length of hero section:', len(hero_txt))
for line in hero_txt.split('\n'):
    line_lower = line.lower()
    if any(k in line_lower for k in ['coin', 'lucky', 'diya', 'lamp', 'flame', '+1', '₹1', 'badge', 'floating']):
        print('FOUND:', line.strip())
