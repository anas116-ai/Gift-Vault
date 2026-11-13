# -*- coding: utf-8 -*-
"""
Generate Separate, Dedicated Desktop and Mobile Versions for GiftVault
- desktop.html: Pure 100% Full-Screen Desktop Experience (No fake mobile chassis)
- mobile.html: Pure 100% Full-Screen Native Mobile App UI (Bottom Nav, Touch Cards, Mobile Munshi)
- index.html: Smart Device Router (Auto-detects device & routes cleanly + testing switcher)
"""
import os
import shutil

PREVIEW_DIR = r"c:\Project\Gift Valut\web_preview"
WEB_DIR = r"c:\Project\Gift Valut\web"

# ==============================================================================
# 1. DESKTOP HTML TEMPLATE
# ==============================================================================
DESKTOP_HTML = """<!DOCTYPE html>
<html lang="te" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault (గిఫ్ట్ వాలెట్) • Desktop Edition</title>
  
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
      --ease-snappy: cubic-bezier(0.23, 1, 0.32, 1);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
      line-height: 1.5;
      overflow-x: hidden;
    }

    /* Ambient Aurora Glow */
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

    .desktop-container {
      position: relative; z-index: 1; max-width: 1440px; margin: 0 auto;
      padding: 0 32px 80px 32px;
    }

    /* Desktop Top Header */
    .desktop-header {
      display: flex; align-items: center; justify-content: space-between;
      padding: 24px 0; border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 32px; position: sticky; top: 0;
      background: rgba(8, 9, 13, 0.88); backdrop-filter: blur(24px); z-index: 100;
    }
    .brand-wrap {
      display: flex; align-items: center; gap: 14px; text-decoration: none; color: inherit;
    }
    .brand-icon {
      width: 44px; height: 44px; border-radius: 14px;
      background: linear-gradient(135deg, #1C2333 0%, #0F131D 100%);
      border: 1px solid rgba(229, 184, 105, 0.35);
      display: flex; align-items: center; justify-content: center;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .brand-name {
      font-family: var(--font-display); font-size: 22px; font-weight: 700;
      letter-spacing: -0.02em;
    }
    .brand-gold {
      background: linear-gradient(135deg, #FFDF88 0%, #E5B869 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .brand-sub { font-size: 11px; font-weight: 600; letter-spacing: 0.05em; color: var(--text-muted); }

    .header-actions { display: flex; align-items: center; gap: 16px; }

    /* Switch to mobile test pill */
    .switch-pill {
      background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-subtle);
      border-radius: 100px; padding: 6px 14px; font-size: 12px; font-weight: 600;
      color: var(--text-muted); text-decoration: none; display: flex; align-items: center; gap: 6px;
      transition: all 0.2s ease;
    }
    .switch-pill:hover {
      background: rgba(229, 184, 105, 0.15); border-color: var(--gold-primary); color: var(--gold-light);
    }

    /* Language select */
    .lang-dropdown {
      background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-subtle);
      color: var(--text-main); font-size: 13px; font-weight: 600; padding: 8px 14px;
      border-radius: 12px; cursor: pointer; outline: none;
    }

    /* Shimmer Button */
    .btn-shimmer {
      position: relative; overflow: hidden;
      background: linear-gradient(135deg, #E5B869 0%, #C89B48 100%);
      color: #08090D; font-family: var(--font-body); font-weight: 700; font-size: 14px;
      border-radius: 12px; padding: 10px 22px; border: 1px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 4px 20px rgba(229, 184, 105, 0.35); cursor: pointer;
      display: inline-flex; align-items: center; gap: 8px; transition: all 0.25s var(--ease-spring);
    }
    .btn-shimmer::before {
      content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
      background: linear-gradient(60deg, transparent 20%, rgba(255, 255, 255, 0.6) 50%, transparent 80%);
      transform: translateX(-100%); animation: shimmer 4s infinite ease-in-out; pointer-events: none;
    }
    @keyframes shimmer {
      0% { transform: translateX(-100%) rotate(25deg); }
      30%, 100% { transform: translateX(100%) rotate(25deg); }
    }
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

    /* Spotlight Card */
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
    .spotlight-card:hover {
      transform: translateY(-2px); border-color: rgba(229, 184, 105, 0.35);
      box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.6);
    }
    .spotlight-content { position: relative; z-index: 2; }

    /* Desktop Navigation Tabs */
    .desktop-tabs-bar {
      display: flex; gap: 8px; margin-bottom: 30px; background: rgba(14, 18, 27, 0.85);
      border: 1px solid var(--border-subtle); border-radius: 16px; padding: 6px;
      backdrop-filter: blur(16px);
    }
    .desk-tab {
      padding: 10px 20px; border-radius: 12px; border: none; background: transparent;
      color: var(--text-muted); font-family: var(--font-body); font-size: 14px; font-weight: 600;
      cursor: pointer; display: flex; align-items: center; gap: 8px;
      transition: all 0.25s var(--ease-spring);
    }
    .desk-tab:hover { color: var(--text-main); background: rgba(255, 255, 255, 0.04); }
    .desk-tab.active {
      background: linear-gradient(135deg, rgba(229, 184, 105, 0.2) 0%, rgba(200, 155, 72, 0.1) 100%);
      color: var(--gold-light); border: 1px solid rgba(229, 184, 105, 0.35);
      box-shadow: 0 4px 15px rgba(229, 184, 105, 0.15);
    }

    /* Dynamic Event Switcher Bar */
    .event-selection-strip {
      display: flex; justify-content: space-between; align-items: center;
      background: rgba(22, 27, 38, 0.6); border: 1px solid var(--border-subtle);
      border-radius: 16px; padding: 14px 20px; margin-bottom: 28px;
    }
    .event-chips { display: flex; gap: 8px; }
    .event-chip-btn {
      padding: 6px 14px; border-radius: 10px; border: 1px solid transparent;
      background: transparent; color: var(--text-muted); font-size: 13px; font-weight: 600;
      cursor: pointer; display: flex; align-items: center; gap: 6px;
      transition: all 0.2s ease;
    }
    .event-chip-btn.active {
      background: rgba(229, 184, 105, 0.15); border-color: rgba(229, 184, 105, 0.4);
      color: var(--gold-light);
    }

    /* KPI Grid */
    .kpi-grid {
      display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 30px;
    }
    .kpi-label { font-size: 13px; font-weight: 600; color: var(--text-muted); margin-bottom: 8px; }
    .kpi-num {
      font-family: var(--font-numbers); font-size: 32px; font-weight: 800;
      letter-spacing: -0.02em; color: var(--text-main); margin-bottom: 6px;
    }

    /* Desktop Form & Two Column Split */
    .split-grid {
      display: grid; grid-template-columns: 1.25fr 0.75fr; gap: 24px;
    }
    .form-group { margin-bottom: 18px; }
    .form-label { display: block; font-size: 13px; font-weight: 600; color: var(--text-muted); margin-bottom: 6px; }
    .form-input {
      width: 100%; background: rgba(255, 255, 255, 0.04); border: 1px solid var(--border-subtle);
      border-radius: 12px; padding: 12px 16px; color: var(--text-main); font-family: inherit;
      font-size: 14px; outline: none; transition: all 0.2s ease;
    }
    .form-input:focus {
      border-color: var(--gold-primary); box-shadow: 0 0 15px rgba(229, 184, 105, 0.2);
    }

    /* Luxury Table */
    .luxury-table { width: 100%; border-collapse: collapse; font-size: 14px; }
    .luxury-table th {
      text-align: left; padding: 14px 16px; color: var(--gold-light); font-weight: 700;
      border-bottom: 1px solid rgba(229, 184, 105, 0.25); font-family: var(--font-display);
    }
    .luxury-table td {
      padding: 16px; border-bottom: 1px solid rgba(255, 255, 255, 0.05); color: var(--text-main);
    }
    .luxury-table tr:hover td { background: rgba(229, 184, 105, 0.05); }

    /* Red Book Container */
    .red-book-box {
      background: #18090C; border: 2px solid #5C1D24; border-radius: 20px;
      padding: 30px; box-shadow: 0 20px 60px rgba(0,0,0,0.8); position: relative;
    }

    /* Subtab panes */
    .tab-pane { display: none; }
    .tab-pane.active { display: block; animation: fadeIn 0.3s var(--ease-spring); }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
  </style>
</head>
<body>
  <div class="ambient-aurora">
    <div class="aurora-orb-1"></div>
    <div class="aurora-orb-2"></div>
  </div>

  <div class="desktop-container">
    <!-- Header -->
    <header class="desktop-header">
      <div class="brand-wrap">
        <div class="brand-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#E5B869" stroke-width="1.8">
            <path d="M12 2L3 7V17L12 22L21 17V7L12 2Z"/>
            <circle cx="12" cy="12" r="3.5" stroke="#FFDF88"/>
          </svg>
        </div>
        <div>
          <div class="brand-name">GIFT<span class="brand-gold">VAULT</span></div>
          <div class="brand-sub">DESKTOP CELEBRATION LEDGER • గిఫ్ట్ వాలెట్</div>
        </div>
      </div>

      <div class="header-actions">
        <!-- Switch to Pure Mobile View link for testing -->
        <a href="mobile.html" class="switch-pill">
          <span>📱 మొబైల్ వెర్షన్ చూడండి (Mobile App View)</span>
        </a>

        <select class="lang-dropdown" onchange="alert('భాష మార్చబడింది: ' + this.value)">
          <option value="te" selected>తెలుగు (Telugu)</option>
          <option value="en">English (Global)</option>
          <option value="hi">हिंदी (Hindi)</option>
        </select>

        <button class="btn-shimmer" onclick="showTab('desk')">
          + కొత్త కానుక ఎంట్రీ (Add Shagun)
        </button>
      </div>
    </header>

    <!-- Event Selection Strip -->
    <div class="event-selection-strip">
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="font-size: 24px;" id="desk-event-icon">💍</span>
        <div>
          <div style="font-weight: 700; font-size: 16px;" id="desk-event-title">రాహుల్ & స్నిగ్ధ వివాహ వేడుక</div>
          <div style="font-size: 12px; color: var(--gold-light);" id="desk-event-detail">వధూవరులు • హైదరాబాద్ • ప్రత్యక్ష వేదిక</div>
        </div>
      </div>

      <div class="event-chips">
        <button class="event-chip-btn active" onclick="setDesktopEvent('wedding', this)">💍 పెళ్లి</button>
        <button class="event-chip-btn" onclick="setDesktopEvent('birthday', this)">👶 బర్త్‌డే</button>
        <button class="event-chip-btn" onclick="setDesktopEvent('halfsaree', this)">🪷 హాఫ్ శారీ</button>
        <button class="event-chip-btn" onclick="setDesktopEvent('dhoti', this)">🧵 ఉపనయనం</button>
        <button class="event-chip-btn" onclick="setDesktopEvent('housewarming', this)">🏡 గృహప్రవేశం</button>
      </div>
    </div>

    <!-- Desktop Navigation Tabs -->
    <nav class="desktop-tabs-bar">
      <button class="desk-tab active" data-tab="dashboard" onclick="showTab('dashboard')">📊 డాష్‌బోర్డ్ (Dashboard)</button>
      <button class="desk-tab" data-tab="desk" onclick="showTab('desk')">⚡ మున్షీ డెస్క్ (Munshi Entry)</button>
      <button class="desk-tab" data-tab="ledger" onclick="showTab('ledger')">📜 ఎర్ర పుస్తకం (Red Ledger)</button>
      <button class="desk-tab" data-tab="expenses" onclick="showTab('expenses')">💸 ఖర్చులు (Expenses)</button>
      <button class="desk-tab" data-tab="reciprocity" onclick="showTab('reciprocity')">🔄 పరస్పర లెక్కలు (Reciprocity)</button>
      <button class="desk-tab" data-tab="invites" onclick="showTab('invites')">💌 ఆహ్వానాలు & RSVP</button>
      <button class="desk-tab" data-tab="qr" onclick="showTab('qr')">🔊 సౌండ్‌బాక్స్ & QR</button>
    </nav>

    <!-- TAB 1: DASHBOARD -->
    <div class="tab-pane active" id="pane-dashboard">
      <div class="kpi-grid">
        <div class="spotlight-card">
          <div class="spotlight-content">
            <div class="kpi-label">మొత్తం కానుకల వసూలు (Inflow)</div>
            <div class="kpi-num" style="color: var(--gold-light);" id="desk-kpi-inflow">₹8,42,101</div>
            <div style="font-size: 12px; color: var(--emerald-green); font-weight: 600;">↑ 148 మంది బంధుమిత్రులు</div>
          </div>
        </div>
        <div class="spotlight-card">
          <div class="spotlight-content">
            <div class="kpi-label">మొత్తం ఫంక్షన్ ఖర్చులు (Expenses)</div>
            <div class="kpi-num" style="color: var(--ruby-red);" id="desk-kpi-expenses">₹4,15,000</div>
            <div style="font-size: 12px; color: var(--text-muted);">క్యాటరింగ్, కల్యాణ మండపం</div>
          </div>
        </div>
        <div class="spotlight-card">
          <div class="spotlight-content">
            <div class="kpi-label">నికర మిగులు నిల్వ (Net Surplus)</div>
            <div class="kpi-num" style="color: var(--emerald-green);" id="desk-kpi-surplus">+₹4,27,101</div>
            <div style="font-size: 12px; color: var(--emerald-green); font-weight: 600;">✓ లాభంలో ఉంది</div>
          </div>
        </div>
        <div class="spotlight-card">
          <div class="spotlight-content">
            <div class="kpi-label">బంగారం & వెండి కానుకలు</div>
            <div class="kpi-num" id="desk-kpi-gold">42.5 <span style="font-size: 16px; color: var(--gold-light);">g Gold</span></div>
            <div style="font-size: 12px; color: var(--text-muted);">వెండి: 550 గ్రాములు (14 పాత్రలు)</div>
          </div>
        </div>
      </div>

      <!-- Recent Entries Table -->
      <div class="spotlight-card">
        <div class="spotlight-content">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700;">ఇటీవలి కానుకల ఎంట్రీలు (Recent Shagun Received)</h3>
            <button class="btn-glass" onclick="showTab('ledger')">మొత్తం చూడండి (View All)</button>
          </div>
          <table class="luxury-table">
            <thead>
              <tr>
                <th>రశీదు సంఖ్య</th>
                <th>అతిథి పేరు</th>
                <th>ఊరు (City)</th>
                <th>తరపు / సంబంధం</th>
                <th>కానుక రకం</th>
                <th>మొత్తం (₹)</th>
                <th>చర్య</th>
              </tr>
            </thead>
            <tbody id="desk-recent-tbody"></tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 2: MUNSHI FAST ENTRY DESK -->
    <div class="tab-pane" id="pane-desk">
      <div class="split-grid">
        <div class="spotlight-card">
          <div class="spotlight-content">
            <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 20px; color: var(--gold-light);">
              ⚡ మున్షీ వేగవంతమైన ఎంట్రీ డెస్క్ (Munshi Fast Entry Desk)
            </h2>
            <form onsubmit="handleDesktopEntry(event)">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                <div class="form-group">
                  <label class="form-label">అతిథి పూర్తి పేరు (Guest Name) *</label>
                  <input type="text" id="desk-name" class="form-input" placeholder="ఉదా: నారాయణ రావు గారు" required>
                </div>
                <div class="form-group">
                  <label class="form-label">ఊరు / నగరం (AP & TG Smart Autocomplete) *</label>
                  <input type="text" id="desk-city" class="form-input" list="cities-list" placeholder="విజయవాడ, హైదరాబాద్..." required>
                  <datalist id="cities-list">
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
                  <select id="desk-side" class="form-input">
                    <option value="పెళ్ళికూతురు తరపు (Bride Side)">పెళ్ళికూతురు తరపు (Bride Side)</option>
                    <option value="పెళ్ళికొడుకు తరపు (Groom Side)">పెళ్ళికొడుకు తరపు (Groom Side)</option>
                    <option value="స్నేహితులు (Friends)">స్నేహితులు (Friends)</option>
                    <option value="బంధువులు (Relatives)">బంధువులు (Relatives)</option>
                  </select>
                </div>
                <div class="form-group">
                  <label class="form-label">మొబైల్ నంబర్ (WhatsApp రశీదు కోసం)</label>
                  <input type="tel" id="desk-phone" class="form-input" placeholder="98480xxxxx">
                </div>
              </div>

              <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 16px;">
                <div class="form-group">
                  <label class="form-label">మొత్తం నగదు (Amount ₹) *</label>
                  <input type="number" id="desk-amount" class="form-input" value="5116" required style="font-family: var(--font-numbers); font-size: 20px; font-weight: 700; color: var(--gold-light);">
                </div>
                <div class="form-group">
                  <label class="form-label">బంగారం / వెండి (గ్రాములు)</label>
                  <input type="text" id="desk-grams" class="form-input" placeholder="ఉదా: 2 గ్రాములు">
                </div>
              </div>

              <div style="display: flex; align-items: center; justify-content: space-between; padding: 12px 16px; background: rgba(229,184,105,0.08); border-radius: 12px; margin-bottom: 20px;">
                <span style="font-size: 13px; font-weight: 600;">+₹1 లక్కీ కాయిన్ ఆటో-రౌండింగ్ (116, 516, 1116, 5116)</span>
                <input type="checkbox" checked style="width: 18px; height: 18px; accent-color: var(--gold-primary);">
              </div>

              <button type="submit" class="btn-shimmer" style="width: 100%; justify-content: center; padding: 14px; font-size: 16px;">
                💾 భద్రపరచండి & వాట్సాప్ రశీదు పంపండి (Save & Send WhatsApp Receipt)
              </button>
            </form>
          </div>
        </div>

        <!-- Live Soundbox & WhatsApp Preview -->
        <div class="spotlight-card">
          <div class="spotlight-content">
            <h3 style="font-family: var(--font-display); font-size: 16px; font-weight: 700; color: var(--gold-light); margin-bottom: 12px;">
              🔊 లైవ్ సౌండ్‌బాక్స్ & ఆడియో చైమ్
            </h3>
            <div style="background: rgba(0,0,0,0.4); border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 20px;">
              <button class="btn-glass" onclick="playDeskChime()">▶ చైమ్ టెస్ట్ చేయండి (Test Bell)</button>
            </div>

            <h3 style="font-family: var(--font-display); font-size: 16px; font-weight: 700; margin-bottom: 10px;">
              డిజిటల్ రశీదు ప్రివ్యూ
            </h3>
            <div style="background: #111520; border: 1px dashed rgba(229,184,105,0.3); border-radius: 12px; padding: 16px; font-size: 12px; line-height: 1.7; color: var(--text-muted);">
              <div style="font-weight: 700; color: var(--gold-light); text-align: center; margin-bottom: 6px;">💍 గిఫ్ట్ వాలెట్ డిజిటల్ రశీదు</div>
              శ్రీ <strong style="color: var(--text-main);" id="desk-rec-name">కొత్తపల్లి రాజశేఖర్ గారు</strong>,<br>
              వివాహ మహోత్సవంలో మీరు అందించిన కానుక <strong style="color: var(--gold-light);" id="desk-rec-amt">₹5,116</strong> కృతజ్ఞతలతో నమోదైంది.<br>
              <em>మీ రాక మాకు ఆనందదాయకం!</em>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 3: LEDGER (ERRA PUSTHAKAM) -->
    <div class="tab-pane" id="pane-ledger">
      <div class="red-book-box">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; border-bottom: 1px solid rgba(229,184,105,0.3); padding-bottom: 16px;">
          <div>
            <h2 style="font-family: var(--font-display); font-size: 24px; font-weight: 700; color: var(--gold-light);">
              📜 సంప్రదాయ ఎర్ర పుస్తకం (Official Erra Pusthakam Ledger)
            </h2>
            <div style="font-size: 13px; color: var(--text-muted);">అమరావతి & తెలంగాణ గ్రామీణ లెక్కల శగున్ చిట్టా</div>
          </div>
          <div style="display: flex; gap: 10px;">
            <input type="text" class="form-input" placeholder="🔍 పేరు లేదా ఊరు వెతకండి..." oninput="filterDesktopLedger(this.value)" style="width: 240px; padding: 8px 14px; font-size: 13px;">
            <button class="btn-shimmer" onclick="alert('ఎర్ర పుస్తకం PDF డౌన్‌లోడ్ పూర్తయింది!')" style="font-size: 13px; padding: 8px 16px;">📥 PDF డౌన్‌లోడ్</button>
          </div>
        </div>

        <table class="luxury-table">
          <thead>
            <tr>
              <th>క్ర.సం</th>
              <th>అతిథి పేరు</th>
              <th>ఊరు / ప్రాంతం</th>
              <th>తరపు / గోత్రం</th>
              <th>కానుక రకం</th>
              <th>మొత్తం (₹)</th>
              <th>బంగారం/వెండి</th>
              <th>సమయం</th>
            </tr>
          </thead>
          <tbody id="desk-full-tbody"></tbody>
        </table>
      </div>
    </div>

    <!-- TAB 4: EXPENSES -->
    <div class="tab-pane" id="pane-expenses">
      <div class="split-grid">
        <div class="spotlight-card">
          <div class="spotlight-content">
            <h2 style="font-family: var(--font-display); font-size: 20px; font-weight: 700; margin-bottom: 16px;">💸 ఈవెంట్ ఖర్చు నమోదు</h2>
            <form onsubmit="handleDeskExpense(event)">
              <div class="form-group">
                <label class="form-label">కేటగిరీ</label>
                <select class="form-input" id="exp-cat">
                  <option>క్యాటరింగ్ & భోజనాలు (Catering)</option>
                  <option>కల్యాణ మండపం అద్దె (Hall)</option>
                  <option>ఫోటో & వీడియో గ్రఫీ (Photography)</option>
                  <option>పూల అలంకరణ & డెకరేషన్ (Decoration)</option>
                </select>
              </div>
              <div class="form-group">
                <label class="form-label">వెండర్ పేరు</label>
                <input type="text" class="form-input" id="exp-ven" placeholder="ఉదా: సుబ్బారావు క్యాటరర్స్" required>
              </div>
              <div class="form-group">
                <label class="form-label">మొత్తం (₹) *</label>
                <input type="number" class="form-input" id="exp-val" placeholder="50000" required style="color: var(--ruby-red); font-weight: 700;">
              </div>
              <button type="submit" class="btn-shimmer" style="width: 100%; justify-content: center;">+ ఖర్చు నమోదు చేయండి</button>
            </form>
          </div>
        </div>

        <div class="spotlight-card">
          <div class="spotlight-content">
            <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; color: var(--gold-light); margin-bottom: 14px;">ఆర్థిక విశ్లేషణ & మిగులు</h3>
            <div style="background: rgba(0,0,0,0.3); border-radius: 12px; padding: 18px; line-height: 2; font-size: 14px;">
              మొత్తం కానుకలు: <strong style="color: var(--gold-light);">₹8,42,101</strong><br>
              మొత్తం ఖర్చులు: <strong style="color: var(--ruby-red);">-₹4,15,000</strong><br>
              <div style="border-top: 1px solid var(--border-subtle); margin-top: 8px; padding-top: 8px; font-size: 16px;">
                నికర మిగులు (Net Surplus): <strong style="color: var(--emerald-green);">+₹4,27,101</strong>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: RECIPROCITY -->
    <div class="tab-pane" id="pane-reciprocity">
      <div class="spotlight-card">
        <div class="spotlight-content">
          <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 16px;">🔄 పరస్పర శగున్ లెక్కింపు (Reciprocity Intelligence)</h2>
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

    <!-- TAB 6: INVITES -->
    <div class="tab-pane" id="pane-invites">
      <div class="split-grid">
        <div class="spotlight-card">
          <div class="spotlight-content">
            <h2 style="font-family: var(--font-display); font-size: 20px; font-weight: 700; margin-bottom: 16px;">💌 వాట్సాప్ ఆహ్వానాలు (Digital RSVP)</h2>
            <div class="form-group"><label class="form-label">అతిథి పేరు</label><input type="text" class="form-input" placeholder="ఉదా: శ్రీనివాసరావు గారు"></div>
            <div class="form-group"><label class="form-label">మొబైల్ సంఖ్య</label><input type="tel" class="form-input" placeholder="98480xxxxx"></div>
            <button class="btn-shimmer" style="width: 100%; justify-content: center;" onclick="alert('వాట్సాప్ ఆహ్వానం పంపబడింది!')">📲 శుభలేఖ కార్డు పంపండి</button>
          </div>
        </div>
        <div class="spotlight-card">
          <div class="spotlight-content">
            <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; color: var(--gold-light); margin-bottom: 14px;">RSVP స్థితి</h3>
            <div style="font-size: 14px; line-height: 2;">
              మొత్తం ఆహ్వానితులు: <strong>450 మంది</strong><br>
              ధృవీకరించినవారు (Confirmed): <strong style="color: var(--emerald-green);">385 మంది</strong><br>
              భోజనాల ప్లానింగ్: <strong>500 ప్లేట్లు</strong>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 7: SOUNDBOX QR -->
    <div class="tab-pane" id="pane-qr">
      <div class="split-grid">
        <div class="spotlight-card" style="text-align: center; padding: 30px;">
          <div class="spotlight-content">
            <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700; margin-bottom: 12px;">డిజిటల్ శగున్ UPI QR</h2>
            <div style="background: #FFF; padding: 16px; border-radius: 16px; width: 200px; height: 200px; margin: 0 auto 16px auto;">
              <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi://pay?pa=giftvault.shagun@hdfcbank&pn=RahulSnigdhaWedding&am=5116&cu=INR" style="width: 100%; height: 100%;">
            </div>
            <div style="font-family: var(--font-numbers); font-size: 24px; font-weight: 800; color: var(--gold-light); margin-bottom: 12px;">₹5,116</div>
            <button class="btn-shimmer" onclick="playDeskChime(); alert('🔊 సౌండ్‌బాక్స్: గిఫ్ట్ వాలెట్ లో ₹5,116 కానుక అందింది!')">🔊 సౌండ్‌బాక్స్ టెస్ట్ చేయండి</button>
          </div>
        </div>
        <div class="spotlight-card">
          <div class="spotlight-content">
            <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; color: var(--gold-light); margin-bottom: 12px;">సౌండ్‌బాక్స్ ప్రయోజనాలు:</h3>
            <ul style="font-size: 14px; line-height: 2; color: var(--text-muted); padding-left: 20px;">
              <li>క్షణం ఆలస్యం లేకుండా వాయిస్ ధృవీకరణ.</li>
              <li>ఆటోమేటిక్ గా ఎర్ర పుస్తకంలో లెడ్జర్ సింక్.</li>
              <li>నగదు వెతుక్కోకుండా క్షణాల్లో డిజిటల్ శగున్.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

  </div>

  <script>
    const DESK_EVENTS = {
      wedding: { icon: '💍', title: 'రాహుల్ & స్నిగ్ధ వివాహ వేడుక', detail: 'వధూవరులు: రాహుల్ (దాసరి) & స్నిగ్ధ (కొత్తపల్లి) • హైదరాబాద్', inflow: '₹8,42,101', exp: '₹4,15,000', sur: '+₹4,27,101', gold: '42.5 g Gold' },
      birthday: { icon: '👶', title: 'చిరంజీవి అన్విత్ ప్రథమ జన్మదినం', detail: 'కుమారుడు • అమరావతి, విజయవాడ', inflow: '₹3,18,501', exp: '₹1,20,000', sur: '+₹1,98,501', gold: '18.0 g Gold' },
      halfsaree: { icon: '🪷', title: 'కుమారి వైష్ణవి లంగాఓణీ శుభకార్యం', detail: 'అమ్మాయి పేరు: వైష్ణవి • రాజమండ్రి', inflow: '₹5,62,116', exp: '₹2,40,000', sur: '+₹3,22,116', gold: '28.5 g Gold' },
      dhoti: { icon: '🧵', title: 'చిరంజీవి సాయి ప్రణవ్ ఉపనయనం', detail: 'అబ్బాయి పేరు: సాయి ప్రణవ్ • తిరుపతి', inflow: '₹4,12,001', exp: '₹1,85,000', sur: '+₹2,27,001', gold: '12.0 g Gold' },
      housewarming: { icon: '🏡', title: 'శ్రీ నిలయం గృహప్రవేశ మహోత్సవం', detail: 'యజమానులు: రాఘవేంద్ర రావు & సుహాసిని • విశాఖపట్నం', inflow: '₹6,88,116', exp: '₹3,10,000', sur: '+₹3,78,116', gold: '24.0 g Gold' }
    };

    let DESK_LEDGER = [
      { id: 'GV-101', name: 'కొత్తపల్లి రాజశేఖర్ గారు', city: 'విజయవాడ', side: 'పెళ్ళికూతురు తరపు', type: 'నగదు', amount: 5116, precious: '-', time: '10:45 AM' },
      { id: 'GV-102', name: 'దాసరి సుబ్బారావు గారు', city: 'హైదరాబాద్', side: 'పెళ్ళికొడుకు తరపు', type: 'నగదు + బంగారం', amount: 10116, precious: '2g Gold', time: '11:02 AM' },
      { id: 'GV-103', name: 'యర్రంశెట్టి వెంకటేశ్వర్లు', city: 'గుంటూరు', side: 'స్నేహితులు', type: 'నగదు', amount: 2116, precious: '-', time: '11:18 AM' },
      { id: 'GV-104', name: 'పొట్లూరి నాగమల్లేశ్వరరావు', city: 'విశాఖపట్నం', side: 'బంధువులు', type: 'వెండి పాత్ర', amount: 1116, precious: '150g Silver', time: '11:35 AM' }
    ];

    // Cursor spotlight
    document.addEventListener('mousemove', (e) => {
      document.querySelectorAll('.spotlight-card').forEach((card) => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
        card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
      });
    });

    function showTab(tabName) {
      document.querySelectorAll('.desk-tab').forEach(b => b.classList.toggle('active', b.getAttribute('data-tab') === tabName));
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.toggle('active', p.id === `pane-${tabName}`));
    }

    function setDesktopEvent(key, btn) {
      document.querySelectorAll('.event-chip-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const ev = DESK_EVENTS[key];
      document.getElementById('desk-event-icon').innerText = ev.icon;
      document.getElementById('desk-event-title').innerText = ev.title;
      document.getElementById('desk-event-detail').innerText = ev.detail;
      document.getElementById('desk-kpi-inflow').innerText = ev.inflow;
      document.getElementById('desk-kpi-expenses').innerText = ev.exp;
      document.getElementById('desk-kpi-surplus').innerText = ev.sur;
      document.getElementById('desk-kpi-gold').innerText = ev.gold;
      playDeskChime();
    }

    function renderDeskTables() {
      const recentTbody = document.getElementById('desk-recent-tbody');
      const fullTbody = document.getElementById('desk-full-tbody');
      if (recentTbody) {
        recentTbody.innerHTML = DESK_LEDGER.map(item => `
          <tr>
            <td><strong style="color: var(--gold-light);">${item.id}</strong></td>
            <td><strong>${item.name}</strong></td>
            <td>${item.city}</td>
            <td>${item.side}</td>
            <td>${item.type}</td>
            <td style="font-family: var(--font-numbers); font-weight: 700; color: var(--gold-light);">₹${item.amount.toLocaleString('en-IN')}</td>
            <td><button class="btn-glass" onclick="alert('వాట్సాప్ రశీదు పంపబడింది!')">రశీదు</button></td>
          </tr>
        `).join('');
      }
      if (fullTbody) {
        fullTbody.innerHTML = DESK_LEDGER.map((item, idx) => `
          <tr>
            <td>${idx + 1}</td>
            <td><strong>${item.name}</strong></td>
            <td>${item.city}</td>
            <td>${item.side}</td>
            <td>${item.type}</td>
            <td style="font-family: var(--font-numbers); font-weight: 700; color: var(--gold-light);">₹${item.amount.toLocaleString('en-IN')}</td>
            <td>${item.precious}</td>
            <td style="font-size: 12px; color: var(--text-dim);">${item.time}</td>
          </tr>
        `).join('');
      }
    }

    function filterDesktopLedger(q) {
      const query = q.toLowerCase();
      const filtered = DESK_LEDGER.filter(i => i.name.toLowerCase().includes(query) || i.city.toLowerCase().includes(query));
      const fullTbody = document.getElementById('desk-full-tbody');
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
        </tr>
      `).join('');
    }

    function handleDesktopEntry(e) {
      e.preventDefault();
      const name = document.getElementById('desk-name').value;
      const city = document.getElementById('desk-city').value;
      const side = document.getElementById('desk-side').value;
      const amt = parseInt(document.getElementById('desk-amount').value) || 0;
      const grams = document.getElementById('desk-grams').value || '-';

      DESK_LEDGER.unshift({
        id: `GV-${100 + DESK_LEDGER.length + 1}`,
        name: name, city: city, side: side, type: 'నగదు', amount: amt, precious: grams, time: 'ఇప్పుడే'
      });
      renderDeskTables();
      playDeskChime();
      document.getElementById('desk-rec-name').innerText = name;
      document.getElementById('desk-rec-amt').innerText = `₹${amt.toLocaleString('en-IN')}`;
      alert(`శ్రీ ${name} గారి నుండి ₹${amt} కానుక నమోదైంది!`);
      e.target.reset();
      document.getElementById('desk-amount').value = 5116;
    }

    function handleDeskExpense(e) {
      e.preventDefault();
      const ven = document.getElementById('exp-ven').value;
      const val = parseInt(document.getElementById('exp-val').value) || 0;
      playDeskChime();
      alert(`ఖర్చు నమోదైంది: ${ven} వారికి ₹${val.toLocaleString('en-IN')}`);
      e.target.reset();
    }

    function playDeskChime() {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const o1 = ctx.createOscillator();
        const g1 = ctx.createGain();
        o1.frequency.setValueAtTime(587.33, ctx.currentTime);
        g1.gain.setValueAtTime(0.3, ctx.currentTime);
        g1.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1.2);
        o1.connect(g1); g1.connect(ctx.destination);
        o1.start(); o1.stop(ctx.currentTime + 1.2);
      } catch (e) {}
    }

    window.addEventListener('DOMContentLoaded', renderDeskTables);
  </script>
</body>
</html>
"""

