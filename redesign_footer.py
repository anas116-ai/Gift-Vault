import re

target_files = [
    r'c:\Project\Gift Valut\web_preview\index.html',
    r'c:\Project\Gift Valut\web_preview\desktop.html',
    r'c:\Project\Gift Valut\web_preview\mobile.html',
    r'c:\Project\Gift Valut\build\web\index.html',
    r'c:\Project\Gift Valut\web\index.html'
]

with open(target_files[0], 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Footer CSS from Black background to Creative Auspicious Warm Parchment & Ivory Card Style
old_footer_css = '''.main-footer {
      background: var(--c-night);
      color: #FFFFFF;
      border-top: 3px solid var(--c-crimson);
      padding: 56px 32px 36px;
      margin-top: auto;
    }
    .footer-grid {
      max-width: 1280px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr;
      gap: 40px;
      margin-bottom: 40px;
    }
    .footer-brand h3 {
      font-family: var(--font-serif);
      font-size: 26px;
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 8px;
    }
    .footer-brand p {
      font-size: 14px;
      color: #94A3B8;
      line-height: 1.6;
    }
    .footer-col h4 {
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--c-crimson);
      margin-bottom: 16px;
    }
    .footer-links-list {
      list-style: none;
    }
    .footer-links-list li {
      margin-bottom: 10px;
    }
    .footer-btn-link {
      background: none;
      border: none;
      color: #CBD5E1;
      font-family: var(--font-sans);
      font-size: 13.5px;
      cursor: pointer;
      transition: color 0.2s ease;
      padding: 0;
    }
    .footer-btn-link:hover {
      color: #FFFFFF;
    }
    .footer-bottom-bar {
      max-width: 1280px;
      margin: 0 auto;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
      padding-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-sans);
      font-size: 12.5px;
      color: #94A3B8;
    }'''

new_footer_css = '''.main-footer {
      background: #F8F9F5;
      color: var(--c-night);
      border-top: 2px solid var(--c-night);
      padding: 0 0 36px;
      margin-top: auto;
      position: relative;
    }
    .footer-top-auspicious-band {
      background: #FFFFFF;
      border-bottom: 1px solid var(--c-border);
      padding: 12px 24px;
      text-align: center;
      font-family: var(--font-serif);
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: var(--c-crimson);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
    }
    .footer-top-auspicious-band::before,
    .footer-top-auspicious-band::after {
      content: "";
      display: inline-block;
      width: 40px;
      height: 1.5px;
      background: var(--c-crimson);
      opacity: 0.5;
    }
    .footer-content-wrap {
      max-width: 1280px;
      margin: 0 auto;
      padding: 48px 32px 0;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.4fr 0.9fr 0.9fr 1.2fr;
      gap: 36px;
      margin-bottom: 36px;
    }
    .footer-brand h3 {
      font-family: var(--font-serif);
      font-size: 26px;
      font-weight: 800;
      color: var(--c-night);
      margin-bottom: 4px;
    }
    .footer-brand p {
      font-size: 13.5px;
      color: #475569;
      line-height: 1.6;
    }
    .footer-col h4 {
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--c-crimson);
      margin-bottom: 16px;
    }
    .footer-links-list {
      list-style: none;
    }
    .footer-links-list li {
      margin-bottom: 10px;
    }
    .footer-btn-link {
      background: none;
      border: none;
      color: #334155;
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
      padding: 0;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .footer-btn-link:hover {
      color: var(--c-crimson);
      transform: translateX(4px);
    }
    .footer-trust-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-night);
      border-radius: 12px;
      padding: 18px;
      box-shadow: 0 4px 16px rgba(0, 4, 17, 0.04);
    }
    .footer-bottom-bar {
      border-top: 1px solid #E2E8F0;
      padding-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-sans);
      font-size: 12.5px;
      color: #64748B;
      flex-wrap: wrap;
      gap: 12px;
    }'''

if old_footer_css in html:
    html = html.replace(old_footer_css, new_footer_css)

# 2. Update Footer HTML structure
old_footer_html = '''  <!-- FOOTER -->
  <footer class="main-footer">
    <div class="footer-grid">
      <div class="footer-brand">
        <h3>GiftVault</h3>
        <p data-i18n="footer_about">The modern digital Red Notebook and Shagun Treasury engineered for Indian family celebrations and reception desks worldwide.</p>
        <div style="margin-top: 16px; font-family: var(--font-sans); font-size: 13.5px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #FFFFFF;">
          SHUBHAM BHAVATU
        </div>
      </div>
      <div class="footer-col">
        <h4 data-i18n="nav_capabilities">Capabilities</h4>
        <ul class="footer-links-list">
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');" data-i18n="cap_1_title">Munshi Rapid Entry</button></li>
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');" data-i18n="cap_2_title">Reciprocity Tracker</button></li>
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');" data-i18n="cap_3_title">Digital Red Notebook</button></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 data-i18n="footer_reception">Reception Desk</h4>
        <ul class="footer-links-list">
          <li><button type="button" class="footer-btn-link" onclick="navToView('login')" data-i18n="btn_open_desk">Open Reception Desk</button></li>
          <li><button type="button" class="footer-btn-link" onclick="navToView('login')" data-i18n="btn_login">Login with OTP</button></li>
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');" data-i18n="btn_view_ledger">View Sample Ledger</button></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom-bar">
      <div>&copy; 2026 GiftVault (గిఫ్ట్ వాలెట్ / రాయల్ శుభకార్య ఖజానా). All rights reserved.</div>
      <div data-i18n="footer_privacy">Engineered with reverence for timeless Indian traditions & modern family privacy.</div>
    </div>
  </footer>'''

new_footer_html = '''  <!-- FOOTER: CREATIVE AUSPICIOUS PARCHMENT AESTHETIC (WITHOUT BLACK BACKGROUND) -->
  <footer class="main-footer">
    <!-- Auspicious Sacred Shlokam Top Band -->
    <div class="footer-top-auspicious-band">
      <span>॥ శ్రీరస్తు - శుభమస్తు - అవిఘ్నమస్తు ॥</span>
    </div>

    <div class="footer-content-wrap">
      <div class="footer-grid">
        <!-- Brand & Vision -->
        <div class="footer-brand">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
            <span style="font-size: 22px;">🏮</span>
            <h3>GiftVault</h3>
          </div>
          <div style="font-size: 11.5px; font-weight: 700; color: var(--c-crimson); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px;" data-i18n="footer_subtag">
            రాయల్ శుభకార్య ఖజానా • OFFICIAL CELEBRATION TREASURY
          </div>
          <p data-i18n="footer_about">
            The modern digital Red Notebook and Shagun Treasury engineered for Indian family celebrations and busy reception desks worldwide.
          </p>
          <div style="margin-top: 14px; display: inline-flex; align-items: center; gap: 6px; background: #FFFFFF; border: 1px solid var(--c-border); padding: 5px 10px; border-radius: 20px; font-size: 11.5px; font-weight: 600; color: var(--c-emerald);">
            <span>🛡️</span> <span>100% End-to-End Encrypted Family Cloud</span>
          </div>
        </div>

        <!-- Core Features -->
        <div class="footer-col">
          <h4 data-i18n="nav_capabilities">Capabilities</h4>
          <ul class="footer-links-list">
            <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');"><span>✍️</span> <span data-i18n="cap_1_title">Munshi Rapid Entry</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');"><span>🔄</span> <span data-i18n="cap_2_title">Reciprocity Tracker</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');"><span>📖</span> <span data-i18n="cap_3_title">Digital Red Notebook</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="openPricingModal();"><span>👑</span> <span data-i18n="nav_plans_btn">Celebration Plans (₹49)</span></button></li>
          </ul>
        </div>

        <!-- Reception Desk & Tools -->
        <div class="footer-col">
          <h4 data-i18n="footer_reception">Reception Desk</h4>
          <ul class="footer-links-list">
            <li><button type="button" class="footer-btn-link" onclick="navToView('login')"><span>🚪</span> <span data-i18n="btn_open_desk">Open Reception Desk</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="enterGuestDemoMode()"><span>👀</span> <span data-i18n="btn_guest_demo">Explore as Guest</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="navToView('hub')"><span>🎪</span> <span data-i18n="hub_title">Family Event Hub</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="openPrintSlip('GV-101', 'K. Venkata Rao Garu', 'Vijayawada', 'UPI PhonePe', '₹10,116')"><span>🖨️</span> <span>Thermal Slip Preview</span></button></li>
          </ul>
        </div>

        <!-- Auspicious Heritage Card -->
        <div class="footer-col">
          <div class="footer-trust-card">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
              <span style="font-size: 18px;">🏛️</span>
              <strong style="font-family: var(--font-serif); font-size: 14.5px; color: var(--c-night);" data-i18n="footer_trust_head">Sacred Milestone Trust</strong>
            </div>
            <div style="font-size: 12px; color: #475569; line-height: 1.5; margin-bottom: 12px;" data-i18n="footer_trust_body">
              Designed for celebration counters in Hyderabad, Vijayawada, Bangalore, Chennai, Mumbai & Indian families worldwide.
            </div>
            <div style="display: flex; gap: 6px; flex-wrap: wrap;">
              <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF; font-size: 10px;">ZERO ADS</span>
              <span class="tag-badge" style="background: var(--c-emerald); color: #FFFFFF; font-size: 10px;">SAFE CLOUD</span>
              <span class="tag-badge" style="background: var(--c-crimson); color: #FFFFFF; font-size: 10px;">LUCKY ₹1 COIN</span>
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom Bar -->
      <div class="footer-bottom-bar">
        <div>
          &copy; 2026 <strong>GiftVault</strong> (గిఫ్ట్ వాలెట్ / రాయల్ శుభకార్య ఖజానా). All rights reserved.
        </div>
        <div data-i18n="footer_privacy">
          Engineered with reverence for timeless Indian traditions & modern family privacy.
        </div>
      </div>
    </div>
  </footer>'''

if old_footer_html in html:
    html = html.replace(old_footer_html, new_footer_html)

# Add i18n keys for new footer items
html = html.replace('footer_privacy: "Engineered with reverence', 'footer_subtag: "రాయల్ శుభకార్య ఖజానా • OFFICIAL CELEBRATION TREASURY",\n    footer_trust_head: "Sacred Milestone Trust",\n    footer_trust_body: "Designed for celebration counters in Hyderabad, Vijayawada, Bangalore, Chennai, Mumbai & Indian families worldwide.",\n    footer_privacy: "Engineered with reverence')

for path in target_files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated Footer: {path} ({len(html)} bytes)")

print("\nSuccessfully updated footer to creative non-black aesthetic across all files!")
