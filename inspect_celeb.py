with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
celeb_match = re.search(r'<section id="celebrations-sec".*?</section>', text, re.DOTALL)
if celeb_match:
    print(celeb_match.group(0))