# ==============================================================================
# 2. MOBILE HTML TEMPLATE (Pure 100% Full-Screen Mobile App Experience)
# ==============================================================================
MOBILE_HTML = """<!DOCTYPE html>
<html lang="te" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>GiftVault (గిఫ్ట్ వాలెట్) • Mobile App</title>
  
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@700,600,500&f[]=cabinet-grotesk@800,700,600,500,400&f[]=satoshi@700,500,400&display=swap" rel="stylesheet">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg-dark: #08090D;
      --bg-surface: #10141E;
      --bg-card: rgba(18, 22, 33, 0.95);
      
      --gold-primary: #E5B869;
      --gold-light: #FFDF88;
      --ruby-red: #E11D48;
      --emerald-green: #10B981;
      
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --text-dim: #64748B;
      
      --border-subtle: rgba(255, 255, 255, 0.08);
      
      --font-display: 'Clash Display', sans-serif;
      --font-numbers: 'Cabinet Grotesk', sans-serif;
      --font-body: 'Plus Jakarta Sans', 'Noto Sans Telugu', sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
    
    html, body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-body);
      width: 100%;
      height: 100%;
      overflow: hidden;
    }

    /* Mobile App Frame Shell (Full Screen edge-to-edge) */
    .mobile-app-shell {
      display: flex;
      flex-direction: column;
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      overflow: hidden;
      position: relative;
    }

    /* Mobile Header */
    .mobile-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 16px;
      background: rgba(16, 20, 30, 0.95);
      border-bottom: 1px solid var(--border-subtle);
      backdrop-filter: blur(20px);
      z-index: 50;
      flex-shrink: 0;
    }
    .mobile-brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .brand-icon-sm {
      width: 34px; height: 34px; border-radius: 10px;
      background: linear-gradient(135deg, #1C2333 0%, #0F131D 100%);
      border: 1px solid rgba(229, 184, 105, 0.35);
      display: flex; align-items: center; justify-content: center;
    }
    .mobile-brand-title {
      font-family: var(--font-display);
      font-size: 17px;
      font-weight: 700;
    }
    .mobile-brand-title span { color: var(--gold-light); }

    .mobile-top-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .switch-desktop-btn {
      font-size: 11px;
      background: rgba(255,255,255,0.06);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 5px 9px;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 600;
    }

    /* Mobile Content Scroll Container */
    .mobile-scroll-body {
      flex: 1;
      overflow-y: auto;
      padding: 16px 16px 100px 16px;
      -webkit-overflow-scrolling: touch;
    }

    /* Mobile Event Chip Strip */
    .mobile-event-card {
      background: linear-gradient(135deg, rgba(22, 27, 40, 0.9) 0%, rgba(14, 18, 27, 0.95) 100%);
      border: 1px solid rgba(229, 184, 105, 0.25);
      border-radius: 16px;
      padding: 16px;
      margin-bottom: 16px;
    }
    .event-pills-row {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 8px;
      margin-top: 12px;
      scrollbar-width: none;
    }
    .event-pills-row::-webkit-scrollbar { display: none; }
    .mob-pill {
      flex-shrink: 0;
      padding: 6px 12px;
      border-radius: 100px;
      font-size: 11px;
      font-weight: 600;
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      cursor: pointer;
    }
    .mob-pill.active {
      background: rgba(229, 184, 105, 0.15);
      border-color: var(--gold-primary);
      color: var(--gold-light);
    }

    /* 2x2 Mobile KPI Grid */
    .mob-kpi-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 18px;
    }
    .mob-kpi-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      padding: 14px;
    }
    .mob-kpi-label { font-size: 11px; font-weight: 600; color: var(--text-dim); margin-bottom: 4px; }
    .mob-kpi-num {
      font-family: var(--font-numbers);
      font-size: 20px;
      font-weight: 800;
      color: var(--text-main);
    }

    /* Mobile Form Controls */
    .mob-form-group { margin-bottom: 14px; }
    .mob-form-label { display: block; font-size: 12px; font-weight: 600; color: var(--text-muted); margin-bottom: 6px; }
    .mob-form-input {
      width: 100%;
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 12px 14px;
      color: var(--text-main);
      font-family: inherit;
      font-size: 14px;
      outline: none;
    }
    .mob-form-input:focus { border-color: var(--gold-primary); }

    /* Quick Preset Amount Chips */
    .mob-quick-chips {
      display: flex;
      gap: 6px;
      margin-top: 8px;
      overflow-x: auto;
    }
    .amount-chip {
      padding: 6px 12px;
      border-radius: 8px;
      background: rgba(255,255,255,0.06);
      font-size: 12px;
      font-weight: 700;
      color: var(--gold-light);
      cursor: pointer;
    }

    /* Mobile Native Shimmer Button */
    .mob-btn-primary {
      width: 100%;
      background: linear-gradient(135deg, #E5B869 0%, #C89B48 100%);
      color: #08090D;
      font-family: var(--font-body);
      font-size: 15px;
      font-weight: 700;
      padding: 14px;
      border-radius: 14px;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 15px rgba(229, 184, 105, 0.35);
    }
    .mob-btn-primary:active { transform: scale(0.98); }

    /* Mobile Card List */
    .mob-list-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 14px;
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* Floating Action Button (+) */
    .mob-fab {
      position: fixed;
      bottom: 84px;
      right: 20px;
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: linear-gradient(135deg, #FFDF88 0%, #E5B869 100%);
      color: #08090D;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 26px;
      font-weight: 700;
      box-shadow: 0 8px 25px rgba(229, 184, 105, 0.45);
      border: none;
      cursor: pointer;
      z-index: 90;
      transition: transform 0.2s ease;
    }
    .mob-fab:active { transform: scale(0.92); }

    /* Native Bottom Navigation Bar */
    .mobile-bottom-nav {
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100vw;
      background: rgba(16, 20, 30, 0.95);
      border-top: 1px solid var(--border-subtle);
      backdrop-filter: blur(24px);
      display: flex;
      justify-content: space-around;
      padding: 10px 0 16px 0;
      z-index: 100;
      flex-shrink: 0;
    }
    .mob-nav-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      background: transparent;
      border: none;
      color: var(--text-dim);
      font-family: var(--font-body);
      font-size: 11px;
      font-weight: 600;
      cursor: pointer;
      width: 20%;
    }
    .mob-nav-item.active {
      color: var(--gold-light);
    }
    .mob-nav-icon { font-size: 20px; }

    /* Mobile Screens */
    .mob-screen { display: none; }
    .mob-screen.active { display: block; animation: mobFade 0.25s ease forwards; }
    @keyframes mobFade { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }
  </style>
</head>
<body>

  <div class="mobile-app-shell">
    <!-- Top Bar -->
    <header class="mobile-top-bar">
      <div class="mobile-brand">
        <div class="brand-icon-sm">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#E5B869" stroke-width="2">
            <path d="M12 2L3 7V17L12 22L21 17V7L12 2Z"/>
            <circle cx="12" cy="12" r="3.5" stroke="#FFDF88"/>
          </svg>
        </div>
        <div class="mobile-brand-title">GIFT<span>VAULT</span></div>
      </div>

      <div class="mobile-top-actions">
        <!-- Discreet switcher to open Desktop view -->
        <a href="desktop.html" class="switch-desktop-btn">💻 Desktop</a>
        <button onclick="playMobChime()" style="background: transparent; border: none; font-size: 18px; cursor: pointer;">🔊</button>
      </div>
    </header>

    <!-- Scrollable Body -->
    <main class="mobile-scroll-body">

      <!-- SCREEN 1: DASHBOARD -->
      <section class="mob-screen active" id="mob-screen-dashboard">
        <!-- Event Card -->
        <div class="mobile-event-card">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 22px;" id="mob-ev-icon">💍</span>
              <div>
                <div style="font-weight: 700; font-size: 15px;" id="mob-ev-title">రాహుల్ & స్నిగ్ధ వివాహం</div>
                <div style="font-size: 11px; color: var(--gold-light);">హైదరాబాద్ • ప్రత్యక్షం</div>
              </div>
            </div>
            <span style="font-size: 10px; background: rgba(16,185,129,0.15); color: #10B981; padding: 2px 8px; border-radius: 100px; font-weight: 700;">LIVE</span>
          </div>

          <div class="event-pills-row">
            <button class="mob-pill active" onclick="setMobileEvent('wedding', this)">💍 పెళ్లి</button>
            <button class="mob-pill" onclick="setMobileEvent('birthday', this)">👶 బర్త్‌డే</button>
            <button class="mob-pill" onclick="setMobileEvent('halfsaree', this)">🪷 హాఫ్ శారీ</button>
            <button class="mob-pill" onclick="setMobileEvent('dhoti', this)">🧵 ఉపనయనం</button>
            <button class="mob-pill" onclick="setMobileEvent('housewarming', this)">🏡 గృహప్రవేశం</button>
          </div>
        </div>

        <!-- 2x2 Metric Grid -->
        <div class="mob-kpi-grid">
          <div class="mob-kpi-card">
            <div class="mob-kpi-label">మొత్తం కానుకలు</div>
            <div class="mob-kpi-num" style="color: var(--gold-light);" id="mob-val-inflow">₹8,42,101</div>
          </div>
          <div class="mob-kpi-card">
            <div class="mob-kpi-label">ఫంక్షన్ ఖర్చులు</div>
            <div class="mob-kpi-num" style="color: var(--ruby-red);" id="mob-val-expenses">₹4,15,000</div>
          </div>
          <div class="mob-kpi-card">
            <div class="mob-kpi-label">నికర మిగులు</div>
            <div class="mob-kpi-num" style="color: var(--emerald-green);" id="mob-val-surplus">+₹4,27,101</div>
          </div>
          <div class="mob-kpi-card">
            <div class="mob-kpi-label">బంగారం (Gold)</div>
            <div class="mob-kpi-num">42.5g</div>
          </div>
        </div>

        <!-- Recent List -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin: 16px 0 10px 0;">
          <span style="font-weight: 700; font-size: 14px;">ఇటీవలి కానుకలు</span>
          <span style="font-size: 12px; color: var(--gold-light); cursor: pointer;" onclick="navTo('ledger')">అన్నీ చూడండి</span>
        </div>

        <div id="mob-recent-list">
          <!-- Populated by JS -->
        </div>
      </section>

      <!-- SCREEN 2: FAST MUNSHI ENTRY -->
      <section class="mob-screen" id="mob-screen-desk">
        <h2 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 14px; color: var(--gold-light);">
          ⚡ మున్షీ వేగవంతమైన ఎంట్రీ
        </h2>
        
        <form onsubmit="handleMobileEntry(event)">
          <div class="mob-form-group">
            <label class="mob-form-label">అతిథి పేరు (Guest Name) *</label>
            <input type="text" id="m-name" class="mob-form-input" placeholder="ఉదా: కొత్తపల్లి రాజశేఖర్ గారు" required>
          </div>

          <div class="mob-form-group">
            <label class="mob-form-label">ఊరు / నగరం (AP & TG Autocomplete) *</label>
            <input type="text" id="m-city" class="mob-form-input" list="m-cities" placeholder="విజయవాడ, హైదరాబాద్..." required>
            <datalist id="m-cities">
              <option value="హైదరాబాద్ (Hyderabad)">
              <option value="విజయవాడ (Vijayawada)">
              <option value="విశాఖపట్నం (Visakhapatnam)">
              <option value="గుంటూరు (Guntur)">
              <option value="వరంగల్ (Warangal)">
            </datalist>
          </div>

          <div class="mob-form-group">
            <label class="mob-form-label">సంబంధం / తరపు</label>
            <select id="m-side" class="mob-form-input">
              <option value="పెళ్ళికూతురు తరపు">పెళ్ళికూతురు తరపు (Bride)</option>
              <option value="పెళ్ళికొడుకు తరపు">పెళ్ళికొడుకు తరపు (Groom)</option>
              <option value="స్నేహితులు">స్నేహితులు (Friends)</option>
              <option value="బంధువులు">బంధువులు (Relatives)</option>
            </select>
          </div>

          <div class="mob-form-group">
            <label class="mob-form-label">మొత్తం నగదు (Amount ₹) *</label>
            <input type="number" id="m-amount" class="mob-form-input" value="5116" required style="font-family: var(--font-numbers); font-size: 22px; font-weight: 800; color: var(--gold-light);">
            
            <!-- Quick Chips -->
            <div class="mob-quick-chips">
              <div class="amount-chip" onclick="document.getElementById('m-amount').value = 516">+516</div>
              <div class="amount-chip" onclick="document.getElementById('m-amount').value = 1116">+1,116</div>
              <div class="amount-chip" onclick="document.getElementById('m-amount').value = 2116">+2,116</div>
              <div class="amount-chip" onclick="document.getElementById('m-amount').value = 5116">+5,116</div>
              <div class="amount-chip" onclick="document.getElementById('m-amount').value = 11116">+11,116</div>
            </div>
          </div>

          <div class="mob-form-group">
            <label class="mob-form-label">మొబైల్ సంఖ్య (WhatsApp రశీదు కోసం)</label>
            <input type="tel" id="m-phone" class="mob-form-input" placeholder="98480xxxxx">
          </div>

          <button type="submit" class="mob-btn-primary" style="margin-top: 16px;">
            💾 భద్రపరచండి & వాట్సాప్ రశీదు
          </button>
        </form>
      </section>

      <!-- SCREEN 3: RED BOOK LEDGER -->
      <section class="mob-screen" id="mob-screen-ledger">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <h2 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; color: var(--gold-light);">
            📜 ఎర్ర పుస్తకం (Red Ledger)
          </h2>
          <span style="font-size: 12px; color: var(--emerald-green); font-weight: 700;">148 మంది</span>
        </div>

        <input type="text" class="mob-form-input" placeholder="🔍 పేరు లేదా ఊరు వెతకండి..." oninput="filterMobileLedger(this.value)" style="margin-bottom: 14px;">

        <div id="mob-full-list">
          <!-- Populated by JS -->
        </div>
      </section>

      <!-- SCREEN 4: EXPENSES -->
      <section class="mob-screen" id="mob-screen-expenses">
        <h2 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 14px; color: var(--ruby-red);">
          💸 ఈవెంట్ ఖర్చులు
        </h2>
        <div class="mob-kpi-card" style="margin-bottom: 16px; background: rgba(225,29,72,0.08); border-color: rgba(225,29,72,0.3);">
          <div class="mob-kpi-label">మొత్తం ఖర్చులు</div>
          <div class="mob-kpi-num" style="color: var(--ruby-red);">₹4,15,000</div>
          <div style="font-size: 12px; color: var(--text-muted); margin-top: 4px;">మిగులు నిల్వ: <strong style="color: var(--emerald-green);">+₹4,27,101</strong></div>
        </div>

        <form onsubmit="handleMobileExpense(event)">
          <div class="mob-form-group">
            <label class="mob-form-label">కేటగిరీ</label>
            <select id="me-cat" class="mob-form-input">
              <option>క్యాటరింగ్ & భోజనాలు</option>
              <option>కల్యాణ మండపం</option>
              <option>ఫోటోగ్రఫీ</option>
              <option>డెకరేషన్</option>
            </select>
          </div>
          <div class="mob-form-group">
            <label class="mob-form-label">వెండర్ పేరు</label>
            <input type="text" id="me-ven" class="mob-form-input" placeholder="ఉదా: శ్రీనివాస క్యాటరర్స్" required>
          </div>
          <div class="mob-form-group">
            <label class="mob-form-label">ఖర్చు మొత్తం (₹) *</label>
            <input type="number" id="me-val" class="mob-form-input" placeholder="25000" required>
          </div>
          <button type="submit" class="mob-btn-primary">+ ఖర్చు నమోదు చేయండి</button>
        </form>
      </section>

      <!-- SCREEN 5: MORE (QR Soundbox & Reciprocity) -->
      <section class="mob-screen" id="mob-screen-more">
        <h2 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 14px; color: var(--gold-light);">
          ⚙️ మరిన్ని ఫీచర్లు (More)
        </h2>

        <!-- QR Soundbox Card -->
        <div class="mob-kpi-card" style="text-align: center; margin-bottom: 14px; padding: 20px;">
          <div style="font-size: 13px; font-weight: 700; color: var(--gold-light); margin-bottom: 10px;">డిజిటల్ శగున్ UPI QR</div>
          <div style="background: #FFF; padding: 10px; border-radius: 12px; width: 150px; height: 150px; margin: 0 auto 12px auto;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=upi://pay?pa=giftvault.shagun@hdfcbank&pn=RahulSnigdha&am=5116&cu=INR" style="width: 100%; height: 100%;">
          </div>
          <div style="font-family: var(--font-numbers); font-size: 20px; font-weight: 800; color: var(--gold-light); margin-bottom: 10px;">₹5,116</div>
          <button class="mob-btn-primary" onclick="playMobChime(); alert('🔊 సౌండ్‌బాక్స్: గిఫ్ట్ వాలెట్ లో ₹5,116 అందింది!')">
            🔊 సౌండ్‌బాక్స్ వాయిస్ టెస్ట్
          </button>
        </div>

        <!-- Reciprocity intelligence card -->
        <div class="mob-kpi-card" style="margin-bottom: 14px;">
          <div style="font-size: 13px; font-weight: 700; margin-bottom: 8px;">🔄 పరస్పర శగున్ విశ్లేషణ</div>
          <div style="font-size: 12px; line-height: 1.8; color: var(--text-muted);">
            • <strong>చల్లా శ్రీనివాసరావు:</strong> వారు ఇచ్చింది ₹5,116 (మనం ఇవ్వాల్సింది: ₹5,116)<br>
            • <strong>బోళ్ల వేణుగోపాల్:</strong> వారు ఇచ్చింది ₹2,116 (మనం ఇచ్చింది: ₹5,116)
          </div>
        </div>
      </section>

    </main>

    <!-- Floating Action Button -->
    <button class="mob-fab" onclick="navTo('desk')">+</button>

    <!-- Mobile Native Bottom Navigation -->
    <nav class="mobile-bottom-nav">
      <button class="mob-nav-item active" data-nav="dashboard" onclick="navTo('dashboard')">
        <span class="mob-nav-icon">📊</span>
        <span>డాష్‌బోర్డ్</span>
      </button>
      <button class="mob-nav-item" data-nav="desk" onclick="navTo('desk')">
        <span class="mob-nav-icon">⚡</span>
        <span>మున్షీ</span>
      </button>
      <button class="mob-nav-item" data-nav="ledger" onclick="navTo('ledger')">
        <span class="mob-nav-icon">📜</span>
        <span>లెడ్జర్</span>
      </button>
      <button class="mob-nav-item" data-nav="expenses" onclick="navTo('expenses')">
        <span class="mob-nav-icon">💸</span>
        <span>ఖర్చులు</span>
      </button>
      <button class="mob-nav-item" data-nav="more" onclick="navTo('more')">
        <span class="mob-nav-icon">⚙️</span>
        <span>మరిన్ని</span>
      </button>
    </nav>
  </div>

  <script>
    let MOB_DATA = [
      { id: 'GV-101', name: 'కొత్తపల్లి రాజశేఖర్ గారు', city: 'విజయవాడ', side: 'పెళ్ళికూతురు తరపు', amount: 5116, time: '10:45 AM' },
      { id: 'GV-102', name: 'దాసరి సుబ్బారావు గారు', city: 'హైదరాబాద్', side: 'పెళ్ళికొడుకు తరపు', amount: 10116, time: '11:02 AM' },
      { id: 'GV-103', name: 'యర్రంశెట్టి వెంకటేశ్వర్లు', city: 'గుంటూరు', side: 'స్నేహితులు', amount: 2116, time: '11:18 AM' },
      { id: 'GV-104', name: 'పొట్లూరి నాగమల్లేశ్వరరావు', city: 'విశాఖపట్నం', side: 'బంధువులు', amount: 1116, time: '11:35 AM' }
    ];

    function navTo(screenId) {
      document.querySelectorAll('.mob-nav-item').forEach(b => b.classList.toggle('active', b.getAttribute('data-nav') === screenId));
      document.querySelectorAll('.mob-screen').forEach(s => s.classList.toggle('active', s.id === `mob-screen-${screenId}`));
    }

    function setMobileEvent(key, btn) {
      document.querySelectorAll('.mob-pill').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      playMobChime();
    }

    function renderMobileLists() {
      const recentBox = document.getElementById('mob-recent-list');
      const fullBox = document.getElementById('mob-full-list');

      if (recentBox) {
        recentBox.innerHTML = MOB_DATA.slice(0, 3).map(item => `
          <div class="mob-list-card">
            <div>
              <div style="font-weight: 700; font-size: 14px;">${item.name}</div>
              <div style="font-size: 11px; color: var(--text-muted);">${item.city} • ${item.side}</div>
            </div>
            <div style="text-align: right;">
              <div style="font-family: var(--font-numbers); font-weight: 800; font-size: 16px; color: var(--gold-light);">₹${item.amount.toLocaleString('en-IN')}</div>
              <div style="font-size: 10px; color: var(--text-dim);">${item.time}</div>
            </div>
          </div>
        `).join('');
      }

      if (fullBox) {
        fullBox.innerHTML = MOB_DATA.map(item => `
          <div class="mob-list-card">
            <div>
              <div style="font-weight: 700; font-size: 14px;">${item.name}</div>
              <div style="font-size: 11px; color: var(--text-muted);">${item.city} • ${item.side}</div>
            </div>
            <div style="text-align: right;">
              <div style="font-family: var(--font-numbers); font-weight: 800; font-size: 16px; color: var(--gold-light);">₹${item.amount.toLocaleString('en-IN')}</div>
              <div style="font-size: 10px; color: var(--gold-light); cursor: pointer;" onclick="alert('వాట్సాప్ రశీదు పంపబడింది!')">రశీదు 📲</div>
            </div>
          </div>
        `).join('');
      }
    }

    function filterMobileLedger(q) {
      const query = q.toLowerCase();
      const filtered = MOB_DATA.filter(i => i.name.toLowerCase().includes(query) || i.city.toLowerCase().includes(query));
      const fullBox = document.getElementById('mob-full-list');
      fullBox.innerHTML = filtered.map(item => `
        <div class="mob-list-card">
          <div>
            <div style="font-weight: 700; font-size: 14px;">${item.name}</div>
            <div style="font-size: 11px; color: var(--text-muted);">${item.city} • ${item.side}</div>
          </div>
          <div style="text-align: right;">
            <div style="font-family: var(--font-numbers); font-weight: 800; font-size: 16px; color: var(--gold-light);">₹${item.amount.toLocaleString('en-IN')}</div>
          </div>
        </div>
      `).join('');
    }

    function handleMobileEntry(e) {
      e.preventDefault();
      const name = document.getElementById('m-name').value;
      const city = document.getElementById('m-city').value;
      const side = document.getElementById('m-side').value;
      const amt = parseInt(document.getElementById('m-amount').value) || 0;

      MOB_DATA.unshift({
        id: `GV-${100 + MOB_DATA.length + 1}`,
        name: name, city: city, side: side, amount: amt, time: 'ఇప్పుడే'
      });
      renderMobileLists();
      playMobChime();
      alert(`శ్రీ ${name} గారి నుండి ₹${amt} కానుక నమోదైంది! వాట్సాప్ రశీదు పంపబడింది.`);
      e.target.reset();
      document.getElementById('m-amount').value = 5116;
      navTo('dashboard');
    }

    function handleMobileExpense(e) {
      e.preventDefault();
      const ven = document.getElementById('me-ven').value;
      const val = parseInt(document.getElementById('me-val').value) || 0;
      playMobChime();
      alert(`ఖర్చు నమోదైంది: ${ven} వారికి ₹${val}`);
      e.target.reset();
      navTo('dashboard');
    }

    function playMobChime() {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.frequency.setValueAtTime(587.33, ctx.currentTime);
        g.gain.setValueAtTime(0.3, ctx.currentTime);
        g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 1);
        o.connect(g); g.connect(ctx.destination);
        o.start(); o.stop(ctx.currentTime + 1);
      } catch (e) {}
    }

    window.addEventListener('DOMContentLoaded', renderMobileLists);
  </script>
</body>
</html>
"""

