import os
import re

# 1. NEW LUXURY AURA FOOTER HTML
new_footer_html = '''<footer class="footer-master no-print">
    <div class="container-app">
      
      <!-- Top 4-Column Luxury Grid (Aura.build Standard) -->
      <div class="footer-grid-luxury">
        
        <!-- Col 1: Brand & Sacred Commitment -->
        <div class="footer-col-brand">
          <div class="footer-brand-lockup" onclick="navToView('landing')">
            <div class="footer-emblem-box">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
                <path d="M4 10C4 8.89543 4.89543 8 6 8H18C19.1046 8 20 8.89543 20 10V18C20 19.6569 18.6569 21 17 21H7C5.34315 21 4 19.6569 4 18V10Z" fill="url(#footerEmblemGrad)" stroke="#FFE8A3" stroke-width="1.2"/>
                <path d="M12 8V21" stroke="#FFE8A3" stroke-width="1.6" stroke-linecap="round"/>
                <path d="M4 13.5H20" stroke="#FFE8A3" stroke-width="1.6" stroke-linecap="round"/>
                <path d="M12 8C10.5 8 8 5.5 9.5 4C11 2.5 12 5.5 12 8Z" fill="#FFE8A3"/>
                <path d="M12 8C13.5 8 16 5.5 14.5 4C13 2.5 12 5.5 12 8Z" fill="#F5D061"/>
                <circle cx="12" cy="13.5" r="2.2" fill="#FFFFFF" stroke="#9E1B32" stroke-width="0.8"/>
                <defs>
                  <linearGradient id="footerEmblemGrad" x1="4" y1="8" x2="20" y2="21" gradientUnits="userSpaceOnUse">
                    <stop stop-color="#C41E3A"/>
                    <stop offset="1" stop-color="#7A0C1E"/>
                  </linearGradient>
                </defs>
              </svg>
            </div>
            <div>
              <div class="footer-brand-name">Gift<span class="nav-v-swoosh">V</span>ault</div>
              <div class="footer-brand-tagline">THE SACRED LEDGER</div>
            </div>
          </div>

          <p class="footer-brand-desc">
            The private digital shagun sanctuary honoring sacred Indian family celebrations with immutable offline security.
          </p>

          <div class="footer-trust-chips">
            <span class="footer-chip">🛡️ 256-Bit Encrypted</span>
            <span class="footer-chip">⚡ 100% Offline</span>
            <span class="footer-chip">🖨️ Thermal Ready</span>
          </div>
        </div>

        <!-- Col 2: Curated Clean Celebrations (Royal Wedding & Housewarming Only) -->
        <div class="footer-col-links">
          <h5 class="footer-heading">CELEBRATIONS</h5>
          <div class="footer-links-list">
            <a href="#culture" class="footer-nav-link">Royal Wedding & Reception (రాయల్ వివాహం)</a>
            <a href="#culture" class="footer-nav-link">Auspicious Housewarming (గృహప్రవేశం)</a>
            <a href="#culture" class="footer-nav-link">Baby Shower & Naming (శ్రీమంతం & బారసాల)</a>
            <a href="#culture" class="footer-nav-link">Milestone Birthday Celebrations</a>
          </div>
        </div>

        <!-- Col 3: Clean Plain Language Features -->
        <div class="footer-col-links">
          <h5 class="footer-heading">FEATURES</h5>
          <div class="footer-links-list">
            <a href="#features" class="footer-nav-link">Digital Shagun Ledger (డిజిటల్ శగున్ లెడ్జర్)</a>
            <a href="#features" class="footer-nav-link">Instant 2-Inch Thermal Slips (తక్షణ రసీదు)</a>
            <a href="#features" class="footer-nav-link">Offline Safe Vault Sync (సురక్షిత సింక్)</a>
            <a href="#features" class="footer-nav-link">Family Multi-Desk Access (కుటుంబ భాగస్వామ్యం)</a>
            <a href="#features" class="footer-nav-link">Instant PDF & Excel Reports</a>
          </div>
        </div>

        <!-- Col 4: Family Access Actions with ThreeUI Tactile Buttons -->
        <div class="footer-col-actions">
          <h5 class="footer-heading">FAMILY ACCESS</h5>
          <div class="footer-actions-wrap">
            <button type="button" class="threeui-tactile-btn footer-action-btn" onclick="navToView('login')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              <span>Reception Desk Login</span>
            </button>
            <button type="button" class="btn-footer-secondary" onclick="openHeroDemo()">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              <span>Explore Guest Demo Hub</span>
            </button>
            <div class="footer-audit-note">
              Dedicated 256-bit Local Vault Security
            </div>
          </div>
        </div>

      </div>

      <!-- Bottom Bar -->
      <div class="footer-bottom-bar">
        <div class="footer-copyright">
          © 2026 GiftVault Technologies. Crafted with devotion for Indian family celebrations.
        </div>
        <div class="footer-legal-links">
          <span>Privacy Vault</span>
          <span class="dot-sep">•</span>
          <span>Celebration Terms</span>
          <span class="dot-sep">•</span>
          <span>Security Audit</span>
        </div>
      </div>

    </div>
  </footer>'''

