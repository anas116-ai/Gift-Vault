import os
import re

new_login_html = '''<main id="view-login" class="view-screen-pane">
    <div class="login-fullscreen-portal">
      
      <!-- Top Floating Navigation Bar -->
      <div class="login-top-bar">
        <button type="button" class="login-back-btn" onclick="navToView('landing')">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          <span>Back to Celebrations</span>
        </button>
        <div class="login-trust-top">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          <span>256-Bit SSL Encrypted Vault</span>
        </div>
      </div>

      <!-- Master Floating Split Card (Lovebirds & Organic Wave Architecture) -->
      <div class="combined-master-card">
        
        <!-- LEFT PANEL: Real Indian Wedding Scene with iPhone & iPad Counter -->
        <div class="combined-left-scene">
          <img src="assets/images/giftvault_login_showcase_final.jpg" alt="GiftVault Wedding Table Registry Scene" class="scene-img">
          <div class="scene-overlay-gradient"></div>
          
          <!-- Bottom Narrative with Lovebirds Style Carousel Indicators -->
          <div class="scene-bottom-content">
            <div class="carousel-dots-row">
              <span class="dot-pill-active"></span>
              <span class="dot-circle-subtle"></span>
              <span class="dot-circle-subtle"></span>
            </div>
            <h3 class="scene-title">Every Sacred Blessing, Preserved</h3>
            <p class="scene-subtitle">The private digital shagun sanctuary for royal weddings, housewarmings, and timeless family traditions.</p>
          </div>
        </div>

        <!-- RIGHT PANEL: Exact Ivory Authentication Card -->
        <div class="combined-right-pane">
          <div class="exact-auth-card">
            
            <!-- Three dots menu top right -->
            <div class="card-dots-menu" title="Options">⋮</div>

            <!-- Brand Logo Lockup -->
            <div class="brand-lockup">
              <div class="brand-name">
                Gift<span class="brand-v-swoosh">V</span>ault
              </div>
              <div class="brand-subtitle">The Sacred Ledger</div>
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
        </div>

      </div>

      <!-- Bottom Trust Strip -->
      <div class="login-bottom-trust">
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
  </main>'''

# Apply to index.html and replicas
target_html_files = [
    'index.html',
    'web_preview/index.html',
    'build/web/index.html',
    'web/index.html'
]

for file_path in target_html_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated, count = re.subn(r'<main id="view-login".*?</main>', new_login_html, content, flags=re.DOTALL)
        if count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Successfully updated #view-login in: {file_path}")
        else:
            print(f"Could not find #view-login in: {file_path}")

print("HTML update complete!")
