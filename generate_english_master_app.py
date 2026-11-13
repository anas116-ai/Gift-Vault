# -*- coding: utf-8 -*-
"""
Generate the Grand, English-Only, Modern Animated Celebration Ledger App:
- 100% English (clean, zero spelling mistakes, no broken mixed languages).
- 5 Harmonious Designer Palette Colors:
  1. Base Ivory Alabaster: #FDFBF7 / #FFFFFF (Background & Cards)
  2. Deep Slate Charcoal: #0F172A / #334155 (Crisp High-Contrast Typography & Nav)
  3. Auspicious Crimson Red: #E11D48 / #BE123C (Primary Brand Accent & Buttons)
  4. Royal Indigo Sapphire: #4338CA / #3730A3 (Modern Fintech Secondary)
  5. Emerald Prosperity: #059669 / #047857 (Net Surplus & Positive Ledger)
- Fluid Framer-like micro-interactions, smooth hover elevations, card shine, and modal transitions.
- "Create New Event" Modal with Pre-populated Celebration Types:
  - Wedding (Nikah / Vivaha)
  - Birthday & Barasala
  - First Haircut / Tonsure (Mundan / Odugu / Khatna)
  - Half Saree / Puberty Ceremony (Pushpalankarana / Langa Voni)
  - Dhoti Ceremony / Panchala Function (Pancha Pandaga / Upanayanam)
  - Housewarming (Griha Pravesh)
  - Custom Event (User can enter any custom event name, date, venue, host pair)
- Realistic high-resolution celebration imagery embedded with interactive switcher.
- Seamless flow: Landing Page -> Dedicated Login Screen -> Full In-App Workspace (Dashboard, Create Event, Munshi Fast Entry Desk, Red Ledger, Expenses vs Surplus, Reciprocity, Soundbox QR, Settings).
"""

