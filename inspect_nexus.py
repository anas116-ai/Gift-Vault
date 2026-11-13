with open('extracted_nexus-tactile.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of nexus-tactile.html:", len(text))
import re
styles = re.findall(r'<style[^>]*>.*?</style>', text, re.DOTALL)
for s in styles:
    print("STYLE SNIPPET:\n", s[:1500])
    print('---')
buttons = re.findall(r'<button[^>]*>.*?</button>', text, re.DOTALL)
for b in buttons:
    print("BUTTON SNIPPET:\n", b)
