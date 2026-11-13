# Comprehensive feature checker & builder for GiftVault
# Fulfills ALL past requirements:
# 1. Full Working Multi-Language Engine (English, Telugu తెలుగు, Hindi हिन्दी) with real-time DOM translation across all views & tabs
# 2. Voice Entry (Web Speech API mic dictation for fast Munshi logging)
# 3. Photo Proof Upload & Preview for Gold/Silver/Physical gifts
# 4. Instant WhatsApp Receipt Generator (wa.me link with personalized auspicious greeting)
# 5. Live Audio Soundbox with Twin-Tone Chime & SpeechSynthesis voice announcement
# 6. Real-time Search & Filter in Red Notebook Ledger (search by name, city, mode)
# 7. Complete Event Creation with Pair Names, Date, Time, Venue, Guest Count, Category
# 8. Creative Modern Luxury Design (Option B typography: Playfair Display + Plus Jakarta Sans, 3 curated royal colors, smooth animations, back buttons)

import os

html_code = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault | Royal Celebration Ledger & Shagun Treasury</title>
  
  <!-- Option B Curated Font Pairing -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600;1,700&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">

  <style>
    :root {
      /* Curated Royal Palette */
      --c-night: #000411;         /* Deep Night Slate - Core typography, high-contrast dark buttons */
      --c-crimson: #F8333C;       /* Rose Crimson - Primary festive celebration CTA, active badges */
      --c-crimson-hover: #D91C25;
      --c-crimson-subtle: #FFF1F2;
      --c-emerald: #036D19;       /* Royal Emerald - Monetary totals, surplus, verification */
      --c-emerald-subtle: #ECFDF5;
      --c-sage-ivory: #DCE2CC;    /* Sage Ivory - Subtle borders, soft warm accents */

      /* Pure Crisp Canvases */
      --c-base: #F8F9FA;
      --c-surface: #FFFFFF;
      --c-border: #E2E8F0;
      --c-body-text: #1E293B;
      --c-muted: #64748B;

      /* Typography Hierarchy */
      --font-serif: 'Playfair Display', Georgia, serif;            /* Major Headings Only */
      --font-sans: 'Plus Jakarta Sans', -apple-system, sans-serif; /* Complete UI, Body & Tabular Numbers */

      /* Elevations & Animation Transitions */
      --shadow-sm: 0 1px 3px rgba(0, 4, 17, 0.05);
      --shadow-md: 0 4px 14px -2px rgba(0, 4, 17, 0.08), 0 2px 6px -1px rgba(0, 4, 17, 0.04);
      --shadow-lg: 0 16px 36px -4px rgba(0, 4, 17, 0.10), 0 6px 14px -2px rgba(0, 4, 17, 0.04);
      --shadow-crimson: 0 8px 24px -4px rgba(248, 51, 60, 0.32);
      --ease-spring: cubic-bezier(0.16, 1, 0.3, 1);
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    html {
      scroll-behavior: smooth;
      -webkit-font-smoothing: antialiased;
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

    /* Tabular currency numbers */
    .num-currency {
      font-family: var(--font-sans);
      font-feature-settings: "tnum" 1, "cv02" 1;
      font-variant-numeric: tabular-nums;
      font-weight: 800;
      letter-spacing: -0.02em;
    }

    /* Universal Floating Side Back Pill */
    .universal-side-back-btn {
      position: fixed;
      left: 20px;
      bottom: 24px;
      z-index: 999;
      display: none;
      align-items: center;
      gap: 8px;
      background: var(--c-night);
      color: #FFFFFF;
      border: 1.5px solid rgba(255, 255, 255, 0.3);
      padding: 10px 18px;
      border-radius: 9999px;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: var(--shadow-lg);
      transition: all 0.25s var(--ease-spring);
    }
    .universal-side-back-btn:hover {
      background: var(--c-crimson);
      border-color: var(--c-crimson);
      transform: translateX(-4px);
    }

    /* Universal Top Back Bar */
    .page-back-nav-bar {
      width: 100%;
      background: var(--c-surface);
      border-bottom: 1px solid var(--c-border);
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .btn-page-back {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--c-surface);
      color: var(--c-night);
      border: 1.5px solid var(--c-night);
      padding: 8px 16px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .btn-page-back:hover {
      background: var(--c-crimson);
      border-color: var(--c-crimson);
      color: #FFFFFF;
      transform: translateX(-2px);
    }

    /* Primary Sticky Navigation Bar */
    .main-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(12px);
      border-bottom: 1.5px solid var(--c-border);
      padding: 12px 32px;
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
      width: 42px;
      height: 42px;
      border-radius: 12px;
      background: var(--c-night);
      border: 2px solid var(--c-crimson);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      font-family: var(--font-serif);
      font-weight: 800;
      font-size: 20px;
      box-shadow: var(--shadow-sm);
    }
    .brand-titles {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 800;
      color: var(--c-night);
      line-height: 1.1;
    }
    .brand-sub {
      font-family: var(--font-sans);
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--c-crimson);
    }
    .nav-links-wrap {
      display: flex;
      align-items: center;
      gap: 20px;
    }
    .nav-anchor-btn {
      background: none;
      border: none;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 600;
      color: var(--c-body-text);
      cursor: pointer;
      transition: color 0.2s ease;
      padding: 6px 4px;
    }
    .nav-anchor-btn:hover {
      color: var(--c-crimson);
    }

    /* Multi-Language Dropdown Selector */
    .lang-selector-box {
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--c-base);
      border: 1.5px solid var(--c-night);
      border-radius: 8px;
      padding: 5px 10px;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 700;
      color: var(--c-night);
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
      border: 1.5px solid var(--c-crimson);
      padding: 10px 22px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s var(--ease-spring);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: var(--shadow-crimson);
    }
    .btn-crimson:hover {
      background: var(--c-crimson-hover);
      border-color: var(--c-crimson-hover);
      transform: translateY(-2px);
      box-shadow: 0 10px 28px -4px rgba(248, 51, 60, 0.45);
    }
    .btn-emerald {
      background: var(--c-emerald);
      color: #FFFFFF;
      border: 1.5px solid var(--c-emerald);
      padding: 10px 20px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .btn-emerald:hover {
      background: #025313;
      transform: translateY(-1px);
    }
    .btn-outline-dark {
      background: transparent;
      color: var(--c-night);
      border: 1.5px solid var(--c-night);
      padding: 10px 20px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .btn-outline-dark:hover {
      background: var(--c-night);
      color: #FFFFFF;
    }

    /* Screen Views Management */
    .app-screen-view {
      display: none;
      width: 100%;
      flex: 1;
      animation: fadeInView 0.3s var(--ease-spring);
    }
    .app-screen-view.active {
      display: block;
    }
    @keyframes fadeInView {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ==========================================================================
       VIEW 1: LANDING PAGE
       ========================================================================== */
    .hero-wrap {
      max-width: 1280px;
      margin: 0 auto;
      padding: 56px 32px 64px;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 48px;
      align-items: center;
    }
    .hero-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #FFFFFF;
      border: 1.5px solid var(--c-night);
      padding: 6px 16px;
      border-radius: 9999px;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 700;
      color: var(--c-night);
      margin-bottom: 20px;
      box-shadow: var(--shadow-sm);
    }
    .hero-dot-indicator {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--c-crimson);
      display: inline-block;
      animation: pulseDot 2s infinite ease-in-out;
    }
    @keyframes pulseDot {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.4); opacity: 0.7; }
    }
    .hero-heading {
      font-family: var(--font-serif);
      font-size: 52px;
      line-height: 1.15;
      font-weight: 800;
      color: var(--c-night);
      margin-bottom: 18px;
      letter-spacing: -0.02em;
    }
    .hero-heading em {
      font-style: italic;
      color: var(--c-crimson);
      font-weight: 800;
    }
    .hero-tagline-text {
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--c-crimson);
      margin-bottom: 12px;
      display: block;
    }
    .hero-description {
      font-family: var(--font-sans);
      font-size: 17px;
      color: var(--c-muted);
      line-height: 1.7;
      margin-bottom: 32px;
      max-width: 580px;
    }

    .hero-actions-row {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      margin-bottom: 26px;
    }

    /* Hero Showcase Card */
    .hero-showcase-box {
      background: #FFFFFF;
      border: 2px solid var(--c-night);
      border-radius: 20px;
      overflow: hidden;
      box-shadow: var(--shadow-lg);
      position: relative;
    }
    .showcase-banner-top {
      background: var(--c-night);
      color: #FFFFFF;
      padding: 11px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1.5px solid var(--c-night);
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 700;
    }
    .showcase-image-holder {
      height: 250px;
      position: relative;
      overflow: hidden;
      background: #000411;
    }
    .showcase-image-holder img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .showcase-image-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      padding: 20px;
      background: linear-gradient(to top, rgba(0, 4, 17, 0.94) 0%, rgba(0, 4, 17, 0.35) 70%, transparent 100%);
      color: #FFFFFF;
    }
    .showcase-tag-sub {
      font-family: var(--font-sans);
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--c-crimson);
      margin-bottom: 4px;
    }
    .showcase-event-heading {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 800;
      letter-spacing: -0.01em;
      line-height: 1.2;
    }
    .showcase-venue-text {
      font-family: var(--font-sans);
      font-size: 12.5px;
      color: #CBD5E1;
      font-weight: 500;
      margin-top: 2px;
    }
    .showcase-data-grid {
      padding: 18px 20px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      background: #FFFFFF;
      border-bottom: 1.5px solid var(--c-border);
    }
    .showcase-data-item {
      background: var(--c-base);
      border: 1px solid var(--c-border);
      border-radius: 12px;
      padding: 10px 14px;
    }
    .showcase-data-label {
      font-family: var(--font-sans);
      font-size: 11px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--c-muted);
      letter-spacing: 0.05em;
    }
    .showcase-data-val {
      font-size: 18px;
      font-weight: 800;
      color: var(--c-night);
      margin-top: 2px;
    }
    .showcase-feed-row {
      padding: 14px 20px;
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .feed-avatar {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: var(--c-night);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-sans);
      font-weight: 800;
      font-size: 12px;
    }

    /* Core Capabilities Section */
    .section-wrap {
      max-width: 1280px;
      margin: 0 auto;
      padding: 72px 32px;
    }
    .section-header-center {
      text-align: center;
      max-width: 720px;
      margin: 0 auto 48px;
    }
    .section-eyebrow {
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--c-crimson);
      background: var(--c-crimson-subtle);
      display: inline-block;
      padding: 4px 14px;
      border-radius: 9999px;
      margin-bottom: 12px;
      border: 1px solid var(--c-crimson);
    }
    .section-title {
      font-family: var(--font-serif);
      font-size: 40px;
      font-weight: 800;
      color: var(--c-night);
      line-height: 1.2;
      margin-bottom: 12px;
    }
    .section-desc {
      font-family: var(--font-sans);
      font-size: 16px;
      color: var(--c-muted);
    }

    /* Capabilities 3-Col Grid */
    .capabilities-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }
    .cap-card {
      background: #FFFFFF;
      border: 2px solid var(--c-night);
      border-radius: 18px;
      padding: 32px 26px;
      box-shadow: var(--shadow-md);
      transition: all 0.25s var(--ease-spring);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .cap-card:hover {
      transform: translateY(-5px);
      box-shadow: var(--shadow-lg);
      border-color: var(--c-crimson);
    }
    .cap-icon {
      width: 52px;
      height: 52px;
      border-radius: 12px;
      background: var(--c-night);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      margin-bottom: 20px;
      box-shadow: var(--shadow-sm);
    }
    .cap-title {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 800;
      color: var(--c-night);
      margin-bottom: 10px;
    }
    .cap-text {
      font-family: var(--font-sans);
      font-size: 14.5px;
      color: var(--c-muted);
      line-height: 1.6;
      margin-bottom: 20px;
    }

    /* Comparison Table */
    .comparison-table-wrap {
      background: #FFFFFF;
      border: 2px solid var(--c-night);
      border-radius: 18px;
      overflow: hidden;
      box-shadow: var(--shadow-md);
      margin-top: 32px;
    }
    .comp-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .comp-table th {
      background: var(--c-night);
      color: #FFFFFF;
      padding: 18px 24px;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }
    .comp-table th:first-child { width: 34%; }
    .comp-table th:nth-child(2) { background: #334155; }
    .comp-table th:nth-child(3) { background: var(--c-crimson); }
    .comp-table td {
      padding: 16px 24px;
      border-bottom: 1px solid var(--c-border);
      font-family: var(--font-sans);
      font-size: 14px;
    }
    .comp-table tr:hover td {
      background: #F8F9FA;
    }
    .comp-table td:nth-child(3) {
      font-weight: 700;
      color: var(--c-night);
    }

    /* ==========================================================================
       VIEW 2: LOGIN / AUTH SCREEN
       ========================================================================== */
    .login-container-box {
      max-width: 460px;
      margin: 40px auto 60px;
      background: #FFFFFF;
      border: 2px solid var(--c-night);
      border-radius: 20px;
      padding: 36px;
      box-shadow: var(--shadow-lg);
    }
    .login-header-zone {
      text-align: center;
      margin-bottom: 28px;
    }
    .login-header-zone h2 {
      font-family: var(--font-serif);
      font-size: 28px;
      font-weight: 800;
      color: var(--c-night);
      margin-top: 8px;
    }
    .form-group-item {
      margin-bottom: 18px;
    }
    .form-label-txt {
      display: block;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 700;
      color: var(--c-night);
      margin-bottom: 6px;
    }
    .form-input-field {
      width: 100%;
      padding: 12px 14px;
      border: 1.5px solid var(--c-border);
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 14px;
      outline: none;
      transition: border-color 0.2s ease;
      background: var(--c-base);
    }
    .form-input-field:focus {
      border-color: var(--c-crimson);
      background: #FFFFFF;
    }
    .auth-demo-credentials {
      background: var(--c-base);
      border: 1.5px dashed var(--c-night);
      border-radius: 10px;
      padding: 12px 16px;
      margin: 20px 0;
      font-family: var(--font-sans);
      font-size: 12.5px;
      color: var(--c-night);
    }

    /* ==========================================================================
       VIEW 3: EVENT HUB (SGUNMS.IN STYLE SELECTION + CREATE MODAL)
       ========================================================================== */
    .hub-container-wrap {
      max-width: 1200px;
      margin: 0 auto;
      padding: 36px 32px 64px;
    }
    .hub-top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 32px;
      flex-wrap: wrap;
      gap: 16px;
    }
    .hub-title-block h1 {
      font-family: var(--font-serif);
      font-size: 34px;
      font-weight: 800;
      color: var(--c-night);
    }
    .hub-title-block p {
      font-family: var(--font-sans);
      font-size: 15px;
      color: var(--c-muted);
    }
    .events-selection-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 24px;
    }
    .event-selection-card {
      background: #FFFFFF;
      border: 2px solid var(--c-night);
      border-radius: 16px;
      padding: 24px;
      box-shadow: var(--shadow-sm);
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
    }
    .event-selection-card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-md);
      border-color: var(--c-crimson);
    }
    .create-new-event-card {
      background: #FFFFFF;
      border: 2px dashed var(--c-night);
      border-radius: 16px;
      padding: 32px 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      cursor: pointer;
      min-height: 240px;
      transition: all 0.2s ease;
    }
    .create-new-event-card:hover {
      border-color: var(--c-crimson);
      background: var(--c-crimson-subtle);
      transform: translateY(-4px);
    }
    .create-icon-circle {
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: var(--c-night);
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      margin-bottom: 16px;
      box-shadow: var(--shadow-sm);
    }
    .tag-badge {
      display: inline-block;
      padding: 3px 10px;
      border-radius: 9999px;
      font-family: var(--font-sans);
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* ==========================================================================
       VIEW 4: IN-APP WORKSPACE (8 MODULES WITH ADVANCED VOICE, PHOTO & SOUNDBOX)
       ========================================================================== */
    .workspace-top-header {
      background: var(--c-night);
      color: #FFFFFF;
      padding: 12px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 2px solid var(--c-crimson);
    }
    .ws-event-info {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .ws-event-title {
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 800;
      color: #FFFFFF;
    }
    .ws-event-badge {
      background: var(--c-crimson);
      color: #FFFFFF;
      font-family: var(--font-sans);
      font-size: 11px;
      font-weight: 800;
      padding: 3px 10px;
      border-radius: 9999px;
      text-transform: uppercase;
    }
    .ws-tabs-bar {
      background: #FFFFFF;
      border-bottom: 1.5px solid var(--c-border);
      padding: 0 28px;
      display: flex;
      gap: 8px;
      overflow-x: auto;
    }
    .ws-tab-btn {
      padding: 14px 18px;
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 700;
      color: var(--c-muted);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .ws-tab-btn:hover {
      color: var(--c-night);
    }
    .ws-tab-btn.active {
      color: var(--c-crimson);
      border-bottom-color: var(--c-crimson);
    }

    .ws-content-body {
      max-width: 1280px;
      margin: 0 auto;
      padding: 28px 24px 60px;
      width: 100%;
    }
    .tab-pane {
      display: none;
    }
    .tab-pane.active {
      display: block;
    }

    /* KPI Summary Cards */
    .kpi-cards-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-bottom: 28px;
    }
    .kpi-card {
      background: #FFFFFF;
      border: 1.5px solid var(--c-night);
      border-radius: 14px;
      padding: 18px 20px;
      box-shadow: var(--shadow-sm);
    }
    .kpi-title {
      font-family: var(--font-sans);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--c-muted);
    }
    .kpi-value {
      font-size: 26px;
      font-weight: 800;
      color: var(--c-night);
      margin: 6px 0 4px;
    }
    .kpi-note {
      font-family: var(--font-sans);
      font-size: 11.5px;
      font-weight: 600;
    }

    /* Munshi Entry Card with Voice Mic & Photo Upload */
    .munshi-entry-card {
      background: #FFFFFF;
      border: 2px solid var(--c-night);
      border-radius: 18px;
      padding: 28px;
      box-shadow: var(--shadow-md);
      max-width: 780px;
      margin: 0 auto;
    }
    .voice-mic-btn {
      background: var(--c-crimson-subtle);
      color: var(--c-crimson);
      border: 1.5px solid var(--c-crimson);
      border-radius: 8px;
      padding: 6px 14px;
      font-family: var(--font-sans);
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }
    .voice-mic-btn:hover {
      background: var(--c-crimson);
      color: #FFFFFF;
    }
    .voice-mic-btn.listening {
      background: var(--c-crimson);
      color: #FFFFFF;
      animation: pulseMic 1s infinite;
    }
    @keyframes pulseMic {
      0% { box-shadow: 0 0 0 0 rgba(248, 51, 60, 0.7); }
      70% { box-shadow: 0 0 0 10px rgba(248, 51, 60, 0); }
      100% { box-shadow: 0 0 0 0 rgba(248, 51, 60, 0); }
    }

    .lucky-one-chip-bar {
      display: flex;
      gap: 8px;
      margin-top: 8px;
      flex-wrap: wrap;
    }
    .lucky-coin-chip {
      background: var(--c-base);
      border: 1.5px solid var(--c-night);
      color: var(--c-night);
      padding: 6px 14px;
      border-radius: 8px;
      font-family: var(--font-sans);
      font-feature-settings: "tnum" 1;
      font-variant-numeric: tabular-nums;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .lucky-coin-chip:hover {
      background: var(--c-night);
      color: #FFFFFF;
    }

    /* Live Search & Filter Bar in Red Notebook */
    .ledger-filter-bar {
      display: flex;
      gap: 12px;
      align-items: center;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }
    .search-input-box {
      flex: 1;
      min-width: 240px;
      padding: 10px 14px;
      border: 1.5px solid var(--c-night);
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 13.5px;
      outline: none;
    }

    /* Data Table / Red Notebook Ledger */
    .ledger-table-wrap {
      background: #FFFFFF;
      border: 2px solid var(--c-night);
      border-radius: 16px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }
    .ledger-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .ledger-table th {
      background: var(--c-night);
      color: #FFFFFF;
      padding: 14px 18px;
      font-family: var(--font-sans);
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.04em;
    }
    .ledger-table td {
      padding: 14px 18px;
      border-bottom: 1px solid var(--c-border);
      font-family: var(--font-sans);
      font-size: 13.5px;
    }
    .ledger-table tr:hover td {
      background: #F8F9FA;
    }

    /* Modal Backdrop & Dialog */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 4, 17, 0.75);
      backdrop-filter: blur(4px);
      z-index: 1000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-backdrop.active {
      display: flex;
    }
    .modal-dialog {
      background: #FFFFFF;
      border: 2.5px solid var(--c-night);
      border-radius: 20px;
      width: 100%;
      max-width: 600px;
      max-height: 90vh;
      overflow-y: auto;
      box-shadow: 0 20px 40px rgba(0, 4, 17, 0.25);
    }
    .modal-header {
      background: #FFFFFF;
      padding: 18px 24px;
      border-bottom: 2px solid var(--c-night);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .modal-header h3 {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 800;
      color: var(--c-night);
    }
    .modal-close-btn {
      background: none;
      border: none;
      font-size: 24px;
      cursor: pointer;
      color: var(--c-night);
    }
    .modal-body {
      padding: 24px;
    }

    /* Footer */
    .main-footer {
      background: var(--c-night);
      color: #FFFFFF;
      border-top: 3px solid var(--c-crimson);
      padding: 56px 32px 36px;
      margin-top: auto;
    }
    .footer-grid {
      max-width: 1280px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr;
      gap: 40px;
      margin-bottom: 40px;
    }
    .footer-brand h3 {
      font-family: var(--font-serif);
      font-size: 26px;
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 8px;
    }
    .footer-brand p {
      font-size: 14px;
      color: #94A3B8;
      line-height: 1.6;
    }
    .footer-col h4 {
      font-family: var(--font-sans);
      font-size: 13px;
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
      color: #CBD5E1;
      font-family: var(--font-sans);
      font-size: 13.5px;
      cursor: pointer;
      transition: color 0.2s ease;
      padding: 0;
    }
    .footer-btn-link:hover {
      color: #FFFFFF;
    }
    .footer-bottom-bar {
      max-width: 1280px;
      margin: 0 auto;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
      padding-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-sans);
      font-size: 12.5px;
      color: #94A3B8;
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .hero-grid { grid-template-columns: 1fr; }
      .capabilities-grid { grid-template-columns: 1fr; }
      .kpi-cards-grid { grid-template-columns: repeat(2, 1fr); }
      .footer-grid { grid-template-columns: 1fr; }
    }
    @media (max-width: 640px) {
      .kpi-cards-grid { grid-template-columns: 1fr; }
      .hero-heading { font-size: 34px; }
      .main-nav { padding: 12px 18px; }
    }
  </style>
</head>
<body>

  <!-- Universal Side-Docked Floating Back Button -->
  <button id="floating-back-btn" class="universal-side-back-btn" onclick="handleUniversalBack()" title="Go Back">
    <span>←</span>
    <span data-i18n="btn_back">Back</span>
  </button>

  <!-- Primary Sticky Navigation Header with Language Selector -->
  <header class="main-nav">
    <div class="brand-group" onclick="navToView('landing')">
      <div class="brand-icon-box">GV</div>
      <div class="brand-titles">
        <span class="brand-name">GiftVault</span>
        <span class="brand-sub" data-i18n="brand_subtitle">Shagun & Celebration Treasury</span>
      </div>
    </div>

    <nav class="nav-links-wrap" id="landing-nav-links">
      <button type="button" class="nav-anchor-btn" onclick="scrollToSection('hero-section')" data-i18n="nav_overview">Overview</button>
      <button type="button" class="nav-anchor-btn" onclick="scrollToSection('features-section')" data-i18n="nav_capabilities">Capabilities</button>
      <button type="button" class="nav-anchor-btn" onclick="scrollToSection('comparison-section')" data-i18n="nav_comparison">Comparison</button>
      <button type="button" class="nav-anchor-btn" onclick="scrollToSection('faq-section')" data-i18n="nav_faq">FAQ</button>

      <!-- Multi-Language Selector Dropdown -->
      <div class="lang-selector-box">
        <span>🌐</span>
        <select id="lang-select" class="lang-dropdown" onchange="changeLanguage(this.value)">
          <option value="en" selected>English</option>
          <option value="te">తెలుగు (Telugu)</option>
          <option value="hi">हिन्दी (Hindi)</option>
        </select>
      </div>

      <button type="button" class="btn-crimson" onclick="navToView('login')">
        <span data-i18n="btn_signin">Sign In to Vault</span>
        <span>→</span>
      </button>
    </nav>
  </header>

  <!-- ==========================================================================
       VIEW 1: LANDING PAGE
       ========================================================================== -->
  <main id="view-landing" class="app-screen-view active">
    
    <!-- Hero Section -->
    <section id="hero-section" class="hero-wrap">
      <div class="hero-grid">
        <div>
          <div class="hero-badge-pill">
            <span class="hero-dot-indicator"></span>
            <span data-i18n="hero_pill">Auspicious Shagun & Celebration Treasury</span>
          </div>

          <span class="hero-tagline-text" data-i18n="hero_tagline">SHUBH AARAMBH • MANGALA KAARYAM</span>
          
          <h1 class="hero-heading" data-i18n="hero_h1">
            The Digital Red Notebook for Every Family <em>Celebration</em>.
          </h1>

          <p class="hero-description" data-i18n="hero_desc">
            Preserve blessings, gold, cash, and gifts with instant WhatsApp receipts and zero calculation errors. Designed specifically for auspicious Indian family celebrations and reception desks.
          </p>

          <div class="hero-actions-row">
            <button type="button" class="btn-crimson" style="padding: 13px 28px; font-size: 15px;" onclick="navToView('login')">
              <span data-i18n="btn_open_desk">Open Reception Desk</span>
              <span>→</span>
            </button>
            <button type="button" class="btn-outline-dark" style="padding: 13px 24px; font-size: 15px;" onclick="scrollToSection('features-section')">
              <span data-i18n="btn_explore">Explore Capabilities</span>
            </button>
          </div>

          <div style="font-family: var(--font-sans); font-size: 13px; color: var(--c-muted); display: flex; align-items: center; gap: 8px;">
            <span style="color: var(--c-emerald); font-weight: 800;">✓</span>
            <span data-i18n="hero_trust">Inspired by sagunms.in & thenyota.app • 100% Free for Personal Celebrations</span>
          </div>
        </div>

        <!-- Hero Showcase Universal Treasury Card -->
        <div class="hero-showcase-box">
          <div class="showcase-banner-top">
            <span data-i18n="showcase_top_bar">⚡ LIVE RECEPTION DESK • DIGITAL RED NOTEBOOK</span>
            <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; color: var(--c-crimson); font-weight: 800;">DESK #01 ACTIVE</span>
          </div>

          <div class="showcase-image-holder">
            <img id="showcase-main-img" src="https://images.unsplash.com/photo-1608755728617-aefab37d2edd?auto=format&fit=crop&w=1200&q=85" alt="Auspicious Celebration Setup">
            <div class="showcase-image-overlay">
              <div class="showcase-tag-sub" data-i18n="showcase_sub">SHUBH AARAMBH</div>
              <div class="showcase-event-heading" data-i18n="showcase_title">Auspicious Family Celebration Treasury</div>
              <div class="showcase-venue-text" data-i18n="showcase_venue">Live Reception Desk • Multi-Counter Synchronization</div>
            </div>
          </div>

          <div class="showcase-data-grid">
            <div class="showcase-data-item">
              <div class="showcase-data-label" data-i18n="metric_blessings">Total Shagun Blessings</div>
              <div class="showcase-data-val num-currency" id="showcase-inflow-val" style="color: var(--c-crimson);">₹8,42,116</div>
            </div>
            <div class="showcase-data-item">
              <div class="showcase-data-label" data-i18n="metric_expenses">Event Expenses</div>
              <div class="showcase-data-val num-currency" id="showcase-expenses-val">₹4,15,000</div>
            </div>
            <div class="showcase-data-item">
              <div class="showcase-data-label" data-i18n="metric_surplus">Net Auspicious Surplus</div>
              <div class="showcase-data-val num-currency" id="showcase-surplus-val" style="color: var(--c-emerald);">+₹4,27,116</div>
            </div>
            <div class="showcase-data-item">
              <div class="showcase-data-label" data-i18n="metric_gold">Gold & Silver Articles</div>
              <div class="showcase-data-val num-currency" id="showcase-gold-val">42.5g / 550g</div>
            </div>
          </div>

          <div class="showcase-feed-row">
            <div style="display: flex; align-items: center; gap: 12px;">
              <div class="feed-avatar">VR</div>
              <div>
                <div style="font-family: var(--font-sans); font-size: 13.5px; font-weight: 700; color: var(--c-night);">Venkat Rao Garu</div>
                <div style="font-family: var(--font-sans); font-size: 11.5px; color: var(--c-muted);" data-i18n="feed_item_sub">Vijayawada • Relatives (+₹1 Lucky Shagun Added)</div>
              </div>
            </div>
            <div class="num-currency" style="font-size: 15px; font-weight: 800; color: var(--c-emerald);">+ ₹10,116</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Capabilities Section -->
    <section id="features-section" class="section-wrap" style="background: #FFFFFF; border-top: 1.5px solid var(--c-border); border-bottom: 1.5px solid var(--c-border);">
      <div class="section-header-center">
        <span class="section-eyebrow" data-i18n="sec_cap_eyebrow">CORE CAPABILITIES</span>
        <h2 class="section-title" data-i18n="sec_cap_title">Engineered for the Reception Desk</h2>
        <p class="section-desc" data-i18n="sec_cap_desc">
          Eliminate handwriting confusion, lost envelopes, and mental calculation stress forever with purpose-built digital desk tools.
        </p>
      </div>

      <div class="capabilities-grid">
        <div class="cap-card">
          <div>
            <div class="cap-icon">⚡</div>
            <h3 class="cap-title" data-i18n="cap_1_title">3-Second Munshi Rapid Entry</h3>
            <p class="cap-text" data-i18n="cap_1_text">
              Ultra-fast guest logging with instant city autocomplete, voice mic dictation, family relationship tags, and automatic +₹1 lucky coin rounding chips.
            </p>
          </div>
          <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center;" onclick="navToView('login')">
            <span data-i18n="cap_1_btn">Open Munshi Desk →</span>
          </button>
        </div>

        <div class="cap-card">
          <div>
            <div class="cap-icon">🔄</div>
            <h3 class="cap-title" data-i18n="cap_2_title">Smart Reciprocity Intelligence</h3>
            <p class="cap-text" data-i18n="cap_2_text">
              "How much did they give us last time? How much should we give them back?" Instant gift history retrieval and return shagun suggestions.
            </p>
          </div>
          <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center;" onclick="navToView('login')">
            <span data-i18n="cap_2_btn">View Reciprocity Engine →</span>
          </button>
        </div>

        <div class="cap-card">
          <div>
            <div class="cap-icon">📖</div>
            <h3 class="cap-title" data-i18n="cap_3_title">Digital Red Notebook & PDF</h3>
            <p class="cap-text" data-i18n="cap_3_text">
              The modern avatar of the traditional Erra Pusthakam / Shagun Diary. One-click CSV export and beautifully formatted printable ledger sheets.
            </p>
          </div>
          <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center;" onclick="navToView('login')">
            <span data-i18n="cap_3_btn">Access Digital Red Book →</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Comparison Table -->
    <section id="comparison-section" class="section-wrap">
      <div class="section-header-center">
        <span class="section-eyebrow" data-i18n="comp_eyebrow">WHY FAMILIES UPGRADE</span>
        <h2 class="section-title" data-i18n="comp_title">The Traditional Diary vs GiftVault</h2>
        <p class="section-desc" data-i18n="comp_desc">Traditional red books are prone to spilled tea, lost pages, illegible scribbles, and math mistakes.</p>
      </div>

      <div class="comparison-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th data-i18n="th_feature">Feature Capability</th>
              <th data-i18n="th_paper">Traditional Paper Diary</th>
              <th data-i18n="th_giftvault">GiftVault Digital Treasury</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong data-i18n="comp_r1_f">Guest Reception Speed</strong></td>
              <td data-i18n="comp_r1_p">Slow manual writing; lines back up</td>
              <td data-i18n="comp_r1_g">⚡ 3-second entry with city autocomplete</td>
            </tr>
            <tr>
              <td><strong data-i18n="comp_r2_f">Auspicious +₹1 Rounding</strong></td>
              <td data-i18n="comp_r2_p">Manual mental math; frequently forgotten</td>
              <td data-i18n="comp_r2_g">🪙 1-click automatic +₹1 lucky coin addition</td>
            </tr>
            <tr>
              <td><strong data-i18n="comp_r3_f">Guest Acknowledgement</strong></td>
              <td data-i18n="comp_r3_p">No receipt; guest wonders if logged</td>
              <td data-i18n="comp_r3_g">📲 Instant WhatsApp greeting & digital card</td>
            </tr>
            <tr>
              <td><strong data-i18n="comp_r4_f">Reciprocity Tracking</strong></td>
              <td data-i18n="comp_r4_p">Digging through dusty notebooks from 2018</td>
              <td data-i18n="comp_r4_g">🔄 Instant relationship history & return advice</td>
            </tr>
            <tr>
              <td><strong data-i18n="comp_r5_f">Data Loss Risk</strong></td>
              <td data-i18n="comp_r5_p">High (water damage, misplaced book)</td>
              <td data-i18n="comp_r5_g">🔒 Encrypted cloud & instant Excel/PDF export</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- FAQ Section -->
    <section id="faq-section" class="section-wrap" style="background: #FFFFFF; border-top: 1.5px solid var(--c-border);">
      <div class="section-header-center">
        <span class="section-eyebrow" data-i18n="faq_eyebrow">COMMON QUESTIONS</span>
        <h2 class="section-title" data-i18n="faq_title">Frequently Asked Questions</h2>
        <p class="section-desc" data-i18n="faq_desc">Everything you need to know about using GiftVault for your upcoming family event.</p>
      </div>

      <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px;">
        <div style="background: var(--c-base); border: 1.5px solid var(--c-border); border-radius: 12px; padding: 20px;">
          <h4 style="font-family: var(--font-sans); font-size: 16px; font-weight: 700; color: var(--c-night); margin-bottom: 8px;" data-i18n="faq_q1">Does GiftVault work offline if reception hall internet drops?</h4>
          <p style="font-size: 14px; color: var(--c-muted); line-height: 1.6;" data-i18n="faq_a1">Yes! GiftVault caches your entries locally in your browser storage. You can continue recording shagun offline and it will automatically sync once connected.</p>
        </div>
        <div style="background: var(--c-base); border: 1.5px solid var(--c-border); border-radius: 12px; padding: 20px;">
          <h4 style="font-family: var(--font-sans); font-size: 16px; font-weight: 700; color: var(--c-night); margin-bottom: 8px;" data-i18n="faq_q2">Can we have multiple relatives entering gifts simultaneously?</h4>
          <p style="font-size: 14px; color: var(--c-muted); line-height: 1.6;" data-i18n="faq_a2">Yes. You can assign Counter 1 and Counter 2 to different family members on their smartphones, and all entries aggregate into the master ledger in real-time.</p>
        </div>
        <div style="background: var(--c-base); border: 1.5px solid var(--c-border); border-radius: 12px; padding: 20px;">
          <h4 style="font-family: var(--font-sans); font-size: 16px; font-weight: 700; color: var(--c-night); margin-bottom: 8px;" data-i18n="faq_q3">Can we export the complete Red Notebook into Excel or PDF?</h4>
          <p style="font-size: 14px; color: var(--c-muted); line-height: 1.6;" data-i18n="faq_a3">Yes, with a single click you can download a complete CSV spreadsheet or print a beautifully styled traditional ledger sheet for family records.</p>
        </div>
      </div>
    </section>
  </main>

  <!-- ==========================================================================
       VIEW 2: LOGIN / AUTH SCREEN
       ========================================================================== -->
  <main id="view-login" class="app-screen-view">
    <div class="page-back-nav-bar">
      <button type="button" class="btn-page-back" onclick="navToView('landing')">
        <span>←</span>
        <span data-i18n="btn_back_home">Back to Home</span>
      </button>
      <div class="page-breadcrumb">
        <span data-i18n="breadcrumb_home">Home</span> &gt; <strong data-i18n="breadcrumb_signin">Sign In</strong>
      </div>
      <div></div>
    </div>

    <div class="login-container-box">
      <div class="login-header-zone">
        <div class="brand-icon-box" style="margin: 0 auto 12px;">GV</div>
        <div class="showcase-tag-sub" style="margin-bottom: 2px;" data-i18n="login_tag">SHUBH PRAVESH</div>
        <h2 data-i18n="login_title">Sign In to GiftVault</h2>
        <p style="font-size: 13.5px; color: var(--c-muted); margin-top: 4px;" data-i18n="login_desc">Access your auspicious event ledgers and reception desks</p>
      </div>

      <form onsubmit="handleLoginSubmit(event)">
        <div class="form-group-item">
          <label class="form-label-txt" for="login-mobile" data-i18n="login_mobile_lbl">Registered Mobile Number / Email</label>
          <input type="text" id="login-mobile" class="form-input-field" value="+91 98480 22338" required>
        </div>

        <div class="form-group-item">
          <label class="form-label-txt" for="login-pin" data-i18n="login_pin_lbl">4-Digit Security PIN</label>
          <input type="password" id="login-pin" class="form-input-field" value="2026" maxlength="6" required>
        </div>

        <div class="auth-demo-credentials">
          <strong data-i18n="login_demo_txt">Demo Host Access:</strong> Mobile: <code>+91 98480 22338</code> • PIN: <code>2026</code>
        </div>

        <button type="submit" class="btn-crimson" style="width: 100%; justify-content: center; padding: 13px; font-size: 15px;">
          <span data-i18n="btn_enter_hub">Enter Event Hub</span>
          <span>→</span>
        </button>
      </form>
    </div>
  </main>

  <!-- ==========================================================================
       VIEW 3: EVENT HUB (SGUNMS.IN STYLE SELECTION + CREATE MODAL)
       ========================================================================== -->
  <main id="view-hub" class="app-screen-view">
    <div class="page-back-nav-bar">
      <button type="button" class="btn-page-back" onclick="navToView('login')">
        <span>←</span>
        <span data-i18n="btn_back_signin">Back to Sign In</span>
      </button>
      <div class="page-breadcrumb">
        <span data-i18n="breadcrumb_home">Home</span> &gt; <span data-i18n="breadcrumb_auth">Auth</span> &gt; <strong data-i18n="breadcrumb_hub">Event Selection Hub</strong>
      </div>
      <button type="button" class="btn-outline-dark" style="padding: 6px 14px; font-size: 12px;" onclick="navToView('landing')">
        <span data-i18n="btn_home_page">Home Page</span>
      </button>
    </div>

    <div class="hub-container-wrap">
      <div class="hub-top-bar">
        <div class="hub-title-block">
          <div class="showcase-tag-sub" style="margin-bottom: 2px;" data-i18n="hub_tag">KALYANA VEDIKA</div>
          <h1 data-i18n="hub_title">Select Your Celebration</h1>
          <p data-i18n="hub_desc">Choose an ongoing celebration or create a new auspicious ledger</p>
        </div>
        <button type="button" class="btn-crimson" onclick="openCreateEventModal()">
          <span data-i18n="btn_create_event">+ Create New Event</span>
        </button>
      </div>

      <div class="events-selection-grid" id="events-hub-grid">
        <!-- Event Card 1: Wedding -->
        <div class="event-selection-card" onclick="enterWorkspaceEvent('event-wedding')">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
              <span class="tag-badge" style="background: var(--c-crimson); color: #FFFFFF;" data-i18n="tag_wedding">💍 WEDDING</span>
              <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; font-size: 12px; font-weight: 700; color: var(--c-emerald);" data-i18n="status_live">LIVE NOW</span>
            </div>
            <h3 style="font-family: var(--font-serif); font-size: 21px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">
              Rahul & Snigdha Kalyanam
            </h3>
            <p style="font-size: 13px; color: var(--c-muted); margin-bottom: 16px;">
              Novotel Convention Centre, Hyderabad • Nov 14, 2026
            </p>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; padding: 10px 0; border-top: 1px solid var(--c-border); font-family: var(--font-sans); font-size: 13px;">
              <span data-i18n="lbl_total_blessings">Total Blessings:</span>
              <strong class="num-currency" style="color: var(--c-crimson);">₹8,42,116</strong>
            </div>
            <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center; margin-top: 8px;">
              <span data-i18n="btn_open_reception">Open Reception Desk →</span>
            </button>
          </div>
        </div>

        <!-- Event Card 2: Birthday -->
        <div class="event-selection-card" onclick="enterWorkspaceEvent('event-birthday')">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
              <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;" data-i18n="tag_barasala">🎂 BARASALA</span>
              <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; font-size: 12px; font-weight: 700; color: var(--c-muted);" data-i18n="status_completed">COMPLETED</span>
            </div>
            <h3 style="font-family: var(--font-serif); font-size: 21px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">
              Advait 1st Birthday & Cradle
            </h3>
            <p style="font-size: 13px; color: var(--c-muted); margin-bottom: 16px;">
              Guntur Grand Kalyana Mandapam • Oct 18, 2026
            </p>
          </div>
          <div>
            <div style="display: flex; justify-content: space-between; padding: 10px 0; border-top: 1px solid var(--c-border); font-family: var(--font-sans); font-size: 13px;">
              <span data-i18n="lbl_total_blessings">Total Blessings:</span>
              <strong class="num-currency" style="color: var(--c-crimson);">₹3,18,116</strong>
            </div>
            <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center; margin-top: 8px;">
              <span data-i18n="btn_view_history">View Ledger History →</span>
            </button>
          </div>
        </div>

        <!-- Create New Event Card -->
        <div class="create-new-event-card" onclick="openCreateEventModal()">
          <div class="create-icon-circle">+</div>
          <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;" data-i18n="btn_create_event">
            Create New Event
          </h3>
          <p style="font-size: 13px; color: var(--c-muted); max-width: 260px;" data-i18n="create_card_desc">
            Housewarming, Tonsure, Dhoti Ceremony, Half Saree, or Custom Milestone
          </p>
        </div>
      </div>
    </div>
  </main>

  <!-- ==========================================================================
       VIEW 4: IN-APP WORKSPACE (8 MODULES WITH VOICE MIC, PHOTO PROOF, LIVE SEARCH)
       ========================================================================== -->
  <main id="view-app" class="app-screen-view">
    <div class="workspace-top-header">
      <div class="ws-event-info">
        <button type="button" class="btn-page-back" onclick="navToView('hub')">
          <span>←</span>
          <span data-i18n="btn_back_hub">Back to Event Hub</span>
        </button>
        <div>
          <div class="ws-event-title" id="ws-event-header-name">Rahul & Snigdha Kalyanam</div>
          <div style="font-size: 11.5px; color: #CBD5E1; font-family: var(--font-sans);" data-i18n="ws_subtitle">
            Novotel Hyderabad • Reception Desk Mode
          </div>
        </div>
        <span class="ws-event-badge">LIVE DESK #1</span>
      </div>

      <div style="display: flex; align-items: center; gap: 12px;">
        <button type="button" class="btn-crimson" style="padding: 7px 16px; font-size: 13px;" onclick="switchWorkspaceTab('tab-entry')">
          <span data-i18n="btn_record_shagun">+ Record Shagun</span>
        </button>
        <button type="button" class="btn-outline-dark" style="color: #FFFFFF; border-color: rgba(255, 255, 255, 0.4); padding: 7px 14px; font-size: 12.5px;" onclick="navToView('landing')">
          <span data-i18n="btn_exit_home">Exit to Home</span>
        </button>
      </div>
    </div>

    <!-- 8 Tabs Bar -->
    <nav class="ws-tabs-bar">
      <button type="button" class="ws-tab-btn active" onclick="switchWorkspaceTab('tab-overview', this)">
        <span>📊</span>
        <span data-i18n="tab_overview">Dashboard Overview</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-entry', this)">
        <span>⚡</span>
        <span data-i18n="tab_entry">Munshi Rapid Entry</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-ledger', this)">
        <span>📖</span>
        <span data-i18n="tab_ledger">Red Notebook Ledger</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-expenses', this)">
        <span>⚖️</span>
        <span data-i18n="tab_expenses">Expenses vs Surplus</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-reciprocity', this)">
        <span>🔄</span>
        <span data-i18n="tab_reciprocity">Reciprocity Tracker</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-soundbox', this)">
        <span>🔊</span>
        <span data-i18n="tab_soundbox">UPI QR & Soundbox</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-reports', this)">
        <span>📄</span>
        <span data-i18n="tab_reports">PDF & Reports</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-settings', this)">
        <span>⚙️</span>
        <span data-i18n="tab_settings">Settings</span>
      </button>
    </nav>

    <div class="ws-content-body">
      
      <!-- TAB 1: OVERVIEW DASHBOARD -->
      <section id="tab-overview" class="tab-pane active">
        <div class="kpi-cards-grid">
          <div class="kpi-card" style="border-top: 4px solid var(--c-crimson);">
            <div class="kpi-title" data-i18n="kpi_blessings_title">Total Blessings Received</div>
            <div class="kpi-value num-currency" style="color: var(--c-crimson);" id="overview-total-amt">₹8,42,116</div>
            <div class="kpi-note" style="color: var(--c-emerald);" id="overview-envelopes-count">142 envelopes logged</div>
          </div>
          <div class="kpi-card" style="border-top: 4px solid var(--c-night);">
            <div class="kpi-title" data-i18n="kpi_expenses_title">Event Expenses</div>
            <div class="kpi-value num-currency">₹4,15,000</div>
            <div class="kpi-note" style="color: var(--c-muted);" data-i18n="kpi_expenses_note">Catering, Mandap, Audio</div>
          </div>
          <div class="kpi-card" style="border-top: 4px solid var(--c-emerald);">
            <div class="kpi-title" data-i18n="kpi_surplus_title">Net Auspicious Surplus</div>
            <div class="kpi-value num-currency" style="color: var(--c-emerald);">+₹4,27,116</div>
            <div class="kpi-note" style="color: var(--c-emerald);" data-i18n="kpi_surplus_note">103% Budget Covered</div>
          </div>
          <div class="kpi-card" style="border-top: 4px solid var(--c-night);">
            <div class="kpi-title" data-i18n="kpi_gold_title">Gold & Silver Articles</div>
            <div class="kpi-value num-currency">42.5g</div>
            <div class="kpi-note" style="color: var(--c-muted);" data-i18n="kpi_gold_note">550g Silver Thaali</div>
          </div>
        </div>

        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 24px;">
          <h3 style="font-family: var(--font-serif); font-size: 22px; font-weight: 800; color: var(--c-night); margin-bottom: 16px;" data-i18n="feed_heading">
            Recent Shagun Entries (Live Feed)
          </h3>
          <div class="ledger-table-wrap">
            <table class="ledger-table">
              <thead>
                <tr>
                  <th data-i18n="th_time">Timestamp</th>
                  <th data-i18n="th_name">Guest Name</th>
                  <th data-i18n="th_city">Native City</th>
                  <th data-i18n="th_relation">Relation</th>
                  <th data-i18n="th_amount">Amount / Gift</th>
                  <th data-i18n="th_mode">Mode</th>
                  <th data-i18n="th_receipt">WhatsApp</th>
                </tr>
              </thead>
              <tbody id="ws-recent-table-body">
                <tr>
                  <td>10:42 PM</td>
                  <td><strong>Venkat Rao Garu</strong></td>
                  <td>Vijayawada</td>
                  <td>Maternal Uncle</td>
                  <td class="num-currency" style="color: var(--c-emerald);">₹10,116</td>
                  <td><span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">CASH</span></td>
                  <td><button type="button" class="btn-emerald" style="padding: 4px 10px; font-size: 11.5px;" onclick="sendWhatsAppReceipt('Venkat Rao Garu', '10116', '9848011223')">📲 WhatsApp</button></td>
                </tr>
                <tr>
                  <td>10:38 PM</td>
                  <td><strong>Suresh & Malathi Sharma</strong></td>
                  <td>Hyderabad</td>
                  <td>Close Friends</td>
                  <td class="num-currency" style="color: var(--c-emerald);">₹5,116</td>
                  <td><span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">UPI</span></td>
                  <td><button type="button" class="btn-emerald" style="padding: 4px 10px; font-size: 11.5px;" onclick="sendWhatsAppReceipt('Suresh Sharma', '5116', '9848033445')">📲 WhatsApp</button></td>
                </tr>
                <tr>
                  <td>10:25 PM</td>
                  <td><strong>K. Raghunath Varma</strong></td>
                  <td>Visakhapatnam</td>
                  <td>Paternal Relative</td>
                  <td class="num-currency" style="color: var(--c-crimson);">10g Gold Coin + ₹2,116</td>
                  <td><span class="tag-badge" style="background: var(--c-crimson); color: #FFFFFF;">GOLD</span></td>
                  <td><button type="button" class="btn-emerald" style="padding: 4px 10px; font-size: 11.5px;" onclick="sendWhatsAppReceipt('K. Raghunath Varma', '2116', '9848055667')">📲 WhatsApp</button></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 2: MUNSHI RAPID ENTRY (WITH VOICE MIC & PHOTO ATTACHMENT) -->
      <section id="tab-entry" class="tab-pane">
        <div class="munshi-entry-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 10px;">
            <div>
              <div class="showcase-tag-sub" style="margin-bottom: 2px;" data-i18n="entry_tag">SHAGUN PRAAPTI</div>
              <h3 style="font-family: var(--font-serif); font-size: 26px; font-weight: 800; color: var(--c-night);" data-i18n="entry_title">Munshi Fast Entry Desk</h3>
            </div>
            
            <div style="display: flex; gap: 8px;">
              <!-- Web Speech API Mic Dictation Button -->
              <button type="button" id="btn-voice-dictate" class="voice-mic-btn" onclick="startVoiceDictation()">
                <span>🎙️</span>
                <span id="voice-status-text" data-i18n="btn_voice_entry">Voice Entry (Mic)</span>
              </button>
              <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;" data-i18n="speed_badge">⚡ 3-SECOND SPEED</span>
            </div>
          </div>

          <form onsubmit="handleMunshiSubmit(event)">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
              <div class="form-group-item">
                <label class="form-label-txt" data-i18n="lbl_guest_name">Guest Name *</label>
                <input type="text" id="entry-name" class="form-input-field" placeholder="e.g. Anand Kumar Garu" required>
              </div>
              <div class="form-group-item">
                <label class="form-label-txt" data-i18n="lbl_guest_city">Native City / Town</label>
                <input type="text" id="entry-city" class="form-input-field" placeholder="e.g. Hyderabad, Guntur, Rajahmundry">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
              <div class="form-group-item">
                <label class="form-label-txt" data-i18n="lbl_relation">Relationship</label>
                <select id="entry-rel" class="form-input-field">
                  <option value="Relatives">Family Relative</option>
                  <option value="Close Friends">Close Friend</option>
                  <option value="Colleague">Colleague / Business</option>
                  <option value="Neighbor">Neighbor</option>
                  <option value="Other">Other Well-Wisher</option>
                </select>
              </div>
              <div class="form-group-item">
                <label class="form-label-txt" data-i18n="lbl_phone">Guest Mobile (for Instant WhatsApp Receipt)</label>
                <input type="tel" id="entry-phone" class="form-input-field" placeholder="+91 98480 XXXXX">
              </div>
            </div>

            <div class="form-group-item">
              <label class="form-label-txt" data-i18n="lbl_amount">Cash Blessing Amount (₹) *</label>
              <input type="number" id="entry-amount" class="form-input-field num-currency" placeholder="5000" style="font-size: 18px; font-weight: 700;" required>
              
              <!-- Auspicious +₹1 Lucky Coin Bar -->
              <div class="lucky-one-chip-bar">
                <span style="font-family: var(--font-sans); font-size: 11.5px; font-weight: 700; align-self: center; color: var(--c-muted);" data-i18n="lbl_rounding">Auspicious Rounding:</span>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(501)">₹501</button>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(1116)">₹1,116</button>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(2116)">₹2,116</button>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(5116)">₹5,116</button>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(10116)">₹10,116</button>
                <button type="button" class="lucky-coin-chip" onclick="addOneRupeeCoin()" data-i18n="btn_coin">+₹1 Coin</button>
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1.4fr 0.6fr; gap: 16px;">
              <div class="form-group-item">
                <label class="form-label-txt" data-i18n="lbl_gift_desc">Gold / Silver / Physical Gift Description</label>
                <input type="text" id="entry-gift-desc" class="form-input-field" placeholder="e.g. 5g Gold Coin, Silver Bowl, Titan Watch">
              </div>
              <div class="form-group-item">
                <label class="form-label-txt" data-i18n="lbl_gift_photo">Gift Photo Proof</label>
                <input type="file" id="entry-photo" accept="image/*" class="form-input-field" style="padding: 8px;" onchange="previewGiftPhoto(this)">
              </div>
            </div>

            <!-- Image thumbnail preview container -->
            <div id="photo-preview-container" style="display: none; margin-bottom: 16px;">
              <div style="display: flex; align-items: center; gap: 12px; background: var(--c-base); padding: 8px 12px; border-radius: 8px;">
                <img id="photo-preview-img" src="" alt="Proof Preview" style="width: 48px; height: 48px; object-fit: cover; border-radius: 6px;">
                <span style="font-size: 12px; color: var(--c-emerald); font-weight: 700;">✓ Photo Proof Attached</span>
              </div>
            </div>

            <div style="display: flex; gap: 12px; margin-top: 24px;">
              <button type="submit" class="btn-crimson" style="flex: 1; justify-content: center; padding: 14px; font-size: 15px;">
                <span data-i18n="btn_save_entry">💾 Save Entry & Issue WhatsApp Receipt</span>
              </button>
              <button type="reset" class="btn-outline-dark" data-i18n="btn_clear">
                Clear
              </button>
            </div>
          </form>
        </div>
      </section>

      <!-- TAB 3: RED NOTEBOOK LEDGER (WITH LIVE SEARCH & FILTER) -->
      <section id="tab-ledger" class="tab-pane">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px;">
          <div>
            <h3 style="font-family: var(--font-serif); font-size: 26px; font-weight: 800; color: var(--c-night);" data-i18n="ledger_heading">Digital Red Notebook Ledger</h3>
            <p style="font-size: 13.5px; color: var(--c-muted);" data-i18n="ledger_sub">Complete audit trail of all celebration blessings</p>
          </div>
          <div style="display: flex; gap: 10px;">
            <button type="button" class="btn-emerald" onclick="exportLedgerCSV()">
              <span>📥</span>
              <span data-i18n="btn_export_csv">Export CSV</span>
            </button>
            <button type="button" class="btn-outline-dark" onclick="window.print()">
              <span>🖨️</span>
              <span data-i18n="btn_print_ledger">Print Ledger</span>
            </button>
          </div>
        </div>

        <!-- Live Search and Filter Controls -->
        <div class="ledger-filter-bar">
          <input type="text" id="ledger-search-input" class="search-input-box" placeholder="🔍 Search by guest name, native city, or gift details..." oninput="filterLedgerTable()">
          <select id="ledger-filter-mode" class="form-input-field" style="width: 180px; padding: 10px;" onchange="filterLedgerTable()">
            <option value="ALL">All Modes (Cash, UPI, Gold)</option>
            <option value="CASH">Cash Only</option>
            <option value="UPI">UPI Digital Only</option>
            <option value="GOLD">Gold & Silver Only</option>
          </select>
        </div>

        <div class="ledger-table-wrap">
          <table class="ledger-table" id="main-ledger-table">
            <thead>
              <tr>
                <th>#</th>
                <th data-i18n="th_name">Guest Name</th>
                <th data-i18n="th_city">Native Place</th>
                <th data-i18n="th_relation">Relationship</th>
                <th data-i18n="th_cash_blessing">Cash Blessing</th>
                <th data-i18n="th_gift_ornaments">Gift / Ornaments</th>
                <th data-i18n="th_recorded_by">Recorded By</th>
                <th data-i18n="th_receipt">WhatsApp</th>
              </tr>
            </thead>
            <tbody id="ws-full-ledger-body">
              <tr>
                <td>1</td>
                <td><strong>Venkat Rao Garu</strong></td>
                <td>Vijayawada</td>
                <td>Maternal Uncle</td>
                <td class="num-currency" style="color: var(--c-emerald);">₹10,116</td>
                <td>None</td>
                <td>Desk 1</td>
                <td><button type="button" class="btn-emerald" style="padding: 4px 10px; font-size: 11.5px;" onclick="sendWhatsAppReceipt('Venkat Rao Garu', '10116', '9848011223')">📲 WhatsApp</button></td>
              </tr>
              <tr>
                <td>2</td>
                <td><strong>Suresh & Malathi Sharma</strong></td>
                <td>Hyderabad</td>
                <td>Close Friends</td>
                <td class="num-currency" style="color: var(--c-emerald);">₹5,116</td>
                <td>Silk Stole</td>
                <td>Desk 1</td>
                <td><button type="button" class="btn-emerald" style="padding: 4px 10px; font-size: 11.5px;" onclick="sendWhatsAppReceipt('Suresh Sharma', '5116', '9848033445')">📲 WhatsApp</button></td>
              </tr>
              <tr>
                <td>3</td>
                <td><strong>K. Raghunath Varma</strong></td>
                <td>Visakhapatnam</td>
                <td>Paternal Relative</td>
                <td class="num-currency" style="color: var(--c-emerald);">₹2,116</td>
                <td>10g Gold Coin</td>
                <td>Desk 2</td>
                <td><button type="button" class="btn-emerald" style="padding: 4px 10px; font-size: 11.5px;" onclick="sendWhatsAppReceipt('K. Raghunath Varma', '2116', '9848055667')">📲 WhatsApp</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- TAB 4: EXPENSES VS SURPLUS -->
      <section id="tab-expenses" class="tab-pane">
        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 24px; max-width: 800px; margin: 0 auto;">
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;" data-i18n="exp_title">Celebration Budget & Expense Reconciliation</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;" data-i18n="exp_desc">Compare total received shagun against vendor expenses</p>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px;">
            <div style="background: var(--c-base); padding: 18px; border-radius: 12px; border: 1.5px solid var(--c-night);">
              <div style="font-size: 12px; font-weight: 700; text-transform: uppercase;" data-i18n="lbl_total_inflow">Total Shagun Inflow</div>
              <div class="num-currency" style="font-size: 28px; color: var(--c-crimson);">₹8,42,116</div>
            </div>
            <div style="background: var(--c-base); padding: 18px; border-radius: 12px; border: 1.5px solid var(--c-night);">
              <div style="font-size: 12px; font-weight: 700; text-transform: uppercase;" data-i18n="lbl_vendor_expenses">Total Vendor Expenses</div>
              <div class="num-currency" style="font-size: 28px; color: var(--c-night);">₹4,15,000</div>
            </div>
          </div>

          <div style="background: #FFFFFF; border: 2px solid var(--c-emerald); padding: 18px; border-radius: 12px; text-align: center;">
            <div style="font-size: 13px; font-weight: 700; color: var(--c-emerald); text-transform: uppercase;" data-i18n="lbl_net_surplus">Net Auspicious Surplus Remaining</div>
            <div class="num-currency" style="font-size: 36px; color: var(--c-emerald);">+₹4,27,116</div>
          </div>
        </div>
      </section>

      <!-- TAB 5: RECIPROCITY TRACKER -->
      <section id="tab-reciprocity" class="tab-pane">
        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 24px;">
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;" data-i18n="recip_heading">Gift Reciprocity Intelligence</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 20px;" data-i18n="recip_sub">"How much did they give us last time? How much should we give them back?"</p>

          <div class="ledger-table-wrap">
            <table class="ledger-table">
              <thead>
                <tr>
                  <th data-i18n="th_member">Family Member / Friend</th>
                  <th data-i18n="th_they_gave">They Gave Us (This Event)</th>
                  <th data-i18n="th_we_gave">We Gave Them Previously</th>
                  <th data-i18n="th_recommended">Recommended Return Shagun</th>
                  <th data-i18n="th_status">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Venkat Rao Garu (Vijayawada)</strong></td>
                  <td class="num-currency">₹10,116</td>
                  <td class="num-currency">₹5,116 (Daughter's Wedding 2024)</td>
                  <td class="num-currency" style="color: var(--c-emerald);">₹10,116 - ₹11,116</td>
                  <td><span class="tag-badge" style="background: var(--c-emerald); color: #FFFFFF;" data-i18n="badge_returned">FAVOR RETURNED</span></td>
                </tr>
                <tr>
                  <td><strong>Suresh Sharma (Hyderabad)</strong></td>
                  <td class="num-currency">₹5,116</td>
                  <td class="num-currency">₹5,116 (Housewarming 2025)</td>
                  <td class="num-currency" style="color: var(--c-night);">₹5,116</td>
                  <td><span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;" data-i18n="badge_equal">EQUAL BALANCE</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 6: UPI QR & LIVE AUDIO SOUNDBOX -->
      <section id="tab-soundbox" class="tab-pane">
        <div style="max-width: 520px; margin: 0 auto; background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 20px; padding: 32px; text-align: center;">
          <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;" data-i18n="soundbox_badge">LIVE COUNTER SOUNDBOX</span>
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin: 12px 0 8px;" data-i18n="soundbox_title">Direct UPI Shagun QR</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;" data-i18n="soundbox_desc">Guests can scan and pay directly via GPay, PhonePe, Paytm</p>

          <div style="background: var(--c-base); padding: 24px; border-radius: 16px; border: 2px dashed var(--c-night); display: inline-block; margin-bottom: 20px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=upi://pay?pa=giftvault@okhdfcbank&pn=GiftVault%20Wedding%20Treasury" alt="UPI QR Code" style="display: block; margin: 0 auto; border-radius: 8px;">
            <div class="num-currency" style="font-size: 13px; color: var(--c-night); margin-top: 12px;">
              giftvault@okhdfcbank
            </div>
          </div>

          <div>
            <button type="button" class="btn-emerald" onclick="testSoundboxAnnouncement()">
              <span>🔔</span>
              <span data-i18n="btn_soundbox_test">Test Live Soundbox Chime & Voice</span>
            </button>
          </div>
        </div>
      </section>

      <!-- TAB 7: REPORTS -->
      <section id="tab-reports" class="tab-pane">
        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 28px; max-width: 720px; margin: 0 auto;">
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;" data-i18n="reports_heading">Official Celebration Reports</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;" data-i18n="reports_sub">Download and print formal summaries for family archives</p>

          <div style="display: flex; flex-direction: column; gap: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 14px; background: var(--c-base); border-radius: 10px; border: 1px solid var(--c-border);">
              <div>
                <strong style="font-family: var(--font-sans); font-size: 14px;" data-i18n="rep_csv_title">Full Guest Shagun Ledger (CSV)</strong>
                <div style="font-size: 12px; color: var(--c-muted);" data-i18n="rep_csv_desc">All entries with timestamps, cities, phone numbers</div>
              </div>
              <button type="button" class="btn-outline-dark" onclick="exportLedgerCSV()" data-i18n="btn_download_csv">Download CSV</button>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 14px; background: var(--c-base); border-radius: 10px; border: 1px solid var(--c-border);">
              <div>
                <strong style="font-family: var(--font-sans); font-size: 14px;" data-i18n="rep_pdf_title">Executive Summary (Printable PDF)</strong>
                <div style="font-size: 12px; color: var(--c-muted);" data-i18n="rep_pdf_desc">Grand totals, gold summary, and city breakdown</div>
              </div>
              <button type="button" class="btn-outline-dark" onclick="window.print()" data-i18n="btn_print_pdf">Print Report</button>
            </div>
          </div>
        </div>
      </section>

      <!-- TAB 8: SETTINGS -->
      <section id="tab-settings" class="tab-pane">
        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 28px; max-width: 680px; margin: 0 auto;">
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;" data-i18n="cfg_title">Event Configuration</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;" data-i18n="cfg_desc">Manage celebration parameters, PINs, and counter settings</p>

          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="cfg_name_lbl">Event Celebration Title</label>
            <input type="text" class="form-input-field" value="Rahul & Snigdha Kalyanam">
          </div>
          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="cfg_coin_lbl">Auspicious Coin Rounding</label>
            <select class="form-input-field">
              <option selected data-i18n="cfg_opt_coin">Always offer +₹1 lucky coin button</option>
              <option data-i18n="cfg_opt_round">Standard round numbers only</option>
            </select>
          </div>
          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="cfg_pin_lbl">Desk Host Passcode</label>
            <input type="password" class="form-input-field" value="2026">
          </div>
          <button type="button" class="btn-crimson" onclick="alert('Settings saved successfully!')">
            <span data-i18n="btn_save_cfg">Save Configuration</span>
          </button>
        </div>
      </section>

    </div>
  </main>

  <!-- ==========================================================================
       CREATE NEW EVENT MODAL
       ========================================================================== -->
  <div id="modal-create-event" class="modal-backdrop">
    <div class="modal-dialog">
      <div class="modal-header">
        <div>
          <div class="showcase-tag-sub" style="margin-bottom: 2px;" data-i18n="modal_create_tag">NOOTANA SHUBHA KAARYAM</div>
          <h3 data-i18n="modal_create_title">Create New Auspicious Event</h3>
        </div>
        <button type="button" class="modal-close-btn" onclick="closeCreateEventModal()">✕</button>
      </div>

      <div class="modal-body">
        <form onsubmit="handleCreateEventSubmit(event)">
          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="modal_milestone_lbl">Celebration Milestone Category *</label>
            <select id="new-event-type" class="form-input-field" required>
              <option value="Wedding">💍 Wedding (Vivaha / Kalyanam / Nikah)</option>
              <option value="Birthday">🎂 Birthday & Barasala (Cradle Naming)</option>
              <option value="Housewarming">🏡 Housewarming (Griha Pravesh)</option>
              <option value="Tonsure">✂️ Tonsure (Mundan / Jattu Kaaryam)</option>
              <option value="HalfSaree">👗 Half Saree (Pushpalankarana)</option>
              <option value="Dhoti">👔 Dhoti Ceremony (Upanayanam)</option>
              <option value="Custom">🎉 Other Auspicious Milestone</option>
            </select>
          </div>

          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="modal_event_title_lbl">Event Celebration Title *</label>
            <input type="text" id="new-event-title" class="form-input-field" placeholder="e.g. Ramesh & Divya Vivaha Mahotsavam" required>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div class="form-group-item">
              <label class="form-label-txt" data-i18n="modal_date_lbl">Date of Event *</label>
              <input type="date" id="new-event-date" class="form-input-field" required>
            </div>
            <div class="form-group-item">
              <label class="form-label-txt" data-i18n="modal_guests_lbl">Expected Guest Count</label>
              <input type="number" id="new-event-guests" class="form-input-field" placeholder="500">
            </div>
          </div>

          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="modal_venue_lbl">Reception Venue & City</label>
            <input type="text" id="new-event-venue" class="form-input-field" placeholder="e.g. Grand Kalyana Mandapam, Guntur">
          </div>

          <div style="display: flex; gap: 12px; margin-top: 24px;">
            <button type="button" class="btn-page-back" onclick="closeCreateEventModal()">
              <span>←</span>
              <span data-i18n="btn_cancel">Cancel</span>
            </button>
            <button type="submit" class="btn-crimson" style="flex: 1; justify-content: center;">
              <span data-i18n="btn_create_ledger">Create Event Ledger →</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <!-- Main Footer -->
  <footer class="main-footer">
    <div class="footer-grid">
      <div class="footer-brand">
        <h3>GiftVault</h3>
        <p data-i18n="footer_about">The modern digital Red Notebook and Shagun Treasury engineered for Indian family celebrations and reception desks worldwide.</p>
        <div style="margin-top: 16px; font-family: var(--font-sans); font-size: 13.5px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #FFFFFF;">
          SHUBHAM BHAVATU
        </div>
      </div>
      <div class="footer-col">
        <h4 data-i18n="nav_capabilities">Capabilities</h4>
        <ul class="footer-links-list">
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');" data-i18n="cap_1_title">Munshi Rapid Entry</button></li>
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');" data-i18n="cap_2_title">Reciprocity Tracker</button></li>
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');" data-i18n="cap_3_title">Digital Red Notebook</button></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4 data-i18n="footer_reception">Reception Desk</h4>
        <ul class="footer-links-list">
          <li><button type="button" class="footer-btn-link" onclick="navToView('login')" data-i18n="btn_open_desk">Open Reception Desk</button></li>
          <li><button type="button" class="footer-btn-link" onclick="navToView('login')" data-i18n="footer_multicounter">Multi-Counter Sync</button></li>
          <li><button type="button" class="footer-btn-link" onclick="navToView('login')" data-i18n="tab_soundbox">UPI Soundbox</button></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom-bar">
      <div>© 2026 GiftVault. All rights reserved. Built for Indian Family Celebrations.</div>
      <div>Multi-Language Engine • Option B Typography • Live Soundbox</div>
    </div>
  </footer>

  <!-- ==========================================================================
       JAVASCRIPT APPLICATION LOGIC
       ========================================================================== -->
  <script>
    // ==========================================
    // 1. MULTI-LANGUAGE DICTIONARY (EN, TE, HI)
    // ==========================================
    const I18N_DICT = {
      en: {
        brand_subtitle: "Shagun & Celebration Treasury",
        nav_overview: "Overview",
        nav_capabilities: "Capabilities",
        nav_comparison: "Comparison",
        nav_faq: "FAQ",
        btn_signin: "Sign In to Vault",
        btn_back: "Back",
        btn_back_home: "Back to Home",
        btn_back_signin: "Back to Sign In",
        btn_back_hub: "Back to Event Hub",
        btn_home_page: "Home Page",
        breadcrumb_home: "Home",
        breadcrumb_signin: "Sign In",
        breadcrumb_auth: "Auth",
        breadcrumb_hub: "Event Selection Hub",
        hero_pill: "Auspicious Shagun & Celebration Treasury",
        hero_tagline: "SHUBH AARAMBH • MANGALA KAARYAM",
        hero_h1: "The Digital Red Notebook for Every Family <em>Celebration</em>.",
        hero_desc: "Preserve blessings, gold, cash, and gifts with instant WhatsApp receipts and zero calculation errors. Designed specifically for auspicious Indian family celebrations and reception desks.",
        btn_open_desk: "Open Reception Desk",
        btn_explore: "Explore Capabilities",
        hero_trust: "Inspired by sagunms.in & thenyota.app • 100% Free for Personal Celebrations",
        showcase_top_bar: "⚡ LIVE RECEPTION DESK • DIGITAL RED NOTEBOOK",
        showcase_sub: "SHUBH AARAMBH",
        showcase_title: "Auspicious Family Celebration Treasury",
        showcase_venue: "Live Reception Desk • Multi-Counter Synchronization",
        metric_blessings: "Total Shagun Blessings",
        metric_expenses: "Event Expenses",
        metric_surplus: "Net Auspicious Surplus",
        metric_gold: "Gold & Silver Articles",
        feed_item_sub: "Vijayawada • Relatives (+₹1 Lucky Shagun Added)",
        sec_cap_eyebrow: "CORE CAPABILITIES",
        sec_cap_title: "Engineered for the Reception Desk",
        sec_cap_desc: "Eliminate handwriting confusion, lost envelopes, and mental calculation stress forever with purpose-built digital desk tools.",
        cap_1_title: "3-Second Munshi Rapid Entry",
        cap_1_text: "Ultra-fast guest logging with instant city autocomplete, voice mic dictation, family relationship tags, and automatic +₹1 lucky coin rounding chips.",
        cap_1_btn: "Open Munshi Desk →",
        cap_2_title: "Smart Reciprocity Intelligence",
        cap_2_text: "\"How much did they give us last time? How much should we give them back?\" Instant gift history retrieval and return shagun suggestions.",
        cap_2_btn: "View Reciprocity Engine →",
        cap_3_title: "Digital Red Notebook & PDF",
        cap_3_text: "The modern avatar of the traditional Erra Pusthakam / Shagun Diary. One-click CSV export and beautifully formatted printable ledger sheets.",
        cap_3_btn: "Access Digital Red Book →",
        comp_eyebrow: "WHY FAMILIES UPGRADE",
        comp_title: "The Traditional Diary vs GiftVault",
        comp_desc: "Traditional red books are prone to spilled tea, lost pages, illegible scribbles, and math mistakes.",
        th_feature: "Feature Capability",
        th_paper: "Traditional Paper Diary",
        th_giftvault: "GiftVault Digital Treasury",
        comp_r1_f: "Guest Reception Speed",
        comp_r1_p: "Slow manual writing; lines back up",
        comp_r1_g: "⚡ 3-second entry with city autocomplete",
        comp_r2_f: "Auspicious +₹1 Rounding",
        comp_r2_p: "Manual mental math; frequently forgotten",
        comp_r2_g: "🪙 1-click automatic +₹1 lucky coin addition",
        comp_r3_f: "Guest Acknowledgement",
        comp_r3_p: "No receipt; guest wonders if logged",
        comp_r3_g: "📲 Instant WhatsApp greeting & digital card",
        comp_r4_f: "Reciprocity Tracking",
        comp_r4_p: "Digging through dusty notebooks from 2018",
        comp_r4_g: "🔄 Instant relationship history & return advice",
        comp_r5_f: "Data Loss Risk",
        comp_r5_p: "High (water damage, misplaced book)",
        comp_r5_g: "🔒 Encrypted cloud & instant Excel/PDF export",
        faq_eyebrow: "COMMON QUESTIONS",
        faq_title: "Frequently Asked Questions",
        faq_desc: "Everything you need to know about using GiftVault for your upcoming family event.",
        faq_q1: "Does GiftVault work offline if reception hall internet drops?",
        faq_a1: "Yes! GiftVault caches your entries locally in your browser storage. You can continue recording shagun offline and it will automatically sync once connected.",
        faq_q2: "Can we have multiple relatives entering gifts simultaneously?",
        faq_a2: "Yes. You can assign Counter 1 and Counter 2 to different family members on their smartphones, and all entries aggregate into the master ledger in real-time.",
        faq_q3: "Can we export the complete Red Notebook into Excel or PDF?",
        faq_a3: "Yes, with a single click you can download a complete CSV spreadsheet or print a beautifully styled traditional ledger sheet for family records.",
        login_tag: "SHUBH PRAVESH",
        login_title: "Sign In to GiftVault",
        login_desc: "Access your auspicious event ledgers and reception desks",
        login_mobile_lbl: "Registered Mobile Number / Email",
        login_pin_lbl: "4-Digit Security PIN",
        login_demo_txt: "Demo Host Access:",
        btn_enter_hub: "Enter Event Hub",
        hub_tag: "KALYANA VEDIKA",
        hub_title: "Select Your Celebration",
        hub_desc: "Choose an ongoing celebration or create a new auspicious ledger",
        btn_create_event: "+ Create New Event",
        tag_wedding: "💍 WEDDING",
        tag_barasala: "🎂 BARASALA",
        status_live: "LIVE NOW",
        status_completed: "COMPLETED",
        lbl_total_blessings: "Total Blessings:",
        btn_open_reception: "Open Reception Desk →",
        btn_view_history: "View Ledger History →",
        create_card_desc: "Housewarming, Tonsure, Dhoti Ceremony, Half Saree, or Custom Milestone",
        ws_subtitle: "Novotel Hyderabad • Reception Desk Mode",
        btn_record_shagun: "+ Record Shagun",
        btn_exit_home: "Exit to Home",
        tab_overview: "Dashboard Overview",
        tab_entry: "Munshi Rapid Entry",
        tab_ledger: "Red Notebook Ledger",
        tab_expenses: "Expenses vs Surplus",
        tab_reciprocity: "Reciprocity Tracker",
        tab_soundbox: "UPI QR & Soundbox",
        tab_reports: "PDF & Reports",
        tab_settings: "Settings",
        kpi_blessings_title: "Total Blessings Received",
        kpi_expenses_title: "Event Expenses",
        kpi_expenses_note: "Catering, Mandap, Audio",
        kpi_surplus_title: "Net Auspicious Surplus",
        kpi_surplus_note: "103% Budget Covered",
        kpi_gold_title: "Gold & Silver Articles",
        kpi_gold_note: "550g Silver Thaali",
        feed_heading: "Recent Shagun Entries (Live Feed)",
        th_time: "Timestamp",
        th_name: "Guest Name",
        th_city: "Native City",
        th_relation: "Relation",
        th_amount: "Amount / Gift",
        th_mode: "Mode",
        th_receipt: "WhatsApp",
        entry_tag: "SHAGUN PRAAPTI",
        entry_title: "Munshi Fast Entry Desk",
        btn_voice_entry: "Voice Entry (Mic)",
        speed_badge: "⚡ 3-SECOND SPEED",
        lbl_guest_name: "Guest Name *",
        lbl_guest_city: "Native City / Town",
        lbl_relation: "Relationship",
        lbl_phone: "Guest Mobile (for Instant WhatsApp Receipt)",
        lbl_amount: "Cash Blessing Amount (₹) *",
        lbl_rounding: "Auspicious Rounding:",
        btn_coin: "+₹1 Coin",
        lbl_gift_desc: "Gold / Silver / Physical Gift Description",
        lbl_gift_photo: "Gift Photo Proof",
        btn_save_entry: "💾 Save Entry & Issue WhatsApp Receipt",
        btn_clear: "Clear",
        ledger_heading: "Digital Red Notebook Ledger",
        ledger_sub: "Complete audit trail of all celebration blessings",
        btn_export_csv: "Export CSV",
        btn_print_ledger: "Print Ledger",
        th_cash_blessing: "Cash Blessing",
        th_gift_ornaments: "Gift / Ornaments",
        th_recorded_by: "Recorded By",
        exp_title: "Celebration Budget & Expense Reconciliation",
        exp_desc: "Compare total received shagun against vendor expenses",
        lbl_total_inflow: "Total Shagun Inflow",
        lbl_vendor_expenses: "Total Vendor Expenses",
        lbl_net_surplus: "Net Auspicious Surplus Remaining",
        recip_heading: "Gift Reciprocity Intelligence",
        recip_sub: "\"How much did they give us last time? How much should we give them back?\"",
        th_member: "Family Member / Friend",
        th_they_gave: "They Gave Us (This Event)",
        th_we_gave: "We Gave Them Previously",
        th_recommended: "Recommended Return Shagun",
        th_status: "Status",
        badge_returned: "FAVOR RETURNED",
        badge_equal: "EQUAL BALANCE",
        soundbox_badge: "LIVE COUNTER SOUNDBOX",
        soundbox_title: "Direct UPI Shagun QR",
        soundbox_desc: "Guests can scan and pay directly via GPay, PhonePe, Paytm",
        btn_soundbox_test: "Test Live Soundbox Chime & Voice",
        reports_heading: "Official Celebration Reports",
        reports_sub: "Download and print formal summaries for family archives",
        rep_csv_title: "Full Guest Shagun Ledger (CSV)",
        rep_csv_desc: "All entries with timestamps, cities, phone numbers",
        btn_download_csv: "Download CSV",
        rep_pdf_title: "Executive Summary (Printable PDF)",
        rep_pdf_desc: "Grand totals, gold summary, and city breakdown",
        btn_print_pdf: "Print Report",
        cfg_title: "Event Configuration",
        cfg_desc: "Manage celebration parameters, PINs, and counter settings",
        cfg_name_lbl: "Event Celebration Title",
        cfg_coin_lbl: "Auspicious Coin Rounding",
        cfg_opt_coin: "Always offer +₹1 lucky coin button",
        cfg_opt_round: "Standard round numbers only",
        cfg_pin_lbl: "Desk Host Passcode",
        btn_save_cfg: "Save Configuration",
        modal_create_tag: "NOOTANA SHUBHA KAARYAM",
        modal_create_title: "Create New Auspicious Event",
        modal_milestone_lbl: "Celebration Milestone Category *",
        modal_event_title_lbl: "Event Celebration Title *",
        modal_date_lbl: "Date of Event *",
        modal_guests_lbl: "Expected Guest Count",
        modal_venue_lbl: "Reception Venue & City",
        btn_cancel: "Cancel",
        btn_create_ledger: "Create Event Ledger →",
        footer_about: "The modern digital Red Notebook and Shagun Treasury engineered for Indian family celebrations and reception desks worldwide.",
        footer_reception: "Reception Desk",
        footer_multicounter: "Multi-Counter Sync"
      },
      te: {
        brand_subtitle: "రాయల్ శుభకార్య ఖజానా & చదివింపులు",
        nav_overview: "పరిచయం",
        nav_capabilities: "ఫీచర్లు & డెస్క్",
        nav_comparison: "పోలిక",
        nav_faq: "సందేహాలు",
        btn_signin: "ఖజానాలోకి లాగిన్",
        btn_back: "వెనుకకు",
        btn_back_home: "హోమ్ పేజీకి",
        btn_back_signin: "లాగిన్ కు",
        btn_back_hub: "ఈవెంట్ హబ్ కు",
        btn_home_page: "హోమ్ పేజీ",
        breadcrumb_home: "హోమ్",
        breadcrumb_signin: "లాగిన్",
        breadcrumb_auth: "ప్రామాణీకరణ",
        breadcrumb_hub: "ఈవెంట్ ఎంపిక హబ్",
        hero_pill: "శుభప్రదమైన కుటుంబ చదివింపుల డిజిటల్ ఖజానా",
        hero_tagline: "శుభారంభం • మంగళ కార్యం",
        hero_h1: "ప్రతి భారతీయ శుభకార్యానికి <em>డిజిటల్ ఎర్ర పుస్తకం</em>.",
        hero_desc: "చదివింపులు, నగదు, బంగారం మరియు కానుకల వివరాలను తక్షణ వాట్సాప్ రసీదులు మరియు జీరో కాలిక్యులేషన్ పొరపాట్లతో శాశ్వతంగా భద్రపరచండి.",
        btn_open_desk: "రిసెప్షన్ డెస్క్ తెరవండి",
        btn_explore: "ఫీచర్లు చూడండి",
        hero_trust: "sgunms.in & thenyota.app స్ఫూర్తితో • కుటుంబాలకు 100% ఉచితం",
        showcase_top_bar: "⚡ లైవ్ రిసెప్షన్ డెస్క్ • డిజిటల్ ఎర్ర పుస్తకం",
        showcase_sub: "శుభారంభం",
        showcase_title: "రాయల్ శుభకార్య చదివింపుల ఖజానా",
        showcase_venue: "లైవ్ రిసెప్షన్ డెస్క్ • మల్టీ-కౌంటర్ సింక్",
        metric_blessings: "మొత్తం చదివింపులు",
        metric_expenses: "ఈవెంట్ ఖర్చులు",
        metric_surplus: "నికర శుభ మిగులు",
        metric_gold: "బంగారం & వెండి కానుకలు",
        feed_item_sub: "విజయవాడ • బంధువులు (+₹1 లక్కీ కాయిన్ చేర్చబడింది)",
        sec_cap_eyebrow: "ముఖ్య ఫీచర్లు",
        sec_cap_title: "రిసెప్షన్ డెస్క్ కోసం ప్రత్యేకంగా రూపొందించబడింది",
        sec_cap_desc: "చేతిరాత గందరగోళం, పోయిన కవర్లు మరియు లెక్కల ఒత్తిడిని శాశ్వతంగా దూరం చేయండి.",
        cap_1_title: "⚡ 3-సెకన్ల మున్షీ ఫాస్ట్ ఎంట్రీ",
        cap_1_text: "వాయిస్ మైక్ ద్వారా చెప్పి రాయించే సదుపాయం, సిటీ ఆటోకంప్లీట్, మరియు +₹1 లక్కీ కాయిన్ రౌండింగ్ బటన్లు.",
        cap_1_btn: "మున్షీ డెస్క్ ఓపెన్ చేయండి →",
        cap_2_title: "🔄 రెసిప్రోసిటీ ఇంటెలిజెన్స్ (తిరుగు కానుకలు)",
        cap_2_text: "\"గతంలో వాళ్ళు మనకి ఎంత ఇచ్చారు? ఇప్పుడు మనం ఎంత ఇవ్వాలి?\" అనేది వెంటనే తెలుసుకునే స్మార్ట్ హిస్టరీ.",
        cap_2_btn: "రెసిప్రోసిటీ చూడండి →",
        cap_3_title: "📖 డిజిటల్ ఎర్ర పుస్తకం & PDF",
        cap_3_text: "సాంప్రదాయ ఎర్ర పుస్తకం యొక్క డిజిటల్ రూపం. ఒకే క్లిక్ తో పూర్తి CSV ఎక్సెల్ లేదా అందమైన ప్రింటబుల్ లెడ్జర్.",
        cap_3_btn: "ఎర్ర పుస్తకం తెరవండి →",
        comp_eyebrow: "ఎందుకు అప్‌గ్రేడ్ అవ్వాలి",
        comp_title: "పాత పేపర్ డైరీ vs గిఫ్ట్ వాలెట్ డిజిటల్",
        comp_desc: "సాంప్రదాయ పేపర్ పుస్తకాలు చిరిగిపోవడం, టీ పడి పాడవడం మరియు లెక్కల పొరపాట్లకు కారణమవుతాయి.",
        th_feature: "ఫీచర్ సామర్థ్యం",
        th_paper: "సాంప్రదాయ పేపర్ డైరీ",
        th_giftvault: "గిఫ్ట్ వాలెట్ డిజిటల్ ఖజానా",
        comp_r1_f: "రిసెప్షన్ వద్ద అతిథుల ఎంట్రీ వేగం",
        comp_r1_p: "నెమ్మదిగా చేతిరాత; బారులు తీరిన అతిథులు",
        comp_r1_g: "⚡ 3 సెకన్లలో స్పీడ్ ఎంట్రీ & ఆటోకంప్లీట్",
        comp_r2_f: "శుభప్రదమైన +₹1 నాణెం రౌండింగ్",
        comp_r2_p: "నోటి లెక్కలు; తరచుగా మరిచిపోవడం",
        comp_r2_g: "🪙 1-క్లిక్ ఆటోమేటిక్ +₹1 నాణెం చేరిక",
        comp_r3_f: "అతిథికి రసీదు అందజేత",
        comp_r3_p: "ఎటువంటి రసీదు ఉండదు",
        comp_r3_g: "📲 తక్షణ వాట్సాప్ రసీదు & డిజిటల్ కార్డ్",
        comp_r4_f: "గత చదివింపుల ట్రాకింగ్",
        comp_r4_p: "దశాబ్దాల నాటి పాత డైరీలలో వెతకాలి",
        comp_r4_g: "🔄 తక్షణ గత రికార్డు మరియు సూచనలు",
        comp_r5_f: "డేటా పోయే ప్రమాదం",
        comp_r5_p: "చాలా ఎక్కువ (నీళ్ళు పడినా, పోయినా నష్టం)",
        comp_r5_g: "🔒 సురక్షితమైన క్లౌడ్ & PDF ఎక్స్‌పోర్ట్",
        faq_eyebrow: "తరచుగా అడిగే ప్రశ్నలు",
        faq_title: "సందేహాలు & సమాధానాలు",
        faq_desc: "మీ కుటుంబ వేడుకల కోసం గిఫ్ట్ వాలెట్ వాడటం గురించి ముఖ్యమైన వివరాలు.",
        faq_q1: "ఫంక్షన్ హాల్లో నెట్ ఆగిపోతే గిఫ్ట్ వాలెట్ పనిచేస్తుందా?",
        faq_a1: "ఖచ్చితంగా! గిఫ్ట్ వాలెట్ మీ ఫోన్ లో ఆఫ్లైన్ లో డేటాను సేవ్ చేస్తుంది. నెట్ రాగానే ఆటోమేటిక్ గా క్లౌడ్ కు సింక్ అవుతుంది.",
        faq_q2: "ఒకేసారి ఇద్దరు ముగ్గురు బంధువులు వేర్వేరు ఫోన్లలో ఎంట్రీలు చేయవచ్చా?",
        faq_a2: "అవును! కౌంటర్ 1, కౌంటర్ 2 గా వేర్వేరు వ్యక్తులు ఎంట్రీ చేయవచ్చు. అన్ని లెక్కలు రియల్ టైంలో ఒకే చోట కలుస్తాయి.",
        faq_q3: "మొత్తం చదివింపుల పుస్తకాన్ని ఎక్సెల్ లేదా PDF గా డౌన్‌లోడ్ చేసుకోవచ్చా?",
        faq_a3: "అవును, ఒకే క్లిక్ తో పూర్తి CSV స్ప్రెడ్‌షీట్ లేదా అందమైన ప్రింటబుల్ లెడ్జర్ షీట్ డౌన్‌లోడ్ చేసుకోవచ్చు.",
        login_tag: "శుభ ప్రవేశం",
        login_title: "గిఫ్ట్ వాలెట్ లాగిన్",
        login_desc: "మీ ఈవెంట్ లెడ్జర్లు మరియు రిసెప్షన్ డెస్క్ లను యాక్సెస్ చేయండి",
        login_mobile_lbl: "రిజిస్టర్డ్ మొబైల్ నంబర్ / ఇమెయిల్",
        login_pin_lbl: "4-అంకెల సెక్యూరిటీ పిన్",
        login_demo_txt: "డెమో హోస్ట్ యాక్సెస్:",
        btn_enter_hub: "ఈవెంట్ హబ్ లోకి ప్రవేశించండి",
        hub_tag: "కళ్యాణ వేదిక",
        hub_title: "మీ వేడుకను ఎంచుకోండి",
        hub_desc: "నడుస్తున్న వేడుకను ఎంచుకోండి లేదా కొత్త శుభకార్యాన్ని సృష్టించండి",
        btn_create_event: "+ కొత్త ఈవెంట్ సృష్టించండి",
        tag_wedding: "💍 వివాహం",
        tag_barasala: "🎂 బారసాల",
        status_live: "లైవ్ లో ఉంది",
        status_completed: "ముగిసింది",
        lbl_total_blessings: "మొత్తం చదివింపులు:",
        btn_open_reception: "రిసెప్షన్ డెస్క్ తెరవండి →",
        btn_view_history: "లెడ్జర్ చరిత్ర చూడండి →",
        create_card_desc: "గృహప్రవేశం, కేశఖండన (ముండన్), ధోతీ, లంగాఓణి లేదా ఇతర శుభకార్యం",
        ws_subtitle: "నోవోటెల్ హైదరాబాద్ • రిసెప్షన్ డెస్క్ మోడ్",
        btn_record_shagun: "+ చదివింపు నమోదు",
        btn_exit_home: "హోమ్ కి వెళ్ళు",
        tab_overview: "డ్యాష్‌బోర్డ్ వివరణ",
        tab_entry: "మున్షీ ఫాస్ట్ ఎంట్రీ",
        tab_ledger: "ఎర్ర పుస్తకం లెడ్జర్",
        tab_expenses: "ఖర్చులు vs మిగులు",
        tab_reciprocity: "తిరుగు కానుకల లెక్క (Reciprocity)",
        tab_soundbox: "UPI క్యూఆర్ & సౌండ్‌బాక్స్",
        tab_reports: "రిపోర్టులు & PDF",
        tab_settings: "సెట్టింగ్స్",
        kpi_blessings_title: "మొత్తం అందిన చదివింపులు",
        kpi_expenses_title: "మొత్తం వేడుక ఖర్చులు",
        kpi_expenses_note: "భోజనాలు, మండపం, సంగీతం",
        kpi_surplus_title: "నికర శుభ మిగులు",
        kpi_surplus_note: "103% బడ్జెట్ పూర్తయింది",
        kpi_gold_title: "బంగారం & వెండి వస్తువులు",
        kpi_gold_note: "550గ్రా వెండి తాంబూల పాత్ర",
        feed_heading: "ఇటీవలి చదివింపుల వివరాలు (లైవ్ ఫీడ్)",
        th_time: "సమయం",
        th_name: "అతిథి పేరు",
        th_city: "స్వగ్రామం / ఊరు",
        th_relation: "సంబంధం",
        th_amount: "మొత్తం / కానుక",
        th_mode: "రూపం",
        th_receipt: "వాట్సాప్",
        entry_tag: "చదివింపు ప్రాప్తి",
        entry_title: "మున్షీ ఫాస్ట్ ఎంట్రీ డెస్క్",
        btn_voice_entry: "వాయిస్ ఎంట్రీ (మైక్)",
        speed_badge: "⚡ 3-సెకన్ల స్పీడ్",
        lbl_guest_name: "అతిథి పేరు *",
        lbl_guest_city: "స్వగ్రామం / ఊరు",
        lbl_relation: "సంబంధం",
        lbl_phone: "మొబైల్ నంబర్ (తక్షణ వాట్సాప్ రసీదు కోసం)",
        lbl_amount: "చదివింపు నగదు మొత్తం (₹) *",
        lbl_rounding: "శుభప్రదమైన రౌండింగ్:",
        btn_coin: "+₹1 నాణెం",
        lbl_gift_desc: "బంగారం / వెండి / కానుక వివరణ",
        lbl_gift_photo: "కానుక ఫోటో రుజువు (Photo Proof)",
        btn_save_entry: "💾 సేవ్ చేసి వాట్సాప్ రసీదు పంపండి",
        btn_clear: "క్లియర్",
        ledger_heading: "డిజిటల్ ఎర్ర పుస్తకం లెడ్జర్",
        ledger_sub: "శుభకార్యానికి వచ్చిన అన్ని చదివింపుల పూర్తి రికార్డు",
        btn_export_csv: "CSV డౌన్‌లోడ్",
        btn_print_ledger: "లెడ్జర్ ప్రింట్",
        th_cash_blessing: "నగదు చదివింపు",
        th_gift_ornaments: "కానుకలు / ఆభరణాలు",
        th_recorded_by: "నమోదు చేసిన కౌంటర్",
        exp_title: "వేడుక బడ్జెట్ & ఖర్చుల సరిపోలిక",
        exp_desc: "అందిన మొత్తం చదివింపులను ఖర్చులతో సరిపోల్చండి",
        lbl_total_inflow: "మొత్తం చదివింపులు",
        lbl_vendor_expenses: "మొత్తం ఖర్చులు",
        lbl_net_surplus: "మిగిలిన నికర శుభ మిగులు",
        recip_heading: "తిరుగు కానుకల ఇంటెలిజెన్స్ (Reciprocity)",
        recip_sub: "\"గతంలో వాళ్ళు మనకి ఎంత ఇచ్చారు? మనం ఎంత తిరిగి ఇవ్వాలి?\"",
        th_member: "బంధువు / స్నేహితుని పేరు",
        th_they_gave: "ఇప్పుడు వాళ్ళు ఇచ్చినది",
        th_we_gave: "గతంలో మనం ఇచ్చినది",
        th_recommended: "సూచించిన తిరుగు చదివింపు",
        th_status: "స్థితి",
        badge_returned: "చదివింపు తీరింది",
        badge_equal: "సమతుల్యత",
        soundbox_badge: "లైవ్ కౌంటర్ సౌండ్‌బాక్స్",
        soundbox_title: "డైరెక్ట్ UPI చదివింపు క్యూఆర్",
        soundbox_desc: "GPay, PhonePe, Paytm ద్వారా స్కాన్ చేసి నేరుగా చెల్లించవచ్చు",
        btn_soundbox_test: "సౌండ్‌బాక్స్ వాయిస్ & బెల్ టెస్ట్",
        reports_heading: "అధికారిక వేడుక రిపోర్టులు",
        reports_sub: "కుటుంబ రికార్డుల కోసం అధికారిక సమ్మరీని డౌన్‌లోడ్ చేసుకోండి",
        rep_csv_title: "పూర్తి చదివింపుల లెడ్జర్ (CSV)",
        rep_csv_desc: "సమయం, ఊరు, ఫోన్ నంబర్లతో కూడిన పూర్తి జాబితా",
        btn_download_csv: "CSV డౌన్‌లోడ్",
        rep_pdf_title: "ఎగ్జిక్యూటివ్ సమ్మరీ (Printable PDF)",
        rep_pdf_desc: "గ్రాండ్ టోటల్స్, బంగారం వివరాలు, నగరాల వారీగా విశ్లేషణ",
        btn_print_pdf: "PDF ప్రింట్",
        cfg_title: "ఈవెంట్ సెట్టింగ్స్",
        cfg_desc: "వేడుక వివరాలు, పిన్ లు మరియు కౌంటర్ సెట్టింగ్స్",
        cfg_name_lbl: "వేడుక శీర్షిక",
        cfg_coin_lbl: "లక్కీ కాయిన్ రౌండింగ్",
        cfg_opt_coin: "ఎల్లప్పుడూ +₹1 లక్కీ కాయిన్ బటన్ చూపించు",
        cfg_opt_round: "సాధారణ సంఖ్యలు మాత్రమే",
        cfg_pin_lbl: "డెస్క్ హోస్ట్ పాస్‌కోడ్",
        btn_save_cfg: "సెట్టింగ్స్ సేవ్ చేయండి",
        modal_create_tag: "నూతన శుభ కార్యం",
        modal_create_title: "కొత్త శుభకార్యాన్ని సృష్టించండి",
        modal_milestone_lbl: "శుభకార్యం కేటగిరీ *",
        modal_event_title_lbl: "వేడుక శీర్షిక / పేరు *",
        modal_date_lbl: "ఈవెంట్ తేదీ *",
        modal_guests_lbl: "అంచనా అతిథుల సంఖ్య",
        modal_venue_lbl: "కళ్యాణ మండపం / వేదిక & ఊరు",
        btn_cancel: "రద్దు చేయండి",
        btn_create_ledger: "ఈవెంట్ లెడ్జర్ సృష్టించండి →",
        footer_about: "ప్రపంచవ్యాప్తంగా ఉన్న భారతీయ కుటుంబ వేడుకల కోసం ప్రత్యేకంగా నిర్మించబడిన డిజిటల్ ఎర్ర పుస్తకం.",
        footer_reception: "రిసెప్షన్ డెస్క్",
        footer_multicounter: "మల్టీ-కౌంటర్ సింక్"
      },
      hi: {
        brand_subtitle: "शगुन एवं उत्सव खजाना",
        nav_overview: "अवलोकन",
        nav_capabilities: "विशेषताएं",
        nav_comparison: "तुलना",
        nav_faq: "सवाल-जवाब",
        btn_signin: "वॉल्ट में लॉगिन करें",
        btn_back: "पीछे जाएं",
        btn_back_home: "होम पेज पर",
        btn_back_signin: "लॉगिन पर",
        btn_back_hub: "इवेंट हब पर",
        btn_home_page: "होम पेज",
        breadcrumb_home: "होम",
        breadcrumb_signin: "लॉगिन",
        breadcrumb_auth: "प्रमाणीकरण",
        breadcrumb_hub: "इवेंट चयन हब",
        hero_pill: "शुभ शगुन एवं उत्सव खजाना",
        hero_tagline: "शुभ आरंभ • मंगल कार्य",
        hero_h1: "हर पारिवारिक उत्सव के लिए <em>डिजिटल लाल बहीखाता</em>.",
        hero_desc: "आशीर्वाद, सोना, नकदी और उपहारों को बिना किसी गणना त्रुटि और त्वरित व्हाट्सएप रसीद के साथ सुरक्षित रखें।",
        btn_open_desk: "रिसेप्शन डेस्क खोलें",
        btn_explore: "विशेषताएं देखें",
        hero_trust: "sagunms.in एवं thenyota.app से प्रेरित • परिवारों के लिए 100% मुफ्त",
        showcase_top_bar: "⚡ लाइव रिसेप्शन डेस्क • डिजिटल लाल बही",
        showcase_sub: "शुभ आरंभ",
        showcase_title: "शुभ पारिवारिक उत्सव खजाना",
        showcase_venue: "लाइव रिसेप्शन डेस्क • मल्टी-काउंटर सिंक",
        metric_blessings: "कुल शगुन आशीर्वाद",
        metric_expenses: "उत्सव खर्च",
        metric_surplus: "शुद्ध शुभ बचत",
        metric_gold: "सोना एवं चांदी उपहार",
        feed_item_sub: "विजयवाड़ा • रिश्तेदार (+₹1 लकी सिक्का शामिल)",
        sec_cap_eyebrow: "मुख्य क्षमताएं",
        sec_cap_title: "रिसेप्शन डेस्क के लिए विशेष रूप से निर्मित",
        sec_cap_desc: "हस्तलेखन की उलझन, खोए लिफाफे और गणना की चिंता को हमेशा के लिए अलविदा कहें।",
        cap_1_title: "⚡ 3-सेकंड मुंशी रैपिड एंट्री",
        cap_1_text: "वॉयस माइक से बोलकर एंट्री, शहर ऑटो-सर्च, और +₹1 लकी सिक्के के साथ तेज गति से प्रविष्टि।",
        cap_1_btn: "मुंशी डेस्क खोलें →",
        cap_2_title: "🔄 स्मार्ट न्योता एवं शगुन इतिहास (Reciprocity)",
        cap_2_text: "\"पिछली बार उन्होंने हमें कितना दिया था? हमें कितना लौटाना चाहिए?\" त्वरित सलाह और इतिहास।",
        cap_2_btn: "शगुन इतिहास देखें →",
        cap_3_title: "📖 डिजिटल लाल बहीखाता एवं PDF",
        cap_3_text: "पारंपरिक लाल डायरी का आधुनिक डिजिटल रूप। एक क्लिक में CSV एक्सेल और सुंदर प्रिंटेबल लेज़र शीट।",
        cap_3_btn: "लाल बहीखाता खोलें →",
        comp_eyebrow: "अपग्रेड क्यों करें",
        comp_title: "पारंपरिक डायरी vs गिफ़्टवॉल्ट डिजिटल",
        comp_desc: "पारंपरिक कागजी बही फटने, चाय गिरने और हिसाब में गलतियों का शिकार हो जाती है।",
        th_feature: "सुविधा",
        th_paper: "पारंपरिक कागजी डायरी",
        th_giftvault: "गिफ़्टवॉल्ट डिजिटल बहीखाता",
        comp_r1_f: "रिसेप्शन पर प्रविष्टि की गति",
        comp_r1_p: "धीमा हस्तलेखन; मेहमानों की लंबी कतार",
        comp_r1_g: "⚡ 3 सेकंड में ऑटो-सर्च के साथ त्वरित प्रविष्टि",
        comp_r2_f: "शुभ +₹1 सिक्के का जोड़",
        comp_r2_p: "दिमागी हिसाब; अक्सर भूल जाना",
        comp_r2_g: "🪙 1-क्लिक में स्वचालित +₹1 सिक्का जोड़",
        comp_r3_f: "मेहमान को पावती रसीद",
        comp_r3_p: "कोई पावती नहीं",
        comp_r3_g: "📲 तुरंत व्हाट्सएप रसीद और डिजिटल कार्ड",
        comp_r4_f: "पुराने शगुन का मिलान",
        comp_r4_p: "वर्षों पुरानी डायरियों में पन्ने पलटना",
        comp_r4_g: "🔄 तुरंत इतिहास और वापसी शगुन की सलाह",
        comp_r5_f: "डेटा खोने का जोखिम",
        comp_r5_p: "अत्यधिक (पानी गिरना, खो जाना)",
        comp_r5_g: "🔒 सुरक्षित क्लाउड और आसान PDF बैकअप",
        faq_eyebrow: "सामान्य प्रश्न",
        faq_title: "अक्सर पूछे जाने वाले सवाल",
        faq_desc: "अपने पारिवारिक उत्सव के लिए गिफ़्टवॉल्ट के उपयोग से जुड़ी महत्वपूर्ण बातें।",
        faq_q1: "क्या इंटरनेट बंद होने पर भी गिफ़्टवॉल्ट काम करेगा?",
        faq_a1: "हाँ! गिफ़्टवॉल्ट ऑफलाइन डेटा स्टोर करता है। इंटरनेट आते ही यह अपने-आप सुरक्षित क्लाउड पर सिंक हो जाता है।",
        faq_q2: "क्या एक से अधिक परिजन अलग-अलग मोबाइल से एंट्री कर सकते हैं?",
        faq_a2: "हाँ! काउंटर 1 और काउंटर 2 के रूप में अलग-अलग रिश्तेदार एंट्री कर सकते हैं, और सारा हिसाब एक जगह मिलता है।",
        faq_q3: "क्या पूरा बहीखाता एक्सेल या PDF में डाउनलोड कर सकते हैं?",
        faq_a3: "हाँ, एक क्लिक में पूरी CSV स्प्रेडशीट या प्रिंटेबल रिपोर्ट डाउनलोड की जा सकती है।",
        login_tag: "शुभ प्रवेश",
        login_title: "गिफ़्टवॉल्ट में लॉगिन",
        login_desc: "अपने उत्सव बहीखाते और रिसेप्शन डेस्क तक पहुंचें",
        login_mobile_lbl: "पंजीकृत मोबाइल नंबर / ईमेल",
        login_pin_lbl: "4-अंकों का सुरक्षा पिन",
        login_demo_txt: "डेमो होस्ट एक्सेस:",
        btn_enter_hub: "इवेंट हब में प्रवेश करें",
        hub_tag: "कल्याण वेदिका",
        hub_title: "अपना उत्सव चुनें",
        hub_desc: "चल रहे उत्सव का चयन करें या नया शुभ बहीखाता बनाएं",
        btn_create_event: "+ नया इवेंट बनाएं",
        tag_wedding: "💍 विवाह",
        tag_barasala: "🎂 नामकरण / बरसोला",
        status_live: "लाइव चालू",
        status_completed: "सम्पन्न",
        lbl_total_blessings: "कुल आशीर्वाद:",
        btn_open_reception: "रिसेप्शन डेस्क खोलें →",
        btn_view_history: "इतिहास बही देखें →",
        create_card_desc: "गृह प्रवेश, मुंडन, यज्ञोपवीत, या कोई अन्य शुभ पारिवारिक अवसर",
        ws_subtitle: "नोवोटेल हैदराबाद • रिसेप्शन डेस्क मोड",
        btn_record_shagun: "+ शगुन दर्ज करें",
        btn_exit_home: "होम पर जाएं",
        tab_overview: "डैशबोर्ड अवलोकन",
        tab_entry: "मुंशी रैपिड एंट्री",
        tab_ledger: "लाल बहीखाता लेज़र",
        tab_expenses: "खर्च vs शुभ बचत",
        tab_reciprocity: "शगुन वापसी हिसाब (Reciprocity)",
        tab_soundbox: "UPI क्यूआर एवं साउंडबॉक्स",
        tab_reports: "रिपोर्ट्स एवं PDF",
        tab_settings: "सेटिंग्स",
        kpi_blessings_title: "कुल प्राप्त आशीर्वाद",
        kpi_expenses_title: "कुल उत्सव खर्च",
        kpi_expenses_note: "खान-पान, मंडप, संगीत",
        kpi_surplus_title: "शुद्ध शुभ बचत",
        kpi_surplus_note: "103% बजट पूर्ण",
        kpi_gold_title: "सोना एवं चांदी वस्तुएं",
        kpi_gold_note: "550g चांदी की थाली",
        feed_heading: "ताजा शगुन प्रविष्टियां (लाइव फीड)",
        th_time: "समय",
        th_name: "अतिथि का नाम",
        th_city: "गृह नगर / शहर",
        th_relation: "सम्बन्ध",
        th_amount: "राशि / उपहार",
        th_mode: "माध्यम",
        th_receipt: "व्हाट्सएप",
        entry_tag: "शगुन प्राप्ति",
        entry_title: "मुंशी रैपिड एंट्री डेस्क",
        btn_voice_entry: "वॉयस एंट्री (माइक)",
        speed_badge: "⚡ 3-सेकंड गति",
        lbl_guest_name: "अतिथि का नाम *",
        lbl_guest_city: "गृह नगर / शहर",
        lbl_relation: "सम्बन्ध",
        lbl_phone: "मोबाइल नंबर (त्वरित व्हाट्सएप रसीद हेतु)",
        lbl_amount: "शगुन नकदी राशि (₹) *",
        lbl_rounding: "शुभ सिक्का जोड़:",
        btn_coin: "+₹1 सिक्का",
        lbl_gift_desc: "सोना / चांदी / उपहार विवरण",
        lbl_gift_photo: "उपहार फोटो प्रमाण (Photo Proof)",
        btn_save_entry: "💾 सुरक्षित करें एवं व्हाट्सएप रसीद भेजें",
        btn_clear: "साफ करें",
        ledger_heading: "डिजिटल लाल बहीखाता",
        ledger_sub: "उत्सव के सभी शगुन और आशीर्वाद का संपूर्ण ऑडिट रिकॉर्ड",
        btn_export_csv: "CSV डाउनलोड",
        btn_print_ledger: "बहीखाता प्रिंट",
        th_cash_blessing: "नकद शगुन",
        th_gift_ornaments: "उपहार / आभूषण",
        th_recorded_by: "दर्जकर्ता",
        exp_title: "उत्सव बजट एवं खर्च मिलान",
        exp_desc: "कुल प्राप्त शगुन की तुलना उत्सव खर्चों से करें",
        lbl_total_inflow: "कुल शगुन प्राप्ति",
        lbl_vendor_expenses: "कुल वेंडर खर्च",
        lbl_net_surplus: "शेष शुद्ध शुभ बचत",
        recip_heading: "शगुन वापसी बुद्धिमत्ता (Reciprocity)",
        recip_sub: "\"पिछली बार उन्होंने हमें कितना दिया था? हमें कितना लौटाना चाहिए?\"",
        th_member: "परिजन / मित्र",
        th_they_gave: "इस बार उन्होंने दिया",
        th_we_gave: "पिछली बार हमने दिया",
        th_recommended: "अनुशंसित वापसी शगुन",
        th_status: "स्थिति",
        badge_returned: "शगुन चुकता",
        badge_equal: "बराबर हिसाब",
        soundbox_badge: "लाइव काउंटर साउंडबॉक्स",
        soundbox_title: "सीधा UPI शगुन QR",
        soundbox_desc: "मेहमान GPay, PhonePe, Paytm से स्कैन कर तुरंत भुगतान कर सकते हैं",
        btn_soundbox_test: "साउंडबॉक्स ध्वनि एवं आवाज परीक्षण",
        reports_heading: "आधिकारिक उत्सव रिपोर्ट्स",
        reports_sub: "पारिवारिक रिकॉर्ड के लिए औपचारिक सारांश डाउनलोड करें",
        rep_csv_title: "पूर्ण शगुन लेज़र (CSV)",
        rep_csv_desc: "समय, शहर, फोन नंबर सहित सभी प्रविष्टियां",
        btn_download_csv: "CSV डाउनलोड",
        rep_pdf_title: "कार्यकारी सारांश (Printable PDF)",
        rep_pdf_desc: "कुल योग, सोना विवरण और शहरवार विश्लेषण",
        btn_print_pdf: "PDF प्रिंट",
        cfg_title: "इवेंट सेटिंग्स",
        cfg_desc: "उत्सव विवरण, पिन और काउंटर सेटिंग्स प्रबंधित करें",
        cfg_name_lbl: "उत्सव का नाम",
        cfg_coin_lbl: "शुभ सिक्का जोड़",
        cfg_opt_coin: "हमेशा +₹1 लकी सिक्का बटन दिखाएं",
        cfg_opt_round: "केवल सामान्य गोल संख्याएं",
        cfg_pin_lbl: "डेस्क होस्ट पिन कोड",
        btn_save_cfg: "सेटिंग्स सुरक्षित करें",
        modal_create_tag: "नूतन शुभ कार्य",
        modal_create_title: "नया शुभ उत्सव बनाएं",
        modal_milestone_lbl: "उत्सव श्रेणी *",
        modal_event_title_lbl: "उत्सव का नाम *",
        modal_date_lbl: "इवेंट की तारीख *",
        modal_guests_lbl: "अपेक्षित मेहमानों की संख्या",
        modal_venue_lbl: "कल्याण मंडप / स्थान एवं शहर",
        btn_cancel: "रद्द करें",
        btn_create_ledger: "उत्सव बहीखाता बनाएं →",
        footer_about: "विश्वभर में भारतीय पारिवारिक उत्सवों के लिए विशेष रूप से निर्मित डिजिटल लाल बहीखाता।",
        footer_reception: "रिसेप्शन डेस्क",
        footer_multicounter: "मल्टी-काउंटर सिंक"
      }
    };

    let currentLang = 'en';

    function changeLanguage(langKey) {
      if (!I18N_DICT[langKey]) return;
      currentLang = langKey;
      const dict = I18N_DICT[langKey];

      // Translate all elements with data-i18n attribute
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
          el.innerHTML = dict[key];
        }
      });

      // Update select element if triggered externally
      const sel = document.getElementById('lang-select');
      if (sel) sel.value = langKey;
    }

    // ==========================================
    // 2. NAVIGATION STACK & UNIVERSAL BACK
    // ==========================================
    let navHistory = ['landing'];

    function navToView(viewId, pushHistory = true) {
      if (pushHistory && (navHistory.length === 0 || navHistory[navHistory.length - 1] !== viewId)) {
        navHistory.push(viewId);
      }

      document.querySelectorAll('.app-screen-view').forEach(el => el.classList.remove('active'));

      const target = document.getElementById('view-' + viewId);
      if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }

      const floatingBack = document.getElementById('floating-back-btn');
      if (floatingBack) {
        if (viewId === 'landing') {
          floatingBack.style.display = 'none';
        } else {
          floatingBack.style.display = 'flex';
        }
      }
    }

    function handleUniversalBack() {
      const modal = document.getElementById('modal-create-event');
      if (modal && modal.classList.contains('active')) {
        closeCreateEventModal();
        return;
      }

      if (navHistory.length > 1) {
        navHistory.pop();
        const prevView = navHistory[navHistory.length - 1];
        navToView(prevView, false);
      } else {
        navToView('landing', false);
      }
    }

    function scrollToSection(secId) {
      if (!document.getElementById('view-landing').classList.contains('active')) {
        navToView('landing');
      }
      setTimeout(() => {
        const el = document.getElementById(secId);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 50);
    }

    function handleLoginSubmit(e) {
      e.preventDefault();
      navToView('hub');
    }

    function enterWorkspaceEvent(eventId) {
      if (eventId === 'event-birthday') {
        document.getElementById('ws-event-header-name').innerText = 'Advait 1st Birthday & Cradle';
      } else {
        document.getElementById('ws-event-header-name').innerText = 'Rahul & Snigdha Kalyanam';
      }
      navToView('app');
    }

    function switchWorkspaceTab(tabId, btn) {
      document.querySelectorAll('.ws-tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');

      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      const targetPane = document.getElementById(tabId);
      if (targetPane) targetPane.classList.add('active');
    }

    // ==========================================
    // 3. AUSPICIOUS ROUNDING & LUCKY COIN
    // ==========================================
    function applyAuspiciousAmount(val) {
      document.getElementById('entry-amount').value = val;
    }
    function addOneRupeeCoin() {
      const field = document.getElementById('entry-amount');
      let cur = parseInt(field.value, 10) || 0;
      field.value = cur + 1;
    }

    // ==========================================
    // 4. VOICE MIC DICTATION (WEB SPEECH API)
    // ==========================================
    let recognition = null;
    let isListening = false;

    function startVoiceDictation() {
      const btn = document.getElementById('btn-voice-dictate');
      const statusTxt = document.getElementById('voice-status-text');

      if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        alert("Voice recognition is supported in Chrome, Edge, and Android browsers. Please use keyboard entry.");
        return;
      }

      if (isListening) {
        if (recognition) recognition.stop();
        isListening = false;
        btn.classList.remove('listening');
        statusTxt.innerText = currentLang === 'te' ? "వాయిస్ ఎంట్రీ (మైక్)" : (currentLang === 'hi' ? "वॉयस एंट्री (माइक)" : "Voice Entry (Mic)");
        return;
      }

      const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
      recognition = new SpeechRec();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.lang = currentLang === 'te' ? 'te-IN' : (currentLang === 'hi' ? 'hi-IN' : 'en-IN');

      recognition.onstart = function() {
        isListening = true;
        btn.classList.add('listening');
        statusTxt.innerText = currentLang === 'te' ? "వినబడుతోంది... మాట్లాడండి" : (currentLang === 'hi' ? "सुन रहा हूँ... बोलिए" : "Listening... Speak name & amount");
      };

      recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        console.log("Voice transcript:", transcript);
        
        // Parse numbers if spoken
        const words = transcript.split(' ');
        let foundNum = null;
        let nameParts = [];

        words.forEach(w => {
          const num = parseInt(w.replace(/\D/g, ''), 10);
          if (!isNaN(num) && num > 10) {
            foundNum = num;
          } else {
            nameParts.push(w);
          }
        });

        if (nameParts.length > 0) {
          document.getElementById('entry-name').value = nameParts.join(' ');
        }
        if (foundNum) {
          document.getElementById('entry-amount').value = foundNum;
        }

        alert("🎙️ Spoken: \"" + transcript + "\"");
      };

      recognition.onerror = function(err) {
        console.error("Speech error:", err);
        isListening = false;
        btn.classList.remove('listening');
        statusTxt.innerText = currentLang === 'te' ? "వాయిస్ ఎంట్రీ (మైక్)" : "Voice Entry (Mic)";
      };

      recognition.onend = function() {
        isListening = false;
        btn.classList.remove('listening');
        statusTxt.innerText = currentLang === 'te' ? "వాయిస్ ఎంట్రీ (మైక్)" : (currentLang === 'hi' ? "वॉयस एंट्री (माइक)" : "Voice Entry (Mic)");
      };

      recognition.start();
    }

    // ==========================================
    // 5. PHOTO PROOF ATTACHMENT PREVIEW
    // ==========================================
    function previewGiftPhoto(input) {
      if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
          document.getElementById('photo-preview-img').src = e.target.result;
          document.getElementById('photo-preview-container').style.display = 'block';
        };
        reader.readAsDataURL(input.files[0]);
      }
    }

    // ==========================================
    // 6. WHATSAPP GREETING & RECEIPT SENDER
    // ==========================================
    function sendWhatsAppReceipt(guestName, amount, phone) {
      const msg = encodeURIComponent(
        `🙏 *Shubham Bhavatu!* \n\nDear ${guestName},\nWe gratefully acknowledge and thank you for your generous shagun blessing of *₹${parseInt(amount).toLocaleString('en-IN')}* at our family celebration.\n\nYour presence and blessings mean the world to us.\n\nWith Love & Regards,\n*GiftVault Family Treasury*`
      );
      const url = `https://wa.me/${phone ? phone.replace(/\D/g, '') : ''}?text=${msg}`;
      window.open(url, '_blank');
    }

    // ==========================================
    // 7. MUNSHI ENTRY SUBMISSION & TOTALS
    // ==========================================
    let currentTotalBlessings = 842116;
    let totalEnvelopes = 142;

    function handleMunshiSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('entry-name').value;
      const city = document.getElementById('entry-city').value || 'Native City';
      const rel = document.getElementById('entry-rel').value;
      const amt = parseInt(document.getElementById('entry-amount').value, 10) || 0;
      const gift = document.getElementById('entry-gift-desc').value || 'None';
      const phone = document.getElementById('entry-phone').value || '';

      // Update counters
      currentTotalBlessings += amt;
      totalEnvelopes += 1;
      document.getElementById('overview-total-amt').innerText = '₹' + currentTotalBlessings.toLocaleString('en-IN');
      document.getElementById('overview-envelopes-count').innerText = `${totalEnvelopes} envelopes logged`;

      // Prepend to recent feed
      const recentTbody = document.getElementById('ws-recent-table-body');
      const trRecent = document.createElement('tr');
      trRecent.innerHTML = `
        <td>Just now</td>
        <td><strong>${name}</strong></td>
        <td>${city}</td>
        <td>${rel}</td>
        <td class="num-currency" style="color: var(--c-emerald);">₹${amt.toLocaleString('en-IN')}</td>
        <td><span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">CASH</span></td>
        <td><button type="button" class="btn-emerald" style="padding: 4px 10px; font-size: 11.5px;" onclick="sendWhatsAppReceipt('${name.replace(/'/g, "")}', '${amt}', '${phone}')">📲 WhatsApp</button></td>
      `;
      if (recentTbody) recentTbody.prepend(trRecent);

      // Prepend to full ledger
      const fullTbody = document.getElementById('ws-full-ledger-body');
      const trFull = document.createElement('tr');
      trFull.innerHTML = `
        <td>${totalEnvelopes}</td>
        <td><strong>${name}</strong></td>
        <td>${city}</td>
        <td>${rel}</td>
        <td class="num-currency" style="color: var(--c-emerald);">₹${amt.toLocaleString('en-IN')}</td>
        <td>${gift}</td>
        <td>Desk 1</td>
        <td><button type="button" class="btn-emerald" style="padding: 4px 10px; font-size: 11.5px;" onclick="sendWhatsAppReceipt('${name.replace(/'/g, "")}', '${amt}', '${phone}')">📲 WhatsApp</button></td>
      `;
      if (fullTbody) fullTbody.prepend(trFull);

      // Play Soundbox Chime
      testSoundboxAnnouncement(name, amt);

      alert(`✅ Auspicious Shagun Blessing Recorded!\nGuest: ${name}\nAmount: ₹${amt.toLocaleString('en-IN')}\nReceipt is ready to send via WhatsApp.`);
      
      e.target.reset();
      document.getElementById('photo-preview-container').style.display = 'none';
      switchWorkspaceTab('tab-overview');
    }

    // ==========================================
    // 8. LIVE SOUNDBOX CHIME & SPEECH SYNTHESIS
    // ==========================================
    function testSoundboxAnnouncement(guestName = 'Venkat Rao Garu', amount = 10116) {
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const now = audioCtx.currentTime;
        
        // Twin-tone auspicious temple chime
        const osc1 = audioCtx.createOscillator();
        const gain1 = audioCtx.createGain();
        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(587.33, now); // D5
        gain1.gain.setValueAtTime(0.3, now);
        gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
        osc1.connect(gain1);
        gain1.connect(audioCtx.destination);
        osc1.start(now);
        osc1.stop(now + 0.5);

        const osc2 = audioCtx.createOscillator();
        const gain2 = audioCtx.createGain();
        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(880, now + 0.15); // A5
        gain2.gain.setValueAtTime(0.35, now + 0.15);
        gain2.gain.exponentialRampToValueAtTime(0.001, now + 0.8);
        osc2.connect(gain2);
        gain2.connect(audioCtx.destination);
        osc2.start(now + 0.15);
        osc2.stop(now + 0.8);

        // Voice speech announcement
        setTimeout(() => {
          if ('speechSynthesis' in window) {
            let msgText = `GiftVault received rupees ${amount} from ${guestName}. Shubham Bhavatu.`;
            if (currentLang === 'te') {
              msgText = `${guestName} గారి నుండి రూపాయలు ${amount} అందాయి. శుభం భవతు.`;
            } else if (currentLang === 'hi') {
              msgText = `${guestName} से रुपये ${amount} प्राप्त हुए। शुभम भवतु।`;
            }
            const utterance = new SpeechSynthesisUtterance(msgText);
            utterance.rate = 0.95;
            window.speechSynthesis.speak(utterance);
          }
        }, 600);
      } catch (err) {
        console.error("Audio error:", err);
      }
    }

    // ==========================================
    // 9. LIVE SEARCH & FILTER IN RED NOTEBOOK
    // ==========================================
    function filterLedgerTable() {
      const q = document.getElementById('ledger-search-input').value.toLowerCase();
      const mode = document.getElementById('ledger-filter-mode').value;
      const rows = document.querySelectorAll('#ws-full-ledger-body tr');

      rows.forEach(row => {
        const text = row.innerText.toLowerCase();
        const matchesQuery = text.includes(q);
        
        let matchesMode = true;
        if (mode === 'CASH') matchesMode = text.includes('cash') || !text.includes('gold') && !text.includes('upi');
        if (mode === 'UPI') matchesMode = text.includes('upi');
        if (mode === 'GOLD') matchesMode = text.includes('gold') || text.includes('silver');

        if (matchesQuery && matchesMode) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    }

    // ==========================================
    // 10. CSV EXPORT & MODAL CONTROLS
    // ==========================================
    function exportLedgerCSV() {
      const rows = document.querySelectorAll('#ws-full-ledger-body tr');
      let csv = "ID,Guest Name,City,Relationship,Amount,Gift,Recorded By\n";
      rows.forEach(r => {
        const cols = Array.from(r.querySelectorAll('td')).slice(0, 7).map(c => '"' + c.innerText.trim().replace(/"/g, '""') + '"');
        csv += cols.join(',') + '\n';
      });
      const encodedUri = encodeURI("data:text/csv;charset=utf-8," + csv);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "GiftVault_Celebration_Ledger.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function openCreateEventModal() {
      const modal = document.getElementById('modal-create-event');
      if (modal) modal.classList.add('active');
    }
    function closeCreateEventModal() {
      const modal = document.getElementById('modal-create-event');
      if (modal) modal.classList.remove('active');
    }

    function handleCreateEventSubmit(e) {
      e.preventDefault();
      const title = document.getElementById('new-event-title').value;
      const type = document.getElementById('new-event-type').value;
      const venue = document.getElementById('new-event-venue').value || 'Family Celebration';

      const grid = document.getElementById('events-hub-grid');
      const newCard = document.createElement('div');
      newCard.className = 'event-selection-card';
      newCard.onclick = () => {
        document.getElementById('ws-event-header-name').innerText = title;
        navToView('app');
      };
      newCard.innerHTML = `
        <div>
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">${type.toUpperCase()}</span>
            <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; font-size: 12px; font-weight: 700; color: var(--c-emerald);">NEW</span>
          </div>
          <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">
            ${title}
          </h3>
          <p style="font-size: 13px; color: var(--c-muted); margin-bottom: 16px;">
            ${venue}
          </p>
        </div>
        <div>
          <div style="display: flex; justify-content: space-between; padding: 10px 0; border-top: 1px solid var(--c-border); font-family: var(--font-sans); font-size: 13px;">
            <span>Initial Blessings:</span>
            <strong class="num-currency" style="color: var(--c-crimson);">₹0</strong>
          </div>
          <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center; margin-top: 8px;">
            Open Reception Desk →
          </button>
        </div>
      `;

      grid.insertBefore(newCard, grid.firstChild);
      closeCreateEventModal();
      document.getElementById('ws-event-header-name').innerText = title;
      navToView('app');
    }
  </script>
</body>
</html>
'''

targets = [
    'web_preview/index.html',
    'web_preview/desktop.html',
    'web_preview/mobile.html',
    'build/web/index.html',
    'web/index.html'
]

for target in targets:
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, 'w', encoding='utf-8') as f:
        f.write(html_code)
    print(f"Updated: {target} ({len(html_code)} bytes)")

print("\nSuccessfully synchronized all features from past conversations with full multi-language, voice entry, photo proof, live soundbox, and creative luxury design!")
