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
sen_font_face = """
@font-face {
  font-family: 'Sen';
  src: url('../fonts/Sen-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: 'Sen';
  src: url('../fonts/Sen-Medium.ttf') format('truetype');
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}
"""

sen_header_css = """
/* UNIVERSAL SEN REGULAR 400 HEADERS SYSTEM */
h1, h2, h3, h4,
.hero-heading,
.hero-massive-heading,
.section-title-large,
.section-title,
.nav-brand-title,
.login-hero-headline,
.features-section h2,
.culture-section h2,
.timeline-section h2,
.pricing-section h2,
.faq-section h2,
.etale-calc-title,
.hub-title,
.ws-event-title-h1,
.culture-title,
.card-culture-title {
  font-family: 'Sen', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-weight: 400 !important;
  letter-spacing: -0.01em !important;
}
"""

for cpath in css_files:
    if os.path.exists(cpath):
        with open(cpath, 'r', encoding='utf-8') as f:
            css = f.read()
        
        # Insert font face if not present
        if "@font-face {\n  font-family: 'Sen';" not in css:
            css = sen_font_face + css
        
        # Add universal sen header rule
        if "/* UNIVERSAL SEN REGULAR 400 HEADERS SYSTEM */" not in css:
            css += "\n" + sen_header_css
        else:
            css = re.sub(r'/\* UNIVERSAL SEN REGULAR 400 HEADERS SYSTEM \*/.*?letter-spacing: -0.01em !important;\n\}', sen_header_css.strip(), css, flags=re.DOTALL)
            
        with open(cpath, 'w', encoding='utf-8') as f:
            f.write(css)
        print(f"Updated CSS: {cpath}")

# 2. Update HTML files
google_font_link = '<link href="https://fonts.googleapis.com/css2?family=Sen:wght@400;500;600;700;800&display=swap" rel="stylesheet">'

for hpath in html_files:
    if os.path.exists(hpath):
        with open(hpath, 'r', encoding='utf-8') as f:
            html = f.read()

        # Add Google Font link if not present
        if 'family=Sen' not in html:
            html = html.replace('</head>', f'  {google_font_link}\n</head>')

        # Update Navbar Brand Title
        html = re.sub(
            r'<div class="nav-brand-title"[^>]*>.*?</div>',
            r'<div class="nav-brand-title" style="font-family: \'Sen\', sans-serif !important; font-size: 22px; font-weight: 400 !important; color: #37000A; letter-spacing: -0.01em;">Gift<span style="color: #FF1F3D;">Vault</span></div>',
            html,
            count=1
        )

        # Update Hero Massive Heading
        new_hero_h1 = '''<h1 class="hero-massive-heading hero-heading" style="font-family: 'Sen', sans-serif !important; font-size: clamp(38px, 4.6vw, 56px); font-weight: 400 !important; color: #37000A; line-height: 1.15; letter-spacing: -0.01em; margin: 0 0 18px; text-transform: none;">
            Every Gift.<br/>
            Every Occasion.<br/>
            <span style="color: #FF1F3D;">All in One Place.</span>
          </h1>'''
        html = re.sub(
            r'<h1 class="hero-massive-heading hero-heading"[^>]*>.*?</h1>',
            new_hero_h1,
            html,
            flags=re.DOTALL
        )

        # Update Section Titles
        # Features title
        html = re.sub(
            r'<h2 class="section-title-large"[^>]*>(.*?)</h2>',
            r'<h2 class="section-title-large" style="font-family: \'Sen\', sans-serif !important; font-weight: 400 !important; font-size: clamp(28px, 3.2vw, 42px); color: #37000A; letter-spacing: -0.01em; text-align: center; margin-bottom: 14px;">\1</h2>',
            html
        )

        # Replace any remaining inline 'Branch' or 'Bosch' in headings
        html = html.replace("font-family: 'Branch', serif;", "font-family: 'Sen', sans-serif !important; font-weight: 400 !important;")
        html = html.replace("font-family: 'Branch',", "font-family: 'Sen',")
        html = html.replace("font-family: 'Bosch',", "font-family: 'Sen',")
        html = html.replace("font-family: 'Bosch'", "font-family: 'Sen'")

        with open(hpath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated HTML: {hpath}")

print("Applied Sen Regular 400 to complete headers across all files!")
