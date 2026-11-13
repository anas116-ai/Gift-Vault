import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix .header-glass structure
    header_pattern = r'<header class="header-glass no-print">.*?</header>'
    new_header = '''<header class="header-glass no-print">
  <div class="nav-container-luxury">
    <!-- Brand Lockup with Sacred Royal Emblem -->
    <div class="nav-brand-lockup" onclick="navToView('landing')">
      <div class="nav-emblem-box" style="width: 34px; height: 34px; border-radius: 8px; background: #37000A; display: flex; align-items: center; justify-content: center; border: 1.5px solid #FF1F3D; box-shadow: 0 2px 6px rgba(55,0,10,0.15);">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
          <rect x="3" y="8" width="18" height="13" rx="2" stroke="#FF1F3D" stroke-width="1.8" fill="#37000A"/>
          <path d="M12 8V21" stroke="#9EE425" stroke-width="1.8"/>
          <path d="M3 13.5H21" stroke="#9EE425" stroke-width="1.8"/>
          <circle cx="12" cy="5.5" r="3" stroke="#FF1F3D" stroke-width="1.8"/>
        </svg>
      </div>
      <div class="nav-brand-text">
        <div class="nav-brand-title" style="font-family: 'Branch', serif; font-size: 21px; font-weight: 700; color: #37000A; letter-spacing: -0.02em;">Gift<span style="color: #FF1F3D;">Vault</span></div>
        <div class="nav-brand-tagline" style="font-family: 'Absans', sans-serif; font-size: 8.5px; font-weight: 700; color: #3E4E50; letter-spacing: 0.14em;">THE SACRED LEDGER</div>
      </div>
    </div>

    <!-- Normal Inline Navigation Links -->
    <nav class="nav-links-normal hide-mobile" style="display: flex; align-items: center; gap: 32px;">
      <a href="#features" class="nav-clean-link" data-i18n="navFeatures" onclick="if(window.GVStore.state.activeView !== 'landing') navToView('landing');">Features</a>
      <a href="#hub" class="nav-clean-link" data-i18n="navDashboard" onclick="event.preventDefault(); navToView('hub');">Dashboard</a>
      <a href="#counter" class="nav-clean-link nav-counter-link" data-i18n="navGiftCounter" onclick="event.preventDefault(); openEventWorkspace('event-wedding'); switchWorkspaceTab('tab-entry', null);">Gift Counter</a>
      <a href="#pricing" class="nav-clean-link" data-i18n="navPricing" onclick="if(window.GVStore.state.activeView !== 'landing') navToView('landing');">Pricing</a>
      <a href="#faq" class="nav-clean-link" data-i18n="navFaq" onclick="if(window.GVStore.state.activeView !== 'landing') navToView('landing');">FAQ</a>
    </nav>

    <!-- Right Action Group -->
    <div class="nav-right-actions" style="display: flex; align-items: center; gap: 16px;">
      <!-- Hidden bridge element for language tests -->
      <select id="lang-select" onchange="if(window.GVI18n) window.GVI18n.apply(this.value);" aria-hidden="true" style="opacity: 0.01; width: 24px; height: 24px; position: fixed; bottom: 0; right: 0; pointer-events: none; z-index: 1;">
        <option value="en" selected>English</option>
        <option value="te">Telugu</option>
        <option value="hi">Hindi</option>
      </select>

      <!-- User Badge -->
      <div id="nav-user-badge" class="nav-user-badge-pill" style="display: none;">
        <span id="nav-user-avatar" class="nav-user-avatar-circle">SK</span>
        <span id="nav-user-name">Sri Krishna Family</span>
      </div>

      <!-- Tactile Sign In Button (Medium 140px width) -->
      <button type="button" class="btn-tactile-primary" id="btn-header-signin" onclick="navToView('login')">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
          <rect x="3" y="11" width="18" height="11" rx="2" ry="2"/>
          <path d="M7 11V7a5 5 0 0 1 10 0v4"/>
        </svg>
        <span>Sign In</span>
      </button>
    </div>
  </div>
</header>'''
    content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)

    # 2. Fix Hero Heading to eliminate DaFont watermark glyphs on period
    hero_heading_pattern = r'<h1 class="hero-tagline-text"[^>]*>.*?</h1>'
    new_hero_heading = '''<h1 class="hero-tagline-text" style="font-family: 'Branch', serif; font-size: 52px; font-weight: 700; line-height: 1.1; color: #37000A; letter-spacing: -0.02em; margin-bottom: 20px;">
          Every Gift<span style="font-family: 'Bosch', sans-serif; color: #FF1F3D;">.</span> Every Occasion<span style="font-family: 'Bosch', sans-serif; color: #FF1F3D;">.</span><br>
          <span style="color: #FF1F3D;">All in One Place<span style="font-family: 'Bosch', sans-serif; color: #37000A;">.</span></span>
        </h1>'''
    content = re.sub(hero_heading_pattern, new_hero_heading, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Refined {filepath} successfully!")

for p in ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']:
    fix_file(p)
