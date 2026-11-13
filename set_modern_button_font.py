import os
import re

css_targets = [
    'assets/css/layout.css',
    'web_preview/assets/css/layout.css',
    'build/web/assets/css/layout.css',
    'web/assets/css/layout.css'
]

modern_button_css = """
/* UNIVERSAL MODERN BUTTON TYPOGRAPHY & FLUIDIC SIZING (Outfit / Plus Jakarta Sans) */
.btn-tactile-primary,
.threeui-tactile-btn,
.btn-nav-signin,
#btn-header-signin,
#btn-hero-signin,
.btn-hero-demo,
.btn-enter-vault,
.btn-pricing-activate {
  height: 32px !important;
  min-height: 32px !important;
  max-height: 32px !important;
  line-height: 32px !important;
  padding: 0 16px !important;
  font-family: 'Outfit', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  letter-spacing: 0.01em !important;
  text-transform: none !important;
  border-radius: 7px !important;
  border: none !important;
  background: #8A1526 !important;
  color: #FFFFFF !important;
  cursor: pointer !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 7px !important;
  box-shadow: none !important;
  margin: 0 !important;
}
"""

for t in css_targets:
    if os.path.exists(t):
        with open(t, 'r', encoding='utf-8') as f:
            content = f.read()
        # Append clean universal rule
        content = content.rstrip() + "\n" + modern_button_css + "\n"
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {t}")
