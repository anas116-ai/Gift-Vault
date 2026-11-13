import os
import re
from PIL import Image, ImageEnhance, ImageFilter

# =========================================================================
# 1. PROCESS 4K CRISP MASTER IMAGE (ZERO BLURRINESS)
# =========================================================================
src_ai_16k = r'C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\luxury_indian_wedding_giftvault_reception_1794493761850.jpg'
if os.path.exists(src_ai_16k):
    im = Image.open(src_ai_16k)
    # Upscale to crisp 2752 x 1536
    im_scaled = im.resize((2752, 1536), Image.Resampling.LANCZOS)
    im_sharp = im_scaled.filter(ImageFilter.UnsharpMask(radius=2.0, percent=130, threshold=2))
    im_contrasted = ImageEnhance.Contrast(im_sharp).enhance(1.05)
    im_vibrant = ImageEnhance.Color(im_contrasted).enhance(1.04)

    target_dirs = [
        'assets/images',
        'web_preview/assets/images',
        'build/web/assets/images',
        'web/assets/images'
    ]
    for td in target_dirs:
        os.makedirs(td, exist_ok=True)
        im_vibrant.save(os.path.join(td, 'giftvault_login_showcase_final.jpg'), 'JPEG', quality=96, subsampling=0)
        im_vibrant.save(os.path.join(td, 'giftvault_showcase_16k_master.jpg'), 'JPEG', quality=96, subsampling=0)
    print('Generated 4K master images across all directories (Zero Blurriness)')

# =========================================================================
# 2. UPDATE app.js TO NEVER HIDE SIGN IN ON LANDING PAGE
# =========================================================================
app_js_files = ['assets/js/app.js', 'web_preview/assets/js/app.js', 'build/web/assets/js/app.js', 'web/assets/js/app.js']
for aj in app_js_files:
    if not os.path.exists(aj):
        continue
    with open(aj, 'r', encoding='utf-8') as f:
        js = f.read()

    # In checkAuthSession: always ensure signinBtn is visible on landing
    old_code = "if (signinBtn) signinBtn.style.display = 'none';"
    new_code = "// Keep Sign In button always visible on landing navbar per user direction\n        if (signinBtn) signinBtn.style.display = 'inline-flex';\n        if (badge) badge.style.display = 'none';"
    if old_code in js:
        js = js.replace(old_code, new_code)
        with open(aj, 'w', encoding='utf-8') as f:
            f.write(js)
        print('Updated checkAuthSession in:', aj)

