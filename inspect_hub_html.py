with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
hub_start = text.find('id="view-hub"')
hub_end = text.find('</main>', hub_start)
print(text[hub_start:hub_start+1500])
