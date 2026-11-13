import re

target_h1 = '''<h1 class="hero-massive-heading hero-heading" style="font-family: 'Branch', 'Bosch', serif !important; font-size: clamp(38px, 4.6vw, 58px); font-weight: 700; color: #37000A; line-height: 1.1; letter-spacing: -0.02em; margin: 0 0 18px; text-transform: none;">
            Every Gift.<br/>
            Every Occasion.<br/>
<span style="color: #FF1F3D;">All in One Place.</span>
</h1>'''

replacement_h1 = '''<h1 class="hero-massive-heading hero-heading" style="font-family: 'Branch', serif !important; font-size: clamp(38px, 4.6vw, 58px); font-weight: 700; color: #37000A; line-height: 1.1; letter-spacing: -0.02em; margin: 0 0 18px; text-transform: none;">
            Every Gift<span style="font-family: 'Bosch', sans-serif; color: #FF1F3D;">.</span><br/>
            Every Occasion<span style="font-family: 'Bosch', sans-serif; color: #FF1F3D;">.</span><br/>
            <span style="color: #FF1F3D;">All in One Place<span style="font-family: 'Bosch', sans-serif; color: #37000A;">.</span></span>
</h1>'''

for path in ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target_h1 in content:
        content = content.replace(target_h1, replacement_h1)
        print(f"Replaced in {path}")
    else:
        # regex fallback
        content = re.sub(
            r'<h1 class="hero-massive-heading hero-heading"[^>]*>.*?</h1>',
            replacement_h1,
            content,
            flags=re.DOTALL
        )
        print(f"Regex replaced in {path}")
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
