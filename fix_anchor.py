# -*- coding: utf-8 -*-
paths = [
    r"c:\Project\Gift Valut\web_preview\index.html",
    r"c:\Project\Gift Valut\build\web\index.html",
    r"c:\Project\Gift Valut\web\index.html"
]

for p in paths:
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    c = c.replace('<a href="#" onclick="showMasterView(\'landing\')"', '<button type="button" onclick="showMasterView(\'landing\')"')
    c = c.replace('← తిరిగి హోమ్ పేజీకి వెళ్లండి</a>', '← తిరిగి హోమ్ పేజీకి వెళ్లండి</button>')
    with open(p, "w", encoding="utf-8") as f:
        f.write(c)

print("Fixed anchor to button cleanly.")
