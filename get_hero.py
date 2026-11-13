with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
hero_match = re.search(r'<section id="hero-section".*?</section>', text, re.DOTALL)
if hero_match:
    print(hero_match.group(0))
