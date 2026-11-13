import re

css_fix = """
/* DISABLE RED PSEUDO-ELEMENTS TO ALLOW PURE LEMON GREEN (#9EE425) WITH MAROON TEXT */
.btn-tactile-primary::before,
.btn-enter-vault::before,
#btn-header-signin::before,
#btn-hero-signin::before,
.btn-tactile-primary::after,
.btn-enter-vault::after {
  display: none !important;
  content: none !important;
  opacity: 0 !important;
}

.btn-tactile-primary,
.btn-enter-vault,
#btn-header-signin,
#btn-hero-signin,
.btn-card-action {
  background: #9EE425 !important;
  background-color: #9EE425 !important;
  background-image: none !important;
  color: #37000A !important;
  border: 1.5px solid #37000A !important;
  border-radius: 999px !important;
  font-family: 'Sen', sans-serif !important;
  font-weight: 700 !important;
  box-shadow: 0 4px 14px rgba(158, 228, 37, 0.45) !important;
}

.btn-tactile-primary span,
.btn-enter-vault span,
#btn-header-signin span,
#btn-hero-signin span,
.btn-tactile-label {
  color: #37000A !important;
  font-family: 'Sen', sans-serif !important;
  font-weight: 700 !important;
}

.btn-tactile-primary svg,
.btn-enter-vault svg,
#btn-header-signin svg,
#btn-hero-signin svg {
  stroke: #37000A !important;
  color: #37000A !important;
}
"""

css_files = [
    'assets/css/layout.css',
    'web_preview/assets/css/layout.css',
    'build/web/assets/css/layout.css',
    'web/assets/css/layout.css'
]

for p in css_files:
    with open(p, 'a', encoding='utf-8') as f:
        f.write(css_fix)
    print(f"Appended button fix to {p}")

# Also update HTML titles to ensure crisp white text in dark cards and login scene
html_files = [
    'index.html',
    'web_preview/index.html',
    'build/web/index.html',
    'web/index.html'
]

for hp in html_files:
    with open(hp, 'r', encoding='utf-8') as f:
        html = f.read()

    # Fix Card 1, 2, 3 titles
    html = html.replace(
        '<h2 style="font-family: \'Sen\', sans-serif !important; font-size: 26px; font-weight: 700 !important; color: #FFFFFF; margin: 0 0 18px; line-height: 1.2;">Track Gifts & Shagun</h2>',
        '<div style="font-family: \'Sen\', sans-serif; font-size: 26px; font-weight: 700; color: #FFFFFF !important; margin: 0 0 18px; line-height: 1.2;">Track Gifts & Shagun</div>'
    )
    html = html.replace(
        '<h2 style="font-family: \'Sen\', sans-serif !important; font-size: 26px; font-weight: 700 !important; color: #FFFFFF; margin: 0 0 18px; line-height: 1.2;">Family Celebrations</h2>',
        '<div style="font-family: \'Sen\', sans-serif; font-size: 26px; font-weight: 700; color: #FFFFFF !important; margin: 0 0 18px; line-height: 1.2;">Family Celebrations</div>'
    )
    html = html.replace(
        '<h2 style="font-family: \'Sen\', sans-serif !important; font-size: 26px; font-weight: 700 !important; color: #FFFFFF; margin: 0 0 18px; line-height: 1.2;">Instant Slips & Reports</h2>',
        '<div style="font-family: \'Sen\', sans-serif; font-size: 26px; font-weight: 700; color: #FFFFFF !important; margin: 0 0 18px; line-height: 1.2;">Instant Slips & Reports</div>'
    )

    # Fix Login Left column title
    html = html.replace(
        '<h2 style="font-family: \'Sen\', sans-serif !important; font-size: 32px; font-weight: 700 !important; color: #FFFFFF; line-height: 1.25; margin: 0 0 12px;">\n            Because every gift<br>has a story.\n          </h2>',
        '<div style="font-family: \'Sen\', sans-serif; font-size: 32px; font-weight: 700; color: #FFFFFF !important; line-height: 1.25; margin: 0 0 12px; text-shadow: 0 2px 10px rgba(0,0,0,0.6);">Because every gift<br>has a story.</div>'
    )

    # Navbar sign in button styling
    html = re.sub(
        r'<button class="btn-tactile-primary" id="btn-header-signin"[^>]*>',
        '<button class="btn-tactile-primary" id="btn-header-signin" onclick="navToView(\'login\')" type="button" style="background: #9EE425 !important; color: #37000A !important; border: 1.5px solid #37000A !important; border-radius: 999px !important; font-family: \'Sen\', sans-serif !important; font-weight: 700 !important; height: 36px !important; padding: 0 18px !important; display: inline-flex !important; align-items: center !important; gap: 6px !important; box-shadow: 0 3px 12px rgba(158,228,37,0.4) !important;">',
        html
    )

    with open(hp, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {hp}")

print("Polish perfection completed!")