APP_HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>GiftVault • The Modern Digital Red Notebook for Celebrations</title>
  
  <!-- Premium Fonts: Plus Jakarta Sans & Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <style>
    /* ============================================================
       5-COLOR DESIGNER PALETTE (NO GOLD, NO AI SLOP)
       Color 1: #FDFBF7 (Base Warm Alabaster) & #FFFFFF (Card Surface)
       Color 2: #0F172A (Deep Slate Charcoal Typography)
       Color 3: #E11D48 (Auspicious Crimson Red Accent & Primary CTAs)
       Color 4: #4338CA (Royal Indigo Sapphire Highlights)
       Color 5: #059669 (Emerald Prosperity & Surplus Green)
       ============================================================ */
    :root {
      --c-base: #FDFBF7;
      --c-surface: #FFFFFF;
      --c-surface-soft: #F8FAFC;
      --c-slate-dark: #0F172A;
      --c-slate-body: #334155;
      --c-slate-muted: #64748B;
      --c-slate-border: #E2E8F0;
      --c-crimson: #E11D48;
      --c-crimson-dark: #BE123C;
      --c-crimson-soft: #FFF1F2;
      --c-crimson-border: #FFE4E6;
      --c-indigo: #4338CA;
      --c-indigo-soft: #EEF2FF;
      --c-emerald: #059669;
      --c-emerald-soft: #ECFDF5;

      --font-heading: 'Plus Jakarta Sans', -apple-system, sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;

      --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.06);
      --shadow-md: 0 4px 12px -2px rgba(15, 23, 42, 0.08), 0 2px 4px -2px rgba(15, 23, 42, 0.04);
      --shadow-lg: 0 12px 24px -4px rgba(15, 23, 42, 0.08), 0 4px 8px -2px rgba(15, 23, 42, 0.04);
      --shadow-xl: 0 20px 32px -6px rgba(15, 23, 42, 0.12), 0 8px 16px -4px rgba(15, 23, 42, 0.06);
      --shadow-crimson: 0 10px 24px -4px rgba(225, 29, 72, 0.32);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    body {
      background-color: var(--c-base);
      color: var(--c-slate-body);
      font-family: var(--font-body);
      line-height: 1.5;
      overflow-x: hidden;
    }

    h1, h2, h3, h4, .brand-title {
      font-family: var(--font-heading);
    }

    /* Ambient Subtle Background Blobs */
    .ambient-glow-1 {
      position: absolute;
      top: 0;
      right: 0;
      width: 520px;
      height: 520px;
      background: radial-gradient(circle, rgba(225, 29, 72, 0.05) 0%, rgba(253, 251, 247, 0) 70%);
      pointer-events: none;
      z-index: 0;
    }
    .ambient-glow-2 {
      position: absolute;
      top: 500px;
      left: 0;
      width: 480px;
      height: 480px;
      background: radial-gradient(circle, rgba(67, 56, 202, 0.04) 0%, rgba(253, 251, 247, 0) 70%);
      pointer-events: none;
      z-index: 0;
    }

    /* ============================================================
       TOP STICKY NAVBAR
       ============================================================ */
    .site-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--c-slate-border);
      transition: all 0.2s ease;
    }
    .nav-inner {
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
    .brand-symbol {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--c-crimson), var(--c-crimson-dark));
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(225, 29, 72, 0.28);
    }
    .brand-title {
      font-size: 21px;
      font-weight: 800;
      color: var(--c-slate-dark);
      letter-spacing: -0.03em;
    }
    .brand-title span {
      color: var(--c-crimson);
    }

    .nav-links-box {
      display: flex;
      align-items: center;
      gap: 28px;
    }
    @media (max-width: 900px) {
      .nav-links-box { display: none; }
    }
    .nav-btn {
      background: none;
      border: none;
      font-size: 14.5px;
      font-weight: 600;
      color: var(--c-slate-body);
      cursor: pointer;
      padding: 6px 0;
      transition: color 0.15s ease;
    }
    .nav-btn:hover {
      color: var(--c-crimson);
    }

    /* Buttons */
    .btn-crimson {
      background: var(--c-crimson);
      color: #FFFFFF;
      font-size: 14px;
      font-weight: 700;
      padding: 10px 22px;
      border-radius: 9999px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: var(--shadow-crimson);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-crimson:hover {
      background: var(--c-crimson-dark);
      transform: translateY(-1.5px);
      box-shadow: 0 12px 28px -4px rgba(225, 29, 72, 0.4);
    }
    .btn-crimson:active {
      transform: translateY(0);
    }

    .btn-outline {
      background: #FFFFFF;
      color: var(--c-slate-dark);
      font-size: 14px;
      font-weight: 600;
      padding: 9px 20px;
      border-radius: 9999px;
      border: 1.5px solid var(--c-slate-border);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.15s ease;
    }
    .btn-outline:hover {
      border-color: var(--c-slate-dark);
      background: var(--c-surface-soft);
    }

    /* Master Views */
    .view-container {
      display: none;
      position: relative;
      z-index: 1;
    }
    .view-container.active {
      display: block;
      animation: fadeInView 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes fadeInView {
      from { opacity: 0; transform: translateY(8px); }
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
      background: var(--c-crimson-soft);
      border: 1px solid var(--c-crimson-border);
      color: var(--c-crimson);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.04em;
      margin-bottom: 20px;
    }
    .pill-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--c-crimson);
      box-shadow: 0 0 8px rgba(225, 29, 72, 0.6);
    }

    .hero-h1 {
      font-size: 50px;
      font-weight: 800;
      line-height: 1.14;
      letter-spacing: -0.03em;
      color: var(--c-slate-dark);
      margin-bottom: 18px;
    }
    @media (max-width: 640px) {
      .hero-h1 { font-size: 36px; }
    }
    .hero-h1 span {
      color: var(--c-crimson);
    }

    .hero-desc {
      font-size: 17px;
      line-height: 1.65;
      color: var(--c-slate-body);
      margin-bottom: 30px;
      max-width: 580px;
    }

    /* Celebration Category Switcher in Hero */
    .category-chips {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 8px;
      margin-bottom: 28px;
    }
    .cat-chip {
      padding: 8px 16px;
      border-radius: 9999px;
      border: 1.5px solid var(--c-slate-border);
      background: #FFFFFF;
      font-size: 13px;
      font-weight: 600;
      color: var(--c-slate-body);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
    }
    .cat-chip.active {
      background: var(--c-crimson);
      border-color: var(--c-crimson);
      color: #FFFFFF;
    }

    /* Interactive Live Celebration Card with Realistic Imagery */
    .hero-showcase-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 28px;
      overflow: hidden;
      box-shadow: var(--shadow-xl);
      transition: transform 0.3s ease;
    }
    .hero-showcase-card:hover {
      transform: translateY(-3px);
    }
    .showcase-img-box {
      position: relative;
      width: 100%;
      height: 200px;
      overflow: hidden;
    }
    .showcase-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }
    .hero-showcase-card:hover .showcase-img {
      transform: scale(1.04);
    }
    .showcase-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(15, 23, 42, 0.1) 0%, rgba(15, 23, 42, 0.7) 100%);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 20px;
      color: #FFFFFF;
    }
    .showcase-event-title {
      font-size: 18px;
      font-weight: 800;
    }
    .showcase-event-venue {
      font-size: 12.5px;
      opacity: 0.9;
    }

    .showcase-body {
      padding: 24px;
    }
    .metric-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 20px;
    }
    .metric-cell {
      background: var(--c-surface-soft);
      border: 1px solid var(--c-slate-border);
      border-radius: 14px;
      padding: 12px 14px;
    }
    .metric-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--c-slate-muted);
      margin-bottom: 4px;
    }
    .metric-val {
      font-size: 20px;
      font-weight: 800;
      color: var(--c-slate-dark);
    }

    .live-feed-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 14px;
      border: 1px solid var(--c-slate-border);
      border-radius: 12px;
      background: #FFFFFF;
      margin-bottom: 8px;
      box-shadow: var(--shadow-sm);
    }

    /* ============================================================
       FOUNDATION CARDS & BENTO FEATURES
       ============================================================ */
    .section-wrap {
      max-width: 1240px;
      margin: 0 auto;
      padding: 72px 24px;
    }
    .section-center-head {
      text-align: center;
      max-width: 720px;
      margin: 0 auto 52px auto;
    }
    .sec-tag {
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--c-crimson);
      margin-bottom: 8px;
    }
    .sec-h2 {
      font-size: 36px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--c-slate-dark);
      margin-bottom: 12px;
    }
    .sec-desc {
      font-size: 16px;
      color: var(--c-slate-body);
      line-height: 1.6;
    }

    /* 3 Foundations */
    .foundations-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-bottom: 64px;
    }
    @media (max-width: 900px) {
      .foundations-grid { grid-template-columns: 1fr; }
    }
    .foundation-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 24px;
      padding: 32px 28px;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
    }
    .foundation-card:hover {
      box-shadow: var(--shadow-lg);
      transform: translateY(-3px);
      border-color: #CBD5E1;
    }
    .foundation-icon {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      margin-bottom: 20px;
    }

    /* 6 Bento Grid Feature Cards */
    .bento-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    @media (max-width: 960px) {
      .bento-grid { grid-template-columns: 1fr; }
    }
    .bento-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 24px;
      padding: 32px 28px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
    }
    .bento-card:hover {
      box-shadow: var(--shadow-md);
      transform: translateY(-3px);
      border-color: #CBD5E1;
    }
    .bento-tag {
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--c-crimson);
      margin-bottom: 8px;
    }
    .bento-title {
      font-size: 19px;
      font-weight: 800;
      color: var(--c-slate-dark);
      margin-bottom: 8px;
    }
    .bento-desc {
      font-size: 14px;
      color: var(--c-slate-body);
      line-height: 1.6;
    }

    /* ============================================================
       CELEBRATIONS SHOWCASE (WITH DETAILED CARDS & REAL IMAGES)
       ============================================================ */
    .celebrations-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    @media (max-width: 960px) {
      .celebrations-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .celebrations-grid { grid-template-columns: 1fr; }
    }
    .celebration-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 22px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
    }
    .celebration-card:hover {
      box-shadow: var(--shadow-md);
      transform: translateY(-3px);
      border-color: #CBD5E1;
    }
    .cel-img {
      width: 100%;
      height: 160px;
      object-fit: cover;
    }
    .cel-content {
      padding: 20px;
    }
    .cel-h3 {
      font-size: 17px;
      font-weight: 800;
      color: var(--c-slate-dark);
      margin-bottom: 6px;
    }
    .cel-p {
      font-size: 13.5px;
      color: var(--c-slate-muted);
      line-height: 1.5;
    }

    /* ============================================================
       MODAL: CREATE NEW EVENT (COMPREHENSIVE MULTI-EVENT CREATOR)
       ============================================================ */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.6);
      backdrop-filter: blur(8px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 28px;
      max-width: 580px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 32px;
      box-shadow: var(--shadow-xl);
      animation: modalPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes modalPop {
      from { opacity: 0; transform: scale(0.96) translateY(10px); }
      to { opacity: 1; transform: scale(1) translateY(0); }
    }

    .form-group {
      margin-bottom: 18px;
    }
    .form-label {
      display: block;
      font-size: 13px;
      font-weight: 700;
      color: var(--c-slate-dark);
      margin-bottom: 6px;
    }
    .form-input {
      width: 100%;
      padding: 12px 14px;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 12px;
      font-size: 14px;
      font-family: inherit;
      color: var(--c-slate-dark);
      background: #FFFFFF;
      transition: all 0.15s ease;
    }
    .form-input:focus {
      outline: none;
      border-color: var(--c-crimson);
      box-shadow: 0 0 0 3px rgba(225, 29, 72, 0.12);
    }

    /* ============================================================
       DEDICATED FULL-PAGE SIGN-IN (VIEW 2)
       ============================================================ */
    .login-container {
      max-width: 960px;
      margin: 48px auto;
      padding: 0 24px;
    }
    .login-split-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 28px;
      overflow: hidden;
      box-shadow: var(--shadow-xl);
      display: grid;
      grid-template-columns: 1fr 1fr;
    }
    @media (max-width: 768px) {
      .login-split-card { grid-template-columns: 1fr; }
      .login-banner-side { display: none; }
    }
    .login-banner-side {
      background: linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%);
      border-right: 1.5px solid var(--c-slate-border);
      padding: 48px 36px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .login-form-side {
      padding: 48px 36px;
    }

    .role-pills {
      display: flex;
      gap: 8px;
      margin-bottom: 18px;
    }
    .role-pill {
      flex: 1;
      text-align: center;
      padding: 10px 8px;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 12px;
      background: #FFFFFF;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .role-pill.active {
      border-color: var(--c-crimson);
      background: var(--c-crimson-soft);
      color: var(--c-crimson);
      font-weight: 700;
    }

    /* ============================================================
       IN-APP COMPLETE WORKSPACE (VIEW 3)
       ============================================================ */
    .app-workspace {
      max-width: 1280px;
      margin: 0 auto;
      padding: 28px 24px;
    }
    .app-top-header {
      background: #FFFFFF;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 20px;
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }

    .tab-nav-bar {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 6px;
      margin-bottom: 24px;
      border-bottom: 1.5px solid var(--c-slate-border);
    }
    .tab-nav-btn {
      padding: 10px 18px;
      border: none;
      background: none;
      font-size: 14px;
      font-weight: 600;
      color: var(--c-slate-muted);
      cursor: pointer;
      border-bottom: 2.5px solid transparent;
      margin-bottom: -1.5px;
      white-space: nowrap;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .tab-nav-btn.active {
      color: var(--c-crimson);
      border-bottom-color: var(--c-crimson);
      font-weight: 700;
    }

    .app-screen {
      display: none;
    }
    .app-screen.active {
      display: block;
      animation: fadeInView 0.2s ease;
    }

    /* Munshi Desk Quick Coins */
    .coin-group {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 10px 0 18px 0;
    }
    .coin-chip {
      padding: 6px 14px;
      border-radius: 9999px;
      border: 1.5px solid var(--c-crimson-border);
      background: var(--c-crimson-soft);
      color: var(--c-crimson);
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .coin-chip:hover {
      background: var(--c-crimson);
      color: #FFFFFF;
    }

    /* Data Table */
    .table-container {
      background: #FFFFFF;
      border: 1.5px solid var(--c-slate-border);
      border-radius: 20px;
      overflow-x: auto;
      box-shadow: var(--shadow-sm);
    }
    .data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .data-table th, .data-table td {
      padding: 14px 18px;
      border-bottom: 1px solid var(--c-slate-border);
      font-size: 13.5px;
    }
    .data-table th {
      background: var(--c-surface-soft);
      font-weight: 700;
      color: var(--c-slate-dark);
      font-size: 11.5px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Toast */
    .toast-box {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--c-slate-dark);
      color: #FFFFFF;
      padding: 12px 22px;
      border-radius: 12px;
      font-size: 14px;
      font-weight: 600;
      box-shadow: var(--shadow-xl);
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

  <div class="ambient-glow-1"></div>
  <div class="ambient-glow-2"></div>

  <!-- ============================================================
       TOP STICKY NAVBAR
       ============================================================ -->
  <header class="site-nav">
    <div class="nav-inner">
      <div class="brand-group" onclick="showView('landing')">
        <div class="brand-symbol">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
          </svg>
        </div>
        <div class="brand-title">Gift<span>Vault</span></div>
      </div>

      <nav class="nav-links-box">
        <button type="button" class="nav-btn" onclick="showView('landing')">Home</button>
        <button type="button" class="nav-btn" onclick="scrollToId('features-section')">Features</button>
        <button type="button" class="nav-btn" onclick="scrollToId('celebrations-section')">Celebrations</button>
        <button type="button" class="nav-btn" onclick="scrollToId('compare-section')">Comparison</button>
        <button type="button" class="nav-btn" onclick="scrollToId('faq-section')">FAQ</button>
      </nav>

      <div style="display: flex; gap: 10px; align-items: center;">
        <button type="button" class="btn-outline" onclick="openCreateEventModal()">
          + Create Event
        </button>
        <button type="button" class="btn-outline" onclick="showView('login')">
          Sign In
        </button>
        <button type="button" class="btn-crimson" onclick="showView('app'); openTab('desk');">
          Launch Vault →
        </button>
      </div>
    </div>
  </header>

  <!-- ============================================================
       VIEW 1: LUXURY GRAND LANDING PAGE
       ============================================================ -->
  <main id="view-landing" class="view-container active">
    
    <!-- Hero Section -->
    <section class="hero-wrap">
      <div class="hero-grid">
        <div>
          <div class="pill-badge">
            <span class="pill-dot"></span>
            <span>2026 EDITION • 100% SECURE DIGITAL RED BOOK</span>
          </div>

          <h1 class="hero-h1">
            The Digital Ledger for Every Family <span>Celebration</span>.
          </h1>

          <p class="hero-desc">
            Organize weddings, barasala birthdays, tonsure mundan ceremonies, puberty celebrations, and housewarmings. Record cash, gold, and UPI blessings with instant receipts and complete reciprocity analytics.
          </p>

          <!-- Interactive Celebration Chips -->
          <div class="category-chips">
            <button type="button" class="cat-chip active" onclick="switchHeroCelebration('wedding', this)">💍 Wedding</button>
            <button type="button" class="cat-chip" onclick="switchHeroCelebration('birthday', this)">👶 Barasala / Birthday</button>
            <button type="button" class="cat-chip" onclick="switchHeroCelebration('tonsure', this)">✂️ Tonsure (Mundan / Khatna)</button>
            <button type="button" class="cat-chip" onclick="switchHeroCelebration('puberty', this)">🪷 Half Saree / Puberty</button>
            <button type="button" class="cat-chip" onclick="switchHeroCelebration('dhoti', this)">🧵 Dhoti / Upanayanam</button>
            <button type="button" class="cat-chip" onclick="switchHeroCelebration('housewarming', this)">🏡 Housewarming</button>
          </div>

          <div style="display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 28px;">
            <button type="button" class="btn-crimson" style="padding: 13px 28px; font-size: 15px;" onclick="showView('app'); openTab('desk');">
              ⚡ Open Munshi Desk (Fast Entry)
            </button>
            <button type="button" class="btn-outline" style="padding: 13px 24px; font-size: 15px;" onclick="openCreateEventModal()">
              + Create New Event
            </button>
          </div>

          <div style="font-size: 13.5px; color: var(--c-slate-muted); display: flex; align-items: center; gap: 8px;">
            <span>🌍</span>
            <span>Trusted by thousands of South Asian families worldwide • Free for personal use</span>
          </div>
        </div>

        <!-- Realistic Interactive Showcase Card -->
        <div class="hero-showcase-card">
          <div class="showcase-img-box">
            <img id="hero-img-src" src="https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=800&q=80" alt="Celebration" class="showcase-img">
            <div class="showcase-overlay">
              <div class="showcase-event-title" id="hero-card-title">Rahul & Snigdha Wedding Celebration</div>
              <div class="showcase-event-venue" id="hero-card-venue">Gachibowli, Hyderabad • Live Shagun Vault</div>
            </div>
          </div>

          <div class="showcase-body">
            <div class="metric-grid">
              <div class="metric-cell">
                <div class="metric-label">Total Blessings</div>
                <div class="metric-val" id="hero-val-inflow" style="color: var(--c-crimson);">₹8,42,116</div>
              </div>
              <div class="metric-cell">
                <div class="metric-label">Event Expenses</div>
                <div class="metric-val" id="hero-val-expenses" style="color: var(--c-slate-dark);">₹4,15,000</div>
              </div>
              <div class="metric-cell">
                <div class="metric-label">Net Surplus</div>
                <div class="metric-val" id="hero-val-surplus" style="color: var(--c-emerald);">+₹4,27,116</div>
              </div>
              <div class="metric-cell">
                <div class="metric-label">Gold & Silver</div>
                <div class="metric-val" id="hero-val-jewels">42.5g / 550g</div>
              </div>
            </div>

            <div style="font-size: 11.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--c-slate-muted); margin-bottom: 8px;">
              Live Reception Desk Feed
            </div>
            <div class="live-feed-item">
              <div>
                <div style="font-weight: 700; font-size: 13.5px; color: var(--c-slate-dark);">Venkat Rao Garu</div>
                <div style="font-size: 11px; color: var(--c-slate-muted);">Vijayawada • Relatives</div>
              </div>
              <div style="font-weight: 800; font-size: 15px; color: var(--c-crimson);">+ ₹10,116</div>
            </div>
            <div class="live-feed-item">
              <div>
                <div style="font-weight: 700; font-size: 13.5px; color: var(--c-slate-dark);">Syed Mansoor Ali</div>
                <div style="font-size: 11px; color: var(--c-slate-muted);">Hyderabad • Close Friend</div>
              </div>
              <div style="font-weight: 800; font-size: 15px; color: var(--c-crimson);">+ ₹5,116</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Secure Foundations Section -->
    <section class="section-wrap" style="background: #FFFFFF; border-top: 1px solid var(--c-slate-border);">
      <div class="section-center-head">
        <div class="sec-tag">BUILT ON INTEGRITY</div>
        <h2 class="sec-h2">Secure Foundations for Modern Traditions</h2>
        <p class="sec-desc">We combine centuries-old cultural customs with world-class fintech encryption so your family records remain protected forever.</p>
      </div>

      <div class="foundations-grid">
        <div class="foundation-card">
          <div class="foundation-icon" style="background: var(--c-crimson-soft); color: var(--c-crimson);">🔒</div>
          <h3 style="font-size: 19px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 10px;">Secure & Private</h3>
          <p style="font-size: 14px; color: var(--c-slate-body); line-height: 1.6;">
            Your data is encrypted end-to-end and stored safely. Accessible strictly by your authorized family members.
          </p>
        </div>

        <div class="foundation-card">
          <div class="foundation-icon" style="background: var(--c-indigo-soft); color: var(--c-indigo);">🏛️</div>
          <h3 style="font-size: 19px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 10px;">Every Community & Tradition</h3>
          <p style="font-size: 14px; color: var(--c-slate-body); line-height: 1.6;">
            Whether it is an Indian wedding, Barasala, Khatna tonsure, Pushpalankarana ceremony, or Upanayanam.
          </p>
        </div>

        <div class="foundation-card">
          <div class="foundation-icon" style="background: var(--c-emerald-soft); color: var(--c-emerald);">📑</div>
          <h3 style="font-size: 19px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 10px;">Instant CSV & PDF Export</h3>
          <p style="font-size: 14px; color: var(--c-slate-body); line-height: 1.6;">
            Download complete Excel sheets or print physical summaries at the click of a button to settle accounts effortlessly.
          </p>
        </div>
      </div>
    </section>

    <!-- Bento Features Section -->
    <section id="features-section" class="section-wrap">
      <div class="section-center-head">
        <div class="sec-tag">SUPERPOWERS FOR YOUR EVENT</div>
        <h2 class="sec-h2">Designed for the Busy Reception Desk</h2>
        <p class="sec-desc">Replace messy paper notes and rushed scribbles with an intuitive digital ledger that never loses a single rupee.</p>
      </div>

      <div class="bento-grid">
        <div class="bento-card">
          <div>
            <div class="bento-tag">SPEED OPTIMIZED</div>
            <h3 class="bento-title">⚡ 3-Second Munshi Desk</h3>
            <p class="bento-desc">Designed specifically for long queues. Type guest names, pick cities, choose Cash, Gold, or UPI, and auto-round with +₹1 lucky coins.</p>
          </div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-tag">RECIPROCITY TRACKER</div>
            <h3 class="bento-title">🔄 Smart Gift History</h3>
            <p class="bento-desc">"How much did they give us last time? How much should we give them back?" Instant relationship history and return gift recommendations.</p>
          </div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-tag">COMPLETE TRANSPARENCY</div>
            <h3 class="bento-title">📖 Digital Red Notebook</h3>
            <p class="bento-desc">The modern version of traditional Erra Pusthakam / Shagun Diary. Search by city, guest name, or amount with zero calculation errors.</p>
          </div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-tag">GUEST COURTESY</div>
            <h3 class="bento-title">📲 Instant WhatsApp Receipts</h3>
            <p class="bento-desc">Automatically generate a respectful, personalized digital acknowledgement sent directly to the guest’s WhatsApp number.</p>
          </div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-tag">SOUND NOTIFICATIONS</div>
            <h3 class="bento-title">🔔 Dynamic UPI Soundbox</h3>
            <p class="bento-desc">Display a personalized UPI QR code on the counter. The moment guests scan and pay, a pleasant chime announces the verified amount.</p>
          </div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-tag">FINANCIAL AUDIT</div>
            <h3 class="bento-title">💸 Expenses vs Net Savings</h3>
            <p class="bento-desc">Log hall rental, catering, floral decor, and photography expenses. Compare total collections against total costs in real-time.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Celebrations We Support Section with Photos -->
    <section id="celebrations-section" class="section-wrap" style="background: #FFFFFF; border-top: 1px solid var(--c-slate-border);">
      <div class="section-center-head">
        <div class="sec-tag">VERSATILE LEDGER</div>
        <h2 class="sec-h2">Celebrations We Support</h2>
        <p class="sec-desc">Every auspicious milestone in your family is covered with dedicated templates and tracking.</p>
      </div>

      <div class="celebrations-grid">
        <div class="celebration-card">
          <img src="https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80" alt="Wedding" class="cel-img">
          <div class="cel-content">
            <h3 class="cel-h3">💍 Weddings (Vivaha / Nikah)</h3>
            <p class="cel-p">Manage thousands of guests over multi-day sangeet, reception, and wedding ceremonies with multi-counter sync.</p>
          </div>
        </div>

        <div class="celebration-card">
          <img src="https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=600&q=80" alt="Birthday" class="cel-img">
          <div class="cel-content">
            <h3 class="cel-h3">👶 Barasala & Birthdays</h3>
            <p class="cel-p">Cradle ceremonies, naming festivities, and milestone 1st birthdays. Keep track of clothing, gold chains, and cash blessings.</p>
          </div>
        </div>

        <div class="celebration-card">
          <img src="https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80" alt="Celebration" class="cel-img">
          <div class="cel-content">
            <h3 class="cel-h3">✂️ Tonsure (Mundan / Khatna)</h3>
            <p class="cel-p">Traditional first haircut ceremonies, Odugu, and Khatna functions. Organize maternal uncle gifts and family offerings.</p>
          </div>
        </div>

        <div class="celebration-card">
          <img src="https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=600&q=80" alt="Half Saree" class="cel-img">
          <div class="cel-content">
            <h3 class="cel-h3">🪷 Half Saree / Puberty Ceremony</h3>
            <p class="cel-p">Pushpalankarana, Langa Voni, and coming-of-age celebrations. Record sarees, gold jewelry, and shagun amounts.</p>
          </div>
        </div>

        <div class="celebration-card">
          <img src="https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80" alt="Dhoti Ceremony" class="cel-img">
          <div class="cel-content">
            <h3 class="cel-h3">🧵 Dhoti Ceremony & Upanayanam</h3>
            <p class="cel-p">Sacred thread rituals, Vedic upanayanam, and boys' dhoti functions with precise ledger records.</p>
          </div>
        </div>

        <div class="celebration-card">
          <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80" alt="Housewarming" class="cel-img">
          <div class="cel-content">
            <h3 class="cel-h3">🏡 Housewarming (Griha Pravesh)</h3>
            <p class="cel-p">Celebrate your new home. Keep a permanent, sacred digital record of all family and neighbour blessings.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Comparison Matrix Section -->
    <section id="compare-section" class="section-wrap">
      <div class="section-center-head">
        <div class="sec-tag">HONEST COMPARISON</div>
        <h2 class="sec-h2">Old Paper Notebook vs GiftVault</h2>
      </div>

      <div style="background: #FFFFFF; border: 1.5px solid var(--c-slate-border); border-radius: 24px; overflow: hidden; box-shadow: var(--shadow-sm);">
        <table class="data-table">
          <thead>
            <tr>
              <th>Feature / Capability</th>
              <th>Traditional Paper Ledger</th>
              <th style="color: var(--c-crimson);">GiftVault Digital Ledger</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Entry Speed</strong></td>
              <td style="color: var(--c-slate-muted);">Slow, handwriting legibility issues</td>
              <td style="color: var(--c-emerald); font-weight: 700;">⚡ 3 seconds with auto-complete</td>
            </tr>
            <tr>
              <td><strong>Disaster Protection</strong></td>
              <td style="color: var(--c-slate-muted);">Easily lost, damaged by spills or water</td>
              <td style="color: var(--c-emerald); font-weight: 700;">🔒 Cloud synced & exportable to Excel</td>
            </tr>
            <tr>
              <td><strong>Guest Acknowledgement</strong></td>
              <td style="color: var(--c-slate-muted);">None (pure verbal thank you)</td>
              <td style="color: var(--c-emerald); font-weight: 700;">📲 Instant WhatsApp digital card</td>
            </tr>
            <tr>
              <td><strong>Return Gift Calculation</strong></td>
              <td style="color: var(--c-slate-muted);">Hours spent searching old handwritten notes</td>
              <td style="color: var(--c-emerald); font-weight: 700;">🔄 Automatic reciprocity recommendation</td>
            </tr>
            <tr>
              <td><strong>Net Financial Surplus</strong></td>
              <td style="color: var(--c-slate-muted);">Manual calculator math prone to mistakes</td>
              <td style="color: var(--c-emerald); font-weight: 700;">📊 Real-time revenue vs expense balance</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- FAQ Section -->
    <section id="faq-section" class="section-wrap" style="background: #FFFFFF; border-top: 1px solid var(--c-slate-border);">
      <div class="section-center-head">
        <div class="sec-tag">CLARITY FIRST</div>
        <h2 class="sec-h2">Frequently Asked Questions</h2>
      </div>

      <div style="max-width: 800px; margin: 0 auto;">
        <div style="background: var(--c-surface-soft); border: 1.5px solid var(--c-slate-border); border-radius: 16px; padding: 20px 24px; margin-bottom: 12px;">
          <h4 style="font-size: 16px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 6px;">Can I create custom celebration events not listed above?</h4>
          <p style="font-size: 14px; color: var(--c-slate-body); line-height: 1.6;">Yes! Simply click "+ Create Event", select "Custom Event", and enter your own celebration title, date, venue, and host family names.</p>
        </div>
        <div style="background: var(--c-surface-soft); border: 1.5px solid var(--c-slate-border); border-radius: 16px; padding: 20px 24px; margin-bottom: 12px;">
          <h4 style="font-size: 16px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 6px;">Does Desk Mode work when wedding hall WiFi is unstable?</h4>
          <p style="font-size: 14px; color: var(--c-slate-body); line-height: 1.6;">Yes. All gift entries are instantly cached to local device storage. You can continue typing without pause, and export your spreadsheet at any moment.</p>
        </div>
        <div style="background: var(--c-surface-soft); border: 1.5px solid var(--c-slate-border); border-radius: 16px; padding: 20px 24px;">
          <h4 style="font-size: 16px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 6px;">Is GiftVault free for our family?</h4>
          <p style="font-size: 14px; color: var(--c-slate-body); line-height: 1.6;">Yes. Personal events are completely free forever, with unlimited entries and exports.</p>
        </div>
      </div>
    </section>

    <!-- Grand CTA Footer -->
    <footer style="background: #FFFFFF; border-top: 1px solid var(--c-slate-border); padding: 64px 24px 32px 24px;">
      <div style="max-width: 1240px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
        <div class="brand-group">
          <div class="brand-symbol" style="width: 32px; height: 32px;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          </div>
          <div class="brand-title" style="font-size: 18px;">Gift<span>Vault</span></div>
        </div>
        <div style="font-size: 13.5px; color: var(--c-slate-muted);">
          © 2026 GiftVault Inc. The Modern Red Notebook for South Asian Celebrations.
        </div>
      </div>
    </footer>
  </main>

  <!-- ============================================================
       VIEW 2: DEDICATED SIGN-IN SCREEN
       ============================================================ -->
  <main id="view-login" class="view-container">
    <div class="login-container">
      <div class="login-split-card">
        <!-- Banner Side -->
        <div class="login-banner-side">
          <div>
            <div class="pill-badge" style="background: #FFFFFF;">
              <span class="pill-dot"></span>
              <span>256-BIT ENCRYPTION</span>
            </div>
            <h2 style="font-size: 28px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 12px; line-height: 1.25;">
              Welcome to Your Family Vault
            </h2>
            <p style="font-size: 14.5px; color: var(--c-slate-body); line-height: 1.6;">
              Sign in as the Host Family Admin to oversee all accounts, or as the Munshi Desk Cashier for high-speed counter entries.
            </p>
          </div>

          <div style="border-top: 1px solid var(--c-crimson-border); padding-top: 20px;">
            <div style="font-size: 12px; font-weight: 800; color: var(--c-crimson); text-transform: uppercase; margin-bottom: 4px;">Zero Leakage Policy</div>
            <div style="font-size: 13px; color: var(--c-slate-muted);">Your auspicious family ledgers remain strictly confidential.</div>
          </div>
        </div>

        <!-- Form Side -->
        <div class="login-form-side">
          <div style="margin-bottom: 24px;">
            <h3 style="font-size: 22px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 6px;">Sign In</h3>
            <p style="font-size: 13px; color: var(--c-slate-muted);">Access your active events via Phone OTP or Google.</p>
          </div>

          <!-- Role Selector -->
          <div class="form-group">
            <label class="form-label">Select Your Role</label>
            <div class="role-pills">
              <div class="role-pill active" onclick="setRole('admin', this)">👑 Host Admin</div>
              <div class="role-pill" onclick="setRole('munshi', this)">⚡ Munshi Cashier</div>
              <div class="role-pill" onclick="setRole('viewer', this)">👁️ Relative / Guest</div>
            </div>
          </div>

          <div id="login-phone-step">
            <div class="form-group">
              <label class="form-label">Mobile Number</label>
              <div style="display: flex; gap: 8px;">
                <span style="background: var(--c-surface-soft); border: 1.5px solid var(--c-slate-border); padding: 12px 14px; border-radius: 12px; font-weight: 600; font-size: 14px;">+91</span>
                <input type="tel" id="login-phone-field" class="form-input" placeholder="98480 12345" value="9848012345" maxlength="10">
              </div>
            </div>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 12px; margin-bottom: 16px;" onclick="sendLoginOTP()">
              Send Verification OTP →
            </button>
          </div>

          <div id="login-otp-step" style="display: none;">
            <div class="form-group">
              <label class="form-label">Enter 4-Digit OTP (Test Code: <strong style="color: var(--c-crimson);">1234</strong>)</label>
              <div style="display: flex; gap: 10px; justify-content: center; margin: 12px 0;">
                <input type="text" class="form-input" maxlength="1" value="1" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
                <input type="text" class="form-input" maxlength="1" value="2" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
                <input type="text" class="form-input" maxlength="1" value="3" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
                <input type="text" class="form-input" maxlength="1" value="4" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
              </div>
            </div>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 12px; margin-bottom: 16px;" onclick="verifyLoginOTP()">
              Verify & Launch Vault ✓
            </button>
          </div>

          <div style="text-align: center; margin: 12px 0; font-size: 12px; color: var(--c-slate-muted);">or</div>

          <button type="button" class="btn-outline" style="width: 100%; justify-content: center; padding: 11px; margin-bottom: 16px;" onclick="verifyLoginOTP()">
            <svg width="16" height="16" viewBox="0 0 24 24"><path fill="#EA4335" d="M12 5c1.6 0 3 .6 4.1 1.6l3.1-3.1C17.3 1.7 14.8 1 12 1 7.5 1 3.7 3.6 1.9 7.3l3.7 2.9C6.5 7.4 9 5 12 5z"/><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.7-.2-2.3H12v4.5h6.5c-.3 1.5-1.1 2.8-2.4 3.7l3.7 2.9c2.2-2 3.7-5.1 3.7-8.8z"/><path fill="#FBBC05" d="M5.6 14.8c-.2-.7-.4-1.5-.4-2.3 0-.8.2-1.6.4-2.3L1.9 7.3C.7 9.7 0 12.3 0 15s.7 5.3 1.9 7.7l3.7-2.9z"/><path fill="#34A853" d="M12 23c3.2 0 6-1.1 8-3l-3.7-2.9c-1.1.7-2.5 1.2-4.3 1.2-3 0-5.5-2.4-6.4-5.2L1.9 16c1.8 3.7 5.6 7 10.1 7z"/></svg>
            Sign in with Google
          </button>

          <div style="text-align: center;">
            <button type="button" onclick="showView('landing')" style="font-size: 13px; color: var(--c-slate-muted); background: none; border: none; cursor: pointer;">
              ← Back to Home
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>

  <!-- ============================================================
       VIEW 3: IN-APP COMPLETE WORKSPACE
       ============================================================ -->
  <main id="view-app" class="view-container">
    <div class="app-workspace">
      
      <!-- Top Workspace Bar -->
      <div class="app-top-header">
        <div style="display: flex; align-items: center; gap: 14px;">
          <div class="brand-symbol" style="width: 38px; height: 38px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          </div>
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span id="active-event-title-display" style="font-weight: 800; font-size: 16px; color: var(--c-slate-dark);">Rahul & Snigdha Wedding</span>
              <span style="background: var(--c-emerald-soft); color: var(--c-emerald); font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 9999px;">LIVE VAULT</span>
            </div>
            <div id="active-event-sub-display" style="font-size: 12px; color: var(--c-slate-muted);">Wedding Ceremony • Hyderabad</div>
          </div>
        </div>

        <div style="display: flex; gap: 10px;">
          <button type="button" class="btn-outline" onclick="openCreateEventModal()" style="padding: 7px 14px; font-size: 13px;">
            + Switch / Create Event
          </button>
          <button type="button" class="btn-outline" onclick="showView('landing')" style="padding: 7px 14px; font-size: 13px;">
            Home
          </button>
          <button type="button" class="btn-crimson" onclick="openTab('desk')" style="padding: 7px 16px; font-size: 13px;">
            ⚡ Munshi Desk
          </button>
        </div>
      </div>

      <!-- Tab Navigation -->
      <div class="tab-nav-bar">
        <button type="button" class="tab-nav-btn active" onclick="openTab('dashboard', this)">📊 Dashboard</button>
        <button type="button" class="tab-nav-btn" onclick="openTab('desk', this)">✍️ Munshi Desk</button>
        <button type="button" class="tab-nav-btn" onclick="openTab('ledger', this)">📖 Red Notebook (Ledger)</button>
        <button type="button" class="tab-nav-btn" onclick="openTab('expenses', this)">💸 Expenses & Surplus</button>
        <button type="button" class="tab-nav-btn" onclick="openTab('reciprocity', this)">🔄 Reciprocity Tracker</button>
        <button type="button" class="tab-nav-btn" onclick="openTab('soundbox', this)">🔔 UPI QR Soundbox</button>
        <button type="button" class="tab-nav-btn" onclick="openTab('settings', this)">⚙️ Settings</button>
      </div>

      <!-- TAB 1: DASHBOARD -->
      <div id="tab-dashboard" class="app-screen active">
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;">
          <div class="metric-cell" style="background: #FFFFFF;">
            <div class="metric-label">Total Blessings</div>
            <div class="metric-val" id="dash-inflow" style="color: var(--c-crimson);">₹0</div>
            <div style="font-size: 11.5px; color: var(--c-slate-muted); margin-top: 4px;">0 entries recorded</div>
          </div>
          <div class="metric-cell" style="background: #FFFFFF;">
            <div class="metric-label">Cash In Counter</div>
            <div class="metric-val" id="dash-cash">₹0</div>
            <div style="font-size: 11.5px; color: var(--c-slate-muted); margin-top: 4px;">Physical envelope box</div>
          </div>
          <div class="metric-cell" style="background: #FFFFFF;">
            <div class="metric-label">Online UPI Transfers</div>
            <div class="metric-val" id="dash-upi">₹0</div>
            <div style="font-size: 11.5px; color: var(--c-slate-muted); margin-top: 4px;">Direct to bank account</div>
          </div>
          <div class="metric-cell" style="background: #FFFFFF;">
            <div class="metric-label">Gold & Silver</div>
            <div class="metric-val" id="dash-jewels">0g / 0g</div>
            <div style="font-size: 11.5px; color: var(--c-slate-muted); margin-top: 4px;">Jewelry offerings</div>
          </div>
        </div>

        <!-- Empty State Box -->
        <div id="dash-empty-prompt" style="text-align: center; padding: 60px 20px; background: #FFFFFF; border: 1.5px dashed var(--c-slate-border); border-radius: 20px;">
          <div style="font-size: 38px; margin-bottom: 12px;">🪙</div>
          <h3 style="font-size: 19px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 6px;">Fresh Event Vault Ready</h3>
          <p style="font-size: 14px; color: var(--c-slate-muted); max-width: 440px; margin: 0 auto 20px auto;">
            Zero dummy records. Click below to record your first real guest blessing at the Munshi counter.
          </p>
          <button type="button" class="btn-crimson" onclick="openTab('desk')">+ Record First Blessing</button>
        </div>

        <!-- Recent Records Table -->
        <div id="dash-table-wrap" style="display: none;" class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Receipt #</th>
                <th>Guest Name</th>
                <th>City / Town</th>
                <th>Amount</th>
                <th>Type</th>
                <th>WhatsApp</th>
              </tr>
            </thead>
            <tbody id="dash-tbody"></tbody>
          </table>
        </div>
      </div>

      <!-- TAB 2: MUNSHI FAST ENTRY DESK -->
      <div id="tab-desk" class="app-screen">
        <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px;">
          <div style="background: #FFFFFF; border: 1.5px solid var(--c-slate-border); border-radius: 20px; padding: 28px;">
            <h3 style="font-size: 18px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 18px;">✍️ Reception Desk Entry</h3>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
              <div class="form-group">
                <label class="form-label">Guest Name *</label>
                <input type="text" id="desk-name" class="form-input" placeholder="e.g. Venkat Rao">
              </div>
              <div class="form-group">
                <label class="form-label">City / Native Place</label>
                <input type="text" id="desk-city" class="form-input" placeholder="e.g. Hyderabad, Vijayawada">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
              <div class="form-group">
                <label class="form-label">Mobile (for WhatsApp Card)</label>
                <input type="tel" id="desk-phone" class="form-input" placeholder="9848012345">
              </div>
              <div class="form-group">
                <label class="form-label">Relation / Side</label>
                <select id="desk-relation" class="form-input">
                  <option value="Relatives">Relatives</option>
                  <option value="Friends">Friends</option>
                  <option value="Colleagues">Colleagues</option>
                  <option value="Neighbours">Neighbours</option>
                  <option value="Well Wisher">Well Wisher</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">Blessing Type</label>
              <div style="display: flex; gap: 10px;">
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--c-slate-border); border-radius: 12px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="gift-mode" value="CASH" checked onchange="toggleMode('cash')"> 💵 Cash
                </label>
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--c-slate-border); border-radius: 12px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="gift-mode" value="UPI" onchange="toggleMode('cash')"> 📲 Online UPI
                </label>
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--c-slate-border); border-radius: 12px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="gift-mode" value="GOLD" onchange="toggleMode('gold')"> 🥇 Gold/Silver
                </label>
              </div>
            </div>

            <div id="desk-cash-box" class="form-group">
              <label class="form-label">Amount (INR) *</label>
              <input type="number" id="desk-amount" class="form-input" style="font-size: 20px; font-weight: 800; color: var(--c-crimson);" placeholder="₹ 1116">
              <div class="coin-group">
                <button type="button" class="coin-chip" onclick="setCoin(516)">+ ₹516</button>
                <button type="button" class="coin-chip" onclick="setCoin(1116)">+ ₹1,116</button>
                <button type="button" class="coin-chip" onclick="setCoin(2116)">+ ₹2,116</button>
                <button type="button" class="coin-chip" onclick="setCoin(5116)">+ ₹5,116</button>
                <button type="button" class="coin-chip" onclick="setCoin(10116)">+ ₹10,116</button>
                <button type="button" class="coin-chip" onclick="addLuckyCoin()">+ ₹1 Lucky Coin</button>
              </div>
            </div>

            <div id="desk-gold-box" class="form-group" style="display: none;">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div>
                  <label class="form-label">Gold Weight (grams)</label>
                  <input type="number" step="0.1" id="desk-gold" class="form-input" placeholder="e.g. 8.0">
                </div>
                <div>
                  <label class="form-label">Silver Weight (grams)</label>
                  <input type="number" step="1" id="desk-silver" class="form-input" placeholder="e.g. 100">
                </div>
              </div>
            </div>

            <div style="display: flex; gap: 12px; margin-top: 14px;">
              <button type="button" class="btn-crimson" style="flex: 1; justify-content: center; padding: 13px;" onclick="saveEntry()">
                💾 Save Entry
              </button>
              <button type="button" class="btn-outline" onclick="clearForm()">
                Clear
              </button>
            </div>
          </div>

          <!-- Soundbox & Live Feed Card -->
          <div style="background: #FFFFFF; border: 1.5px solid var(--c-slate-border); border-radius: 20px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <h4 style="font-size: 16px; font-weight: 800; color: var(--c-slate-dark); margin-bottom: 12px;">
                🔔 Audio Confirmation & Last Receipt
              </h4>
              <p style="font-size: 13.5px; color: var(--c-slate-muted); line-height: 1.6; margin-bottom: 18px;">
                Every saved entry plays a pleasant audio chime to confirm accuracy at the desk.
              </p>

              <div style="background: var(--c-crimson-soft); border: 1px solid var(--c-crimson-border); border-radius: 14px; padding: 16px; margin-bottom: 18px;">
                <div style="font-size: 11.5px; font-weight: 700; color: var(--c-crimson); text-transform: uppercase; margin-bottom: 4px;">Latest Receipt:</div>
                <div id="desk-last-receipt" style="font-size: 14px; font-weight: 700; color: var(--c-slate-dark);">No entries recorded yet</div>
              </div>
            </div>

            <button type="button" class="btn-outline" style="width: 100%; justify-content: center;" onclick="playAudioChime(); showToast('🔊 Audio soundbox chime tested successfully!');">
              🔊 Test Soundbox Chime
            </button>
          </div>
        </div>
      </div>

      <!-- TAB 3: RED BOOK LEDGER -->
      <div id="tab-ledger" class="app-screen">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; flex-wrap: wrap; gap: 12px;">
          <div>
            <h3 style="font-size: 20px; font-weight: 800; color: var(--c-slate-dark);">📖 Red Notebook (Full Digital Ledger)</h3>
            <p style="font-size: 13px; color: var(--c-slate-muted);">Comprehensive record of all guest offerings and jewelry</p>
          </div>
          <div style="display: flex; gap: 10px;">
            <button type="button" class="btn-outline" onclick="exportCSV()">📥 Download Excel (CSV)</button>
            <button type="button" class="btn-crimson" onclick="window.print()">🖨️ Print Summary</button>
          </div>
        </div>

        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>#</th>
                <th>Receipt No</th>
                <th>Guest Name</th>
                <th>City / Place</th>
                <th>Relationship</th>
                <th>Blessing Amount</th>
                <th>Gold / Silver</th>
                <th>Mode</th>
                <th>WhatsApp</th>
              </tr>
            </thead>
            <tbody id="ledger-tbody">
              <tr>
                <td colspan="9" style="text-align: center; color: var(--c-slate-muted); padding: 32px;">No records found. Entries made in Desk Mode will appear here.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TAB 4: EXPENSES -->
      <div id="tab-expenses" class="app-screen">
        <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px;">
          <div style="background: #FFFFFF; border: 1.5px solid var(--c-slate-border); border-radius: 20px; padding: 28px;">
            <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 16px; color: var(--c-slate-dark);">💸 Log Event Expense</h3>
            <div class="form-group">
              <label class="form-label">Expense Category</label>
              <select id="exp-cat" class="form-input">
                <option value="Hall & Venue">Hall & Venue Rental</option>
                <option value="Catering & Food">Catering & Dining</option>
                <option value="Decor & Flowers">Decor & Lighting</option>
                <option value="Photo & Video">Photography & Video</option>
                <option value="Music & Sangeet">Music, Band & Sound</option>
                <option value="Traditional Attire">Traditional Clothing / Attire</option>
                <option value="Miscellaneous">Miscellaneous</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Description / Vendor Notes</label>
              <input type="text" id="exp-notes" class="form-input" placeholder="e.g. Catering Advance Payment">
            </div>
            <div class="form-group">
              <label class="form-label">Amount (INR) *</label>
              <input type="number" id="exp-amt" class="form-input" placeholder="₹ 50000">
            </div>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 12px;" onclick="saveExpense()">
              + Add Expense Record
            </button>
          </div>

          <div style="background: #FFFFFF; border: 1.5px solid var(--c-slate-border); border-radius: 20px; padding: 28px;">
            <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 16px; color: var(--c-slate-dark);">📊 Financial Balance Sheet</h3>
            <div class="metric-cell" style="margin-bottom: 12px; background: #FFFFFF;">
              <div class="metric-label">Total Blessings Inflow</div>
              <div class="metric-val" id="exp-inflow-val" style="color: var(--c-crimson);">₹0</div>
            </div>
            <div class="metric-cell" style="margin-bottom: 12px; background: #FFFFFF;">
              <div class="metric-label">Total Event Expenses</div>
              <div class="metric-val" id="exp-outflow-val" style="color: var(--c-slate-dark);">₹0</div>
            </div>
            <div class="metric-cell" style="background: #FFFFFF;">
              <div class="metric-label">Net Financial Surplus</div>
              <div class="metric-val" id="exp-surplus-val" style="color: var(--c-emerald);">₹0</div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 5: RECIPROCITY -->
      <div id="tab-reciprocity" class="app-screen">
        <div style="background: #FFFFFF; border: 1.5px solid var(--c-slate-border); border-radius: 20px; padding: 24px; margin-bottom: 20px;">
          <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 8px; color: var(--c-slate-dark);">🔄 Reciprocity Intelligence</h3>
          <p style="font-size: 14px; color: var(--c-slate-muted);">
            Preserve family relationships with automated recommendations for return blessings (+₹1 lucky coin standard).
          </p>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>Guest Name</th>
                <th>Place</th>
                <th>They Blessed Us</th>
                <th>Recommended Return (+₹1)</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody id="recip-tbody">
              <tr>
                <td colspan="5" style="text-align: center; color: var(--c-slate-muted); padding: 32px;">Recorded guest entries will automatically appear here.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TAB 6: SOUNDBOX QR -->
      <div id="tab-soundbox" class="app-screen">
        <div style="max-width: 480px; margin: 0 auto; background: #FFFFFF; border: 1.5px solid var(--c-slate-border); border-radius: 24px; padding: 36px; text-align: center; box-shadow: var(--shadow-md);">
          <div class="pill-badge" style="margin-bottom: 14px;">
            <span class="pill-dot"></span>
            <span>COUNTER SOUNDBOX QR</span>
          </div>
          <h3 style="font-size: 20px; font-weight: 800; margin-bottom: 6px; color: var(--c-slate-dark);">Scan to Transfer Blessings</h3>
          <p style="font-size: 13px; color: var(--c-slate-muted); margin-bottom: 20px;">Support for PhonePe, Google Pay, Paytm, and BHIM.</p>

          <div style="background: #FFFFFF; padding: 14px; border: 1.5px solid var(--c-slate-border); border-radius: 16px; display: inline-block; margin-bottom: 18px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=upi://pay?pa=giftvault@hdfcbank&am=1116&cu=INR" alt="UPI QR" style="display: block; border-radius: 8px;">
          </div>

          <div style="font-weight: 800; font-size: 15px; margin-bottom: 4px; color: var(--c-slate-dark);">UPI ID: giftvault@hdfcbank</div>
          <div style="font-size: 12.5px; color: var(--c-slate-muted); margin-bottom: 20px;">Counter speaker automatically chimes upon successful transfer</div>

          <button type="button" class="btn-crimson" style="width: 100%; justify-content: center;" onclick="playAudioChime(); showToast('🔔 Simulated payment verified with soundbox chime!');">
            🔔 Test Payment Audio
          </button>
        </div>
      </div>

      <!-- TAB 7: SETTINGS -->
      <div id="tab-settings" class="app-screen">
        <div style="max-width: 600px; margin: 0 auto; background: #FFFFFF; border: 1.5px solid var(--c-slate-border); border-radius: 20px; padding: 28px;">
          <h3 style="font-size: 19px; font-weight: 800; margin-bottom: 18px; color: var(--c-slate-dark);">⚙️ Event Settings</h3>
          <div class="form-group">
            <label class="form-label">Active Event Name</label>
            <input type="text" id="setting-title" class="form-input" value="Rahul & Snigdha Wedding Celebration">
          </div>
          <div class="form-group">
            <label class="form-label">Host Contact Mobile</label>
            <input type="tel" id="setting-phone" class="form-input" value="9848012345">
          </div>
          <div style="border-top: 1px solid var(--c-slate-border); padding-top: 20px; margin-top: 20px;">
            <button type="button" class="btn-outline" style="color: var(--c-crimson); border-color: var(--c-crimson-border);" onclick="resetAllData()">
              🗑️ Reset All Data to Fresh ₹0 State
            </button>
          </div>
        </div>
      </div>

    </div>
  </main>

  <!-- ============================================================
       MODAL: CREATE NEW EVENT (WITH PRE-POPULATED CELEBRATION TYPES)
       ============================================================ -->
  <div id="create-event-modal" class="modal-backdrop">
    <div class="modal-card">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <h3 style="font-size: 20px; font-weight: 800; color: var(--c-slate-dark);">+ Create or Switch Event</h3>
        <button type="button" onclick="closeCreateEventModal()" style="background: none; border: none; font-size: 22px; cursor: pointer; color: var(--c-slate-muted);">✕</button>
      </div>

      <div class="form-group">
        <label class="form-label">Select Celebration Type *</label>
        <select id="modal-event-type" class="form-input" onchange="handleCelebrationTypeChange(this.value)">
          <option value="Wedding">💍 Wedding (Vivaha / Nikah)</option>
          <option value="Birthday">👶 Barasala / Naming / 1st Birthday</option>
          <option value="Tonsure">✂️ Tonsure (Mundan / Khatna / Odugu)</option>
          <option value="Puberty">🪷 Half Saree / Puberty (Pushpalankarana)</option>
          <option value="Dhoti">🧵 Dhoti Ceremony / Upanayanam</option>
          <option value="Housewarming">🏡 Housewarming (Griha Pravesh)</option>
          <option value="Custom">✨ Custom Event (Enter Own Celebration)</option>
        </select>
      </div>

      <div class="form-group">
        <label class="form-label">Event Title *</label>
        <input type="text" id="modal-event-title" class="form-input" placeholder="e.g. Rahul & Snigdha Wedding Celebration" value="Rahul & Snigdha Wedding Celebration">
      </div>

      <div class="form-group">
        <label class="form-label">Venue / City *</label>
        <input type="text" id="modal-event-venue" class="form-input" placeholder="e.g. Royal Palace Hall, Hyderabad" value="Hyderabad">
      </div>

      <div class="form-group">
        <label class="form-label">Event Date</label>
        <input type="date" id="modal-event-date" class="form-input" value="2026-11-20">
      </div>

      <div class="form-group">
        <label class="form-label">Host Family / Couple Name</label>
        <input type="text" id="modal-event-host" class="form-input" placeholder="e.g. Rao & Reddy Families">
      </div>

      <div style="display: flex; gap: 12px; margin-top: 24px;">
        <button type="button" class="btn-crimson" style="flex: 1; justify-content: center; padding: 13px;" onclick="confirmCreateEvent()">
          Create & Open Vault →
        </button>
        <button type="button" class="btn-outline" onclick="closeCreateEventModal()">
          Cancel
        </button>
      </div>
    </div>
  </div>

  <!-- Toast -->
  <div id="toast" class="toast-box"></div>

  <!-- Application Logic -->
  <script>
    let VAULT_DATA = {
      eventName: 'Rahul & Snigdha Wedding Celebration',
      eventVenue: 'Hyderabad',
      eventType: 'Wedding',
      entries: [],
      expenses: []
    };

    // Load Local Storage
    try {
      const s = localStorage.getItem('GIFTVAULT_ENGLISH_DATA');
      if (s) {
        const p = JSON.parse(s);
        VAULT_DATA.eventName = p.eventName || VAULT_DATA.eventName;
        VAULT_DATA.eventVenue = p.eventVenue || VAULT_DATA.eventVenue;
        VAULT_DATA.eventType = p.eventType || VAULT_DATA.eventType;
        VAULT_DATA.entries = p.entries || [];
        VAULT_DATA.expenses = p.expenses || [];
      }
    } catch(e) {}

    function persist() {
      try {
        localStorage.setItem('GIFTVAULT_ENGLISH_DATA', JSON.stringify(VAULT_DATA));
      } catch(e) {}
      renderAll();
    }

    // View Navigation
    function showView(viewId) {
      document.querySelectorAll('.view-container').forEach(v => v.classList.remove('active'));
      const t = document.getElementById('view-' + viewId);
      if (t) {
        t.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    function openTab(tabId, el) {
      showView('app');
      document.querySelectorAll('.app-screen').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.tab-nav-btn').forEach(b => b.classList.remove('active'));
      const s = document.getElementById('tab-' + tabId);
      if (s) s.classList.add('active');
      if (el) el.classList.add('active');
    }

    function scrollToId(id) {
      showView('landing');
      setTimeout(() => {
        const el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    }

    function showToast(msg) {
      const t = document.getElementById('toast');
      t.innerText = msg;
      t.style.display = 'block';
      setTimeout(() => { t.style.display = 'none'; }, 2600);
    }

    // Web Audio Soundbox
    function playAudioChime() {
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

    // Hero Switcher with Realistic Unsplash Images
    const HERO_SWITCHER = {
      wedding: {
        title: 'Rahul & Snigdha Wedding Celebration',
        venue: 'Gachibowli, Hyderabad • Live Shagun Vault',
        img: 'https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=800&q=80',
        inflow: '₹8,42,116',
        exp: '₹4,15,000',
        sur: '+₹4,27,116'
      },
      birthday: {
        title: 'Advait 1st Birthday & Barasala Festivity',
        venue: 'Guntur Grand Hall • Live Ledger',
        img: 'https://images.unsplash.com/photo-1530103862676-de8c9debad1d?auto=format&fit=crop&w=800&q=80',
        inflow: '₹3,18,116',
        exp: '₹1,20,000',
        sur: '+₹1,98,116'
      },
      tonsure: {
        title: 'Ayaan First Tonsure Ceremony (Khatna / Mundan)',
        venue: 'Banjara Hills, Hyderabad • Auspicious Blessings',
        img: 'https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=800&q=80',
        inflow: '₹4,11,116',
        exp: '₹1,80,000',
        sur: '+₹2,31,116'
      },
      puberty: {
        title: 'Sahasra Half Saree (Pushpalankarana) Function',
        venue: 'A-Plus Convention, Vijayawada • Live Ledger',
        img: 'https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=800&q=80',
        inflow: '₹5,62,116',
        exp: '₹2,50,000',
        sur: '+₹3,12,116'
      },
      dhoti: {
        title: 'Sai Charan Upanayanam & Dhoti Function',
        venue: 'Vedic Hall, Warangal • Traditional Ledger',
        img: 'https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=800&q=80',
        inflow: '₹3,85,116',
        exp: '₹1,50,000',
        sur: '+₹2,35,116'
      },
      housewarming: {
        title: 'Sri Nilayam Griha Pravesh Celebration',
        venue: 'MVP Colony, Visakhapatnam • Housewarming Vault',
        img: 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80',
        inflow: '₹6,75,116',
        exp: '₹3,10,000',
        sur: '+₹3,65,116'
      }
    };

    function switchHeroCelebration(key, btn) {
      document.querySelectorAll('.cat-chip').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const d = HERO_SWITCHER[key];
      if (d) {
        document.getElementById('hero-card-title').innerText = d.title;
        document.getElementById('hero-card-venue').innerText = d.venue;
        document.getElementById('hero-img-src').src = d.img;
        document.getElementById('hero-val-inflow').innerText = d.inflow;
        document.getElementById('hero-val-expenses').innerText = d.exp;
        document.getElementById('hero-val-surplus').innerText = d.sur;
      }
    }

    // Modal Create Event
    function openCreateEventModal() {
      document.getElementById('create-event-modal').style.display = 'flex';
    }
    function closeCreateEventModal() {
      document.getElementById('create-event-modal').style.display = 'none';
    }
    function handleCelebrationTypeChange(type) {
      const titleInput = document.getElementById('modal-event-title');
      if (type === 'Wedding') titleInput.value = 'Rahul & Snigdha Wedding Celebration';
      else if (type === 'Birthday') titleInput.value = 'Advait 1st Birthday & Barasala';
      else if (type === 'Tonsure') titleInput.value = 'Ayaan First Tonsure Ceremony (Mundan / Khatna)';
      else if (type === 'Puberty') titleInput.value = 'Sahasra Half Saree (Pushpalankarana) Function';
      else if (type === 'Dhoti') titleInput.value = 'Sai Charan Dhoti & Upanayanam Ceremony';
      else if (type === 'Housewarming') titleInput.value = 'Sri Nilayam Griha Pravesh Function';
      else if (type === 'Custom') titleInput.value = 'Our Family Special Celebration';
    }

    function confirmCreateEvent() {
      const type = document.getElementById('modal-event-type').value;
      const title = document.getElementById('modal-event-title').value.trim() || 'My Family Celebration';
      const venue = document.getElementById('modal-event-venue').value.trim() || 'Hyderabad';
      
      VAULT_DATA.eventType = type;
      VAULT_DATA.eventName = title;
      VAULT_DATA.eventVenue = venue;
      VAULT_DATA.entries = [];
      VAULT_DATA.expenses = [];
      persist();

      closeCreateEventModal();
      showToast(`🎉 "${title}" created successfully with fresh ₹0 vault!`);
      showView('app');
      openTab('desk');
    }

    // Login Logic
    function setRole(r, el) {
      document.querySelectorAll('.role-pill').forEach(p => p.classList.remove('active'));
      if (el) el.classList.add('active');
    }
    function sendLoginOTP() {
      const p = document.getElementById('login-phone-field').value.trim();
      if (!p || p.length < 10) { showToast('Please enter a valid 10-digit mobile number.'); return; }
      document.getElementById('login-phone-step').style.display = 'none';
      document.getElementById('login-otp-step').style.display = 'block';
      showToast('Verification code 1234 sent!');
    }
    function verifyLoginOTP() {
      showToast('Login successful! Launching your family vault...');
      setTimeout(() => {
        showView('app');
        openTab('dashboard');
      }, 350);
    }

    // Munshi Entry
    function setCoin(amt) { document.getElementById('desk-amount').value = amt; }
    function addLuckyCoin() {
      const f = document.getElementById('desk-amount');
      let val = parseInt(f.value) || 0;
      f.value = val + (val % 10 === 0 ? 1 : 16);
    }
    function toggleMode(m) {
      if (m === 'gold') {
        document.getElementById('desk-cash-box').style.display = 'none';
        document.getElementById('desk-gold-box').style.display = 'block';
      } else {
        document.getElementById('desk-cash-box').style.display = 'block';
        document.getElementById('desk-gold-box').style.display = 'none';
      }
    }

    function saveEntry() {
      const name = document.getElementById('desk-name').value.trim();
      const city = document.getElementById('desk-city').value.trim() || 'Local';
      const phone = document.getElementById('desk-phone').value.trim();
      const rel = document.getElementById('desk-relation').value;
      const mode = document.querySelector('input[name="gift-mode"]:checked').value;

      let amount = 0, gold = 0, silver = 0;
      if (mode === 'GOLD') {
        gold = parseFloat(document.getElementById('desk-gold').value) || 0;
        silver = parseFloat(document.getElementById('desk-silver').value) || 0;
        if (gold <= 0 && silver <= 0) { showToast('Please enter gold or silver weight.'); return; }
      } else {
        amount = parseInt(document.getElementById('desk-amount').value) || 0;
        if (amount <= 0) { showToast('Please enter a valid amount.'); return; }
      }

      if (!name) { showToast('Please enter guest name.'); return; }

      const receiptNo = 'GV-' + (100 + VAULT_DATA.entries.length + 1);
      VAULT_DATA.entries.unshift({
        id: Date.now(),
        receiptNo,
        name,
        city,
        phone,
        relation: rel,
        mode,
        amount,
        gold,
        silver,
        time: new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })
      });

      persist();
      playAudioChime();
      document.getElementById('desk-last-receipt').innerText = `${name} (${city}) - ${amount > 0 ? '₹' + amount.toLocaleString('en-IN') : gold + 'g Gold'} [#${receiptNo}]`;
      showToast(`Receipt #${receiptNo} recorded successfully!`);
      clearForm();
    }

    function clearForm() {
      document.getElementById('desk-name').value = '';
      document.getElementById('desk-city').value = '';
      document.getElementById('desk-phone').value = '';
      document.getElementById('desk-amount').value = '';
      document.getElementById('desk-gold').value = '';
      document.getElementById('desk-silver').value = '';
    }

    function saveExpense() {
      const cat = document.getElementById('exp-cat').value;
      const notes = document.getElementById('exp-notes').value.trim();
      const amt = parseInt(document.getElementById('exp-amt').value) || 0;
      if (amt <= 0) { showToast('Please enter valid expense amount.'); return; }
      VAULT_DATA.expenses.push({ id: Date.now(), cat, notes, amt });
      persist();
      showToast('Expense recorded successfully!');
      document.getElementById('exp-notes').value = '';
      document.getElementById('exp-amt').value = '';
    }

    function resetAllData() {
      if (confirm('Reset entire vault to clean ₹0 fresh state?')) {
        VAULT_DATA.entries = [];
        VAULT_DATA.expenses = [];
        persist();
        showToast('Vault wiped clean to fresh state!');
      }
    }

    function exportCSV() {
      if (VAULT_DATA.entries.length === 0) { showToast('No records to export.'); return; }
      let csv = "\uFEFFReceipt,Name,City,Relation,Amount,Gold_g,Silver_g,Mode,Time\n";
      VAULT_DATA.entries.forEach(e => {
        csv += `"${e.receiptNo}","${e.name}","${e.city}","${e.relation}",${e.amount},${e.gold},${e.silver},"${e.mode}","${e.time}"\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `GiftVault_Ledger_${Date.now()}.csv`;
      a.click();
      showToast('Excel CSV download initiated!');
    }

    function renderAll() {
      document.getElementById('active-event-title-display').innerText = VAULT_DATA.eventName;
      document.getElementById('active-event-sub-display').innerText = `${VAULT_DATA.eventType} • ${VAULT_DATA.eventVenue}`;

      let tot = 0, c = 0, u = 0, g = 0, s = 0;
      VAULT_DATA.entries.forEach(e => {
        tot += e.amount || 0;
        if (e.mode === 'CASH') c += e.amount || 0;
        if (e.mode === 'UPI') u += e.amount || 0;
        g += e.gold || 0;
        s += e.silver || 0;
      });

      let expTot = 0;
      VAULT_DATA.expenses.forEach(x => { expTot += x.amt || 0; });
      const surplus = tot - expTot;

      // Dashboard
      document.getElementById('dash-inflow').innerText = '₹' + tot.toLocaleString('en-IN');
      document.getElementById('dash-cash').innerText = '₹' + c.toLocaleString('en-IN');
      document.getElementById('dash-upi').innerText = '₹' + u.toLocaleString('en-IN');
      document.getElementById('dash-jewels').innerText = `${g}g / ${s}g`;

      // Expenses
      document.getElementById('exp-inflow-val').innerText = '₹' + tot.toLocaleString('en-IN');
      document.getElementById('exp-outflow-val').innerText = '₹' + expTot.toLocaleString('en-IN');
      document.getElementById('exp-surplus-val').innerText = (surplus >= 0 ? '+₹' : '-₹') + Math.abs(surplus).toLocaleString('en-IN');

      const emptyPrompt = document.getElementById('dash-empty-prompt');
      const tableWrap = document.getElementById('dash-table-wrap');
      const dashTbody = document.getElementById('dash-tbody');
      const ledgerTbody = document.getElementById('ledger-tbody');
      const recipTbody = document.getElementById('recip-tbody');

      if (VAULT_DATA.entries.length === 0) {
        emptyPrompt.style.display = 'block';
        tableWrap.style.display = 'none';
        ledgerTbody.innerHTML = '<tr><td colspan="9" style="text-align: center; color: var(--c-slate-muted); padding: 32px;">No records found. Entries made in Desk Mode will appear here.</td></tr>';
        recipTbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: var(--c-slate-muted); padding: 32px;">Recorded guest entries will automatically appear here.</td></tr>';
      } else {
        emptyPrompt.style.display = 'none';
        tableWrap.style.display = 'block';

        let rH = '';
        let lH = '';
        let recH = '';

        VAULT_DATA.entries.forEach((e, idx) => {
          const amtStr = e.amount > 0 ? '₹' + e.amount.toLocaleString('en-IN') : '-';
          const jewelStr = (e.gold > 0 ? e.gold + 'g Gold ' : '') + (e.silver > 0 ? e.silver + 'g Silver' : '') || '-';
          const recAmt = e.amount > 0 ? '₹' + (e.amount + 100).toLocaleString('en-IN') : 'Jewelry';

          rH += `
            <tr>
              <td><strong>#${e.receiptNo}</strong></td>
              <td style="font-weight: 700;">${e.name}</td>
              <td>${e.city}</td>
              <td style="font-weight: 800; color: var(--c-crimson);">${amtStr}</td>
              <td><span style="font-size: 11px; background: var(--c-crimson-soft); color: var(--c-crimson); padding: 3px 8px; border-radius: 6px; font-weight: 700;">${e.mode}</span></td>
              <td><button type="button" class="btn-outline" style="padding: 4px 10px; font-size: 11px;" onclick="window.open('https://wa.me/91${e.phone||'9848012345'}?text=Thank you for blessing us!', '_blank')">WhatsApp</button></td>
            </tr>
          `;

          lH += `
            <tr>
              <td>${idx + 1}</td>
              <td><strong>#${e.receiptNo}</strong></td>
              <td style="font-weight: 700;">${e.name}</td>
              <td>${e.city}</td>
              <td>${e.relation}</td>
              <td style="font-weight: 800; color: var(--c-crimson);">${amtStr}</td>
              <td>${jewelStr}</td>
              <td><span style="font-size: 11px; background: var(--c-crimson-soft); color: var(--c-crimson); padding: 3px 8px; border-radius: 6px; font-weight: 700;">${e.mode}</span></td>
              <td><button type="button" class="btn-outline" style="padding: 4px 10px; font-size: 11px;" onclick="alert('Receipt #${e.receiptNo}: ${e.name} - ${amtStr}')">Details</button></td>
            </tr>
          `;

          recH += `
            <tr>
              <td><strong>${e.name}</strong></td>
              <td>${e.city}</td>
              <td style="font-weight: 700;">${amtStr}</td>
              <td style="font-weight: 800; color: var(--c-emerald);">${recAmt}</td>
              <td><span style="color: var(--c-emerald); font-size: 12px; font-weight: 800;">Recommendation Ready</span></td>
            </tr>
          `;
        });

        dashTbody.innerHTML = rH;
        ledgerTbody.innerHTML = lH;
        recipTbody.innerHTML = recH;
      }
    }

    renderAll();
  </script>
</body>
</html>
'''

# Write to all web targets
for p in ['web_preview/index.html', 'web_preview/desktop.html', 'web_preview/mobile.html', 'build/web/index.html', 'web/index.html']:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(APP_HTML)

print('Generated clean, 100% English, 5-palette, multi-event creation application!')
