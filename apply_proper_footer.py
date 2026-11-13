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

# 1. High-Precision Modern Footer CSS
proper_footer_css = '''
    /* ==========================================
       PROPER LUXURY AUSPICIOUS FOOTER
       ========================================== */
    .main-footer {
      background: #FFFFFF;
      color: var(--c-night);
      border-top: 2px solid var(--c-night);
      margin-top: auto;
      width: 100%;
    }
    .footer-top-auspicious-band {
      background: #FFF1F2;
      border-bottom: 1px solid #FECDD3;
      padding: 12px 24px;
      text-align: center;
      font-family: var(--font-serif);
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.1em;
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
      width: 48px;
      height: 1.5px;
      background: var(--c-crimson);
      opacity: 0.45;
    }
    .footer-content-wrap {
      max-width: 1200px;
      margin: 0 auto;
      padding: 52px 28px 36px;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.35fr 0.95fr 0.95fr 1.25fr;
      gap: 36px;
      margin-bottom: 40px;
    }
    .footer-brand h3 {
      font-family: var(--font-serif);
      font-size: 26px;
      font-weight: 800;
      color: var(--c-night);
      margin-bottom: 4px;
      letter-spacing: -0.01em;
    }
    .footer-brand p {
      font-size: 14px;
      color: #475569;
      line-height: 1.65;
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
      padding: 0;
      margin: 0;
    }
    .footer-links-list li {
      margin-bottom: 12px;
    }
    .footer-btn-link {
      background: none;
      border: none;
      color: #334155;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      padding: 0;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      text-align: left;
    }
    .footer-btn-link:hover {
      color: var(--c-crimson);
      transform: translateX(4px);
    }
    .footer-trust-card {
      background: #F8F9FA;
      border: 1.5px solid var(--c-night);
      border-radius: 14px;
      padding: 20px;
      box-shadow: 0 4px 16px rgba(0, 4, 17, 0.04);
    }
    .footer-bottom-bar {
      border-top: 1px solid #E2E8F0;
      padding-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-sans);
      font-size: 13px;
      color: #64748B;
      flex-wrap: wrap;
      gap: 12px;
    }

    @media (max-width: 960px) {
      .footer-grid {
        grid-template-columns: 1fr 1fr !important;
        gap: 32px !important;
      }
    }
    @media (max-width: 600px) {
      .footer-grid {
        grid-template-columns: 1fr !important;
        gap: 28px !important;
      }
      .footer-content-wrap {
        padding: 36px 18px 28px !important;
      }
      .footer-bottom-bar {
        flex-direction: column;
        align-items: flex-start;
      }
    }
'''

# Replace footer CSS in html
old_footer_css_regex = r'\.main-footer\s*\{.*?(?=\/\*|\@media|\.universal|\.form|\.ws|<|\Z)'
# Let's replace the .main-footer and all footer rules
html = re.sub(r'\.main-footer\s*\{[^}]+\}', '', html)
html = re.sub(r'\.footer-top-auspicious-band[^{]*\{[^}]+\}', '', html)
html = re.sub(r'\.footer-content-wrap[^{]*\{[^}]+\}', '', html)
html = re.sub(r'\.footer-grid[^{]*\{[^}]+\}', '', html)
html = re.sub(r'\.footer-brand[^{]*\{[^}]+\}', '', html)
html = re.sub(r'\.footer-col[^{]*\{[^}]+\}', '', html)
html = re.sub(r'\.footer-links-list[^{]*\{[^}]+\}', '', html)
html = re.sub(r'\.footer-btn-link[^{]*\{[^}]+\}', '', html)
html = re.sub(r'\.footer-trust-card[^{]*\{[^}]+\}', '', html)
html = re.sub(r'\.footer-bottom-bar[^{]*\{[^}]+\}', '', html)

# Insert clean proper_footer_css before </style>
html = html.replace('</style>', proper_footer_css + '\n  </style>')

