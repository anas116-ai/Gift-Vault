import os

full_upgrade_css = '''
/* ==========================================================================
   LUXURY REDESIGNED NAVBAR (Top-Notch Senior SaaS Standard)
   ========================================================================== */
.header-glass {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border-bottom: 1px solid rgba(226, 218, 205, 0.7);
  padding: 0;
  box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);
  transition: all 0.25s ease;
}

.nav-container-luxury {
  max-width: 1360px;
  width: 100%;
  height: 68px;
  margin: 0 auto;
  padding: 0 28px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Brand Lockup */
.nav-brand-lockup {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  cursor: pointer;
  user-select: none;
}

.nav-emblem-box {
  width: 38px;
  height: 38px;
  border-radius: 11px;
  background: linear-gradient(135deg, #9E1B32 0%, #680E1C 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 4px 14px rgba(158, 27, 50, 0.32);
  border: 1px solid rgba(245, 208, 97, 0.45);
  flex-shrink: 0;
  transition: transform 0.2s ease;
}
.nav-brand-lockup:hover .nav-emblem-box {
  transform: translateY(-1px) scale(1.03);
}

.nav-brand-text {
  display: flex;
  flex-direction: column;
}

.nav-brand-title {
  font-family: 'Outfit', sans-serif;
  font-size: 22px;
  font-weight: 800;
  color: #8B1528;
  letter-spacing: -0.02em;
  line-height: 1.1;
  display: inline-flex;
  align-items: center;
}

.nav-v-swoosh {
  color: #B38438;
  font-family: 'Cinzel', serif;
  font-style: italic;
  font-weight: 700;
  display: inline-block;
  padding: 0 1px;
}

.nav-brand-tagline {
  font-family: 'Cinzel', serif;
  font-size: 9.5px;
  font-weight: 700;
  color: #B38438;
  letter-spacing: 0.12em;
  margin-top: 2px;
}

/* Center Dock */
.nav-center-dock {
  display: flex;
  align-items: center;
  gap: 3px;
  background: rgba(248, 246, 240, 0.85);
  border: 1px solid rgba(226, 218, 205, 0.65);
  border-radius: 999px;
  padding: 4px 6px;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.03);
}

.nav-dock-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 16px;
  border-radius: 999px;
  color: #334155;
  text-decoration: none;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 13.5px;
  font-weight: 600;
  transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
}

.nav-dock-link:hover {
  background: #FFFFFF;
  color: #8B1528;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.nav-dock-counter {
  position: relative;
}

.nav-live-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2);
}

/* Right Actions */
.nav-right-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.nav-lang-picker {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #FFFFFF;
  border: 1.5px solid #E2D8CD;
  border-radius: 999px;
  padding: 5px 12px;
  color: #475569;
  font-size: 12.5px;
  font-weight: 600;
  transition: border-color 0.18s;
}
.nav-lang-picker:focus-within {
  border-color: #8B1528;
}

.nav-lang-select {
  border: none;
  outline: none;
  background: transparent;
  font-family: inherit;
  font-size: 12.5px;
  font-weight: 600;
  color: #1E293B;
  cursor: pointer;
}

.btn-nav-signin {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: linear-gradient(135deg, #9E1B32 0%, #7E1225 100%);
  color: #FFFFFF;
  font-family: 'Outfit', sans-serif;
  font-size: 13.5px;
  font-weight: 700;
  padding: 9px 20px;
  border-radius: 999px;
  border: 1px solid rgba(245, 208, 97, 0.35);
  box-shadow: 0 4px 14px rgba(158, 27, 50, 0.28);
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  text-decoration: none;
}
.btn-nav-signin:hover {
  background: linear-gradient(135deg, #8B1528 0%, #680E1C 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(158, 27, 50, 0.38);
}

.nav-user-badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  font-weight: 700;
  color: #0F172A;
  background: #FFFFFF;
  padding: 4px 12px;
  border-radius: 20px;
  border: 1px solid rgba(226, 218, 205, 0.8);
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.nav-user-avatar-circle {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: #9E1B32;
  color: #FFF;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 10.5px;
  font-weight: 800;
}


/* ==========================================================================
   FULL-SCREEN EDGE-TO-EDGE SIGN-IN PORTAL (100vw x 100vh Golden Ratio)
   ========================================================================== */
#view-login {
  min-height: 100vh;
  width: 100%;
  margin: 0;
  padding: 0;
  background: #FAF7F2;
}

#view-login.active {
  display: block !important;
  opacity: 1 !important;
  transform: none !important;
  animation: none !important;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  max-height: 100vh;
  overflow: hidden;
  z-index: 9999;
}

.login-fullscreen-edge {
  width: 100vw;
  height: 100vh;
  min-height: 100vh;
  max-height: 100vh;
  display: grid;
  grid-template-columns: 1.14fr 0.86fr;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background: #FAF7F2;
}

/* Left 52% Panel: Full Bleed Photo */
.login-edge-left {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  background: #140307;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.login-edge-photo {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

.login-edge-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(180deg, rgba(15, 23, 42, 0.15) 0%, rgba(20, 3, 7, 0.3) 45%, rgba(15, 2, 5, 0.94) 100%);
  pointer-events: none;
}

.login-edge-topbar {
  position: relative;
  z-index: 5;
  padding: 28px 36px;
}

.login-edge-back-btn {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 255, 255, 0.28);
  color: #FFFFFF;
  padding: 9px 20px;
  border-radius: 999px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.login-edge-back-btn:hover {
  background: rgba(255, 255, 255, 0.26);
  transform: translateX(-3px);
}

.login-edge-narrative {
  position: relative;
  z-index: 5;
  padding: 36px 44px 40px;
  color: #FFFFFF;
}

.login-carousel-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 14px;
}

.carousel-pill-live {
  width: 26px;
  height: 6px;
  border-radius: 999px;
  background: #FFFFFF;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
}

.carousel-circle-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.45);
}

.login-edge-heading {
  font-family: 'Outfit', sans-serif;
  font-size: 26px;
  font-weight: 700;
  color: #FFFFFF;
  letter-spacing: -0.015em;
  margin-bottom: 8px;
  line-height: 1.25;
}

.login-edge-subtext {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 14px;
  color: rgba(255, 255, 255, 0.88);
  line-height: 1.55;
  max-width: 480px;
}

/* Right 48% Panel: Full Height Ivory Sacred Ledger */
.login-edge-right {
  width: 100%;
  height: 100vh;
  background: #FAF7F2;
  padding: 28px 44px 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  overflow-y: auto;
  position: relative;
}

.login-right-top {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.login-security-tag {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  color: #475569;
  font-size: 12px;
  font-weight: 600;
  background: #FFFFFF;
  padding: 5px 12px;
  border-radius: 999px;
  border: 1px solid rgba(226, 218, 205, 0.7);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
}

.exact-auth-card-edge {
  max-width: 420px;
  width: 100%;
  background: #FFFDF9;
  border: 1.5px solid rgba(226, 218, 205, 0.85);
  border-radius: 24px;
  padding: 34px 34px 28px;
  box-shadow: 0 18px 40px -10px rgba(15, 23, 42, 0.06), 0 4px 12px rgba(0, 0, 0, 0.02);
  position: relative;
  margin: auto 0;
}

.card-dots-menu {
  position: absolute;
  top: 18px;
  right: 20px;
  color: #94A3B8;
  font-size: 18px;
  cursor: pointer;
  line-height: 1;
  padding: 4px 8px;
  border-radius: 6px;
  transition: all 0.2s;
}
.card-dots-menu:hover {
  background: rgba(0, 0, 0, 0.04);
  color: #475569;
}

.brand-lockup {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  margin-bottom: 22px;
}

.brand-name {
  font-family: 'Outfit', sans-serif;
  font-size: 34px;
  font-weight: 700;
  color: #8B1528;
  letter-spacing: -0.01em;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  line-height: 1.1;
}

.brand-v-swoosh {
  color: #B38438;
  font-family: 'Cinzel', serif;
  font-style: italic;
  font-weight: 700;
  display: inline-block;
  padding: 0 1px;
}

.brand-subtitle {
  font-family: 'Cinzel', serif;
  font-size: 13.5px;
  font-weight: 700;
  color: #B38438;
  letter-spacing: 0.08em;
  margin-top: 5px;
  display: block;
}

.form-field-group {
  margin-bottom: 16px;
}

.field-label {
  display: block;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: #1F2937;
  margin-bottom: 7px;
}

.phone-input-container {
  display: flex;
  align-items: center;
  border: 1.5px solid #D1D5DB;
  border-radius: 12px;
  background: #FFFFFF;
  padding: 4px 14px;
  transition: all 0.2s ease;
}
.phone-input-container:focus-within {
  border-color: #8B1528;
  box-shadow: 0 0 0 3px rgba(139, 21, 40, 0.08);
}

.phone-prefix {
  font-size: 14.5px;
  font-weight: 700;
  color: #111827;
  padding-right: 12px;
  border-right: 1.5px solid #E5E7EB;
  user-select: none;
}

.phone-input {
  flex: 1;
  border: none;
  background: transparent;
  outline: none;
  padding: 8px 0 8px 12px;
  font-size: 14.5px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  color: #111827;
}

.otp-boxes-row {
  display: flex;
  gap: 8px;
  justify-content: space-between;
}

.otp-box {
  width: 44px;
  height: 46px;
  border: 1.5px solid #D1D5DB;
  border-radius: 10px;
  text-align: center;
  font-size: 19px;
  font-weight: 700;
  color: #111827;
  background: #FFFFFF;
  outline: none;
  transition: all 0.2s ease;
  font-family: 'Outfit', sans-serif;
}
.otp-box:focus {
  border-color: #8B1528;
  box-shadow: 0 0 0 3px rgba(139, 21, 40, 0.08);
}

.btn-enter-vault {
  width: 100%;
  background: #9E1B32;
  color: #FFFFFF;
  border-radius: 999px;
  padding: 13px 26px;
  font-family: 'Outfit', sans-serif;
  font-size: 14.5px;
  font-weight: 700;
  letter-spacing: 0.02em;
  border: none;
  cursor: pointer;
  box-shadow: 0 8px 22px rgba(158, 27, 50, 0.32);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  margin-top: 18px;
}
.btn-enter-vault:hover {
  background: #801326;
  transform: translateY(-1px);
  box-shadow: 0 10px 26px rgba(158, 27, 50, 0.4);
}

.resend-row {
  text-align: center;
  margin-top: 11px;
  font-size: 12px;
  color: #4B5563;
  font-weight: 500;
}

.need-help-link {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  margin-top: 16px;
  font-size: 12.5px;
  font-weight: 600;
  color: #1F2937;
  cursor: pointer;
  text-decoration: none;
  transition: color 0.15s;
}
.need-help-link:hover {
  color: #8B1528;
}

.security-strip {
  text-align: center;
  font-size: 10.5px;
  color: #6B7280;
  margin-top: 5px;
  letter-spacing: 0.02em;
}

.btn-guest-pass {
  margin-top: 14px;
  width: 100%;
  background: #FFF5F6;
  border: 1px dashed rgba(158, 27, 50, 0.35);
  border-radius: 999px;
  padding: 9px 18px;
  font-size: 12px;
  font-weight: 700;
  color: #9E1B32;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}
.btn-guest-pass:hover {
  background: #FEE2E2;
  border-color: #9E1B32;
}

.login-bottom-trust-edge {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  color: #64748B;
  font-size: 11px;
  font-weight: 500;
  padding-top: 12px;
}

@media (max-width: 960px) {
  .login-fullscreen-edge {
    grid-template-columns: 1fr;
    overflow-y: auto;
  }
  .login-edge-left {
    min-height: 320px;
    height: 320px;
  }
  .login-edge-right {
    height: auto;
    min-height: 100vh;
    padding: 24px 20px;
  }
  .exact-auth-card-edge {
    padding: 26px 20px 20px;
  }
}
'''

target_css_files = [
    'assets/css/layout.css',
    'web_preview/assets/css/layout.css',
    'build/web/assets/css/layout.css',
    'web/assets/css/layout.css'
]

for css_file in target_css_files:
    if os.path.exists(css_file):
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Strip older combined architecture block
        start = content.find('/* ==========================================================================\n   LUXURY REDESIGNED NAVBAR')
        if start != -1:
            content = content[:start]
        else:
            start2 = content.find('/* ==========================================================================\n   COMBINED LOGIN ARCHITECTURE')
            if start2 != -1:
                content = content[:start2]
        
        content = content.rstrip() + '\n\n' + full_upgrade_css.strip() + '\n'
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated CSS in: {css_file}")

print("CSS update completed successfully!")
