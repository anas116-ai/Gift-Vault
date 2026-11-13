import os
import re

fontshare_link = '<link href="https://api.fontshare.com/v2/css?f[]=clash-display@700,600,500&f[]=satoshi@700,500,400&display=swap" rel="stylesheet">'

html_targets = [
    'index.html',
    'web_preview/index.html',
    'build/web/index.html',
    'web/index.html'
]

for t in html_targets:
    if not os.path.exists(t):
        continue
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Fontshare link in <head> if not present
    if 'clash-display' not in content:
        content = content.replace('</head>', f'  {fontshare_link}\n</head>')

    # 2. Update Hero Heading font-family to 'Clash Display', 'Outfit'
    content = re.sub(
        r"font-family:\s*['\x22]Outfit['\x22],\s*['\x22]Plus Jakarta Sans['\x22][^;!]*!important;",
        "font-family: 'Clash Display', 'Outfit', sans-serif !important;",
        content
    )

    # 3. Update Hero Subtext font-family to 'Satoshi', 'Plus Jakarta Sans'
    content = re.sub(
        r"font-family:\s*['\x22]Plus Jakarta Sans['\x22],\s*['\x22]Inter['\x22][^;!]*!important;",
        "font-family: 'Satoshi', 'Plus Jakarta Sans', sans-serif !important;",
        content
    )

    # 4. Update Button font-family to 'Clash Display' or 'Satoshi'
    content = re.sub(
        r"font-family:\s*['\x22]Outfit['\x22],\s*['\x22]Plus Jakarta Sans['\x22][^;!]*!important;",
        "font-family: 'Satoshi', 'Outfit', sans-serif !important;",
        content
    )

    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated HTML with Awwwards fonts: {t}")

# Update CSS targets as well
css_targets = [
    'assets/css/layout.css',
    'web_preview/assets/css/layout.css',
    'build/web/assets/css/layout.css',
    'web/assets/css/layout.css'
]

awwwards_css_rule = """
/* ==========================================================================
   AWWWARDS PREMIER TYPOGRAPHY SYSTEM (Clash Display + Satoshi)
   ========================================================================== */
.hero-massive-heading,
.hero-heading {
  font-family: 'Clash Display', 'Outfit', sans-serif !important;
  letter-spacing: -0.03em !important;
  font-weight: 700 !important;
}

#hero-subtext,
.hero-ref1-features-strip div div:last-child {
  font-family: 'Satoshi', 'Plus Jakarta Sans', sans-serif !important;
  letter-spacing: -0.01em !important;
}

.btn-tactile-primary,
.threeui-tactile-btn,
.btn-nav-signin,
#btn-header-signin,
#btn-hero-signin,
.btn-hero-demo,
.btn-enter-vault,
.btn-pricing-activate {
  font-family: 'Satoshi', 'Outfit', -apple-system, sans-serif !important;
  font-weight: 700 !important;
}
"""

for c in css_targets:
    if os.path.exists(c):
        with open(c, 'a', encoding='utf-8') as f:
            f.write("\n" + awwwards_css_rule + "\n")
        print(f"Appended Awwwards CSS to {c}")
