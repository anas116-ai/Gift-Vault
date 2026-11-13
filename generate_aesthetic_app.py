# -*- coding: utf-8 -*-
"""
Generate the aesthetic, light-mode, 60-30-10 celebration master app.
Follows:
- 60% Dominant: Soft warm alabaster/ivory parchment (#FAF8F5, #FFFFFF)
- 30% Structural: Deep espresso warm slate (#1C1917, #57534E, #E7E2DA)
- 10% Accent: Noble Champagne Gold (#B8860B, #C5A059) + Auspicious Kumkum Vermilion (#C2410C)
- Complete Landing Page with sticky nav, interactive hero calculator, 6 Bento cards, comparison table, testimonials, and FAQ.
- Dedicated Login Page with OTP verification simulation & Google login.
- In-App Workspace with 8 functional tabs (Dashboard, Munshi Desk with +₹1 coin, Red Ledger, Expenses, Reciprocity, Invites, Soundbox QR, Settings).
"""

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault (గిఫ్ట్ వాలెట్) • రాయల్ శుభకార్య ఖజానా & డిజిటల్ లెడ్జర్</title>
  
  <!-- Premium Fontshare Fonts: Clash Display, Cabinet Grotesk, Satoshi -->
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@700,600,500&f[]=cabinet-grotesk@800,700,600,500,400&f[]=satoshi@700,500,400&display=swap" rel="stylesheet">
  <!-- Google Fonts: Plus Jakarta Sans, Noto Sans Telugu, Playfair Display -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    /* ============================================================
       60-30-10 RULE AESTHETIC LIGHT PALETTE
       60% Dominant: #FAF8F5 (Ivory Silk Alabaster) & #FFFFFF (Pure Card Surface)
       30% Structural: #1C1917 (Deep Charcoal Espresso) & #57534E (Warm Stone) & #EAE5DD (Border)
       10% Accent Highlight: #B8860B (Noble Polished Gold) & #C2410C (Auspicious Kumkum)
       ============================================================ */
    :root {
      --bg-page: #FAF8F5;
      --bg-surface: #FFFFFF;
      --bg-surface-elevated: #F5EFEB;
      --bg-card: #FFFFFF;
      --bg-card-hover: #FDFBF7;
      
      --text-main: #1C1917;
      --text-muted: #57534E;
      --text-dim: #78716C;
      --border-subtle: #E7E2DA;
      --border-focus: #B8860B;
      
      --gold-primary: #B8860B;
      --gold-light: #D4AF37;
      --gold-surface: #FBF6EC;
      --gold-border: #E8D7B0;
      
      --vermilion: #C2410C;
      --vermilion-surface: #FEF3EE;
      
      --emerald: #15803D;
      --emerald-surface: #ECFDF5;
      
      --shadow-sm: 0 1px 3px rgba(28,25,23,0.05);
      --shadow-md: 0 4px 14px -2px rgba(28,25,23,0.06), 0 2px 6px -1px rgba(28,25,23,0.03);
      --shadow-lg: 0 14px 34px -4px rgba(28,25,23,0.08), 0 4px 12px -2px rgba(28,25,23,0.04);
      --shadow-gold: 0 10px 25px -4px rgba(184,134,11,0.18);
      
      --font-display: 'Clash Display', 'Playfair Display', serif;
      --font-body: 'Plus Jakarta Sans', 'Noto Sans Telugu', sans-serif;
      --font-numbers: 'Cabinet Grotesk', 'Satoshi', sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-page);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    /* Subtle Auspicious Rangoli/Mandala Background Accent */
    .bg-pattern {
      position: fixed;
      inset: 0;
      background-image: radial-gradient(var(--border-subtle) 1px, transparent 1px);
      background-size: 28px 28px;
      opacity: 0.45;
      pointer-events: none;
      z-index: 0;
    }

    /* Ambient Warm Glow */
    .glow-ambient {
      position: fixed;
      top: -150px;
      left: 50%;
      transform: translateX(-50%);
      width: 900px;
      height: 450px;
      background: radial-gradient(circle, rgba(212,175,55,0.09) 0%, rgba(250,248,245,0) 70%);
      pointer-events: none;
      z-index: 0;
    }

    /* ============================================================
       TOP STICKY NAVBAR
       ============================================================ */
    .top-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      transition: all 0.25s ease;
    }
    .nav-container {
      max-width: 1240px;
      margin: 0 auto;
      padding: 14px 24px;
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
    .brand-emblem {
      width: 40px;
      height: 40px;
      background: linear-gradient(135deg, #FAF4E6, #F2E3C6);
      border: 1.5px solid var(--gold-border);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: var(--shadow-sm);
    }
    .brand-title {
      font-family: var(--font-display);
      font-size: 20px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
    }
    .brand-title span {
      color: var(--gold-primary);
    }
    .brand-subtitle {
      font-size: 11px;
      color: var(--text-muted);
      font-weight: 600;
      letter-spacing: 0.04em;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 24px;
    }
    .nav-link {
      color: var(--text-muted);
      text-decoration: none;
      font-size: 14px;
      font-weight: 600;
      transition: color 0.2s ease;
      background: none;
      border: none;
      cursor: pointer;
    }
    .nav-link:hover {
      color: var(--gold-primary);
    }
    .nav-link.active {
      color: var(--gold-primary);
      font-weight: 700;
    }

    /* Buttons */
    .btn-gold {
      background: linear-gradient(135deg, #B8860B, #996515);
      color: #FFFFFF;
      font-weight: 600;
      font-size: 14px;
      padding: 10px 20px;
      border-radius: 9999px;
      border: 1px solid rgba(255,255,255,0.2);
      box-shadow: var(--shadow-gold);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-gold:hover {
      transform: translateY(-1.5px);
      box-shadow: 0 12px 28px -4px rgba(184,134,11,0.28);
    }
    .btn-gold:active {
      transform: translateY(0);
    }

    .btn-outline {
      background: var(--bg-surface);
      color: var(--text-main);
      font-weight: 600;
      font-size: 14px;
      padding: 9px 18px;
      border-radius: 9999px;
      border: 1.5px solid var(--border-subtle);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .btn-outline:hover {
      border-color: var(--gold-primary);
      color: var(--gold-primary);
      background: var(--gold-surface);
    }

    /* Main View Wrapper */
    .master-view {
      position: relative;
      z-index: 1;
      display: none;
    }
    .master-view.active {
      display: block;
      animation: fadeIn 0.3s ease-out;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ============================================================
       HERO SECTION (LANDING)
       ============================================================ */
    .hero-wrap {
      max-width: 1240px;
      margin: 0 auto;
      padding: 56px 24px 72px 24px;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 48px;
      align-items: center;
    }
    @media (max-width: 960px) {
      .hero-grid {
        grid-template-columns: 1fr;
        gap: 36px;
      }
    }

    .pill-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 9999px;
      background: var(--gold-surface);
      border: 1px solid var(--gold-border);
      color: var(--gold-primary);
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 20px;
      box-shadow: var(--shadow-sm);
    }
    .pill-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--gold-primary);
      box-shadow: 0 0 6px rgba(184,134,11,0.6);
    }

    .hero-h1 {
      font-family: var(--font-display);
      font-size: 46px;
      font-weight: 700;
      line-height: 1.18;
      letter-spacing: -0.02em;
      color: var(--text-main);
      margin-bottom: 18px;
    }
    .hero-h1 em {
      font-family: 'Playfair Display', serif;
      font-style: italic;
      color: var(--gold-primary);
      font-weight: 600;
    }

    .hero-desc {
      font-size: 16px;
      line-height: 1.65;
      color: var(--text-muted);
      margin-bottom: 28px;
      max-width: 580px;
    }

    /* Event Category Selector Bar */
    .category-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 32px;
    }
    .cat-btn {
      padding: 8px 16px;
      border-radius: 9999px;
      border: 1px solid var(--border-subtle);
      background: var(--bg-surface);
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .cat-btn:hover {
      border-color: var(--gold-primary);
      color: var(--gold-primary);
    }
    .cat-btn.active {
      background: var(--gold-surface);
      border-color: var(--gold-primary);
      color: var(--gold-primary);
      font-weight: 700;
    }

    /* Interactive Live Shagun Simulator Card */
    .hero-card {
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 20px;
      padding: 28px;
      box-shadow: var(--shadow-lg);
      position: relative;
    }
    .hero-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 28px;
      right: 28px;
      height: 3px;
      background: linear-gradient(90deg, transparent, var(--gold-light), transparent);
    }

    .badge-live {
      background: var(--emerald-surface);
      color: var(--emerald);
      border: 1px solid rgba(21,128,61,0.2);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 9999px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .badge-live::before {
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--emerald);
    }

    .stat-metric-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin: 20px 0;
    }
    .stat-metric-box {
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 14px;
    }
    .stat-label {
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
      margin-bottom: 4px;
    }
    .stat-val {
      font-family: var(--font-numbers);
      font-size: 22px;
      font-weight: 800;
      color: var(--text-main);
    }

    /* Live Calculator Slider inside Hero */
    .calc-slider-box {
      background: var(--gold-surface);
      border: 1px solid var(--gold-border);
      border-radius: 14px;
      padding: 14px 16px;
      margin-top: 18px;
    }
    .slider-header {
      display: flex;
      justify-content: space-between;
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 8px;
    }
    .calc-slider {
      width: 100%;
      accent-color: var(--gold-primary);
      cursor: pointer;
    }

    /* ============================================================
       BENTO FEATURE GRID
       ============================================================ */
    .section-wrap {
      max-width: 1240px;
      margin: 0 auto;
      padding: 48px 24px;
    }
    .section-header {
      text-align: center;
      max-width: 680px;
      margin: 0 auto 48px auto;
    }
    .section-sub {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--gold-primary);
      margin-bottom: 8px;
    }
    .section-title {
      font-family: var(--font-display);
      font-size: 32px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 12px;
    }
    .section-desc {
      font-size: 15px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    .bento-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    @media (max-width: 900px) {
      .bento-grid {
        grid-template-columns: 1fr;
      }
    }

    .bento-card {
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 18px;
      padding: 28px;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .bento-card:hover {
      border-color: var(--gold-border);
      box-shadow: var(--shadow-md);
      transform: translateY(-3px);
    }

    .bento-icon {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      background: var(--gold-surface);
      border: 1px solid var(--gold-border);
      color: var(--gold-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      margin-bottom: 20px;
    }
    .bento-h3 {
      font-family: var(--font-display);
      font-size: 18px;
      font-weight: 700;
      margin-bottom: 8px;
      color: var(--text-main);
    }
    .bento-p {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* Comparison Table: GiftVault vs Old Manual Red Diary */
    .compare-table-box {
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 18px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      margin-top: 32px;
    }
    .compare-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .compare-table th, .compare-table td {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-subtle);
      font-size: 14px;
    }
    .compare-table th {
      background: var(--bg-surface-elevated);
      font-weight: 700;
      color: var(--text-main);
    }
    .compare-table tr:last-child td {
      border-bottom: none;
    }
    .check-yes {
      color: var(--emerald);
      font-weight: 700;
    }
    .check-no {
      color: var(--text-dim);
    }

    /* Footer */
    .footer-wrap {
      border-top: 1px solid var(--border-subtle);
      background: var(--bg-surface);
      padding: 48px 24px;
      margin-top: 64px;
    }
    .footer-content {
      max-width: 1240px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
    }

    /* ============================================================
       DEDICATED LOGIN SCREEN (VIEW 2)
       ============================================================ */
    .login-container {
      max-width: 940px;
      margin: 40px auto;
      padding: 0 24px;
    }
    .login-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 24px;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
    }
    @media (max-width: 768px) {
      .login-grid {
        grid-template-columns: 1fr;
      }
      .login-banner {
        display: none;
      }
    }
    .login-banner {
      background: linear-gradient(135deg, #FBF6EC 0%, #F5EFEB 100%);
      border-right: 1.5px solid var(--border-subtle);
      padding: 48px 36px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .login-form-side {
      padding: 48px 36px;
    }

    .form-group {
      margin-bottom: 20px;
    }
    .form-label {
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 8px;
    }
    .form-input {
      width: 100%;
      padding: 12px 14px;
      border: 1.5px solid var(--border-subtle);
      border-radius: 10px;
      background: var(--bg-page);
      font-family: inherit;
      font-size: 14px;
      color: var(--text-main);
      transition: all 0.2s ease;
    }
    .form-input:focus {
      outline: none;
      border-color: var(--gold-primary);
      background: #FFFFFF;
      box-shadow: 0 0 0 3px rgba(184,134,11,0.12);
    }

    .role-pills {
      display: flex;
      gap: 8px;
      margin-bottom: 20px;
    }
    .role-pill {
      flex: 1;
      text-align: center;
      padding: 10px 8px;
      border: 1.5px solid var(--border-subtle);
      border-radius: 10px;
      background: var(--bg-page);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .role-pill.active {
      border-color: var(--gold-primary);
      background: var(--gold-surface);
      color: var(--gold-primary);
      font-weight: 700;
    }

    /* ============================================================
       IN-APP COMPLETE WORKSPACE (VIEW 3)
       ============================================================ */
    .app-layout {
      max-width: 1280px;
      margin: 0 auto;
      padding: 24px;
    }
    .app-topbar {
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 16px;
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }
    .app-subnav {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 4px;
      margin-bottom: 24px;
      border-bottom: 1.5px solid var(--border-subtle);
    }
    .subnav-btn {
      padding: 10px 18px;
      border: none;
      background: none;
      font-size: 14px;
      font-weight: 600;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2.5px solid transparent;
      margin-bottom: -1.5px;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .subnav-btn:hover {
      color: var(--gold-primary);
    }
    .subnav-btn.active {
      color: var(--gold-primary);
      border-bottom-color: var(--gold-primary);
      font-weight: 700;
    }

    .tab-content {
      display: none;
    }
    .tab-content.active {
      display: block;
      animation: fadeIn 0.25s ease-out;
    }

    /* Munshi Quick Desk Styles */
    .desk-grid {
      display: grid;
      grid-template-columns: 1.2fr 0.8fr;
      gap: 24px;
    }
    @media (max-width: 900px) {
      .desk-grid {
        grid-template-columns: 1fr;
      }
    }
    .desk-card {
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 18px;
      padding: 24px;
      box-shadow: var(--shadow-sm);
    }
    .coin-group {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 10px 0 20px 0;
    }
    .coin-btn {
      padding: 7px 14px;
      border-radius: 9999px;
      border: 1.5px solid var(--gold-border);
      background: var(--gold-surface);
      color: var(--gold-primary);
      font-family: var(--font-numbers);
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .coin-btn:hover {
      background: var(--gold-primary);
      color: #FFFFFF;
      transform: translateY(-1px);
    }

    /* Ledger Table */
    .ledger-table-wrap {
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 16px;
      overflow-x: auto;
      box-shadow: var(--shadow-sm);
    }
    .ledger-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .ledger-table th, .ledger-table td {
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-subtle);
      font-size: 13.5px;
    }
    .ledger-table th {
      background: var(--bg-surface-elevated);
      font-weight: 700;
      color: var(--text-main);
      text-transform: uppercase;
      font-size: 11px;
      letter-spacing: 0.05em;
    }
    .ledger-table tr:hover td {
      background: var(--bg-card-hover);
    }

    /* Soundbox & QR */
    .qr-card-box {
      max-width: 480px;
      margin: 0 auto;
      background: var(--bg-surface);
      border: 1.5px solid var(--gold-border);
      border-radius: 20px;
      padding: 32px;
      text-align: center;
      box-shadow: var(--shadow-md);
    }

    /* Toast Notification */
    .toast-box {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--text-main);
      color: #FFFFFF;
      padding: 12px 22px;
      border-radius: 12px;
      font-size: 14px;
      font-weight: 600;
      box-shadow: var(--shadow-lg);
      display: none;
      z-index: 9999;
      animation: slideUp 0.3s ease;
    }
    @keyframes slideUp {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
  </style>
</head>
<body>

  <!-- Subtle Texture & Ambient Light -->
  <div class="bg-pattern"></div>
  <div class="glow-ambient"></div>

  <!-- ============================================================
       TOP STICKY NAVBAR
       ============================================================ -->
  <header class="top-nav">
    <div class="nav-container">
      <div class="brand-group" onclick="showMasterView('landing')">
        <div class="brand-emblem">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2L3 7v10l9 5 9-5V7l-9-5z"/>
            <path d="M12 22V12"/>
            <path d="M12 12L3 7"/>
            <path d="M12 12l9-5"/>
          </svg>
        </div>
        <div>
          <div class="brand-title">Gift<span>Vault</span></div>
          <div class="brand-subtitle">రాయల్ శుభకార్య ఖజానా</div>
        </div>
      </div>

      <nav class="nav-links">
        <button type="button" class="nav-link active" onclick="showMasterView('landing')">హోమ్ (Home)</button>
        <button type="button" class="nav-link" onclick="scrollToSection('features')">ఫీచర్స్ (Features)</button>
        <button type="button" class="nav-link" onclick="scrollToSection('compare')">ఎర్ర పుస్తకం పోలిక</button>
        <button type="button" class="nav-link" onclick="showMasterView('app'); showTab('desk');">మున్షీ డెస్క్</button>
      </nav>

      <div style="display: flex; gap: 10px; align-items: center;">
        <button type="button" class="btn-outline" onclick="showMasterView('login')">
          లాగిన్ (Sign In)
        </button>
        <button type="button" class="btn-gold" onclick="showMasterView('app'); showTab('dashboard');">
          ఖజానా తెరవండి →
        </button>
      </div>
    </div>
  </header>

  <!-- ============================================================
       VIEW 1: LUXURY AESTHETIC LANDING PAGE
       ============================================================ -->
  <main id="view-landing" class="master-view active">
    <!-- Hero Section -->
    <section class="hero-wrap">
      <div class="hero-grid">
        <div>
          <div class="pill-badge">
            <span class="pill-dot"></span>
            <span>60-30-10 ఏస్తెటిక్ ఎడిషన్ • 100% లైవ్ ఇండియన్ ఫిన్‌టెక్</span>
          </div>

          <h1 class="hero-h1">
            సాంప్రదాయ చదివింపులకు <em>రాయల్ డిజిటల్ ఖజానా</em>.
          </h1>

          <p class="hero-desc">
            వివాహం, బారసాల, లంగా వోణి, ఉపనయనం, గృహప్రవేశం — మీ ఇంటి ప్రతి శుభకార్యానికి వచ్చిన నగదు, బంగారం, వెండి బహుమతుల ఖచ్చితమైన లెక్కలు, +₹1 లక్కీ కాయిన్ రసీదులు, మరియు పూర్తి ఎర్ర పుస్తకం (శగున్ డైరీ).
          </p>

          <!-- Celebration Switcher -->
          <div class="category-pills">
            <button type="button" class="cat-btn active" onclick="switchEventTheme('wedding', this)">💍 వివాహం (Marriage)</button>
            <button type="button" class="cat-btn" onclick="switchEventTheme('birthday', this)">👶 బారసాల / బర్త్‌డే</button>
            <button type="button" class="cat-btn" onclick="switchEventTheme('halfsaree', this)">🪷 హాఫ్ శారీ వేడుక</button>
            <button type="button" class="cat-btn" onclick="switchEventTheme('dhoti', this)">🧵 ఉపనయనం / ధోతి</button>
            <button type="button" class="cat-btn" onclick="switchEventTheme('housewarming', this)">🏡 గృహప్రవేశం</button>
          </div>

          <div style="display: flex; gap: 14px; align-items: center; flex-wrap: wrap;">
            <button type="button" class="btn-gold" onclick="showMasterView('app'); showTab('desk');" style="padding: 13px 28px; font-size: 15px;">
              ⚡ మున్షీ డెస్క్ ప్రారంభించండి (Fast Entry)
            </button>
            <button type="button" class="btn-outline" onclick="showMasterView('login')" style="padding: 13px 24px; font-size: 15px;">
              రాయల్ లాగిన్ (Login)
            </button>
          </div>
        </div>

        <!-- Interactive Hero Showcase Card -->
        <div class="hero-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
            <div style="display: flex; align-items: center; gap: 10px;">
              <span id="hero-event-icon" style="font-size: 28px;">💍</span>
              <div>
                <div id="hero-event-title" style="font-weight: 700; font-size: 17px; color: var(--text-main);">రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం</div>
                <div id="hero-event-sub" style="font-size: 12px; color: var(--text-muted);">వధూవరుల కుటుంబ ఖజానా • హైదరాబాద్</div>
              </div>
            </div>
            <span class="badge-live">లైవ్ ఖజానా</span>
          </div>

          <!-- Metrics -->
          <div class="stat-metric-grid">
            <div class="stat-metric-box">
              <div class="stat-label">మొత్తం చదివింపులు</div>
              <div class="stat-val" id="hero-inflow" style="color: var(--gold-primary);">₹8,42,116</div>
            </div>
            <div class="stat-metric-box">
              <div class="stat-label">ఫంక్షన్ ఖర్చులు</div>
              <div class="stat-val" id="hero-expense" style="color: var(--vermilion);">₹4,15,000</div>
            </div>
            <div class="stat-metric-box">
              <div class="stat-label">నికర మిగులు ఆదా</div>
              <div class="stat-val" id="hero-surplus" style="color: var(--emerald);">+₹4,27,116</div>
            </div>
            <div class="stat-metric-box">
              <div class="stat-label">బంగారం & వెండి</div>
              <div class="stat-val" id="hero-jewel">42.5 గ్రా / 550 గ్రా</div>
            </div>
          </div>

          <!-- Interactive Live Shagun Simulator -->
          <div class="calc-slider-box">
            <div class="slider-header">
              <span>🧮 లైవ్ కాలిక్యులేటర్ (అతిథుల సంఖ్య):</span>
              <strong id="slider-guests-text" style="color: var(--gold-primary);">400 మంది</strong>
            </div>
            <input type="range" class="calc-slider" id="guest-slider" min="50" max="1500" step="25" value="400" oninput="updateGuestEstimate(this.value)">
            <div style="display: flex; justify-content: space-between; font-size: 11px; color: var(--text-dim); margin-top: 6px;">
              <span>50 అతిథులు</span>
              <span>అంచనా చదివింపులు: <strong id="slider-est-amt" style="color: var(--gold-primary);">₹4,00,000</strong></span>
              <span>1500 అతిథులు</span>
            </div>
          </div>

          <div style="margin-top: 18px; padding-top: 14px; border-top: 1px solid var(--border-subtle); display: flex; justify-content: space-between; font-size: 12px; color: var(--text-muted);">
            <span>ఆఖరి ఎంట్రీ: వెంకట్ రావు గారు (విజయవాడ)</span>
            <strong style="color: var(--gold-primary);">+ ₹10,116</strong>
          </div>
        </div>
      </div>
    </section>

    <!-- Bento Features Section -->
    <section id="features" class="section-wrap">
      <div class="section-header">
        <div class="section-sub">అధునాతన సౌలభ్యాలు</div>
        <h2 class="section-title">ఎందుకు ప్రతి కుటుంబం GiftVault నే ఎంచుకుంటుంది?</h2>
        <p class="section-desc">సాంప్రదాయ విలువలకు ఆధునిక ఫిన్‌టెక్ భద్రతను జోడించి రూపొందించబడింది.</p>
      </div>

      <div class="bento-grid">
        <div class="bento-card">
          <div>
            <div class="bento-icon">⚡</div>
            <h3 class="bento-h3">3 సెకన్ల మున్షీ డెస్క్</h3>
            <p class="bento-p">రద్దీ సమయాల్లో క్యూ లేకుండా వేగంగా ఎంట్రీ చేయండి. AP & తెలంగాణ నగరాల ఆటోకంప్లీట్, నగదు / బంగారం / వెండి ఆప్షన్స్.</p>
          </div>
          <div style="margin-top: 18px; font-size: 12px; font-weight: 700; color: var(--gold-primary);">+₹1 లక్కీ కాయిన్ ఆటో-రౌండింగ్ →</div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-icon">📜</div>
            <h3 class="bento-h3">ఎర్ర పుస్తకం (డిజిటల్ లెడ్జర్)</h3>
            <p class="bento-p">గ్రామీణ మరియు నగర సంప్రదాయాల ప్రకారం ఎవరు ఎంత ఇచ్చారు, ఏ వస్తువు సమర్పించారు అనేది ఎక్సెల్ లేదా PDF రూపంలో భద్రం.</p>
          </div>
          <div style="margin-top: 18px; font-size: 12px; font-weight: 700; color: var(--gold-primary);">ఎక్సెల్ & ప్రింట్ ఎక్స్‌పోర్ట్ →</div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-icon">🔊</div>
            <h3 class="bento-h3">UPI QR & స్మార్ట్ సౌండ్‌బాక్స్</h3>
            <p class="bento-p">డైనమిక్ QR కోడ్ స్కాన్ చేసి అతిథులు కానుక పంపిన వెంటనే స్పీకర్ ద్వారా తెలుగులోనే శబ్ద ధృవీకరణ.</p>
          </div>
          <div style="margin-top: 18px; font-size: 12px; font-weight: 700; color: var(--gold-primary);">వెబ్ ఆడియో సిస్టమ్ రెడీ →</div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-icon">📲</div>
            <h3 class="bento-h3">వాట్సాప్ డిజిటల్ రసీదు</h3>
            <p class="bento-p">ఎంట్రీ సేవ్ అయిన వెంటనే అతిథి మొబైల్ వాట్సాప్‌కు కృతజ్ఞతలతో కూడిన అధికారిక డిజిటల్ తాంబూలం పంపవచ్చు.</p>
          </div>
          <div style="margin-top: 18px; font-size: 12px; font-weight: 700; color: var(--gold-primary);">డైరెక్ట్ wa.me ఇంటిగ్రేషన్ →</div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-icon">🔄</div>
            <h3 class="bento-h3">పరస్పర మర్యాదల విశ్లేషణ</h3>
            <p class="bento-p">"వారు మన ఇంట్లో ఎంత ఇచ్చారు? మనం తిరిగి వారి వేడుకకు ఎంత ఇవ్వాలి?" అనే పక్కా లెక్కలతో కూడిన సాంప్రదాయ రికార్డు.</p>
          </div>
          <div style="margin-top: 18px; font-size: 12px; font-weight: 700; color: var(--gold-primary);">Reciprocity Engine →</div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-icon">💸</div>
            <h3 class="bento-h3">ఖర్చులు vs నికర మిగులు</h3>
            <p class="bento-p">కల్యాణ మండపం, భోజనాలు, డెకరేషన్ ఖర్చులను ఎప్పటికప్పుడు సరిచూస్తూ నికర మిగులు లాభాలను రియల్-టైమ్‌లో ట్రాక్ చేయండి.</p>
          </div>
          <div style="margin-top: 18px; font-size: 12px; font-weight: 700; color: var(--gold-primary);">బడ్జెట్ ఆడిట్ టూల్ →</div>
        </div>
      </div>
    </section>

    <!-- Comparison Section -->
    <section id="compare" class="section-wrap">
      <div class="section-header">
        <div class="section-sub">పోలిక (Comparison)</div>
        <h2 class="section-title">పాత కాగితపు పుస్తకం vs రాయల్ GiftVault</h2>
      </div>

      <div class="compare-table-box">
        <table class="compare-table">
          <thead>
            <tr>
              <th>ఫీచర్ / అంశం</th>
              <th>సాంప్రదాయ కాగితపు పుస్తకం</th>
              <th style="color: var(--gold-primary);">GiftVault డిజిటల్ ఖజానా</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>ఎంట్రీ వేగం & స్పీడ్</td>
              <td class="check-no">చేతిరాతతో ఆలస్యం, రద్దీ క్యూలు</td>
              <td class="check-yes">⚡ 3 సెకన్లలో ఫాస్ట్ ఆటోకంప్లీట్</td>
            </tr>
            <tr>
              <td>డేటా భద్రత & బ్యాకప్</td>
              <td class="check-no">పుస్తకం పోతే లెక్కలు మాయం</td>
              <td class="check-yes">🔒 లోకల్ & క్లౌడ్ ఎక్సెల్ బ్యాకప్</td>
            </tr>
            <tr>
              <td>అతిథికి రసీదు అందజేత</td>
              <td class="check-no">ఏమీ ఉండదు (కేవలం నమ్మకం)</td>
              <td class="check-yes">📲 తక్షణమే వాట్సాప్ తాంబూలం రసీదు</td>
            </tr>
            <tr>
              <td>తిరిగి ఎంత ఇవ్వాలనే రికార్డు</td>
              <td class="check-no">పాత పేజీలు వెతుక్కోవాలి</td>
              <td class="check-yes">🔄 ఆటోమేటిక్ మర్యాదల విశ్లేషణ</td>
            </tr>
            <tr>
              <td>ఖర్చుల నికర మిగులు గణన</td>
              <td class="check-no">క్యాలిక్యులేటర్‌తో గంటల పని</td>
              <td class="check-yes">📊 క్షణాల్లో ఆటోమేటిక్ లెక్క</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="section-wrap" style="text-align: center; background: var(--bg-surface); border: 1.5px solid var(--border-subtle); border-radius: 24px; padding: 56px 24px; box-shadow: var(--shadow-md);">
      <h2 style="font-family: var(--font-display); font-size: 32px; font-weight: 700; margin-bottom: 12px;">మీ కుటుంబ వేడుకను ఇప్పుడే నమోదు చేసుకోండి</h2>
      <p style="font-size: 15px; color: var(--text-muted); max-width: 540px; margin: 0 auto 28px auto;">ఎలాంటి డమ్మీ డేటా లేకుండా ఫ్రెష్‌గా మీ మొదటి నిజమైన ఈవెంట్‌ను ప్రారంభించండి.</p>
      <div style="display: flex; gap: 14px; justify-content: center;">
        <button type="button" class="btn-gold" onclick="showMasterView('login')" style="padding: 13px 30px; font-size: 15px;">
          ఉచితంగా ప్రారంభించండి →
        </button>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer-wrap">
      <div class="footer-content">
        <div style="display: flex; align-items: center; gap: 10px;">
          <div class="brand-emblem" style="width: 32px; height: 32px;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2"><path d="M12 2L3 7v10l9 5 9-5V7l-9-5z"/></svg>
          </div>
          <span style="font-weight: 700; font-size: 15px;">GiftVault • రాయల్ శుభకార్య ఖజానా</span>
        </div>
        <div style="font-size: 13px; color: var(--text-muted);">
          © 2026 GiftVault India. Designed with 60-30-10 Aesthetic Standards.
        </div>
      </div>
    </footer>
  </main>

  <!-- ============================================================
       VIEW 2: DEDICATED FULL-PAGE LOGIN
       ============================================================ -->
  <main id="view-login" class="master-view">
    <div class="login-container">
      <div class="login-grid">
        <!-- Banner Side -->
        <div class="login-banner">
          <div>
            <div class="pill-badge" style="background: #FFFFFF;">
              <span class="pill-dot"></span>
              <span>భద్రమైన ప్రవేశం (Secure Access)</span>
            </div>
            <h2 style="font-family: var(--font-display); font-size: 28px; font-weight: 700; color: var(--text-main); margin-bottom: 12px;">
              మీ కుటుంబ ఖాతాలోకి స్వాగతం
            </h2>
            <p style="font-size: 14px; color: var(--text-muted); line-height: 1.6;">
              శుభకార్య యజమానిగా పూర్తి నిర్వహణ చేయండి లేదా మున్షీగా వేగవంతమైన ఎంట్రీలను నమోదు చేయండి.
            </p>
          </div>
          <div style="border-top: 1px solid var(--border-subtle); padding-top: 20px;">
            <div style="font-size: 12px; font-weight: 600; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;">256-బిట్ ఎన్‌క్రిప్షన్</div>
            <div style="font-size: 13px; color: var(--text-muted);">మీ కుటుంబ సంప్రదాయ లెక్కలు పూర్తిగా మీ నియంత్రణలోనే సురక్షితం.</div>
          </div>
        </div>

        <!-- Form Side -->
        <div class="login-form-side">
          <div style="margin-bottom: 24px;">
            <h3 style="font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 6px;">లాగిన్ / సైన్-ఇన్</h3>
            <p style="font-size: 13px; color: var(--text-muted);">OTP లేదా Google ద్వారా సులభంగా లాగిన్ అవ్వండి.</p>
          </div>

          <!-- Role Selector -->
          <div class="form-group">
            <label class="form-label">మీ హోదా (Role)</label>
            <div class="role-pills">
              <div class="role-pill active" onclick="setLoginRole('admin', this)">👑 యజమాని</div>
              <div class="role-pill" onclick="setLoginRole('munshi', this)">⚡ మున్షీ</div>
              <div class="role-pill" onclick="setLoginRole('viewer', this)">👁️ బంధువు</div>
            </div>
          </div>

          <!-- Phone OTP Section -->
          <div id="login-phone-box">
            <div class="form-group">
              <label class="form-label">మొబైల్ నంబర్</label>
              <div style="display: flex; gap: 8px;">
                <span style="background: var(--bg-page); border: 1.5px solid var(--border-subtle); padding: 12px 14px; border-radius: 10px; font-weight: 600; font-size: 14px;">+91</span>
                <input type="tel" id="login-phone" class="form-input" placeholder="98480 12345" value="9848012345" maxlength="10">
              </div>
            </div>
            <button type="button" class="btn-gold" style="width: 100%; justify-content: center; padding: 12px; margin-bottom: 16px;" onclick="sendLoginOTP()">
              OTP కోడ్ పంపండి →
            </button>
          </div>

          <!-- OTP Input Step -->
          <div id="login-otp-box" style="display: none;">
            <div class="form-group">
              <label class="form-label">నమోదు చేసిన మొబైల్ కోడ్ (టెస్ట్ కోడ్: <strong style="color: var(--gold-primary);">1234</strong>)</label>
              <div style="display: flex; gap: 10px; justify-content: center; margin: 12px 0;">
                <input type="text" class="form-input" maxlength="1" value="1" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
                <input type="text" class="form-input" maxlength="1" value="2" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
                <input type="text" class="form-input" maxlength="1" value="3" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
                <input type="text" class="form-input" maxlength="1" value="4" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
              </div>
            </div>
            <button type="button" class="btn-gold" style="width: 100%; justify-content: center; padding: 12px; margin-bottom: 16px;" onclick="verifyAndEnter()">
              ధృవీకరించి ప్రవేశించండి ✓
            </button>
          </div>

          <div style="text-align: center; margin: 14px 0; font-size: 12px; color: var(--text-dim);">లేదా</div>

          <button type="button" class="btn-outline" style="width: 100%; justify-content: center; padding: 11px; margin-bottom: 16px;" onclick="googleQuickSignIn()">
            <svg width="16" height="16" viewBox="0 0 24 24"><path fill="#EA4335" d="M12 5c1.6 0 3 .6 4.1 1.6l3.1-3.1C17.3 1.7 14.8 1 12 1 7.5 1 3.7 3.6 1.9 7.3l3.7 2.9C6.5 7.4 9 5 12 5z"/><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.7-.2-2.3H12v4.5h6.5c-.3 1.5-1.1 2.8-2.4 3.7l3.7 2.9c2.2-2 3.7-5.1 3.7-8.8z"/><path fill="#FBBC05" d="M5.6 14.8c-.2-.7-.4-1.5-.4-2.3 0-.8.2-1.6.4-2.3L1.9 7.3C.7 9.7 0 12.3 0 15s.7 5.3 1.9 7.7l3.7-2.9z"/><path fill="#34A853" d="M12 23c3.2 0 6-1.1 8-3l-3.7-2.9c-1.1.7-2.5 1.2-4.3 1.2-3 0-5.5-2.4-6.4-5.2L1.9 16c1.8 3.7 5.6 7 10.1 7z"/></svg>
            Google ఖాతాతో లాగిన్
          </button>

          <div style="text-align: center;">
            <button type="button" onclick="showMasterView('landing')" style="font-size: 13px; color: var(--text-muted); background: none; border: none; cursor: pointer;">
              ← ల్యాండింగ్ పేజీకి తిరిగి వెళ్లండి
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>

  <!-- ============================================================
       VIEW 3: IN-APP COMPLETE WORKSPACE
       ============================================================ -->
  <main id="view-app" class="master-view">
    <div class="app-layout">
      <!-- App Top Bar -->
      <div class="app-topbar">
        <div style="display: flex; align-items: center; gap: 14px;">
          <div class="brand-emblem" style="width: 38px; height: 38px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2"><path d="M12 2L3 7v10l9 5 9-5V7l-9-5z"/></svg>
          </div>
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span id="app-event-name" style="font-weight: 700; font-size: 16px;">మీ మొదటి శుభకార్యం</span>
              <span class="pill-badge" style="margin: 0; padding: 2px 8px; font-size: 10px;">లైవ్</span>
            </div>
            <div style="font-size: 12px; color: var(--text-muted);">రాయల్ ఖజానా కార్యస్థలి • జీరో డేటా ఫ్రెష్ స్టేట్</div>
          </div>
        </div>

        <div style="display: flex; gap: 10px; align-items: center;">
          <button type="button" class="btn-outline" onclick="openCreateEventModal()" style="font-size: 13px; padding: 8px 14px;">
            + కొత్త వేడుక
          </button>
          <button type="button" class="btn-outline" onclick="showMasterView('landing')" style="font-size: 13px; padding: 8px 14px;">
            హోమ్ పేజీ
          </button>
          <button type="button" class="btn-gold" onclick="showTab('desk')" style="font-size: 13px; padding: 8px 16px;">
            ⚡ ఎంట్రీ డెస్క్
          </button>
        </div>
      </div>

      <!-- App Sub-navigation (8 Tabs) -->
      <div class="app-subnav">
        <button type="button" class="subnav-btn active" onclick="showTab('dashboard', this)">📊 డాష్‌బోర్డ్</button>
        <button type="button" class="subnav-btn" onclick="showTab('desk', this)">✍️ మున్షీ డెస్క్</button>
        <button type="button" class="subnav-btn" onclick="showTab('ledger', this)">📖 ఎర్ర పుస్తకం</button>
        <button type="button" class="subnav-btn" onclick="showTab('expenses', this)">💸 ఖర్చులు & సేవింగ్స్</button>
        <button type="button" class="subnav-btn" onclick="showTab('reciprocity', this)">🔄 మర్యాదలు (Reciprocity)</button>
        <button type="button" class="subnav-btn" onclick="showTab('invites', this)">💌 వాట్సాప్ ఇన్వైట్స్</button>
        <button type="button" class="subnav-btn" onclick="showTab('soundbox', this)">🔔 UPI QR సౌండ్‌బాక్స్</button>
        <button type="button" class="subnav-btn" onclick="showTab('settings', this)">⚙️ సెట్టింగ్స్</button>
      </div>

      <!-- TAB 1: DASHBOARD -->
      <div id="tab-dashboard" class="tab-content active">
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;">
          <div class="stat-metric-box" style="background: var(--bg-surface);">
            <div class="stat-label">మొత్తం ఆదాయం</div>
            <div class="stat-val" id="dash-total" style="color: var(--gold-primary);">₹0</div>
            <div style="font-size: 11px; color: var(--text-dim); margin-top: 4px;">0 ఎంట్రీలు నమోదయ్యాయి</div>
          </div>
          <div class="stat-metric-box" style="background: var(--bg-surface);">
            <div class="stat-label">నగదు (Cash)</div>
            <div class="stat-val" id="dash-cash">₹0</div>
            <div style="font-size: 11px; color: var(--text-dim); margin-top: 4px;">కౌంటర్ బాక్స్ క్యాష్</div>
          </div>
          <div class="stat-metric-box" style="background: var(--bg-surface);">
            <div class="stat-label">ఆన్‌లైన్ (UPI / QR)</div>
            <div class="stat-val" id="dash-upi">₹0</div>
            <div style="font-size: 11px; color: var(--text-dim); margin-top: 4px;">నేరుగా బ్యాంక్ ఖాతాకు</div>
          </div>
          <div class="stat-metric-box" style="background: var(--bg-surface);">
            <div class="stat-label">బంగారం / వెండి</div>
            <div class="stat-val" id="dash-jewel">0g / 0g</div>
            <div style="font-size: 11px; color: var(--text-dim); margin-top: 4px;">బహుమతి ఆభరణాలు</div>
          </div>
        </div>

        <!-- Empty State Prompt -->
        <div id="dash-empty" style="text-align: center; padding: 60px 20px; background: var(--bg-surface); border: 1.5px dashed var(--border-subtle); border-radius: 18px;">
          <div style="font-size: 38px; margin-bottom: 12px;">🪙</div>
          <h3 style="font-family: var(--font-display); font-size: 20px; font-weight: 700; margin-bottom: 6px;">ఖజానా ఖాళీగా ఉంది (Fresh State)</h3>
          <p style="font-size: 14px; color: var(--text-muted); max-width: 440px; margin: 0 auto 20px auto;">మీ వేడుక కానుకలను నమోదు చేయడం కోసం మున్షీ డెస్క్ తెరవండి.</p>
          <button type="button" class="btn-gold" onclick="showTab('desk')">+ మొదటి ఎంట్రీ నమోదు చేయండి</button>
        </div>

        <!-- Recent Table -->
        <div id="dash-table-box" style="display: none;" class="ledger-table-wrap">
          <table class="ledger-table">
            <thead>
              <tr>
                <th>రసీదు నంబర్</th>
                <th>అతిథి పేరు</th>
                <th>గ్రామం / నగరం</th>
                <th>కానుక మొత్తం</th>
                <th>రకం</th>
                <th>వాట్సాప్</th>
              </tr>
            </thead>
            <tbody id="dash-tbody"></tbody>
          </table>
        </div>
      </div>

      <!-- TAB 2: MUNSHI FAST ENTRY DESK -->
      <div id="tab-desk" class="tab-content">
        <div class="desk-grid">
          <!-- Form -->
          <div class="desk-card">
            <h3 style="font-family: var(--font-display); font-size: 19px; font-weight: 700; margin-bottom: 18px; display: flex; align-items: center; gap: 8px;">
              <span>✍️</span> మున్షీ ఫాస్ట్ ఎంట్రీ ఫారం
            </h3>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
              <div class="form-group">
                <label class="form-label">అతిథి పేరు *</label>
                <input type="text" id="desk-name" class="form-input" placeholder="ఉదా: రామారావు గారు">
              </div>
              <div class="form-group">
                <label class="form-label">ఊరు / నగరం</label>
                <input type="text" id="desk-city" class="form-input" placeholder="విజయవాడ, గుంటూరు, హైదరాబాద్" list="cities-list">
                <datalist id="cities-list">
                  <option value="హైదరాబాద్">
                  <option value="విజయవాడ">
                  <option value="విశాఖపట్నం">
                  <option value="గుంటూరు">
                  <option value="వరంగల్">
                  <option value="రాజమండ్రి">
                  <option value="నెల్లూరు">
                  <option value="తిరుపతి">
                </datalist>
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
              <div class="form-group">
                <label class="form-label">మొబైల్ (వాట్సాప్ కోసం)</label>
                <input type="tel" id="desk-phone" class="form-input" placeholder="9848012345">
              </div>
              <div class="form-group">
                <label class="form-label">సంబంధం</label>
                <select id="desk-relation" class="form-input">
                  <option value="బంధువులు">బంధువులు (Relatives)</option>
                  <option value="స్నేహితులు">స్నేహితులు (Friends)</option>
                  <option value="సహోద్యోగులు">సహోద్యోగులు (Colleagues)</option>
                  <option value="శ్రేయోభిలాషి">శ్రేయోభిలాషి (Well Wisher)</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">కానుక రకం</label>
              <div style="display: flex; gap: 10px;">
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--border-subtle); border-radius: 10px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="gift-type" value="CASH" checked onchange="toggleGiftFields('cash')"> 💵 నగదు (Cash)
                </label>
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--border-subtle); border-radius: 10px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="gift-type" value="UPI" onchange="toggleGiftFields('cash')"> 📲 ఆన్‌లైన్ (UPI)
                </label>
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--border-subtle); border-radius: 10px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="gift-type" value="GOLD" onchange="toggleGiftFields('jewel')"> 🥇 బంగారం/వెండి
                </label>
              </div>
            </div>

            <!-- Cash Input with Lucky Coins -->
            <div id="box-cash-entry" class="form-group">
              <label class="form-label">మొత్తం (రూపాయల్లో) *</label>
              <input type="number" id="desk-amount" class="form-input" style="font-size: 20px; font-weight: 700; color: var(--gold-primary);" placeholder="₹ 1116">
              
              <div class="coin-group">
                <button type="button" class="coin-btn" onclick="setQuickAmount(516)">+ ₹516</button>
                <button type="button" class="coin-btn" onclick="setQuickAmount(1116)">+ ₹1,116</button>
                <button type="button" class="coin-btn" onclick="setQuickAmount(2116)">+ ₹2,116</button>
                <button type="button" class="coin-btn" onclick="setQuickAmount(5116)">+ ₹5,116</button>
                <button type="button" class="coin-btn" onclick="setQuickAmount(10116)">+ ₹10,116</button>
                <button type="button" class="coin-btn" onclick="addLuckyOne()">+ ₹1 కాయిన్</button>
              </div>
            </div>

            <!-- Jewel Input Box -->
            <div id="box-jewel-entry" class="form-group" style="display: none;">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div>
                  <label class="form-label">బంగారం (గ్రాముల్లో)</label>
                  <input type="number" step="0.1" id="desk-gold" class="form-input" placeholder="ఉదా: 8.0">
                </div>
                <div>
                  <label class="form-label">వెండి (గ్రాముల్లో)</label>
                  <input type="number" step="1" id="desk-silver" class="form-input" placeholder="ఉదా: 100">
                </div>
              </div>
            </div>

            <div style="display: flex; gap: 12px; margin-top: 14px;">
              <button type="button" class="btn-gold" style="flex: 1; justify-content: center; padding: 13px;" onclick="saveDeskEntry()">
                💾 ఎంట్రీ భద్రపరచండి (Save Entry)
              </button>
              <button type="button" class="btn-outline" onclick="clearDeskForm()">
                క్లియర్
              </button>
            </div>
          </div>

          <!-- Quick Receipts & Audio Preview -->
          <div class="desk-card" style="display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <h4 style="font-family: var(--font-display); font-size: 16px; font-weight: 700; margin-bottom: 14px;">
                🔔 మున్షీ సౌండ్ & స్మార్ట్ టిక్కర్
              </h4>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6; margin-bottom: 16px;">
                ప్రతి ఎంట్రీ నమోదు కాగానే ఆటోమేటిక్‌గా వెబ్ ఆడియో సిస్టమ్ ధ్వని వినిపిస్తుంది.
              </p>
              
              <div style="background: var(--gold-surface); border: 1px solid var(--gold-border); border-radius: 12px; padding: 14px; margin-bottom: 16px;">
                <div style="font-size: 12px; font-weight: 600; color: var(--gold-primary); margin-bottom: 4px;">ఆఖరి నమోదు రసీదు:</div>
                <div id="last-receipt-preview" style="font-size: 14px; font-weight: 700; color: var(--text-main);">ఇంకా ఏమీ నమోదు కాలేదు</div>
              </div>
            </div>

            <button type="button" class="btn-outline" style="width: 100%; justify-content: center;" onclick="testSound()">
              🔊 సౌండ్‌బాక్స్ టెస్ట్ చేయండి
            </button>
          </div>
        </div>
      </div>

      <!-- TAB 3: RED BOOK LEDGER -->
      <div id="tab-ledger" class="tab-content">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 12px;">
          <div>
            <h3 style="font-family: var(--font-display); font-size: 20px; font-weight: 700;">📖 ఎర్ర పుస్తకం (డిజిటల్ శగున్ లెడ్జర్)</h3>
            <p style="font-size: 13px; color: var(--text-muted);">పూర్తి చదివింపుల వివరాలు మరియు రికార్డులు</p>
          </div>
          <div style="display: flex; gap: 10px;">
            <button type="button" class="btn-outline" onclick="exportToCSV()">📥 ఎక్సెల్ (CSV) డౌన్‌లోడ్</button>
            <button type="button" class="btn-gold" onclick="window.print()">🖨️ ప్రింట్ రిపోర్ట్</button>
          </div>
        </div>

        <div class="ledger-table-wrap">
          <table class="ledger-table">
            <thead>
              <tr>
                <th>క్రమ సంఖ్య</th>
                <th>రశీదు సంఖ్య</th>
                <th>పేరు</th>
                <th>ఊరు</th>
                <th>సంబంధం</th>
                <th>కానుక మొత్తం</th>
                <th>బంగారం/వెండి</th>
                <th>రకం</th>
                <th>చర్య</th>
              </tr>
            </thead>
            <tbody id="ledger-tbody">
              <tr>
                <td colspan="9" style="text-align: center; color: var(--text-dim); padding: 32px;">ఇంకా ఎలాంటి రికార్డులు నమోదు కాలేదు.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TAB 4: EXPENSES -->
      <div id="tab-expenses" class="tab-content">
        <div class="desk-grid">
          <div class="desk-card">
            <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 16px;">💸 ఫంక్షన్ ఖర్చు నమోదు</h3>
            <div class="form-group">
              <label class="form-label">ఖర్చు కేటగిరీ</label>
              <select id="exp-category" class="form-input">
                <option value="కల్యాణ మండపం / వేదిక">కల్యాణ మండపం / వేదిక</option>
                <option value="క్యాటరింగ్ / భోజనాలు">క్యాటరింగ్ / భోజనాలు</option>
                <option value="డెకరేషన్ & లైటింగ్">డెకరేషన్ & లైటింగ్</option>
                <option value="ఫోటో & వీడియోగ్రఫీ">ఫోటో & వీడియోగ్రఫీ</option>
                <option value="బాజా భజంత్రీలు / సంగీతం">బాజా భజంత్రీలు / సంగీతం</option>
                <option value="ఇతర ఖర్చులు">ఇతర ఖర్చులు</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">వివరాలు / నోట్స్</label>
              <input type="text" id="exp-notes" class="form-input" placeholder="ఉదా: అడ్వాన్స్ అమౌంట్ చెల్లింపు">
            </div>
            <div class="form-group">
              <label class="form-label">మొత్తం (రూపాయల్లో) *</label>
              <input type="number" id="exp-amount" class="form-input" placeholder="₹ 50000">
            </div>
            <button type="button" class="btn-gold" style="width: 100%; justify-content: center; padding: 12px;" onclick="saveExpense()">
              + ఖర్చును జోడించండి
            </button>
          </div>

          <div class="desk-card">
            <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 16px;">📊 ఖర్చులు vs నికర మిగులు</h3>
            <div class="stat-metric-box" style="margin-bottom: 12px;">
              <div class="stat-label">మొత్తం ఆదాయం</div>
              <div class="stat-val" id="exp-sum-inflow" style="color: var(--gold-primary);">₹0</div>
            </div>
            <div class="stat-metric-box" style="margin-bottom: 12px;">
              <div class="stat-label">మొత్తం ఖర్చులు</div>
              <div class="stat-val" id="exp-sum-outflow" style="color: var(--vermilion);">₹0</div>
            </div>
            <div class="stat-metric-box">
              <div class="stat-label">నికర మిగులు ఆదా</div>
              <div class="stat-val" id="exp-net-surplus" style="color: var(--emerald);">₹0</div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 5: RECIPROCITY -->
      <div id="tab-reciprocity" class="tab-content">
        <div class="desk-card" style="margin-bottom: 24px;">
          <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 12px;">🔄 పరస్పర మర్యాదల విశ్లేషణ (Reciprocity Tracker)</h3>
          <p style="font-size: 14px; color: var(--text-muted); line-height: 1.6;">
            గతంలో మన శుభకార్యానికి ఎవరు ఎంత ఇచ్చారు? భవిష్యత్తులో మనం వారి వేడుకకు ఎంత తిరిగి ఇవ్వాలి? అనే లెక్కలను ఇక్కడ సరిచూసుకోవచ్చు.
          </p>
        </div>
        <div class="ledger-table-wrap">
          <table class="ledger-table">
            <thead>
              <tr>
                <th>వ్యక్తి పేరు</th>
                <th>ఊరు</th>
                <th>వారు మనకిచ్చింది</th>
                <th>మనం తిరిగి ఇవ్వవలసిన సిఫార్సు (+₹1)</th>
                <th>స్థితి</th>
              </tr>
            </thead>
            <tbody id="recip-tbody">
              <tr>
                <td colspan="5" style="text-align: center; color: var(--text-dim); padding: 32px;">ఎంట్రీలు నమోదు కాగానే ఇక్కడ ఆటోమేటిక్‌గా విశ్లేషణ కనిపిస్తుంది.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TAB 6: WHATSAPP INVITES -->
      <div id="tab-invites" class="tab-content">
        <div class="desk-grid">
          <div class="desk-card">
            <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 14px;">💌 వాట్సాప్ శుభలేఖ & తాంబూలం</h3>
            <div class="form-group">
              <label class="form-label">అతిథి మొబైల్ సంఖ్య</label>
              <input type="tel" id="wa-phone" class="form-input" placeholder="9848012345">
            </div>
            <div class="form-group">
              <label class="form-label">సందేశం టెంప్లేట్</label>
              <textarea id="wa-message" class="form-input" rows="4" style="resize: vertical;">మా కుటుంబ శుభకార్యానికి విచ్చేసి వధూవరులను ఆశీర్వదించినందుకు మరియు మీ ప్రేమపూర్వక చదివింపులకు మా హృదయపూర్వక ధన్యవాదాలు! - GiftVault డిజిటల్ రసీదు</textarea>
            </div>
            <button type="button" class="btn-gold" style="width: 100%; justify-content: center; padding: 12px;" onclick="sendWhatsAppDirect()">
              📲 వాట్సాప్‌లో సందేశం పంపండి
            </button>
          </div>
          <div class="desk-card">
            <h4 style="font-family: var(--font-display); font-size: 16px; font-weight: 700; margin-bottom: 12px;">నమూనా ప్రివ్యూ</h4>
            <div style="background: var(--gold-surface); border: 1.5px solid var(--gold-border); border-radius: 14px; padding: 18px; font-size: 13px; line-height: 1.6; color: var(--text-main);">
              🙏 <strong>శుభకార్య కృతజ్ఞతలు</strong><br>
              శ్రీయుతులు: రామారావు గారు (విజయవాడ)<br>
              కానుక: ₹5,116 • రసీదు సంఖ్య: #GV-101<br><br>
              మీ రాక మాకెంతో సంతోషాన్నిచ్చింది!
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 7: SOUNDBOX QR -->
      <div id="tab-soundbox" class="tab-content">
        <div class="qr-card-box">
          <div class="pill-badge" style="margin-bottom: 14px;">
            <span class="pill-dot"></span>
            <span>లైవ్ UPI కౌంటర్ సౌండ్‌బాక్స్</span>
          </div>
          <h3 style="font-family: var(--font-display); font-size: 20px; font-weight: 700; margin-bottom: 6px;">స్కాన్ చేసి కానుకను పంపండి</h3>
          <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">మొబైల్ ఫోన్‌పే, గూగుల్‌పే, పేటీఎం ద్వారా నేరుగా జమ చేయవచ్చు.</p>

          <div style="background: #FFFFFF; padding: 16px; border: 1.5px solid var(--border-subtle); border-radius: 16px; display: inline-block; margin-bottom: 18px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=upi://pay?pa=giftvault@hdfcbank&am=1116&cu=INR" alt="UPI QR" style="display: block; border-radius: 8px;">
          </div>

          <div style="font-weight: 700; font-size: 15px; margin-bottom: 4px;">UPI ID: giftvault@hdfcbank</div>
          <div style="font-size: 12px; color: var(--text-dim); margin-bottom: 20px;">స్కాన్ చేసి చెల్లించిన వెంటనే ఆడియో అలర్ట్ వస్తుంది</div>

          <button type="button" class="btn-gold" style="width: 100%; justify-content: center;" onclick="simulateQRPayment()">
            🔔 చెల్లింపును ధ్వనితో ధృవీకరించండి (Simulate)
          </button>
        </div>
      </div>

      <!-- TAB 8: SETTINGS -->
      <div id="tab-settings" class="tab-content">
        <div class="desk-card" style="max-width: 640px; margin: 0 auto;">
          <h3 style="font-family: var(--font-display); font-size: 20px; font-weight: 700; margin-bottom: 18px;">⚙️ ఖజానా సెట్టింగ్స్</h3>
          
          <div class="form-group">
            <label class="form-label">శుభకార్యం పేరు</label>
            <input type="text" id="setting-event-name" class="form-input" value="రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం">
          </div>

          <div class="form-group">
            <label class="form-label">యజమాని సంప్రదింపు నంబర్</label>
            <input type="tel" id="setting-phone" class="form-input" value="9848012345">
          </div>

          <div class="form-group">
            <label class="form-label">లక్కీ కాయిన్ డీఫాల్ట్ రౌండింగ్</label>
            <select class="form-input">
              <option value="1">+ ₹1 లక్కీ కాయిన్ (116, 516, 1116)</option>
              <option value="0">సాధారణ రౌండింగ్ (500, 1000)</option>
            </select>
          </div>

          <div style="border-top: 1px solid var(--border-subtle); padding-top: 20px; margin-top: 20px;">
            <button type="button" class="btn-outline" style="color: var(--vermilion); border-color: var(--vermilion);" onclick="resetAllData()">
              🗑️ డేటాను పూర్తిగా రీసెట్ చేయండి (Fresh ₹0 State)
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>

  <!-- Toast Element -->
  <div id="toast" class="toast-box"></div>

  <!-- Client-side Logic -->
  <script>
    // State Store
    let APP_STATE = {
      entries: [],
      expenses: [],
      currentRole: 'admin',
      eventName: 'రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం'
    };

    // Load from LocalStorage
    try {
      const saved = localStorage.getItem('GIFTVAULT_AESTHETIC_DATA');
      if (saved) {
        const parsed = JSON.parse(saved);
        APP_STATE.entries = parsed.entries || [];
        APP_STATE.expenses = parsed.expenses || [];
      }
    } catch(e) {}

    function persistState() {
      try {
        localStorage.setItem('GIFTVAULT_AESTHETIC_DATA', JSON.stringify({
          entries: APP_STATE.entries,
          expenses: APP_STATE.expenses
        }));
      } catch(e) {}
      renderAll();
    }

    // Navigation Switcher
    function showMasterView(viewId) {
      document.querySelectorAll('.master-view').forEach(v => v.classList.remove('active'));
      const target = document.getElementById('view-' + viewId);
      if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
      document.querySelectorAll('.nav-link').forEach(btn => btn.classList.remove('active'));
    }

    function showTab(tabId, el) {
      document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.subnav-btn').forEach(b => b.classList.remove('active'));
      const target = document.getElementById('tab-' + tabId);
      if (target) target.classList.add('active');
      if (el) el.classList.add('active');
    }

    function scrollToSection(id) {
      showMasterView('landing');
      setTimeout(() => {
        const el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    }

    function toast(msg) {
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.style.display = 'block';
      setTimeout(() => { t.style.display = 'none'; }, 3200);
    }

    // Web Audio Soundbox chime
    function playChime() {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.type = 'sine';
        osc.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
        osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.15); // A5
        gain.gain.setValueAtTime(0.4, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.8);
        osc.start();
        osc.stop(ctx.currentTime + 0.85);
      } catch(e) {}
    }

    function testSound() {
      playChime();
      toast('🔊 సౌండ్‌బాక్స్ టెస్ట్ శబ్దం వినిపించింది!');
    }

    // Switch Event Theme on Hero
    const EVENT_THEMES = {
      wedding: { title: 'రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం', sub: 'వధూవరుల కుటుంబ ఖజానా • హైదరాబాద్', icon: '💍', inflow: '₹8,42,116', exp: '₹4,15,000', sur: '+₹4,27,116' },
      birthday: { title: 'అద్వైత్ మొదటి పుట్టినరోజు & బారసాల', sub: 'కుటుంబ వేడుక • గుంటూరు', icon: '👶', inflow: '₹3,18,116', exp: '₹1,20,000', sur: '+₹1,98,116' },
      halfsaree: { title: 'సహస్ర లంగా వోణి (హాఫ్ శారీ) వేడుక', sub: 'శుభకార్య ఖజానా • విజయవాడ', icon: '🪷', inflow: '₹5,62,116', exp: '₹2,50,000', sur: '+₹3,12,116' },
      dhoti: { title: 'సాయి చరణ్ ఉపనయన మహోత్సవం', sub: 'వైదిక వేడుక • వరంగల్', icon: '🧵', inflow: '₹4,11,116', exp: '₹1,80,000', sur: '+₹2,31,116' },
      housewarming: { title: 'శ్రీ నిలయం గృహప్రవేశ మహోత్సవం', sub: 'కొత్త ఇల్లు • విశాఖపట్నం', icon: '🏡', inflow: '₹6,75,116', exp: '₹3,10,000', sur: '+₹3,65,116' }
    };

    function switchEventTheme(key, btn) {
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const data = EVENT_THEMES[key];
      if (data) {
        document.getElementById('hero-event-title').innerText = data.title;
        document.getElementById('hero-event-sub').innerText = data.sub;
        document.getElementById('hero-event-icon').innerText = data.icon;
        document.getElementById('hero-inflow').innerText = data.inflow;
        document.getElementById('hero-expense').innerText = data.exp;
        document.getElementById('hero-surplus').innerText = data.sur;
      }
    }

    // Guest Estimate Slider
    function updateGuestEstimate(val) {
      document.getElementById('slider-guests-text').innerText = val + ' మంది';
      const est = Math.round(val * 1000);
      document.getElementById('slider-est-amt').innerText = '₹' + est.toLocaleString('en-IN');
    }

    // Login logic
    function setLoginRole(role, el) {
      APP_STATE.currentRole = role;
      document.querySelectorAll('.role-pill').forEach(p => p.classList.remove('active'));
      if (el) el.classList.add('active');
    }

    function sendLoginOTP() {
      const phone = document.getElementById('login-phone').value.trim();
      if (!phone || phone.length < 10) {
        toast('దయచేసి సరైన 10 అంకెల మొబైల్ నంబర్ ఎంటర్ చేయండి.');
        return;
      }
      document.getElementById('login-phone-box').style.display = 'none';
      document.getElementById('login-otp-box').style.display = 'block';
      toast('టెస్ట్ OTP కోడ్: 1234 పంపబడింది!');
    }

    function verifyAndEnter() {
      toast('ధృవీకరణ విజయవంతమైంది! ఖజానాలోకి ప్రవేశిస్తున్నారు...');
      setTimeout(() => {
        showMasterView('app');
        showTab('dashboard');
      }, 500);
    }

    function googleQuickSignIn() {
      toast('Google ద్వారా విజయవంతంగా సైన్-ఇన్ అయ్యారు!');
      setTimeout(() => {
        showMasterView('app');
        showTab('dashboard');
      }, 500);
    }

    // Munshi Fast Desk Entry
    function setQuickAmount(amt) {
      document.getElementById('desk-amount').value = amt;
    }

    function addLuckyOne() {
      const f = document.getElementById('desk-amount');
      let val = parseInt(f.value) || 0;
      if (val % 10 === 0) val += 1;
      else if (val % 100 === 0) val += 16;
      else val += 1;
      f.value = val;
    }

    function toggleGiftFields(mode) {
      if (mode === 'jewel') {
        document.getElementById('box-cash-entry').style.display = 'none';
        document.getElementById('box-jewel-entry').style.display = 'block';
      } else {
        document.getElementById('box-cash-entry').style.display = 'block';
        document.getElementById('box-jewel-entry').style.display = 'none';
      }
    }

    function saveDeskEntry() {
      const name = document.getElementById('desk-name').value.trim();
      const city = document.getElementById('desk-city').value.trim() || 'స్థానిక';
      const phone = document.getElementById('desk-phone').value.trim();
      const relation = document.getElementById('desk-relation').value;
      const type = document.querySelector('input[name="gift-type"]:checked').value;

      let amount = 0;
      let gold = 0;
      let silver = 0;

      if (type === 'GOLD') {
        gold = parseFloat(document.getElementById('desk-gold').value) || 0;
        silver = parseFloat(document.getElementById('desk-silver').value) || 0;
        if (gold <= 0 && silver <= 0) {
          toast('దయచేసి బంగారం లేదా వెండి బరువును నమోదు చేయండి.');
          return;
        }
      } else {
        amount = parseInt(document.getElementById('desk-amount').value) || 0;
        if (amount <= 0) {
          toast('దయచేసి చెల్లుబాటు అయ్యే నగదు మొత్తాన్ని నమోదు చేయండి.');
          return;
        }
      }

      if (!name) {
        toast('దయచేసి అతిథి పేరు నమోదు చేయండి.');
        return;
      }

      const receiptNo = 'GV-' + (100 + APP_STATE.entries.length + 1);
      const entry = {
        id: Date.now(),
        receiptNo,
        name,
        city,
        phone,
        relation,
        type,
        amount,
        gold,
        silver,
        date: new Date().toLocaleTimeString('te-IN', { hour: '2-digit', minute: '2-digit' })
      };

      APP_STATE.entries.unshift(entry);
      persistState();
      playChime();

      document.getElementById('last-receipt-preview').innerText = `${name} (${city}) - ${amount > 0 ? '₹' + amount.toLocaleString('en-IN') : gold + 'g గోల్డ్'} [${receiptNo}]`;
      toast(`రశీదు #${receiptNo} విజయవంతంగా నమోదైంది!`);
      clearDeskForm();
    }

    function clearDeskForm() {
      document.getElementById('desk-name').value = '';
      document.getElementById('desk-city').value = '';
      document.getElementById('desk-phone').value = '';
      document.getElementById('desk-amount').value = '';
      document.getElementById('desk-gold').value = '';
      document.getElementById('desk-silver').value = '';
    }

    // Expense Save
    function saveExpense() {
      const cat = document.getElementById('exp-category').value;
      const notes = document.getElementById('exp-notes').value.trim();
      const amt = parseInt(document.getElementById('exp-amount').value) || 0;
      if (amt <= 0) {
        toast('దయచేసి సరైన ఖర్చు మొత్తాన్ని నమోదు చేయండి.');
        return;
      }
      APP_STATE.expenses.push({ id: Date.now(), cat, notes, amt });
      persistState();
      toast('ఖర్చు విజయవంతంగా నమోదైంది!');
      document.getElementById('exp-notes').value = '';
      document.getElementById('exp-amount').value = '';
    }

    function resetAllData() {
      if (confirm('మీరు ఖజానాలోని అన్ని రికార్డులను క్లియర్ చేసి ఫ్రెష్ ₹0 స్టేట్‌లోకి మార్చాలనుకుంటున్నారా?')) {
        APP_STATE.entries = [];
        APP_STATE.expenses = [];
        persistState();
        toast('డేటా పూర్తిగా రీసెట్ చేయబడింది! ఫ్రెష్ ఖజానా సిద్ధం.');
      }
    }

    function exportToCSV() {
      if (APP_STATE.entries.length === 0) {
        toast('ఎక్స్‌పోర్ట్ చేయడానికి ఎలాంటి ఎంట్రీలు లేవు.');
        return;
      }
      let csv = "\uFEFFరసీదు,పేరు,ఊరు,సంబంధం,కానుక మొత్తం,బంగారం,వెండి,రకం,సమయం\n";
      APP_STATE.entries.forEach(e => {
        csv += `"${e.receiptNo}","${e.name}","${e.city}","${e.relation}",${e.amount},${e.gold},${e.silver},"${e.type}","${e.date}"\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `GiftVault_Erra_Pusthakam_${Date.now()}.csv`;
      a.click();
      toast('ఎక్సెల్ (CSV) ఫైల్ డౌన్‌లోడ్ ప్రారంభమైంది!');
    }

    function sendWhatsAppDirect() {
      const phone = document.getElementById('wa-phone').value.trim();
      const msg = document.getElementById('wa-message').value.trim();
      if (!phone) {
        toast('దయచేసి అతిథి ఫోన్ నంబర్ నమోదు చేయండి.');
        return;
      }
      const cleanPhone = phone.replace(/[^0-9]/g, '');
      const url = `https://wa.me/91${cleanPhone}?text=${encodeURIComponent(msg)}`;
      window.open(url, '_blank');
    }

    function simulateQRPayment() {
      playChime();
      toast('🔔 ₹1,116 జమ అయ్యింది! వాయిస్ సౌండ్‌బాక్స్ ధృవీకరించబడింది.');
    }

    // Render Function
    function renderAll() {
      let total = 0, cash = 0, upi = 0, goldTotal = 0, silverTotal = 0;
      APP_STATE.entries.forEach(e => {
        total += e.amount || 0;
        if (e.type === 'CASH') cash += e.amount || 0;
        if (e.type === 'UPI') upi += e.amount || 0;
        goldTotal += e.gold || 0;
        silverTotal += e.silver || 0;
      });

      let totalExp = 0;
      APP_STATE.expenses.forEach(x => { totalExp += x.amt || 0; });
      const surplus = total - totalExp;

      // Dashboard
      document.getElementById('dash-total').innerText = '₹' + total.toLocaleString('en-IN');
      document.getElementById('dash-cash').innerText = '₹' + cash.toLocaleString('en-IN');
      document.getElementById('dash-upi').innerText = '₹' + upi.toLocaleString('en-IN');
      document.getElementById('dash-jewel').innerText = `${goldTotal}g / ${silverTotal}g`;

      // Expenses Tab
      document.getElementById('exp-sum-inflow').innerText = '₹' + total.toLocaleString('en-IN');
      document.getElementById('exp-sum-outflow').innerText = '₹' + totalExp.toLocaleString('en-IN');
      document.getElementById('exp-net-surplus').innerText = (surplus >= 0 ? '+₹' : '-₹') + Math.abs(surplus).toLocaleString('en-IN');

      // Empty vs Table state
      const emptyDiv = document.getElementById('dash-empty');
      const tableBox = document.getElementById('dash-table-box');
      const dashTbody = document.getElementById('dash-tbody');
      const ledgerTbody = document.getElementById('ledger-tbody');
      const recipTbody = document.getElementById('recip-tbody');

      if (APP_STATE.entries.length === 0) {
        emptyDiv.style.display = 'block';
        tableBox.style.display = 'none';
        ledgerTbody.innerHTML = '<tr><td colspan="9" style="text-align: center; color: var(--text-dim); padding: 32px;">ఇంకా ఎలాంటి రికార్డులు నమోదు కాలేదు.</td></tr>';
        recipTbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: var(--text-dim); padding: 32px;">ఎంట్రీలు నమోదు కాగానే ఇక్కడ ఆటోమేటిక్‌గా విశ్లేషణ కనిపిస్తుంది.</td></tr>';
      } else {
        emptyDiv.style.display = 'none';
        tableBox.style.display = 'block';

        let rowsHtml = '';
        let ledgerHtml = '';
        let recipHtml = '';

        APP_STATE.entries.forEach((e, idx) => {
          const amtStr = e.amount > 0 ? '₹' + e.amount.toLocaleString('en-IN') : '-';
          const jewelStr = (e.gold > 0 ? e.gold + 'g బంగారం ' : '') + (e.silver > 0 ? e.silver + 'g వెండి' : '') || '-';
          const recAmt = e.amount > 0 ? '₹' + (e.amount + 100).toLocaleString('en-IN') : 'ఆభరణం';

          rowsHtml += `
            <tr>
              <td><strong>#${e.receiptNo}</strong></td>
              <td>${e.name}</td>
              <td>${e.city}</td>
              <td style="font-weight: 700; color: var(--gold-primary); font-family: var(--font-numbers);">${amtStr}</td>
              <td><span style="font-size: 11px; background: var(--gold-surface); padding: 3px 8px; border-radius: 6px;">${e.type}</span></td>
              <td><button type="button" class="btn-outline" style="padding: 4px 10px; font-size: 12px;" onclick="document.getElementById('wa-phone').value='${e.phone||''}'; showTab('invites');">వాట్సాప్</button></td>
            </tr>
          `;

          ledgerHtml += `
            <tr>
              <td>${idx + 1}</td>
              <td><strong>#${e.receiptNo}</strong></td>
              <td><strong>${e.name}</strong></td>
              <td>${e.city}</td>
              <td>${e.relation}</td>
              <td style="font-weight: 700; color: var(--gold-primary); font-family: var(--font-numbers);">${amtStr}</td>
              <td>${jewelStr}</td>
              <td><span style="font-size: 11px; background: var(--gold-surface); padding: 3px 8px; border-radius: 6px;">${e.type}</span></td>
              <td><button type="button" class="btn-outline" style="padding: 4px 10px; font-size: 11px;" onclick="alert('రశీదు వివరాలు: ${e.name} - ${amtStr}')">వివరాలు</button></td>
            </tr>
          `;

          recipHtml += `
            <tr>
              <td><strong>${e.name}</strong></td>
              <td>${e.city}</td>
              <td style="font-weight: 700; color: var(--text-main); font-family: var(--font-numbers);">${amtStr}</td>
              <td style="font-weight: 700; color: var(--emerald); font-family: var(--font-numbers);">${recAmt}</td>
              <td><span style="color: var(--emerald); font-size: 12px; font-weight: 600;">సిఫార్సు సిద్ధం</span></td>
            </tr>
          `;
        });

        dashTbody.innerHTML = rowsHtml;
        ledgerTbody.innerHTML = ledgerHtml;
        recipTbody.innerHTML = recipHtml;
      }
    }

    // Initial render
    renderAll();
  </script>
</body>
</html>
'''

with open('web_preview/index.html', 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

print('Updated web_preview/index.html with 60-30-10 Aesthetic Light Palette!')
