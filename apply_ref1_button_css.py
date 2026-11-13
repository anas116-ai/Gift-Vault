import os

css_targets = [
    'assets/css/layout.css',
    'web_preview/assets/css/layout.css',
    'build/web/assets/css/layout.css',
    'web/assets/css/layout.css'
]

override_css = """
/* ==========================================================================
   REFERENCE 1 DESIGN BUTTON STYLES (WARM HONEY-GOLD PILL & CREAM SECONDARY)
   ========================================================================== */
#btn-hero-signin,
.btn-ref1-primary {
  height: 38px !important;
  min-height: 38px !important;
  max-height: 38px !important;
  line-height: 38px !important;
  padding: 0 22px !important;
  font-size: 13.5px !important;
  font-weight: 600 !important;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  text-transform: none !important;
  letter-spacing: normal !important;
  border-radius: 999px !important;
  border: none !important;
  background: linear-gradient(135deg, #C28B38 0%, #A66E22 100%) !important;
  color: #FFFFFF !important;
  box-shadow: 0 4px 14px rgba(160, 110, 30, 0.28) !important;
  cursor: pointer !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  margin: 0 !important;
}

#btn-hero-signin:hover,
.btn-ref1-primary:hover {
  background: linear-gradient(135deg, #CF9743 0%, #B2782A 100%) !important;
  box-shadow: 0 6px 18px rgba(160, 110, 30, 0.38) !important;
  transform: translateY(-2px) !important;
}

.btn-hero-demo,
.btn-ref1-secondary {
  height: 38px !important;
  min-height: 38px !important;
  max-height: 38px !important;
  line-height: 38px !important;
  padding: 0 18px !important;
  font-size: 13.5px !important;
  font-weight: 600 !important;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
  text-transform: none !important;
  letter-spacing: normal !important;
  border-radius: 999px !important;
  border: 1.5px solid #E2D5C8 !important;
  background: #FFF9F2 !important;
  color: #2C2520 !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03) !important;
  cursor: pointer !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  margin: 0 !important;
}

.btn-hero-demo:hover,
.btn-ref1-secondary:hover {
  border-color: #C28B38 !important;
  background: #FFF3E6 !important;
  transform: translateY(-2px) !important;
}
"""

for target in css_targets:
    if os.path.exists(target):
        with open(target, 'a', encoding='utf-8') as f:
            f.write("\n" + override_css + "\n")
        print(f"Appended Reference 1 button CSS to {target}")
