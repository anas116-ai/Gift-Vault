import os
import re

css_additions = """
/* ==========================================================================
   MASTER REFINEMENTS: UNIVERSAL 32PX BUTTON SIZING & LUXURY CARD SYSTEM
   ========================================================================== */

/* Universal 32px Button Sizing System - Matching Navbar Sign In exactly */
#btn-header-signin,
#btn-hero-signin,
.btn-hero-demo,
#btn-features-dashboard,
.btn-enter-vault,
.btn-pricing-activate,
.login-cream-back-btn,
.btn-tactile-primary,
.btn-primary,
.btn-secondary {
  height: 32px !important;
  min-height: 32px !important;
  max-height: 32px !important;
  line-height: 32px !important;
  padding: 0 16px !important;
  font-size: 12.5px !important;
  font-weight: 700 !important;
  border-radius: 7px !important;
  box-shadow: none !important;
  text-shadow: none !important;
  margin: 0 !important;
  box-sizing: border-box !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  vertical-align: middle !important;
  gap: 6px !important;
  white-space: nowrap !important;
  cursor: pointer !important;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

/* Ensure Hero Action Buttons container has flawless horizontal alignment */
.hero-actions-container {
  display: flex !important;
  flex-direction: row !important;
  align-items: center !important;
  justify-content: flex-start !important;
  gap: 12px !important;
  flex-wrap: nowrap !important;
  margin-top: 0 !important;
  margin-bottom: 28px !important;
  padding: 0 !important;
}

#btn-hero-signin {
  border: none !important;
  background: #8A1526 !important;
  color: #FFFFFF !important;
}

.btn-hero-demo {
  border: 1.5px solid rgba(138, 21, 38, 0.25) !important;
  background: #FFFFFF !important;
  color: #8A1526 !important;
}

.btn-hero-demo:hover {
  background: #FFF5F6 !important;
  border-color: #8A1526 !important;
}

/* Hide green dot completely */
.nav-live-dot {
  display: none !important;
  opacity: 0 !important;
  visibility: hidden !important;
  width: 0 !important;
  height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
}

/* ==========================================================================
   REFINED CARD STYLES (UI/UX PRO MAX STANDARDS)
   ========================================================================== */

/* 1. Feature Cards (Aura Editorial Cards) */
.aura-editorial-card {
  background: #FFFFFF !important;
  border: 1px solid rgba(220, 212, 198, 0.75) !important;
  border-radius: 16px !important;
  padding: 28px 24px !important;
  box-shadow: 0 8px 24px -6px rgba(35, 18, 12, 0.05), 0 1px 3px rgba(0, 0, 0, 0.02) !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  position: relative !important;
}

.aura-editorial-card:hover {
  transform: translateY(-4px) !important;
  border-color: rgba(138, 21, 38, 0.35) !important;
  box-shadow: 0 16px 36px -8px rgba(138, 21, 38, 0.1), 0 2px 6px rgba(0, 0, 0, 0.03) !important;
}

/* 2. Tradition / Sacred Celebration Cards */
.tradition-card-luxury {
  background: #FFFFFF !important;
  border: 1.5px solid rgba(212, 160, 23, 0.25) !important;
  border-radius: 16px !important;
  padding: 26px 22px !important;
  box-shadow: 0 8px 22px -6px rgba(35, 18, 12, 0.04) !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
  position: relative !important;
}

.tradition-card-luxury:hover {
  transform: translateY(-3px) !important;
  border-color: rgba(212, 160, 23, 0.6) !important;
  box-shadow: 0 14px 32px -6px rgba(212, 160, 23, 0.12) !important;
}

/* 3. Pricing Cards */
.card-luxury {
  border-radius: 20px !important;
  box-shadow: 0 16px 38px -10px rgba(35, 18, 12, 0.08) !important;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.card-luxury:hover {
  transform: translateY(-4px) !important;
  box-shadow: 0 22px 48px -12px rgba(35, 18, 12, 0.12) !important;
}

/* 4. Login Card */
.exact-auth-card-edge {
  width: 100% !important;
  max-width: 420px !important;
  background: #FFFFFF !important;
  border: 1.5px solid rgba(220, 212, 198, 0.85) !important;
  border-radius: 18px !important;
  padding: 38px 34px 30px !important;
  box-shadow: 0 20px 45px -12px rgba(35, 18, 12, 0.09), 0 2px 6px rgba(0, 0, 0, 0.03) !important;
  position: relative !important;
  margin: 0 !important;
  box-sizing: border-box !important;
}
"""

