import re

for css_file in ['assets/css/layout.css', 'assets/css/landing-sections.css', 'assets/css/components.css']:
    try:
        content = open(css_file, encoding='utf-8').read()
        matches = re.findall(r'(\.footer-master[^{]*\{[^}]*\})', content)
        if matches:
            print(f"In {css_file}:")
            for m in matches:
                print(" ", m)
    except Exception as e:
        pass
