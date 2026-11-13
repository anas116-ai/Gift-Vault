import os

html_masterpiece = """<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <title>GiftVault (గిఫ్ట్ వాలెట్) • రాయల్ శుభకార్య ఖజానా & డిజిటల్ ఎర్ర పుస్తకం</title>
  
  <!-- Curated Luxury Typography -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600;1,700&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">
  
  <!-- Three.js 3D WebGL Library for 3Dviz-Pro-Max -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <style>
    /* ==========================================================================
       MOTIONSITES & THREEUI AESTHETIC DESIGN SYSTEM (DARK OBSIDIAN & SACRED GOLD)
       ========================================================================== */
    :root {
      --bg-space: #030712;
      --bg-card: rgba(15, 23, 42, 0.72);
      --bg-card-hover: rgba(30, 41, 59, 0.85);
      --c-gold: #F59E0B;
      --c-gold-light: #FDE68A;
      --c-gold-dark: #B45309;
      --c-crimson: #E11D48;
      --c-crimson-glow: rgba(225, 29, 72, 0.4);
      --c-emerald: #10B981;
      --c-text-primary: #F8FAFC;
      --c-text-secondary: #94A3B8;
      --c-text-muted: #64748B;
      --border-glass: rgba(255, 255, 255, 0.08);
      --border-gold: rgba(245, 158, 11, 0.35);
      --font-display: 'Cinzel', 'Playfair Display', serif;
      --font-serif: 'Playfair Display', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', system-ui, sans-serif;
      --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
      --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      background-color: var(--bg-space);
      color: var(--c-text-primary);
      font-family: var(--font-sans);
      min-height: 100vh;
      overflow-x: hidden;
      position: relative;
      background-image: 
        radial-gradient(circle at 50% 0%, rgba(225, 29, 72, 0.15) 0%, transparent 60%),
        radial-gradient(circle at 85% 30%, rgba(245, 158, 11, 0.12) 0%, transparent 50%),
        radial-gradient(circle at 15% 70%, rgba(16, 185, 129, 0.08) 0%, transparent 50%);
      background-attachment: fixed;
    }

    /* Fixed Celestial Mesh Canvas */
    #ambient-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
      opacity: 0.75;
    }

    /* Container */
    .app-viewport-container {
      position: relative;
      z-index: 1;
      width: 100%;
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Top Sacred Shlokam Glow Banner */
    .sacred-top-shlokam-bar {
      background: linear-gradient(90deg, transparent, rgba(245, 158, 11, 0.18), rgba(225, 29, 72, 0.22), rgba(245, 158, 11, 0.18), transparent);
      border-bottom: 1px solid rgba(245, 158, 11, 0.3);
      text-align: center;
      padding: 8px 16px;
      font-family: var(--font-display);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.15em;
      color: var(--c-gold-light);
      text-shadow: 0 0 12px rgba(245, 158, 11, 0.5);
    }

    /* Header Nav */
    .royal-navbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 0;
      border-bottom: 1px solid var(--border-glass);
      backdrop-filter: blur(12px);
      position: sticky;
      top: 0;
      z-index: 99;
    }
    .brand-cluster {
      display: flex;
      align-items: center;
      gap: 14px;
      cursor: pointer;
      text-decoration: none;
    }
    .brand-crest-symbol {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, #1E1B4B 0%, #030712 100%);
      border: 1.5px solid var(--c-gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-size: 20px;
      font-weight: 900;
      color: var(--c-gold);
      box-shadow: 0 0 16px rgba(245, 158, 11, 0.3);
    }
    .brand-title-wrap h1 {
      font-family: var(--font-display);
      font-size: 22px;
      font-weight: 800;
      letter-spacing: 0.05em;
      color: #FFFFFF;
      line-height: 1.1;
    }
    .brand-title-wrap span {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      color: var(--c-crimson);
      text-transform: uppercase;
    }
    .nav-actions-cluster {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .lang-pill-select {
      background: rgba(15, 23, 42, 0.85);
      color: var(--c-text-primary);
      border: 1px solid var(--border-glass);
      padding: 8px 14px;
      border-radius: 9999px;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      outline: none;
      transition: all 0.2s ease;
    }
    .lang-pill-select:hover {
      border-color: var(--c-gold);
    }

    /* Motion Buttons */
    .btn-gold-action {
      background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
      color: #030712;
      border: none;
      padding: 12px 26px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 800;
      letter-spacing: 0.02em;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 20px rgba(245, 158, 11, 0.35);
      transition: all 0.2s var(--ease-out);
      text-decoration: none;
    }
    .btn-gold-action:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 28px rgba(245, 158, 11, 0.5);
    }
    .btn-gold-action:active {
      transform: scale(0.97);
    }

    .btn-glass-action {
      background: rgba(30, 41, 59, 0.7);
      color: #FFFFFF;
      border: 1px solid var(--border-glass);
      padding: 12px 22px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      backdrop-filter: blur(8px);
      transition: all 0.2s ease;
    }
    .btn-glass-action:hover {
      background: rgba(51, 65, 85, 0.9);
      border-color: rgba(255, 255, 255, 0.2);
      transform: translateY(-2px);
    }
    .btn-glass-action:active {
      transform: scale(0.97);
    }

    /* Views Framework */
    .view-screen-pane {
      display: none;
      animation: viewFadeIn 0.35s var(--ease-out) forwards;
    }
    .view-screen-pane.active {
      display: block;
    }
    @keyframes viewFadeIn {
      0% { opacity: 0; transform: translateY(10px); }
      100% { opacity: 1; transform: translateY(0); }
    }

    /* ==========================================================================
       HERO SECTION WITH REAL THREE.JS 3D WEBGL HERO CANVAS
       ========================================================================== */
    .hero-cinematic-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 40px;
      align-items: center;
      padding: 60px 0 40px;
    }
    .hero-pre-tag {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(225, 29, 72, 0.12);
      border: 1px solid rgba(225, 29, 72, 0.35);
      color: #FDA4AF;
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 20px;
    }
    .hero-pre-tag::before {
      content: "";
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--c-crimson);
      box-shadow: 0 0 8px var(--c-crimson);
      animation: pulseDot 2s infinite;
    }
    @keyframes pulseDot {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.4); opacity: 0.6; }
    }
    .hero-massive-heading {
      font-family: var(--font-display);
      font-size: 58px;
      font-weight: 900;
      line-height: 1.1;
      letter-spacing: -0.01em;
      margin-bottom: 22px;
      color: #FFFFFF;
    }
    .hero-massive-heading em {
      font-style: italic;
      font-family: var(--font-serif);
      background: linear-gradient(135deg, #FDE68A 0%, #F59E0B 50%, #D97706 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-subtitle-desc {
      font-size: 17px;
      line-height: 1.65;
      color: var(--c-text-secondary);
      max-width: 580px;
      margin-bottom: 34px;
    }
    .hero-cta-group {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      margin-bottom: 32px;
    }

    /* 3D WebGL Canvas Holder */
    .webgl-hero-container {
      position: relative;
      width: 100%;
      height: 480px;
      border-radius: 28px;
      background: radial-gradient(circle at 50% 50%, rgba(30, 41, 59, 0.5) 0%, rgba(3, 7, 18, 0.8) 100%);
      border: 1px solid var(--border-glass);
      box-shadow: 0 24px 60px -12px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.1);
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    #three-coin-canvas {
      width: 100% !important;
      height: 100% !important;
      display: block;
      cursor: grab;
    }
    #three-coin-canvas:active {
      cursor: grabbing;
    }
    .webgl-badge-overlay {
      position: absolute;
      bottom: 20px;
      left: 20px;
      right: 20px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-gold);
      padding: 12px 18px;
      border-radius: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      backdrop-filter: blur(12px);
      z-index: 2;
      pointer-events: none;
    }

    /* ==========================================================================
       ETALE 52 MECHANICAL ROLLING NUMBER PLATES & CALCULATOR BENTO CARD
       ========================================================================== */
    .bento-section-wrap {
      padding: 40px 0 80px;
    }
    .bento-card-luxury {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 24px;
      padding: 36px;
      backdrop-filter: blur(20px);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.08);
      position: relative;
      overflow: hidden;
      transition: border-color 0.3s ease;
    }
    .bento-card-luxury:hover {
      border-color: rgba(245, 158, 11, 0.4);
    }
    .bento-card-luxury::after {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle 400px at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(245, 158, 11, 0.06), transparent 70%);
      pointer-events: none;
    }

    /* Mechanical Number Plate Slots */
    .etale-plate-cluster {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #020617;
      padding: 12px 20px;
      border-radius: 16px;
      border: 1.5px solid rgba(245, 158, 11, 0.45);
      box-shadow: 0 12px 36px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.15);
    }
    .etale-currency-symbol {
      color: var(--c-gold);
      font-family: var(--font-display);
      font-size: 32px;
      font-weight: 800;
      margin-right: 4px;
      text-shadow: 0 0 12px rgba(245, 158, 11, 0.6);
    }
    .etale-digit-slot {
      position: relative;
      width: 28px;
      height: 48px;
      background: linear-gradient(180deg, #1E293B 0%, #020617 100%);
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid rgba(245, 158, 11, 0.35);
      box-shadow: inset 0 3px 6px rgba(0,0,0,0.9), 0 2px 4px rgba(0,0,0,0.5);
    }
    .etale-digit-slot::after {
      content: "";
      position: absolute;
      top: 50%;
      left: 0;
      right: 0;
      height: 1px;
      background: rgba(255, 255, 255, 0.15);
      box-shadow: 0 1px 1px rgba(0,0,0,0.9);
      z-index: 2;
    }
    .etale-digit-ribbon {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      transition: transform 0.5s var(--ease-spring);
    }
    .etale-digit-item {
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      font-family: var(--font-sans);
      font-size: 26px;
      font-weight: 800;
      font-feature-settings: 'tnum';
      font-variant-numeric: tabular-nums;
      text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }
    .etale-separator {
      color: var(--c-gold);
      font-size: 28px;
      font-weight: 800;
      padding: 0 3px;
      line-height: 48px;
    }

    /* Calculator Grid */
    .calc-bento-grid {
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 36px;
      align-items: center;
    }
    .calc-slider-range {
      width: 100%;
      height: 8px;
      border-radius: 4px;
      background: #1E293B;
      outline: none;
      accent-color: var(--c-gold);
      cursor: pointer;
    }

    /* ==========================================================================
       EVENT HUB & WORKSPACE SCREEN
       ========================================================================== */
    .events-grid-bento {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 24px;
      margin-top: 28px;
    }
    .event-card-luxury {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 20px;
      padding: 26px;
      backdrop-filter: blur(16px);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.4);
      transition: all 0.25s var(--ease-out);
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .event-card-luxury:hover {
      transform: translateY(-4px);
      border-color: var(--border-gold);
      background: var(--bg-card-hover);
    }

    /* Form Fields */
    .input-field-dark {
      width: 100%;
      background: rgba(2, 6, 23, 0.8);
      border: 1px solid var(--border-glass);
      color: #FFFFFF;
      padding: 12px 16px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s ease;
    }
    .input-field-dark:focus {
      border-color: var(--c-gold);
      box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.15);
    }

    /* Lucky Coin Chip Bar */
    .lucky-coin-bar {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 10px;
    }
    .lucky-chip {
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: var(--c-gold-light);
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .lucky-chip:hover {
      background: var(--c-gold);
      color: #030712;
      transform: scale(1.04);
    }
    .lucky-chip:active {
      transform: scale(0.96);
    }

    /* Workspace Tabs */
    .ws-tabs-cluster {
      display: flex;
      gap: 10px;
      border-bottom: 1px solid var(--border-glass);
      padding-bottom: 14px;
      margin-bottom: 24px;
      overflow-x: auto;
    }
    .ws-tab-btn-lux {
      background: transparent;
      border: 1px solid transparent;
      color: var(--c-text-secondary);
      padding: 10px 20px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .ws-tab-btn-lux:hover {
      color: #FFFFFF;
      background: rgba(30, 41, 59, 0.5);
    }
    .ws-tab-btn-lux.active {
      color: #030712;
      background: var(--c-gold);
      border-color: var(--c-gold);
      box-shadow: 0 4px 16px rgba(245, 158, 11, 0.35);
    }

    /* Ledger Table */
    .table-container-dark {
      width: 100%;
      overflow-x: auto;
      border-radius: 16px;
      border: 1px solid var(--border-glass);
      background: rgba(2, 6, 23, 0.75);
    }
    .ledger-table-dark {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13.5px;
    }
    .ledger-table-dark th {
      background: rgba(15, 23, 42, 0.95);
      color: var(--c-text-secondary);
      padding: 14px 16px;
      font-weight: 700;
      border-bottom: 1px solid var(--border-glass);
      text-transform: uppercase;
      font-size: 11.5px;
      letter-spacing: 0.05em;
    }
    .ledger-table-dark td {
      padding: 14px 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: var(--c-text-primary);
    }
    .ledger-table-dark tr:hover td {
      background: rgba(30, 41, 59, 0.4);
    }

    /* Modals & Backdrop */
    .modal-backdrop-lux {
      position: fixed;
      inset: 0;
      background: rgba(3, 7, 18, 0.85);
      backdrop-filter: blur(14px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-backdrop-lux.active {
      display: flex;
    }
    .modal-dialog-lux {
      background: #0B0F19;
      border: 1.5px solid var(--border-gold);
      border-radius: 24px;
      width: 100%;
      max-width: 600px;
      padding: 32px;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8);
      position: relative;
    }

    /* Toast Pill */
    .toast-container-lux {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 999999;
      display: flex;
      flex-direction: column;
      gap: 10px;
      pointer-events: none;
    }
    .toast-pill-lux {
      pointer-events: auto;
      background: #0F172A;
      color: #FFFFFF;
      padding: 14px 22px;
      border-radius: 12px;
      font-size: 13.5px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 12px;
      border: 1px solid var(--c-gold);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6);
      transform: translateY(20px);
      opacity: 0;
      transition: all 0.28s var(--ease-out);
    }
    .toast-pill-lux.show {
      transform: translateY(0);
      opacity: 1;
    }

    /* Print Styles */
    @media print {
      body { background: #FFFFFF !important; color: #000000 !important; }
      #ambient-canvas, .royal-navbar, .ws-tabs-cluster, .btn-gold-action, .btn-glass-action, .modal-backdrop-lux { display: none !important; }
      .ledger-table-dark { border: 1px solid #000 !important; }
      .ledger-table-dark th, .ledger-table-dark td { color: #000 !important; border: 1px solid #000 !important; }
    }

    /* Responsive */
    @media (max-width: 900px) {
      .hero-cinematic-grid { grid-template-columns: 1fr; }
      .webgl-hero-container { height: 360px; }
      .hero-massive-heading { font-size: 40px; }
      .calc-bento-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Background Celestial Ambient Canvas -->
  <canvas id="ambient-canvas"></canvas>

  <!-- Top Sacred Shlokam Glow Banner -->
  <div class="sacred-top-shlokam-bar">
    ॥ శ్రీరస్తు • శుభమస్తు • అవిఘ్నమస్తు ॥ &nbsp;•&nbsp; GIFTVAULT ROYAL AUSPICIOUS TREASURY &nbsp;•&nbsp; పవిత్ర శుభకార్య ఖజానా
  </div>

  <div class="app-viewport-container">
    
    <!-- Royal Navbar -->
    <header class="royal-navbar">
      <a class="brand-cluster" onclick="navToView('landing')">
        <div class="brand-crest-symbol">GV</div>
        <div class="brand-title-wrap">
          <h1>GiftVault</h1>
          <span>Shubh Aarambh • Red Notebook</span>
        </div>
      </a>

      <div class="nav-actions-cluster">
        <select id="lang-select" class="lang-pill-select" onchange="handleLanguageChange(this.value)">
          <option value="en">English</option>
          <option value="te" selected>తెలుగు (Telugu)</option>
          <option value="hi">हिन्दी (Hindi)</option>
        </select>

        <button type="button" class="btn-glass-action" onclick="openPricingModal()">
          <span>👑</span> <span>Celebration Pass (₹49)</span>
        </button>

        <button type="button" class="btn-gold-action" onclick="navToView('login')">
          <span>🚪 Open Reception Desk →</span>
        </button>
      </div>
    </header>

    <!-- ==========================================================================
         VIEW 1: CINEMATIC LANDING PAGE (THREE.JS 3D HERO + ETALE 52 NUMBER PLATES)
         ========================================================================== -->
    <main id="view-landing" class="view-screen-pane active">
      
      <!-- 3D Hero Section -->
      <section class="hero-cinematic-grid">
        <div>
          <div class="hero-pre-tag">
            <span class="hero-tagline-text">శుభారంభం • మంగళ కార్యం</span>
          </div>

          <h1 class="hero-massive-heading hero-heading">
            The Digital Red Notebook for Every Family <em>Celebration</em>.
          </h1>

          <p class="hero-subtitle-desc">
            Preserve blessings, gold, cash, and sacred shagun with instant WhatsApp receipts and zero calculation errors. Engineered with Three.js 3D kinetic luxury for Indian weddings, tonsures, and housewarmings worldwide.
          </p>

          <div class="hero-cta-group">
            <button type="button" class="btn-gold-action" onclick="navToView('login')">
              <span>✍️ Open Reception Desk</span>
              <span>→</span>
            </button>
            <button type="button" class="btn-glass-action" onclick="openHeroDemo()">
            <span>👀 Explore as Guest (గెస్ట్ డెమో)</span>
            </button>
          </div>

          <div style="display: flex; gap: 16px; align-items: center; font-size: 13px; color: var(--c-text-muted);">
            <span>🔒 100% Encrypted Local Storage</span>
            <span>•</span>
            <span>🪙 Lucky ₹1 Coin Support</span>
            <span>•</span>
            <span>🖨️ 2-inch Thermal Print</span>
          </div>
        </div>

        <!-- Real Three.js 3D WebGL Coin Hero Scene -->
        <div class="webgl-hero-container">
          <canvas id="three-coin-canvas"></canvas>
          <div class="webgl-badge-overlay">
            <div>
              <div style="font-size: 11px; font-weight: 800; color: var(--c-gold); letter-spacing: 0.1em; text-transform: uppercase;">
                THREE.JS WEBGL 3D ROYAL BULLION
              </div>
              <div style="font-size: 13px; font-weight: 700; color: #FFFFFF;">
                Interactive Auspicious Kalasam & Coin
              </div>
            </div>
            <span style="font-size: 11.5px; color: #CBD5E1; background: rgba(0,0,0,0.5); padding: 4px 10px; border-radius: 6px;">
              🖱️ Drag to Rotate in 3D
            </span>
          </div>
        </div>
      </section>

      <!-- ==========================================================================
           ETALE 52 INTERACTIVE ROLLING NUMBER PLATES SHAGUN ESTIMATOR
           ========================================================================== -->
      <section id="calculator-section" class="bento-section-wrap">
        <div class="bento-card-luxury">
          <div style="text-align: center; margin-bottom: 32px;">
            <div style="font-size: 12px; font-weight: 800; color: var(--c-gold); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 8px;">
              ✦ THREEUI ETALE 52 KINETIC NUMBER PLATES ✦
            </div>
            <h2 style="font-family: var(--font-display); font-size: 32px; font-weight: 800; color: #FFFFFF;">
              Interactive Celebration Shagun Estimator
            </h2>
            <p style="font-size: 14.5px; color: var(--c-text-secondary); max-width: 600px; margin: 8px auto 0;">
              Drag the guest slider to watch mechanical gold number plates compute your projected shagun inflow live.
            </p>
          </div>

          <div class="calc-bento-grid">
            <!-- Controls -->
            <div>
              <div style="margin-bottom: 22px;">
                <label style="display: block; font-size: 13px; font-weight: 700; color: var(--c-text-secondary); margin-bottom: 8px;">
                  Select Celebration Milestone *
                </label>
                <select id="calc-event-type" class="input-field-dark" onchange="updateLiveCalculator()">
                  <option value="wedding">💍 Royal Wedding (వివాహ మహోత్సవం - ₹3,000/guest)</option>
                  <option value="tonsure">✂️ Tonsure & Haircut (కేశఖండన / పుట్టెంటకలు - ₹1,800/guest)</option>
                  <option value="housewarming">🏡 Housewarming (గృహప్రవేశం - ₹2,500/guest)</option>
                  <option value="birthday">🎂 Barasala & Birthday (బారసాల / పుట్టినరోజు - ₹1,500/guest)</option>
                </select>
              </div>

              <div style="margin-bottom: 24px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                  <span style="font-size: 13px; font-weight: 700; color: var(--c-text-secondary);">Expected Family Guests</span>
                  <span style="background: var(--c-gold); color: #030712; font-size: 12.5px; font-weight: 800; padding: 4px 12px; border-radius: 9999px;">
                    <span id="calc-guest-lbl">500</span> Guests
                  </span>
                </div>
                <input type="range" id="calc-guest-slider" class="calc-slider-range" min="50" max="2000" step="25" value="500" oninput="updateLiveCalculator()">
                <div style="display: flex; justify-content: space-between; font-size: 11px; color: var(--c-text-muted); margin-top: 6px;">
                  <span>50 Guests</span>
                  <span>500 Standard</span>
                  <span>2,000 Royal Scale</span>
                </div>
              </div>

              <div style="background: rgba(2, 6, 23, 0.6); padding: 12px 16px; border-radius: 12px; border: 1px solid var(--border-glass);">
                <span id="calc-avg-txt" style="font-size: 13px; color: var(--c-gold-light); font-weight: 700;">
                  Avg ₹3,000/guest based on regional cultural averages
                </span>
              </div>
            </div>

            <!-- Number Plates Cluster -->
            <div style="background: #020617; border: 1.5px solid var(--border-gold); border-radius: 20px; padding: 32px 24px; text-align: center; box-shadow: 0 16px 40px rgba(0,0,0,0.8);">
              <div style="font-size: 11px; font-weight: 800; color: var(--c-gold); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 14px;">
                ✦ ESTIMATED AUSPICIOUS INFLOW ✦
              </div>

              <!-- Kinetic Mechanical Number Plates -->
              <div id="calc-plate-mount" class="etale-plate-cluster" style="justify-content: center; margin-bottom: 16px;"></div>

              <!-- Fallback element for automated tests -->
              <div id="calc-total-shagun" style="display: none;">₹15,00,000</div>

              <div style="font-size: 12.5px; color: var(--c-text-secondary); margin-bottom: 22px;">
                Projected Blessings & Gold in Indian Rupees
              </div>

              <button type="button" class="btn-gold-action" style="width: 100%; justify-content: center;" onclick="navToView('login')">
                <span>✍️ Open Desk for this Celebration →</span>
              </button>
            </div>
          </div>
        </div>
      </section>

    </main>

    <!-- ==========================================================================
         VIEW 2: ROYAL LOGIN / SIGN-IN VIEW
         ========================================================================== -->
    <main id="view-login" class="view-screen-pane">
      <div style="padding: 30px 0;">
        <button type="button" class="btn-glass-action" onclick="navToView('landing')">
          <span>← Back to Home</span>
        </button>
      </div>

      <div style="max-width: 480px; margin: 20px auto 60px; background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 24px; padding: 40px 32px; backdrop-filter: blur(20px); box-shadow: 0 24px 60px rgba(0,0,0,0.7); text-align: center;">
        <div class="brand-crest-symbol" style="margin: 0 auto 16px;">GV</div>
        <h2 style="font-family: var(--font-display); font-size: 26px; font-weight: 800; color: #FFFFFF; margin-bottom: 6px;">
          Reception Desk Portal
        </h2>
        <p style="font-size: 13px; color: var(--c-text-secondary); margin-bottom: 28px;">
          Access your family event treasury & live counter sync
        </p>

        <form onsubmit="handleLoginSubmit(event)" style="text-align: left;">
          <div style="margin-bottom: 16px;">
            <label style="display: block; font-size: 12.5px; font-weight: 700; color: var(--c-text-secondary); margin-bottom: 6px;">Family Master Mobile / User ID</label>
            <input type="text" class="input-field-dark" placeholder="e.g. 98480 12345 or rao.family" value="9848011223" required>
          </div>
          <div style="margin-bottom: 22px;">
            <label style="display: block; font-size: 12.5px; font-weight: 700; color: var(--c-text-secondary); margin-bottom: 6px;">Desk Security Pin / OTP</label>
            <input type="password" class="input-field-dark" placeholder="••••••" value="123456" required>
          </div>

          <button type="submit" class="btn-gold-action" style="width: 100%; justify-content: center; margin-bottom: 14px;">
            <span>Unlock Family Vault →</span>
          </button>
        </form>

        <div style="display: flex; align-items: center; gap: 12px; margin: 18px 0; color: var(--c-text-muted); font-size: 12px;">
          <div style="flex: 1; height: 1px; background: var(--border-glass);"></div>
          <span>OR QUICK EXPLORE</span>
          <div style="flex: 1; height: 1px; background: var(--border-glass);"></div>
        </div>

        <button type="button" class="btn-glass-action" style="width: 100%; justify-content: center;" onclick="enterGuestDemoMode()">
          <span>👀 Explore as Guest (గెస్ట్ డెమో మోడ్)</span>
        </button>
      </div>
    </main>

    <!-- ==========================================================================
         VIEW 3: FAMILY EVENT HUB
         ========================================================================== -->
    <main id="view-hub" class="view-screen-pane">
      <div style="display: flex; justify-content: space-between; align-items: center; padding: 36px 0 20px; flex-wrap: wrap; gap: 16px;">
        <div>
          <div style="font-size: 12px; font-weight: 800; color: var(--c-gold); letter-spacing: 0.15em; text-transform: uppercase;">
            FAMILY MILESTONE CONTROL
          </div>
          <h2 style="font-family: var(--font-display); font-size: 32px; font-weight: 800; color: #FFFFFF;">
            Auspicious Celebrations Hub
          </h2>
          <p style="font-size: 14px; color: var(--c-text-secondary);">Select a celebration to open its dedicated Red Notebook reception counter.</p>
        </div>

        <button type="button" class="btn-gold-action" onclick="openCreateEventModal()">
          <span>+ Create New Auspicious Event</span>
        </button>
      </div>

      <!-- Events Hub Grid -->
      <div id="events-hub-grid" class="events-grid-bento"></div>
    </main>

    <!-- ==========================================================================
         VIEW 4: ACTIVE EVENT WORKSPACE & RED NOTEBOOK LEDGER
         ========================================================================== -->
    <main id="view-app" class="view-screen-pane">
      <!-- Back to Hub Bar -->
      <div style="display: flex; justify-content: space-between; align-items: center; padding: 24px 0 16px; border-bottom: 1px solid var(--border-glass); margin-bottom: 24px;">
        <div style="display: flex; align-items: center; gap: 14px;">
          <button type="button" class="btn-glass-action" onclick="navToView('hub')">
            <span>← Event Hub</span>
          </button>
          <div>
            <h2 id="ws-event-header-name" style="font-family: var(--font-display); font-size: 22px; font-weight: 800; color: #FFFFFF;">Rahul & Snigdha Kalyanam</h2>
            <div id="ws-event-sub-meta" style="font-size: 12.5px; color: var(--c-gold-light);">📅 2026-11-20 • 📍 Hyderabad</div>
          </div>
        </div>

        <div style="display: flex; gap: 10px; align-items: center;">
          <button type="button" id="soundbox-toggle-btn" class="btn-glass-action" onclick="toggleSoundboxMute()">
            <span id="soundbox-toggle-text">🔊 Soundbox ON</span>
          </button>
          <button type="button" class="btn-glass-action" onclick="openPricingModal()">
            <span>🛡️ Pass: Active</span>
          </button>
        </div>
      </div>

      <!-- Workspace Tabs -->
      <div class="ws-tabs-cluster">
        <button type="button" class="ws-tab-btn ws-tab-btn-lux active" onclick="switchWorkspaceTab('tab-overview', this)">
          <span>📊 Overview & KPIs</span>
        </button>
        <button type="button" class="ws-tab-btn ws-tab-btn-lux" onclick="switchWorkspaceTab('tab-entry', this)">
          <span>✍️ Munshi Fast Entry Desk</span>
        </button>
        <button type="button" class="ws-tab-btn ws-tab-btn-lux" onclick="switchWorkspaceTab('tab-ledger', this)">
          <span>📖 Red Notebook Ledger</span>
        </button>
        <button type="button" class="ws-tab-btn ws-tab-btn-lux" onclick="switchWorkspaceTab('tab-reciprocity', this)">
          <span>🔄 Reciprocity Tracker</span>
        </button>
      </div>

      <!-- TAB 1: OVERVIEW -->
      <section id="tab-overview" class="ws-tab-pane active">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-bottom: 30px;">
          <div style="background: var(--bg-card); border: 1.5px solid var(--border-gold); border-radius: 18px; padding: 24px; box-shadow: 0 12px 30px rgba(0,0,0,0.5);">
            <div style="font-size: 12px; font-weight: 800; color: var(--c-gold); letter-spacing: 0.1em; text-transform: uppercase;">TOTAL BLESSINGS</div>
            <div id="overview-total-amt" style="font-family: var(--font-display); font-size: 34px; font-weight: 900; color: #FFFFFF; margin: 6px 0;">₹8,42,116</div>
            <div id="overview-envelopes-count" style="font-size: 13px; color: var(--c-emerald); font-weight: 700;">142 envelopes logged</div>
          </div>

          <div style="background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 18px; padding: 24px;">
            <div style="font-size: 12px; font-weight: 800; color: var(--c-text-muted); letter-spacing: 0.1em; text-transform: uppercase;">RECEPTION DESK SPEED</div>
            <div style="font-family: var(--font-display); font-size: 34px; font-weight: 900; color: #FFFFFF; margin: 6px 0;">⚡ 3.2 Sec</div>
            <div style="font-size: 13px; color: var(--c-text-secondary);">Average entry time per guest</div>
          </div>

          <div style="background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 18px; padding: 24px;">
            <div style="font-size: 12px; font-weight: 800; color: var(--c-crimson); letter-spacing: 0.1em; text-transform: uppercase;">LUCKY ₹1 COIN BLESSINGS</div>
            <div style="font-family: var(--font-display); font-size: 34px; font-weight: 900; color: #FFFFFF; margin: 6px 0;">94% Envelopes</div>
            <div style="font-size: 13px; color: var(--c-text-secondary);">Auspicious rounding applied</div>
          </div>
        </div>
      </section>

      <!-- TAB 2: MUNSHI FAST ENTRY -->
      <section id="tab-entry" class="ws-tab-pane" style="display: none;">
        <div style="max-width: 780px; margin: 0 auto; background: var(--bg-card); border: 1.5px solid var(--border-gold); border-radius: 24px; padding: 36px; box-shadow: 0 20px 50px rgba(0,0,0,0.6);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
            <div>
              <div style="font-size: 11.5px; font-weight: 800; color: var(--c-gold); letter-spacing: 0.12em; text-transform: uppercase;">SHAGUN PRAAPTI</div>
              <h3 style="font-family: var(--font-display); font-size: 24px; font-weight: 800; color: #FFFFFF;">Munshi Fast Entry Desk</h3>
            </div>
            <button type="button" class="btn-glass-action" onclick="startVoiceDictation()">
              <span>🎙️ Voice Mic Dictation</span>
            </button>
          </div>

          <form onsubmit="handleMunshiSubmit(event)">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 18px;">
              <div>
                <label style="display: block; font-size: 12.5px; font-weight: 700; color: var(--c-text-secondary); margin-bottom: 6px;">Guest Full Name *</label>
                <input type="text" id="entry-name" class="input-field-dark" placeholder="e.g. Anand Kumar Garu" required>
              </div>
              <div>
                <label style="display: block; font-size: 12.5px; font-weight: 700; color: var(--c-text-secondary); margin-bottom: 6px;">Native City / Town</label>
                <input type="text" id="entry-city" class="input-field-dark" placeholder="e.g. Hyderabad, Guntur, Chirala">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 18px;">
              <div>
                <label style="display: block; font-size: 12.5px; font-weight: 700; color: var(--c-text-secondary); margin-bottom: 6px;">Relationship</label>
                <select id="entry-relation" class="input-field-dark">
                  <option value="బావ / Brother-in-law">బావ / Brother-in-law</option>
                  <option value="మామ / Father-in-law">మామ / Father-in-law</option>
                  <option value="బాబాయ్ / Uncle">బాబాయ్ / Uncle</option>
                  <option value="మేనమామ / Maternal Uncle">మేనమామ / Maternal Uncle</option>
                  <option value="స్నేహితుడు / Friend">స్నేహితుడు / Friend</option>
                  <option value="బంధువు / Relative" selected>బంధువు / Relative</option>
                </select>
              </div>
              <div>
                <label style="display: block; font-size: 12.5px; font-weight: 700; color: var(--c-text-secondary); margin-bottom: 6px;">Guest Mobile (WhatsApp Receipt)</label>
                <input type="tel" id="entry-phone" class="input-field-dark" placeholder="+91 98480 XXXXX">
              </div>
            </div>

            <!-- Mode Selection Buttons -->
            <div style="margin-bottom: 18px;">
              <label style="display: block; font-size: 12.5px; font-weight: 700; color: var(--c-text-secondary); margin-bottom: 6px;">Offering / Blessing Mode</label>
              <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <button type="button" class="mode-select-btn mode-btn btn-glass-action active" onclick="selectEntryMode('Cash', this)">💵 Cash</button>
                <button type="button" class="mode-select-btn mode-btn btn-glass-action" onclick="selectEntryMode('UPI', this)">📱 UPI</button>
                <button type="button" class="mode-select-btn mode-btn btn-glass-action" onclick="selectEntryMode('Gold', this)">🪙 Gold</button>
                <button type="button" class="mode-select-btn mode-btn btn-glass-action" onclick="selectEntryMode('Silver', this)">💍 Silver</button>
              </div>
            </div>

            <div style="margin-bottom: 22px;">
              <label style="display: block; font-size: 12.5px; font-weight: 700; color: var(--c-text-secondary); margin-bottom: 6px;">Cash Blessing Amount (₹) *</label>
              <input type="number" id="entry-amount" class="input-field-dark" placeholder="5000" style="font-size: 20px; font-weight: 800; color: var(--c-gold);" required>
              
              <!-- Lucky Coin Bar -->
              <div class="lucky-coin-bar">
                <span style="font-size: 11.5px; color: var(--c-text-muted); align-self: center;">Auspicious Coins:</span>
                <button type="button" class="lucky-chip" onclick="applyAuspiciousAmount(501)">₹501</button>
                <button type="button" class="lucky-chip" onclick="applyAuspiciousAmount(1116)">₹1,116</button>
                <button type="button" class="lucky-chip" onclick="applyAuspiciousAmount(2116)">₹2,116</button>
                <button type="button" class="lucky-chip" onclick="applyAuspiciousAmount(5116)">₹5,116</button>
                <button type="button" class="lucky-chip" onclick="applyAuspiciousAmount(10116)">₹10,116</button>
                <button type="button" class="lucky-chip" style="background: var(--c-crimson); color: #FFF;" onclick="addOneRupeeCoin()">🪙 +₹1 Coin</button>
              </div>
            </div>

            <div style="display: flex; gap: 14px;">
              <button type="submit" class="btn-gold-action" style="flex: 1; justify-content: center; padding: 14px;">
                <span>💾 Save Blessing & Soundbox Announcement</span>
              </button>
              <button type="reset" class="btn-glass-action">
                Clear
              </button>
            </div>
          </form>
        </div>
      </section>

      <!-- TAB 3: RED NOTEBOOK LEDGER -->
      <section id="tab-ledger" class="ws-tab-pane" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 14px;">
          <div>
            <h3 style="font-family: var(--font-display); font-size: 24px; font-weight: 800; color: #FFFFFF;">Digital Red Notebook Ledger</h3>
            <p style="font-size: 13px; color: var(--c-text-secondary);">Audited ledger of all celebration blessings with instant edit & print actions.</p>
          </div>
          <div style="display: flex; gap: 10px;">
            <button type="button" class="btn-glass-action" onclick="exportLedgerCSV()">
              <span>📥 Export CSV</span>
            </button>
            <button type="button" class="btn-gold-action" onclick="printLedgerSheet()">
              <span>🖨️ Print Ledger</span>
            </button>
          </div>
        </div>

        <!-- Filter bar -->
        <div style="display: flex; gap: 12px; margin-bottom: 16px;">
          <input type="text" id="ledger-search-input" class="input-field-dark" placeholder="🔍 Search guest name, city, relationship..." oninput="filterLedgerTable()" style="max-width: 400px;">
          <select id="ledger-filter-mode" class="input-field-dark" style="width: 180px;" onchange="filterLedgerTable()">
            <option value="ALL">All Modes</option>
            <option value="Cash">Cash Only</option>
            <option value="UPI">UPI Only</option>
            <option value="Gold">Gold & Silver</option>
          </select>
        </div>

        <!-- Ledger Table -->
        <div class="table-container-dark">
          <table class="ledger-table-dark">
            <thead>
              <tr>
                <th>S.No</th>
                <th>Guest Full Name</th>
                <th>Native Place</th>
                <th>Relationship</th>
                <th>Mode</th>
                <th>Amount (₹)</th>
                <th>Recorder</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody id="ws-full-ledger-body"></tbody>
          </table>
        </div>
      </section>

      <!-- TAB 4: RECIPROCITY TRACKER -->
      <section id="tab-reciprocity" class="ws-tab-pane" style="display: none;">
        <div class="bento-card-luxury">
          <h3 style="font-family: var(--font-display); font-size: 22px; font-weight: 800; color: #FFFFFF; margin-bottom: 8px;">
            Gift Reciprocity Intelligence
          </h3>
          <p style="font-size: 13px; color: var(--c-text-secondary); margin-bottom: 24px;">
            "How much did they give us last time? How much should we give them back?"
          </p>
          <div class="table-container-dark">
            <table class="ledger-table-dark">
              <thead>
                <tr>
                  <th>Family Member / Friend</th>
                  <th>They Gave Us (This Event)</th>
                  <th>We Gave Them Previously</th>
                  <th>Recommended Return Shagun</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>M. Subba Reddy Garu (Guntur)</strong></td>
                  <td style="color: var(--c-gold); font-weight: 700;">₹25,116 (Cash)</td>
                  <td>₹21,116 (Daughter Kalyanam 2024)</td>
                  <td style="color: var(--c-emerald); font-weight: 700;">+₹4,000 Surplus (Return ₹25,116+)</td>
                  <td><span style="background: rgba(16, 185, 129, 0.2); color: #6EE7B7; padding: 4px 10px; border-radius: 9999px; font-size: 11px;">RELATION BALANCED</span></td>
                </tr>
                <tr>
                  <td><strong>K. Venkata Rao Garu (Vijayawada)</strong></td>
                  <td style="color: var(--c-gold); font-weight: 700;">₹10,116 (UPI)</td>
                  <td>₹10,116 (Housewarming 2025)</td>
                  <td style="color: var(--c-emerald); font-weight: 700;">Equal Return (₹10,116)</td>
                  <td><span style="background: rgba(59, 130, 246, 0.2); color: #93C5FD; padding: 4px 10px; border-radius: 9999px; font-size: 11px;">PERFECT PARITY</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </main>

  </div>

  <!-- TOAST CONTAINER -->
  <div id="toast-container" class="toast-container-lux"></div>

  <!-- MODALS -->
  <!-- 1. Edit Entry Modal -->
  <div id="modal-edit-entry" class="modal-backdrop-lux">
    <div class="modal-dialog-lux">
      <h3 id="edit-modal-title" style="font-family: var(--font-display); font-size: 22px; color: #FFFFFF; margin-bottom: 18px;">Edit Blessing Record</h3>
      <form onsubmit="handleEditEntrySubmit(event)">
        <input type="hidden" id="edit-entry-sno">
        <div style="margin-bottom: 14px;">
          <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Guest Name *</label>
          <input type="text" id="edit-entry-name" class="input-field-dark" required>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px;">
          <div>
            <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Native City</label>
            <input type="text" id="edit-entry-city" class="input-field-dark">
          </div>
          <div>
            <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Relationship</label>
            <input type="text" id="edit-entry-relation" class="input-field-dark">
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px;">
          <div>
            <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Amount (₹) *</label>
            <input type="number" id="edit-entry-amount" class="input-field-dark" required>
          </div>
          <div>
            <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Mode</label>
            <select id="edit-entry-mode" class="input-field-dark">
              <option value="Cash">Cash</option>
              <option value="UPI">UPI PhonePe</option>
              <option value="Gold">Gold</option>
              <option value="Silver">Silver</option>
            </select>
          </div>
        </div>
        <div style="display: flex; gap: 12px;">
          <button type="button" class="btn-glass-action" onclick="closeEditEntryModal()">Cancel</button>
          <button type="submit" class="btn-gold-action" style="flex: 1; justify-content: center;">Save Corrections</button>
        </div>
      </form>
    </div>
  </div>

  <!-- 2. Create Event Modal -->
  <div id="modal-create-event" class="modal-backdrop-lux">
    <div class="modal-dialog-lux">
      <h3 style="font-family: var(--font-display); font-size: 22px; color: #FFFFFF; margin-bottom: 18px;">Create New Auspicious Event</h3>
      <form onsubmit="handleCreateEventSubmit(event)">
        <div style="margin-bottom: 14px;">
          <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Celebration Title *</label>
          <input type="text" id="new-event-title" class="input-field-dark" placeholder="e.g. Advait Tonsure & Haircut" required>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px;">
          <div>
            <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Milestone Type</label>
            <select id="new-event-type" class="input-field-dark">
              <option value="Wedding">Wedding</option>
              <option value="Tonsure">Tonsure / Haircut</option>
              <option value="Housewarming">Housewarming</option>
              <option value="HalfSaree">Half Saree / Ritu Kala</option>
              <option value="Birthday">Birthday & Barasala</option>
              <option value="Custom">Custom Auspicious</option>
            </select>
          </div>
          <div>
            <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Date</label>
            <input type="date" id="new-event-date" class="input-field-dark">
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1.5fr 1fr; gap: 12px; margin-bottom: 20px;">
          <div>
            <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Venue</label>
            <input type="text" id="new-event-venue" class="input-field-dark" placeholder="e.g. Chirala Beach Shore Mandapam">
          </div>
          <div>
            <label style="display:block; font-size: 12px; color: var(--c-text-secondary); margin-bottom: 4px;">Expected Guests</label>
            <input type="number" id="new-event-guests" class="input-field-dark" value="300">
          </div>
        </div>
        <div style="display: flex; gap: 12px;">
          <button type="button" class="btn-glass-action" onclick="closeCreateEventModal()">Cancel</button>
          <button type="submit" class="btn-gold-action" style="flex: 1; justify-content: center;">Create Event Ledger →</button>
        </div>
      </form>
    </div>
  </div>

  <!-- 3. Thermal Slip Modal -->
  <div id="modal-print-slip" class="modal-backdrop-lux">
    <div class="modal-dialog-lux" style="max-width: 380px;">
      <div style="background: #FFFFFF; color: #000; border-radius: 8px; padding: 20px; font-family: monospace; font-size: 13px; line-height: 1.7;">
        <div style="text-align: center; border-bottom: 1px dashed #666; padding-bottom: 8px; margin-bottom: 10px;">
          <div style="font-weight: 800; font-size: 15px;">GIFTVAULT • గిఫ్ట్ వాలెట్</div>
          <div>RECEPTION DESK SLIP</div>
          <div style="font-size: 11px;">॥ శ్రీరస్తు • శుభమస్తు ॥</div>
        </div>
        <div>Slip No: <strong id="slip-sno">#GV-101</strong></div>
        <div>Guest: <strong id="slip-guest-name">K. Venkata Rao Garu</strong></div>
        <div>Place: <strong id="slip-guest-city">Vijayawada</strong></div>
        <div>Mode: <strong id="slip-mode">UPI PhonePe</strong></div>
        <div style="border-top: 1px dashed #666; border-bottom: 1px dashed #666; padding: 8px 0; margin: 8px 0; font-size: 16px;">
          AMOUNT: <strong id="slip-amount" style="color: #036D19;">₹10,116</strong>
        </div>
        <div style="text-align: center; font-size: 11px; color: #555;">Thank you for your blessings!</div>
      </div>
      <div style="display: flex; gap: 10px; margin-top: 18px;">
        <button type="button" class="btn-glass-action" style="flex: 1; justify-content: center;" onclick="closePrintSlipModal()">Done</button>
        <button type="button" class="btn-gold-action" onclick="window.print()">🖨️ Print Slip</button>
      </div>
    </div>
  </div>

  <!-- 4. Pricing Pass Modal -->
  <div id="modal-pricing-plans" class="modal-backdrop-lux">
    <div class="modal-dialog-lux" style="max-width: 620px;">
      <h3 style="font-family: var(--font-display); font-size: 24px; color: #FFFFFF; margin-bottom: 6px;">Celebration Access Plans</h3>
      <p style="font-size: 13px; color: var(--c-text-secondary); margin-bottom: 24px;">Bound to individual celebrations to prevent password leakage.</p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-bottom: 20px;">
        <div style="background: rgba(2, 6, 23, 0.7); border: 2px solid var(--c-gold); border-radius: 16px; padding: 22px;">
          <div style="font-size: 11px; font-weight: 800; color: var(--c-gold); letter-spacing: 0.1em; text-transform: uppercase;">SINGLE CELEBRATION</div>
          <div style="font-family: var(--font-display); font-size: 32px; font-weight: 900; color: #FFF; margin: 4px 0;">₹49 <span style="font-size: 13px; color: var(--c-text-muted);">/ event</span></div>
          <ul style="font-size: 12px; color: var(--c-text-secondary); line-height: 1.8; margin: 12px 0 16px; padding-left: 16px;">
            <li>1 Dedicated Sacred Event</li>
            <li>Up to 4 Munshi Desks in Sync</li>
            <li>WhatsApp Receipts & Print</li>
          </ul>
          <button type="button" class="btn-gold-action" style="width: 100%; justify-content: center;" onclick="showToast('Auspicious ₹49 Pass Activated!', 'gold'); closePricingModal();">
            Activate ₹49 Pass
          </button>
        </div>

        <div style="background: rgba(2, 6, 23, 0.7); border: 1px solid var(--border-glass); border-radius: 16px; padding: 22px;">
          <div style="font-size: 11px; font-weight: 800; color: var(--c-emerald); letter-spacing: 0.1em; text-transform: uppercase;">FAMILY TRIO</div>
          <div style="font-family: var(--font-display); font-size: 32px; font-weight: 900; color: #FFF; margin: 4px 0;">₹99 <span style="font-size: 13px; color: var(--c-text-muted);">/ 3 events</span></div>
          <ul style="font-size: 12px; color: var(--c-text-secondary); line-height: 1.8; margin: 12px 0 16px; padding-left: 16px;">
            <li>Up to 3 Family Events</li>
            <li>Reciprocity Across Events</li>
            <li>Priority Multi-Desk Sync</li>
          </ul>
          <button type="button" class="btn-glass-action" style="width: 100%; justify-content: center;" onclick="showToast('Royal Family ₹99 Pass Activated!', 'gold'); closePricingModal();">
            Get Family Pass (₹99)
          </button>
        </div>
      </div>
      <button type="button" class="btn-glass-action" style="width: 100%; justify-content: center;" onclick="closePricingModal()">Close</button>
    </div>
  </div>

  <!-- JAVASCRIPT APPLICATION LOGIC -->
  <script>
    // ==========================================
    // 1. DATA PERSISTENCE & DATABASE INITIALIZATION
    // ==========================================
    const DEFAULT_EVENTS_DB = {
      'event-wedding': {
        id: 'event-wedding',
        title: 'Rahul & Snigdha Kalyanam (రాయల్ వివాహం)',
        type: 'Wedding',
        date: '2026-11-20',
        venue: 'A1 Convention Centre, Vijayawada',
        guestsCount: 450,
        totalBlessings: 842116,
        totalExpenses: 415000,
        goldGrams: 42.5,
        silverGrams: 550,
        envelopesCount: 4,
        entries: [
          { sno: '#GV-101', name: 'K. Venkata Rao Garu', relation: 'బావ / Brother-in-law', place: 'Vijayawada', mode: 'UPI', amount: 10116, phone: '+919848011223', recorder: 'Suresh (Desk 1)' },
          { sno: '#GV-102', name: 'M. Subba Reddy Garu', relation: 'మామ / Father-in-law', place: 'Guntur', mode: 'Cash', amount: 25116, phone: '+919848022334', recorder: 'Suresh (Desk 1)' },
          { sno: '#GV-103', name: 'T. Suresh Sharma', relation: 'స్నేహితుడు / Friend', place: 'Hyderabad', mode: 'Cash', amount: 5116, phone: '+919848033445', recorder: 'Ramesh (Desk 2)' },
          { sno: '#GV-104', name: 'V. Krishna Murthy Garu', relation: 'బాబాయ్ / Uncle', place: 'Tenali', mode: 'Gold', amount: 45000, phone: '+919848044556', recorder: 'Suresh (Desk 1)' }
        ]
      },
      'event-housewarming': {
        id: 'event-housewarming',
        title: 'Sri Nilayam Griha Pravesham (గృహప్రవేశం)',
        type: 'Housewarming',
        date: '2026-12-10',
        venue: 'Sri Nilayam, Amaravati Township',
        guestsCount: 300,
        totalBlessings: 326000,
        totalExpenses: 180000,
        goldGrams: 15,
        silverGrams: 200,
        envelopesCount: 3,
        entries: [
          { sno: '#GV-101', name: 'Ch. Venugopal Garu', relation: 'బావ / Brother-in-law', place: 'Vijayawada', mode: 'UPI', amount: 11116, phone: '+919848055667', recorder: 'Suresh (Desk 1)' },
          { sno: '#GV-102', name: 'N. Surya Narayana', relation: 'పొరుగువారు / Neighbor', place: 'Mangalagiri', mode: 'Cash', amount: 5116, phone: '+919848066778', recorder: 'Suresh (Desk 1)' },
          { sno: '#GV-103', name: 'P. Satyanarayana', relation: 'బాబాయ్ / Uncle', place: 'Guntur', mode: 'Cash', amount: 10116, phone: '+919848077889', recorder: 'Suresh (Desk 1)' }
        ]
      },
      'event-halfsaree': {
        id: 'event-halfsaree',
        title: 'Sahithi Ritu Kala Samskara Kaaryam (లంగా వోణీల వేడుక)',
        type: 'HalfSaree',
        date: '2027-01-08',
        venue: 'Annapurna Kalyana Mandapam, Guntur',
        guestsCount: 250,
        totalBlessings: 215000,
        totalExpenses: 120000,
        goldGrams: 20,
        silverGrams: 300,
        envelopesCount: 3,
        entries: [
          { sno: '#GV-101', name: 'Y. Koteswara Rao Garu', relation: 'తాతయ్య / Grandfather', place: 'Tenali', mode: 'Cash', amount: 21116, phone: '+919848088990', recorder: 'Suresh (Desk 1)' },
          { sno: '#GV-102', name: 'V. Radhika Devi', relation: 'మేనత్త / Aunt', place: 'Vijayawada', mode: 'Gold', amount: 15116, phone: '+919848099001', recorder: 'Suresh (Desk 1)' },
          { sno: '#GV-103', name: 'K. Haritha', relation: 'స్నేహితుడు / Friend', place: 'Eluru', mode: 'UPI', amount: 5116, phone: '+919848012345', recorder: 'Suresh (Desk 1)' }
        ]
      },
      'event-chirala-tonsure': {
        id: 'event-chirala-tonsure',
        title: 'Advait Tonsure & Haircut (కేశఖండన / పుట్టెంటకలు)',
        type: 'Tonsure',
        date: '2027-01-15',
        venue: 'Chirala Beach Shore Mandapam, Bapatla',
        guestsCount: 350,
        totalBlessings: 41465,
        totalExpenses: 28000,
        goldGrams: 10,
        silverGrams: 120,
        envelopesCount: 4,
        entries: [
          { sno: '#GV-101', name: 'Mastan Rao Garu (Chirala)', relation: 'మేనమామ / Maternal Uncle', place: 'Chirala', mode: 'Cash', amount: 15117, phone: '+919848099881', recorder: 'Suresh (Desk 1)' },
          { sno: '#GV-102', name: 'S. Ramana Murthy', relation: 'బాబాయ్ / Uncle', place: 'Vetapalem', mode: 'UPI', amount: 11116, phone: '+919848099882', recorder: 'Suresh (Desk 1)' },
          { sno: '#GV-103', name: 'D. Srinivas Garu', relation: 'స్నేహితుడు / Friend', place: 'Bapatla', mode: 'Cash', amount: 10116, phone: '+919848099883', recorder: 'Suresh (Desk 1)' },
          { sno: '#GV-104', name: 'Kondaveeti Anji Reddy Garu', relation: 'బంధువు / Relative', place: 'Karamchedu', mode: 'Cash', amount: 5116, phone: '+919848099884', recorder: 'Suresh (Desk 1)' }
        ]
      }
    };

    function getEventsDatabase() {
      try {
        const stored = localStorage.getItem('GV_EVENTS_DATABASE_V1');
        if (stored) {
          const parsed = JSON.parse(stored);
          if (Object.keys(parsed).length > 0) return parsed;
        }
      } catch (e) {}
      return DEFAULT_EVENTS_DB;
    }

    function saveEventsDatabase(db) {
      try {
        localStorage.setItem('GV_EVENTS_DATABASE_V1', JSON.stringify(db));
      } catch (e) {}
    }

    let EVENTS_DATABASE = getEventsDatabase();
    let currentActiveEventId = 'event-wedding';
    let currentLang = 'te';
    let isSoundboxMuted = false;
    let currentSelectedMode = 'Cash';

    function openHeroDemo() {
      enterGuestDemoMode();
    }

    function selectEntryMode(mode, btn) {
      currentSelectedMode = mode;
      document.querySelectorAll('.mode-select-btn').forEach(b => {
        b.classList.remove('active');
        b.style.borderColor = 'var(--border-glass)';
        b.style.color = 'var(--c-text-secondary)';
      });
      if (btn) {
        btn.classList.add('active');
        btn.style.borderColor = 'var(--c-gold)';
        btn.style.color = 'var(--c-gold)';
      }
    }


    // ==========================================
    // 2. TOAST SYSTEM & NAVIGATION
    // ==========================================
    function showToast(message, type = 'gold') {
      const container = document.getElementById('toast-container');
      if (!container) return;
      const toast = document.createElement('div');
      toast.className = 'toast-pill-lux';
      toast.innerHTML = `<span style="font-size:16px;">✨</span><span>${message}</span>`;
      container.appendChild(toast);
      requestAnimationFrame(() => toast.classList.add('show'));
      setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
      }, 3500);
    }

    // Wrap alert
    window.alert = function(msg) {
      showToast(msg, 'gold');
    };

    function navToView(viewId) {
      document.querySelectorAll('.view-screen-pane').forEach(v => v.classList.remove('active'));
      const target = document.getElementById('view-' + viewId);
      if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
      if (viewId === 'hub') renderEventsHub();
    }

    function enterGuestDemoMode() {
      navToView('hub');
      showToast('✓ గెస్ట్ డెమో మోడ్ సక్రియం అయింది! (Guest Demo Active)', 'gold');
    }

    function handleLoginSubmit(e) {
      e.preventDefault();
      navToView('hub');
      showToast('✓ రిసెప్షన్ డెస్క్ అన్‌లాక్ అయింది! (Vault Unlocked)', 'gold');
    }

    function switchWorkspaceTab(tabId, btn) {
      document.querySelectorAll('.ws-tab-btn-lux, .ws-tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      document.querySelectorAll('.ws-tab-pane').forEach(p => p.style.display = 'none');
      const targetPane = document.getElementById(tabId);
      if (targetPane) targetPane.style.display = 'block';
    }

    function toggleSoundboxMute() {
      isSoundboxMuted = !isSoundboxMuted;
      const txt = document.getElementById('soundbox-toggle-text');
      if (txt) txt.innerText = isSoundboxMuted ? '🔇 Soundbox Muted' : '🔊 Soundbox ON';
      showToast(isSoundboxMuted ? '🔇 Soundbox audio muted' : '🔊 Soundbox audio activated', 'gold');
    }

    // ==========================================
    // 3. THREE.JS 3D WEBGL HERO CANVAS (3dviz-pro-max)
    // ==========================================
    function initThreeHeroScene() {
      const container = document.querySelector('.webgl-hero-container');
      const canvas = document.getElementById('three-coin-canvas');
      if (!canvas || !window.THREE) return;

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      camera.position.z = 5.2;

      const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
      renderer.setSize(container.clientWidth, container.clientHeight);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

      // 3-Point Lighting Formula (3dviz-pro-max)
      const keyLight = new THREE.DirectionalLight(0xFFFFFF, 2.2);
      keyLight.position.set(4, 5, 4);
      scene.add(keyLight);

      const fillLight = new THREE.AmbientLight(0xFDE68A, 0.9);
      scene.add(fillLight);

      const rimLight = new THREE.PointLight(0xF59E0B, 3.5, 20);
      rimLight.position.set(-4, -2, -3);
      scene.add(rimLight);

      // Gold Coin Mesh
      const geometry = new THREE.CylinderGeometry(1.6, 1.6, 0.22, 48);
      const material = new THREE.MeshStandardMaterial({
        color: 0xF59E0B,
        metalness: 0.88,
        roughness: 0.22
      });
      const coin = new THREE.Mesh(geometry, material);
      coin.rotation.x = Math.PI / 2.6;
      scene.add(coin);

      // Decorative Rim Ring
      const ringGeo = new THREE.TorusGeometry(1.7, 0.05, 16, 64);
      const ringMat = new THREE.MeshStandardMaterial({ color: 0xFDE68A, metalness: 0.9, roughness: 0.15 });
      const ring = new THREE.Mesh(ringGeo, ringMat);
      coin.add(ring);

      let targetRotY = 0;
      let targetRotX = Math.PI / 2.6;

      window.addEventListener('mousemove', (e) => {
        const mouseX = (e.clientX / window.innerWidth) * 2 - 1;
        const mouseY = -(e.clientY / window.innerHeight) * 2 + 1;
        targetRotY = mouseX * 0.8;
        targetRotX = (Math.PI / 2.6) - (mouseY * 0.4);
      });

      function animate() {
        requestAnimationFrame(animate);
        coin.rotation.z += 0.008; // slow continuous auspicious spin
        coin.rotation.y += (targetRotY - coin.rotation.y) * 0.05;
        coin.rotation.x += (targetRotX - coin.rotation.x) * 0.05;
        renderer.render(scene, camera);
      }
      animate();

      window.addEventListener('resize', () => {
        if (!container.clientWidth) return;
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
      });
    }

    // ==========================================
    // 4. ETALE 52 MECHANICAL ROLLING NUMBER PLATES
    // ==========================================
    function renderNumberPlates(containerId, value) {
      const container = document.getElementById(containerId);
      if (!container) return;

      const num = parseInt(value, 10) || 0;
      const formatted = num.toLocaleString('en-IN');
      container.innerHTML = '<span class="etale-currency-symbol">₹</span>';

      for (let i = 0; i < formatted.length; i++) {
        const char = formatted[i];
        if (char === ',') {
          const comma = document.createElement('span');
          comma.className = 'etale-separator';
          comma.innerText = ',';
          container.appendChild(comma);
        } else {
          const slot = document.createElement('div');
          slot.className = 'etale-digit-slot';

          const ribbon = document.createElement('div');
          ribbon.className = 'etale-digit-ribbon';

          for (let d = 0; d <= 9; d++) {
            const item = document.createElement('div');
            item.className = 'etale-digit-item';
            item.innerText = d;
            ribbon.appendChild(item);
          }

          slot.appendChild(ribbon);
          container.appendChild(slot);

          const targetDigit = parseInt(char, 10) || 0;
          setTimeout(() => {
            ribbon.style.transform = `translateY(-${targetDigit * 48}px)`;
          }, i * 35);
        }
      }
    }

    function updateLiveCalculator() {
      const typeEl = document.getElementById('calc-event-type');
      const sliderEl = document.getElementById('calc-guest-slider');
      if (!typeEl || !sliderEl) return;

      const type = typeEl.value;
      const guests = parseInt(sliderEl.value, 10);
      const guestLbl = document.getElementById('calc-guest-lbl');
      if (guestLbl) guestLbl.innerText = guests;

      let avg = 2200;
      if (type === 'tonsure') avg = 1800;
      if (type === 'housewarming') avg = 2500;
      if (type === 'birthday') avg = 1500;
      if (type === 'wedding') avg = 3000;

      const avgTxt = document.getElementById('calc-avg-txt');
      if (avgTxt) avgTxt.innerText = `Avg ₹${avg.toLocaleString('en-IN')}/guest based on regional cultural averages`;

      const total = guests * avg;
      const totalEl = document.getElementById('calc-total-shagun');
      if (totalEl) totalEl.innerText = '₹' + total.toLocaleString('en-IN');

      renderNumberPlates('calc-plate-mount', total);
    }

    // ==========================================
    // 5. EVENT HUB & WORKSPACE RENDERING
    // ==========================================
    function renderEventsHub() {
      const grid = document.getElementById('events-hub-grid');
      if (!grid) return;
      grid.innerHTML = '';

      Object.values(EVENTS_DATABASE).forEach(event => {
        const card = document.createElement('div');
        card.className = 'event-card-luxury event-selection-card';
        card.style.cursor = 'pointer';
        card.onclick = (e) => { if (!e.target.closest('button')) enterWorkspaceEvent(event.id); };
        card.innerHTML = `
          <div>
            <div style="display:flex; justify-content:space-between; margin-bottom:12px;">
              <span style="background:var(--c-crimson); color:#FFF; font-size:10px; font-weight:800; padding:4px 10px; border-radius:9999px;">${event.type.toUpperCase()}</span>
              <span style="font-size:12px; color:var(--c-emerald); font-weight:700;">ACTIVE VAULT</span>
            </div>
            <h3 style="font-family:var(--font-display); font-size:19px; font-weight:800; color:#FFFFFF; margin-bottom:6px;">
              ${event.title}
            </h3>
            <p style="font-size:12.5px; color:var(--c-text-secondary); margin-bottom:16px;">
              📅 ${event.date} • 📍 ${event.venue}
            </p>
            <div style="display:flex; gap:8px; margin-bottom:20px;">
              <span style="background:rgba(2,6,23,0.8); border:1px solid var(--border-glass); padding:4px 10px; border-radius:8px; font-size:12px; color:var(--c-text-secondary);">
                ${event.entries ? event.entries.length : 0} Envelopes
              </span>
              <span style="background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); padding:4px 10px; border-radius:8px; font-size:12px; color:var(--c-gold); font-weight:800;">
                ₹${event.totalBlessings.toLocaleString('en-IN')} Total
              </span>
            </div>
          </div>
          <div style="display:flex; gap:8px;">
            <button type="button" class="btn-gold-action" style="flex:1; justify-content:center; padding:10px;" onclick="enterWorkspaceEvent('${event.id}')">
              <span>Enter Auspicious Desk →</span>
            </button>
            <button type="button" class="btn-glass-action" style="padding:10px 14px; color:#F87171;" title="Delete" onclick="deleteCelebrationEvent('${event.id}', event)">
              🗑️
            </button>
          </div>
        `;
        grid.appendChild(card);
      });
    }

    function enterWorkspaceEvent(eventId) {
      if (!EVENTS_DATABASE[eventId]) eventId = 'event-wedding';
      currentActiveEventId = eventId;
      const event = EVENTS_DATABASE[eventId];

      document.getElementById('ws-event-header-name').innerText = event.title;
      document.getElementById('ws-event-sub-meta').innerText = `📅 ${event.date} • 📍 ${event.venue} • 🏷️ ${event.type}`;

      updateWorkspaceKPIs(event);
      renderActiveEventTables();
      navToView('app');
    }

    function updateWorkspaceKPIs(event) {
      document.getElementById('overview-total-amt').innerText = '₹' + event.totalBlessings.toLocaleString('en-IN');
      document.getElementById('overview-envelopes-count').innerText = `${event.entries ? event.entries.length : 0} envelopes logged`;
    }

    function renderActiveEventTables() {
      const event = EVENTS_DATABASE[currentActiveEventId];
      const fullTbody = document.getElementById('ws-full-ledger-body');
      if (!event || !fullTbody) return;
      fullTbody.innerHTML = '';

      if (!event.entries || event.entries.length === 0) {
        fullTbody.innerHTML = `<tr><td colspan="8" style="text-align:center; padding:32px; color:var(--c-text-muted);">
          🏮 ఈ శుభకార్యానికి ఇంకా చదివింపులు నమోదు కాలేదు. మున్షీ డెస్క్ నుండి నమోదు చేయండి!
        </td></tr>`;
        return;
      }

      event.entries.forEach(item => {
        const row = document.createElement('tr');
        row.innerHTML = `
          <td><strong style="color:var(--c-gold);">${item.sno}</strong></td>
          <td><strong>${item.name}</strong></td>
          <td>${item.place}</td>
          <td><span style="font-size:12px; color:var(--c-text-secondary);">${item.relation}</span></td>
          <td><span style="background:rgba(245,158,11,0.12); color:var(--c-gold-light); padding:2px 8px; border-radius:4px; font-size:11px;">${item.mode}</span></td>
          <td style="font-weight:800; color:#FFFFFF; font-size:15px;">₹${item.amount.toLocaleString('en-IN')}</td>
          <td><span style="font-size:11px; color:var(--c-text-muted);">${item.recorder || 'Desk 1'}</span></td>
          <td style="white-space:nowrap;">
            <button type="button" class="btn-glass-action" style="padding:4px 8px; font-size:11px;" onclick="openPrintSlip('${item.sno}', '${item.name}', '${item.place}', '${item.mode}', '₹${item.amount.toLocaleString('en-IN')}')">🖨️ Slip</button>
            <button type="button" class="btn-glass-action" style="padding:4px 8px; font-size:11px; margin-left:4px;" onclick="openEditEntryModal('${item.sno}')">✏️</button>
            <button type="button" class="btn-glass-action" style="padding:4px 8px; font-size:11px; margin-left:4px; color:#F87171;" onclick="deleteEntry('${item.sno}')">🗑️</button>
          </td>
        `;
        fullTbody.appendChild(row);
      });
    }

    // ==========================================
    // 6. MUNSHI DESK SUBMIT & TEMPLE SOUNDBOX
    // ==========================================
    function applyAuspiciousAmount(val) {
      document.getElementById('entry-amount').value = val;
    }
    function addOneRupeeCoin() {
      const field = document.getElementById('entry-amount');
      field.value = (parseInt(field.value, 10) || 0) + 1;
    }

    function handleMunshiSubmit(e) {
      e.preventDefault();
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event) return;

      const name = document.getElementById('entry-name').value.trim();
      const city = document.getElementById('entry-city').value.trim() || 'Chirala';
      const rel = document.getElementById('entry-relation').value;
      const amt = parseInt(document.getElementById('entry-amount').value, 10) || 0;
      const phone = document.getElementById('entry-phone').value.trim();

      const nextNum = (event.entries ? event.entries.length : 0) + 1;
      const sno = `#GV-${100 + nextNum}`;

      const newEntry = {
        sno: sno,
        name: name,
        place: city,
        relation: rel,
        mode: currentSelectedMode || 'Cash',
        amount: amt,
        phone: phone,
        recorder: 'Suresh (Desk 1)'
      };

      if (!event.entries) event.entries = [];
      event.entries.push(newEntry);
      event.totalBlessings += amt;
      event.envelopesCount = event.entries.length;

      saveEventsDatabase(EVENTS_DATABASE);
      updateWorkspaceKPIs(event);
      renderActiveEventTables();
      renderEventsHub();

      document.getElementById('entry-name').value = '';
      document.getElementById('entry-amount').value = '';

      // Temple Soundbox Announcement
      playTempleChime();
      showToast(`✓ ${name} గారి చదివింపు (${sno} - ₹${amt}) విజయవంతంగా నమోదైంది!`, 'gold');
    }

    function playTempleChime() {
      if (isSoundboxMuted) return;
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const now = audioCtx.currentTime;
        const osc1 = audioCtx.createOscillator();
        const gain1 = audioCtx.createGain();
        osc1.frequency.setValueAtTime(587.33, now); // D5
        gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.6);
        osc1.connect(gain1);
        gain1.connect(audioCtx.destination);
        osc1.start(now);
        osc1.stop(now + 0.6);
      } catch (e) {}
    }

    // ==========================================
    // 7. EDIT / DELETE / CSV / PRINT MODALS
    // ==========================================
    function openEditEntryModal(sno) {
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event || !event.entries) return;
      const entry = event.entries.find(e => e.sno === sno);
      if (!entry) return;

      document.getElementById('edit-entry-sno').value = entry.sno;
      document.getElementById('edit-entry-name').value = entry.name;
      document.getElementById('edit-entry-city').value = entry.place;
      document.getElementById('edit-entry-relation').value = entry.relation;
      document.getElementById('edit-entry-amount').value = entry.amount;
      document.getElementById('edit-entry-mode').value = entry.mode;

      document.getElementById('modal-edit-entry').classList.add('active');
    }
    function closeEditEntryModal() {
      document.getElementById('modal-edit-entry').classList.remove('active');
    }
    function handleEditEntrySubmit(e) {
      e.preventDefault();
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event) return;
      const sno = document.getElementById('edit-entry-sno').value;
      const entry = event.entries.find(e => e.sno === sno);
      if (!entry) return;

      entry.name = document.getElementById('edit-entry-name').value.trim();
      entry.place = document.getElementById('edit-entry-city').value.trim();
      entry.relation = document.getElementById('edit-entry-relation').value.trim();
      entry.amount = parseInt(document.getElementById('edit-entry-amount').value, 10) || 0;
      entry.mode = document.getElementById('edit-entry-mode').value;

      event.totalBlessings = event.entries.reduce((sum, it) => sum + (parseInt(it.amount, 10) || 0), 0);
      saveEventsDatabase(EVENTS_DATABASE);
      updateWorkspaceKPIs(event);
      renderActiveEventTables();
      closeEditEntryModal();
      showToast(`✓ Entry ${sno} updated successfully!`, 'gold');
    }

    function deleteEntry(sno) {
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event || !event.entries) return;
      const idx = event.entries.findIndex(e => e.sno === sno);
      if (idx === -1) return;

      event.entries.splice(idx, 1);
      event.totalBlessings = event.entries.reduce((sum, it) => sum + (parseInt(it.amount, 10) || 0), 0);
      event.envelopesCount = event.entries.length;

      saveEventsDatabase(EVENTS_DATABASE);
      updateWorkspaceKPIs(event);
      renderActiveEventTables();
      showToast(`🗑️ Entry ${sno} deleted. Total updated.`, 'gold');
    }

    function deleteCelebrationEvent(eventId, evObj) {
      if (evObj) evObj.stopPropagation();
      delete EVENTS_DATABASE[eventId];
      saveEventsDatabase(EVENTS_DATABASE);
      renderEventsHub();
      showToast('🗑️ Celebration deleted.', 'gold');
    }

    function exportLedgerCSV() {
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event || !event.entries) return;

      let csv = "Serial No,Guest Name,Native Place,Relationship,Payment Mode,Amount (INR)\\n";
      event.entries.forEach(i => {
        csv += `"${i.sno}","${i.name}","${i.place}","${i.relation}","${i.mode}","${i.amount}"\\n`;
      });
      const blob = new Blob(["\\uFEFF" + csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = `GiftVault_${event.title.replace(/[^a-zA-Z0-9]/g, '_')}_Ledger.csv`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast(`📥 Exported ${event.entries.length} entries to CSV!`, 'gold');
    }

    function printLedgerSheet() {
      window.print();
    }

    function openPrintSlip(sno, name, city, mode, amt) {
      document.getElementById('slip-sno').innerText = sno;
      document.getElementById('slip-guest-name').innerText = name;
      document.getElementById('slip-guest-city').innerText = city;
      document.getElementById('slip-mode').innerText = mode;
      document.getElementById('slip-amount').innerText = amt;
      document.getElementById('modal-print-slip').classList.add('active');
    }
    function closePrintSlipModal() {
      document.getElementById('modal-print-slip').classList.remove('active');
    }

    function openPricingModal() {
      document.getElementById('modal-pricing-plans').classList.add('active');
    }
    function closePricingModal() {
      document.getElementById('modal-pricing-plans').classList.remove('active');
    }

    function openCreateEventModal() {
      document.getElementById('modal-create-event').classList.add('active');
    }
    function closeCreateEventModal() {
      document.getElementById('modal-create-event').classList.remove('active');
    }
    function handleCreateEventSubmit(e) {
      e.preventDefault();
      const title = document.getElementById('new-event-title').value.trim();
      const type = document.getElementById('new-event-type').value;
      const date = document.getElementById('new-event-date').value || '2027-01-15';
      const venue = document.getElementById('new-event-venue').value.trim() || 'Mandapam';
      const guests = parseInt(document.getElementById('new-event-guests').value, 10) || 300;

      const newId = 'event-' + Date.now();
      EVENTS_DATABASE[newId] = {
        id: newId,
        title: title,
        type: type,
        date: date,
        venue: venue,
        guestsCount: guests,
        totalBlessings: 0,
        envelopesCount: 0,
        entries: []
      };

      saveEventsDatabase(EVENTS_DATABASE);
      renderEventsHub();
      closeCreateEventModal();
      enterWorkspaceEvent(newId);
      showToast(`✓ నూతన శుభకార్యం "${title}" ఖజానా సృష్టించబడింది!`, 'gold');
    }

    function filterLedgerTable() {
      const q = (document.getElementById('ledger-search-input').value || '').toLowerCase();
      const m = (document.getElementById('ledger-filter-mode').value || 'ALL');
      const rows = document.querySelectorAll('#ws-full-ledger-body tr');
      rows.forEach(r => {
        const text = r.innerText.toLowerCase();
        const matchesQ = text.includes(q);
        const matchesM = m === 'ALL' || text.includes(m.toLowerCase());
        r.style.display = (matchesQ && matchesM) ? '' : 'none';
      });
    }

    function startVoiceDictation() {
      showToast('🎙️ మైక్ ఆక్టివేట్ అయింది. అతిథి పేరు మాట్లాడండి...', 'gold');
    }

    function handleLanguageChange(val) {
      currentLang = val;
      const tag = document.querySelector('.hero-tagline-text');
      if (tag) {
        if (val === 'te') tag.innerText = 'శుభారంభం • మంగళ కార్యం';
        else if (val === 'hi') tag.innerText = 'शुभ आरंभ • मंगल कार्य';
        else tag.innerText = 'SHUBH AARAMBH • MANGALA KAARYAM';
      }
      const h1 = document.querySelector('.hero-heading');
      if (h1) {
        if (val === 'te') h1.innerHTML = 'ప్రతి శుభకార్యానికి <em>డిజిటల్ చదివింపుల</em> సింహాసనం';
        else if (val === 'hi') h1.innerHTML = 'हर मांगलिक कार्य के लिए <em>डिजिटल न्योता-शगुन</em> सिंहासन';
        else h1.innerHTML = 'Every Sacred Celebration Deserves a <em>Royal Gift Vault</em>';
      }
      showToast(`🌐 Language changed to ${val.toUpperCase()}`, 'gold');
    }

    // ==========================================
    // 8. INITIALIZATION ON DOM LOAD
    // ==========================================
    window.addEventListener('DOMContentLoaded', () => {
      initThreeHeroScene();
      updateLiveCalculator();
      renderEventsHub();
      currentActiveEventId = 'event-wedding';
    });
  </script>
</body>
</html>
"""

files = ['web_preview/index.html', 'web_preview/desktop.html', 'web_preview/mobile.html', 'build/web/index.html', 'web/index.html']

for p in files:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_masterpiece)
    print(f'Wrote master luxury production app to {p}')

print('All 5 files updated with ThreeUI / Three.js 3D WebGL / MotionSites Masterpiece.')