def update_css():
    for p in ['assets/css/layout.css', 'web_preview/assets/css/layout.css', 'build/web/assets/css/layout.css', 'web/assets/css/layout.css']:
        if os.path.exists(p):
            with open(p, 'a', encoding='utf-8') as f:
                f.write(css_additions)
            print("Appended master CSS to", p)

def update_html(path):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Remove nav-live-dot
    c = re.sub(r'<span class="nav-live-dot"></span>\s*', '', c)

    # 2. Hero action buttons alignment & exact 32px styling
    old_hero_actions = re.search(r'<div class="hero-actions-container".*?</div>\s*</div>', c, re.DOTALL)
    # We can replace the inner buttons of hero-actions-container cleanly:
    new_hero_actions = """<div class="hero-actions-container" style="display: flex; flex-direction: row; align-items: center; justify-content: flex-start; gap: 12px; flex-wrap: nowrap; margin-bottom: 28px;">
            <button type="button" id="btn-hero-signin" class="btn-tactile-primary" style="height: 32px !important; padding: 0 16px !important; font-size: 12.5px !important; font-weight: 700 !important; border-radius: 7px !important; border: none !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; box-shadow: none !important; margin: 0 !important;" onclick="navToView('login')">
              <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Sign In</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            <button type="button" class="btn-hero-demo" style="height: 32px !important; padding: 0 16px !important; font-size: 12.5px !important; font-weight: 700 !important; border-radius: 7px !important; border: 1.5px solid rgba(138, 21, 38, 0.25) !important; color: #8A1526 !important; background: #FFFFFF !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; box-shadow: none !important; margin: 0 !important;" onclick="openHeroDemo()">
              <span>Explore Demo</span>
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            </button>
          </div>"""

    c = re.sub(r'<div class="hero-actions-container"[^>]*>.*?</div>\s*</div>', new_hero_actions + '\n          </div>', c, flags=re.DOTALL)

    # 3. Features "Explore Celebration Dashboard" button replacement
    old_feat_btn = re.search(r'<div style="text-align: center; margin-top: 32px;">\s*<button type="button" class="btn-primary".*?Explore Celebration Dashboard.*?</div>', c, re.DOTALL)
    new_feat_btn = """<div style="text-align: center; margin-top: 32px;">
          <button type="button" id="btn-features-dashboard" class="btn-tactile-primary" style="height: 32px !important; padding: 0 18px !important; font-size: 12.5px !important; font-weight: 700 !important; border-radius: 7px !important; border: none !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; box-shadow: none !important; margin: 0 !important;" onclick="openHeroDemo()">
            <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Open Celebration Hub</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>"""

    if old_feat_btn:
        c = c.replace(old_feat_btn.group(0), new_feat_btn)
    else:
        # Fallback regex
        c = re.sub(r'<button[^>]*onclick="openHeroDemo\(\)"[^>]*>.*?Explore Celebration Dashboard.*?</button>',
                   """<button type="button" id="btn-features-dashboard" class="btn-tactile-primary" style="height: 32px !important; padding: 0 18px !important; font-size: 12.5px !important; font-weight: 700 !important; border-radius: 7px !important; border: none !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; box-shadow: none !important; margin: 0 !important;" onclick="openHeroDemo()">
            <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Open Celebration Hub</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>""", c, flags=re.DOTALL)

    # 4. Update Hero Image src
    c = re.sub(r'src="assets/images/giftvault_flagship_hero_vertical.jpg"', 'src="assets/images/giftvault_hero_sacred_shagun_ledger.jpg"', c)
    c = re.sub(r'alt="GiftVault Flagship Royal Hardware UI"', 'alt="GiftVault Sacred Shagun & Gift Ledger"', c)

    # 5. Update Login Image src
    c = re.sub(r'src="assets/images/giftvault_login_showcase_final.jpg"', 'src="assets/images/giftvault_signin_luxury_gateway.jpg"', c)

    # 6. Ensure login Enter Family Vault button has height: 32px
    c = re.sub(r'class="btn-enter-vault" style="[^"]*"', 'class="btn-enter-vault" style="height: 32px !important; max-width: 200px !important; border-radius: 7px !important; margin: 18px auto 0 !important; box-shadow: none !important;"', c)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Applied master HTML refinements to {path}")

update_css()
for p in ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']:
    update_html(p)

print("All master refinements successfully written!")
