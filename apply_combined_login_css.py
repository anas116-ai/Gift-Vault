import os

# Update layout.css across all locations
combined_css = '''
/* ==========================================================================
   COMBINED LOGIN ARCHITECTURE (Lovebirds Floating Split + Exact Sacred Card)
   ========================================================================== */
.view-screen-pane.active {
  display: block !important;
  opacity: 1 !important;
  transform: none !important;
  animation: none !important;
}

#view-login {
  min-height: 100vh;
  width: 100%;
  margin: 0;
  padding: 0;
  background: #111418;
}

.login-fullscreen-portal {
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px 32px 24px;
  position: relative;
  overflow-y: auto;
  background: radial-gradient(circle at 50% 25%, #252D37 0%, #161A20 55%, #0B0E12 100%);
}

.login-top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1080px;
  width: 100%;
  margin: 0 auto 12px;
  position: relative;
  z-index: 2;
}

.login-trust-top {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: #CBD5E1;
  font-size: 12px;
  font-weight: 600;
}

/* Master Floating Split Card */
.combined-master-card {
  max-width: 1080px;
  width: 100%;
  min-height: 620px;
  margin: auto;
  display: grid;
  grid-template-columns: 1.08fr 0.92fr;
  border-radius: 28px;
  overflow: hidden;
  box-shadow: 0 40px 100px -20px rgba(0, 0, 0, 0.75), 0 0 0 1px rgba(255, 255, 255, 0.12);
  background: #FAF7F2;
  position: relative;
  z-index: 2;
}

/* LEFT PANEL: Real Indian Wedding Scene */
.combined-left-scene {
  position: relative;
  overflow: hidden;
  background: #1A050A;
  min-height: 600px;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

.combined-left-scene .scene-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

.combined-master-card:hover .combined-left-scene .scene-img {
  transform: scale(1.03);
}

.combined-left-scene .scene-overlay-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(180deg, rgba(15, 23, 42, 0.02) 0%, rgba(26, 5, 10, 0.25) 45%, rgba(20, 3, 7, 0.94) 100%);
  pointer-events: none;
}

.scene-bottom-content {
  position: relative;
  z-index: 2;
  padding: 32px 34px 28px;
  color: #FFFFFF;
}

.carousel-dots-row {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 12px;
}

.dot-pill-active {
  width: 24px;
  height: 6px;
  border-radius: 999px;
  background: #FFFFFF;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.25);
}

.dot-circle-subtle {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.45);
}

.scene-title {
  font-family: 'Outfit', sans-serif;
  font-size: 22px;
  font-weight: 700;
  color: #FFFFFF;
  letter-spacing: -0.01em;
  margin-bottom: 6px;
  line-height: 1.3;
}

.scene-subtitle {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.88);
  line-height: 1.55;
  max-width: 440px;
}

/* RIGHT PANEL: Exact Ivory Card */
.combined-right-pane {
  background: #FAF7F2;
  padding: 32px 36px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position: relative;
}

.exact-auth-card {
  max-width: 420px;
  width: 100%;
  background: #FFFDF9;
  border: 1.5px solid rgba(226, 218, 205, 0.85);
  border-radius: 24px;
  padding: 34px 32px 26px;
  box-shadow: 0 15px 35px -5px rgba(15, 23, 42, 0.05), 0 4px 12px rgba(0, 0, 0, 0.02);
  position: relative;
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

.login-bottom-trust {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 32px;
  color: #94A3B8;
  font-size: 11.5px;
  font-weight: 500;
  margin-top: 14px;
}

@media (max-width: 960px) {
  .combined-master-card {
    grid-template-columns: 1fr;
  }
  .combined-left-scene {
    min-height: 280px;
  }
  .combined-right-pane {
    padding: 24px 20px;
  }
  .exact-auth-card {
    padding: 28px 22px 22px;
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
        
        start = content.find('/* ==========================================================================\n   COMBINED LOGIN ARCHITECTURE')
        if start != -1:
            content = content[:start]
        
        content = content.rstrip() + '\n\n' + combined_css.strip() + '\n'
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated CSS in: {css_file}")

print("CSS update completed successfully!")
