import os
import re

# 1. DEFINE @font-face FOR THE 3 AWWWARDS FONTS
awwwards_font_face_css = """
/* ==========================================================================
   AWWWARDS TRIO @font-face DEFINITIONS
   ========================================================================== */
@font-face {
  font-family: 'Branch';
  src: url('../fonts/Branch.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Bosch';
  src: url('../fonts/Bosch.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'Absans';
  src: url('../fonts/Absans-Regular.woff2') format('woff2'),
       url('../fonts/Absans-Regular.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
  font-display: swap;
}

/* ==========================================================================
   PALETTE VARIABLES (Strict 5-Color System per User Reference)
   #FF1F3D (Strawberry Red), #3E4E50 (Iron Grey), #F2EFEA (Parchment),
   #37000A (Rich Mahogany), #9EE425 (Slime Lime)
   ========================================================================== */
:root {
  --c-strawberry: #FF1F3D;
  --c-iron-grey: #3E4E50;
  --c-parchment: #F2EFEA;
  --c-mahogany: #37000A;
  --c-lime: #9EE425;

  --bg-primary: #F2EFEA;
  --text-primary: #37000A;
  --text-secondary: #3E4E50;
  --c-primary: #FF1F3D;
  --c-accent: #9EE425;
}

body {
  background-color: #F2EFEA !important;
  color: #37000A !important;
  font-family: 'Satoshi', 'Plus Jakarta Sans', sans-serif;
}

/* UNIVERSAL EQUAL MEDIUM-LENGTH BUTTON SYSTEM */
.btn-tactile-primary,
.threeui-tactile-btn,
.btn-nav-signin,
#btn-header-signin,
#btn-hero-signin,
.btn-hero-demo,
.btn-enter-vault,
.btn-pricing-activate {
  height: 34px !important;
  min-height: 34px !important;
  max-height: 34px !important;
  line-height: 34px !important;
  width: 140px !important;
  min-width: 140px !important;
  max-width: 140px !important;
  padding: 0 12px !important;
  font-family: 'Absans', 'Satoshi', sans-serif !important;
  font-size: 12.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.02em !important;
  text-transform: none !important;
  border-radius: 7px !important;
  border: none !important;
  background: #FF1F3D !important;
  color: #FFFFFF !important;
  cursor: pointer !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 6px !important;
  box-shadow: 0 4px 14px rgba(255, 31, 61, 0.25) !important;
  margin: 0 !important;
  transition: transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease !important;
  white-space: nowrap !important;
  overflow: hidden !important;
}

.btn-tactile-primary:hover,
#btn-header-signin:hover,
#btn-hero-signin:hover,
.btn-hero-demo:hover,
.btn-enter-vault:hover {
  background: #E01330 !important;
  box-shadow: 0 6px 18px rgba(255, 31, 61, 0.35) !important;
  transform: translateY(-2px) !important;
}

/* Secondary Button Variant with Same Medium Length */
.btn-hero-demo {
  background: #37000A !important;
  color: #F2EFEA !important;
  box-shadow: 0 4px 14px rgba(55, 0, 10, 0.2) !important;
}

.btn-hero-demo:hover {
  background: #4E0B16 !important;
  box-shadow: 0 6px 18px rgba(55, 0, 10, 0.3) !important;
}

/* STRICT VIEW ISOLATION: LOGIN IS HIDDEN WHEN NOT ACTIVE */
#view-login {
  display: none !important;
}

#view-login.active {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: 100vw !important;
  height: 100vh !important;
  min-height: 100vh !important;
  max-height: 100vh !important;
  background: #F2EFEA !important;
  z-index: 99999 !important;
  overflow-y: auto !important;
  padding: 24px 20px !important;
  box-sizing: border-box !important;
}

/* SECTION HEADERS TYPOGRAPHY: Bosch Display */
h2, .section-title, #features h2, #culture h2, #pricing h2, #how-it-works h2, #faq h2 {
  font-family: 'Bosch', 'Branch', serif !important;
  color: #37000A !important;
}
"""

css_targets = [
    'assets/css/layout.css',
    'web_preview/assets/css/layout.css',
    'build/web/assets/css/layout.css',
    'web/assets/css/layout.css'
]

for c in css_targets:
    if os.path.exists(c):
        with open(c, 'a', encoding='utf-8') as f:
            f.write("\n" + awwwards_font_face_css + "\n")
        print(f"Appended master CSS to {c}")

print("Master CSS updated successfully!")
