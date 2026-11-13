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

# Let's replace the CSS <style>...</style> block with a completely pristine, clean, modern design inspired by thenyota.app and sgunms.in!
# First, extract what's between <style> and </style>

new_style = '''<style>
    :root {
      /* Curated Auspicious Royal Palette (Strictly 3 Colors + Clean Canvases) */
      --c-night: #000411;         /* Deep Night Slate - Primary typography, high-contrast badges */
      --c-crimson: #F8333C;       /* Rose Crimson - Primary auspicious CTA, highlights */
      --c-crimson-hover: #D91C25;
      --c-crimson-subtle: #FFF1F2;
      --c-crimson-border: #FECDD3;
      --c-emerald: #036D19;       /* Royal Emerald - Monetary totals, surplus, verified status */
      --c-emerald-subtle: #ECFDF5;
      --c-emerald-border: #A7F3D0;
      
      /* Pure Crisp Canvases & Soft Surfaces (Thenyota / Sgunms standard) */
      --c-base: #F8F9FA;          /* Soft modern canvas background */
      --c-surface: #FFFFFF;       /* Crisp card white */
      --c-surface-hover: #F1F5F9;
      --c-border: #E2E8F0;        /* Subtle, clean border (no harsh 2px black lines) */
      --c-border-hover: #CBD5E1;
      --c-border-strong: #94A3B8;
      
      --c-body-text: #1E293B;     /* Crisp slate body text */
      --c-muted: #64748B;         /* Secondary muted text */
      --c-muted-light: #94A3B8;

      /* Typography Hierarchy (Option B) */
      --font-serif: 'Playfair Display', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;

      /* Refined Elevations & Spring Physics */
      --shadow-xs: 0 1px 2px rgba(0, 4, 17, 0.04);
      --shadow-sm: 0 2px 6px rgba(0, 4, 17, 0.04), 0 1px 2px rgba(0, 4, 17, 0.02);
      --shadow-md: 0 8px 24px -4px rgba(0, 4, 17, 0.06), 0 4px 10px -2px rgba(0, 4, 17, 0.03);
      --shadow-lg: 0 16px 40px -6px rgba(0, 4, 17, 0.08), 0 8px 16px -4px rgba(0, 4, 17, 0.04);
      --shadow-crimson: 0 8px 20px -3px rgba(248, 51, 60, 0.28);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-xl: 24px;
      --radius-full: 9999px;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    body {
      font-family: var(--font-sans);
      background-color: var(--c-base);
      color: var(--c-body-text);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    /* Tabular currency numbers - Perfectly aligned */
    .num-currency {
      font-family: var(--font-sans);
      font-feature-settings: "tnum" 1, "cv02" 1;
      font-variant-numeric: tabular-nums;
      letter-spacing: -0.02em;
    }

    /* Screen Views Management */
    .app-screen-view {
      display: none;
      width: 100%;
    }
    .app-screen-view.active {
      display: block;
      animation: fadeInView 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes fadeInView {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ==========================================
       TOP NAVIGATION BAR (Clean, Frosted Glass)
       ========================================== */
    .main-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--c-border);
      padding: 0 32px;
      height: 72px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      text-decoration: none;
    }
    .brand-icon-box {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: var(--c-night);
      border: 1.5px solid var(--c-crimson);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      font-family: var(--font-serif);
      font-weight: 800;
      font-size: 19px;
      box-shadow: var(--shadow-sm);
    }
    .brand-titles {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 800;
      color: var(--c-night);
      line-height: 1.1;
      letter-spacing: -0.01em;
    }
    .brand-sub {
      font-family: var(--font-sans);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--c-crimson);
    }

    .nav-links-wrap {
      display: flex;
      align-items: center;
      gap: 28px;
    }
    .nav-anchor-btn {
      background: none;
      border: none;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 600;
      color: #475569;
      cursor: pointer;
      transition: color 0.15s ease;
      padding: 6px 0;
    }
    .nav-anchor-btn:hover {
      color: var(--c-crimson);
    }

    .nav-right-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* Multi-Language Dropdown Selector */
    .lang-selector-box {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-sm);
      padding: 6px 12px;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 600;
      color: var(--c-night);
      height: 38px;
      box-shadow: var(--shadow-xs);
    }
    .lang-dropdown {
      border: none;
      background: transparent;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 700;
      color: var(--c-night);
      outline: none;
      cursor: pointer;
    }

    /* Buttons */
    .btn-crimson {
      background: var(--c-crimson);
      color: #FFFFFF;
      border: 1px solid var(--c-crimson);
      padding: 9px 20px;
      border-radius: var(--radius-md);
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      height: 40px;
      box-shadow: var(--shadow-crimson);
    }
    .btn-crimson:hover {
      background: var(--c-crimson-hover);
      transform: translateY(-1px);
      box-shadow: 0 10px 24px -4px rgba(248, 51, 60, 0.4);
    }
    .btn-outline-dark {
      background: #FFFFFF;
      color: var(--c-night);
      border: 1px solid var(--c-border);
      padding: 8px 16px;
      border-radius: var(--radius-md);
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      height: 40px;
      box-shadow: var(--shadow-xs);
    }
    .btn-outline-dark:hover {
      background: var(--c-surface-hover);
      border-color: var(--c-border-hover);
      color: var(--c-night);
    }

    /* Top Back Bar & Floating Pill */
    .page-back-nav-bar {
      width: 100%;
      background: #FFFFFF;
      border-bottom: 1px solid var(--c-border);
      padding: 12px 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .btn-page-back {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #FFFFFF;
      color: var(--c-night);
      border: 1px solid var(--c-border);
      padding: 6px 14px;
      border-radius: var(--radius-sm);
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .btn-page-back:hover {
      background: var(--c-crimson-subtle);
      border-color: var(--c-crimson);
      color: var(--c-crimson);
    }
    .page-breadcrumb {
      font-size: 13px;
      color: var(--c-muted);
    }
    .universal-side-back-btn {
      position: fixed;
      left: 24px;
      bottom: 24px;
      z-index: 999;
      display: none;
      align-items: center;
      gap: 8px;
      background: var(--c-night);
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 10px 18px;
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: var(--shadow-lg);
      transition: all 0.2s ease;
    }
    .universal-side-back-btn:hover {
      background: var(--c-crimson);
      transform: translateX(-3px);
    }

    /* ==========================================
       HERO SECTION (Thenyota / Sgunms Luxury Cleanliness)
       ========================================== */
    .hero-section-wrap {
      max-width: 1240px;
      margin: 0 auto;
      padding: 64px 32px 80px;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 56px;
      align-items: center;
    }
    .hero-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--c-crimson-subtle);
      border: 1px solid var(--c-crimson-border);
      color: var(--c-crimson);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.04em;
      margin-bottom: 20px;
    }
    .hero-dot-indicator {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--c-crimson);
      box-shadow: 0 0 0 3px rgba(248, 51, 60, 0.25);
    }
    .hero-heading {
      font-family: var(--font-serif);
      font-size: 46px;
      font-weight: 800;
      line-height: 1.18;
      color: var(--c-night);
      letter-spacing: -0.02em;
      margin-bottom: 18px;
    }
    .hero-heading em {
      font-style: italic;
      color: var(--c-crimson);
      font-weight: 700;
    }
    .hero-desc {
      font-size: 16.5px;
      line-height: 1.65;
      color: #475569;
      margin-bottom: 32px;
      max-width: 540px;
    }
    .hero-actions-row {
      display: flex;
      gap: 14px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }

    /* Hero Showcase Card - Minimalist High-Craft Preview */
    .hero-showcase-box {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      transition: transform 0.3s ease;
    }
    .showcase-banner-top {
      background: #FAFAFA;
      border-bottom: 1px solid var(--c-border);
      padding: 10px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.06em;
      color: #64748B;
    }
    .showcase-image-holder {
      height: 200px;
      position: relative;
      background: #000;
    }
    .showcase-image-holder img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      opacity: 0.85;
    }
    .showcase-image-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 20%, rgba(0, 4, 17, 0.85) 100%);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 18px 22px;
      color: #FFFFFF;
    }
    .showcase-tag-sub {
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--c-crimson);
      margin-bottom: 3px;
    }
    .showcase-event-heading {
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 800;
      line-height: 1.2;
    }
    .showcase-venue-text {
      font-size: 11.5px;
      color: #E2E8F0;
      margin-top: 3px;
    }
    .showcase-data-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 1px;
      background: var(--c-border);
    }
    .showcase-data-item {
      background: #FFFFFF;
      padding: 14px 18px;
    }
    .showcase-data-label {
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      color: var(--c-muted);
      margin-bottom: 3px;
    }
    .showcase-data-val {
      font-size: 18px;
      font-weight: 800;
      color: var(--c-night);
    }
    .showcase-feed-row {
      background: #FAFAFA;
      border-top: 1px solid var(--c-border);
      padding: 12px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .feed-avatar {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: var(--c-night);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 800;
    }

    /* ==========================================
       SECTIONS & CARDS (Spacious, Clean)
       ========================================== */
    .section-wrap {
      max-width: 1240px;
      margin: 0 auto;
      padding: 80px 32px;
    }
    .section-header-center {
      text-align: center;
      max-width: 680px;
      margin: 0 auto 48px;
    }
    .section-eyebrow {
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--c-crimson);
      display: block;
      margin-bottom: 8px;
    }
    .section-title {
      font-family: var(--font-serif);
      font-size: 34px;
      font-weight: 800;
      color: var(--c-night);
      letter-spacing: -0.01em;
      margin-bottom: 12px;
    }
    .section-desc {
      font-size: 15.5px;
      color: #64748B;
      line-height: 1.6;
    }

    .capabilities-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }
    .cap-card {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-lg);
      padding: 32px 28px;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .cap-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: var(--c-border-hover);
    }
    .cap-icon-box {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: var(--c-crimson-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      margin-bottom: 20px;
    }
    .cap-title {
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 800;
      color: var(--c-night);
      margin-bottom: 8px;
    }
    .cap-desc {
      font-size: 14px;
      color: #64748B;
      line-height: 1.6;
      margin-bottom: 20px;
    }

    /* Comparison Table Wrap */
    .comparison-table-wrap {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }
    .comp-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .comp-table th {
      background: #F8F9FA;
      padding: 16px 24px;
      font-size: 13px;
      font-weight: 700;
      color: var(--c-night);
      border-bottom: 1px solid var(--c-border);
    }
    .comp-table td {
      padding: 16px 24px;
      font-size: 14px;
      border-bottom: 1px solid #F1F5F9;
      color: #334155;
    }

    /* ==========================================
       EVENT HUB (Clean Cards & Top Bar)
       ========================================== */
    .hub-container-wrap {
      max-width: 1200px;
      margin: 0 auto;
      padding: 40px 32px 72px;
    }
    .hub-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 36px;
      flex-wrap: wrap;
      gap: 16px;
    }
    .hub-title-block h1 {
      font-family: var(--font-serif);
      font-size: 32px;
      font-weight: 800;
      color: var(--c-night);
      margin-bottom: 4px;
    }
    .hub-title-block p {
      font-size: 14.5px;
      color: var(--c-muted);
    }
    .events-selection-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 28px;
    }
    .event-selection-card {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .event-selection-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: var(--c-border-hover);
    }
    .event-card-body {
      padding: 22px;
    }

    /* ==========================================
       WORKSPACE / RED NOTEBOOK LEDGER
       ========================================== */
    .ws-header {
      background: #FFFFFF;
      border-bottom: 1px solid var(--c-border);
      padding: 16px 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .ws-event-name {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 800;
      color: var(--c-night);
    }
    .ws-container {
      max-width: 1240px;
      margin: 0 auto;
      padding: 32px 24px 64px;
    }
    .tab-pane {
      display: none;
    }
    .tab-pane.active {
      display: block;
      animation: fadeInView 0.2s ease forwards;
    }

    /* KPIs Grid */
    .kpi-cards-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-bottom: 32px;
    }
    .kpi-card {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-md);
      padding: 20px 22px;
      box-shadow: var(--shadow-xs);
    }
    .kpi-title {
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--c-muted);
      margin-bottom: 6px;
    }
    .kpi-value {
      font-size: 26px;
      font-weight: 800;
      line-height: 1.1;
      color: var(--c-night);
    }
    .kpi-sub {
      font-size: 12px;
      color: var(--c-muted);
      margin-top: 4px;
    }

    /* Munshi Fast Entry Card */
    .munshi-entry-card {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-xl);
      padding: 36px;
      box-shadow: var(--shadow-sm);
      max-width: 820px;
      margin: 0 auto;
    }

    /* Form Fields */
    .form-group-item {
      margin-bottom: 18px;
    }
    .form-label-txt {
      display: block;
      font-family: var(--font-sans);
      font-size: 12.5px;
      font-weight: 700;
      color: var(--c-night);
      margin-bottom: 6px;
    }
    .form-input-field {
      width: 100%;
      height: 44px;
      padding: 10px 14px;
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: var(--radius-sm);
      font-family: var(--font-sans);
      font-size: 14px;
      color: var(--c-night);
      transition: all 0.15s ease;
    }
    .form-input-field:focus {
      border-color: var(--c-crimson) !important;
      outline: none;
      box-shadow: 0 0 0 3px rgba(248, 51, 60, 0.12) !important;
    }

    /* Tag Badges */
    .tag-badge {
      display: inline-flex;
      align-items: center;
      padding: 4px 9px;
      border-radius: var(--radius-full);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    /* Filter Pills */
    .ledger-filter-pills {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .filter-pill {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-size: 12.5px;
      font-weight: 600;
      color: #475569;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .filter-pill:hover {
      background: var(--c-surface-hover);
      color: var(--c-night);
    }
    .filter-pill.active {
      background: var(--c-night);
      color: #FFFFFF;
      border-color: var(--c-night);
    }

    /* Payment Mode Badges in Table */
    .mode-badge {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
    }
    .mode-cash { background: #DCFCE7; color: #166534; }
    .mode-upi { background: #E0E7FF; color: #3730A3; }
    .mode-gold { background: #FEF3C7; color: #92400E; }
    .mode-silver { background: #F1F5F9; color: #475569; }

    /* Buttons inside Table */
    .btn-whatsapp-sm {
      background: #25D366;
      color: #FFFFFF;
      border: none;
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .btn-whatsapp-sm:hover {
      background: #1EBE5D;
    }

    /* Serial Number Tag */
    .serial-num {
      font-family: var(--font-sans);
      font-feature-settings: "tnum";
      font-weight: 700;
      color: var(--c-muted);
      font-size: 12px;
    }

    /* ==========================================
       MODALS (Centered, Clean, Backdrop-blur)
       ========================================== */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 4, 17, 0.6);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-backdrop.active {
      display: flex;
    }
    .modal-card {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-xl);
      width: 100%;
      max-height: 88vh;
      overflow-y: auto;
      box-shadow: 0 24px 48px -12px rgba(0, 4, 17, 0.25);
      padding: 28px;
    }
    .modal-dialog {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-xl);
      width: 100%;
      max-width: 580px;
      max-height: 88vh;
      overflow-y: auto;
      box-shadow: 0 24px 48px -12px rgba(0, 4, 17, 0.25);
    }
    .modal-header {
      padding: 20px 24px;
      border-bottom: 1px solid var(--c-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .modal-header h3 {
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 800;
      color: var(--c-night);
    }
    .modal-body {
      padding: 24px;
    }
    .modal-close-btn {
      background: none;
      border: none;
      font-size: 22px;
      color: var(--c-muted);
      cursor: pointer;
      line-height: 1;
      padding: 4px;
    }
    .modal-close-btn:hover {
      color: var(--c-night);
    }

    /* ==========================================
       FOOTER (Soft Parchment Luxury Standard)
       ========================================== */
    .main-footer {
      background: #F8F9F5;
      color: var(--c-night);
      border-top: 1px solid var(--c-border);
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
      opacity: 0.4;
    }
    .footer-content-wrap {
      max-width: 1240px;
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
      font-size: 24px;
      font-weight: 800;
      color: var(--c-night);
      margin-bottom: 4px;
    }
    .footer-brand p {
      font-size: 13.5px;
      color: #64748B;
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
      color: #475569;
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
      padding: 0;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .footer-btn-link:hover {
      color: var(--c-crimson);
      transform: translateX(3px);
    }
    .footer-trust-card {
      background: #FFFFFF;
      border: 1px solid var(--c-border);
      border-radius: var(--radius-md);
      padding: 18px;
      box-shadow: var(--shadow-xs);
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
    }

    /* ==========================================
       RESPONSIVE BREAKPOINTS (Mobile, Tablet, Desktop)
       ========================================== */
    .form-grid-3 {
      display: grid;
      grid-template-columns: 1.2fr 1fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }
    .form-grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }
    .responsive-split-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }

    @media (max-width: 1080px) {
      .hero-grid {
        grid-template-columns: 1fr !important;
        gap: 40px !important;
      }
      .capabilities-grid {
        grid-template-columns: 1fr 1fr !important;
      }
      .footer-grid {
        grid-template-columns: 1fr 1fr !important;
        gap: 32px !important;
      }
      .kpi-cards-grid {
        grid-template-columns: repeat(2, 1fr) !important;
      }
    }

    @media (max-width: 820px) {
      .form-grid-3,
      .form-grid-2,
      .responsive-split-2 {
        grid-template-columns: 1fr !important;
        gap: 14px !important;
      }
      .capabilities-grid {
        grid-template-columns: 1fr !important;
      }
      .main-nav {
        padding: 0 16px !important;
        height: auto;
        min-height: 64px;
        flex-wrap: wrap;
        gap: 10px;
      }
      .nav-links-wrap {
        display: none !important;
      }
      .nav-right-actions {
        margin-left: auto;
      }
      .hero-section-wrap {
        padding: 40px 20px 56px !important;
      }
      .hero-heading {
        font-size: 34px !important;
      }
      .hub-container-wrap,
      .ws-container {
        padding: 24px 16px 48px !important;
      }
      .events-selection-grid {
        grid-template-columns: 1fr !important;
      }
      .footer-grid {
        grid-template-columns: 1fr !important;
        gap: 24px !important;
      }
      .footer-bottom-bar {
        flex-direction: column;
        align-items: flex-start;
      }
    }

    @media (max-width: 580px) {
      .kpi-cards-grid {
        grid-template-columns: 1fr !important;
      }
      .hero-heading {
        font-size: 28px !important;
      }
      .hero-actions-row {
        flex-direction: column;
      }
      .hero-actions-row .btn-crimson,
      .hero-actions-row .btn-outline-dark {
        width: 100%;
      }
      .page-back-nav-bar {
        padding: 10px 16px !important;
      }
      .page-breadcrumb {
        display: none !important;
      }
      .munshi-entry-card {
        padding: 20px 16px !important;
      }
    }
  </style>'''

# Replace whatever is between <style> and </style> with new_style
old_style_match = re.search(r'<style>.*?</style>', html, re.DOTALL)
if old_style_match:
    html = html[:old_style_match.start()] + new_style + html[old_style_match.end():]
    print("Replaced entire <style> block with pristine, clean luxury design system!")
else:
    print("⚠️ Could not match <style> block!")

# Remove any lingering inline "border: 2px solid var(--c-night)" and replace with clean "border: 1px solid var(--c-border)"
html = html.replace('border: 2px solid var(--c-night);', 'border: 1px solid var(--c-border);')
html = html.replace('border: 2.5px solid var(--c-night);', 'border: 1px solid var(--c-border);')
html = html.replace('border: 1.5px solid var(--c-night);', 'border: 1px solid var(--c-border);')

# Also update any inline background: var(--c-base) inside cards to clean #FFFFFF or #FAFAFA
html = html.replace('background: var(--c-base); border: 1.5px solid var(--c-night);', 'background: #FFFFFF; border: 1px solid var(--c-border);')

# Write back to all target files
for path in target_files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {path} ({len(html)} bytes)")

print("\nSuccessfully deployed Thenyota & Sgunms clean luxury design overhaul!")