# 2. Complete High-Precision Footer HTML
proper_footer_html = '''  <!-- FOOTER: PROPER AUSPICIOUS LUXURY DESIGN -->
  <footer class="main-footer">
    <!-- Top Sacred Shlokam Accent Band -->
    <div class="footer-top-auspicious-band">
      <span>॥ శ్రీరస్తు - శుభమస్తు - అవిఘ్నమస్తు ॥ • రాయల్ శుభకార్య ఖజానా</span>
    </div>

    <div class="footer-content-wrap">
      <div class="footer-grid">
        
        <!-- Column 1: Brand & Purpose -->
        <div class="footer-brand">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
            <div class="brand-icon-box" style="width: 36px; height: 36px; font-size: 17px;">GV</div>
            <h3>GiftVault</h3>
          </div>
          <div style="font-size: 11px; font-weight: 800; color: var(--c-crimson); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 10px;">
            SHUBH AARAMBH • DIGITAL RED NOTEBOOK
          </div>
          <p data-i18n="footer_about">
            The official modern celebration treasury and digital Red Notebook engineered for Indian weddings, housewarmings, cradle ceremonies, and reception counters worldwide.
          </p>
          <div style="margin-top: 16px; display: inline-flex; align-items: center; gap: 8px; background: #F8F9FA; border: 1.5px solid var(--c-night); padding: 6px 14px; border-radius: 9999px; font-size: 12px; font-weight: 700; color: var(--c-night);">
            <span>🔒</span> <span>100% End-to-End Encrypted Family Cloud</span>
          </div>
        </div>

        <!-- Column 2: Capabilities -->
        <div class="footer-col">
          <h4 data-i18n="nav_capabilities">Capabilities</h4>
          <ul class="footer-links-list">
            <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');"><span>✍️</span> <span data-i18n="cap_1_title">Munshi Rapid Entry</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');"><span>🔄</span> <span data-i18n="cap_2_title">Reciprocity Tracker</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');"><span>📖</span> <span data-i18n="cap_3_title">Digital Red Notebook</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="openPricingModal();"><span>👑</span> <span data-i18n="nav_plans_btn">Celebration Plans (₹49)</span></button></li>
          </ul>
        </div>

        <!-- Column 3: Reception Desk -->
        <div class="footer-col">
          <h4 data-i18n="footer_reception">Reception Desk</h4>
          <ul class="footer-links-list">
            <li><button type="button" class="footer-btn-link" onclick="navToView('login')"><span>🚪</span> <span data-i18n="btn_open_desk">Open Reception Desk</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="enterGuestDemoMode()"><span>👀</span> <span data-i18n="btn_guest_demo">Explore as Guest</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="navToView('hub')"><span>🎪</span> <span data-i18n="hub_title">Family Event Hub</span></button></li>
            <li><button type="button" class="footer-btn-link" onclick="openPrintSlip('GV-101', 'K. Venkata Rao Garu', 'Vijayawada', 'UPI PhonePe', '₹10,116')"><span>🖨️</span> <span>2-inch Slip Preview</span></button></li>
          </ul>
        </div>

        <!-- Column 4: Trust & Regional Heritage -->
        <div class="footer-col">
          <div class="footer-trust-card">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
              <span style="font-size: 20px;">🏛️</span>
              <strong style="font-family: var(--font-serif); font-size: 15px; color: var(--c-night);" data-i18n="footer_trust_head">Sacred Milestone Trust</strong>
            </div>
            <div style="font-size: 12.5px; color: #475569; line-height: 1.5; margin-bottom: 14px;" data-i18n="footer_trust_body">
              Designed for celebration counters in Hyderabad, Vijayawada, Bangalore, Chennai, Mumbai & Indian families worldwide.
            </div>
            <div style="display: flex; gap: 6px; flex-wrap: wrap;">
              <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF; font-size: 10.5px; padding: 4px 8px;">ZERO ADS</span>
              <span class="tag-badge" style="background: var(--c-emerald); color: #FFFFFF; font-size: 10.5px; padding: 4px 8px;">SAFE CLOUD</span>
              <span class="tag-badge" style="background: var(--c-crimson); color: #FFFFFF; font-size: 10.5px; padding: 4px 8px;">LUCKY ₹1 COIN</span>
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

# Replace existing <footer>...</footer> in html
html = re.sub(r'<footer.*?</footer>', proper_footer_html, html, flags=re.DOTALL)

for path in target_files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated Proper Footer in: {path} ({len(html)} bytes)")

print("\nProper footer overhaul complete and synchronized!")
