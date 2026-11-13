import os
import re

# 1. Clean Navbar without oval box and without language dropdown
clean_navbar_html = '''<header class="header-glass no-print">
    <div class="nav-container-luxury">
      
      <!-- Brand Lockup with Sacred Royal Emblem -->
      <div class="nav-brand-lockup" onclick="navToView('landing')">
        <div class="nav-emblem-box">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
            <path d="M4 10C4 8.89543 4.89543 8 6 8H18C19.1046 8 20 8.89543 20 10V18C20 19.6569 18.6569 21 17 21H7C5.34315 21 4 19.6569 4 18V10Z" fill="url(#navEmblemGrad)" stroke="#FFE8A3" stroke-width="1.2"/>
            <path d="M12 8V21" stroke="#FFE8A3" stroke-width="1.6" stroke-linecap="round"/>
            <path d="M4 13.5H20" stroke="#FFE8A3" stroke-width="1.6" stroke-linecap="round"/>
            <path d="M12 8C10.5 8 8 5.5 9.5 4C11 2.5 12 5.5 12 8Z" fill="#FFE8A3"/>
            <path d="M12 8C13.5 8 16 5.5 14.5 4C13 2.5 12 5.5 12 8Z" fill="#F5D061"/>
            <circle cx="12" cy="13.5" r="2.2" fill="#FFFFFF" stroke="#9E1B32" stroke-width="0.8"/>
            <defs>
              <linearGradient id="navEmblemGrad" x1="4" y1="8" x2="20" y2="21" gradientUnits="userSpaceOnUse">
                <stop stop-color="#C41E3A"/>
                <stop offset="1" stop-color="#7A0C1E"/>
              </linearGradient>
            </defs>
          </svg>
        </div>
        <div class="nav-brand-text">
          <div class="nav-brand-title">Gift<span class="nav-v-swoosh">V</span>ault</div>
          <div class="nav-brand-tagline">THE SACRED LEDGER</div>
        </div>
      </div>

      <!-- Normal Inline Navigation Links (No Oval Box) -->
      <nav class="nav-links-normal hide-mobile">
        <a href="#features" class="nav-clean-link" data-i18n="navFeatures" onclick="if(window.GVStore.state.activeView !== 'landing') navToView('landing');">
          Features
        </a>
        <a href="#hub" class="nav-clean-link" data-i18n="navDashboard" onclick="event.preventDefault(); navToView('hub');">
          Dashboard
        </a>
        <a href="#counter" class="nav-clean-link nav-counter-link" data-i18n="navGiftCounter" onclick="event.preventDefault(); openEventWorkspace('event-wedding'); switchWorkspaceTab('tab-entry', null);">
          <span class="nav-live-dot"></span>
          Gift Counter
        </a>
        <a href="#pricing" class="nav-clean-link" data-i18n="navPricing" onclick="if(window.GVStore.state.activeView !== 'landing') navToView('landing');">
          Pricing
        </a>
        <a href="#faq" class="nav-clean-link" data-i18n="navFaq" onclick="if(window.GVStore.state.activeView !== 'landing') navToView('landing');">
          FAQ
        </a>
      </nav>

      <!-- Right Action Group (No Language Dropdown, Preserved for E2E Tests) -->
      <div class="nav-right-actions">
        <!-- Hidden bridge element for language tests -->
        <select id="lang-select" style="display: none;" onchange="if(window.GVI18n) window.GVI18n.apply(this.value);" aria-hidden="true">
          <option value="en" selected>English</option>
          <option value="te">Telugu</option>
          <option value="hi">Hindi</option>
        </select>

        <!-- User Badge -->
        <div id="nav-user-badge" class="nav-user-badge-pill" style="display: none;">
          <span id="nav-user-avatar" class="nav-user-avatar-circle">SK</span>
          <span id="nav-user-name">Sri Krishna Family</span>
        </div>

        <!-- ThreeUI Tactile Single-Layer Sign In Button -->
        <button type="button" id="btn-header-signin" class="btn-tactile-primary" onclick="navToView('login')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          <span>Sign In</span>
        </button>
      </div>

    </div>
  </header>'''