# =========================================================================
# 3. UPDATE layout.css STYLES
# =========================================================================
with open('assets/css/layout.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .btn-enter-vault to be compact and centered
css = re.sub(
    r'\.btn-enter-vault\s*\{[^}]*\}',
    '''.btn-enter-vault {
  width: 100%;
  max-width: 250px;
  height: 42px !important;
  background: #8A1526 !important;
  color: #FFFFFF !important;
  border-radius: 999px !important;
  font-family: 'Cinzel', 'Playfair Display', Georgia, serif !important;
  font-size: 14px !important;
  font-weight: 700 !important;
  letter-spacing: 0.03em !important;
  border: none !important;
  cursor: pointer !important;
  box-shadow: none !important;
  margin: 18px auto 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: background-color 0.15s ease !important;
}
.btn-enter-vault:hover {
  background: #730F1E !important;
  box-shadow: none !important;
}
.btn-enter-vault:active {
  background: #5E0C18 !important;
  box-shadow: none !important;
}''',
    css
)

# Add .login-cream-topbar & .login-cream-back-btn
cream_back_css = '''
.login-cream-topbar {
  width: 100%;
  max-width: 380px;
  margin-bottom: 14px;
  display: flex;
  justify-content: flex-start;
}
.login-cream-back-btn {
  background: #FFFFFF;
  border: 1px solid rgba(220, 212, 198, 0.95);
  color: #8A1526;
  padding: 6px 14px;
  border-radius: 999px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
  transition: all 0.15s ease;
}
.login-cream-back-btn:hover {
  background: #FFF5F6;
  border-color: #8A1526;
  transform: translateX(-2px);
}
'''
if '.login-cream-topbar' not in css:
    css += '\n' + cream_back_css

# Save layout.css across directories
css_dirs = ['assets/css', 'web_preview/assets/css', 'build/web/assets/css', 'web/assets/css']
for cd in css_dirs:
    os.makedirs(cd, exist_ok=True)
    with open(os.path.join(cd, 'layout.css'), 'w', encoding='utf-8') as f:
        f.write(css)
print('Updated layout.css in all directories')

# =========================================================================
# 4. UPDATE HTML FILES (index.html and replicas)
# =========================================================================
html_files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for fn in html_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    # A. Hero Buttons: Replace "Sign In to Family Vault" with clean "Sign In" and "Explore Demo"
    hero_pattern = re.compile(
        r'<div class="threeui-tactile-wrapper">\s*<button type="button" class="threeui-tactile-btn"[^>]*>.*?Sign In to Family Vault.*?</div>\s*<button type="button" class="btn-secondary"[^>]*>.*?Explore Live Demo.*?</span>\s*<svg[^>]*>.*?</svg>\s*</button>',
        re.DOTALL
    )
    new_hero_buttons = '''<div class="hero-actions-container" style="display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 32px; align-items: center;">
            <button type="button" id="btn-hero-signin" class="btn-tactile-primary" style="height: 46px; padding: 0 26px; border-radius: 999px; font-weight: 700; font-size: 15px; border: none; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; box-shadow: none;" onclick="navToView('login')">
              <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Sign In</span>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            <button type="button" class="btn-hero-demo" style="height: 46px; padding: 0 22px; font-size: 14px; font-weight: 700; border-radius: 999px; background: #FFFFFF; border: 1.5px solid rgba(138, 21, 38, 0.25); color: #8A1526; display: inline-flex; align-items: center; gap: 8px; cursor: pointer; box-shadow: none; transition: all 0.2s ease;" onclick="openHeroDemo()">
              <span>Explore Demo</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            </button>
          </div>'''
    html = hero_pattern.sub(new_hero_buttons, html)

    # B. Pricing Section: Sculpted luxury cards with compact Activate buttons
    # Replace giant button in Plan 1
    html = re.sub(
        r'<div class="threeui-tactile-wrapper" style="width: 100%;">\s*<button type="button" class="threeui-tactile-btn" style="padding: 13px;" onclick="openEventWorkspace\(\'event-wedding\'\)">\s*<span>Activate Single Event \(₹49\)</span>.*?</div>',
        '''<div style="display: flex; justify-content: center; width: 100%;">
                <button type="button" class="btn-tactile-primary btn-pricing-activate" style="height: 42px; max-width: 230px; width: 100%; border-radius: 999px; font-size: 13.5px; font-weight: 700; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;" onclick="openEventWorkspace('event-wedding')">
                  <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Activate Single Event (₹49)</span>
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </button>
              </div>''',
        html,
        flags=re.DOTALL
    )

    # Replace giant button in Plan 2
    html = re.sub(
        r'<div class="threeui-tactile-wrapper" style="width: 100%;">\s*<button type="button" class="threeui-tactile-btn" style="padding: 13px;" onclick="openPricingModal\(\)">\s*<span>Get Royal Family Pass \(₹99\)</span>.*?</div>',
        '''<div style="display: flex; justify-content: center; width: 100%;">
                <button type="button" class="btn-tactile-primary btn-pricing-activate" style="height: 42px; max-width: 230px; width: 100%; border-radius: 999px; font-size: 13.5px; font-weight: 700; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px;" onclick="openPricingModal()">
                  <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Get Family Pass (₹99)</span>
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </button>
              </div>''',
        html,
        flags=re.DOTALL
    )

    # C. Login Page: Remove Back button from the left image side!
    html = re.sub(
        r'<!-- Top Left Back Button -->\s*<div class="login-edge-topbar">.*?</div>',
        '',
        html,
        flags=re.DOTALL
    )

    # D. Login Page: Place Back button on the RIGHT side (cream background) above the card
    if '<div class="login-cream-topbar">' not in html:
        html = html.replace(
            '<div class="login-edge-right">',
            '''<div class="login-edge-right">
        <!-- Back Button on Cream Background per User Request -->
        <div class="login-cream-topbar">
          <button type="button" class="login-cream-back-btn" onclick="navToView('landing')">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            <span>Back to Celebrations</span>
          </button>
        </div>'''
        )

    # E. Login Page Button: Make sure text is in a styled span so letters are 100% visible
    html = re.sub(
        r'<button type="submit" class="btn-enter-vault">\s*Enter Family Vault\s*</button>',
        '''<button type="submit" class="btn-enter-vault">
              <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important; font-family: 'Cinzel', serif; font-size: 14px; font-weight: 700; letter-spacing: 0.03em; text-shadow: 0 1px 2px rgba(0,0,0,0.6); pointer-events: none;">Enter Family Vault</span>
            </button>''',
        html
    )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated HTML in:', fn)

print('All requested user updates applied successfully!')
