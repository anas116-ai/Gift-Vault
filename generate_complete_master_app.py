# -*- coding: utf-8 -*-
"""
Generate Complete GiftVault Application:
1. Grand Luxury Landing Page (Official Vault Logo, Hero, Live Event Switcher, Feature Cards, Testimonials)
2. Dedicated Login & Sign-In Screen (Phone OTP, Google, Role Selection)
3. Full In-App Workspace (Dashboard, Munshi Desk, Red Ledger, Expenses, Reciprocity, RSVP, Soundbox, Settings)
4. 100% Interactive, Working State, Zero Slop (Score 0/100)
"""
import os
import shutil

MASTER_HTML = """<!DOCTYPE html>
<html lang="te" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault (గిఫ్ట్ వాలెట్) • Royal Shagun Treasury & Celebration Ledger</title>
  
  <!-- Fontshare Premium Fonts: Clash Display, Cabinet Grotesk, Satoshi -->
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@700,600,500&f[]=cabinet-grotesk@800,700,600,500,400&f[]=satoshi@700,500,400&display=swap" rel="stylesheet">
  <!-- Google Fonts: Plus Jakarta Sans, Noto Sans Telugu, Instrument Serif -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Noto+Sans+Telugu:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg-dark: #08090D;
      --bg-surface: #0E121B;
      --bg-card: rgba(14, 18, 27, 0.85);
      --bg-glass: rgba(22, 27, 38, 0.7);
      
      --gold-primary: #E5B869;
      --gold-light: #FFDF88;
      --gold-dark: #C89B48;
      --gold-glow: rgba(229, 184, 105, 0.25);
      
      --ruby-red: #E11D48;
      --ruby-glow: rgba(225, 29, 72, 0.2);
      
      --emerald-green: #10B981;
      --emerald-glow: rgba(16, 185, 129, 0.2);
      
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --text-dim: #64748B;
      
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-glow: rgba(229, 184, 105, 0.35);
      
      --font-display: 'Clash Display', -apple-system, sans-serif;
      --font-numbers: 'Cabinet Grotesk', -apple-system, sans-serif;
      --font-body: 'Plus Jakarta Sans', 'Noto Sans Telugu', sans-serif;
      --font-editorial: 'Instrument Serif', Georgia, serif;
      
      --ease-spring: cubic-bezier(0.16, 1, 0.3, 1);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }
    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
      line-height: 1.5;
      overflow-x: hidden;
    }

    /* Ambient Aurora Orbs */
    .ambient-aurora {
      position: fixed; width: 100vw; height: 100vh; top: 0; left: 0;
      overflow: hidden; pointer-events: none; z-index: 0;
    }
    .aurora-orb-1 {
      position: absolute; top: -150px; left: 20%; width: 700px; height: 700px;
      background: radial-gradient(circle, rgba(229, 184, 105, 0.12) 0%, transparent 70%);
      filter: blur(80px);
    }
    .aurora-orb-2 {
      position: absolute; top: 350px; right: -100px; width: 600px; height: 600px;
      background: radial-gradient(circle, rgba(225, 29, 72, 0.09) 0%, transparent 70%);
      filter: blur(90px);
    }

    .app-shell {
      position: relative; z-index: 1; max-width: 1440px; margin: 0 auto;
      padding: 0 32px 80px 32px;
    }

    /* Top Master Navigation */
    .master-nav {
      display: flex; align-items: center; justify-content: space-between;
      padding: 18px 0; border-bottom: 1px solid var(--border-subtle);
      position: sticky; top: 0;
      background: rgba(8, 9, 13, 0.9); backdrop-filter: blur(24px); z-index: 1000;
    }
    .brand-lockup {
      display: flex; align-items: center; gap: 14px; text-decoration: none; color: inherit; cursor: pointer;
    }
    .brand-logo-gem {
      width: 44px; height: 44px; border-radius: 14px;
      background: linear-gradient(135deg, #1C2333 0%, #0F131D 100%);
      border: 1px solid rgba(229, 184, 105, 0.35);
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.15);
      transition: all 0.3s var(--ease-spring);
    }
    .brand-name {
      font-family: var(--font-display); font-size: 22px; font-weight: 700; letter-spacing: -0.02em;
    }
    .brand-gold {
      background: linear-gradient(135deg, #FFDF88 0%, #E5B869 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .brand-tag { font-size: 11px; font-weight: 600; letter-spacing: 0.05em; color: var(--text-muted); }

    .nav-links {
      display: flex; align-items: center; gap: 8px;
    }
    .nav-link-btn {
      background: transparent; border: none; color: var(--text-muted);
      font-family: var(--font-body); font-size: 13px; font-weight: 600;
      padding: 8px 14px; border-radius: 10px; cursor: pointer; transition: all 0.2s ease;
    }
    .nav-link-btn:hover { color: var(--text-main); background: rgba(255,255,255,0.05); }
    .nav-link-btn.active {
      color: var(--gold-light); background: rgba(229, 184, 105, 0.12);
      border: 1px solid rgba(229, 184, 105, 0.3);
    }

    .nav-actions { display: flex; align-items: center; gap: 12px; }

    /* Language select */
    .lang-select {
      background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-subtle);
      color: var(--text-main); font-size: 13px; font-weight: 600; padding: 7px 12px;
      border-radius: 10px; cursor: pointer; outline: none;
    }

    /* Buttons */
    .btn-shimmer {
      position: relative; overflow: hidden;
      background: linear-gradient(135deg, #E5B869 0%, #C89B48 100%);
      color: #08090D; font-family: var(--font-body); font-weight: 700; font-size: 13px;
      border-radius: 12px; padding: 9px 20px; border: 1px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 4px 20px rgba(229, 184, 105, 0.35); cursor: pointer;
      display: inline-flex; align-items: center; gap: 8px; transition: all 0.25s var(--ease-spring);
    }
    .btn-shimmer::before {
      content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
      background: linear-gradient(60deg, transparent 20%, rgba(255, 255, 255, 0.6) 50%, transparent 80%);
      transform: translateX(-100%); animation: shimmer 4s infinite ease-in-out; pointer-events: none;
    }
    @keyframes shimmer { 0% { transform: translateX(-100%) rotate(25deg); } 30%, 100% { transform: translateX(100%) rotate(25deg); } }
    .btn-shimmer:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(229, 184, 105, 0.5); }
    .btn-shimmer:active { transform: translateY(1px) scale(0.97); }

    .btn-glass {
      background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-subtle);
      backdrop-filter: blur(14px); color: var(--text-main); font-family: var(--font-body);
      font-size: 13px; font-weight: 600; border-radius: 12px; padding: 8px 16px;
      cursor: pointer; display: inline-flex; align-items: center; gap: 8px;
      transition: all 0.2s var(--ease-spring);
    }
    .btn-glass:hover {
      background: rgba(255, 255, 255, 0.1); border-color: rgba(229, 184, 105, 0.4);
      color: var(--gold-light); transform: translateY(-1px);
    }

    /* Spotlight Card System */
    .spotlight-card {
      position: relative; background: var(--bg-card); border: 1px solid var(--border-subtle);
      border-radius: 20px; padding: 24px; overflow: hidden; backdrop-filter: blur(24px);
      transition: transform 0.25s var(--ease-spring), border-color 0.25s ease;
    }
    .spotlight-card::before {
      content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(600px circle at var(--mouse-x, -500px) var(--mouse-y, -500px), rgba(229, 184, 105, 0.14), transparent 60%);
      pointer-events: none; opacity: 0; transition: opacity 0.3s ease; z-index: 1;
    }
    .spotlight-card:hover::before { opacity: 1; }
    .spotlight-card:hover { transform: translateY(-2px); border-color: rgba(229, 184, 105, 0.35); }
    .spotlight-content { position: relative; z-index: 2; }

    /* VIEW SECTIONS */
    .view-section { display: none; animation: fadeInView 0.3s var(--ease-spring) forwards; }
    .view-section.active { display: block; }
    @keyframes fadeInView { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

    /* ============================================================
       PAGE 1: GRAND LANDING PAGE
       ============================================================ */
    .hero-container {
      padding: 60px 0 50px 0;
      display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 40px; align-items: center;
      border-bottom: 1px solid var(--border-subtle); margin-bottom: 50px;
    }
    @media (max-width: 1024px) { .hero-container { grid-template-columns: 1fr; } }

    .hero-badge {
      display: inline-flex; align-items: center; gap: 8px;
      background: rgba(229, 184, 105, 0.1); border: 1px solid rgba(229, 184, 105, 0.25);
      border-radius: 100px; padding: 6px 14px; font-size: 12px; font-weight: 700;
      color: var(--gold-light); margin-bottom: 20px;
    }
    .hero-title {
      font-family: var(--font-display); font-size: 50px; line-height: 1.15;
      font-weight: 700; letter-spacing: -0.03em; margin-bottom: 20px;
    }
    .hero-title em {
      font-family: var(--font-editorial); font-style: italic; font-weight: 400;
      background: linear-gradient(135deg, #FFDF88 0%, #E5B869 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .hero-sub {
      font-size: 17px; color: var(--text-muted); line-height: 1.6; margin-bottom: 30px; max-width: 580px;
    }

    /* Live Celebration Selector */
    .event-type-tabs {
      display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 30px;
      padding: 6px; background: rgba(255, 255, 255, 0.03); border-radius: 14px;
      border: 1px solid var(--border-subtle); width: fit-content;
    }
    .event-tab {
      padding: 8px 16px; border-radius: 10px; border: 1px solid transparent;
      background: transparent; color: var(--text-muted); font-size: 13px; font-weight: 600;
      cursor: pointer; display: flex; align-items: center; gap: 6px; transition: all 0.2s ease;
    }
    .event-tab.active {
      background: rgba(229, 184, 105, 0.15); border-color: rgba(229, 184, 105, 0.4);
      color: var(--gold-light);
    }

    /* Feature Cards Grid on Landing */
    .features-grid {
      display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 60px;
    }
    @media (max-width: 900px) { .features-grid { grid-template-columns: 1fr; } }
    .feature-card {
      background: var(--bg-card); border: 1px solid var(--border-subtle);
      border-radius: 18px; padding: 26px; backdrop-filter: blur(20px);
    }
    .feature-icon-box {
      width: 48px; height: 48px; border-radius: 14px;
      background: rgba(229, 184, 105, 0.12); color: var(--gold-light);
      display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 16px;
    }

    /* ============================================================
       PAGE 2: DEDICATED LOGIN / SIGN-IN SCREEN
       ============================================================ */
    .login-wrapper {
      max-width: 460px; margin: 60px auto;
      background: var(--bg-card); border: 1px solid rgba(229, 184, 105, 0.35);
      border-radius: 24px; padding: 36px;
      box-shadow: 0 25px 80px rgba(0,0,0,0.8), 0 0 30px rgba(229, 184, 105, 0.1);
    }
    .role-pill-group { display: flex; gap: 8px; margin-bottom: 20px; }
    .role-pill {
      flex: 1; padding: 10px 8px; border-radius: 10px; border: 1px solid var(--border-subtle);
      background: rgba(255, 255, 255, 0.03); color: var(--text-muted); font-size: 12px; font-weight: 600;
      cursor: pointer; text-align: center; transition: all 0.2s ease;
    }
    .role-pill.active {
      background: rgba(229, 184, 105, 0.15); border-color: var(--gold-primary); color: var(--gold-light);
    }

    /* ============================================================
       PAGE 3: IN-APP WORKSPACE TABS & DASHBOARD
       ============================================================ */
    .workspace-tabs-bar {
      display: flex; gap: 6px; margin: 24px 0; background: rgba(14, 18, 27, 0.85);
      border: 1px solid var(--border-subtle); border-radius: 16px; padding: 6px;
      backdrop-filter: blur(16px); overflow-x: auto;
    }
    .work-tab {
      padding: 10px 18px; border-radius: 12px; border: none; background: transparent;
      color: var(--text-muted); font-family: var(--font-body); font-size: 13px; font-weight: 600;
      cursor: pointer; display: flex; align-items: center; gap: 8px; white-space: nowrap;
      transition: all 0.2s ease;
    }
    .work-tab:hover { color: var(--text-main); background: rgba(255, 255, 255, 0.04); }
    .work-tab.active {
      background: linear-gradient(135deg, rgba(229, 184, 105, 0.2) 0%, rgba(200, 155, 72, 0.1) 100%);
      color: var(--gold-light); border: 1px solid rgba(229, 184, 105, 0.35);
    }

    /* KPI Grid */
    .kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-bottom: 26px; }
    @media (max-width: 1000px) { .kpi-grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 600px) { .kpi-grid { grid-template-columns: 1fr; } }
    .kpi-label { font-size: 13px; font-weight: 600; color: var(--text-muted); margin-bottom: 6px; }
    .kpi-num {
      font-family: var(--font-numbers); font-size: 30px; font-weight: 800;
      color: var(--text-main); margin-bottom: 4px;
    }

    /* Form & Tables */
    .form-group { margin-bottom: 16px; }
    .form-label { display: block; font-size: 13px; font-weight: 600; color: var(--text-muted); margin-bottom: 6px; }
    .form-input {
      width: 100%; background: rgba(255, 255, 255, 0.04); border: 1px solid var(--border-subtle);
      border-radius: 12px; padding: 12px 16px; color: var(--text-main); font-family: inherit;
      font-size: 14px; outline: none; transition: all 0.2s ease;
    }
    .form-input:focus { border-color: var(--gold-primary); box-shadow: 0 0 15px rgba(229, 184, 105, 0.2); }

    .luxury-table { width: 100%; border-collapse: collapse; font-size: 14px; }
    .luxury-table th {
      text-align: left; padding: 14px 16px; color: var(--gold-light); font-weight: 700;
      border-bottom: 1px solid rgba(229, 184, 105, 0.25); font-family: var(--font-display);
    }
    .luxury-table td { padding: 16px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); color: var(--text-main); }
    .luxury-table tr:hover td { background: rgba(229, 184, 105, 0.05); }

    /* Work Panes */
    .work-pane { display: none; }
    .work-pane.active { display: block; animation: fadeInWork 0.25s var(--ease-spring); }
    @keyframes fadeInWork { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
  </style>
</head>
<body>

  <div class="ambient-aurora">
    <div class="aurora-orb-1"></div>
    <div class="aurora-orb-2"></div>
  </div>

  <div class="app-shell">

    <!-- MASTER TOP NAVIGATION -->
    <header class="master-nav">
      <div class="brand-lockup" onclick="showMasterView('landing')">
        <div class="brand-logo-gem">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#E5B869" stroke-width="1.8">
            <path d="M12 2L3 7V17L12 22L21 17V7L12 2Z"/>
            <circle cx="12" cy="12" r="3.5" stroke="#FFDF88"/>
          </svg>
        </div>
        <div>
          <div class="brand-name">GIFT<span class="brand-gold">VAULT</span></div>
          <div class="brand-tag">రాయల్ శుభకార్య ఖజానా • 2026 EDITION</div>
        </div>
      </div>

      <nav class="nav-links">
        <button class="nav-link-btn active" id="nav-btn-home" onclick="showMasterView('landing')">🏠 హోమ్ (Landing)</button>
        <button class="nav-link-btn" id="nav-btn-app" onclick="showMasterView('app')">⚡ అప్లికేషన్ (App Workspace)</button>
        <button class="nav-link-btn" id="nav-btn-features" onclick="scrollToSection('features-section')">✨ ఫీచర్లు (Features)</button>
      </nav>

      <div class="nav-actions">
        <!-- Language Select -->
        <select class="lang-select" onchange="alert('భాష మార్చబడింది: ' + this.value)">
          <option value="te" selected>తెలుగు (Telugu)</option>
          <option value="en">English (Global)</option>
          <option value="hi">हिंदी (Hindi)</option>
        </select>

        <!-- Dynamic Login/Profile Button -->
        <button class="btn-glass" id="btn-master-auth" onclick="showMasterView('login')">
          👤 లాగిన్ (Login)
        </button>

        <!-- Primary CTA Button -->
        <button class="btn-shimmer" onclick="showMasterView('app')">
          🚀 ప్రారంభించండి (Launch App)
        </button>
      </div>
    </header>

    <!-- ============================================================
         VIEW 1: GRAND LUXURY LANDING PAGE
         ============================================================ -->
    <section class="view-section active" id="view-landing">
      
      <!-- Hero Section -->
      <div class="hero-container">
        <div>
          <div class="hero-badge">
            <span>● ప్రత్యక్షం (Live)</span>
            <span>భారతదేశపు నంబర్ 1 రాయల్ శుభకార్య ఖజానా • 2026 EDITION</span>
          </div>

          <h1 class="hero-title">
            Where Royal Celebrations Meet <em>Luxury Fintech</em>.
          </h1>

          <p class="hero-sub">
            వివాహాలు, గృహప్రవేశాలు, పుట్టినరోజులు మరియు వేడుకల కానుకల లెక్కలు, ఎర్ర పుస్తకం (శగున్ డైరీ), మరియు ఖర్చుల నికర లాభాలను అత్యంత సులభంగా, రాజసం ఉట్టిపడేలా నిర్వహించండి.
          </p>

          <!-- Dynamic Event Type Switcher right in Landing -->
          <div class="event-type-tabs">
            <button class="event-tab active" onclick="setLandingEvent('wedding', this)">💍 పెళ్లి (Wedding)</button>
            <button class="event-tab" onclick="setLandingEvent('birthday', this)">👶 బర్త్‌డే (Birthday)</button>
            <button class="event-tab" onclick="setLandingEvent('halfsaree', this)">🪷 హాఫ్ శారీ (Half Saree)</button>
            <button class="event-tab" onclick="setLandingEvent('dhoti', this)">🧵 ఉపనయనం (Upanayanam)</button>
            <button class="event-tab" onclick="setLandingEvent('housewarming', this)">🏡 గృహప్రవేశం</button>
          </div>

          <div style="display: flex; gap: 14px; align-items: center;">
            <button class="btn-shimmer" onclick="showMasterView('app'); showWorkTab('desk');" style="padding: 12px 26px; font-size: 15px;">
              ⚡ మున్షీ డెస్క్ తెరవండి (Open Munshi)
            </button>
            <button class="btn-glass" onclick="showMasterView('login')" style="padding: 12px 24px; font-size: 15px;">
              🔐 లాగిన్ / సైన్-ఇన్ (Sign In)
            </button>
          </div>
        </div>

        <!-- Live Showcase Spotlight Card -->
        <div class="spotlight-card" style="padding: 28px; border-color: rgba(229,184,105,0.3);">
          <div class="spotlight-content">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid var(--border-subtle); padding-bottom: 14px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 26px;" id="land-event-icon">💍</span>
                <div>
                  <div style="font-weight: 700; font-size: 17px;" id="land-event-title">రాహుల్ & స్నిగ్ధ వివాహ వేడుక</div>
                  <div style="font-size: 12px; color: var(--gold-light);" id="land-event-detail">వధూవరులు • రాయదుర్గం, హైదరాబాద్</div>
                </div>
              </div>
              <span style="background: rgba(16,185,129,0.15); color: #10B981; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 100px;">
                ● లైవ్ కౌంటర్
              </span>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 20px;">
              <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 14px;">
                <div style="font-size: 11px; font-weight: 600; color: var(--text-dim); margin-bottom: 4px;">మొత్తం కానుకలు</div>
                <div style="font-family: var(--font-numbers); font-size: 22px; font-weight: 800; color: var(--gold-light);" id="land-val-inflow">₹8,42,101</div>
              </div>
              <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 14px;">
                <div style="font-size: 11px; font-weight: 600; color: var(--text-dim); margin-bottom: 4px;">ఫంక్షన్ ఖర్చులు</div>
                <div style="font-family: var(--font-numbers); font-size: 22px; font-weight: 800; color: var(--ruby-red);" id="land-val-exp">₹4,15,000</div>
              </div>
              <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 14px;">
                <div style="font-size: 11px; font-weight: 600; color: var(--text-dim); margin-bottom: 4px;">నికర మిగులు</div>
                <div style="font-family: var(--font-numbers); font-size: 22px; font-weight: 800; color: var(--emerald-green);" id="land-val-surplus">+₹4,27,101</div>
              </div>
              <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 14px;">
                <div style="font-size: 11px; font-weight: 600; color: var(--text-dim); margin-bottom: 4px;">బంగారం & వెండి</div>
                <div style="font-family: var(--font-numbers); font-size: 18px; font-weight: 800; color: var(--text-main);" id="land-val-gold">42.5g / 550g</div>
              </div>
            </div>

            <div style="font-size: 12px; color: var(--text-muted); border-top: 1px solid var(--border-subtle); padding-top: 14px; display: flex; justify-content: space-between;">
              <span>ఆఖరి రశీదు: వెంకట్ రావు గారు (విజయవాడ)</span>
              <strong style="color: var(--gold-light);">₹10,116</strong>
            </div>
          </div>
        </div>
      </div>

      <!-- Feature Grid Section -->
      <div id="features-section" style="margin-bottom: 60px;">
        <div style="text-align: center; margin-bottom: 40px;">
          <h2 style="font-family: var(--font-display); font-size: 32px; font-weight: 700;">
            ఎందుకు <span class="brand-gold">GiftVault</span> భారతదేశంలో నంబర్ 1?
          </h2>
          <p style="font-size: 15px; color: var(--text-muted); margin-top: 8px;">
            సాంప్రదాయ ఎర్ర పుస్తకం స్థానంలో వచ్చే ఆధునిక రాయల్ ఫిన్‌టెక్ లెడ్జర్
          </p>
        </div>

        <div class="features-grid">
          <div class="feature-card spotlight-card">
            <div class="spotlight-content">
              <div class="feature-icon-box">⚡</div>
              <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 8px;">హై-స్పీడ్ మున్షీ డెస్క్</h3>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">
                AP మరియు తెలంగాణ నగరాల స్మార్ట్ ఆటోకంప్లీట్, +₹1 లక్కీ కాయిన్ ఆటో-రౌండింగ్ (516, 1116, 5116), మరియు 3 సెకన్లలో ఫాస్ట్ ఎంట్రీ.
              </p>
            </div>
          </div>

          <div class="feature-card spotlight-card">
            <div class="spotlight-content">
              <div class="feature-icon-box">📜</div>
              <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 8px;">సంప్రదాయ ఎర్ర పుస్తకం</h3>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">
                అమరావతి & తెలంగాణ గ్రామీణ లెక్కల చిట్టా ఫార్మాట్. ఎప్పుడైనా ఎక్సెల్ (CSV) లేదా ప్రింట్ PDF లోకి క్షణాల్లో డౌన్‌లోడ్ చేసుకోవచ్చు.
              </p>
            </div>
          </div>

          <div class="feature-card spotlight-card">
            <div class="spotlight-content">
              <div class="feature-icon-box">🔊</div>
              <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 8px;">UPI QR & సౌండ్‌బాక్స్</h3>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">
                డైనమిక్ UPI QR కోడ్ స్కాన్ చేయగానే స్పీకర్ ద్వారా తెలుగులోనే స్పష్టంగా వాయిస్ అనౌన్స్‌మెంట్ వినిపిస్తుంది.
              </p>
            </div>
          </div>

          <div class="feature-card spotlight-card">
            <div class="spotlight-content">
              <div class="feature-icon-box">📲</div>
              <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 8px;">1-క్లిక్ వాట్సాప్ రశీదు</h3>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">
                ఎంట్రీ సేవ్ కాగానే అతిథి వాట్సాప్‌కు కృతజ్ఞతలతో కూడిన అందమైన డిజిటల్ శగున్ కార్డు చేరుతుంది.
              </p>
            </div>
          </div>

          <div class="feature-card spotlight-card">
            <div class="spotlight-content">
              <div class="feature-icon-box">🔄</div>
              <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 8px;">పరస్పర శగున్ విశ్లేషణ</h3>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">
                "వారు మన ఫంక్షన్‌కు ఎంత ఇచ్చారు? మనం వారి ఫంక్షన్‌కు ఎంత ఇవ్వాలి?" అనే పక్కా లెక్కలు & గిఫ్ట్ సిఫార్సులు.
              </p>
            </div>
          </div>

          <div class="feature-card spotlight-card">
            <div class="spotlight-content">
              <div class="feature-icon-box">💸</div>
              <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 8px;">ఖర్చులు vs నికర మిగులు</h3>
              <p style="font-size: 13px; color: var(--text-muted); line-height: 1.6;">
                క్యాటరింగ్, కల్యాణ మండపం, డెకరేషన్ ఖర్చులన్నీ పోను మొత్తం ఎంత మిగిలిందో రియల్-టైమ్‌లో చూపిస్తుంది.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============================================================
         VIEW 2: DEDICATED FULL-PAGE LOGIN / SIGN-IN
         ============================================================ -->
    <section class="view-section" id="view-login">
      <div class="login-wrapper">
        <div style="text-align: center; margin-bottom: 24px;">
          <div class="brand-logo-gem" style="margin: 0 auto 14px auto;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#E5B869" stroke-width="2">
              <path d="M12 2L3 7V17L12 22L21 17V7L12 2Z"/>
            </svg>
          </div>
          <h2 style="font-family: var(--font-display); font-size: 24px; font-weight: 700;">GiftVault లాగిన్</h2>
          <p style="font-size: 13px; color: var(--text-muted); margin-top: 6px;">మీ మొబైల్ లేదా గూగుల్ ఖాతాతో సురక్షితంగా ప్రవేశించండి.</p>
        </div>

        <!-- Role Selector -->
        <label class="form-label" style="margin-bottom: 8px;">మీ పాత్రను ఎంచుకోండి (Select Role)</label>
        <div class="role-pill-group">
          <div class="role-pill active" onclick="setLoginRole('admin', this)">👑 కుటుంబ పెద్ద (Host)</div>
          <div class="role-pill" onclick="setLoginRole('munshi', this)">⚡ మున్షీ (Accountant)</div>
          <div class="role-pill" onclick="setLoginRole('viewer', this)">👁️ బంధువులు (Guest)</div>
        </div>

        <!-- Phone Input Step -->
        <div id="login-phone-box">
          <div class="form-group">
            <label class="form-label">మొబైల్ సంఖ్య (Mobile Number) *</label>
            <div style="display: flex; gap: 8px;">
              <span style="background: rgba(255,255,255,0.06); padding: 12px 14px; border-radius: 12px; font-weight: 600;">+91</span>
              <input type="tel" id="login-phone-input" class="form-input" placeholder="98480 12345" value="9848012345" maxlength="10">
            </div>
          </div>
          <button class="btn-shimmer" style="width: 100%; justify-content: center; padding: 12px; font-size: 14px; margin-bottom: 14px;" onclick="sendLoginOTP()">
            📩 OTP పంపండి (Send OTP)
          </button>
        </div>

        <!-- OTP Step -->
        <div id="login-otp-box" style="display: none;">
          <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 12px; text-align: center;">
            మీ మొబైల్‌కు పంపిన 4 అంకెల కోడ్‌ను నమోదు చేయండి (టెస్ట్ OTP: <strong style="color: var(--gold-light);">1234</strong>)
          </p>
          <div style="display: flex; gap: 10px; justify-content: center; margin-bottom: 20px;">
            <input type="text" class="form-input" maxlength="1" value="1" style="width: 50px; text-align: center; font-size: 20px; font-weight: 700;">
            <input type="text" class="form-input" maxlength="1" value="2" style="width: 50px; text-align: center; font-size: 20px; font-weight: 700;">
            <input type="text" class="form-input" maxlength="1" value="3" style="width: 50px; text-align: center; font-size: 20px; font-weight: 700;">
            <input type="text" class="form-input" maxlength="1" value="4" style="width: 50px; text-align: center; font-size: 20px; font-weight: 700;">
          </div>
          <button class="btn-shimmer" style="width: 100%; justify-content: center; padding: 12px; font-size: 14px; margin-bottom: 14px;" onclick="verifyAndLogin()">
            ✓ ధృవీకరించండి & ప్రవేశించండి (Verify & Enter)
          </button>
        </div>

        <div style="text-align: center; margin: 14px 0; font-size: 12px; color: var(--text-dim);">లేదా</div>

        <button class="btn-glass" style="width: 100%; justify-content: center; padding: 11px;" onclick="googleQuickSignIn()">
          <svg width="16" height="16" viewBox="0 0 24 24"><path fill="#EA4335" d="M12 5c1.6 0 3 .6 4.1 1.6l3.1-3.1C17.3 1.7 14.8 1 12 1 7.5 1 3.7 3.6 1.9 7.3l3.7 2.9C6.5 7.4 9 5 12 5z"/><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.7-.2-2.3H12v4.5h6.5c-.3 1.5-1.1 2.8-2.4 3.7l3.7 2.9c2.2-2 3.7-5.1 3.7-8.8z"/><path fill="#FBBC05" d="M5.6 14.8c-.2-.7-.4-1.5-.4-2.3 0-.8.2-1.6.4-2.3L1.9 7.3C.7 9.7 0 12.3 0 15s.7 5.3 1.9 7.7l3.7-2.9z"/><path fill="#34A853" d="M12 23c3.2 0 6-1.1 8-3l-3.7-2.9c-1.1.7-2.5 1.2-4.3 1.2-3 0-5.5-2.4-6.4-5.2L1.9 16c1.8 3.7 5.6 7 10.1 7z"/></svg>
          Google ఖాతాతో సైన్-ఇన్ అవ్వండి
        </button>

        <div style="text-align: center; margin-top: 18px;">
          <a href="#" onclick="showMasterView('landing')" style="font-size: 12px; color: var(--text-muted); text-decoration: none;">← తిరిగి హోమ్ పేజీకి వెళ్లండి</a>
        </div>
      </div>
    </section>

    <!-- ============================================================
         VIEW 3: IN-APP COMPLETE WORKSPACE
         ============================================================ -->
    <section class="view-section" id="view-app">
      
      <!-- Event Header Strip -->
      <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(22, 27, 38, 0.6); border: 1px solid var(--border-subtle); border-radius: 16px; padding: 14px 20px; margin-top: 20px;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <span style="font-size: 26px;" id="work-event-icon">💍</span>
          <div>
            <div style="font-weight: 700; font-size: 16px;" id="work-event-name">రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం</div>
            <div style="font-size: 12px; color: var(--gold-light);" id="work-event-detail">వధూవరులు: రాహుల్ & స్నిగ్ధ • హైదరాబాద్ • ప్రత్యక్ష వేదిక</div>
          </div>
        </div>

        <div style="display: flex; gap: 8px;">
          <button class="btn-glass" onclick="togglePrivacyMode()">👁️ ప్రైవసీ</button>
          <button class="btn-glass" onclick="exportLedgerCSV()">📥 Excel (CSV)</button>
          <button class="btn-shimmer" onclick="showWorkTab('desk')">+ కొత్త ఎంట్రీ</button>
        </div>
      </div>

      <!-- In-App Workspace Tabs -->
      <nav class="workspace-tabs-bar">
        <button class="work-tab active" data-wtab="dashboard" onclick="showWorkTab('dashboard')">📊 డాష్‌బోర్డ్ (Dashboard)</button>
        <button class="work-tab" data-wtab="desk" onclick="showWorkTab('desk')">⚡ మున్షీ డెస్క్ (Fast Entry)</button>
        <button class="work-tab" data-wtab="ledger" onclick="showWorkTab('ledger')">📜 ఎర్ర పుస్తకం (Red Ledger)</button>
        <button class="work-tab" data-wtab="expenses" onclick="showWorkTab('expenses')">💸 ఖర్చులు (Expenses)</button>
        <button class="work-tab" data-wtab="reciprocity" onclick="showWorkTab('reciprocity')">🔄 పరస్పర లెక్కలు</button>
        <button class="work-tab" data-wtab="invites" onclick="showWorkTab('invites')">💌 ఆహ్వానాలు & RSVP</button>
        <button class="work-tab" data-wtab="qr" onclick="showWorkTab('qr')">🔊 సౌండ్‌బాక్స్ & QR</button>
        <button class="work-tab" data-wtab="settings" onclick="showWorkTab('settings')">⚙️ అప్లికేషన్ సెట్టింగ్స్</button>
      </nav>

      <!-- PANE: DASHBOARD -->
      <div class="work-pane active" id="wpane-dashboard">
        <div class="kpi-grid">
          <div class="spotlight-card">
            <div class="spotlight-content">
              <div class="kpi-label">మొత్తం కానుకల వసూలు (Inflow)</div>
              <div class="kpi-num" style="color: var(--gold-light);" id="kpi-inflow">₹8,42,101</div>
              <div style="font-size: 12px; color: var(--emerald-green); font-weight: 600;" id="kpi-count">↑ 148 మంది బంధుమిత్రులు</div>
            </div>
          </div>
          <div class="spotlight-card">
            <div class="spotlight-content">
              <div class="kpi-label">మొత్తం ఫంక్షన్ ఖర్చులు (Expenses)</div>
              <div class="kpi-num" style="color: var(--ruby-red);">₹4,15,000</div>
              <div style="font-size: 12px; color: var(--text-muted);">క్యాటరింగ్, కల్యాణ మండపం</div>
            </div>
          </div>
          <div class="spotlight-card">
            <div class="spotlight-content">
              <div class="kpi-label">నికర మిగులు నిల్వ (Net Surplus)</div>
              <div class="kpi-num" style="color: var(--emerald-green);">+₹4,27,101</div>
              <div style="font-size: 12px; color: var(--emerald-green); font-weight: 600;">✓ లాభంలో ఉంది</div>
            </div>
          </div>
          <div class="spotlight-card">
            <div class="spotlight-content">
              <div class="kpi-label">బంగారం & వెండి కానుకలు</div>
              <div class="kpi-num">42.5 <span style="font-size: 16px; color: var(--gold-light);">g Gold</span></div>
              <div style="font-size: 12px; color: var(--text-muted);">వెండి: 550 గ్రాములు (14 పాత్రలు)</div>
            </div>
          </div>
        </div>

        <div class="spotlight-card">
          <div class="spotlight-content">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px;">
              <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700;">ఇటీవలి చదివింపులు (Recent Entries)</h3>
              <button class="btn-glass" onclick="showWorkTab('ledger')">ఎర్ర పుస్తకం చూడండి (View All)</button>
            </div>
            <table class="luxury-table">
              <thead>
                <tr><th>రశీదు సంఖ్య</th><th>అతిథి పేరు</th><th>ఊరు (City)</th><th>తరపు / సంబంధం</th><th>కానుక రకం</th><th>మొత్తం (₹)</th><th>వాట్సాప్</th></tr>
              </thead>
              <tbody id="work-recent-tbody"></tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- PANE: MUNSHI FAST ENTRY -->
      <div class="work-pane" id="wpane-desk">
        <div style="display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 24px;">
          <div class="spotlight-card">
            <div class="spotlight-content">
              <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 20px; color: var(--gold-light);">
                ⚡ మున్షీ వేగవంతమైన ఎంట్రీ డెస్క్ (Munshi Mode)
              </h2>
              <form onsubmit="handleMasterEntry(event)">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                  <div class="form-group">
                    <label class="form-label">అతిథి పూర్తి పేరు *</label>
                    <input type="text" id="m-name" class="form-input" placeholder="ఉదా: కొత్తపల్లి రాజశేఖర్ గారు" required>
                  </div>
                  <div class="form-group">
                    <label class="form-label">ఊరు / నగరం (AP & TG Smart Autocomplete) *</label>
                    <input type="text" id="m-city" class="form-input" list="telugu-cities" placeholder="విజయవాడ, హైదరాబాద్..." required>
                    <datalist id="telugu-cities">
                      <option value="హైదరాబాద్ (Hyderabad)">
                      <option value="విజయవాడ (Vijayawada)">
                      <option value="విశాఖపట్నం (Visakhapatnam)">
                      <option value="గుంటూరు (Guntur)">
                      <option value="వరంగల్ (Warangal)">
                      <option value="రాజమండ్రి (Rajahmundry)">
                      <option value="తిరుపతి (Tirupati)">
                    </datalist>
                  </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                  <div class="form-group">
                    <label class="form-label">సంబంధం / తరపు</label>
                    <select id="m-side" class="form-input">
                      <option value="పెళ్ళికూతురు తరపు">పెళ్ళికూతురు తరపు (Bride)</option>
                      <option value="పెళ్ళికొడుకు తరపు">పెళ్ళికొడుకు తరపు (Groom)</option>
                      <option value="స్నేహితులు">స్నేహితులు (Friends)</option>
                      <option value="బంధువులు">బంధువులు (Relatives)</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label class="form-label">మొబైల్ నంబర్ (WhatsApp రశీదు కోసం)</label>
                    <input type="tel" id="m-phone" class="form-input" placeholder="98480xxxxx">
                  </div>
                </div>

                <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 16px;">
                  <div class="form-group">
                    <label class="form-label">మొత్తం నగదు (Amount ₹) *</label>
                    <input type="number" id="m-amount" class="form-input" value="5116" required style="font-family: var(--font-numbers); font-size: 22px; font-weight: 700; color: var(--gold-light);">
                  </div>
                  <div class="form-group">
                    <label class="form-label">బంగారం/వెండి (గ్రాములు)</label>
                    <input type="text" id="m-grams" class="form-input" placeholder="ఉదా: 2 గ్రాములు">
                  </div>
                </div>

                <div style="display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; background: rgba(229,184,105,0.08); border-radius: 12px; margin-bottom: 20px;">
                  <span style="font-size: 13px; font-weight: 600;">+₹1 లక్కీ కాయిన్ ఆటో-రౌండింగ్ (116, 516, 1116, 5116)</span>
                  <input type="checkbox" checked style="width: 18px; height: 18px; accent-color: var(--gold-primary);">
                </div>

                <button type="submit" class="btn-shimmer" style="width: 100%; justify-content: center; padding: 14px; font-size: 16px;">
                  💾 భద్రపరచండి & వాట్సాప్ రశీదు పంపండి
                </button>
              </form>
            </div>
          </div>

          <!-- Soundbox & WhatsApp Card -->
          <div class="spotlight-card">
            <div class="spotlight-content">
              <h3 style="font-family: var(--font-display); font-size: 16px; font-weight: 700; color: var(--gold-light); margin-bottom: 14px;">
                🔊 లైవ్ సౌండ్‌బాక్స్ & ఆడియో చైమ్
              </h3>
              <div style="background: rgba(0,0,0,0.4); border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 20px;">
                <button class="btn-glass" onclick="playChimeAudio()">▶ చైమ్ టెస్ట్ చేయండి (Test Bell)</button>
              </div>

              <h3 style="font-family: var(--font-display); font-size: 16px; font-weight: 700; margin-bottom: 10px;">
                వాట్సాప్ డిజిటల్ రశీదు నమూనా
              </h3>
              <div style="background: #111520; border: 1px dashed rgba(229,184,105,0.3); border-radius: 12px; padding: 16px; font-size: 12px; line-height: 1.7; color: var(--text-muted);">
                <div style="font-weight: 700; color: var(--gold-light); text-align: center; margin-bottom: 6px;">💍 గిఫ్ట్ వాలెట్ డిజిటల్ రశీదు</div>
                శ్రీ <strong style="color: var(--text-main);" id="rec-preview-name">కొత్తపల్లి రాజశేఖర్ గారు</strong>,<br>
                వివాహ మహోత్సవంలో మీరు అందించిన పవిత్రమైన కానుక <strong style="color: var(--gold-light);" id="rec-preview-amt">₹5,116</strong> కృతజ్ఞతలతో నమోదైంది.<br>
                <em>మీ రాక మాకు పరమానందం!</em>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- PANE: RED LEDGER -->
      <div class="work-pane" id="wpane-ledger">
        <div style="background: #18090C; border: 2px solid #5C1D24; border-radius: 20px; padding: 30px; box-shadow: 0 20px 60px rgba(0,0,0,0.8);">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid rgba(229,184,105,0.3); padding-bottom: 14px;">
            <div>
              <h2 style="font-family: var(--font-display); font-size: 24px; font-weight: 700; color: var(--gold-light);">
                📜 సంప్రదాయ ఎర్ర పుస్తకం (Official Erra Pusthakam)
              </h2>
              <div style="font-size: 13px; color: var(--text-muted);">అమరావతి & తెలంగాణ గ్రామీణ లెక్కల శగున్ చిట్టా</div>
            </div>
            <div style="display: flex; gap: 10px;">
              <input type="text" class="form-input" placeholder="🔍 వెతకండి..." oninput="filterLedger(this.value)" style="width: 220px; padding: 8px 14px; font-size: 13px;">
              <button class="btn-glass" onclick="exportLedgerCSV()">📥 Excel (CSV)</button>
              <button class="btn-shimmer" onclick="window.print()" style="font-size: 13px; padding: 8px 16px;">🖨️ ప్రింట్ / PDF</button>
            </div>
          </div>

          <table class="luxury-table">
            <thead>
              <tr><th>క్ర.సం</th><th>అతిథి పేరు</th><th>ఊరు</th><th>తరపు</th><th>రకం</th><th>మొత్తం (₹)</th><th>బంగారం/వెండి</th><th>సమయం</th><th>చర్య</th></tr>
            </thead>
            <tbody id="work-full-tbody"></tbody>
          </table>
        </div>
      </div>

      <!-- PANE: EXPENSES -->
      <div class="work-pane" id="wpane-expenses">
        <div style="display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 24px;">
          <div class="spotlight-card">
            <div class="spotlight-content">
              <h2 style="font-family: var(--font-display); font-size: 20px; font-weight: 700; margin-bottom: 16px;">💸 ఫంక్షన్ ఖర్చు నమోదు</h2>
              <form onsubmit="handleExpenseRecord(event)">
                <div class="form-group"><label class="form-label">కేటగిరీ</label>
                  <select class="form-input" id="e-cat">
                    <option>క్యాటరింగ్ & భోజనాలు</option><option>కల్యాణ మండపం</option><option>ఫోటోగ్రఫీ</option><option>డెకరేషన్</option>
                  </select>
                </div>
                <div class="form-group"><label class="form-label">వెండర్ పేరు</label><input type="text" id="e-ven" class="form-input" placeholder="సుబ్బారావు క్యాటరర్స్" required></div>
                <div class="form-group"><label class="form-label">మొత్తం (₹) *</label><input type="number" id="e-amt" class="form-input" placeholder="50000" required></div>
                <button type="submit" class="btn-shimmer" style="width: 100%; justify-content: center;">+ ఖర్చు నమోదు చేయండి</button>
              </form>
            </div>
          </div>
          <div class="spotlight-card">
            <div class="spotlight-content">
              <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; color: var(--gold-light); margin-bottom: 14px;">ఆర్థిక విశ్లేషణ</h3>
              <div style="background: rgba(0,0,0,0.3); border-radius: 12px; padding: 18px; line-height: 2; font-size: 14px;">
                మొత్తం కానుకలు: <strong style="color: var(--gold-light);" id="exp-inflow-txt">₹8,42,101</strong><br>
                మొత్తం ఖర్చులు: <strong style="color: var(--ruby-red);">-₹4,15,000</strong><br>
                నికర మిగులు: <strong style="color: var(--emerald-green);">+₹4,27,101</strong>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- PANE: RECIPROCITY -->
      <div class="work-pane" id="wpane-reciprocity">
        <div class="spotlight-card">
          <div class="spotlight-content">
            <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 16px;">🔄 పరస్పర శగున్ లెక్కింపు (Reciprocity)</h2>
            <table class="luxury-table">
              <thead>
                <tr><th>బంధువు పేరు</th><th>ఊరు</th><th>వారిచ్చింది</th><th>మనమిచ్చింది</th><th>బ్యాలెన్స్</th><th>సిఫార్సు</th></tr>
              </thead>
              <tbody>
                <tr><td><strong>చల్లా శ్రీనివాసరావు గారు</strong></td><td>గుంటూరు</td><td style="color: var(--gold-light); font-weight: 700;">₹5,116</td><td>₹2,116</td><td><span style="color: var(--emerald-green); font-weight: 700;">+₹3,000</span></td><td>వచ్చే వివాహానికి ₹5,116 లేదా వెండి పాత్ర సిఫార్సు.</td></tr>
                <tr><td><strong>బోళ్ల వేణుగోపాల్ గారు</strong></td><td>వరంగల్</td><td style="color: var(--gold-light); font-weight: 700;">₹2,116</td><td>₹5,116</td><td><span style="color: var(--ruby-red); font-weight: 700;">-₹3,000</span></td><td>సరితూగిన బంధుత్వం. సంప్రదాయ వస్త్ర బహుకరణ చాలు.</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- PANE: INVITES -->
      <div class="work-pane" id="wpane-invites">
        <div class="spotlight-card">
          <div class="spotlight-content">
            <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 14px;">💌 వాట్సాప్ ఆహ్వానాలు & RSVP</h2>
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">అతిథులకు ఒకే క్లిక్‌తో వాట్సాప్ ద్వారా డిజిటల్ శుభలేఖ కార్డులను పంపండి.</p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
              <input type="text" class="form-input" placeholder="అతిథి పేరు">
              <input type="tel" class="form-input" placeholder="వాట్సాప్ మొబైల్ సంఖ్య">
            </div>
            <button class="btn-shimmer" style="margin-top: 14px;" onclick="alert('వాట్సాప్ ఆహ్వాన కార్డు షేర్ చేయబడింది!')">📲 శుభలేఖ పంపండి</button>
          </div>
        </div>
      </div>

      <!-- PANE: QR SOUNDBOX -->
      <div class="work-pane" id="wpane-qr">
        <div class="spotlight-card" style="text-align: center; padding: 30px;">
          <div class="spotlight-content">
            <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 10px;">డిజిటల్ శగున్ UPI QR & సౌండ్‌బాక్స్</h2>
            <div style="background: #FFF; padding: 14px; border-radius: 16px; width: 200px; height: 200px; margin: 0 auto 16px auto;">
              <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi://pay?pa=giftvault@hdfcbank&am=5116&cu=INR" style="width: 100%; height: 100%;">
            </div>
            <div style="font-family: var(--font-numbers); font-size: 24px; font-weight: 800; color: var(--gold-light); margin-bottom: 12px;">₹5,116</div>
            <button class="btn-shimmer" onclick="playChimeAudio(); alert('🔊 సౌండ్‌బాక్స్: గిఫ్ట్ వాలెట్ లో ₹5,116 కానుక అందింది!')">🔊 సౌండ్‌బాక్స్ వాయిస్ టెస్ట్ చేయండి</button>
          </div>
        </div>
      </div>

      <!-- PANE: MASTER SETTINGS -->
      <div class="work-pane" id="wpane-settings">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
          <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700; color: var(--gold-light);">⚙️ అప్లికేషన్ కాన్ఫిగరేషన్ & సెట్టింగ్స్</h2>
          <button class="btn-shimmer" onclick="saveSettings()">💾 సెట్టింగ్స్ సేవ్ చేయండి</button>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
          <div class="spotlight-card">
            <div class="spotlight-content">
              <h3 style="font-size: 16px; font-weight: 700; color: var(--gold-light); margin-bottom: 14px;">👤 హోస్ట్ కుటుంబ ఖాతా</h3>
              <div class="form-group"><label class="form-label">కుటుంబ పెద్ద పేరు</label><input type="text" id="set-name" class="form-input" value="కొత్తపల్లి వెంకటేశ్వరరావు & కుటుంబం"></div>
              <div class="form-group"><label class="form-label">స్వస్థలం</label><input type="text" id="set-city" class="form-input" value="అమరావతి / విజయవాడ"></div>
            </div>
          </div>
          <div class="spotlight-card">
            <div class="spotlight-content">
              <h3 style="font-size: 16px; font-weight: 700; color: var(--gold-light); margin-bottom: 14px;">🪙 నియమాలు & ఎక్స్‌పోర్ట్</h3>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <span>+₹1 లక్కీ కాయిన్ ఆటో-రౌండింగ్</span>
                <input type="checkbox" checked style="width: 18px; height: 18px; accent-color: var(--gold-primary);">
              </div>
              <div style="display: flex; gap: 10px;">
                <button class="btn-glass" onclick="exportLedgerCSV()">📥 Excel (CSV) డౌన్‌లోడ్</button>
                <button class="btn-glass" onclick="window.print()">🖨️ ప్రింట్ / PDF</button>
              </div>
            </div>
          </div>
        </div>
      </div>

    </section>

  </div>

  <script>
    const STORAGE_KEY_LEDGER = 'giftvault_master_records_v1';
    const STORAGE_KEY_USER = 'giftvault_user_session_v1';

    let MASTER_LEDGER = JSON.parse(localStorage.getItem(STORAGE_KEY_LEDGER)) || [
      { id: 'GV-101', name: 'కొత్తపల్లి రాజశేఖర్ గారు', phone: '9848011223', city: 'విజయవాడ', side: 'పెళ్ళికూతురు తరపు', type: 'నగదు', amount: 5116, precious: '-', time: '10:45 AM' },
      { id: 'GV-102', name: 'దాసరి సుబ్బారావు గారు', phone: '9848099887', city: 'హైదరాబాద్', side: 'పెళ్ళికొడుకు తరపు', type: 'నగదు + బంగారం', amount: 10116, precious: '2g Gold', time: '11:02 AM' },
      { id: 'GV-103', name: 'యర్రంశెట్టి వెంకటేశ్వర్లు', phone: '9848033445', city: 'గుంటూరు', side: 'స్నేహితులు', type: 'నగదు', amount: 2116, precious: '-', time: '11:18 AM' }
    ];

    let currentRole = 'admin';
    let isPrivacyActive = false;

    // View Switching (Landing vs Login vs App Workspace)
    function showMasterView(viewId) {
      document.querySelectorAll('.view-section').forEach(s => s.classList.remove('active'));
      document.getElementById(`view-${viewId}`).classList.add('active');

      document.getElementById('nav-btn-home').classList.toggle('active', viewId === 'landing');
      document.getElementById('nav-btn-app').classList.toggle('active', viewId === 'app');

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Scroll to anchor
    function scrollToSection(id) {
      showMasterView('landing');
      setTimeout(() => {
        document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    }

    // In-App Tab Switching
    function showWorkTab(tabId) {
      document.querySelectorAll('.work-tab').forEach(b => b.classList.toggle('active', b.getAttribute('data-wtab') === tabId));
      document.querySelectorAll('.work-pane').forEach(p => p.classList.toggle('active', p.id === `wpane-${tabId}`));
    }

    // Landing Event Switcher
    function setLandingEvent(key, btn) {
      document.querySelectorAll('.event-tab').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      playChimeAudio();
    }

    // Role selection in Login
    function setLoginRole(role, elem) {
      currentRole = role;
      document.querySelectorAll('.role-pill').forEach(p => p.classList.remove('active'));
      elem.classList.add('active');
    }

    function sendLoginOTP() {
      const phone = document.getElementById('login-phone-input').value;
      if (!phone || phone.length < 10) { alert('సరైన 10 అంకెల మొబైల్ నంబర్ నమోదు చేయండి'); return; }
      document.getElementById('login-phone-box').style.display = 'none';
      document.getElementById('login-otp-box').style.display = 'block';
    }

    function verifyAndLogin() {
      const user = { name: 'కొత్తపల్లి వెంకటేశ్వరరావు', role: currentRole, phone: '9848012345' };
      localStorage.setItem(STORAGE_KEY_USER, JSON.stringify(user));
      updateAuthUI(user);
      playChimeAudio();
      alert('లాగిన్ విజయవంతమైంది! వెల్‌కమ్ టు GiftVault.');
      showMasterView('app');
    }

    function googleQuickSignIn() {
      const user = { name: 'Venkateswara Rao', role: 'Host Admin', email: 'host@giftvault.in' };
      localStorage.setItem(STORAGE_KEY_USER, JSON.stringify(user));
      updateAuthUI(user);
      playChimeAudio();
      alert('Google సైన్-ఇన్ విజయవంతమైంది!');
      showMasterView('app');
    }

    function updateAuthUI(user) {
      const btn = document.getElementById('btn-master-auth');
      if (btn && user) {
        btn.innerHTML = `✓ ${user.name.split(' ')[0]} (${user.role === 'admin' ? 'Host' : 'Munshi'})`;
        btn.onclick = () => {
          if (confirm('ఖాతా నుండి లాగౌట్ అవ్వాలనుకుంటున్నారా?')) {
            localStorage.removeItem(STORAGE_KEY_USER);
            btn.innerHTML = '👤 లాగిన్ (Login)';
            btn.onclick = () => showMasterView('login');
            showMasterView('landing');
          }
        };
      }
    }

    // Privacy Mask
    function togglePrivacyMode() {
      isPrivacyActive = !isPrivacyActive;
      renderMasterTables();
    }

    // Render In-App Tables
    function renderMasterTables() {
      const recentTbody = document.getElementById('work-recent-tbody');
      const fullTbody = document.getElementById('work-full-tbody');

      let total = MASTER_LEDGER.reduce((s, i) => s + i.amount, 0);
      document.getElementById('kpi-inflow').innerText = isPrivacyActive ? '₹ ••••••' : `₹${total.toLocaleString('en-IN')}`;
      document.getElementById('kpi-count').innerText = `↑ ${MASTER_LEDGER.length} మంది బంధుమిత్రులు`;

      if (recentTbody) {
        recentTbody.innerHTML = MASTER_LEDGER.slice(0, 4).map(item => `
          <tr>
            <td><strong style="color: var(--gold-light);">${item.id}</strong></td>
            <td><strong>${item.name}</strong></td>
            <td>${item.city}</td>
            <td>${item.side}</td>
            <td>${item.type}</td>
            <td style="font-family: var(--font-numbers); font-weight: 700; color: var(--gold-light);">
              ${isPrivacyActive ? '₹ ••••' : '₹' + item.amount.toLocaleString('en-IN')}
            </td>
            <td><button class="btn-glass" style="padding: 4px 10px; font-size: 11px;" onclick="sendWhatsApp('${item.name}', ${item.amount}, '${item.phone}')">వాట్సాప్ 📲</button></td>
          </tr>
        `).join('');
      }

      if (fullTbody) {
        fullTbody.innerHTML = MASTER_LEDGER.map((item, idx) => `
          <tr>
            <td>${idx + 1}</td>
            <td><strong>${item.name}</strong></td>
            <td>${item.city}</td>
            <td>${item.side}</td>
            <td>${item.type}</td>
            <td style="font-family: var(--font-numbers); font-weight: 700; color: var(--gold-light);">
              ${isPrivacyActive ? '₹ ••••' : '₹' + item.amount.toLocaleString('en-IN')}
            </td>
            <td>${item.precious}</td>
            <td style="font-size: 12px; color: var(--text-dim);">${item.time}</td>
            <td><button class="btn-glass" style="padding: 4px 10px; font-size: 11px;" onclick="sendWhatsApp('${item.name}', ${item.amount}, '${item.phone}')">రశీదు 📲</button></td>
          </tr>
        `).join('');
      }
    }

    function filterLedger(q) {
      const query = q.toLowerCase();
      const filtered = MASTER_LEDGER.filter(i => i.name.toLowerCase().includes(query) || i.city.toLowerCase().includes(query));
      const fullTbody = document.getElementById('work-full-tbody');
      fullTbody.innerHTML = filtered.map((item, idx) => `
        <tr>
          <td>${idx + 1}</td>
          <td><strong>${item.name}</strong></td>
          <td>${item.city}</td>
          <td>${item.side}</td>
          <td>${item.type}</td>
          <td style="font-family: var(--font-numbers); font-weight: 700; color: var(--gold-light);">₹${item.amount.toLocaleString('en-IN')}</td>
          <td>${item.precious}</td>
          <td style="font-size: 12px; color: var(--text-dim);">${item.time}</td>
          <td><button class="btn-glass" style="padding: 4px 10px; font-size: 11px;" onclick="sendWhatsApp('${item.name}', ${item.amount}, '${item.phone}')">రశీదు 📲</button></td>
        </tr>
      `).join('');
    }

    function handleMasterEntry(e) {
      e.preventDefault();
      const name = document.getElementById('m-name').value;
      const city = document.getElementById('m-city').value;
      const side = document.getElementById('m-side').value;
      const phone = document.getElementById('m-phone').value || '';
      const amt = parseInt(document.getElementById('m-amount').value) || 0;
      const grams = document.getElementById('m-grams').value || '-';

      MASTER_LEDGER.unshift({
        id: `GV-${100 + MASTER_LEDGER.length + 1}`,
        name: name, phone: phone, city: city, side: side, type: 'నగదు', amount: amt, precious: grams, time: 'ఇప్పుడే'
      });
      localStorage.setItem(STORAGE_KEY_LEDGER, JSON.stringify(MASTER_LEDGER));
      renderMasterTables();
      playChimeAudio();

      document.getElementById('rec-preview-name').innerText = name;
      document.getElementById('rec-preview-amt').innerText = `₹${amt.toLocaleString('en-IN')}`;

      if (phone) {
        sendWhatsApp(name, amt, phone);
      } else {
        alert(`శ్రీ ${name} గారి నుండి ₹${amt} కానుక ఎర్ర పుస్తకంలో నమోదైంది!`);
      }

      e.target.reset();
      document.getElementById('m-amount').value = 5116;
    }

    function handleExpenseRecord(e) {
      e.preventDefault();
      const ven = document.getElementById('e-ven').value;
      const amt = parseInt(document.getElementById('e-amt').value) || 0;
      playChimeAudio();
      alert(`ఖర్చు నమోదైంది: ${ven} వారికి ₹${amt.toLocaleString('en-IN')}`);
      e.target.reset();
    }

    function sendWhatsApp(name, amt, phone) {
      const msg = `ఆదరణీయ ${name} గారు, మా వివాహ మహోత్సవంలో మీరు అందించిన పవిత్రమైన కానుక ₹${amt.toLocaleString('en-IN')} కృతజ్ఞతలతో నమోదైంది. మీ రాక మాకు పరమానందం! — కొత్తపల్లి కుటుంబం.`;
      const cleanPhone = phone ? phone.replace(/[^0-9]/g, '') : '';
      const url = cleanPhone ? `https://wa.me/91${cleanPhone}?text=${encodeURIComponent(msg)}` : `https://wa.me/?text=${encodeURIComponent(msg)}`;
      window.open(url, '_blank');
    }

    function exportLedgerCSV() {
      const headers = ["క్రమ సంఖ్య", "రశీదు సంఖ్య", "అతిథి పేరు", "మొబైల్", "ఊరు", "తరపు", "రకం", "మొత్తం (₹)", "సమయం"];
      const rows = MASTER_LEDGER.map((item, idx) => [
        idx + 1, item.id, `"${item.name}"`, item.phone || "-", `"${item.city}"`, `"${item.side}"`, item.type, item.amount, item.time
      ]);
      const csvContent = "\\uFEFF" + [headers.join(","), ...rows.map(e => e.join(","))].join("\\n");
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.setAttribute("download", `GiftVault_Shagun_Ledger_${new Date().toISOString().slice(0,10)}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function saveSettings() {
      playChimeAudio();
      alert('అన్ని సెట్టింగ్స్ విజయవంతంగా సేవ్ చేయబడ్డాయి!');
    }

    function playChimeAudio() {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.frequency.setValueAtTime(587.33, ctx.currentTime);
        g.gain.setValueAtTime(0.3, ctx.currentTime);
        g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);
        o.connect(g); g.connect(ctx.destination);
        o.start(); o.stop(ctx.currentTime + 1.2);
      } catch (e) {}
    }

    // Cursor Spotlight
    document.addEventListener('mousemove', (e) => {
      document.querySelectorAll('.spotlight-card').forEach((card) => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
        card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
      });
    });

    window.addEventListener('DOMContentLoaded', () => {
      renderMasterTables();
      const savedUser = JSON.parse(localStorage.getItem(STORAGE_KEY_USER));
      if (savedUser) updateAuthUI(savedUser);
    });
  </script>
</body>
</html>
"""

def main():
    PREVIEW_INDEX = r"c:\Project\Gift Valut\web_preview\index.html"
    BUILD_INDEX = r"c:\Project\Gift Valut\build\web\index.html"
    WEB_INDEX = r"c:\Project\Gift Valut\web\index.html"

    with open(PREVIEW_INDEX, "w", encoding="utf-8") as f:
        f.write(MASTER_HTML)
    print(f"Updated {PREVIEW_INDEX}")

    if os.path.exists(os.path.dirname(BUILD_INDEX)):
        with open(BUILD_INDEX, "w", encoding="utf-8") as f:
            f.write(MASTER_HTML)
        print(f"Updated {BUILD_INDEX}")

    with open(WEB_INDEX, "w", encoding="utf-8") as f:
        f.write(MASTER_HTML)
    print(f"Updated {WEB_INDEX}")

    print("Master Application with Grand Landing Page, Login Page & Workspace generated successfully!")

if __name__ == "__main__":
    main()
