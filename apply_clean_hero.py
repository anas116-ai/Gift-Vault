# Script to remove 3 core pillars & wedding/birthday/housewarming from the hero section
# Clean, universal hero focused purely on the Auspicious Digital Red Notebook & Shagun Treasury

import os

html_content = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault | Royal Celebration Ledger & Shagun Treasury</title>
  
  <!-- Option B: Curated 2-Font Luxury Pairing Suite -->
  <!-- 1. Luxury Serif (Headings Only): Playfair Display -->
  <!-- 2. Modern Sans-Serif (Entire UI, Cards, Buttons, Body & Tabular Numbers): Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600;1,700&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       CURATED LUXURY SYSTEM:
       - Font 1 (Headings Only): 'Playfair Display', Georgia, serif
       - Font 2 (Entire UI, Body, Buttons, Currency): 'Plus Jakarta Sans', sans-serif
       - Colors: #000411 (Deep Night), #F8333C (Rose Crimson), #036D19 (Royal Emerald)
       ========================================================================== */
    :root {
      /* Curated Palette */
      --c-night: #000411;         /* Deep Night Slate - Core typography, luxury contrast */
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

      /* Option B Typography Hierarchy */
      --font-serif: 'Playfair Display', Georgia, serif;            /* Major Headings Only */
      --font-sans: 'Plus Jakarta Sans', -apple-system, sans-serif; /* Complete UI, Body & Numbers */

      /* Elevations */
      --shadow-sm: 0 1px 3px rgba(0, 4, 17, 0.05);
      --shadow-md: 0 4px 14px -2px rgba(0, 4, 17, 0.08), 0 2px 6px -1px rgba(0, 4, 17, 0.04);
      --shadow-lg: 0 16px 36px -4px rgba(0, 4, 17, 0.10), 0 6px 14px -2px rgba(0, 4, 17, 0.04);
      --shadow-crimson: 0 8px 24px -4px rgba(248, 51, 60, 0.32);
    }

    /* Reset & Base */
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

    /* Typography Classes */
    .font-serif {
      font-family: var(--font-serif);
      letter-spacing: -0.015em;
    }
    .font-sans {
      font-family: var(--font-sans);
    }
    .num-currency {
      font-family: var(--font-sans);
      font-feature-settings: "tnum" 1, "cv02" 1;
      font-variant-numeric: tabular-nums;
      font-weight: 800;
      letter-spacing: -0.02em;
    }

    /* Universal Floating Side Back Pill (Clean, unobtrusive on left side) */
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
      transition: all 0.2s ease;
    }
    .universal-side-back-btn:hover {
      background: var(--c-crimson);
      border-color: var(--c-crimson);
      transform: translateX(-3px);
    }

    /* Universal Top Back Bar for Inner Screens */
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
    .page-breadcrumb {
      font-family: var(--font-sans);
      font-size: 13px;
      color: var(--c-muted);
      font-weight: 600;
    }
    .page-breadcrumb strong {
      color: var(--c-night);
    }

    /* Primary Navigation Bar */
    .main-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(12px);
      border-bottom: 1.5px solid var(--c-border);
      padding: 14px 32px;
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
      letter-spacing: -0.01em;
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
      gap: 24px;
    }
    .nav-anchor-btn {
      background: none;
      border: none;
      font-family: var(--font-sans);
      font-size: 14.5px;
      font-weight: 600;
      color: var(--c-body-text);
      cursor: pointer;
      transition: color 0.2s ease;
      padding: 6px 4px;
    }
    .nav-anchor-btn:hover {
      color: var(--c-crimson);
    }

    /* Curated Buttons */
    .btn-crimson {
      background: var(--c-crimson);
      color: #FFFFFF;
      border: 1.5px solid var(--c-crimson);
      padding: 11px 22px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: var(--shadow-crimson);
    }
    .btn-crimson:hover {
      background: var(--c-crimson-hover);
      border-color: var(--c-crimson-hover);
      transform: translateY(-1px);
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
    }
    .app-screen-view.active {
      display: block;
    }

    /* ==========================================================================
       VIEW 1: LANDING PAGE (CLEAN HERO WITHOUT EVENT NAMES OR 3 PILLARS SWITCHER)
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

    /* Clean Hero Action CTAs (No occasion names or 3 pillars switcher) */
    .hero-actions-row {
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      margin-bottom: 26px;
    }

    /* Hero Showcase Universal Treasury Card */
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
      transition: transform 0.4s ease;
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
      font-family: var(--font-sans);
      font-feature-settings: "tnum" 1;
      font-variant-numeric: tabular-nums;
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

    /* Core Capabilities Section (Focused on Reception Desk Features) */
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
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .cap-card:hover {
      transform: translateY(-4px);
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
       VIEW 2: LOGIN / AUTH SCREEN (PROMINENT "<- BACK" BAR AT TOP-LEFT)
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
       VIEW 4: IN-APP WORKSPACE (8 INTEGRATED MODULES)
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
      font-family: var(--font-sans);
      font-feature-settings: "tnum" 1;
      font-variant-numeric: tabular-nums;
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

    /* Munshi Entry Card */
    .munshi-entry-card {
      background: #FFFFFF;
      border: 2px solid var(--c-night);
      border-radius: 18px;
      padding: 28px;
      box-shadow: var(--shadow-md);
      max-width: 760px;
      margin: 0 auto;
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
      max-width: 580px;
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
      font-family: var(--font-sans);
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
      .hero-heading { font-size: 36px; }
      .main-nav { padding: 12px 18px; }
    }
  </style>
</head>
<body>

  <!-- Universal Side-Docked Floating Back Button (Appears on non-landing views) -->
  <button id="floating-back-btn" class="universal-side-back-btn" onclick="handleUniversalBack()" title="Go Back">
    <span>←</span>
    <span>Back</span>
  </button>

  <!-- Primary Sticky Navigation Header -->
  <header class="main-nav">
    <div class="brand-group" onclick="navToView('landing')">
      <div class="brand-icon-box">GV</div>
      <div class="brand-titles">
        <span class="brand-name">GiftVault</span>
        <span class="brand-sub">Shagun & Celebration Treasury</span>
      </div>
    </div>

    <nav class="nav-links-wrap" id="landing-nav-links">
      <button type="button" class="nav-anchor-btn" onclick="scrollToSection('hero-section')">Overview</button>
      <button type="button" class="nav-anchor-btn" onclick="scrollToSection('features-section')">Capabilities</button>
      <button type="button" class="nav-anchor-btn" onclick="scrollToSection('comparison-section')">Comparison</button>
      <button type="button" class="nav-anchor-btn" onclick="scrollToSection('faq-section')">FAQ</button>
      <button type="button" class="btn-crimson" onclick="navToView('login')">
        <span>Sign In to Vault</span>
        <span>→</span>
      </button>
    </nav>
  </header>

  <!-- ==========================================================================
       VIEW 1: LANDING PAGE (CLEAN, FOCUSED HERO WITHOUT EVENT NAMES)
       ========================================================================== -->
  <main id="view-landing" class="app-screen-view active">
    
    <!-- Hero Section -->
    <section id="hero-section" class="hero-wrap">
      <div class="hero-grid">
        <div>
          <div class="hero-badge-pill">
            <span class="hero-dot-indicator"></span>
            <span>Auspicious Shagun & Celebration Treasury</span>
          </div>

          <span class="hero-tagline-text">SHUBH AARAMBH • MANGALA KAARYAM</span>
          
          <h1 class="hero-heading">
            The Digital Red Notebook for Every Family <em>Celebration</em>.
          </h1>

          <p class="hero-description">
            Preserve blessings, gold, cash, and gifts with instant WhatsApp receipts and zero calculation errors. Designed specifically for auspicious Indian family celebrations and reception desks.
          </p>

          <!-- Clean Action CTAs (No 3-pillars switcher or occasion names) -->
          <div class="hero-actions-row">
            <button type="button" class="btn-crimson" style="padding: 13px 28px; font-size: 15px;" onclick="navToView('login')">
              <span>Open Reception Desk</span>
              <span>→</span>
            </button>
            <button type="button" class="btn-outline-dark" style="padding: 13px 24px; font-size: 15px;" onclick="scrollToSection('features-section')">
              <span>Explore Capabilities</span>
            </button>
          </div>

          <div style="font-family: var(--font-sans); font-size: 13px; color: var(--c-muted); display: flex; align-items: center; gap: 8px;">
            <span style="color: var(--c-emerald); font-weight: 800;">✓</span>
            <span>Inspired by sagunms.in & thenyota.app • 100% Free for Personal Celebrations</span>
          </div>
        </div>

        <!-- Hero Showcase Universal Treasury Card -->
        <div class="hero-showcase-box">
          <div class="showcase-banner-top">
            <span>⚡ LIVE RECEPTION DESK • DIGITAL RED NOTEBOOK</span>
            <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; color: var(--c-crimson); font-weight: 800;">DESK #01 ACTIVE</span>
          </div>

          <div class="showcase-image-holder">
            <!-- Authentic High-Resolution Indian Auspicious Diya Celebration Photo -->
            <img id="showcase-main-img" src="https://images.unsplash.com/photo-1608755728617-aefab37d2edd?auto=format&fit=crop&w=1200&q=85" alt="Auspicious Celebration Setup">
            <div class="showcase-image-overlay">
              <div class="showcase-tag-sub">SHUBH AARAMBH</div>
              <div class="showcase-event-heading">Auspicious Family Celebration Treasury</div>
              <div class="showcase-venue-text">Live Reception Desk • Multi-Counter Synchronization</div>
            </div>
          </div>

          <!-- Dynamic 4-KPI Grid (Plus Jakarta Sans Tabular Numerals) -->
          <div class="showcase-data-grid">
            <div class="showcase-data-item">
              <div class="showcase-data-label">Total Shagun Blessings</div>
              <div class="showcase-data-val num-currency" id="showcase-inflow-val" style="color: var(--c-crimson);">₹8,42,116</div>
            </div>
            <div class="showcase-data-item">
              <div class="showcase-data-label">Event Expenses</div>
              <div class="showcase-data-val num-currency" id="showcase-expenses-val">₹4,15,000</div>
            </div>
            <div class="showcase-data-item">
              <div class="showcase-data-label">Net Auspicious Surplus</div>
              <div class="showcase-data-val num-currency" id="showcase-surplus-val" style="color: var(--c-emerald);">+₹4,27,116</div>
            </div>
            <div class="showcase-data-item">
              <div class="showcase-data-label">Gold & Silver Articles</div>
              <div class="showcase-data-val num-currency" id="showcase-gold-val">42.5g / 550g</div>
            </div>
          </div>

          <!-- Live Reception Desk Feed Row -->
          <div class="showcase-feed-row">
            <div style="display: flex; align-items: center; gap: 12px;">
              <div class="feed-avatar">VR</div>
              <div>
                <div style="font-family: var(--font-sans); font-size: 13.5px; font-weight: 700; color: var(--c-night);">Venkat Rao Garu</div>
                <div style="font-family: var(--font-sans); font-size: 11.5px; color: var(--c-muted);">Vijayawada • Relatives (+₹1 Lucky Shagun Added)</div>
              </div>
            </div>
            <div class="num-currency" style="font-size: 15px; font-weight: 800; color: var(--c-emerald);">+ ₹10,116</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Capabilities Section (Focused on Reception Desk Engineering) -->
    <section id="features-section" class="section-wrap" style="background: #FFFFFF; border-top: 1.5px solid var(--c-border); border-bottom: 1.5px solid var(--c-border);">
      <div class="section-header-center">
        <span class="section-eyebrow">CORE CAPABILITIES</span>
        <h2 class="section-title">Engineered for the Reception Desk</h2>
        <p class="section-desc">
          Eliminate handwriting confusion, lost envelopes, and mental calculation stress forever with purpose-built digital desk tools.
        </p>
      </div>

      <div class="capabilities-grid">
        <!-- Capability 1 -->
        <div class="cap-card">
          <div>
            <div class="cap-icon">⚡</div>
            <h3 class="cap-title">3-Second Munshi Rapid Entry</h3>
            <p class="cap-text">
              Ultra-fast guest logging with instant city autocomplete, family relationship tags, and automatic +₹1 lucky coin rounding chips.
            </p>
          </div>
          <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center;" onclick="navToView('login')">
            Open Munshi Desk →
          </button>
        </div>

        <!-- Capability 2 -->
        <div class="cap-card">
          <div>
            <div class="cap-icon">🔄</div>
            <h3 class="cap-title">Smart Reciprocity Intelligence</h3>
            <p class="cap-text">
              "How much did they give us last time? How much should we give them back?" Instant gift history retrieval and return shagun suggestions.
            </p>
          </div>
          <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center;" onclick="navToView('login')">
            View Reciprocity Engine →
          </button>
        </div>

        <!-- Capability 3 -->
        <div class="cap-card">
          <div>
            <div class="cap-icon">📖</div>
            <h3 class="cap-title">Digital Red Notebook & PDF</h3>
            <p class="cap-text">
              The modern avatar of the traditional Erra Pusthakam / Shagun Diary. One-click CSV export and beautifully formatted printable ledger sheets.
            </p>
          </div>
          <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center;" onclick="navToView('login')">
            Access Digital Red Book →
          </button>
        </div>
      </div>
    </section>

    <!-- Comparison Table: Traditional Diary vs GiftVault -->
    <section id="comparison-section" class="section-wrap">
      <div class="section-header-center">
        <span class="section-eyebrow">WHY FAMILIES UPGRADE</span>
        <h2 class="section-title">The Traditional Diary vs GiftVault</h2>
        <p class="section-desc">Traditional red books are prone to spilled tea, lost pages, illegible scribbles, and math mistakes.</p>
      </div>

      <div class="comparison-table-wrap">
        <table class="comp-table">
          <thead>
            <tr>
              <th>Feature Capability</th>
              <th>Traditional Paper Diary</th>
              <th>GiftVault Digital Treasury</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Guest Reception Speed</strong></td>
              <td>Slow manual writing; lines back up</td>
              <td>⚡ 3-second entry with city autocomplete</td>
            </tr>
            <tr>
              <td><strong>Auspicious +₹1 Rounding</strong></td>
              <td>Manual mental math; frequently forgotten</td>
              <td>🪙 1-click automatic +₹1 lucky coin addition</td>
            </tr>
            <tr>
              <td><strong>Guest Acknowledgement</strong></td>
              <td>No receipt; guest wonders if logged</td>
              <td>📲 Instant WhatsApp greeting & digital card</td>
            </tr>
            <tr>
              <td><strong>Reciprocity Tracking</strong></td>
              <td>Digging through dusty notebooks from 2018</td>
              <td>🔄 Instant relationship history & return advice</td>
            </tr>
            <tr>
              <td><strong>Data Loss Risk</strong></td>
              <td>High (water damage, misplaced book)</td>
              <td>🔒 Encrypted cloud & instant Excel/PDF export</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- FAQ Section -->
    <section id="faq-section" class="section-wrap" style="background: #FFFFFF; border-top: 1.5px solid var(--c-border);">
      <div class="section-header-center">
        <span class="section-eyebrow">COMMON QUESTIONS</span>
        <h2 class="section-title">Frequently Asked Questions</h2>
        <p class="section-desc">Everything you need to know about using GiftVault for your upcoming family event.</p>
      </div>

      <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 16px;">
        <div style="background: var(--c-base); border: 1.5px solid var(--c-border); border-radius: 12px; padding: 20px;">
          <h4 style="font-family: var(--font-sans); font-size: 16px; font-weight: 700; color: var(--c-night); margin-bottom: 8px;">Does GiftVault work offline if reception hall internet drops?</h4>
          <p style="font-size: 14px; color: var(--c-muted); line-height: 1.6;">Yes! GiftVault caches your entries locally in your browser storage. You can continue recording shagun offline and it will automatically sync once connected.</p>
        </div>
        <div style="background: var(--c-base); border: 1.5px solid var(--c-border); border-radius: 12px; padding: 20px;">
          <h4 style="font-family: var(--font-sans); font-size: 16px; font-weight: 700; color: var(--c-night); margin-bottom: 8px;">Can we have multiple relatives entering gifts simultaneously?</h4>
          <p style="font-size: 14px; color: var(--c-muted); line-height: 1.6;">Yes. You can assign Counter 1 and Counter 2 to different family members on their smartphones, and all entries aggregate into the master ledger in real-time.</p>
        </div>
        <div style="background: var(--c-base); border: 1.5px solid var(--c-border); border-radius: 12px; padding: 20px;">
          <h4 style="font-family: var(--font-sans); font-size: 16px; font-weight: 700; color: var(--c-night); margin-bottom: 8px;">Can we export the complete Red Notebook into Excel or PDF?</h4>
          <p style="font-size: 14px; color: var(--c-muted); line-height: 1.6;">Yes, with a single click you can download a complete CSV spreadsheet or print a beautifully styled traditional ledger sheet for family records.</p>
        </div>
      </div>
    </section>
  </main>

  <!-- ==========================================================================
       VIEW 2: LOGIN / AUTH SCREEN (PROMINENT "<- BACK" BAR AT TOP-LEFT)
       ========================================================================== -->
  <main id="view-login" class="app-screen-view">
    <!-- Dedicated Page Back Navigation Bar -->
    <div class="page-back-nav-bar">
      <button type="button" class="btn-page-back" onclick="navToView('landing')">
        <span>←</span>
        <span>Back to Home</span>
      </button>
      <div class="page-breadcrumb">
        <span>Home</span> &gt; <strong>Sign In</strong>
      </div>
      <div></div>
    </div>

    <div class="login-container-box">
      <div class="login-header-zone">
        <div class="brand-icon-box" style="margin: 0 auto 12px;">GV</div>
        <div class="showcase-tag-sub" style="margin-bottom: 2px;">SHUBH PRAVESH</div>
        <h2>Sign In to GiftVault</h2>
        <p style="font-size: 13.5px; color: var(--c-muted); margin-top: 4px;">Access your auspicious event ledgers and reception desks</p>
      </div>

      <form onsubmit="handleLoginSubmit(event)">
        <div class="form-group-item">
          <label class="form-label-txt" for="login-mobile">Registered Mobile Number / Email</label>
          <input type="text" id="login-mobile" class="form-input-field" value="+91 98480 22338" required>
        </div>

        <div class="form-group-item">
          <label class="form-label-txt" for="login-pin">4-Digit Security PIN</label>
          <input type="password" id="login-pin" class="form-input-field" value="2026" maxlength="6" required>
        </div>

        <div class="auth-demo-credentials">
          <strong>Demo Host Access:</strong> Mobile: <code>+91 98480 22338</code> • PIN: <code>2026</code>
        </div>

        <button type="submit" class="btn-crimson" style="width: 100%; justify-content: center; padding: 13px; font-size: 15px;">
          <span>Enter Event Hub</span>
          <span>→</span>
        </button>
      </form>
    </div>
  </main>

  <!-- ==========================================================================
       VIEW 3: EVENT HUB (SGUNMS.IN STYLE SELECTION + CREATE MODAL)
       ========================================================================== -->
  <main id="view-hub" class="app-screen-view">
    <!-- Dedicated Page Back Navigation Bar -->
    <div class="page-back-nav-bar">
      <button type="button" class="btn-page-back" onclick="navToView('login')">
        <span>←</span>
        <span>Back to Sign In</span>
      </button>
      <div class="page-breadcrumb">
        <span>Home</span> &gt; <span>Auth</span> &gt; <strong>Event Selection Hub</strong>
      </div>
      <button type="button" class="btn-outline-dark" style="padding: 6px 14px; font-size: 12px;" onclick="navToView('landing')">
        Home Page
      </button>
    </div>

    <div class="hub-container-wrap">
      <div class="hub-top-bar">
        <div class="hub-title-block">
          <div class="showcase-tag-sub" style="margin-bottom: 2px;">KALYANA VEDIKA</div>
          <h1>Select Your Celebration</h1>
          <p>Choose an ongoing celebration or create a new auspicious ledger</p>
        </div>
        <button type="button" class="btn-crimson" onclick="openCreateEventModal()">
          <span>+ Create New Event</span>
        </button>
      </div>

      <!-- Events Selection Grid -->
      <div class="events-selection-grid" id="events-hub-grid">
        <!-- Event Card 1: Wedding -->
        <div class="event-selection-card" onclick="enterWorkspaceEvent('event-wedding')">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
              <span class="tag-badge" style="background: var(--c-crimson); color: #FFFFFF;">💍 WEDDING</span>
              <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; font-size: 12px; font-weight: 700; color: var(--c-emerald);">LIVE NOW</span>
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
              <span>Total Blessings:</span>
              <strong class="num-currency" style="color: var(--c-crimson);">₹8,42,116</strong>
            </div>
            <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center; margin-top: 8px;">
              Open Reception Desk →
            </button>
          </div>
        </div>

        <!-- Event Card 2: Birthday -->
        <div class="event-selection-card" onclick="enterWorkspaceEvent('event-birthday')">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
              <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">🎂 BARASALA</span>
              <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; font-size: 12px; font-weight: 700; color: var(--c-muted);">COMPLETED</span>
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
              <span>Total Blessings:</span>
              <strong class="num-currency" style="color: var(--c-crimson);">₹3,18,116</strong>
            </div>
            <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center; margin-top: 8px;">
              View Ledger History →
            </button>
          </div>
        </div>

        <!-- Create New Event Card (sgunms.in pattern) -->
        <div class="create-new-event-card" onclick="openCreateEventModal()">
          <div class="create-icon-circle">+</div>
          <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">
            Create New Event
          </h3>
          <p style="font-size: 13px; color: var(--c-muted); max-width: 260px;">
            Housewarming, Tonsure, Dhoti Ceremony, Half Saree, or Custom Milestone
          </p>
        </div>
      </div>
    </div>
  </main>

  <!-- ==========================================================================
       VIEW 4: IN-APP WORKSPACE (8 INTEGRATED MODULES)
       ========================================================================== -->
  <main id="view-app" class="app-screen-view">
    <!-- Top Event Header with Prominent Back to Hub Button -->
    <div class="workspace-top-header">
      <div class="ws-event-info">
        <button type="button" class="btn-page-back" onclick="navToView('hub')">
          <span>←</span>
          <span>Back to Event Hub</span>
        </button>
        <div>
          <div class="ws-event-title" id="ws-event-header-name">Rahul & Snigdha Kalyanam</div>
          <div style="font-size: 11.5px; color: #CBD5E1; font-family: var(--font-sans);">
            Novotel Hyderabad • Reception Desk Mode
          </div>
        </div>
        <span class="ws-event-badge">LIVE DESK #1</span>
      </div>

      <div style="display: flex; align-items: center; gap: 12px;">
        <button type="button" class="btn-crimson" style="padding: 7px 16px; font-size: 13px;" onclick="switchWorkspaceTab('tab-entry')">
          <span>+ Record Shagun</span>
        </button>
        <button type="button" class="btn-outline-dark" style="color: #FFFFFF; border-color: rgba(255, 255, 255, 0.4); padding: 7px 14px; font-size: 12.5px;" onclick="navToView('landing')">
          Exit to Home
        </button>
      </div>
    </div>

    <!-- 8 Tabs Bar -->
    <nav class="ws-tabs-bar">
      <button type="button" class="ws-tab-btn active" onclick="switchWorkspaceTab('tab-overview', this)">
        <span>📊</span>
        <span>Dashboard Overview</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-entry', this)">
        <span>⚡</span>
        <span>Munshi Rapid Entry</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-ledger', this)">
        <span>📖</span>
        <span>Red Notebook Ledger</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-expenses', this)">
        <span>⚖️</span>
        <span>Expenses vs Surplus</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-reciprocity', this)">
        <span>🔄</span>
        <span>Reciprocity Tracker</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-soundbox', this)">
        <span>🔊</span>
        <span>UPI QR & Soundbox</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-reports', this)">
        <span>📄</span>
        <span>PDF & Reports</span>
      </button>
      <button type="button" class="ws-tab-btn" onclick="switchWorkspaceTab('tab-settings', this)">
        <span>⚙️</span>
        <span>Settings</span>
      </button>
    </nav>

    <!-- Workspace Body Area -->
    <div class="ws-content-body">
      
      <!-- TAB 1: OVERVIEW DASHBOARD -->
      <section id="tab-overview" class="tab-pane active">
        <div class="kpi-cards-grid">
          <div class="kpi-card" style="border-top: 4px solid var(--c-crimson);">
            <div class="kpi-title">Total Blessings Received</div>
            <div class="kpi-value num-currency" style="color: var(--c-crimson);">₹8,42,116</div>
            <div class="kpi-note" style="color: var(--c-emerald);">142 envelopes logged</div>
          </div>
          <div class="kpi-card" style="border-top: 4px solid var(--c-night);">
            <div class="kpi-title">Event Expenses</div>
            <div class="kpi-value num-currency">₹4,15,000</div>
            <div class="kpi-note" style="color: var(--c-muted);">Catering, Mandap, Audio</div>
          </div>
          <div class="kpi-card" style="border-top: 4px solid var(--c-emerald);">
            <div class="kpi-title">Net Auspicious Surplus</div>
            <div class="kpi-value num-currency" style="color: var(--c-emerald);">+₹4,27,116</div>
            <div class="kpi-note" style="color: var(--c-emerald);">103% Budget Covered</div>
          </div>
          <div class="kpi-card" style="border-top: 4px solid var(--c-night);">
            <div class="kpi-title">Gold & Silver Articles</div>
            <div class="kpi-value num-currency">42.5g</div>
            <div class="kpi-note" style="color: var(--c-muted);">550g Silver Thaali</div>
          </div>
        </div>

        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 24px;">
          <h3 style="font-family: var(--font-serif); font-size: 22px; font-weight: 800; color: var(--c-night); margin-bottom: 16px;">
            Recent Shagun Entries (Live Feed)
          </h3>
          <div class="ledger-table-wrap">
            <table class="ledger-table">
              <thead>
                <tr>
                  <th>Timestamp</th>
                  <th>Guest Name</th>
                  <th>Native City</th>
                  <th>Relation</th>
                  <th>Amount / Gift</th>
                  <th>Mode</th>
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
                </tr>
                <tr>
                  <td>10:38 PM</td>
                  <td><strong>Suresh & Malathi Sharma</strong></td>
                  <td>Hyderabad</td>
                  <td>Close Friends</td>
                  <td class="num-currency" style="color: var(--c-emerald);">₹5,116</td>
                  <td><span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">UPI</span></td>
                </tr>
                <tr>
                  <td>10:25 PM</td>
                  <td><strong>K. Raghunath Varma</strong></td>
                  <td>Visakhapatnam</td>
                  <td>Paternal Relative</td>
                  <td class="num-currency" style="color: var(--c-crimson);">10g Gold Coin + ₹2,116</td>
                  <td><span class="tag-badge" style="background: var(--c-crimson); color: #FFFFFF;">GOLD</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 2: MUNSHI RAPID ENTRY -->
      <section id="tab-entry" class="tab-pane">
        <div class="munshi-entry-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <div>
              <div class="showcase-tag-sub" style="margin-bottom: 2px;">SHAGUN PRAAPTI</div>
              <h3 style="font-family: var(--font-serif); font-size: 26px; font-weight: 800; color: var(--c-night);">Munshi Fast Entry Desk</h3>
            </div>
            <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">⚡ 3-SECOND SPEED</span>
          </div>

          <form onsubmit="handleMunshiSubmit(event)">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
              <div class="form-group-item">
                <label class="form-label-txt">Guest Name *</label>
                <input type="text" id="entry-name" class="form-input-field" placeholder="e.g. Anand Kumar Garu" required>
              </div>
              <div class="form-group-item">
                <label class="form-label-txt">Native City / Town</label>
                <input type="text" id="entry-city" class="form-input-field" placeholder="e.g. Hyderabad, Guntur, Rajahmundry">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
              <div class="form-group-item">
                <label class="form-label-txt">Relationship</label>
                <select id="entry-rel" class="form-input-field">
                  <option value="Relatives">Family Relative</option>
                  <option value="Close Friends">Close Friend</option>
                  <option value="Colleague">Colleague / Business</option>
                  <option value="Neighbor">Neighbor</option>
                  <option value="Other">Other Well-Wisher</option>
                </select>
              </div>
              <div class="form-group-item">
                <label class="form-label-txt">Guest Mobile (WhatsApp Receipt)</label>
                <input type="tel" id="entry-phone" class="form-input-field" placeholder="+91 98480 XXXXX">
              </div>
            </div>

            <div class="form-group-item">
              <label class="form-label-txt">Cash Amount (₹) *</label>
              <input type="number" id="entry-amount" class="form-input-field num-currency" placeholder="5000" style="font-size: 18px; font-weight: 700;" required>
              
              <!-- Auspicious +₹1 Lucky Coin Bar -->
              <div class="lucky-one-chip-bar">
                <span style="font-family: var(--font-sans); font-size: 11.5px; font-weight: 700; align-self: center; color: var(--c-muted);">Auspicious Rounding:</span>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(501)">₹501</button>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(1116)">₹1,116</button>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(2116)">₹2,116</button>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(5116)">₹5,116</button>
                <button type="button" class="lucky-coin-chip" onclick="applyAuspiciousAmount(10116)">₹10,116</button>
                <button type="button" class="lucky-coin-chip" onclick="addOneRupeeCoin()">+₹1 Coin</button>
              </div>
            </div>

            <div class="form-group-item">
              <label class="form-label-txt">Gold / Silver / Physical Gift Description</label>
              <input type="text" id="entry-gift-desc" class="form-input-field" placeholder="e.g. 5g Gold Coin, Silver Bowl, Titan Watch">
            </div>

            <div style="display: flex; gap: 12px; margin-top: 24px;">
              <button type="submit" class="btn-crimson" style="flex: 1; justify-content: center; padding: 14px; font-size: 15px;">
                <span>💾 Save Entry & Issue WhatsApp Receipt</span>
              </button>
              <button type="reset" class="btn-outline-dark">
                Clear
              </button>
            </div>
          </form>
        </div>
      </section>

      <!-- TAB 3: RED NOTEBOOK LEDGER -->
      <section id="tab-ledger" class="tab-pane">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; flex-wrap: wrap; gap: 12px;">
          <div>
            <h3 style="font-family: var(--font-serif); font-size: 26px; font-weight: 800; color: var(--c-night);">Digital Red Notebook Ledger</h3>
            <p style="font-size: 13.5px; color: var(--c-muted);">Complete audit trail of all celebration blessings</p>
          </div>
          <div style="display: flex; gap: 10px;">
            <button type="button" class="btn-emerald" onclick="exportLedgerCSV()">
              <span>📥 Export CSV</span>
            </button>
            <button type="button" class="btn-outline-dark" onclick="window.print()">
              <span>🖨️ Print Ledger</span>
            </button>
          </div>
        </div>

        <div class="ledger-table-wrap">
          <table class="ledger-table">
            <thead>
              <tr>
                <th>#</th>
                <th>Guest Name</th>
                <th>Native Place</th>
                <th>Relationship</th>
                <th>Cash Blessing</th>
                <th>Gift / Ornaments</th>
                <th>Recorded By</th>
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
              </tr>
              <tr>
                <td>2</td>
                <td><strong>Suresh & Malathi Sharma</strong></td>
                <td>Hyderabad</td>
                <td>Close Friends</td>
                <td class="num-currency" style="color: var(--c-emerald);">₹5,116</td>
                <td>Silk Stole</td>
                <td>Desk 1</td>
              </tr>
              <tr>
                <td>3</td>
                <td><strong>K. Raghunath Varma</strong></td>
                <td>Visakhapatnam</td>
                <td>Paternal Relative</td>
                <td class="num-currency" style="color: var(--c-emerald);">₹2,116</td>
                <td>10g Gold Coin</td>
                <td>Desk 2</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- TAB 4: EXPENSES VS SURPLUS -->
      <section id="tab-expenses" class="tab-pane">
        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 24px; max-width: 800px; margin: 0 auto;">
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;">Celebration Budget & Expense Reconciliation</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;">Compare total received shagun against vendor expenses</p>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px;">
            <div style="background: var(--c-base); padding: 18px; border-radius: 12px; border: 1.5px solid var(--c-night);">
              <div style="font-size: 12px; font-weight: 700; text-transform: uppercase;">Total Shagun Inflow</div>
              <div class="num-currency" style="font-size: 28px; color: var(--c-crimson);">₹8,42,116</div>
            </div>
            <div style="background: var(--c-base); padding: 18px; border-radius: 12px; border: 1.5px solid var(--c-night);">
              <div style="font-size: 12px; font-weight: 700; text-transform: uppercase;">Total Vendor Expenses</div>
              <div class="num-currency" style="font-size: 28px; color: var(--c-night);">₹4,15,000</div>
            </div>
          </div>

          <div style="background: #FFFFFF; border: 2px solid var(--c-emerald); padding: 18px; border-radius: 12px; text-align: center;">
            <div style="font-size: 13px; font-weight: 700; color: var(--c-emerald); text-transform: uppercase;">Net Auspicious Surplus Remaining</div>
            <div class="num-currency" style="font-size: 36px; color: var(--c-emerald);">+₹4,27,116</div>
          </div>
        </div>
      </section>

      <!-- TAB 5: RECIPROCITY TRACKER -->
      <section id="tab-reciprocity" class="tab-pane">
        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 24px;">
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;">Gift Reciprocity Intelligence</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 20px;">"How much did they give us last time? How much should we give them back?"</p>

          <div class="ledger-table-wrap">
            <table class="ledger-table">
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
                  <td><strong>Venkat Rao Garu (Vijayawada)</strong></td>
                  <td class="num-currency">₹10,116</td>
                  <td class="num-currency">₹5,116 (Daughter's Wedding 2024)</td>
                  <td class="num-currency" style="color: var(--c-emerald);">₹10,116 - ₹11,116</td>
                  <td><span class="tag-badge" style="background: var(--c-emerald); color: #FFFFFF;">FAVOR RETURNED</span></td>
                </tr>
                <tr>
                  <td><strong>Suresh Sharma (Hyderabad)</strong></td>
                  <td class="num-currency">₹5,116</td>
                  <td class="num-currency">₹5,116 (Housewarming 2025)</td>
                  <td class="num-currency" style="color: var(--c-night);">₹5,116</td>
                  <td><span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">EQUAL BALANCE</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- TAB 6: UPI QR & SOUNDBOX -->
      <section id="tab-soundbox" class="tab-pane">
        <div style="max-width: 520px; margin: 0 auto; background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 20px; padding: 32px; text-align: center;">
          <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">LIVE COUNTER SOUNDBOX</span>
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin: 12px 0 8px;">Direct UPI Shagun QR</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;">Guests can scan and pay directly via GPay, PhonePe, Paytm</p>

          <div style="background: var(--c-base); padding: 24px; border-radius: 16px; border: 2px dashed var(--c-night); display: inline-block; margin-bottom: 20px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=upi://pay?pa=giftvault@okhdfcbank&pn=GiftVault%20Wedding%20Treasury" alt="UPI QR Code" style="display: block; margin: 0 auto; border-radius: 8px;">
            <div class="num-currency" style="font-size: 13px; color: var(--c-night); margin-top: 12px;">
              giftvault@okhdfcbank
            </div>
          </div>

          <div>
            <button type="button" class="btn-emerald" onclick="testSoundboxChime()">
              <span>🔔 Test Audio Announcement Chime</span>
            </button>
          </div>
        </div>
      </section>

      <!-- TAB 7: REPORTS -->
      <section id="tab-reports" class="tab-pane">
        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 28px; max-width: 720px; margin: 0 auto;">
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;">Official Celebration Reports</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;">Download and print formal summaries for family archives</p>

          <div style="display: flex; flex-direction: column; gap: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 14px; background: var(--c-base); border-radius: 10px; border: 1px solid var(--c-border);">
              <div>
                <strong style="font-family: var(--font-sans); font-size: 14px;">Full Guest Shagun Ledger (CSV)</strong>
                <div style="font-size: 12px; color: var(--c-muted);">All 142 entries with timestamps, cities, phone numbers</div>
              </div>
              <button type="button" class="btn-outline-dark" onclick="exportLedgerCSV()">Download CSV</button>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; padding: 14px; background: var(--c-base); border-radius: 10px; border: 1px solid var(--c-border);">
              <div>
                <strong style="font-family: var(--font-sans); font-size: 14px;">Executive Summary (Printable PDF)</strong>
                <div style="font-size: 12px; color: var(--c-muted);">Grand totals, gold summary, and city breakdown</div>
              </div>
              <button type="button" class="btn-outline-dark" onclick="window.print()">Print Report</button>
            </div>
          </div>
        </div>
      </section>

      <!-- TAB 8: SETTINGS -->
      <section id="tab-settings" class="tab-pane">
        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 28px; max-width: 680px; margin: 0 auto;">
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;">Event Configuration</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;">Manage celebration parameters, PINs, and counter settings</p>

          <div class="form-group-item">
            <label class="form-label-txt">Event Celebration Title</label>
            <input type="text" class="form-input-field" value="Rahul & Snigdha Kalyanam">
          </div>
          <div class="form-group-item">
            <label class="form-label-txt">Auspicious Coin Rounding</label>
            <select class="form-input-field">
              <option selected>Always offer +₹1 lucky coin button</option>
              <option>Standard round numbers only</option>
            </select>
          </div>
          <div class="form-group-item">
            <label class="form-label-txt">Desk Host Passcode</label>
            <input type="password" class="form-input-field" value="2026">
          </div>
          <button type="button" class="btn-crimson" onclick="alert('Settings saved successfully!')">
            Save Configuration
          </button>
        </div>
      </section>

    </div>
  </main>

  <!-- ==========================================================================
       CREATE NEW EVENT MODAL (SGUNMS.IN STYLE EVENT SETUP)
       ========================================================================== -->
  <div id="modal-create-event" class="modal-backdrop">
    <div class="modal-dialog">
      <div class="modal-header">
        <div>
          <div class="showcase-tag-sub" style="margin-bottom: 2px;">NOOTANA SHUBHA KAARYAM</div>
          <h3>Create New Auspicious Event</h3>
        </div>
        <button type="button" class="modal-close-btn" onclick="closeCreateEventModal()">✕</button>
      </div>

      <div class="modal-body">
        <form onsubmit="handleCreateEventSubmit(event)">
          <div class="form-group-item">
            <label class="form-label-txt">Celebration Milestone Category *</label>
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
            <label class="form-label-txt">Event Celebration Title *</label>
            <input type="text" id="new-event-title" class="form-input-field" placeholder="e.g. Ramesh & Divya Vivaha Mahotsavam" required>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div class="form-group-item">
              <label class="form-label-txt">Date of Event *</label>
              <input type="date" id="new-event-date" class="form-input-field" required>
            </div>
            <div class="form-group-item">
              <label class="form-label-txt">Expected Guest Count</label>
              <input type="number" id="new-event-guests" class="form-input-field" placeholder="500">
            </div>
          </div>

          <div class="form-group-item">
            <label class="form-label-txt">Reception Venue & City</label>
            <input type="text" id="new-event-venue" class="form-input-field" placeholder="e.g. Grand Kalyana Mandapam, Guntur">
          </div>

          <div style="display: flex; gap: 12px; margin-top: 24px;">
            <button type="button" class="btn-page-back" onclick="closeCreateEventModal()">
              <span>← Cancel</span>
            </button>
            <button type="submit" class="btn-crimson" style="flex: 1; justify-content: center;">
              <span>Create Event Ledger →</span>
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
        <p>The modern digital Red Notebook and Shagun Treasury engineered for Indian family celebrations and reception desks worldwide.</p>
        <div style="margin-top: 16px; font-family: var(--font-sans); font-size: 13.5px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #FFFFFF;">
          SHUBHAM BHAVATU
        </div>
      </div>
      <div class="footer-col">
        <h4>Capabilities</h4>
        <ul class="footer-links-list">
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');">Munshi Rapid Entry</button></li>
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');">Reciprocity Tracker</button></li>
          <li><button type="button" class="footer-btn-link" onclick="scrollToSection('features-section');">Digital Red Notebook</button></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Reception Desk</h4>
        <ul class="footer-links-list">
          <li><button type="button" class="footer-btn-link" onclick="navToView('login')">Open Reception Desk</button></li>
          <li><button type="button" class="footer-btn-link" onclick="navToView('login')">Multi-Counter Sync</button></li>
          <li><button type="button" class="footer-btn-link" onclick="navToView('login')">UPI Soundbox</button></li>
        </ul>
      </div>
    </div>

    <div class="footer-bottom-bar">
      <div>© 2026 GiftVault. All rights reserved. Built for Indian Family Celebrations.</div>
      <div>Designed with Option B (Playfair Display + Plus Jakarta Sans)</div>
    </div>
  </footer>

  <!-- ==========================================================================
       JAVASCRIPT APPLICATION LOGIC
       ========================================================================== -->
  <script>
    // Navigation History Stack for Bulletproof Universal Back Action
    let navHistory = ['landing'];

    function navToView(viewId, pushHistory = true) {
      if (pushHistory && (navHistory.length === 0 || navHistory[navHistory.length - 1] !== viewId)) {
        navHistory.push(viewId);
      }

      // Hide all screen views
      document.querySelectorAll('.app-screen-view').forEach(el => el.classList.remove('active'));

      // Show requested screen view
      const target = document.getElementById('view-' + viewId);
      if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }

      // Show or hide the floating side back button
      const floatingBack = document.getElementById('floating-back-btn');
      if (floatingBack) {
        if (viewId === 'landing') {
          floatingBack.style.display = 'none';
        } else {
          floatingBack.style.display = 'flex';
        }
      }
    }

    // Universal Back Button Handler (Triggered by either floating pill or top back button)
    function handleUniversalBack() {
      // If modal is open, close it first
      const modal = document.getElementById('modal-create-event');
      if (modal && modal.classList.contains('active')) {
        closeCreateEventModal();
        return;
      }

      if (navHistory.length > 1) {
        navHistory.pop(); // Remove current view
        const prevView = navHistory[navHistory.length - 1];
        navToView(prevView, false);
      } else {
        navToView('landing', false);
      }
    }

    // Scroll to section helper
    function scrollToSection(secId) {
      if (!document.getElementById('view-landing').classList.contains('active')) {
        navToView('landing');
      }
      setTimeout(() => {
        const el = document.getElementById(secId);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 50);
    }

    // Login Submission
    function handleLoginSubmit(e) {
      e.preventDefault();
      navToView('hub');
    }

    // Enter Workspace from Hub
    function enterWorkspaceEvent(eventId) {
      if (eventId === 'event-birthday') {
        document.getElementById('ws-event-header-name').innerText = 'Advait 1st Birthday & Cradle';
      } else {
        document.getElementById('ws-event-header-name').innerText = 'Rahul & Snigdha Kalyanam';
      }
      navToView('app');
    }

    // Workspace Tabs Switching
    function switchWorkspaceTab(tabId, btn) {
      document.querySelectorAll('.ws-tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');

      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
      const targetPane = document.getElementById(tabId);
      if (targetPane) targetPane.classList.add('active');
    }

    // Auspicious Rounding Helpers
    function applyAuspiciousAmount(val) {
      document.getElementById('entry-amount').value = val;
    }
    function addOneRupeeCoin() {
      const field = document.getElementById('entry-amount');
      let cur = parseInt(field.value, 10) || 0;
      if (cur % 10 === 0) {
        field.value = cur + 1;
      } else if (cur % 100 === 0) {
        field.value = cur + 1;
      } else {
        field.value = cur + 1;
      }
    }

    // Munshi Entry Submission
    function handleMunshiSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('entry-name').value;
      const city = document.getElementById('entry-city').value || 'Native City';
      const rel = document.getElementById('entry-rel').value;
      const amt = document.getElementById('entry-amount').value;
      const gift = document.getElementById('entry-gift-desc').value || 'None';

      const recentTbody = document.getElementById('ws-recent-table-body');
      const fullTbody = document.getElementById('ws-full-ledger-body');

      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>Just now</td>
        <td><strong>${name}</strong></td>
        <td>${city}</td>
        <td>${rel}</td>
        <td class="num-currency" style="color: var(--c-emerald);">₹${parseInt(amt).toLocaleString('en-IN')}</td>
        <td><span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;">CASH</span></td>
      `;
      if (recentTbody) recentTbody.prepend(tr);

      alert(`Auspicious Blessing Recorded for ${name} (₹${parseInt(amt).toLocaleString('en-IN')})! WhatsApp Receipt Prepared.`);
      e.target.reset();
      switchWorkspaceTab('tab-overview');
    }

    // Export CSV Helper
    function exportLedgerCSV() {
      const csvContent = "data:text/csv;charset=utf-8," 
        + "Timestamp,Guest Name,Native City,Relationship,Amount (INR),Gift Details\n"
        + "10:42 PM,Venkat Rao Garu,Vijayawada,Maternal Uncle,10116,None\n"
        + "10:38 PM,Suresh Sharma,Hyderabad,Close Friend,5116,Silk Stole\n"
        + "10:25 PM,K. Raghunath Varma,Visakhapatnam,Paternal Relative,2116,10g Gold Coin\n";
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", "GiftVault_Celebration_Ledger.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    // Test Audio Soundbox Chime (Web Audio API)
    function testSoundboxChime() {
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const now = audioCtx.currentTime;
        
        // Pleasant twin-tone chime
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

        alert("🔔 [Soundbox Announcement]: 'GiftVault received ₹10,116 from Venkat Rao Garu! Shubham Bhavatu!'");
      } catch (err) {
        alert("🔔 [Soundbox Announcement]: 'GiftVault received ₹10,116 from Venkat Rao Garu! Shubham Bhavatu!'");
      }
    }

    // Modal Control Functions
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

      // Insert new card in Hub Grid before the create card
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

      // Insert as first item in hub grid
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
        f.write(html_content)
    print(f"Updated: {target} ({len(html_content)} bytes)")

print("\nSuccessfully removed 3 core pillars switcher and occasion names from the hero section!")
