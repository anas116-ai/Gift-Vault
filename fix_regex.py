import re

with open('apply_full_creative_master.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace(
    'view_landing_pattern = re.compile(r\'<main id="view-landing".*?</main>\', re.DOTALL)',
    'view_landing_pattern = re.compile(r\'<main[^>]*id="view-landing".*?</main>\', re.DOTALL)'
)

with open('apply_full_creative_master.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated regex in apply_full_creative_master.py")