# ==============================================================================
# 3. SMART ROUTER INDEX.HTML (Auto-Detect Device & Direct Links)
# ==============================================================================
INDEX_ROUTER_HTML = """<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault (గిఫ్ట్ వాలెట్) • Smart Router</title>
  <style>
    body {
      background: #08090D;
      color: #F8FAFC;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      margin: 0;
      text-align: center;
    }
    .spinner {
      width: 44px;
      height: 44px;
      border: 3px solid rgba(229, 184, 105, 0.2);
      border-top-color: #E5B869;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
      margin-bottom: 20px;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
    .choice-box {
      margin-top: 30px;
      display: flex;
      gap: 16px;
    }
    .choice-btn {
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      color: #FFF;
      text-decoration: none;
      padding: 12px 24px;
      border-radius: 12px;
      font-weight: 600;
      font-size: 14px;
      transition: all 0.2s ease;
    }
    .choice-btn:hover {
      background: rgba(229,184,105,0.2);
      border-color: #E5B869;
      color: #FFDF88;
    }
  </style>
  <script>
    // Smart Device Detection
    const params = new URLSearchParams(window.location.search);
    const forced = params.get('mode');
    const isMobileDevice = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) || window.innerWidth < 768;

    if (forced === 'desktop') {
      window.location.replace('desktop.html');
    } else if (forced === 'mobile') {
      window.location.replace('mobile.html');
    } else {
      if (isMobileDevice) {
        window.location.replace('mobile.html');
      } else {
        window.location.replace('desktop.html');
      }
    }
  </script>
</head>
<body>
  <div class="spinner"></div>
  <div style="font-size: 18px; font-weight: 700; color: #E5B869;">GiftVault (గిఫ్ట్ వాలెట్)</div>
  <div style="font-size: 13px; color: #94A3B8; margin-top: 6px;">మీ డివైస్ ని గుర్తించి తగిన వెర్షన్ ఓపెన్ అవుతోంది...</div>

  <div class="choice-box">
    <a href="desktop.html" class="choice-btn">💻 Desktop వెర్షన్</a>
    <a href="mobile.html" class="choice-btn">📱 Mobile వెర్షన్</a>
  </div>
</body>
</html>
"""

def main():
    os.makedirs(PREVIEW_DIR, exist_ok=True)
    os.makedirs(WEB_DIR, exist_ok=True)

    # 1. Desktop version
    desk_path = os.path.join(PREVIEW_DIR, "desktop.html")
    with open(desk_path, "w", encoding="utf-8") as f:
        f.write(DESKTOP_HTML)
    print(f"Created {desk_path}")

    # 2. Mobile version
    mob_path = os.path.join(PREVIEW_DIR, "mobile.html")
    with open(mob_path, "w", encoding="utf-8") as f:
        f.write(MOBILE_HTML)
    print(f"Created {mob_path}")

    # 3. Router index.html
    router_path = os.path.join(PREVIEW_DIR, "index.html")
    with open(router_path, "w", encoding="utf-8") as f:
        f.write(INDEX_ROUTER_HTML)
    print(f"Created {router_path}")

    # Sync to web directory
    shutil.copy(desk_path, os.path.join(WEB_DIR, "desktop.html"))
    shutil.copy(mob_path, os.path.join(WEB_DIR, "mobile.html"))
    shutil.copy(router_path, os.path.join(WEB_DIR, "index.html"))

    print("ALL VERSIONS GENERATED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
