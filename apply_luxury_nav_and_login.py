import os
import re

# 1. NEW LUXURY NAVBAR HTML
new_header_html = '''<header class="header-glass no-print">
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

      <!-- Center Pill Navigation Menu -->
      <nav class="nav-center-dock hide-mobile">
        <a href="#features" class="nav-dock-link" data-i18n="navFeatures" onclick="if(window.GVStore.state.activeView !== 'landing') navToView('landing');">
          <span>Features</span>
        </a>
        <a href="#hub" class="nav-dock-link" data-i18n="navDashboard" onclick="event.preventDefault(); navToView('hub');">
          <span>Dashboard</span>
        </a>
        <a href="#counter" class="nav-dock-link nav-dock-counter" data-i18n="navGiftCounter" onclick="event.preventDefault(); openEventWorkspace('event-wedding'); switchWorkspaceTab('tab-entry', null);">
          <span class="nav-live-dot"></span>
          <span>Gift Counter</span>
        </a>
        <a href="#pricing" class="nav-dock-link" data-i18n="navPricing" onclick="if(window.GVStore.state.activeView !== 'landing') navToView('landing');">
          <span>Pricing</span>
        </a>
        <a href="#faq" class="nav-dock-link" data-i18n="navFaq" onclick="if(window.GVStore.state.activeView !== 'landing') navToView('landing');">
          <span>FAQ</span>
        </a>
      </nav>

      <!-- Right Action Group -->
      <div class="nav-right-actions">
        <!-- Visual Luxury Language Switcher Pill -->
        <div class="nav-lang-picker">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          <select id="lang-select" onchange="if(window.GVI18n) window.GVI18n.apply(this.value);" class="nav-lang-select">
            <option value="en" selected>English</option>
            <option value="te">తెలుగు (Telugu)</option>
            <option value="hi">हिंदी (Hindi)</option>
          </select>
        </div>

        <!-- User Badge -->
        <div id="nav-user-badge" class="nav-user-badge-pill" style="display: none;">
          <span id="nav-user-avatar" class="nav-user-avatar-circle">SK</span>
          <span id="nav-user-name">Sri Krishna Family</span>
        </div>

        <!-- Sign In Button -->
        <button type="button" id="btn-header-signin" class="btn-nav-signin" onclick="navToView('login')">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          <span>Sign In</span>
        </button>
      </div>

    </div>
  </header>'''

