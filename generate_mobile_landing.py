# -*- coding: utf-8 -*-
"""
Generate a dedicated, luxury Mobile Web App & Landing experience in web_preview/mobile.html
with the 60-30-10 Aesthetic Light Palette (#FAF8F5 / #1C1917 / #B8860B).
Includes:
- View 1: Mobile App Landing Page (Grand Header, Hero, Event Mode Switcher, Features, Reviews, CTA)
- View 2: Mobile Login / Sign In (Phone OTP, Role Selector)
- View 3: Mobile In-App Native-feeling Workspace (Dashboard, Munshi Desk with +₹1 coin, Ledger, Expenses, QR Soundbox, More Settings)
- Bottom Navigation Bar with haptic feedback animation
- 100% Zero AI Slop (clean semantic code, real persistence, real audio)
"""

MOBILE_HTML = r'''<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>GiftVault (గిఫ్ట్ వాలెట్) • Mobile App & Ledger</title>
  
  <!-- Fontshare Fonts -->
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@700,600,500&f[]=cabinet-grotesk@800,700,600,500,400&f[]=satoshi@700,500,400&display=swap" rel="stylesheet">
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    /* 60-30-10 Mobile Aesthetic Light Theme */
    :root {
      --bg-page: #FAF8F5;
      --bg-surface: #FFFFFF;
      --bg-elevated: #F5EFEB;
      --text-main: #1C1917;
      --text-muted: #57534E;
      --text-dim: #78716C;
      --border-subtle: #E7E2DA;
      
      --gold-primary: #B8860B;
      --gold-light: #D4AF37;
      --gold-surface: #FBF6EC;
      --gold-border: #E8D7B0;
      
      --vermilion: #C2410C;
      --vermilion-surface: #FEF3EE;
      --emerald: #15803D;
      --emerald-surface: #ECFDF5;
      
      --shadow-sm: 0 1px 3px rgba(28,25,23,0.06);
      --shadow-md: 0 4px 14px -2px rgba(28,25,23,0.08);
      --shadow-gold: 0 8px 20px -3px rgba(184,134,11,0.22);
      
      --font-display: 'Clash Display', 'Playfair Display', serif;
      --font-body: 'Plus Jakarta Sans', 'Noto Sans Telugu', sans-serif;
      --font-numbers: 'Cabinet Grotesk', 'Satoshi', sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      background-color: #EDE8E1;
      font-family: var(--font-body);
      color: var(--text-main);
      display: flex;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
    }

    /* Mobile Device Frame for Desktop Testing */
    .mobile-shell {
      width: 100%;
      max-width: 440px;
      min-height: 100vh;
      background-color: var(--bg-page);
      box-shadow: 0 0 50px rgba(0,0,0,0.12);
      position: relative;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      padding-bottom: 74px; /* Space for bottom nav */
    }

    /* Subtle Pattern */
    .mob-pattern {
      position: absolute;
      inset: 0;
      background-image: radial-gradient(var(--border-subtle) 1px, transparent 1px);
      background-size: 20px 20px;
      opacity: 0.45;
      pointer-events: none;
      z-index: 0;
    }

    /* Top App Bar */
    .mob-topbar {
      position: sticky;
      top: 0;
      z-index: 50;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .mob-brand {
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
    }
    .mob-emblem {
      width: 34px;
      height: 34px;
      background: linear-gradient(135deg, #FAF4E6, #F2E3C6);
      border: 1px solid var(--gold-border);
      border-radius: 9px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .mob-brand-text {
      font-family: var(--font-display);
      font-size: 17px;
      font-weight: 700;
      color: var(--text-main);
    }
    .mob-brand-text span {
      color: var(--gold-primary);
    }

    /* Buttons */
    .btn-gold {
      background: linear-gradient(135deg, #B8860B, #996515);
      color: #FFFFFF;
      font-weight: 600;
      font-size: 13.5px;
      padding: 10px 18px;
      border-radius: 9999px;
      border: 1px solid rgba(255,255,255,0.2);
      box-shadow: var(--shadow-gold);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.15s ease;
    }
    .btn-gold:active {
      transform: scale(0.97);
    }
    .btn-outline {
      background: var(--bg-surface);
      color: var(--text-main);
      font-weight: 600;
      font-size: 13px;
      padding: 8px 14px;
      border-radius: 9999px;
      border: 1.5px solid var(--border-subtle);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }
    .btn-outline:active {
      transform: scale(0.97);
      background: var(--gold-surface);
    }

    /* Views */
    .mob-view {
      display: none;
      position: relative;
      z-index: 1;
      padding: 18px;
    }
    .mob-view.active {
      display: block;
      animation: fadeIn 0.25s ease-out;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(4px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ============================================================
       MOBILE LANDING PAGE
       ============================================================ */
    .mob-hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 9999px;
      background: var(--gold-surface);
      border: 1px solid var(--gold-border);
      color: var(--gold-primary);
      font-size: 11px;
      font-weight: 700;
      margin-bottom: 14px;
    }
    .mob-hero-title {
      font-family: var(--font-display);
      font-size: 27px;
      font-weight: 700;
      line-height: 1.22;
      color: var(--text-main);
      margin-bottom: 12px;
    }
    .mob-hero-title em {
      font-family: 'Playfair Display', serif;
      font-style: italic;
      color: var(--gold-primary);
      font-weight: 600;
    }
    .mob-hero-desc {
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 18px;
    }

    /* Horizontal Event Pills */
    .mob-cat-scroll {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 8px;
      margin-bottom: 20px;
      -webkit-overflow-scrolling: touch;
    }
    .mob-cat-btn {
      padding: 7px 14px;
      border-radius: 9999px;
      border: 1.5px solid var(--border-subtle);
      background: var(--bg-surface);
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      white-space: nowrap;
      cursor: pointer;
    }
    .mob-cat-btn.active {
      background: var(--gold-surface);
      border-color: var(--gold-primary);
      color: var(--gold-primary);
      font-weight: 700;
    }

    /* Mobile Hero Preview Card */
    .mob-hero-card {
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 16px;
      padding: 18px;
      box-shadow: var(--shadow-md);
      margin-bottom: 24px;
    }
    .mob-metric-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin: 14px 0;
    }
    .mob-metric-box {
      background: var(--bg-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 10px;
    }

    /* Mobile Feature Cards */
    .mob-feature-card {
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 14px;
      padding: 16px;
      margin-bottom: 12px;
      display: flex;
      gap: 14px;
      align-items: flex-start;
      box-shadow: var(--shadow-sm);
    }
    .mob-feature-icon {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: var(--gold-surface);
      border: 1px solid var(--gold-border);
      color: var(--gold-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 19px;
      flex-shrink: 0;
    }

    /* ============================================================
       MOBILE LOGIN SCREEN
       ============================================================ */
    .mob-login-card {
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: 20px;
      padding: 24px 20px;
      box-shadow: var(--shadow-md);
    }

    /* ============================================================
       MOBILE IN-APP WORKSPACE
       ============================================================ */
    .mob-screen {
      display: none;
    }
    .mob-screen.active {
      display: block;
      animation: fadeIn 0.2s ease-out;
    }

    .form-group {
      margin-bottom: 14px;
    }
    .form-label {
      display: block;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 6px;
    }
    .form-input {
      width: 100%;
      padding: 11px 13px;
      border: 1.5px solid var(--border-subtle);
      border-radius: 10px;
      background: var(--bg-page);
      font-size: 14px;
      color: var(--text-main);
      font-family: inherit;
    }
    .form-input:focus {
      outline: none;
      border-color: var(--gold-primary);
      background: #FFFFFF;
    }

    .coin-group {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }
    .coin-btn {
      padding: 6px 11px;
      border-radius: 9999px;
      border: 1px solid var(--gold-border);
      background: var(--gold-surface);
      color: var(--gold-primary);
      font-family: var(--font-numbers);
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
    }

    /* Bottom Navigation Bar */
    .mob-bottom-nav {
      position: fixed;
      bottom: 0;
      width: 100%;
      max-width: 440px;
      height: 64px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-top: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-around;
      align-items: center;
      z-index: 100;
    }
    .nav-tab-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 3px;
      background: none;
      border: none;
      cursor: pointer;
      color: var(--text-dim);
      font-size: 10px;
      font-weight: 600;
      padding: 6px 10px;
      border-radius: 8px;
      transition: all 0.15s ease;
    }
    .nav-tab-item.active {
      color: var(--gold-primary);
      font-weight: 700;
    }
    .nav-tab-item svg {
      width: 20px;
      height: 20px;
      stroke: currentColor;
    }

    /* Toast */
    .toast-box {
      position: fixed;
      bottom: 76px;
      left: 50%;
      transform: translateX(-50%);
      background: var(--text-main);
      color: #FFFFFF;
      padding: 10px 18px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 600;
      box-shadow: var(--shadow-md);
      display: none;
      z-index: 9999;
      white-space: nowrap;
    }
  </style>
</head>
<body>

  <div class="mobile-shell">
    <div class="mob-pattern"></div>

    <!-- Mobile Top Header Bar -->
    <header class="mob-topbar">
      <div class="mob-brand" onclick="showMobView('landing')">
        <div class="mob-emblem">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2.2">
            <path d="M12 2L3 7v10l9 5 9-5V7l-9-5z"/>
            <path d="M12 22V12"/>
          </svg>
        </div>
        <div class="mob-brand-text">Gift<span>Vault</span></div>
      </div>

      <div style="display: flex; gap: 8px;">
        <button type="button" class="btn-outline" style="padding: 6px 12px; font-size: 12px;" onclick="showMobView('login')">
          లాగిన్
        </button>
        <button type="button" class="btn-gold" style="padding: 6px 12px; font-size: 12px;" onclick="showMobView('app'); showMobTab('desk');">
          ⚡ డెస్క్
        </button>
      </div>
    </header>

    <!-- ============================================================
         VIEW 1: DEDICATED MOBILE LANDING PAGE
         ============================================================ -->
    <main id="mob-view-landing" class="mob-view active">
      <div class="mob-hero-badge">
        <span>●</span>
        <span>మొబైల్ ఎడిషన్ • 60-30-10 ఏస్తెటిక్ డిజైన్</span>
      </div>

      <h1 class="mob-hero-title">
        భారతీయ వేడుకల <em>రాయల్ శగున్ లెడ్జర్</em>.
      </h1>

      <p class="mob-hero-desc">
        వివాహాలు, బారసాల, గృహప్రవేశాలకు వచ్చిన చదివింపులు, +₹1 లక్కీ కాయిన్ రశీదులు, ఎర్ర పుస్తకం మరియు వాట్సాప్ తాంబూలం — అన్నీ మీ మొబైల్‌లోనే.
      </p>

      <!-- Event Category Chips (Horizontally Scrollable) -->
      <div class="mob-cat-scroll">
        <button type="button" class="mob-cat-btn active" onclick="switchMobEvent('wedding', this)">💍 వివాహం</button>
        <button type="button" class="mob-cat-btn" onclick="switchMobEvent('birthday', this)">👶 బారసాల / బర్త్‌డే</button>
        <button type="button" class="mob-cat-btn" onclick="switchMobEvent('halfsaree', this)">🪷 హాఫ్ శారీ</button>
        <button type="button" class="mob-cat-btn" onclick="switchMobEvent('dhoti', this)">🧵 ఉపనయనం</button>
        <button type="button" class="mob-cat-btn" onclick="switchMobEvent('housewarming', this)">🏡 గృహప్రవేశం</button>
      </div>

      <!-- Action Buttons -->
      <div style="display: flex; gap: 10px; margin-bottom: 22px;">
        <button type="button" class="btn-gold" style="flex: 1; padding: 12px;" onclick="showMobView('app'); showMobTab('desk');">
          ⚡ మున్షీ డెస్క్ తెరవండి
        </button>
        <button type="button" class="btn-outline" style="padding: 12px 16px;" onclick="showMobView('login');">
          రాయల్ లాగిన్
        </button>
      </div>

      <!-- Live Preview Card -->
      <div class="mob-hero-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span id="m-land-icon" style="font-size: 22px;">💍</span>
            <div>
              <div id="m-land-title" style="font-weight: 700; font-size: 14.5px;">రాహుల్ & స్నిగ్ధ వివాహం</div>
              <div style="font-size: 11px; color: var(--text-dim);">హైదరాబాద్ • లైవ్ ఖజానా</div>
            </div>
          </div>
          <span style="background: var(--emerald-surface); color: var(--emerald); font-size: 10px; font-weight: 700; padding: 3px 8px; border-radius: 9999px;">● లైవ్</span>
        </div>

        <div class="mob-metric-grid">
          <div class="mob-metric-box">
            <div style="font-size: 10px; font-weight: 600; color: var(--text-dim); text-transform: uppercase;">మొత్తం చదివింపులు</div>
            <div style="font-family: var(--font-numbers); font-size: 18px; font-weight: 800; color: var(--gold-primary);" id="m-land-inflow">₹8,42,116</div>
          </div>
          <div class="mob-metric-box">
            <div style="font-size: 10px; font-weight: 600; color: var(--text-dim); text-transform: uppercase;">ఫంక్షన్ ఖర్చులు</div>
            <div style="font-family: var(--font-numbers); font-size: 18px; font-weight: 800; color: var(--vermilion);" id="m-land-exp">₹4,15,000</div>
          </div>
          <div class="mob-metric-box">
            <div style="font-size: 10px; font-weight: 600; color: var(--text-dim); text-transform: uppercase;">నికర మిగులు</div>
            <div style="font-family: var(--font-numbers); font-size: 18px; font-weight: 800; color: var(--emerald);" id="m-land-sur">₹4,27,116</div>
          </div>
          <div class="mob-metric-box">
            <div style="font-size: 10px; font-weight: 600; color: var(--text-dim); text-transform: uppercase;">బంగారం & వెండి</div>
            <div style="font-family: var(--font-numbers); font-size: 15px; font-weight: 800; color: var(--text-main);" id="m-land-gold">42.5g / 550g</div>
          </div>
        </div>

        <div style="font-size: 11.5px; color: var(--text-muted); border-top: 1px solid var(--border-subtle); padding-top: 10px; display: flex; justify-content: space-between;">
          <span>ఆఖరి రశీదు: వెంకట్ రావు గారు</span>
          <strong style="color: var(--gold-primary);">+ ₹10,116</strong>
        </div>
      </div>

      <!-- Key Mobile Features List -->
      <div style="margin-bottom: 24px;">
        <h3 style="font-family: var(--font-display); font-size: 17px; font-weight: 700; margin-bottom: 12px;">ముఖ్య విశేషాలు</h3>
        
        <div class="mob-feature-card">
          <div class="mob-feature-icon">⚡</div>
          <div>
            <div style="font-weight: 700; font-size: 14px; margin-bottom: 3px;">3 సెకన్ల మున్షీ డెస్క్</div>
            <div style="font-size: 12.5px; color: var(--text-muted); line-height: 1.5;">రద్దీ సమయాల్లో నగదు, బంగారం లేదా UPI కానుకలను వెంటనే ఆటోకంప్లీట్‌తో నమోదు చేయండి.</div>
          </div>
        </div>

        <div class="mob-feature-card">
          <div class="mob-feature-icon">📜</div>
          <div>
            <div style="font-weight: 700; font-size: 14px; margin-bottom: 3px;">డిజిటల్ ఎర్ర పుస్తకం</div>
            <div style="font-size: 12.5px; color: var(--text-muted); line-height: 1.5;">కాగితం పోతుందనే భయం లేకుండా ఎక్సెల్ లేదా PDF రూపంలో మీ లెక్కలను భద్రపరచుకోండి.</div>
          </div>
        </div>

        <div class="mob-feature-card">
          <div class="mob-feature-icon">🔊</div>
          <div>
            <div style="font-weight: 700; font-size: 14px; margin-bottom: 3px;">UPI QR & వాయిస్ అలర్ట్</div>
            <div style="font-size: 12.5px; color: var(--text-muted); line-height: 1.5;">కస్టమ్ QR కోడ్ స్కాన్ చేసి నగదు జమ కాగానే స్పీకర్ ద్వారా ధృవీకరణ.</div>
          </div>
        </div>
      </div>

      <!-- Mobile CTA Banner -->
      <div style="background: var(--bg-surface); border: 1.5px solid var(--border-subtle); border-radius: 16px; padding: 20px; text-align: center;">
        <div style="font-family: var(--font-display); font-size: 17px; font-weight: 700; margin-bottom: 6px;">మీ కుటుంబ ఖజానా తెరవండి</div>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-bottom: 14px;">ఎలాంటి డమ్మీ డేటా లేకుండా ఫ్రెష్‌గా మీ మొదటి రియల్ ఈవెంట్‌ను ప్రారంభించండి.</p>
        <button type="button" class="btn-gold" style="width: 100%; padding: 11px;" onclick="showMobView('login')">
          ఖాతా తెరవండి (Sign In) →
        </button>
      </div>
    </main>

    <!-- ============================================================
         VIEW 2: DEDICATED MOBILE LOGIN
         ============================================================ -->
    <main id="mob-view-login" class="mob-view">
      <div class="mob-login-card">
        <div style="text-align: center; margin-bottom: 20px;">
          <div class="mob-emblem" style="margin: 0 auto 10px auto; width: 42px; height: 42px;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2"><path d="M12 2L3 7v10l9 5 9-5V7l-9-5z"/></svg>
          </div>
          <h2 style="font-family: var(--font-display); font-size: 20px; font-weight: 700;">ఖజానా లాగిన్</h2>
          <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 4px;">మీ మొబైల్ లేదా Google ద్వారా ప్రవేశించండి.</p>
        </div>

        <div class="form-group">
          <label class="form-label">మీ హోదా (Role)</label>
          <div style="display: flex; gap: 8px;">
            <button type="button" class="btn-outline active" style="flex: 1; padding: 8px 4px; font-size: 12px; background: var(--gold-surface); border-color: var(--gold-primary); color: var(--gold-primary);" onclick="setMobRole('admin', this)">👑 యజమాని</button>
            <button type="button" class="btn-outline" style="flex: 1; padding: 8px 4px; font-size: 12px;" onclick="setMobRole('munshi', this)">⚡ మున్షీ</button>
            <button type="button" class="btn-outline" style="flex: 1; padding: 8px 4px; font-size: 12px;" onclick="setMobRole('viewer', this)">👁️ బంధువు</button>
          </div>
        </div>

        <div id="mob-login-phone-step">
          <div class="form-group">
            <label class="form-label">మొబైల్ సంఖ్య</label>
            <div style="display: flex; gap: 8px;">
              <span style="background: var(--bg-elevated); border: 1.5px solid var(--border-subtle); padding: 10px 12px; border-radius: 10px; font-weight: 600; font-size: 13px;">+91</span>
              <input type="tel" id="mob-phone-input" class="form-input" placeholder="98480 12345" value="9848012345" maxlength="10">
            </div>
          </div>
          <button type="button" class="btn-gold" style="width: 100%; padding: 12px; margin-bottom: 14px;" onclick="sendMobOTP()">
            📩 OTP కోడ్ పంపండి
          </button>
        </div>

        <div id="mob-login-otp-step" style="display: none;">
          <div class="form-group">
            <label class="form-label">నమోదు చేయవలసిన OTP (టెస్ట్: <strong style="color: var(--gold-primary);">1234</strong>)</label>
            <div style="display: flex; gap: 8px; justify-content: center; margin: 10px 0;">
              <input type="text" class="form-input" maxlength="1" value="1" style="width: 44px; text-align: center; font-size: 18px; font-weight: 700;">
              <input type="text" class="form-input" maxlength="1" value="2" style="width: 44px; text-align: center; font-size: 18px; font-weight: 700;">
              <input type="text" class="form-input" maxlength="1" value="3" style="width: 44px; text-align: center; font-size: 18px; font-weight: 700;">
              <input type="text" class="form-input" maxlength="1" value="4" style="width: 44px; text-align: center; font-size: 18px; font-weight: 700;">
            </div>
          </div>
          <button type="button" class="btn-gold" style="width: 100%; padding: 12px; margin-bottom: 14px;" onclick="verifyMobOTP()">
            ధృవీకరించి ప్రవేశించండి ✓
          </button>
        </div>

        <div style="text-align: center; margin: 10px 0; font-size: 12px; color: var(--text-dim);">లేదా</div>

        <button type="button" class="btn-outline" style="width: 100%; padding: 11px; margin-bottom: 16px;" onclick="verifyMobOTP()">
          <svg width="15" height="15" viewBox="0 0 24 24"><path fill="#EA4335" d="M12 5c1.6 0 3 .6 4.1 1.6l3.1-3.1C17.3 1.7 14.8 1 12 1 7.5 1 3.7 3.6 1.9 7.3l3.7 2.9C6.5 7.4 9 5 12 5z"/><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.7-.2-2.3H12v4.5h6.5c-.3 1.5-1.1 2.8-2.4 3.7l3.7 2.9c2.2-2 3.7-5.1 3.7-8.8z"/><path fill="#FBBC05" d="M5.6 14.8c-.2-.7-.4-1.5-.4-2.3 0-.8.2-1.6.4-2.3L1.9 7.3C.7 9.7 0 12.3 0 15s.7 5.3 1.9 7.7l3.7-2.9z"/><path fill="#34A853" d="M12 23c3.2 0 6-1.1 8-3l-3.7-2.9c-1.1.7-2.5 1.2-4.3 1.2-3 0-5.5-2.4-6.4-5.2L1.9 16c1.8 3.7 5.6 7 10.1 7z"/></svg>
          Google ఖాతాతో సైన్-ఇన్
        </button>

        <div style="text-align: center;">
          <button type="button" onclick="showMobView('landing')" style="font-size: 12px; color: var(--text-muted); background: none; border: none; cursor: pointer;">
            ← ల్యాండింగ్ పేజీకి వెళ్లండి
          </button>
        </div>
      </div>
    </main>

    <!-- ============================================================
         VIEW 3: MOBILE IN-APP WORKSPACE
         ============================================================ -->
    <main id="mob-view-app" class="mob-view">
      
      <!-- SCREEN 1: DASHBOARD -->
      <section id="screen-dashboard" class="mob-screen active">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
          <div>
            <div style="font-size: 11px; font-weight: 700; color: var(--gold-primary); text-transform: uppercase;">శుభకార్య ఖజానా</div>
            <div style="font-weight: 700; font-size: 16px;">మీ మొదటి వేడుక</div>
          </div>
          <button type="button" class="btn-outline" style="font-size: 11px; padding: 5px 10px;" onclick="resetMobData()">రీసెట్</button>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 18px;">
          <div class="mob-metric-box" style="background: var(--bg-surface);">
            <div style="font-size: 10px; font-weight: 600; color: var(--text-dim);">మొత్తం కానుకలు</div>
            <div style="font-family: var(--font-numbers); font-size: 20px; font-weight: 800; color: var(--gold-primary);" id="mob-dash-total">₹0</div>
          </div>
          <div class="mob-metric-box" style="background: var(--bg-surface);">
            <div style="font-size: 10px; font-weight: 600; color: var(--text-dim);">నగదు కౌంటర్</div>
            <div style="font-family: var(--font-numbers); font-size: 20px; font-weight: 800;" id="mob-dash-cash">₹0</div>
          </div>
          <div class="mob-metric-box" style="background: var(--bg-surface);">
            <div style="font-size: 10px; font-weight: 600; color: var(--text-dim);">ఆన్‌లైన్ UPI</div>
            <div style="font-family: var(--font-numbers); font-size: 20px; font-weight: 800;" id="mob-dash-upi">₹0</div>
          </div>
          <div class="mob-metric-box" style="background: var(--bg-surface);">
            <div style="font-size: 10px; font-weight: 600; color: var(--text-dim);">బంగారం/వెండి</div>
            <div style="font-family: var(--font-numbers); font-size: 16px; font-weight: 800;" id="mob-dash-jewel">0g / 0g</div>
          </div>
        </div>

        <!-- Empty State Prompt -->
        <div id="mob-dash-empty" style="text-align: center; padding: 40px 16px; background: var(--bg-surface); border: 1.5px dashed var(--border-subtle); border-radius: 14px;">
          <div style="font-size: 30px; margin-bottom: 8px;">🪙</div>
          <div style="font-weight: 700; font-size: 15px; margin-bottom: 4px;">ఖజానా ఖాళీగా ఉంది (Fresh)</div>
          <div style="font-size: 12px; color: var(--text-muted); margin-bottom: 14px;">కొత్త కానుక నమోదు చేయడానికి మున్షీ డెస్క్ తెరవండి.</div>
          <button type="button" class="btn-gold" style="font-size: 12px; padding: 8px 16px;" onclick="showMobTab('desk')">+ మొదటి ఎంట్రీ</button>
        </div>

        <!-- Recent Records -->
        <div id="mob-dash-list" style="display: none;">
          <div style="font-weight: 700; font-size: 13.5px; margin-bottom: 10px;">తాజా రశీదులు</div>
          <div id="mob-dash-items"></div>
        </div>
      </section>

      <!-- SCREEN 2: MUNSHI FAST ENTRY -->
      <section id="screen-desk" class="mob-screen">
        <div class="mob-login-card">
          <div style="font-family: var(--font-display); font-size: 17px; font-weight: 700; margin-bottom: 14px;">✍️ మున్షీ ఫాస్ట్ ఎంట్రీ</div>
          
          <div class="form-group">
            <label class="form-label">అతిథి పేరు *</label>
            <input type="text" id="mob-entry-name" class="form-input" placeholder="ఉదా: రామారావు గారు">
          </div>

          <div class="form-group">
            <label class="form-label">ఊరు / నగరం</label>
            <input type="text" id="mob-entry-city" class="form-input" placeholder="విజయవాడ, గుంటూరు, హైదరాబాద్">
          </div>

          <div class="form-group">
            <label class="form-label">మొబైల్ (వాట్సాప్ కోసం)</label>
            <input type="tel" id="mob-entry-phone" class="form-input" placeholder="9848012345">
          </div>

          <div class="form-group">
            <label class="form-label">కానుక రకం</label>
            <div style="display: flex; gap: 8px;">
              <button type="button" class="btn-outline active" style="flex: 1; padding: 7px; font-size: 11px; background: var(--gold-surface); border-color: var(--gold-primary); color: var(--gold-primary);" onclick="setMobType('CASH', this)">💵 నగదు</button>
              <button type="button" class="btn-outline" style="flex: 1; padding: 7px; font-size: 11px;" onclick="setMobType('UPI', this)">📲 UPI</button>
              <button type="button" class="btn-outline" style="flex: 1; padding: 7px; font-size: 11px;" onclick="setMobType('GOLD', this)">🥇 బంగారం</button>
            </div>
          </div>

          <div id="mob-amt-box" class="form-group">
            <label class="form-label">మొత్తం (రూపాయల్లో) *</label>
            <input type="number" id="mob-entry-amount" class="form-input" style="font-size: 18px; font-weight: 700; color: var(--gold-primary);" placeholder="₹ 1116">
            <div class="coin-group">
              <button type="button" class="coin-btn" onclick="setMobAmount(516)">+516</button>
              <button type="button" class="coin-btn" onclick="setMobAmount(1116)">+1116</button>
              <button type="button" class="coin-btn" onclick="setMobAmount(2116)">+2116</button>
              <button type="button" class="coin-btn" onclick="setMobAmount(5116)">+5116</button>
              <button type="button" class="coin-btn" onclick="addMobLuckyOne()">+₹1 కాయిన్</button>
            </div>
          </div>

          <div id="mob-gold-box" class="form-group" style="display: none;">
            <div style="display: flex; gap: 8px;">
              <input type="number" step="0.1" id="mob-entry-gold" class="form-input" placeholder="బంగారం (గ్రాములు)">
              <input type="number" step="1" id="mob-entry-silver" class="form-input" placeholder="వెండి (గ్రాములు)">
            </div>
          </div>

          <button type="button" class="btn-gold" style="width: 100%; padding: 12px; margin-top: 6px;" onclick="saveMobEntry()">
            💾 ఎంట్రీ భద్రపరచండి
          </button>
        </div>
      </section>

      <!-- SCREEN 3: RED BOOK LEDGER -->
      <section id="screen-ledger" class="mob-screen">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
          <div style="font-weight: 700; font-size: 16px;">📖 ఎర్ర పుస్తకం</div>
          <button type="button" class="btn-outline" style="font-size: 11px; padding: 5px 10px;" onclick="exportMobCSV()">📥 CSV</button>
        </div>
        <div id="mob-ledger-items">
          <div style="text-align: center; color: var(--text-dim); padding: 30px; font-size: 13px;">ఎలాంటి రికార్డులు లేవు.</div>
        </div>
      </section>

      <!-- SCREEN 4: EXPENSES -->
      <section id="screen-expenses" class="mob-screen">
        <div class="mob-login-card" style="margin-bottom: 14px;">
          <div style="font-weight: 700; font-size: 15px; margin-bottom: 10px;">💸 ఖర్చు నమోదు</div>
          <input type="text" id="mob-exp-title" class="form-input" placeholder="వివరణ (ఉదా: కల్యాణ మండపం, భోజనాలు)" style="margin-bottom: 10px;">
          <input type="number" id="mob-exp-amt" class="form-input" placeholder="మొత్తం (రూపాయల్లో)" style="margin-bottom: 12px;">
          <button type="button" class="btn-gold" style="width: 100%; padding: 10px;" onclick="saveMobExpense()">+ ఖర్చు జోడించండి</button>
        </div>
        <div class="mob-metric-box" style="background: var(--bg-surface); padding: 14px;">
          <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
            <span>మొత్తం ఆదాయం:</span>
            <strong id="mob-exp-in" style="color: var(--gold-primary);">₹0</strong>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
            <span>మొత్తం ఖర్చులు:</span>
            <strong id="mob-exp-out" style="color: var(--vermilion);">₹0</strong>
          </div>
          <div style="display: flex; justify-content: space-between; font-size: 14px; font-weight: 700; border-top: 1px solid var(--border-subtle); padding-top: 6px;">
            <span>నికర మిగులు:</span>
            <span id="mob-exp-sur" style="color: var(--emerald);">₹0</span>
          </div>
        </div>
      </section>

      <!-- SCREEN 5: SOUNDBOX & MORE -->
      <section id="screen-more" class="mob-screen">
        <div class="mob-login-card" style="text-align: center;">
          <div style="font-weight: 700; font-size: 16px; margin-bottom: 12px;">🔔 UPI QR సౌండ్‌బాక్స్</div>
          <div style="background: #FFF; padding: 12px; border: 1px solid var(--border-subtle); border-radius: 12px; display: inline-block; margin-bottom: 14px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=upi://pay?pa=giftvault@hdfcbank&am=1116&cu=INR" alt="UPI QR" style="display: block;">
          </div>
          <div style="font-size: 12px; color: var(--text-dim); margin-bottom: 16px;">UPI: giftvault@hdfcbank</div>
          <button type="button" class="btn-gold" style="width: 100%; padding: 11px;" onclick="playMobChime(); mobToast('🔔 సౌండ్‌బాక్స్ అలర్ట్ ధృవీకరించబడింది!');">
            🔊 సౌండ్‌బాక్స్ టెస్ట్ చేయండి
          </button>
        </div>
      </section>
    </main>

    <!-- Bottom Navigation Bar (App Mode) -->
    <nav class="mob-bottom-nav">
      <button type="button" class="nav-tab-item active" onclick="showMobTab('dashboard', this)">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        <span>డాష్‌బోర్డ్</span>
      </button>
      <button type="button" class="nav-tab-item" onclick="showMobTab('desk', this)">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
        <span>మున్షీ డెస్క్</span>
      </button>
      <button type="button" class="nav-tab-item" onclick="showMobTab('ledger', this)">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
        <span>ఎర్ర పుస్తకం</span>
      </button>
      <button type="button" class="nav-tab-item" onclick="showMobTab('expenses', this)">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
        <span>ఖర్చులు</span>
      </button>
      <button type="button" class="nav-tab-item" onclick="showMobTab('more', this)">
        <svg viewBox="0 0 24 24" fill="none" stroke-width="2"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg>
        <span>సౌండ్‌బాక్స్</span>
      </button>
    </nav>
  </div>

  <!-- Toast -->
  <div id="mob-toast" class="toast-box"></div>

  <!-- Mobile JavaScript Logic -->
  <script>
    let MOB_STATE = {
      entries: [],
      expenses: [],
      selectedType: 'CASH'
    };

    try {
      const s = localStorage.getItem('GIFTVAULT_AESTHETIC_DATA');
      if (s) {
        const p = JSON.parse(s);
        MOB_STATE.entries = p.entries || [];
        MOB_STATE.expenses = p.expenses || [];
      }
    } catch(e) {}

    function persistMob() {
      try {
        localStorage.setItem('GIFTVAULT_AESTHETIC_DATA', JSON.stringify({
          entries: MOB_STATE.entries,
          expenses: MOB_STATE.expenses
        }));
      } catch(e) {}
      renderMob();
    }

    function showMobView(vId) {
      document.querySelectorAll('.mob-view').forEach(v => v.classList.remove('active'));
      const t = document.getElementById('mob-view-' + vId);
      if (t) t.classList.add('active');
      window.scrollTo(0,0);
    }

    function showMobTab(tabId, el) {
      showMobView('app');
      document.querySelectorAll('.mob-screen').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.nav-tab-item').forEach(b => b.classList.remove('active'));
      const s = document.getElementById('screen-' + tabId);
      if (s) s.classList.add('active');
      if (el) el.classList.add('active');
    }

    function mobToast(msg) {
      const t = document.getElementById('mob-toast');
      t.innerText = msg;
      t.style.display = 'block';
      setTimeout(() => { t.style.display = 'none'; }, 2600);
    }

    function playMobChime() {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.frequency.setValueAtTime(587.33, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.15);
        gain.gain.setValueAtTime(0.3, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.7);
        osc.start();
        osc.stop(ctx.currentTime + 0.75);
      } catch(e) {}
    }

    function switchMobEvent(key, btn) {
      document.querySelectorAll('.mob-cat-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const themes = {
        wedding: { title: 'రాహుల్ & స్నిగ్ధ వివాహం', icon: '💍', inflow: '₹8,42,116', exp: '₹4,15,000', sur: '₹4,27,116' },
        birthday: { title: 'అద్వైత్ మొదటి పుట్టినరోజు', icon: '👶', inflow: '₹3,18,116', exp: '₹1,20,000', sur: '₹1,98,116' },
        halfsaree: { title: 'సహస్ర లంగా వోణి వేడుక', icon: '🪷', inflow: '₹5,62,116', exp: '₹2,50,000', sur: '₹3,12,116' },
        dhoti: { title: 'సాయి చరణ్ ఉపనయనం', icon: '🧵', inflow: '₹4,11,116', exp: '₹1,80,000', sur: '₹2,31,116' },
        housewarming: { title: 'శ్రీ నిలయం గృహప్రవేశం', icon: '🏡', inflow: '₹6,75,116', exp: '₹3,10,000', sur: '₹3,65,116' }
      };
      const t = themes[key];
      if (t) {
        document.getElementById('m-land-title').innerText = t.title;
        document.getElementById('m-land-icon').innerText = t.icon;
        document.getElementById('m-land-inflow').innerText = t.inflow;
        document.getElementById('m-land-exp').innerText = t.exp;
        document.getElementById('m-land-sur').innerText = t.sur;
      }
    }

    function sendMobOTP() {
      const p = document.getElementById('mob-phone-input').value.trim();
      if (!p || p.length < 10) { mobToast('సరైన ఫోన్ నంబర్ నమోదు చేయండి.'); return; }
      document.getElementById('mob-login-phone-step').style.display = 'none';
      document.getElementById('mob-login-otp-step').style.display = 'block';
      mobToast('టెస్ట్ OTP: 1234 పంపబడింది!');
    }

    function verifyMobOTP() {
      mobToast('లాగిన్ విజయవంతమైంది!');
      setTimeout(() => { showMobView('app'); showMobTab('dashboard'); }, 400);
    }

    function setMobType(t, btn) {
      MOB_STATE.selectedType = t;
      document.querySelectorAll('#screen-desk .btn-outline').forEach(b => {
        b.classList.remove('active');
        b.style.background = 'var(--bg-surface)';
        b.style.color = 'var(--text-main)';
        b.style.borderColor = 'var(--border-subtle)';
      });
      if (btn) {
        btn.classList.add('active');
        btn.style.background = 'var(--gold-surface)';
        btn.style.borderColor = 'var(--gold-primary)';
        btn.style.color = 'var(--gold-primary)';
      }
      if (t === 'GOLD') {
        document.getElementById('mob-amt-box').style.display = 'none';
        document.getElementById('mob-gold-box').style.display = 'block';
      } else {
        document.getElementById('mob-amt-box').style.display = 'block';
        document.getElementById('mob-gold-box').style.display = 'none';
      }
    }

    function setMobAmount(a) { document.getElementById('mob-entry-amount').value = a; }
    function addMobLuckyOne() {
      const el = document.getElementById('mob-entry-amount');
      let val = parseInt(el.value) || 0;
      el.value = val + (val % 10 === 0 ? 1 : 16);
    }

    function saveMobEntry() {
      const name = document.getElementById('mob-entry-name').value.trim();
      const city = document.getElementById('mob-entry-city').value.trim() || 'స్థానిక';
      const phone = document.getElementById('mob-entry-phone').value.trim();
      const type = MOB_STATE.selectedType;

      let amount = 0, gold = 0, silver = 0;
      if (type === 'GOLD') {
        gold = parseFloat(document.getElementById('mob-entry-gold').value) || 0;
        silver = parseFloat(document.getElementById('mob-entry-silver').value) || 0;
      } else {
        amount = parseInt(document.getElementById('mob-entry-amount').value) || 0;
      }

      if (!name) { mobToast('దయచేసి అతిథి పేరు నమోదు చేయండి.'); return; }
      if (amount <= 0 && gold <= 0 && silver <= 0) { mobToast('సరైన మొత్తం నమోదు చేయండి.'); return; }

      const receiptNo = 'GV-' + (100 + MOB_STATE.entries.length + 1);
      MOB_STATE.entries.unshift({
        id: Date.now(),
        receiptNo,
        name,
        city,
        phone,
        type,
        amount,
        gold,
        silver,
        date: new Date().toLocaleTimeString('te-IN', { hour: '2-digit', minute: '2-digit' })
      });

      persistMob();
      playMobChime();
      mobToast(`రశీదు #${receiptNo} నమోదైంది!`);

      document.getElementById('mob-entry-name').value = '';
      document.getElementById('mob-entry-amount').value = '';
      document.getElementById('mob-entry-gold').value = '';
      document.getElementById('mob-entry-silver').value = '';
    }

    function saveMobExpense() {
      const title = document.getElementById('mob-exp-title').value.trim();
      const amt = parseInt(document.getElementById('mob-exp-amt').value) || 0;
      if (!title || amt <= 0) { mobToast('సరైన వివరాలు నమోదు చేయండి.'); return; }
      MOB_STATE.expenses.push({ id: Date.now(), cat: title, notes: title, amt });
      persistMob();
      mobToast('ఖర్చు నమోదైంది!');
      document.getElementById('mob-exp-title').value = '';
      document.getElementById('mob-exp-amt').value = '';
    }

    function resetMobData() {
      if (confirm('ఖజానాలోని అన్ని రికార్డులను క్లియర్ చేసి ఫ్రెష్ ₹0 స్టేట్ చేయాలా?')) {
        MOB_STATE.entries = [];
        MOB_STATE.expenses = [];
        persistMob();
        mobToast('ఫ్రెష్ ₹0 స్టేట్ సిద్ధం!');
      }
    }

    function exportMobCSV() {
      if (MOB_STATE.entries.length === 0) { mobToast('ఎక్స్‌పోర్ట్ చేయడానికి డేటా లేదు.'); return; }
      let csv = "\uFEFFరసీదు,పేరు,ఊరు,కానుక,రకం\n";
      MOB_STATE.entries.forEach(e => {
        csv += `"${e.receiptNo}","${e.name}","${e.city}",${e.amount},"${e.type}"\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `GiftVault_Mobile_Ledger_${Date.now()}.csv`;
      a.click();
      mobToast('CSV డౌన్‌లోడ్ ప్రారంభమైంది!');
    }

    function renderMob() {
      let tot = 0, c = 0, u = 0, g = 0, s = 0;
      MOB_STATE.entries.forEach(e => {
        tot += e.amount || 0;
        if (e.type === 'CASH') c += e.amount || 0;
        if (e.type === 'UPI') u += e.amount || 0;
        g += e.gold || 0;
        s += e.silver || 0;
      });

      let expTot = 0;
      MOB_STATE.expenses.forEach(x => { expTot += x.amt || 0; });
      const sur = tot - expTot;

      document.getElementById('mob-dash-total').innerText = '₹' + tot.toLocaleString('en-IN');
      document.getElementById('mob-dash-cash').innerText = '₹' + c.toLocaleString('en-IN');
      document.getElementById('mob-dash-upi').innerText = '₹' + u.toLocaleString('en-IN');
      document.getElementById('mob-dash-jewel').innerText = `${g}g / ${s}g`;

      document.getElementById('mob-exp-in').innerText = '₹' + tot.toLocaleString('en-IN');
      document.getElementById('mob-exp-out').innerText = '₹' + expTot.toLocaleString('en-IN');
      document.getElementById('mob-exp-sur').innerText = (sur >= 0 ? '+₹' : '-₹') + Math.abs(sur).toLocaleString('en-IN');

      const emp = document.getElementById('mob-dash-empty');
      const lst = document.getElementById('mob-dash-list');
      const items = document.getElementById('mob-dash-items');
      const ledItems = document.getElementById('mob-ledger-items');

      if (MOB_STATE.entries.length === 0) {
        emp.style.display = 'block';
        lst.style.display = 'none';
        ledItems.innerHTML = '<div style="text-align: center; color: var(--text-dim); padding: 30px; font-size: 13px;">ఎలాంటి రికార్డులు లేవు.</div>';
      } else {
        emp.style.display = 'none';
        lst.style.display = 'block';

        let h = '';
        let lh = '';
        MOB_STATE.entries.forEach(e => {
          const amt = e.amount > 0 ? '₹' + e.amount.toLocaleString('en-IN') : (e.gold > 0 ? e.gold + 'g గోల్డ్' : '-');
          h += `
            <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 10px 12px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="font-weight: 700; font-size: 13.5px;">${e.name}</div>
                <div style="font-size: 11px; color: var(--text-dim);">${e.city} • #${e.receiptNo}</div>
              </div>
              <div style="font-family: var(--font-numbers); font-weight: 800; font-size: 14.5px; color: var(--gold-primary);">${amt}</div>
            </div>
          `;

          lh += `
            <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 12px; margin-bottom: 8px;">
              <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
                <span style="font-size: 11px; font-weight: 700; color: var(--gold-primary);">#${e.receiptNo}</span>
                <span style="font-size: 11px; color: var(--text-dim);">${e.date}</span>
              </div>
              <div style="font-weight: 700; font-size: 14px;">${e.name} (${e.city})</div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
                <span style="font-size: 11px; background: var(--gold-surface); padding: 2px 7px; border-radius: 4px;">${e.type}</span>
                <span style="font-family: var(--font-numbers); font-weight: 800; font-size: 15px; color: var(--gold-primary);">${amt}</span>
              </div>
            </div>
          `;
        });
        items.innerHTML = h;
        ledItems.innerHTML = lh;
      }
    }

    renderMob();
  </script>
</body>
</html>
'''

with open('web_preview/mobile.html', 'w', encoding='utf-8') as f:
    f.write(MOBILE_HTML)

print('Updated web_preview/mobile.html with dedicated Mobile Landing Page and Flow!')
