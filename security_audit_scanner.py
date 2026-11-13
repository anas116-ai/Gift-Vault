with open(r'c:\Project\Gift Valut\web_preview\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

print("=== CODE SECURITY SCAN ===")

# 1. Check for innerHTML
inner_matches = [m.start() for m in re.finditer(r'\.innerHTML\s*=', text)]
print(f"Total innerHTML assignments: {len(inner_matches)}")

# 2. Check for escapeHtml function
if 'function escapeHtml' in text:
    print("✅ escapeHtml function exists!")
else:
    print("⚠️ escapeHtml function MISSING!")

# 3. Check for target="_blank" without noopener
raw_blank = re.findall(r'target=["\']_blank["\'](?!.*?rel=["\']noopener)', text)
print(f"target='_blank' potential misses: {len(raw_blank)}")

# 4. Check for eval, document.write
if 'eval(' in text:
    print("⚠️ eval() found!")
else:
    print("✅ Zero eval() found.")

if 'document.write' in text:
    print("⚠️ document.write found!")
else:
    print("✅ Zero document.write found.")

# 5. Check Meta tags (CSP, X-Content-Type-Options, etc.)
meta_csp = '<meta http-equiv="Content-Security-Policy"' in text
print(f"CSP meta tag present: {meta_csp}")

meta_referrer = '<meta name="referrer"' in text
print(f"Referrer policy present: {meta_referrer}")
