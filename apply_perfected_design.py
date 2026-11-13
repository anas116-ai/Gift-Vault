# -*- coding: utf-8 -*-
"""
Generate the fully perfected, typography-curated GiftVault Application with:
1. Exact Color Palette from user image applied visibly:
   - #DCE2CC (Sage Ivory base wash & header badges)
   - #E5D0D5 (Rose Silk subtle panels & glow)
   - #A7D2B7 (Soft Mint borders & status tags)
   - #8E99CC (Slate Periwinkle subheaders & active tabs)
   - #000411 (Deep Night Slate for ultra-crisp typography)
   - #F8333C (Auspicious Rose Crimson for primary action buttons & cash highlights)
   - #036D19 (Prosperity Emerald for Net Surplus & verified receipts)
   - #CAFF0A (Electric Lime live indicators & pulse dots)
2. Typography Hierarchy (5 Typeface Classification applied systematically):
   - Luxury Serif: 'Playfair Display' for emotional luxury headlines & hero accentuation
   - Clean Sans-Serif: 'Plus Jakarta Sans' for crisp UI headers, buttons, cards
   - Editorial Sans: 'Inter' for high-readability body copy & data
   - Monospace: 'JetBrains Mono' for currency amounts, receipts, numbers, ledger codes
   - Script/Cursive: 'Great Vibes' / 'Playfair Display' italic for romantic blessing signatures
3. Ubiquitous Floating/Sticky "← Back" Navigation on Every Inner Screen (Hub, Login, Desk, Workspace)
4. Pristine, verified 1200px celebration imagery with elegant gradient scrims
"""

