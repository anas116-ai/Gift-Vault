import os
import re

# =========================================================================
# 1. UPDATE layout.css
# =========================================================================
with open('assets/css/layout.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Universal button shape: Rectangular with slightly rounded 4 corners (border-radius: 8px)
# and ZERO bottom shade (box-shadow: none)
universal_btn_override = '''
/* UNIVERSAL RECTANGULAR BUTTON SYSTEM - 4 ROUNDED CORNERS (border-radius: 8px) */
.btn-tactile-primary,
.btn-hero-signin,
.btn-hero-demo,
.btn-enter-vault,
.btn-pricing-activate,
.btn-primary,
.btn-cream-back-btn,
.login-cream-back-btn,
.threeui-tactile-btn {
  border-radius: 8px !important;
  box-shadow: none !important;
  text-shadow: none !important;
}

/* Navbar Centering & Compact Sign-in */
.nav-container-luxury {
  height: 64px !important;
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
}

#btn-header-signin.btn-tactile-primary {
  height: 36px !important;
  padding: 0 16px !important;
  font-size: 13px !important;
  font-weight: 700 !important;
  border-radius: 8px !important;
  margin: 0 !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 6px !important;
  box-shadow: none !important;
}

/* Compact Login Button with 4 Rounded Corners & Clear Text */
.btn-enter-vault {
  width: 100% !important;
  max-width: 210px !important;
  height: 38px !important;
  background: #8A1526 !important;
  color: #FFFFFF !important;
  border-radius: 8px !important;
  font-family: 'Cinzel', 'Playfair Display', Georgia, serif !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  letter-spacing: 0.03em !important;
  border: none !important;
  cursor: pointer !important;
  box-shadow: none !important;
  margin: 16px auto 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: background-color 0.15s ease !important;
}
.btn-enter-vault:hover {
  background: #730F1E !important;
  box-shadow: none !important;
}

/* Back button on cream background */
.login-cream-topbar {
  width: 100%;
  max-width: 380px;
  margin-bottom: 12px;
  display: flex;
  justify-content: flex-start;
}
.login-cream-back-btn {
  background: #FFFFFF;
  border: 1px solid rgba(220, 212, 198, 0.9);
  color: #8A1526;
  padding: 6px 14px;
  border-radius: 8px !important;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  box-shadow: none !important;
  transition: all 0.15s ease;
}
.login-cream-back-btn:hover {
  background: #FFF5F6;
  border-color: #8A1526;
}
'''

if 'UNIVERSAL RECTANGULAR BUTTON SYSTEM' not in css:
    css += '\n\n' + universal_btn_override
else:
    # Replace existing override
    s = css.find('/* UNIVERSAL RECTANGULAR BUTTON SYSTEM')
    css = css[:s] + universal_btn_override

# Write css to all targets
for cd in ['assets/css', 'web_preview/assets/css', 'build/web/assets/css', 'web/assets/css']:
    os.makedirs(cd, exist_ok=True)
    with open(os.path.join(cd, 'layout.css'), 'w', encoding='utf-8') as f:
        f.write(css)

print('Updated layout.css with universal 8px rounded rectangular buttons across all directories')

# =========================================================================
# 2. UPDATE HTML FILES (index.html, web_preview, build, web)
# =========================================================================
html_files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for fn in html_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    # -------------------------------------------------------------
    # A. HERO BUTTONS: Matching compact rectangular buttons with 8px rounded corners
    # -------------------------------------------------------------
    hero_pattern = re.compile(
        r'<div class="hero-actions-container".*?</div>\s*</div>',
        re.DOTALL
    )
    # Check if hero-actions exists
    hero_replacement = '''<div class="hero-actions-container" style="display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 28px; align-items: center;">
            <button type="button" id="btn-hero-signin" class="btn-tactile-primary" style="height: 40px; padding: 0 20px; border-radius: 8px !important; font-weight: 700; font-size: 13.5px; border: none; cursor: pointer; display: inline-flex; align-items: center; gap: 7px; box-shadow: none;" onclick="navToView('login')">
              <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Sign In</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            <button type="button" class="btn-hero-demo" style="height: 40px; padding: 0 18px; font-size: 13.5px; font-weight: 700; border-radius: 8px !important; background: #FFFFFF; border: 1.5px solid rgba(138, 21, 38, 0.25); color: #8A1526; display: inline-flex; align-items: center; gap: 7px; cursor: pointer; box-shadow: none; transition: all 0.2s ease;" onclick="openHeroDemo()">
              <span>Explore Demo</span>
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            </button>
          </div>'''
    
    # Try replacing hero-actions-container
    if 'class="hero-actions-container"' in html:
        html = re.sub(r'<div class="hero-actions-container"[^>]*>.*?</div>\s*</div>', hero_replacement + '\n        </div>', html, count=1, flags=re.DOTALL)

    # -------------------------------------------------------------
    # B. PRICING CARDS & BUTTONS: 8px rounded corners, compact, NO extra wrapper box in 99
    # -------------------------------------------------------------
    # Plan 1 (49)
    html = re.sub(
        r'<div style="display: flex; justify-content: center; width: 100%;">\s*<button type="button" class="btn-tactile-primary btn-pricing-activate"[^>]*>.*?</button>\s*</div>',
        '''<div style="display: flex; justify-content: center; width: 100%;">
                <button type="button" class="btn-tactile-primary btn-pricing-activate" style="height: 38px; max-width: 190px; width: 100%; border-radius: 8px !important; font-size: 13px; font-weight: 700; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 6px; box-shadow: none;" onclick="openEventWorkspace('event-wedding')">
                  <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Activate Event (₹49)</span>
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </button>
              </div>''',
        html,
        flags=re.DOTALL
    )

    # Plan 2 (99) - eliminate threeui-tactile-wrapper or separate button container
    html = re.sub(
        r'<div class="threeui-tactile-wrapper"[^>]*>.*?Get Royal Family Pass.*?</div>\s*</div>',
        '''<div style="display: flex; justify-content: center; width: 100%;">
                <button type="button" class="btn-tactile-primary btn-pricing-activate" style="height: 38px; max-width: 190px; width: 100%; border-radius: 8px !important; font-size: 13px; font-weight: 700; border: none; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 6px; box-shadow: none;" onclick="openPricingModal()">
                  <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Get Family Pass (₹99)</span>
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </button>
              </div>\n            </div>''',
        html,
        flags=re.DOTALL
    )

    # -------------------------------------------------------------
    # C. FOOTER: REMOVE "FAMILY ACCESS" & BOTH BUTTONS, REMOVE ALL TELUGU TEXT
    # -------------------------------------------------------------
    # Clean 3-column English footer
    clean_footer = '''<footer class="footer-master no-print" style="background: #FAF7F2 !important; color: #475569 !important; border-top: 1px solid rgba(226, 218, 205, 0.9) !important; padding: 48px 0 24px;">
    <div class="container-app">
      <div style="display: grid; grid-template-columns: 2fr 1.2fr 1.2fr; gap: 40px; margin-bottom: 40px; flex-wrap: wrap;">
        
        <!-- Brand Lockup & Mission -->
        <div>
          <div class="footer-brand-lockup" onclick="navToView('landing')" style="margin-bottom: 12px; display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <div style="width:34px; height:34px; border-radius:8px; background:linear-gradient(135deg, #9E1B32 0%, #680E1C 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; border: 1px solid rgba(245, 208, 97, 0.4);">
              GV
            </div>
            <div>
              <div style="font-family: 'Outfit', sans-serif; font-size: 19px; font-weight: 800; color: #8B1528;">GiftVault</div>
              <div style="font-family: 'Cinzel', serif; font-size: 9px; font-weight: 700; color: #B38438; letter-spacing: 0.1em;">THE SACRED LEDGER</div>
            </div>
          </div>
          <p style="font-size: 13px; color: #64748B; line-height: 1.6; max-width: 340px;">
            The modern digital red notebook dedicated to sacred Indian family celebrations. Preserving generational blessings with 100% offline security.
          </p>
          <div style="margin-top: 14px; font-size: 12px; color: #B38438; font-weight: 600;">
            Auspicious • Prosperous • Blessed
          </div>
        </div>

        <!-- Celebrations (100% Clean English) -->
        <div>
          <h5 style="color: #0F172A; font-family: 'Outfit', sans-serif; font-size: 13px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 14px;">CELEBRATIONS</h5>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 13px; color: #64748B; line-height: 2.1;">
            <li><a href="#hub" onclick="openEventWorkspace('event-wedding')" style="color: inherit; text-decoration: none;">Royal Wedding Ceremony</a></li>
            <li><a href="#hub" onclick="openEventWorkspace('event-housewarming')" style="color: inherit; text-decoration: none;">Housewarming (Griha Pravesham)</a></li>
            <li><a href="#hub" onclick="openEventWorkspace('event-halfsaree')" style="color: inherit; text-decoration: none;">Half-Saree Ceremony</a></li>
            <li><a href="#hub" onclick="openEventWorkspace('event-yagnam')" style="color: inherit; text-decoration: none;">Vedic Shanti Yagnam</a></li>
          </ul>
        </div>

        <!-- Sacred Tools (100% Clean English) -->
        <div>
          <h5 style="color: #0F172A; font-family: 'Outfit', sans-serif; font-size: 13px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 14px;">SACRED TOOLS</h5>
          <ul style="list-style: none; padding: 0; margin: 0; font-size: 13px; color: #64748B; line-height: 2.1;">
            <li><a href="#features" style="color: inherit; text-decoration: none;">Digital Shagun Ledger</a></li>
            <li><a href="#features" style="color: inherit; text-decoration: none;">Instant 2-Inch Thermal Slips</a></li>
            <li><a href="#features" style="color: inherit; text-decoration: none;">Safe Offline Vault Backup</a></li>
            <li><a href="#features" style="color: inherit; text-decoration: none;">Guest Reciprocity Tracking</a></li>
          </ul>
        </div>

      </div>

      <!-- Footer Bottom Copyright -->
      <div style="border-top: 1px solid rgba(226, 218, 205, 0.8); padding-top: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; font-size: 12px; color: #94A3B8;">
        <div>
          © 2026 GiftVault Technologies. Crafted with devotion for Indian family celebrations.
        </div>
        <div style="display: flex; gap: 18px;">
          <span>Privacy Vault</span>
          <span>Terms of Tradition</span>
          <span>Support: +91 98765 43210</span>
        </div>
      </div>
    </div>
  </footer>'''

    footer_pattern = re.compile(r'<footer class="footer-master.*?</footer>', re.DOTALL)
    html = footer_pattern.sub(clean_footer, html)

    # -------------------------------------------------------------
    # D. LOGIN PAGE: REMOVE TEXT OVERLAY ON LEFT IMAGE ENTIRELY
    # -------------------------------------------------------------
    # Remove login-edge-narrative
    html = re.sub(
        r'<div class="login-edge-narrative">.*?</div>\s*</div>\s*<!-- RIGHT 48% PANEL:',
        '</div>\n\n      <!-- RIGHT 48% PANEL:',
        html,
        flags=re.DOTALL
    )

    # Remove login-edge-overlay dark tint so photo is 100% bright & crystal clear
    html = re.sub(
        r'<div class="login-edge-overlay"></div>',
        '',
        html
    )

    # -------------------------------------------------------------
    # E. LOGIN PAGE: BACK BUTTON ON CREAM BACKGROUND WITH 8px RADIUS
    # -------------------------------------------------------------
    # Ensure back button is on cream side
    if 'class="login-cream-back-btn"' in html:
        # Update its style to 8px rounded corners
        html = re.sub(
            r'class="login-cream-back-btn"[^>]*>',
            'class="login-cream-back-btn" style="border-radius: 8px !important;">',
            html
        )

    # -------------------------------------------------------------
    # F. LOGIN BUTTON: 8px rounded rectangular, compact (max-width: 210px), visible text
    # -------------------------------------------------------------
    login_btn_html = '''<button type="submit" class="btn-enter-vault" style="height: 38px !important; max-width: 210px !important; border-radius: 8px !important; margin: 16px auto 0 !important; box-shadow: none !important;">
              <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important; font-family: 'Cinzel', serif; font-size: 13.5px; font-weight: 700; letter-spacing: 0.03em; pointer-events: none;">Enter Family Vault</span>
            </button>'''
    html = re.sub(
        r'<button type="submit" class="btn-enter-vault"[^>]*>.*?</button>',
        login_btn_html,
        html,
        flags=re.DOTALL
    )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated:', fn)

print('All code updates applied cleanly.')