# 2. NEW AURA.BUILD + THREEUI FILMSTRIP CARDS FOR SMART TOOLS
new_smart_tools_html = '''<section id="features" style="padding: 70px 0 60px;">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 48px;">
          <div style="display: inline-block; font-size: 11px; font-weight: 800; color: #9E1B32; background: #FFF5F6; border: 1px solid rgba(158, 27, 50, 0.18); padding: 4px 14px; border-radius: 999px; letter-spacing: 0.12em; text-transform: uppercase;">
            CORE CAPABILITIES
          </div>
          <h2 class="section-title-tactile" style="font-family: 'Outfit', sans-serif; font-size: clamp(28px, 3.2vw, 36px); font-weight: 800; color: #0F172A; margin: 12px 0 8px; letter-spacing: -0.025em;">
            Smart Tools for Every Celebration
          </h2>
          <p style="font-size: 14.5px; color: #475569; line-height: 1.6; margin: 0 auto; max-width: 580px;">
            Engineered with speed, precision, and complete offline security for effortless reception desk management.
          </p>
        </div>

        <div class="aura-filmstrip-grid">
          
          <!-- Card 1: Digital Shagun Ledger -->
          <div class="aura-editorial-card">
            <div class="card-identity-header">
              <div class="card-icon-emblem crimson-theme">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
              </div>
              <span class="card-number-badge">01 / 06 • LEDGER</span>
            </div>
            <h3 class="card-title">Digital Shagun Ledger</h3>
            <p class="card-description">
              Replaces vulnerable paper books with instant guest lookup, native hometown tagging, and verified serial numbers.
            </p>
            <div class="card-footer-status">
              <span class="status-pill-green">✓ Instant Search</span>
              <span class="status-code">Serial #GV-101</span>
            </div>
          </div>

          <!-- Card 2: Sacred Shagun Preserver (Zero Coin Jargon) -->
          <div class="aura-editorial-card">
            <div class="card-identity-header">
              <div class="card-icon-emblem gold-theme">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M14.8 9A2 2 0 0 0 13 8h-2a2 2 0 1 0 0 4h2a2 2 0 1 1 0 4h-2a2 2 0 0 1-1.8-1"/><path d="M12 6v2m0 8v2"/></svg>
              </div>
              <span class="card-number-badge">02 / 06 • TRADITION</span>
            </div>
            <h3 class="card-title">Sacred Shagun Preserver</h3>
            <p class="card-description">
              Respectful traditional shagun recording with automated currency verification and zero calculation errors.
            </p>
            <div class="card-footer-status">
              <span class="status-pill-gold">Traditional Shagun</span>
              <span class="status-code">Zero Math Drift</span>
            </div>
          </div>

          <!-- Card 3: Instant 2-Inch Thermal Slips -->
          <div class="aura-editorial-card">
            <div class="card-identity-header">
              <div class="card-icon-emblem emerald-theme">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
              </div>
              <span class="card-number-badge">03 / 06 • RECEIPTS</span>
            </div>
            <h3 class="card-title">Instant 2-Inch Thermal Slips</h3>
            <p class="card-description">
              Generate instant 2-inch printed acknowledgment slips to slip inside return gift hampers for visiting families.
            </p>
            <div class="card-footer-status">
              <span class="status-pill-green">Bluetooth / USB</span>
              <span class="status-code">Return Gift Bags</span>
            </div>
          </div>

          <!-- Card 4: Family Multi-Desk Access -->
          <div class="aura-editorial-card">
            <div class="card-identity-header">
              <div class="card-icon-emblem crimson-theme">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
              </div>
              <span class="card-number-badge">04 / 06 • MULTI-DESK</span>
            </div>
            <h3 class="card-title">Family Multi-Desk Access</h3>
            <p class="card-description">
              Coordinate up to 4 concurrent reception counters simultaneously with automated serial assignment and zero overlaps.
            </p>
            <div class="card-footer-status">
              <span class="status-pill-green">Simultaneous Entry</span>
              <span class="status-code">Zero Duplication</span>
            </div>
          </div>

          <!-- Card 5: 100% Offline Vault Security -->
          <div class="aura-editorial-card">
            <div class="card-identity-header">
              <div class="card-icon-emblem emerald-theme">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              </div>
              <span class="card-number-badge">05 / 06 • SECURITY</span>
            </div>
            <h3 class="card-title">100% Offline Vault Sync</h3>
            <p class="card-description">
              Operates uninterrupted during convention hall network blackouts with zero cloud leakage and local encrypted persistence.
            </p>
            <div class="card-footer-status">
              <span class="status-pill-green">Offline First</span>
              <span class="status-code">Zero Cloud Leak</span>
            </div>
          </div>

          <!-- Card 6: Executive PDF & Excel Reports -->
          <div class="aura-editorial-card">
            <div class="card-identity-header">
              <div class="card-icon-emblem gold-theme">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
              </div>
              <span class="card-number-badge">06 / 06 • BACKUP</span>
            </div>
            <h3 class="card-title">Instant PDF & Excel Reports</h3>
            <p class="card-description">
              Export beautifully formatted, audit-ready Excel sheets and printable PDFs partitioned by relation, city, and amount.
            </p>
            <div class="card-footer-status">
              <span class="status-pill-gold">1-Click Export</span>
              <span class="status-code">Audit Ready</span>
            </div>
          </div>

        </div>
      </section>'''

target_html_files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for fpath in target_html_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Replace footer
        content = re.sub(r'<footer class="footer-master.*?</footer\s*>', new_footer_html, content, flags=re.DOTALL)
        
        # 2. Replace smart tools section
        content = re.sub(r'<section id="features".*?</section>', new_smart_tools_html, content, flags=re.DOTALL)
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated HTML in: {fpath}")

print("HTML update complete!")
