with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
feat_match = re.search(r'<section id="features-sec".*?</section>', text, re.DOTALL)
if feat_match:
    print(feat_match.group(0)[:1500])