# 2. NEW FULL-SCREEN LOGIN HTML (100vw x 100vh Edge-to-Edge)
new_fullscreen_login_html = '''<main id="view-login" class="view-screen-pane">
    <div class="login-fullscreen-edge">
      
      <!-- LEFT 52% PANEL: Full Bleed Real Indian Wedding Scene -->
      <div class="login-edge-left">
        <img src="assets/images/giftvault_login_showcase_final.jpg" alt="GiftVault Wedding Table Scene" class="login-edge-photo">
        <div class="login-edge-overlay"></div>
        
        <!-- Top Left Back Button -->
        <div class="login-edge-topbar">
          <button type="button" class="login-edge-back-btn" onclick="navToView('landing')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            <span>Back to Celebrations</span>
          </button>
        </div>

        <!-- Bottom Story & Carousel Dots -->
        <div class="login-edge-narrative">
          <div class="login-carousel-row">
            <span class="carousel-pill-live"></span>
            <span class="carousel-circle-dot"></span>
            <span class="carousel-circle-dot"></span>
          </div>
          <h2 class="login-edge-heading">Every Sacred Blessing, Preserved</h2>
          <p class="login-edge-subtext">The private digital shagun sanctuary for royal weddings, housewarmings, and timeless family traditions.</p>
        </div>
      </div>

      <!-- RIGHT 48% PANEL: Full Height Ivory Sacred Ledger Card -->
      <div class="login-edge-right">
        
        <!-- Top Security Row -->
        <div class="login-right-top">
          <div class="login-security-tag">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>256-Bit SSL Encrypted Vault</span>
          </div>
        </div>

        <!-- The Exact Ivory Card Center Stage -->
        <div class="exact-auth-card-edge">
          
          <!-- Options menu top right -->
          <div class="card-dots-menu" title="Options">⋮</div>

          <!-- Brand Logo Lockup -->
          <div class="brand-lockup">
            <div class="brand-name">
              Gift<span class="brand-v-swoosh">V</span>ault
            </div>
            <div class="brand-subtitle">THE SACRED LEDGER</div>
          </div>

          <form onsubmit="handleVerifyOTP(event); return false;">
            <!-- Phone Number Field -->
            <div class="form-field-group">
              <label class="field-label">Phone Number</label>
              <div class="phone-input-container">
                <span class="phone-prefix">+91</span>
                <input type="tel" id="login-mobile-input" class="phone-input" placeholder="Mobile Number" value="9876543210" maxlength="10" required>
              </div>
            </div>

            <!-- 6-digit OTP fields -->
            <div class="form-field-group">
              <label class="field-label">Enter 6-digit OTP</label>
              <div class="otp-boxes-row">
                <input type="text" id="otp-1" class="otp-box" value="1" maxlength="1" oninput="handleOtpInput(this, 1)" onkeydown="handleOtpKeyDown(event, 1)">
                <input type="text" id="otp-2" class="otp-box" value="2" maxlength="1" oninput="handleOtpInput(this, 2)" onkeydown="handleOtpKeyDown(event, 2)">
                <input type="text" id="otp-3" class="otp-box" value="3" maxlength="1" oninput="handleOtpInput(this, 3)" onkeydown="handleOtpKeyDown(event, 3)">
                <input type="text" id="otp-4" class="otp-box" value="4" maxlength="1" oninput="handleOtpInput(this, 4)" onkeydown="handleOtpKeyDown(event, 4)">
                <input type="text" id="otp-5" class="otp-box" value="5" maxlength="1" oninput="handleOtpInput(this, 5)" onkeydown="handleOtpKeyDown(event, 5)">
                <input type="text" id="otp-6" class="otp-box" value="6" maxlength="1" oninput="handleOtpInput(this, 6)" onkeydown="handleOtpKeyDown(event, 6)">
              </div>
            </div>

            <!-- Enter Family Vault Button -->
            <button type="submit" class="btn-enter-vault">
              Enter Family Vault
            </button>

            <!-- Resend OTP -->
            <div class="resend-row">
              Resend OTP (<span id="otp-countdown-val">58</span>s)
            </div>

            <!-- Need Help? -->
            <a class="need-help-link" href="javascript:void(0)" onclick="alert('GiftVault 24/7 Concierge Support: +91 98765 43210')">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              <span>Need Help?</span>
            </a>

            <!-- Security Badges -->
            <div class="security-strip">
              256-Bit Vault Security | End-to-End Encrypted
            </div>

            <!-- Fast-Track Instant Guest Pass for 1-Click Demo -->
            <button type="button" class="btn-guest-pass" onclick="enterGuestDemoMode()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>
              <span>Continue as Guest (Sri Krishna Family Demo)</span>
            </button>
          </form>

        </div>

        <!-- Bottom Trust Strip -->
        <div class="login-bottom-trust-edge">
          <span style="display: inline-flex; align-items: center; gap: 6px;">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            <span>Zero Cloud Leakage • Works 100% Offline</span>
          </span>
          <span style="display: inline-flex; align-items: center; gap: 6px;">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
            <span>Instant 2-Inch Thermal Slips</span>
          </span>
        </div>

      </div>

    </div>
  </main>'''

target_html_files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for fpath in target_html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace header
        content = re.sub(r'<header class="header-glass no-print">.*?</header>', new_header_html, content, flags=re.DOTALL)
        
        # Replace login view
        content = re.sub(r'<main id="view-login".*?</main>', new_fullscreen_login_html, content, flags=re.DOTALL)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML in {fpath}")

print("HTML transformations complete!")
