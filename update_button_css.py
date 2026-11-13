import re

# 1. Update layout.css with master button styling (Lemon Green #9EE425 with Maroon #37000A text)
button_css = """
/* ==========================================================================
   MASTER BUTTON SYSTEM: LEMON GREEN (#9EE425) & MAROON (#37000A)
   ========================================================================== */
.btn-tactile-primary,
.btn-enter-vault,
.btn-nav-primary,
.btn-hero-primary,
#btn-header-signin,
#btn-hero-signin,
.btn-card-action {
  background: #9EE425 !important;
  color: #37000A !important;
  border: 1.5px solid #37000A !important;
  border-radius: 999px !important;
  font-family: 'Sen', -apple-system, sans-serif !important;
  font-weight: 700 !important;
  font-size: 13.5px !important;
  height: 38px !important;
  min-height: 38px !important;
  max-width: 175px !important;
  padding: 0 20px !important;
  box-shadow: 0 4px 14px rgba(158, 228, 37, 0.4) !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  cursor: pointer !important;
  transition: all 0.25s ease !important;
  text-decoration: none !important;
}

.btn-tactile-primary:hover,
.btn-enter-vault:hover,
.btn-nav-primary:hover,
.btn-hero-primary:hover,
#btn-header-signin:hover,
#btn-hero-signin:hover,
.btn-card-action:hover {
  transform: translateY(-2px) scale(1.02) !important;
  background: #A8F02E !important;
  box-shadow: 0 6px 20px rgba(158, 228, 37, 0.55) !important;
}

.btn-tactile-primary:active,
.btn-enter-vault:active,
#btn-header-signin:active,
#btn-hero-signin:active {
  transform: translateY(0) scale(0.98) !important;
}

.btn-tactile-label,
.btn-tactile-primary span,
.btn-enter-vault span {
  color: #37000A !important;
  font-family: 'Sen', -apple-system, sans-serif !important;
  font-weight: 700 !important;
}

.btn-tactile-primary svg,
.btn-enter-vault svg {
  stroke: #37000A !important;
  color: #37000A !important;
}
"""

css_paths = [
    'assets/css/layout.css',
    'web_preview/assets/css/layout.css',
    'build/web/assets/css/layout.css',
    'web/assets/css/layout.css'
]

for p in css_paths:
    with open(p, 'a', encoding='utf-8') as f:
        f.write(button_css)
    print(f"Appended button CSS to {p}")

print("CSS update completed successfully!")
