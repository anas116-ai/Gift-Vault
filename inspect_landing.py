with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
hero_match = re.search(r'<section class="hero-wrap">.*?</section>', text, re.DOTALL)
if hero_match:
    print("HERO SECTION (first 800 chars):")
    print(hero_match.group(0)[:800])
    print("...")

celeb_match = re.search(r'<section id="celebrations-sec".*?</section>', text, re.DOTALL)
if celeb_match:
    print("\nCELEBRATIONS SECTION (first 800 chars):")
    print(celeb_match.group(0)[:800])
    print("...")