PERFECTED_APP = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>GiftVault • Royal Shagun Ledger & Celebration Treasury</title>
  
  <!-- Curated Font Families: Serif, Sans-Serif, Display, Monospace, Script -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600;1,700&family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap" rel="stylesheet">
  
  <style>
    /* ============================================================
       EXACT 8-COLOR SYSTEM FROM USER'S PALETTE
       Row 1: #CAFF0A (Electric Lime), #F8333C (Rose Crimson), #036D19 (Emerald), #000411 (Deep Night)
       Row 2: #DCE2CC (Sage Ivory), #E5D0D5 (Rose Silk), #A7D2B7 (Mint Sage), #8E99CC (Slate Periwinkle)
       ============================================================ */
    :root {
      /* Dominant Canvases (60%) */
      --c-base: #F9F8F5;
      --c-surface: #FFFFFF;
      --c-tint-sage: #DCE2CC;
      --c-tint-rose: #E5D0D5;
      --c-tint-mint: #A7D2B7;
      
      /* Typography & Neutral Structure (30%) */
      --c-night: #000411;
      --c-body: #1E293B;
      --c-muted: #64748B;
      --c-periwinkle: #8E99CC;
      --c-border: #E2E8F0;
      
      /* High-Energy Accents (10%) */
      --c-crimson: #F8333C;
      --c-crimson-hover: #D91C25;
      --c-crimson-bg: #FFF1F2;
      --c-crimson-border: #FFE4E6;
      
      --c-emerald: #036D19;
      --c-emerald-bg: #ECFDF5;
      --c-emerald-border: #A7D2B7;
      
      --c-lime: #CAFF0A;

      /* Typefaces Hierarchy */
      --font-serif: 'Playfair Display', Georgia, serif;
      --font-sans: 'Plus Jakarta Sans', -apple-system, sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --font-script: 'Great Vibes', cursive;

      /* Shadows */
      --shadow-sm: 0 1px 3px rgba(0, 4, 17, 0.05);
      --shadow-md: 0 4px 14px -2px rgba(0, 4, 17, 0.08), 0 2px 6px -1px rgba(0, 4, 17, 0.04);
      --shadow-lg: 0 14px 32px -4px rgba(0, 4, 17, 0.09), 0 6px 14px -2px rgba(0, 4, 17, 0.04);
      --shadow-xl: 0 24px 48px -8px rgba(0, 4, 17, 0.14);
      --shadow-crimson: 0 10px 26px -4px rgba(248, 51, 60, 0.38);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    body {
      background-color: var(--c-base);
      color: var(--c-body);
      font-family: var(--font-body);
      line-height: 1.5;
      overflow-x: hidden;
    }

    h1, h2, h3, h4, .brand-title {
      font-family: var(--font-sans);
    }

    .font-serif {
      font-family: var(--font-serif);
    }
    .font-script {
      font-family: var(--font-script);
    }
    .font-mono {
      font-family: var(--font-mono);
    }

    /* Ambient Soft Gradients */
    .ambient-top {
      position: absolute;
      top: 0;
      right: 0;
      width: 560px;
      height: 560px;
      background: radial-gradient(circle, rgba(229, 208, 213, 0.45) 0%, rgba(249, 248, 245, 0) 70%);
      pointer-events: none;
      z-index: 0;
    }
    .ambient-bottom {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 520px;
      height: 520px;
      background: radial-gradient(circle, rgba(220, 226, 204, 0.5) 0%, rgba(249, 248, 245, 0) 70%);
      pointer-events: none;
      z-index: 0;
    }

    /* Universal Sticky Back Bar Component */
    .universal-back-bar {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
    }
    .btn-back {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: 9999px;
      padding: 8px 16px;
      font-size: 13px;
      font-weight: 700;
      color: var(--c-night);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      box-shadow: var(--shadow-sm);
      transition: all 0.15s ease;
      font-family: var(--font-sans);
    }
    .btn-back:hover {
      border-color: var(--c-crimson);
      color: var(--c-crimson);
      transform: translateX(-3px);
    }

    /* Top Sticky Navbar */
    .main-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1.5px solid var(--c-border);
      transition: all 0.2s ease;
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
    }
    .brand-logo-box {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--c-crimson), #B91C1C);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      box-shadow: 0 4px 12px rgba(248, 51, 60, 0.3);
    }
    .brand-title {
      font-size: 22px;
      font-weight: 900;
      color: var(--c-night);
      letter-spacing: -0.03em;
    }
    .brand-title span {
      color: var(--c-crimson);
    }

    .nav-menu-links {
      display: flex;
      align-items: center;
      gap: 28px;
    }
    @media (max-width: 900px) {
      .nav-menu-links { display: none; }
    }
    .nav-menu-btn {
      background: none;
      border: none;
      font-size: 14.5px;
      font-weight: 600;
      color: var(--c-body);
      cursor: pointer;
      padding: 6px 0;
      transition: color 0.15s ease;
      font-family: var(--font-sans);
    }
    .nav-menu-btn:hover {
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
      font-family: var(--font-sans);
    }
    .btn-crimson:hover {
      background: var(--c-crimson-hover);
      transform: translateY(-1.5px);
      box-shadow: 0 12px 28px -4px rgba(248, 51, 60, 0.45);
    }
    .btn-crimson:active {
      transform: translateY(0);
    }

    .btn-outline {
      background: #FFFFFF;
      color: var(--c-night);
      font-size: 14px;
      font-weight: 600;
      padding: 9px 20px;
      border-radius: 9999px;
      border: 1.5px solid var(--c-border);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.15s ease;
      font-family: var(--font-sans);
    }
    .btn-outline:hover {
      border-color: var(--c-night);
      background: var(--c-surface-warm);
    }

    /* Screen Views */
    .app-screen-view {
      display: none;
      position: relative;
      z-index: 1;
    }
    .app-screen-view.active {
      display: block;
      animation: fadeInView 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes fadeInView {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ============================================================
       VIEW 1: LUXURY CLEAN LANDING PAGE
       ============================================================ */
    .hero-wrap {
      max-width: 1240px;
      margin: 0 auto;
      padding: 56px 24px 72px 24px;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 52px;
      align-items: center;
    }
    @media (max-width: 960px) {
      .hero-grid {
        grid-template-columns: 1fr;
        gap: 36px;
      }
    }

    .hero-pill-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 9999px;
      background: var(--c-tint-sage);
      border: 1px solid var(--c-border-mint);
      color: var(--c-night);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.04em;
      margin-bottom: 20px;
      box-shadow: var(--shadow-sm);
    }
    .hero-live-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--c-lime);
      box-shadow: 0 0 8px rgba(202, 255, 10, 0.9);
      border: 1px solid rgba(0, 4, 17, 0.2);
    }

    .hero-h1 {
      font-size: 50px;
      font-weight: 900;
      line-height: 1.12;
      letter-spacing: -0.03em;
      color: var(--c-night);
      margin-bottom: 20px;
    }
    @media (max-width: 640px) {
      .hero-h1 { font-size: 36px; }
    }
    .hero-h1 em {
      font-family: var(--font-serif);
      font-style: italic;
      color: var(--c-crimson);
      font-weight: 700;
    }

    .hero-p {
      font-size: 17px;
      line-height: 1.65;
      color: var(--c-body);
      margin-bottom: 30px;
      max-width: 560px;
    }

    /* 3 Core Celebration Switcher Bar (Wedding, Birthday, Housewarming) */
    .core-switcher-bar {
      display: flex;
      gap: 8px;
      margin-bottom: 28px;
      flex-wrap: wrap;
    }
    .core-switch-btn {
      padding: 9px 18px;
      border-radius: 9999px;
      border: 1.5px solid var(--c-border);
      background: #FFFFFF;
      font-size: 13.5px;
      font-weight: 700;
      color: var(--c-body);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      font-family: var(--font-sans);
    }
    .core-switch-btn.active {
      background: var(--c-crimson);
      border-color: var(--c-crimson);
      color: #FFFFFF;
    }

    /* Realistic Interactive Showcase Card */
    .showcase-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: 28px;
      overflow: hidden;
      box-shadow: var(--shadow-xl);
      transition: transform 0.3s ease;
    }
    .showcase-card:hover {
      transform: translateY(-3px);
    }
    .showcase-photo-box {
      position: relative;
      width: 100%;
      height: 230px;
      overflow: hidden;
    }
    .showcase-photo {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }
    .showcase-card:hover .showcase-photo {
      transform: scale(1.05);
    }
    .showcase-photo-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(0, 4, 17, 0.1) 0%, rgba(0, 4, 17, 0.8) 100%);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 22px;
      color: #FFFFFF;
    }

    .showcase-body {
      padding: 24px;
    }
    .metrics-2x2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 20px;
    }
    .metric-item {
      background: var(--c-surface-warm);
      border: 1px solid var(--c-border);
      border-radius: 14px;
      padding: 12px 14px;
    }
    .metric-caption {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--c-muted);
      margin-bottom: 4px;
      font-family: var(--font-sans);
    }
    .metric-number {
      font-size: 20px;
      font-weight: 800;
      color: var(--c-night);
      font-family: var(--font-mono);
    }

    .live-ticker-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 14px;
      border: 1px solid var(--c-border);
      border-radius: 12px;
      background: #FFFFFF;
      margin-bottom: 8px;
      box-shadow: var(--shadow-xs);
    }

    /* Bento Features */
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
    .sec-badge {
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--c-crimson);
      margin-bottom: 8px;
    }
    .sec-heading {
      font-size: 36px;
      font-weight: 900;
      letter-spacing: -0.02em;
      color: var(--c-night);
      margin-bottom: 12px;
    }
    .sec-caption {
      font-size: 16px;
      color: var(--c-body);
      line-height: 1.6;
    }

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
      border: 1.5px solid var(--c-border);
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
      border-color: var(--c-tint-mint);
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
      color: var(--c-night);
      margin-bottom: 8px;
    }
    .bento-desc {
      font-size: 14px;
      color: var(--c-body);
      line-height: 1.6;
    }

    /* 3 Pillars Gallery */
    .celebrations-3col-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }
    @media (max-width: 960px) {
      .celebrations-3col-grid { grid-template-columns: 1fr; }
    }
    .cel-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: 24px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
    }
    .cel-card:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
      border-color: var(--c-tint-mint);
    }
    .cel-photo {
      width: 100%;
      height: 180px;
      object-fit: cover;
    }
    .cel-body {
      padding: 24px;
    }

    /* Comparison Table */
    .comparison-wrap {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: 24px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }
    .comp-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .comp-table th, .comp-table td {
      padding: 16px 24px;
      border-bottom: 1px solid var(--c-border);
      font-size: 14px;
    }
    .comp-table th {
      background: var(--c-surface-warm);
      font-weight: 800;
      color: var(--c-night);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .comp-table tr:last-child td {
      border-bottom: none;
    }

    /* FAQ */
    .faq-container {
      max-width: 800px;
      margin: 0 auto;
    }
    .faq-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: 16px;
      margin-bottom: 12px;
      overflow: hidden;
      transition: border-color 0.15s ease;
    }
    .faq-card:hover {
      border-color: var(--c-periwinkle);
    }
    .faq-q {
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 15.5px;
      font-weight: 700;
      color: var(--c-night);
      cursor: pointer;
      user-select: none;
    }
    .faq-a {
      padding: 0 24px 18px 24px;
      font-size: 14px;
      color: var(--c-body);
      line-height: 1.6;
      display: none;
    }
    .faq-card.open .faq-a { display: block; }
    .faq-card.open .faq-arrow { transform: rotate(180deg); }
    .faq-arrow { transition: transform 0.2s ease; color: var(--c-muted); }

    /* ============================================================
       VIEW 2: DEDICATED FULL-PAGE SIGN-IN (SPLIT LUXURY)
       ============================================================ */
    .login-container {
      max-width: 960px;
      margin: 36px auto 60px auto;
      padding: 0 24px;
    }
    .login-split-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: 28px;
      overflow: hidden;
      box-shadow: var(--shadow-xl);
      display: grid;
      grid-template-columns: 1fr 1fr;
    }
    @media (max-width: 768px) {
      .login-split-card { grid-template-columns: 1fr; }
      .login-left-panel { display: none; }
    }
    .login-left-panel {
      background: linear-gradient(135deg, var(--c-tint-sage) 0%, var(--c-tint-rose) 100%);
      border-right: 1.5px solid var(--c-border);
      padding: 48px 36px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .login-right-panel {
      padding: 48px 36px;
    }

    .form-group {
      margin-bottom: 18px;
    }
    .form-label {
      display: block;
      font-size: 13px;
      font-weight: 700;
      color: var(--c-night);
      margin-bottom: 6px;
      font-family: var(--font-sans);
    }
    .form-input {
      width: 100%;
      padding: 12px 14px;
      border: 1.5px solid var(--c-border);
      border-radius: 12px;
      font-size: 14px;
      font-family: inherit;
      color: var(--c-night);
      background: #FFFFFF;
      transition: all 0.15s ease;
    }
    .form-input:focus {
      outline: none;
      border-color: var(--c-crimson);
      box-shadow: 0 0 0 3px rgba(248, 51, 60, 0.12);
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
      border: 1.5px solid var(--c-border);
      border-radius: 12px;
      background: #FFFFFF;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: var(--font-sans);
    }
    .role-pill.active {
      border-color: var(--c-crimson);
      background: var(--c-crimson-bg);
      color: var(--c-crimson);
      font-weight: 700;
    }

    /* ============================================================
       VIEW 3: EVENT SELECTION & HUB (SGUNMS.IN INSPIRED)
       ============================================================ */
    .hub-container {
      max-width: 1100px;
      margin: 32px auto 60px auto;
      padding: 0 24px;
    }
    .hub-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 28px;
      flex-wrap: wrap;
      gap: 16px;
    }
    .event-cards-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    @media (max-width: 900px) {
      .event-cards-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .event-cards-grid { grid-template-columns: 1fr; }
    }
    .event-entry-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: 24px;
      padding: 24px;
      box-shadow: var(--shadow-sm);
      cursor: pointer;
      transition: all 0.25s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 220px;
    }
    .event-entry-card:hover {
      border-color: var(--c-crimson);
      transform: translateY(-3px);
      box-shadow: var(--shadow-lg);
    }
    .create-new-card {
      border: 2px dashed var(--c-periwinkle);
      background: var(--c-surface-warm);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      min-height: 220px;
    }
    .create-new-card:hover {
      border-color: var(--c-crimson);
      background: var(--c-crimson-bg);
    }

    /* ============================================================
       VIEW 4: IN-APP COMPLETE WORKSPACE
       ============================================================ */
    .workspace-shell {
      max-width: 1280px;
      margin: 0 auto;
      padding: 24px;
    }
    .top-action-bar {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: 20px;
      padding: 16px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }

    .subnav-tabs {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 6px;
      margin-bottom: 24px;
      border-bottom: 1.5px solid var(--c-border);
    }
    .subnav-tab-btn {
      padding: 10px 18px;
      border: none;
      background: none;
      font-size: 14px;
      font-weight: 600;
      color: var(--c-muted);
      cursor: pointer;
      border-bottom: 2.5px solid transparent;
      margin-bottom: -1.5px;
      white-space: nowrap;
      transition: all 0.15s ease;
      font-family: var(--font-sans);
    }
    .subnav-tab-btn.active {
      color: var(--c-crimson);
      border-bottom-color: var(--c-crimson);
      font-weight: 700;
    }

    .tab-panel {
      display: none;
    }
    .tab-panel.active {
      display: block;
      animation: fadeInView 0.2s ease;
    }

    /* Munshi Desk Coins */
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
      background: var(--c-crimson-bg);
      color: var(--c-crimson);
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      transition: all 0.15s ease;
      font-family: var(--font-mono);
    }
    .coin-chip:hover {
      background: var(--c-crimson);
      color: #FFFFFF;
    }

    /* Ledger Table */
    .ledger-box-wrap {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
      border-radius: 20px;
      overflow-x: auto;
      box-shadow: var(--shadow-sm);
    }
    .app-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .app-table th, .app-table td {
      padding: 14px 18px;
      border-bottom: 1px solid var(--c-border);
      font-size: 13.5px;
    }
    .app-table th {
      background: var(--c-surface-warm);
      font-weight: 800;
      color: var(--c-night);
      font-size: 11.5px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      font-family: var(--font-sans);
    }

    /* Modal Backdrop */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 4, 17, 0.6);
      backdrop-filter: blur(8px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-sheet {
      background: #FFFFFF;
      border: 1.5px solid var(--c-border);
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

    /* Toast */
    .toast-box {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--c-night);
      color: #FFFFFF;
      padding: 12px 22px;
      border-radius: 12px;
      font-size: 14px;
      font-weight: 600;
      box-shadow: var(--shadow-xl);
      display: none;
      z-index: 9999;
      animation: slideUp 0.3s ease;
      font-family: var(--font-sans);
    }
    @keyframes slideUp {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
  </style>
</head>
<body>

  <div class="ambient-top"></div>
  <div class="ambient-bottom"></div>

  <!-- ============================================================
       TOP STICKY NAVBAR
       ============================================================ -->
  <header class="main-nav">
    <div class="nav-container">
      <div class="brand-group" onclick="navToView('landing')">
        <div class="brand-logo-box">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
          </svg>
        </div>
        <div class="brand-title">Gift<span>Vault</span></div>
      </div>

      <nav class="nav-menu-links">
        <button type="button" class="nav-menu-btn" onclick="navToView('landing')">Home</button>
        <button type="button" class="nav-menu-btn" onclick="scrollToAnchor('features-sec')">Features</button>
        <button type="button" class="nav-menu-btn" onclick="scrollToAnchor('celebrations-sec')">Celebrations</button>
        <button type="button" class="nav-menu-btn" onclick="scrollToAnchor('comparison-sec')">Comparison</button>
        <button type="button" class="nav-menu-btn" onclick="scrollToAnchor('faq-sec')">FAQ</button>
      </nav>

      <div style="display: flex; gap: 10px; align-items: center;">
        <button type="button" class="btn-crimson" onclick="navToView('login')">
          Sign In →
        </button>
      </div>
    </div>
  </header>

  <!-- ============================================================
       VIEW 1: LUXURY CLEAN LANDING PAGE
       ============================================================ -->
  <main id="view-landing" class="app-screen-view active">
    
    <!-- Hero Section -->
    <section class="hero-wrap">
      <div class="hero-grid">
        <div>
          <div class="hero-pill-badge">
            <span class="hero-live-dot"></span>
            <span>Auspicious Family Shagun & Celebration Treasury</span>
          </div>

          <h1 class="hero-h1">
            The Digital Ledger for Every Family <em>Celebration</em>.
          </h1>

          <p class="hero-p">
            Organize weddings, barasala birthdays, and housewarmings with effortless precision. Record cash, gold, and UPI blessings with instant WhatsApp receipts and complete reciprocity analytics.
          </p>

          <!-- Core 3 Celebrations Switcher -->
          <div class="core-switcher-bar">
            <button type="button" class="core-switch-btn active" onclick="switchHeroCore('wedding', this)">💍 Wedding (Vivaha / Nikah)</button>
            <button type="button" class="core-switch-btn" onclick="switchHeroCore('birthday', this)">🎂 Birthday & Barasala</button>
            <button type="button" class="core-switch-btn" onclick="switchHeroCore('housewarming', this)">🏡 Housewarming (Griha Pravesh)</button>
          </div>

          <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 30px;">
            <button type="button" class="btn-crimson" style="padding: 13px 28px; font-size: 15px;" onclick="navToView('login')">
              Sign In to Vault →
            </button>
            <button type="button" class="btn-outline" style="padding: 13px 24px; font-size: 15px;" onclick="scrollToAnchor('features-sec')">
              Explore Capabilities
            </button>
          </div>

          <div style="font-size: 13.5px; color: var(--c-muted); display: flex; align-items: center; gap: 8px;">
            <span>🌍</span>
            <span>Trusted by South Asian families worldwide • Free for personal celebrations</span>
          </div>
        </div>

        <!-- Realistic Interactive Showcase Card -->
        <div class="showcase-card">
          <div class="showcase-photo-box">
            <img id="hero-showcase-img" src="https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=85" alt="Celebration" class="showcase-photo">
            <div class="showcase-photo-overlay">
              <div style="font-size: 18px; font-weight: 800; font-family: var(--font-sans);" id="hero-showcase-title">Rahul & Snigdha Wedding Celebration</div>
              <div style="font-size: 12.5px; opacity: 0.9;" id="hero-showcase-venue">Gachibowli, Hyderabad • Live Shagun Vault</div>
            </div>
          </div>

          <div class="showcase-body">
            <div class="metrics-2x2">
              <div class="metric-item">
                <div class="metric-caption">Total Blessings</div>
                <div class="metric-number" id="hero-inflow" style="color: var(--c-crimson);">₹8,42,116</div>
              </div>
              <div class="metric-item">
                <div class="metric-caption">Event Expenses</div>
                <div class="metric-number" id="hero-expenses">₹4,15,000</div>
              </div>
              <div class="metric-item">
                <div class="metric-caption">Net Surplus</div>
                <div class="metric-number" id="hero-surplus" style="color: var(--c-emerald);">+₹4,27,116</div>
              </div>
              <div class="metric-item">
                <div class="metric-caption">Gold & Silver</div>
                <div class="metric-number" id="hero-jewels">42.5g / 550g</div>
              </div>
            </div>

            <div style="font-size: 11.5px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; color: var(--c-muted); margin-bottom: 8px; font-family: var(--font-sans);">
              Live Reception Desk Feed
            </div>
            <div class="live-ticker-row">
              <div>
                <div style="font-weight: 700; font-size: 13.5px; color: var(--c-night);">Venkat Rao Garu</div>
                <div style="font-size: 11px; color: var(--c-muted);">Vijayawada • Relatives</div>
              </div>
              <div style="font-weight: 800; font-size: 15px; color: var(--c-crimson); font-family: var(--font-mono);">+ ₹10,116</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Bento Features Section -->
    <section id="features-sec" class="section-wrap" style="background: #FFFFFF; border-top: 1.5px solid var(--c-border);">
      <div class="section-center-head">
        <div class="sec-badge">CORE CAPABILITIES</div>
        <h2 class="sec-heading">Engineered for the Reception Desk</h2>
        <p class="sec-caption">Eliminate lost paper diaries, handwriting confusion, and awkward calculation mistakes forever.</p>
      </div>

      <div class="bento-grid">
        <div class="bento-card">
          <div>
            <div class="bento-tag">SPEED OPTIMIZED</div>
            <h3 class="bento-title">⚡ 3-Second Munshi Desk</h3>
            <p class="bento-desc">Rapid counter entry designed specifically for crowded receptions. Autocomplete guest cities and add +₹1 lucky coin rounding instantly.</p>
          </div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-tag">RECIPROCITY TRACKER</div>
            <h3 class="bento-title">🔄 Smart Gift History</h3>
            <p class="bento-desc">"How much did they give us last time? How much should we give them back?" Instant relationship history and return gift suggestions.</p>
          </div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-tag">COMPLETE RECORD</div>
            <h3 class="bento-title">📖 Digital Red Notebook</h3>
            <p class="bento-desc">The modern version of traditional Erra Pusthakam / Shagun Diary. Search by city, guest name, or amount with zero mathematical errors.</p>
          </div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-tag">COURTESY ACKNOWLEDGEMENT</div>
            <h3 class="bento-title">📲 WhatsApp Digital Receipts</h3>
            <p class="bento-desc">Send a polite, elegant digital acknowledgement card directly to the guest’s WhatsApp number the moment an entry is saved.</p>
          </div>
        </div>

        <div class="bento-card">
          <div>
            <div class="bento-tag">VERIFIED TRANSFERS</div>
            <h3 class="bento-title">🔔 Dynamic UPI Soundbox</h3>
            <p class="bento-desc">Display a personalized UPI QR code on the desk. When guests scan and transfer blessings, an audio chime confirms the payment.</p>
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

    <!-- 3 Core Celebrations Gallery Section with Verified Images -->
    <section id="celebrations-sec" class="section-wrap">
      <div class="section-center-head">
        <div class="sec-badge">VERSATILITY & FOCUS</div>
        <h2 class="sec-heading">The 3 Pillars of Family Celebrations</h2>
        <p class="sec-caption">While GiftVault supports every custom milestone, our core experience is tailored to these major life events.</p>
      </div>

      <div class="celebrations-3col-grid">
        <div class="cel-card">
          <img src="https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=1200&q=85" alt="Wedding" class="cel-photo">
          <div class="cel-body">
            <h3 style="font-size: 18px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;">💍 Weddings (Vivaha / Nikah)</h3>
            <p style="font-size: 14px; color: var(--c-muted); line-height: 1.6;">
              Manage thousands of entries across sangeet, reception, and wedding ceremonies with multi-counter sync.
            </p>
          </div>
        </div>

        <div class="cel-card">
          <img src="https://images.unsplash.com/photo-1513151233558-d860c5398176?auto=format&fit=crop&w=1200&q=85" alt="Birthday" class="cel-photo">
          <div class="cel-body">
            <h3 style="font-size: 18px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;">🎂 Birthday & Barasala</h3>
            <p style="font-size: 14px; color: var(--c-muted); line-height: 1.6;">
              Cradle ceremonies, naming festivities, and milestone 1st birthdays. Keep permanent records of gold chains, toys, and cash.
            </p>
          </div>
        </div>

        <div class="cel-card">
          <img src="https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=1200&q=85" alt="Housewarming" class="cel-photo">
          <div class="cel-body">
            <h3 style="font-size: 18px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;">🏡 Housewarming (Griha Pravesh)</h3>
            <p style="font-size: 14px; color: var(--c-muted); line-height: 1.6;">
              Bless your new home with illuminated celebration. Keep a permanent digital record of all family and neighbour blessings.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Comparison Table -->
    <section id="comparison-sec" class="section-wrap" style="background: #FFFFFF; border-top: 1.5px solid var(--c-border);">
      <div class="section-center-head">
        <div class="sec-badge">TRANSPARENT COMPARISON</div>
        <h2 class="sec-heading">Manual Paper Red Notebook vs GiftVault</h2>
      </div>

      <div class="comparison-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Traditional Paper Ledger</th>
              <th style="color: var(--c-crimson);">GiftVault Digital Ledger</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Entry Speed</strong></td>
              <td style="color: var(--c-muted);">Slow, handwriting legibility issues</td>
              <td style="color: var(--c-emerald); font-weight: 800;">⚡ 3 seconds with auto-complete</td>
            </tr>
            <tr>
              <td><strong>Disaster Protection</strong></td>
              <td style="color: var(--c-muted);">Easily lost, damaged by spills or water</td>
              <td style="color: var(--c-emerald); font-weight: 800;">🔒 Cloud synced & exportable to Excel</td>
            </tr>
            <tr>
              <td><strong>Guest Acknowledgement</strong></td>
              <td style="color: var(--c-muted);">None (pure verbal thank you)</td>
              <td style="color: var(--c-emerald); font-weight: 800;">📲 Instant WhatsApp digital card</td>
            </tr>
            <tr>
              <td><strong>Return Gift Calculation</strong></td>
              <td style="color: var(--c-muted);">Hours spent searching old handwritten notes</td>
              <td style="color: var(--c-emerald); font-weight: 800;">🔄 Automatic reciprocity recommendation</td>
            </tr>
            <tr>
              <td><strong>Net Financial Surplus</strong></td>
              <td style="color: var(--c-muted);">Manual calculator math prone to mistakes</td>
              <td style="color: var(--c-emerald); font-weight: 800;">📊 Real-time revenue vs expense balance</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- FAQ Accordion -->
    <section id="faq-sec" class="section-wrap">
      <div class="section-center-head">
        <div class="sec-badge">CLARITY FIRST</div>
        <h2 class="sec-heading">Frequently Asked Questions</h2>
      </div>

      <div class="faq-container">
        <div class="faq-card open">
          <div class="faq-q" onclick="toggleFaq(this)">
            <span>Can I create events for other community ceremonies (e.g. Tonsure, Half Saree, Dhoti)?</span>
            <span class="faq-arrow">▼</span>
          </div>
          <div class="faq-a">
            Yes! Once you sign in, our Event Hub allows you to create Wedding, Birthday, Tonsure (Mundan / Khatna / Odugu), Half Saree (Pushpalankarana), Dhoti Ceremony (Upanayanam), Housewarming, or any Custom Event with your own title.
          </div>
        </div>

        <div class="faq-card">
          <div class="faq-q" onclick="toggleFaq(this)">
            <span>Does Desk Mode work when wedding hall WiFi is unstable?</span>
            <span class="faq-arrow">▼</span>
          </div>
          <div class="faq-a">
            Yes. All entries are cached in local browser storage without interruption, and you can export your Excel spreadsheet at any time.
          </div>
        </div>

        <div class="faq-card">
          <div class="faq-q" onclick="toggleFaq(this)">
            <span>Is GiftVault free for our family celebration?</span>
            <span class="faq-arrow">▼</span>
          </div>
          <div class="faq-a">
            Yes, personal family events are 100% free forever, with unlimited entries and exports.
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer style="background: #FFFFFF; border-top: 1.5px solid var(--c-border); padding: 56px 24px 32px 24px;">
      <div style="max-width: 1240px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
        <div class="brand-group">
          <div class="brand-logo-box" style="width: 32px; height: 32px;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          </div>
          <div class="brand-title" style="font-size: 18px;">Gift<span>Vault</span></div>
        </div>
        <div style="font-size: 13.5px; color: var(--c-muted);">
          © 2026 GiftVault Inc. The Modern Red Notebook for South Asian Celebrations.
        </div>
      </div>
    </footer>
  </main>

  <!-- ============================================================
       VIEW 2: DEDICATED FULL-PAGE SIGN-IN (SPLIT LUXURY)
       ============================================================ -->
  <main id="view-login" class="app-screen-view">
    <div class="login-container">
      
      <!-- Back Navigation Button -->
      <div class="universal-back-bar">
        <button type="button" class="btn-back" onclick="navToView('landing')">
          ← Back to Home
        </button>
      </div>

      <div class="login-split-card">
        <!-- Banner Side -->
        <div class="login-left-panel">
          <div>
            <div class="bento-tag" style="background: #FFFFFF; padding: 4px 10px; border-radius: 9999px; display: inline-block;">
              256-BIT ENCRYPTION
            </div>
            <h2 style="font-size: 28px; font-weight: 800; color: var(--c-night); margin: 16px 0 12px 0; line-height: 1.25;">
              Welcome to Your Family Vault
            </h2>
            <p style="font-size: 14.5px; color: var(--c-body); line-height: 1.6;">
              Sign in as the Host Family Admin to oversee all accounts, or as the Munshi Desk Cashier for high-speed counter entries.
            </p>
          </div>

          <div style="border-top: 1px solid var(--c-crimson-border); padding-top: 20px;">
            <div style="font-size: 12px; font-weight: 800; color: var(--c-crimson); text-transform: uppercase; margin-bottom: 4px;">Zero Leakage Policy</div>
            <div style="font-size: 13px; color: var(--c-muted);">Your auspicious family ledgers remain strictly confidential.</div>
          </div>
        </div>

        <!-- Form Side -->
        <div class="login-right-panel">
          <div style="margin-bottom: 24px;">
            <h3 style="font-size: 22px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">Sign In</h3>
            <p style="font-size: 13px; color: var(--c-muted);">Access your family events via Phone OTP or Google.</p>
          </div>

          <!-- Role Selector -->
          <div class="form-group">
            <label class="form-label">Select Your Role</label>
            <div class="role-pills">
              <div class="role-pill active" onclick="setLoginRole('admin', this)">👑 Host Admin</div>
              <div class="role-pill" onclick="setLoginRole('munshi', this)">⚡ Munshi Cashier</div>
              <div class="role-pill" onclick="setLoginRole('viewer', this)">👁️ Guest / Viewer</div>
            </div>
          </div>

          <div id="login-phone-box">
            <div class="form-group">
              <label class="form-label">Mobile Number</label>
              <div style="display: flex; gap: 8px;">
                <span style="background: var(--c-surface-warm); border: 1.5px solid var(--c-border); padding: 12px 14px; border-radius: 12px; font-weight: 600; font-size: 14px; font-family: var(--font-mono);">+91</span>
                <input type="tel" id="login-phone-field" class="form-input" placeholder="98480 12345" value="9848012345" maxlength="10">
              </div>
            </div>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 12px; margin-bottom: 16px;" onclick="sendLoginOTP()">
              Send Verification OTP →
            </button>
          </div>

          <div id="login-otp-box" style="display: none;">
            <div class="form-group">
              <label class="form-label">Enter 4-Digit OTP (Test Code: <strong style="color: var(--c-crimson);">1234</strong>)</label>
              <div style="display: flex; gap: 10px; justify-content: center; margin: 12px 0;">
                <input type="text" class="form-input" maxlength="1" value="1" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700; font-family: var(--font-mono);">
                <input type="text" class="form-input" maxlength="1" value="2" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700; font-family: var(--font-mono);">
                <input type="text" class="form-input" maxlength="1" value="3" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700; font-family: var(--font-mono);">
                <input type="text" class="form-input" maxlength="1" value="4" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700; font-family: var(--font-mono);">
              </div>
            </div>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 12px; margin-bottom: 16px;" onclick="verifyAndProceed()">
              Verify & Enter Event Hub ✓
            </button>
          </div>

          <div style="text-align: center; margin: 12px 0; font-size: 12px; color: var(--c-muted);">or</div>

          <button type="button" class="btn-outline" style="width: 100%; justify-content: center; padding: 11px; margin-bottom: 16px;" onclick="verifyAndProceed()">
            <svg width="16" height="16" viewBox="0 0 24 24"><path fill="#EA4335" d="M12 5c1.6 0 3 .6 4.1 1.6l3.1-3.1C17.3 1.7 14.8 1 12 1 7.5 1 3.7 3.6 1.9 7.3l3.7 2.9C6.5 7.4 9 5 12 5z"/><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.7-.2-2.3H12v4.5h6.5c-.3 1.5-1.1 2.8-2.4 3.7l3.7 2.9c2.2-2 3.7-5.1 3.7-8.8z"/><path fill="#FBBC05" d="M5.6 14.8c-.2-.7-.4-1.5-.4-2.3 0-.8.2-1.6.4-2.3L1.9 7.3C.7 9.7 0 12.3 0 15s.7 5.3 1.9 7.7l3.7-2.9z"/><path fill="#34A853" d="M12 23c3.2 0 6-1.1 8-3l-3.7-2.9c-1.1.7-2.5 1.2-4.3 1.2-3 0-5.5-2.4-6.4-5.2L1.9 16c1.8 3.7 5.6 7 10.1 7z"/></svg>
            Sign in with Google
          </button>
        </div>
      </div>
    </div>
  </main>

  <!-- ============================================================
       VIEW 3: EVENT SELECTION & HUB (SGUNMS.IN INSPIRED)
       ============================================================ -->
  <main id="view-hub" class="app-screen-view">
    <div class="hub-container">
      
      <!-- Back Navigation Button -->
      <div class="universal-back-bar">
        <button type="button" class="btn-back" onclick="navToView('login')">
          ← Back to Sign In
        </button>
      </div>

      <div class="hub-header">
        <div>
          <div class="bento-tag">WELCOME TO YOUR FAMILY HUB</div>
          <h2 style="font-size: 28px; font-weight: 900; color: var(--c-night);">Choose Celebration Event</h2>
          <p style="font-size: 14px; color: var(--c-muted);">Select an existing event to open its ledger or create a new celebration.</p>
        </div>

        <button type="button" class="btn-crimson" onclick="openCreateModal()">
          + Create New Event
        </button>
      </div>

      <div class="event-cards-grid" id="hub-cards-grid">
        <!-- Event Cards dynamically populated + Create New Card -->
      </div>
    </div>
  </main>

  <!-- ============================================================
       VIEW 4: IN-APP COMPLETE WORKSPACE
       ============================================================ -->
  <main id="view-app" class="app-screen-view">
    <div class="workspace-shell">
      
      <!-- Back Navigation Button to Hub -->
      <div class="universal-back-bar">
        <button type="button" class="btn-back" onclick="navToView('hub')">
          ← Back to Event Hub
        </button>
      </div>

      <!-- Top Workspace Action Bar -->
      <div class="top-action-bar">
        <div style="display: flex; align-items: center; gap: 14px;">
          <div class="brand-logo-box" style="width: 38px; height: 38px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          </div>
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span id="active-event-title-display" style="font-weight: 800; font-size: 16px; color: var(--c-night);">Active Event</span>
              <span style="background: var(--c-emerald-bg); color: var(--c-emerald); font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 9999px;">LIVE VAULT</span>
            </div>
            <div id="active-event-sub-display" style="font-size: 12px; color: var(--c-muted);">Venue & Type</div>
          </div>
        </div>

        <div style="display: flex; gap: 10px;">
          <button type="button" class="btn-outline" onclick="navToView('hub')" style="padding: 7px 14px; font-size: 13px;">
            ⇄ Switch Event
          </button>
          <button type="button" class="btn-outline" onclick="navToView('landing')" style="padding: 7px 14px; font-size: 13px;">
            Home
          </button>
          <button type="button" class="btn-crimson" onclick="openWorkspaceTab('desk')" style="padding: 7px 16px; font-size: 13px;">
            ⚡ Munshi Desk
          </button>
        </div>
      </div>

      <!-- Sub-Navigation Tabs (8 Functional Modules) -->
      <div class="subnav-tabs">
        <button type="button" class="subnav-tab-btn active" onclick="openWorkspaceTab('dashboard', this)">📊 Dashboard</button>
        <button type="button" class="subnav-tab-btn" onclick="openWorkspaceTab('desk', this)">✍️ Munshi Desk</button>
        <button type="button" class="subnav-tab-btn" onclick="openWorkspaceTab('ledger', this)">📖 Red Notebook (Ledger)</button>
        <button type="button" class="subnav-tab-btn" onclick="openWorkspaceTab('expenses', this)">💸 Expenses & Surplus</button>
        <button type="button" class="subnav-tab-btn" onclick="openWorkspaceTab('reciprocity', this)">🔄 Reciprocity Tracker</button>
        <button type="button" class="subnav-tab-btn" onclick="openWorkspaceTab('soundbox', this)">🔔 UPI QR Soundbox</button>
        <button type="button" class="subnav-tab-btn" onclick="openWorkspaceTab('settings', this)">⚙️ Settings</button>
      </div>

      <!-- TAB 1: DASHBOARD -->
      <div id="panel-dashboard" class="tab-panel active">
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;">
          <div class="metric-item" style="background: #FFFFFF;">
            <div class="metric-caption">Total Blessings</div>
            <div class="metric-number" id="dash-inflow" style="color: var(--c-crimson);">₹0</div>
            <div style="font-size: 11.5px; color: var(--c-muted); margin-top: 4px;">0 entries recorded</div>
          </div>
          <div class="metric-item" style="background: #FFFFFF;">
            <div class="metric-caption">Cash Counter</div>
            <div class="metric-number" id="dash-cash">₹0</div>
            <div style="font-size: 11.5px; color: var(--c-muted); margin-top: 4px;">Envelope collection</div>
          </div>
          <div class="metric-item" style="background: #FFFFFF;">
            <div class="metric-caption">Online UPI</div>
            <div class="metric-number" id="dash-upi">₹0</div>
            <div style="font-size: 11.5px; color: var(--c-muted); margin-top: 4px;">Direct bank credit</div>
          </div>
          <div class="metric-item" style="background: #FFFFFF;">
            <div class="metric-caption">Gold & Silver</div>
            <div class="metric-number" id="dash-jewels">0g / 0g</div>
            <div style="font-size: 11.5px; color: var(--c-muted); margin-top: 4px;">Jewelry offerings</div>
          </div>
        </div>

        <!-- Empty State Prompt -->
        <div id="dash-empty-box" style="text-align: center; padding: 60px 20px; background: #FFFFFF; border: 1.5px dashed var(--c-border); border-radius: 20px;">
          <div style="font-size: 38px; margin-bottom: 12px;">🪙</div>
          <h3 style="font-size: 19px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">Fresh Event Vault Ready</h3>
          <p style="font-size: 14px; color: var(--c-muted); max-width: 440px; margin: 0 auto 20px auto;">
            Zero dummy records. Record your first real guest blessing at the Munshi desk.
          </p>
          <button type="button" class="btn-crimson" onclick="openWorkspaceTab('desk')">+ Record First Blessing</button>
        </div>

        <!-- Recent Records Table -->
        <div id="dash-table-wrap" style="display: none;" class="ledger-box-wrap">
          <table class="app-table">
            <thead>
              <tr>
                <th>Receipt #</th>
                <th>Guest Name</th>
                <th>City / Place</th>
                <th>Amount</th>
                <th>Mode</th>
                <th>WhatsApp</th>
              </tr>
            </thead>
            <tbody id="dash-tbody"></tbody>
          </table>
        </div>
      </div>

      <!-- TAB 2: MUNSHI FAST DESK -->
      <div id="panel-desk" class="tab-panel">
        <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px;">
          <div style="background: #FFFFFF; border: 1.5px solid var(--c-border); border-radius: 20px; padding: 28px;">
            <h3 style="font-size: 18px; font-weight: 800; color: var(--c-night); margin-bottom: 18px;">✍️ Reception Desk Entry</h3>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
              <div class="form-group">
                <label class="form-label">Guest Name *</label>
                <input type="text" id="desk-name" class="form-input" placeholder="e.g. Venkat Rao">
              </div>
              <div class="form-group">
                <label class="form-label">City / Town</label>
                <input type="text" id="desk-city" class="form-input" placeholder="e.g. Hyderabad, Vijayawada">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
              <div class="form-group">
                <label class="form-label">Mobile (for WhatsApp Card)</label>
                <input type="tel" id="desk-phone" class="form-input" placeholder="9848012345">
              </div>
              <div class="form-group">
                <label class="form-label">Relationship / Side</label>
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
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--c-border); border-radius: 12px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="gift-type-mode" value="CASH" checked onchange="toggleGiftType('cash')"> 💵 Cash
                </label>
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--c-border); border-radius: 12px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="gift-type-mode" value="UPI" onchange="toggleGiftType('cash')"> 📲 Online UPI
                </label>
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--c-border); border-radius: 12px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="gift-type-mode" value="GOLD" onchange="toggleGiftType('gold')"> 🥇 Gold/Silver
                </label>
              </div>
            </div>

            <div id="desk-cash-fields" class="form-group">
              <label class="form-label">Amount (INR) *</label>
              <input type="number" id="desk-amount" class="form-input font-mono" style="font-size: 20px; font-weight: 800; color: var(--c-crimson);" placeholder="₹ 1116">
              <div class="coin-group">
                <button type="button" class="coin-chip" onclick="setDeskCoin(516)">+ ₹516</button>
                <button type="button" class="coin-chip" onclick="setDeskCoin(1116)">+ ₹1,116</button>
                <button type="button" class="coin-chip" onclick="setDeskCoin(2116)">+ ₹2,116</button>
                <button type="button" class="coin-chip" onclick="setDeskCoin(5116)">+ ₹5,116</button>
                <button type="button" class="coin-chip" onclick="setDeskCoin(10116)">+ ₹10,116</button>
                <button type="button" class="coin-chip" onclick="addDeskLuckyOne()">+ ₹1 Lucky Coin</button>
              </div>
            </div>

            <div id="desk-gold-fields" class="form-group" style="display: none;">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div>
                  <label class="form-label">Gold Weight (grams)</label>
                  <input type="number" step="0.1" id="desk-gold" class="form-input font-mono" placeholder="e.g. 8.0">
                </div>
                <div>
                  <label class="form-label">Silver Weight (grams)</label>
                  <input type="number" step="1" id="desk-silver" class="form-input font-mono" placeholder="e.g. 100">
                </div>
              </div>
            </div>

            <div style="display: flex; gap: 12px; margin-top: 14px;">
              <button type="button" class="btn-crimson" style="flex: 1; justify-content: center; padding: 13px;" onclick="saveDeskEntry()">
                💾 Save Entry
              </button>
              <button type="button" class="btn-outline" onclick="clearDeskForm()">
                Clear
              </button>
            </div>
          </div>

          <!-- Desk Confirmation & Audio Preview -->
          <div style="background: #FFFFFF; border: 1.5px solid var(--c-border); border-radius: 20px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <h4 style="font-size: 16px; font-weight: 800; color: var(--c-night); margin-bottom: 12px;">
                🔔 Audio Confirmation & Last Receipt
              </h4>
              <p style="font-size: 13.5px; color: var(--c-muted); line-height: 1.6; margin-bottom: 18px;">
                Every saved entry plays a pleasant audio chime to confirm accuracy at the desk.
              </p>

              <div style="background: var(--c-crimson-bg); border: 1px solid var(--c-crimson-border); border-radius: 14px; padding: 16px; margin-bottom: 18px;">
                <div style="font-size: 11.5px; font-weight: 700; color: var(--c-crimson); text-transform: uppercase; margin-bottom: 4px;">Latest Receipt:</div>
                <div id="desk-last-receipt" style="font-size: 14px; font-weight: 700; color: var(--c-night); font-family: var(--font-mono);">No entries recorded yet</div>
              </div>
            </div>

            <button type="button" class="btn-outline" style="width: 100%; justify-content: center;" onclick="playAudioChime(); showAppToast('🔊 Audio soundbox chime tested successfully!');">
              🔊 Test Soundbox Chime
            </button>
          </div>
        </div>
      </div>

      <!-- TAB 3: RED BOOK LEDGER -->
      <div id="panel-ledger" class="tab-panel">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; flex-wrap: wrap; gap: 12px;">
          <div>
            <h3 style="font-size: 20px; font-weight: 800; color: var(--c-night);">📖 Red Notebook (Full Digital Ledger)</h3>
            <p style="font-size: 13px; color: var(--c-muted);">Comprehensive record of all guest offerings and jewelry</p>
          </div>
          <div style="display: flex; gap: 10px;">
            <button type="button" class="btn-outline" onclick="exportCSV()">📥 Download Excel (CSV)</button>
            <button type="button" class="btn-crimson" onclick="window.print()">🖨️ Print Summary</button>
          </div>
        </div>

        <div class="ledger-box-wrap">
          <table class="app-table">
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
                <td colspan="9" style="text-align: center; color: var(--c-muted); padding: 32px;">No records found. Entries made in Desk Mode will appear here.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TAB 4: EXPENSES -->
      <div id="panel-expenses" class="tab-panel">
        <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px;">
          <div style="background: #FFFFFF; border: 1.5px solid var(--c-border); border-radius: 20px; padding: 28px;">
            <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 16px; color: var(--c-night);">💸 Log Event Expense</h3>
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
              <input type="number" id="exp-amount" class="form-input font-mono" placeholder="₹ 50000">
            </div>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 12px;" onclick="saveExpense()">
              + Add Expense Record
            </button>
          </div>

          <div style="background: #FFFFFF; border: 1.5px solid var(--c-border); border-radius: 20px; padding: 28px;">
            <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 16px; color: var(--c-night);">📊 Financial Balance Sheet</h3>
            <div class="metric-item" style="margin-bottom: 12px; background: #FFFFFF;">
              <div class="metric-caption">Total Blessings Inflow</div>
              <div class="metric-number" id="exp-sum-in" style="color: var(--c-crimson);">₹0</div>
            </div>
            <div class="metric-item" style="margin-bottom: 12px; background: #FFFFFF;">
              <div class="metric-caption">Total Event Expenses</div>
              <div class="metric-number" id="exp-sum-out">₹0</div>
            </div>
            <div class="metric-item" style="background: #FFFFFF;">
              <div class="metric-caption">Net Financial Surplus</div>
              <div class="metric-number" id="exp-sum-sur" style="color: var(--c-emerald);">₹0</div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 5: RECIPROCITY -->
      <div id="panel-reciprocity" class="tab-panel">
        <div style="background: #FFFFFF; border: 1.5px solid var(--c-border); border-radius: 20px; padding: 24px; margin-bottom: 20px;">
          <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 8px; color: var(--c-night);">🔄 Reciprocity Intelligence</h3>
          <p style="font-size: 14px; color: var(--c-muted);">
            Preserve family relationships with automated recommendations for return blessings (+₹1 lucky coin standard).
          </p>
        </div>
        <div class="ledger-box-wrap">
          <table class="app-table">
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
                <td colspan="5" style="text-align: center; color: var(--c-muted); padding: 32px;">Recorded guest entries will automatically appear here.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TAB 6: SOUNDBOX QR -->
      <div id="panel-soundbox" class="tab-panel">
        <div style="max-width: 480px; margin: 0 auto; background: #FFFFFF; border: 1.5px solid var(--c-border); border-radius: 24px; padding: 36px; text-align: center; box-shadow: var(--shadow-md);">
          <div class="bento-tag" style="margin-bottom: 14px; display: inline-block;">
            COUNTER SOUNDBOX QR
          </div>
          <h3 style="font-size: 20px; font-weight: 800; margin-bottom: 6px; color: var(--c-night);">Scan to Transfer Blessings</h3>
          <p style="font-size: 13px; color: var(--c-muted); margin-bottom: 20px;">Support for PhonePe, Google Pay, Paytm, and BHIM.</p>

          <div style="background: #FFFFFF; padding: 14px; border: 1.5px solid var(--c-border); border-radius: 16px; display: inline-block; margin-bottom: 18px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=upi://pay?pa=giftvault@hdfcbank&am=1116&cu=INR" alt="UPI QR" style="display: block; border-radius: 8px;">
          </div>

          <div style="font-weight: 800; font-size: 15px; margin-bottom: 4px; color: var(--c-night); font-family: var(--font-mono);">UPI ID: giftvault@hdfcbank</div>
          <div style="font-size: 12.5px; color: var(--c-muted); margin-bottom: 20px;">Counter speaker automatically chimes upon successful transfer</div>

          <button type="button" class="btn-crimson" style="width: 100%; justify-content: center;" onclick="playAudioChime(); showAppToast('🔔 Simulated payment verified with soundbox chime!');">
            🔔 Test Payment Audio
          </button>
        </div>
      </div>

      <!-- TAB 7: SETTINGS -->
      <div id="panel-settings" class="tab-panel">
        <div style="max-width: 600px; margin: 0 auto; background: #FFFFFF; border: 1.5px solid var(--c-border); border-radius: 20px; padding: 28px;">
          <h3 style="font-size: 19px; font-weight: 800; margin-bottom: 18px; color: var(--c-night);">⚙️ Event Settings</h3>
          <div class="form-group">
            <label class="form-label">Active Event Name</label>
            <input type="text" id="setting-title" class="form-input" value="Rahul & Snigdha Wedding Celebration">
          </div>
          <div class="form-group">
            <label class="form-label">Host Contact Mobile</label>
            <input type="tel" id="setting-phone" class="form-input" value="9848012345">
          </div>
          <div style="border-top: 1px solid var(--c-border); padding-top: 20px; margin-top: 20px;">
            <button type="button" class="btn-outline" style="color: var(--c-crimson); border-color: var(--c-crimson-border);" onclick="resetActiveEventData()">
              🗑️ Reset All Data to Fresh ₹0 State
            </button>
          </div>
        </div>
      </div>

    </div>
  </main>

  <!-- ============================================================
       MODAL: CREATE NEW EVENT (COMPREHENSIVE MULTI-MILESTONE)
       ============================================================ -->
  <div id="create-event-modal" class="modal-backdrop">
    <div class="modal-sheet">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <h3 style="font-size: 20px; font-weight: 900; color: var(--c-night);">+ Create New Celebration</h3>
        <button type="button" onclick="closeCreateModal()" style="background: none; border: none; font-size: 22px; cursor: pointer; color: var(--c-muted);">✕</button>
      </div>

      <div class="form-group">
        <label class="form-label">Select Celebration Milestone *</label>
        <select id="modal-event-type" class="form-input" onchange="autoPopulateModal(this.value)">
          <option value="Wedding">💍 Wedding (Vivaha / Nikah)</option>
          <option value="Birthday">🎂 Birthday & Barasala (Naming Ceremony)</option>
          <option value="Tonsure">✂️ Tonsure (Mundan / Khatna / Odugu)</option>
          <option value="Puberty">🪷 Half Saree / Puberty (Pushpalankarana / Langa Voni)</option>
          <option value="Dhoti">🧵 Dhoti Ceremony & Upanayanam (Pancha Function)</option>
          <option value="Housewarming">🏡 Housewarming (Griha Pravesh)</option>
          <option value="Custom">✨ Custom Event (Enter Any Custom Milestone)</option>
        </select>
      </div>

      <div class="form-group">
        <label class="form-label">Event Title *</label>
        <input type="text" id="modal-event-title" class="form-input" placeholder="e.g. Rahul & Snigdha Wedding Celebration" value="Rahul & Snigdha Wedding Celebration">
      </div>

      <div class="form-group">
        <label class="form-label">City / Venue *</label>
        <input type="text" id="modal-event-venue" class="form-input" placeholder="e.g. Gachibowli, Hyderabad" value="Hyderabad">
      </div>

      <div class="form-group">
        <label class="form-label">Celebration Date</label>
        <input type="date" id="modal-event-date" class="form-input" value="2026-11-20">
      </div>

      <div class="form-group">
        <label class="form-label">Host Family / Couple Name</label>
        <input type="text" id="modal-event-host" class="form-input" placeholder="e.g. Rao & Reddy Families">
      </div>

      <div style="display: flex; gap: 12px; margin-top: 24px;">
        <button type="button" class="btn-crimson" style="flex: 1; justify-content: center; padding: 13px;" onclick="confirmCreateEventModal()">
          Create & Open Vault →
        </button>
        <button type="button" class="btn-outline" onclick="closeCreateModal()">
          Cancel
        </button>
      </div>
    </div>
  </div>

  <!-- Global Toast Notification -->
  <div id="app-toast" class="toast-box"></div>

  <!-- Client-side Logic & LocalStorage Persistence -->
  <script>
    // State Store
    let APP_STATE = {
      events: [
        {
          id: 'ev-1',
          type: 'Wedding',
          title: 'Rahul & Snigdha Wedding Celebration',
          venue: 'Hyderabad',
          date: '2026-11-20',
          entries: [],
          expenses: []
        }
      ],
      activeEventId: 'ev-1'
    };

    // Load Local Storage
    try {
      const saved = localStorage.getItem('GIFTVAULT_MASTER_HUB_DATA');
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed.events && parsed.events.length > 0) {
          APP_STATE.events = parsed.events;
          APP_STATE.activeEventId = parsed.activeEventId || parsed.events[0].id;
        }
      }
    } catch(e) {}

    function persistState() {
      try {
        localStorage.setItem('GIFTVAULT_MASTER_HUB_DATA', JSON.stringify(APP_STATE));
      } catch(e) {}
      renderActiveEvent();
      renderHubCards();
    }

    function getActiveEvent() {
      return APP_STATE.events.find(e => e.id === APP_STATE.activeEventId) || APP_STATE.events[0];
    }

    // Navigation Switcher
    function navToView(viewId) {
      document.querySelectorAll('.app-screen-view').forEach(v => v.classList.remove('active'));
      const t = document.getElementById('view-' + viewId);
      if (t) {
        t.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
      if (viewId === 'hub') renderHubCards();
      if (viewId === 'app') renderActiveEvent();
    }

    function openWorkspaceTab(tabId, el) {
      navToView('app');
      document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.subnav-tab-btn').forEach(b => b.classList.remove('active'));
      const p = document.getElementById('panel-' + tabId);
      if (p) p.classList.add('active');
      if (el) el.classList.add('active');
    }

    function scrollToAnchor(id) {
      navToView('landing');
      setTimeout(() => {
        const el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    }

    function showAppToast(msg) {
      const t = document.getElementById('app-toast');
      t.innerText = msg;
      t.style.display = 'block';
      setTimeout(() => { t.style.display = 'none'; }, 2600);
    }

    function toggleFaq(el) {
      el.parentElement.classList.toggle('open');
    }

    // Web Audio Soundbox chime
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

    // 3 Core Celebrations Switcher on Landing
    const CORE_CELEBRATIONS = {
      wedding: {
        title: 'Rahul & Snigdha Wedding Celebration',
        venue: 'Gachibowli, Hyderabad • Live Shagun Vault',
        img: 'https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1200&q=85',
        inflow: '₹8,42,116',
        exp: '₹4,15,000',
        sur: '+₹4,27,116'
      },
      birthday: {
        title: 'Advait 1st Birthday & Barasala Festivity',
        venue: 'Guntur Grand Hall • Live Ledger',
        img: 'https://images.unsplash.com/photo-1513151233558-d860c5398176?auto=format&fit=crop&w=1200&q=85',
        inflow: '₹3,18,116',
        exp: '₹1,20,000',
        sur: '+₹1,98,116'
      },
      housewarming: {
        title: 'Sri Nilayam Griha Pravesh Celebration',
        venue: 'Visakhapatnam • Housewarming Vault',
        img: 'https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=1200&q=85',
        inflow: '₹6,75,116',
        exp: '₹3,10,000',
        sur: '+₹3,65,116'
      }
    };

    function switchHeroCore(key, btn) {
      document.querySelectorAll('.core-switch-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const d = CORE_CELEBRATIONS[key];
      if (d) {
        document.getElementById('hero-showcase-title').innerText = d.title;
        document.getElementById('hero-showcase-venue').innerText = d.venue;
        document.getElementById('hero-showcase-img').src = d.img;
        document.getElementById('hero-inflow').innerText = d.inflow;
        document.getElementById('hero-expenses').innerText = d.exp;
        document.getElementById('hero-surplus').innerText = d.sur;
      }
    }

    // Login logic
    function setLoginRole(role, el) {
      document.querySelectorAll('.role-pill').forEach(p => p.classList.remove('active'));
      if (el) el.classList.add('active');
    }
    function sendLoginOTP() {
      const p = document.getElementById('login-phone-field').value.trim();
      if (!p || p.length < 10) { showAppToast('Please enter a valid 10-digit mobile number.'); return; }
      document.getElementById('login-phone-box').style.display = 'none';
      document.getElementById('login-otp-box').style.display = 'block';
      showAppToast('Verification code 1234 sent!');
    }
    function verifyAndProceed() {
      showAppToast('Sign in verified! Opening Event Hub...');
      setTimeout(() => {
        navToView('hub');
      }, 350);
    }

    // Modal Create Event
    function openCreateModal() {
      document.getElementById('create-event-modal').style.display = 'flex';
    }
    function closeCreateModal() {
      document.getElementById('create-event-modal').style.display = 'none';
    }
    function autoPopulateModal(type) {
      const titleInput = document.getElementById('modal-event-title');
      if (type === 'Wedding') titleInput.value = 'Rahul & Snigdha Wedding Celebration';
      else if (type === 'Birthday') titleInput.value = 'Advait 1st Birthday & Barasala';
      else if (type === 'Tonsure') titleInput.value = 'Ayaan First Tonsure Ceremony (Mundan / Khatna)';
      else if (type === 'Puberty') titleInput.value = 'Sahasra Half Saree (Pushpalankarana) Function';
      else if (type === 'Dhoti') titleInput.value = 'Sai Charan Dhoti Ceremony & Upanayanam';
      else if (type === 'Housewarming') titleInput.value = 'Sri Nilayam Griha Pravesh Function';
      else if (type === 'Custom') titleInput.value = 'Our Family Special Celebration';
    }

    function confirmCreateEventModal() {
      const type = document.getElementById('modal-event-type').value;
      const title = document.getElementById('modal-event-title').value.trim() || 'My Family Celebration';
      const venue = document.getElementById('modal-event-venue').value.trim() || 'Hyderabad';
      const date = document.getElementById('modal-event-date').value || '2026-11-20';

      const newEv = {
        id: 'ev-' + Date.now(),
        type,
        title,
        venue,
        date,
        entries: [],
        expenses: []
      };

      APP_STATE.events.unshift(newEv);
      APP_STATE.activeEventId = newEv.id;
      persistState();

      closeCreateModal();
      showAppToast(`🎉 "${title}" created! Opening vault desk...`);
      openWorkspaceTab('desk');
    }

    // Hub Cards Renderer (sgunms.in inspired)
    function renderHubCards() {
      const grid = document.getElementById('hub-cards-grid');
      let html = '';

      APP_STATE.events.forEach(ev => {
        let tot = 0;
        (ev.entries || []).forEach(e => { tot += e.amount || 0; });
        const isActive = ev.id === APP_STATE.activeEventId;

        html += `
          <div class="event-entry-card" style="${isActive ? 'border-color: var(--c-crimson); background: #FFF;' : ''}" onclick="selectEventFromHub('${ev.id}')">
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <span class="bento-tag" style="margin: 0;">${ev.type}</span>
                ${isActive ? '<span style="background: var(--c-emerald-bg); color: var(--c-emerald); font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 9999px;">ACTIVE</span>' : ''}
              </div>
              <h3 style="font-size: 18px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">${ev.title}</h3>
              <div style="font-size: 13px; color: var(--c-muted);">${ev.venue} • ${ev.date}</div>
            </div>

            <div style="border-top: 1px solid var(--c-border); padding-top: 14px; margin-top: 14px; display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="font-size: 11px; font-weight: 700; color: var(--c-muted); text-transform: uppercase;">Total Collected</div>
                <div style="font-size: 18px; font-weight: 800; color: var(--c-crimson); font-family: var(--font-mono);">₹${tot.toLocaleString('en-IN')}</div>
              </div>
              <button type="button" class="btn-crimson" style="padding: 6px 14px; font-size: 12px;">Open Vault →</button>
            </div>
          </div>
        `;
      });

      // Add '+ Create New Event' Card
      html += `
        <div class="event-entry-card create-new-card" onclick="openCreateModal()">
          <div style="font-size: 36px; color: var(--c-crimson); margin-bottom: 8px;">+</div>
          <h3 style="font-size: 17px; font-weight: 800; color: var(--c-night); margin-bottom: 4px;">Create New Celebration</h3>
          <p style="font-size: 13px; color: var(--c-muted);">Wedding, Birthday, Tonsure, Half Saree, Dhoti, or Custom</p>
        </div>
      `;

      grid.innerHTML = html;
    }

    function selectEventFromHub(id) {
      APP_STATE.activeEventId = id;
      persistState();
      openWorkspaceTab('desk');
    }

    // Munshi Fast Entry Desk
    function setDeskCoin(amt) { document.getElementById('desk-amount').value = amt; }
    function addDeskLuckyOne() {
      const f = document.getElementById('desk-amount');
      let val = parseInt(f.value) || 0;
      f.value = val + (val % 10 === 0 ? 1 : 16);
    }
    function toggleGiftType(m) {
      if (m === 'gold') {
        document.getElementById('desk-cash-fields').style.display = 'none';
        document.getElementById('desk-gold-fields').style.display = 'block';
      } else {
        document.getElementById('desk-cash-fields').style.display = 'block';
        document.getElementById('desk-gold-fields').style.display = 'none';
      }
    }

    function saveDeskEntry() {
      const ev = getActiveEvent();
      const name = document.getElementById('desk-name').value.trim();
      const city = document.getElementById('desk-city').value.trim() || 'Local';
      const phone = document.getElementById('desk-phone').value.trim();
      const rel = document.getElementById('desk-relation').value;
      const mode = document.querySelector('input[name="gift-type-mode"]:checked').value;

      let amount = 0, gold = 0, silver = 0;
      if (mode === 'GOLD') {
        gold = parseFloat(document.getElementById('desk-gold').value) || 0;
        silver = parseFloat(document.getElementById('desk-silver').value) || 0;
        if (gold <= 0 && silver <= 0) { showAppToast('Please enter gold or silver weight.'); return; }
      } else {
        amount = parseInt(document.getElementById('desk-amount').value) || 0;
        if (amount <= 0) { showAppToast('Please enter a valid amount.'); return; }
      }

      if (!name) { showAppToast('Please enter guest name.'); return; }

      const receiptNo = 'GV-' + (100 + (ev.entries || []).length + 1);
      ev.entries.unshift({
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

      persistState();
      playAudioChime();
      document.getElementById('desk-last-receipt').innerText = `${name} (${city}) - ${amount > 0 ? '₹' + amount.toLocaleString('en-IN') : gold + 'g Gold'} [#${receiptNo}]`;
      showAppToast(`Receipt #${receiptNo} recorded!`);
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
      const ev = getActiveEvent();
      const cat = document.getElementById('exp-cat').value;
      const notes = document.getElementById('exp-notes').value.trim();
      const amt = parseInt(document.getElementById('exp-amount').value) || 0;
      if (amt <= 0) { showAppToast('Please enter valid expense amount.'); return; }
      ev.expenses.push({ id: Date.now(), cat, notes, amt });
      persistState();
      showAppToast('Expense recorded successfully!');
      document.getElementById('exp-notes').value = '';
      document.getElementById('exp-amount').value = '';
    }

    function resetActiveEventData() {
      if (confirm('Reset this event to clean ₹0 fresh state?')) {
        const ev = getActiveEvent();
        ev.entries = [];
        ev.expenses = [];
        persistState();
        showAppToast('Event reset to clean ₹0 state!');
      }
    }

    function exportCSV() {
      const ev = getActiveEvent();
      if ((ev.entries || []).length === 0) { showAppToast('No records to export.'); return; }
      let csv = "\uFEFFReceipt,Name,City,Relation,Amount,Gold_g,Silver_g,Mode,Time\n";
      ev.entries.forEach(e => {
        csv += `"${e.receiptNo}","${e.name}","${e.city}","${e.relation}",${e.amount},${e.gold},${e.silver},"${e.mode}","${e.time}"\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `${ev.title.replace(/[^a-zA-Z0-9]/g, '_')}_Ledger_${Date.now()}.csv`;
      a.click();
      showAppToast('Excel CSV download initiated!');
    }

    // Render Active Event in In-App Workspace
    function renderActiveEvent() {
      const ev = getActiveEvent();
      document.getElementById('active-event-title-display').innerText = ev.title;
      document.getElementById('active-event-sub-display').innerText = `${ev.type} • ${ev.venue} • ${ev.date}`;
      document.getElementById('setting-title').value = ev.title;

      let tot = 0, c = 0, u = 0, g = 0, s = 0;
      (ev.entries || []).forEach(e => {
        tot += e.amount || 0;
        if (e.mode === 'CASH') c += e.amount || 0;
        if (e.mode === 'UPI') u += e.amount || 0;
        g += e.gold || 0;
        s += e.silver || 0;
      });

      let expTot = 0;
      (ev.expenses || []).forEach(x => { expTot += x.amt || 0; });
      const surplus = tot - expTot;

      // Dashboard Numbers
      document.getElementById('dash-inflow').innerText = '₹' + tot.toLocaleString('en-IN');
      document.getElementById('dash-cash').innerText = '₹' + c.toLocaleString('en-IN');
      document.getElementById('dash-upi').innerText = '₹' + u.toLocaleString('en-IN');
      document.getElementById('dash-jewels').innerText = `${g}g / ${s}g`;

      // Expenses Numbers
      document.getElementById('exp-sum-in').innerText = '₹' + tot.toLocaleString('en-IN');
      document.getElementById('exp-sum-out').innerText = '₹' + expTot.toLocaleString('en-IN');
      document.getElementById('exp-sum-sur').innerText = (surplus >= 0 ? '+₹' : '-₹') + Math.abs(surplus).toLocaleString('en-IN');

      const emptyPrompt = document.getElementById('dash-empty-box');
      const tableWrap = document.getElementById('dash-table-wrap');
      const dashTbody = document.getElementById('dash-tbody');
      const ledgerTbody = document.getElementById('ledger-tbody');
      const recipTbody = document.getElementById('recip-tbody');

      if ((ev.entries || []).length === 0) {
        emptyPrompt.style.display = 'block';
        tableWrap.style.display = 'none';
        ledgerTbody.innerHTML = '<tr><td colspan="9" style="text-align: center; color: var(--c-muted); padding: 32px;">No records found. Entries made in Desk Mode will appear here.</td></tr>';
        recipTbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: var(--c-muted); padding: 32px;">Recorded guest entries will automatically appear here.</td></tr>';
      } else {
        emptyPrompt.style.display = 'none';
        tableWrap.style.display = 'block';

        let rH = '';
        let lH = '';
        let recH = '';

        ev.entries.forEach((e, idx) => {
          const amtStr = e.amount > 0 ? '₹' + e.amount.toLocaleString('en-IN') : '-';
          const jewelStr = (e.gold > 0 ? e.gold + 'g Gold ' : '') + (e.silver > 0 ? e.silver + 'g Silver' : '') || '-';
          const recAmt = e.amount > 0 ? '₹' + (e.amount + 100).toLocaleString('en-IN') : 'Jewelry';

          rH += `
            <tr>
              <td><strong>#${e.receiptNo}</strong></td>
              <td style="font-weight: 700;">${e.name}</td>
              <td>${e.city}</td>
              <td style="font-weight: 800; color: var(--c-crimson); font-family: var(--font-mono);">${amtStr}</td>
              <td><span style="font-size: 11px; background: var(--c-crimson-bg); color: var(--c-crimson); padding: 3px 8px; border-radius: 6px; font-weight: 700;">${e.mode}</span></td>
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
              <td style="font-weight: 800; color: var(--c-crimson); font-family: var(--font-mono);">${amtStr}</td>
              <td>${jewelStr}</td>
              <td><span style="font-size: 11px; background: var(--c-crimson-bg); color: var(--c-crimson); padding: 3px 8px; border-radius: 6px; font-weight: 700;">${e.mode}</span></td>
              <td><button type="button" class="btn-outline" style="padding: 4px 10px; font-size: 11px;" onclick="alert('Receipt #${e.receiptNo}: ${e.name} - ${amtStr}')">Details</button></td>
            </tr>
          `;

          recH += `
            <tr>
              <td><strong>${e.name}</strong></td>
              <td>${e.city}</td>
              <td style="font-weight: 700;">${amtStr}</td>
              <td style="font-weight: 800; color: var(--c-emerald); font-family: var(--font-mono);">${recAmt}</td>
              <td><span style="color: var(--c-emerald); font-size: 12px; font-weight: 800;">Recommendation Ready</span></td>
            </tr>
          `;
        });

        dashTbody.innerHTML = rH;
        ledgerTbody.innerHTML = lH;
        recipTbody.innerHTML = recH;
      }
    }

    // Initial load
    renderHubCards();
    renderActiveEvent();
  </script>
</body>
</html>
'''

# Synchronize across all targets
for path in ['web_preview/index.html', 'web_preview/desktop.html', 'web_preview/mobile.html', 'build/web/index.html', 'web/index.html']:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(PERFECTED_APP)

print('Synchronized perfected typography, colors, and back buttons across all web files!')
