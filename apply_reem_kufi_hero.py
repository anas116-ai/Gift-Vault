import re
import os

css_files = [
    'assets/css/layout.css',
    'web_preview/assets/css/layout.css',
    'build/web/assets/css/layout.css',
    'web/assets/css/layout.css'
]

html_files = [
    'index.html',
    'web_preview/index.html',
    'build/web/index.html',
    'web/index.html'
]

# 1. Update CSS
reem_font_face = """
@font-face {
  font-family: 'Reem Kufi Fun';
  src: url('../fonts/ReemKufiFun-Regular.ttf') format('truetype');
  font-weight: 400 700;
  font-style: normal;
  font-display: swap;
}
"""

hero_font_override = """
/* HERO SECTION SPECIFIC FONT: REEM KUFI FUN */
.hero-heading,
.hero-massive-heading,
section.hero-cinematic-grid h1,
.hero-cinematic-grid .hero-heading {
  font-family: 'Reem Kufi Fun', cursive, sans-serif !important;
  font-weight: 500 !important;
  letter-spacing: -0.01em !important;
  line-height: 1.18 !important;
}
"""

for cpath in css_files:
    if os.path.exists(cpath):
        with open(cpath, 'r', encoding='utf-8') as f:
            css = f.read()

        if "@font-face {\n  font-family: 'Reem Kufi Fun';" not in css:
            css = reem_font_face + css

        if "/* HERO SECTION SPECIFIC FONT: REEM KUFI FUN */" not in css:
            css += "\n" + hero_font_override
        else:
            css = re.sub(r'/\* HERO SECTION SPECIFIC FONT: REEM KUFI FUN \*/.*?line-height: 1.18 !important;\n\}', hero_font_override.strip(), css, flags=re.DOTALL)

        with open(cpath, 'w', encoding='utf-8') as f:
            f.write(css)
        print(f"Updated CSS: {cpath}")

# 2. Update HTML
google_font_link = '<link href="https://fonts.googleapis.com/css2?family=Reem+Kufi+Fun:wght@400;500;600;700&display=swap" rel="stylesheet">'

new_hero_h1 = '''<h1 class="hero-massive-heading hero-heading" style="font-family: 'Reem Kufi Fun', cursive, sans-serif !important; font-size: clamp(38px, 4.6vw, 56px); font-weight: 500 !important; color: #37000A; line-height: 1.18; letter-spacing: -0.01em; margin: 0 0 18px; text-transform: none;">
            Every Gift.<br/>
            Every Occasion.<br/>
            <span style="color: #FF1F3D;">All in One Place.</span>
          </h1>'''

for hpath in html_files:
    if os.path.exists(hpath):
        with open(hpath, 'r', encoding='utf-8') as f:
            html = f.read()

        if 'family=Reem+Kufi+Fun' not in html:
            html = html.replace('</head>', f'  {google_font_link}\n</head>')

        html = re.sub(
            r'<h1 class="hero-massive-heading hero-heading"[^>]*>.*?</h1>',
            new_hero_h1,
            html,
            flags=re.DOTALL
        )

        with open(hpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated HTML: {hpath}")

print("Applied Reem Kufi Fun only to hero section!")
