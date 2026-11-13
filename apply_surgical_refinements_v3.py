import os
import re

# =========================================================================
# 1. UPDATE layout.css
# =========================================================================
with open('assets/css/layout.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Universal button system: 7px rounded corners (rectangular box with slightly rounded 4 corners)
# ZERO bottom shade, compact proportions
v3_button_css = '''
/* =========================================================================
   UNIVERSAL RECTANGULAR BUTTON SYSTEM (7px Rounded Corners - Zero Bottom Shade)
   ========================================================================= */
.btn-tactile-primary,
.btn-hero-signin,
.btn-hero-demo,
.btn-enter-vault,
.btn-pricing-activate,
.btn-primary,
.btn-secondary,
.btn-cream-back-btn,
.login-cream-back-btn,
.threeui-tactile-btn {
  border-radius: 7px !important;
  box-shadow: none !important;
  text-shadow: none !important;
}

/* Navbar Centering & Sleek 32px Compact Sign-in */
.nav-container-luxury {
  height: 60px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
}

.nav-right-actions {
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  margin: 0 !important;
  padding: 0 !important;
  height: 100% !important;
}

#btn-header-signin.btn-tactile-primary {
  height: 32px !important;
  padding: 0 14px !important;
  font-size: 12.5px !important;
  font-weight: 700 !important;
  border-radius: 7px !important;
  margin: 0 !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 6px !important;
  box-shadow: none !important;
}

/* Hero Section Actions - Strictly Side-by-Side */
.hero-actions-container {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  gap: 12px !important;
  flex-wrap: nowrap !important;
  margin-bottom: 28px !important;
}

#btn-hero-signin {
  height: 38px !important;
  padding: 0 18px !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  border-radius: 7px !important;
  box-shadow: none !important;
  white-space: nowrap !important;
}

.btn-hero-demo {
  height: 38px !important;
  padding: 0 18px !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  border-radius: 7px !important;
  box-shadow: none !important;
  white-space: nowrap !important;
  border: 1.5px solid rgba(138, 21, 38, 0.25) !important;
  color: #8A1526 !important;
  background: #FFFFFF !important;
  cursor: pointer !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  transition: all 0.2s ease !important;
}
.btn-hero-demo:hover {
  background: #FFF5F6 !important;
  border-color: #8A1526 !important;
}

/* Right Side Login Card - Generous Height & Perfect Hierarchy */
.login-edge-right {
  position: relative !important;
  width: 100% !important;
  height: 100vh !important;
  background: #FAF7F2 !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  align-items: center !important;
  padding: 24px 32px !important;
  overflow-y: auto !important;
  overflow-x: hidden !important;
}

.exact-auth-card-edge {
  width: 100% !important;
  max-width: 420px !important;
  min-height: 520px !important;
  background: #FAF7F2 !important;
  border: 1.5px solid rgba(220, 212, 198, 0.9) !important;
  border-radius: 20px !important;
  padding: 42px 36px 34px !important;
  box-shadow: 0 20px 45px -12px rgba(0, 0, 0, 0.06) !important;
  position: relative !important;
  margin: 0 !important;
}

.brand-lockup {
  margin-bottom: 26px !important;
  text-align: center !important;
}

.form-field-group {
  margin-bottom: 18px !important;
  text-align: left !important;
}

.field-label {
  display: block !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  color: #1F2937 !important;
  margin-bottom: 7px !important;
  text-align: left !important;
}

.phone-input-container {
  height: 46px !important;
  border: 1.5px solid #CBD5E1 !important;
  border-radius: 7px !important;
  background: #FFFFFF !important;
}

.otp-boxes-row {
  display: flex !important;
  gap: 8px !important;
  justify-content: space-between !important;
}

.otp-box {
  width: 44px !important;
  height: 46px !important;
  border: 1.5px solid #CBD5E1 !important;
  border-radius: 7px !important;
  text-align: center !important;
  font-size: 18px !important;
  font-weight: 700 !important;
  background: #FFFFFF !important;
}

.btn-enter-vault {
  width: 100% !important;
  max-width: 220px !important;
  height: 40px !important;
  background: #8A1526 !important;
  color: #FFFFFF !important;
  border-radius: 7px !important;
  font-family: 'Cinzel', 'Playfair Display', Georgia, serif !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.03em !important;
  border: none !important;
  cursor: pointer !important;
  box-shadow: none !important;
  margin: 20px auto 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.login-cream-topbar {
  width: 100% !important;
  max-width: 420px !important;
  margin-bottom: 14px !important;
  display: flex !important;
  justify-content: flex-start !important;
}

.login-cream-back-btn {
  background: #FFFFFF !important;
  border: 1px solid rgba(220, 212, 198, 0.95) !important;
  color: #8A1526 !important;
  padding: 6px 14px !important;
  border-radius: 7px !important;
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 12.5px !important;
  font-weight: 600 !important;
  cursor: pointer !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  box-shadow: none !important;
}
'''

# Remove any previous UNIVERSAL RECTANGULAR BUTTON SYSTEM block
s = css.find('/* =========================================================================\n   UNIVERSAL RECTANGULAR BUTTON SYSTEM')
if s != -1:
    css = css[:s]
s2 = css.find('/* UNIVERSAL RECTANGULAR BUTTON SYSTEM')
if s2 != -1:
    css = css[:s2]

css += '\n\n' + v3_button_css

for cd in ['assets/css', 'web_preview/assets/css', 'build/web/assets/css', 'web/assets/css']:
    os.makedirs(cd, exist_ok=True)
    with open(os.path.join(cd, 'layout.css'), 'w', encoding='utf-8') as f:
        f.write(css)

print('Updated layout.css with v3 specifications')

# =========================================================================
# 2. UPDATE HTML FILES (index.html and replicas)
# =========================================================================
html_files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for fn in html_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    # A. Hero Buttons: Strictly side-by-side, compact width, 7px radius
    hero_pattern = re.compile(
        r'<div class="hero-actions-container"[^>]*>.*?</div>\s*</div>',
        re.DOTALL
    )
    new_hero_html = '''<div class="hero-actions-container" style="display: flex; flex-direction: row; align-items: center; gap: 12px; flex-wrap: nowrap; margin-bottom: 28px;">
            <button type="button" id="btn-hero-signin" class="btn-tactile-primary" style="height: 38px; padding: 0 18px; border-radius: 7px !important; font-weight: 700; font-size: 13px; border: none; cursor: pointer; display: inline-flex; align-items: center; gap: 6px; box-shadow: none; white-space: nowrap;" onclick="navToView('login')">
              <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Sign In</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            <button type="button" class="btn-hero-demo" style="height: 38px; padding: 0 18px; font-size: 13px; font-weight: 700; border-radius: 7px !important; background: #FFFFFF; border: 1.5px solid rgba(138, 21, 38, 0.25); color: #8A1526; display: inline-flex; align-items: center; gap: 6px; cursor: pointer; box-shadow: none; transition: all 0.2s ease; white-space: nowrap;" onclick="openHeroDemo()">
              <span>Explore Demo</span>
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            </button>
          </div>
        </div>'''
    html = hero_pattern.sub(new_hero_html, html)

    # B. Hero Image Card: Ensure aspect-ratio and clean 3D container
    html = re.sub(
        r'<img src="assets/images/giftvault_flagship_hero[^"]*" alt="GiftVault Vertical 3D Product Showcase"[^>]*>',
        '<img src="assets/images/giftvault_flagship_hero_vertical.jpg" alt="GiftVault 3D Hardware Showcase" style="width: 100%; height: auto; display: block; object-fit: cover; aspect-ratio: 3/4;" loading="eager">',
        html
    )

    # C. Login Page Right Side: Topbar & Card Height & Alignment
    cream_topbar_html = '''<div class="login-cream-topbar" style="width: 100%; max-width: 420px; margin-bottom: 14px; display: flex; justify-content: flex-start;">
          <button type="button" class="login-cream-back-btn" onclick="navToView('landing')" style="border-radius: 7px !important; padding: 6px 14px; font-size: 12.5px; font-weight: 600; background: #FFFFFF; border: 1px solid rgba(220, 212, 198, 0.95); color: #8A1526; display: inline-flex; align-items: center; gap: 6px; cursor: pointer; box-shadow: none;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            <span>Back to Celebrations</span>
          </button>
        </div>'''
    html = re.sub(
        r'<div class="login-cream-topbar".*?</div>\s*</div>',
        cream_topbar_html,
        html,
        flags=re.DOTALL
    )

    # D. Login Button in Card: Compact, 7px radius, visible text
    card_btn_html = '''<button type="submit" class="btn-enter-vault" style="height: 40px !important; max-width: 220px !important; border-radius: 7px !important; margin: 20px auto 0 !important; box-shadow: none !important;">
              <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important; font-family: 'Cinzel', serif; font-size: 13.5px; font-weight: 700; letter-spacing: 0.03em; pointer-events: none;">Enter Family Vault</span>
            </button>'''
    html = re.sub(
        r'<button type="submit" class="btn-enter-vault"[^>]*>.*?</button>',
        card_btn_html,
        html,
        flags=re.DOTALL
    )

    # E. Left Panel: Ensure image is giftvault_login_showcase_final.jpg and NO text overlay
    html = re.sub(
        r'<img src="[^"]*" alt="GiftVault Wedding Table Scene" class="login-edge-photo">',
        '<img src="assets/images/giftvault_login_showcase_final.jpg" alt="GiftVault Royal Palace Banquet Reception" class="login-edge-photo">',
        html
    )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated HTML in:', fn)

print('Surgical refinements applied to all files!')
