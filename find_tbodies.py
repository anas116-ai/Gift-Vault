with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
tbodies = re.findall(r'<tbody[^>]*>', text)
print("Found tbodies:", tbodies)
tables = re.findall(r'<table[^>]*>', text)
print("Found tables:", tables)