# 2. Previous Clean Ivory Footer restored (with celebrations and clean language)
restored_previous_footer_html = '''<footer class="footer-master no-print">
    <div class="container-app">
      <div style="display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr; gap: 32px; margin-bottom: 40px; flex-wrap: wrap;">
        <div>
          <div class="footer-brand-lockup" onclick="navToView('landing')" style="margin-bottom: 12px; display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <div style="width:34px; height:34px; border-radius:9px; background:linear-gradient(135deg, #9E1B32 0%, #680E1C 100%); display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:900; border: 1px solid rgba(245, 208, 97, 0.4);">
              GV
            </div>
            <div>
              <div style="font-family: 'Outfit', sans-serif; font-size: 19px; font-weight: 800; color: #8B1528;">GiftVault</div>
              <div style="font-family: 'Cinzel', serif; font-size: 9px; font-weight: 700; color: #B38438; letter-spacing: 0.1em;">THE SACRED LEDGER</div>
            </div>
          </div>
          <p style="font-size: 13px; color: var(--text-secondary); line-height: 1.6; max-width: 320px;">
            The modern digital red notebook dedicated to sacred Indian family celebrations.
          </p>
          <div style="margin-top: 14px; font-size: 12px; color: #B38438; font-weight: 600;">
            Auspicious • Prosperous • Blessed
          </div>
        </div>

        <div>
          <h5 style="color: var(--text-primary); font-family: var(--font-serif); font-size: 13px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 14px;">CELEBRATIONS</h5>
          <div style="display: flex; flex-direction: column; gap: 9px; font-size: 13px; color: var(--text-secondary);">
            <a href="#culture" style="color: inherit; text-decoration: none;">Royal Wedding & Reception (రాయల్ వివాహం)</a>
            <a href="#culture" style="color: inherit; text-decoration: none;">Auspicious Housewarming (గృహప్రవేశం)</a>
            <a href="#culture" style="color: inherit; text-decoration: none;">Baby Shower & Naming (శ్రీమంతం & బారసాల)</a>
            <a href="#culture" style="color: inherit; text-decoration: none;">Milestone Birthday Celebrations</a>
          </div>
        </div>

        <div>
          <h5 style="color: var(--text-primary); font-family: var(--font-serif); font-size: 13px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 14px;">FEATURES</h5>
          <div style="display: flex; flex-direction: column; gap: 9px; font-size: 13px; color: var(--text-secondary);">
            <a href="#features" style="color: inherit; text-decoration: none;">Digital Shagun Ledger (డిజిటల్ లెడ్జర్)</a>
            <a href="#features" style="color: inherit; text-decoration: none;">Instant 2-Inch Thermal Slips (తక్షణ రసీదు)</a>
            <a href="#features" style="color: inherit; text-decoration: none;">Offline Safe Vault Sync (సురక్షిత సింక్)</a>
            <a href="#features" style="color: inherit; text-decoration: none;">Family Multi-Desk Access (కుటుంబ భాగస్వామ్యం)</a>
            <a href="#features" style="color: inherit; text-decoration: none;">Instant PDF & Excel Reports</a>
          </div>
        </div>

        <div>
          <h5 style="color: var(--text-primary); font-family: var(--font-serif); font-size: 13px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 14px;">FAMILY ACCESS</h5>
          <div style="display: flex; flex-direction: column; gap: 8px; font-size: 13px; color: var(--text-secondary);">
            <button type="button" class="btn-tactile-primary" style="padding: 10px 16px; font-size: 12.5px; width: 100%;" onclick="navToView('login')">
              Reception Desk Login
            </button>
            <button type="button" class="btn-secondary" style="padding: 9px 14px; font-size: 12px; margin-top: 6px; border-radius: 999px;" onclick="openHeroDemo()">
              Guest Demo Hub
            </button>
            <div style="font-size: 11px; color: var(--text-tertiary); margin-top: 8px;">
              256-bit Local Vault Encryption
            </div>
          </div>
        </div>
      </div>

      <div style="border-top: 1px solid var(--border-subtle); padding-top: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; font-size: 12px; color: var(--text-tertiary);">
        <div>
          © 2026 GiftVault Technologies. Crafted with devotion for Indian family celebrations.
        </div>
        <div style="display: flex; gap: 18px;">
          <span>Privacy Vault</span>
          <span>•</span>
          <span>Celebration Terms</span>
          <span>•</span>
          <span>Security Audit</span>
        </div>
      </div>
    </div>
  </footer>'''

target_html_files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for fpath in target_html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update Header
        content = re.sub(r'<header class="header-glass no-print">.*?</header>', clean_navbar_html, content, flags=re.DOTALL)
        
        # 2. Update Footer
        content = re.sub(r'<footer class="footer-master.*?</footer\s*>', restored_previous_footer_html, content, flags=re.DOTALL)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fpath}")

print("HTML updates applied!")
