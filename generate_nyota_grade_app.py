# -*- coding: utf-8 -*-
"""
Generate the Grand, Clean, Luxury South-Asian Wedding & Celebration Ledger Application
Directly modeled on the world-class architecture of https://thenyota.app/ with:
- NO GOLD, NO CHEAP AI GRADIENTS, NO SLOP.
- Professional Palette: Pristine Warm White (#FDF8F6 / #FFFFFF), Deep Heritage Crimson (#D20F1F / #991B1B), Slate Charcoal (#111827 / #374151), Crisp Borders (#F3F4F6 / #E5E7EB).
- Trilingual Support: English, తెలుగు (Telugu), हिंदी (Hindi) with instantaneous switcher right in top nav.
- Grand Sticky Nav with dropdowns (Features, Celebrations, Language Switcher, Get App / Web Login CTA).
- Hero with realistic celebration photography, live phone mockup, badge, and dual CTAs.
- Full 6-Card Features Grid (Desk Mode, Smart History, Digital Reports, WhatsApp Tamboolam, UPI QR Soundbox, Net Surplus).
- 12 Celebrations We Support Showcase with category filter (Wedding, Birthday, Housewarming, Half Saree, Upanayanam, etc.).
- Old Manual Red Book vs Digital Comparison Matrix.
- Frequently Asked Questions (Interactive Accordion).
- Grand Footer with full sitemap and copyright.
- Dedicated Luxury Sign-In / Login Screen (OTP verification, Google Sign-in, Role selector).
- Full In-App Workspace (Dashboard, Munshi Desk with +₹1 coin, Red Ledger, Expenses vs Surplus, Reciprocity, Soundbox QR, Settings).
"""

NYOTA_INSPIRED_APP = r'''<!DOCTYPE html>
<html lang="te" id="app-html">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>GiftVault • The Modern Digital Red Notebook for Family Celebrations</title>
  
  <!-- Inter & Plus Jakarta Sans & Noto Sans Telugu/Devanagari -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;500;600;700&family=Noto+Sans+Telugu:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  
  <style>
    /* ============================================================
       PROFESSIONAL HERITAGE CRIMSON & CRISP WARM WHITE PALETTE
       Modeled after thenyota.app
       60% Dominant: #FDF8F6 (Soft Warm Alabaster) & #FFFFFF (Pristine Card White)
       30% Secondary: #111827 (Slate Charcoal Typography) & #4B5563 / #E5E7EB (Clean Borders)
       10% Accent: #D20F1F (Deep Auspicious Heritage Crimson) & #991B1B (Deep Wine)
       NO GOLD, NO AI SLOP.
       ============================================================ */
    :root {
      --bg-body: #FDF8F6;
      --bg-white: #FFFFFF;
      --bg-surface-soft: #F9FAFB;
      --bg-crimson-soft: #FEF2F2;
      
      --text-heading: #111827;
      --text-body: #374151;
      --text-muted: #6B7280;
      --text-dim: #9CA3AF;
      
      --border-light: #F3F4F6;
      --border-mid: #E5E7EB;
      --border-dark: #D1D5DB;
      
      --crimson-primary: #D20F1F;
      --crimson-dark: #B91C1C;
      --crimson-light: #EF4444;
      --crimson-bg: #FEF2F2;
      --crimson-border: #FEE2E2;
      
      --emerald-accent: #059669;
      --emerald-bg: #ECFDF5;
      
      --blue-accent: #2563EB;
      --blue-bg: #EFF6FF;
      
      --purple-accent: #7C3AED;
      --purple-bg: #F5F3FF;
      
      --amber-accent: #D97706;
      --amber-bg: #FFFBEB;

      --font-main: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-telugu: 'Noto Sans Telugu', var(--font-main);
      --font-hindi: 'Noto Sans Devanagari', var(--font-main);

      --shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.08), 0 1px 2px -1px rgba(0, 0, 0, 0.06);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.07), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
      --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 8px 10px -6px rgba(0, 0, 0, 0.04);
      --shadow-crimson: 0 8px 20px -4px rgba(210, 15, 31, 0.28);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    body {
      background-color: var(--bg-body);
      color: var(--text-body);
      font-family: var(--font-main);
      line-height: 1.5;
      overflow-x: hidden;
    }

    body.lang-te {
      font-family: var(--font-telugu);
    }
    body.lang-hi {
      font-family: var(--font-hindi);
    }

    /* Ambient Subtle Glows (from Nyota) */
    .glow-blob-top {
      position: absolute;
      top: 0;
      right: 0;
      transform: translate(30%, -20%);
      width: 480px;
      height: 480px;
      background: radial-gradient(circle, rgba(210, 15, 31, 0.06) 0%, rgba(253, 248, 246, 0) 70%);
      pointer-events: none;
      z-index: 0;
    }
    .glow-blob-bottom {
      position: absolute;
      bottom: 0;
      left: 0;
      transform: translate(-30%, 20%);
      width: 480px;
      height: 480px;
      background: radial-gradient(circle, rgba(217, 119, 6, 0.05) 0%, rgba(253, 248, 246, 0) 70%);
      pointer-events: none;
      z-index: 0;
    }

    /* ============================================================
       TOP STICKY NAVBAR (EXACT NYOTA PATTERN)
       ============================================================ */
    .nyota-header {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-light);
      transition: all 0.2s ease;
    }
    .header-inner {
      max-width: 1240px;
      margin: 0 auto;
      padding: 14px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .brand-wrap {
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      text-decoration: none;
    }
    .brand-icon-box {
      width: 38px;
      height: 38px;
      background: linear-gradient(135deg, #D20F1F, #991B1B);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      box-shadow: 0 4px 10px rgba(210, 15, 31, 0.25);
    }
    .brand-title {
      font-size: 21px;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: var(--text-heading);
    }
    .brand-title span {
      color: var(--crimson-primary);
    }

    .nav-menu {
      display: flex;
      align-items: center;
      gap: 28px;
    }
    @media (max-width: 900px) {
      .nav-menu { display: none; }
    }
    .nav-item {
      position: relative;
    }
    .nav-link-btn {
      background: none;
      border: none;
      font-size: 14.5px;
      font-weight: 500;
      color: var(--text-body);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      padding: 6px 0;
      transition: color 0.15s ease;
      font-family: inherit;
    }
    .nav-link-btn:hover {
      color: var(--crimson-primary);
    }

    /* Language Switcher Dropdown */
    .lang-switcher-btn {
      background: var(--bg-surface-soft);
      border: 1px solid var(--border-mid);
      border-radius: 9999px;
      padding: 6px 14px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-heading);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }
    .lang-switcher-btn:hover {
      border-color: var(--crimson-primary);
      color: var(--crimson-primary);
    }

    /* Buttons */
    .btn-crimson {
      background: var(--crimson-primary);
      color: #FFFFFF;
      font-size: 14px;
      font-weight: 600;
      padding: 10px 22px;
      border-radius: 9999px;
      border: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: var(--shadow-crimson);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      font-family: inherit;
      text-decoration: none;
    }
    .btn-crimson:hover {
      background: var(--crimson-dark);
      transform: translateY(-1.5px);
      box-shadow: 0 10px 24px -2px rgba(210, 15, 31, 0.38);
    }
    .btn-crimson:active {
      transform: translateY(0);
    }

    .btn-secondary {
      background: #FFFFFF;
      color: var(--text-heading);
      font-size: 14px;
      font-weight: 600;
      padding: 10px 20px;
      border-radius: 9999px;
      border: 1.5px solid var(--border-mid);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .btn-secondary:hover {
      border-color: var(--text-heading);
      background: var(--bg-surface-soft);
    }

    /* Views */
    .app-view {
      display: none;
    }
    .app-view.active {
      display: block;
      animation: fadeIn 0.3s ease;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ============================================================
       HERO SECTION (CLEAN, BOLD, AUTHENTIC NYOTA STYLE)
       ============================================================ */
    .hero-section {
      position: relative;
      padding: 64px 24px 80px 24px;
      max-width: 1240px;
      margin: 0 auto;
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 56px;
      align-items: center;
    }
    @media (max-width: 960px) {
      .hero-grid {
        grid-template-columns: 1fr;
        gap: 40px;
      }
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 9999px;
      background: var(--crimson-bg);
      border: 1px solid var(--crimson-border);
      color: var(--crimson-primary);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 22px;
    }
    .hero-badge-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--crimson-primary);
      box-shadow: 0 0 8px rgba(210, 15, 31, 0.6);
    }

    .hero-title {
      font-size: 48px;
      font-weight: 900;
      line-height: 1.15;
      letter-spacing: -0.03em;
      color: var(--text-heading);
      margin-bottom: 20px;
    }
    @media (max-width: 640px) {
      .hero-title { font-size: 34px; }
    }
    .hero-title span {
      color: var(--crimson-primary);
    }

    .hero-desc {
      font-size: 17px;
      line-height: 1.65;
      color: var(--text-body);
      margin-bottom: 32px;
      max-width: 580px;
    }

    .hero-cta-group {
      display: flex;
      gap: 14px;
      align-items: center;
      flex-wrap: wrap;
      margin-bottom: 32px;
    }

    .hero-social-proof {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 13.5px;
      color: var(--text-muted);
      border-top: 1px solid var(--border-mid);
      padding-top: 20px;
    }

    /* REALISTIC CELEBRATION APP CARD IN HERO */
    .hero-app-mockup {
      background: #FFFFFF;
      border: 1px solid var(--border-mid);
      border-radius: 28px;
      padding: 24px;
      box-shadow: var(--shadow-xl);
      position: relative;
    }
    .mockup-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-light);
    }
    .mockup-header-info {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .mockup-avatar {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: var(--crimson-bg);
      border: 1px solid var(--crimson-border);
      color: var(--crimson-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
    }
    .mockup-event-title {
      font-size: 16px;
      font-weight: 700;
      color: var(--text-heading);
    }
    .mockup-event-sub {
      font-size: 12px;
      color: var(--text-muted);
    }

    /* Celebration Filter Pills (Quick interactive tabs) */
    .celebration-filter-bar {
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 10px;
      margin-bottom: 18px;
    }
    .cel-pill {
      padding: 7px 14px;
      border-radius: 9999px;
      border: 1.5px solid var(--border-mid);
      background: var(--bg-white);
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-body);
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .cel-pill.active {
      background: var(--crimson-primary);
      border-color: var(--crimson-primary);
      color: #FFFFFF;
    }

    .mockup-stat-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 18px;
    }
    .mockup-stat-box {
      background: var(--bg-surface-soft);
      border: 1px solid var(--border-light);
      border-radius: 16px;
      padding: 14px;
    }
    .stat-label {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 4px;
    }
    .stat-value {
      font-size: 20px;
      font-weight: 800;
      color: var(--text-heading);
    }

    /* Live Entry Feed Mockup */
    .mockup-feed-title {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 10px;
    }
    .mockup-feed-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 12px;
      background: #FFFFFF;
      border: 1px solid var(--border-light);
      border-radius: 12px;
      margin-bottom: 8px;
      box-shadow: var(--shadow-xs);
    }
    .feed-guest {
      font-weight: 600;
      font-size: 13.5px;
      color: var(--text-heading);
    }
    .feed-city {
      font-size: 11.5px;
      color: var(--text-muted);
    }
    .feed-amount {
      font-weight: 800;
      font-size: 15px;
      color: var(--crimson-primary);
    }

    /* ============================================================
       FOUNDATIONS / HIGHLIGHTS SECTION
       ============================================================ */
    .section-wrap {
      max-width: 1240px;
      margin: 0 auto;
      padding: 72px 24px;
    }
    .section-header-center {
      text-align: center;
      max-width: 720px;
      margin: 0 auto 52px auto;
    }
    .section-pill-tag {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--crimson-primary);
      margin-bottom: 10px;
    }
    .section-main-heading {
      font-size: 36px;
      font-weight: 800;
      letter-spacing: -0.02em;
      color: var(--text-heading);
      margin-bottom: 14px;
    }
    .section-main-desc {
      font-size: 16px;
      line-height: 1.6;
      color: var(--text-body);
    }

    /* 3 Foundation Cards */
    .foundation-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
      margin-bottom: 60px;
    }
    @media (max-width: 900px) {
      .foundation-grid { grid-template-columns: 1fr; }
    }
    .foundation-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border-light);
      border-radius: 24px;
      padding: 36px 30px;
      box-shadow: var(--shadow-sm);
      transition: all 0.25s ease;
    }
    .foundation-card:hover {
      border-color: var(--border-mid);
      box-shadow: var(--shadow-lg);
      transform: translateY(-3px);
    }
    .foundation-icon-circle {
      width: 52px;
      height: 52px;
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      margin-bottom: 22px;
    }
    .foundation-h3 {
      font-size: 20px;
      font-weight: 700;
      color: var(--text-heading);
      margin-bottom: 10px;
    }
    .foundation-p {
      font-size: 14.5px;
      color: var(--text-muted);
      line-height: 1.65;
    }

    /* 6 Bento Grid Feature Cards (Desk Mode, History, PDF Reports, WhatsApp, QR, Net Surplus) */
    .feature-bento-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }
    @media (max-width: 960px) {
      .feature-bento-grid { grid-template-columns: 1fr; }
    }
    .bento-box {
      background: #FFFFFF;
      border: 1.5px solid var(--border-light);
      border-radius: 24px;
      padding: 32px 28px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
    }
    .bento-box:hover {
      box-shadow: var(--shadow-md);
      transform: translateY(-2px);
      border-color: var(--border-mid);
    }
    .bento-tag {
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--crimson-primary);
      margin-bottom: 8px;
    }
    .bento-title {
      font-size: 19px;
      font-weight: 700;
      color: var(--text-heading);
      margin-bottom: 10px;
    }
    .bento-desc {
      font-size: 14px;
      color: var(--text-body);
      line-height: 1.6;
    }

    /* ============================================================
       CELEBRATIONS WE SUPPORT (CAROUSEL / GRID)
       ============================================================ */
    .celebrations-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }
    @media (max-width: 1024px) {
      .celebrations-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 600px) {
      .celebrations-grid { grid-template-columns: 1fr; }
    }
    .celebration-item-card {
      background: #FFFFFF;
      border: 1.5px solid var(--border-light);
      border-radius: 20px;
      padding: 24px 20px;
      box-shadow: var(--shadow-xs);
      transition: all 0.2s ease;
    }
    .celebration-item-card:hover {
      border-color: var(--border-mid);
      box-shadow: var(--shadow-md);
      transform: translateY(-2px);
    }
    .cel-icon {
      font-size: 32px;
      margin-bottom: 14px;
      display: inline-block;
    }
    .cel-name {
      font-size: 17px;
      font-weight: 700;
      color: var(--text-heading);
      margin-bottom: 6px;
    }
    .cel-desc {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    /* ============================================================
       COMPARISON TABLE (OLD PAPER NOTEBOOK VS GIFTVAULT)
       ============================================================ */
    .compare-container {
      background: #FFFFFF;
      border: 1.5px solid var(--border-mid);
      border-radius: 24px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }
    .compare-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .compare-table th, .compare-table td {
      padding: 18px 24px;
      border-bottom: 1px solid var(--border-light);
      font-size: 14.5px;
    }
    .compare-table th {
      background: var(--bg-surface-soft);
      font-weight: 700;
      color: var(--text-heading);
      font-size: 15px;
    }
    .compare-table tr:last-child td {
      border-bottom: none;
    }

    /* ============================================================
       FAQ ACCORDION
       ============================================================ */
    .faq-list {
      max-width: 800px;
      margin: 0 auto;
    }
    .faq-item {
      background: #FFFFFF;
      border: 1.5px solid var(--border-light);
      border-radius: 16px;
      margin-bottom: 14px;
      overflow: hidden;
      transition: border-color 0.2s ease;
    }
    .faq-item:hover {
      border-color: var(--border-mid);
    }
    .faq-question {
      padding: 20px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 16px;
      font-weight: 700;
      color: var(--text-heading);
      cursor: pointer;
      user-select: none;
    }
    .faq-answer {
      padding: 0 24px 20px 24px;
      font-size: 14.5px;
      line-height: 1.6;
      color: var(--text-body);
      display: none;
    }
    .faq-item.open .faq-answer {
      display: block;
    }
    .faq-item.open .faq-arrow {
      transform: rotate(180deg);
    }
    .faq-arrow {
      transition: transform 0.2s ease;
      color: var(--text-muted);
    }

    /* ============================================================
       GRAND FOOTER
       ============================================================ */
    .site-footer {
      background: #FFFFFF;
      border-top: 1px solid var(--border-mid);
      padding: 64px 24px 32px 24px;
      margin-top: 60px;
    }
    .footer-container {
      max-width: 1240px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr 1fr;
      gap: 40px;
      margin-bottom: 48px;
    }
    @media (max-width: 900px) {
      .footer-container { grid-template-columns: 1fr 1fr; }
    }
    @media (max-width: 600px) {
      .footer-container { grid-template-columns: 1fr; }
    }
    .footer-col-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--text-heading);
      margin-bottom: 16px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .footer-link {
      display: block;
      font-size: 14px;
      color: var(--text-muted);
      text-decoration: none;
      margin-bottom: 10px;
      transition: color 0.15s ease;
    }
    .footer-link:hover {
      color: var(--crimson-primary);
    }

    /* ============================================================
       VIEW 2: DEDICATED FULL-PAGE SIGN-IN (LUXURY REDESIGN)
       ============================================================ */
    .login-wrapper {
      max-width: 960px;
      margin: 48px auto;
      padding: 0 24px;
    }
    .login-card-split {
      background: #FFFFFF;
      border: 1.5px solid var(--border-mid);
      border-radius: 28px;
      overflow: hidden;
      box-shadow: var(--shadow-xl);
      display: grid;
      grid-template-columns: 1fr 1fr;
    }
    @media (max-width: 768px) {
      .login-card-split { grid-template-columns: 1fr; }
      .login-left-panel { display: none; }
    }
    .login-left-panel {
      background: linear-gradient(135deg, #FEF2F2 0%, #FEE2E2 100%);
      border-right: 1.5px solid var(--border-mid);
      padding: 48px 40px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .login-right-panel {
      padding: 48px 40px;
    }

    .form-group {
      margin-bottom: 20px;
    }
    .form-label {
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-heading);
      margin-bottom: 6px;
    }
    .form-input {
      width: 100%;
      padding: 12px 14px;
      border: 1.5px solid var(--border-mid);
      border-radius: 12px;
      font-size: 14px;
      font-family: inherit;
      color: var(--text-heading);
      background: #FFFFFF;
      transition: all 0.15s ease;
    }
    .form-input:focus {
      outline: none;
      border-color: var(--crimson-primary);
      box-shadow: 0 0 0 3px rgba(210, 15, 31, 0.12);
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
      border: 1.5px solid var(--border-mid);
      border-radius: 12px;
      background: #FFFFFF;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-body);
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .role-pill.active {
      border-color: var(--crimson-primary);
      background: var(--crimson-bg);
      color: var(--crimson-primary);
      font-weight: 700;
    }

    /* ============================================================
       VIEW 3: IN-APP COMPLETE WORKSPACE
       ============================================================ */
    .workspace-wrap {
      max-width: 1280px;
      margin: 0 auto;
      padding: 28px 24px;
    }
    .workspace-topbar {
      background: #FFFFFF;
      border: 1.5px solid var(--border-mid);
      border-radius: 20px;
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }
    .tab-pills-bar {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 6px;
      margin-bottom: 24px;
      border-bottom: 1.5px solid var(--border-mid);
    }
    .tab-pill-btn {
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
      transition: all 0.15s ease;
      font-family: inherit;
    }
    .tab-pill-btn.active {
      color: var(--crimson-primary);
      border-bottom-color: var(--crimson-primary);
      font-weight: 700;
    }

    .tab-screen {
      display: none;
    }
    .tab-screen.active {
      display: block;
      animation: fadeIn 0.2s ease;
    }

    /* Munshi Quick Coins */
    .coin-wrap {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 10px 0 18px 0;
    }
    .coin-chip {
      padding: 6px 14px;
      border-radius: 9999px;
      border: 1.5px solid var(--crimson-border);
      background: var(--crimson-bg);
      color: var(--crimson-primary);
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .coin-chip:hover {
      background: var(--crimson-primary);
      color: #FFFFFF;
    }

    /* Ledger Data Table */
    .ledger-card-wrap {
      background: #FFFFFF;
      border: 1.5px solid var(--border-mid);
      border-radius: 20px;
      overflow-x: auto;
      box-shadow: var(--shadow-sm);
    }
    .app-data-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
    }
    .app-data-table th, .app-data-table td {
      padding: 14px 18px;
      border-bottom: 1px solid var(--border-light);
      font-size: 13.5px;
    }
    .app-data-table th {
      background: var(--bg-surface-soft);
      font-weight: 700;
      color: var(--text-heading);
      font-size: 11.5px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .app-data-table tr:hover td {
      background: var(--bg-surface-soft);
    }

    /* Toast */
    .toast-popup {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--text-heading);
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
<body class="lang-te">

  <div class="glow-blob-top"></div>
  <div class="glow-blob-bottom"></div>

  <!-- ============================================================
       TOP STICKY NAVBAR (NYOTA STYLE)
       ============================================================ -->
  <header class="nyota-header">
    <div class="header-inner">
      <div class="brand-wrap" onclick="navToView('landing')">
        <div class="brand-icon-box">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
          </svg>
        </div>
        <div class="brand-title">Gift<span>Vault</span></div>
      </div>

      <nav class="nav-menu">
        <button type="button" class="nav-link-btn" onclick="navToView('landing')" data-i18n="nav_home">Home</button>
        <button type="button" class="nav-link-btn" onclick="jumpToSection('features-section')" data-i18n="nav_features">Features</button>
        <button type="button" class="nav-link-btn" onclick="jumpToSection('events-section')" data-i18n="nav_celebrations">Celebrations</button>
        <button type="button" class="nav-link-btn" onclick="jumpToSection('compare-section')" data-i18n="nav_compare">Comparison</button>
        <button type="button" class="nav-link-btn" onclick="jumpToSection('faq-section')" data-i18n="nav_faq">FAQ</button>
      </nav>

      <div style="display: flex; gap: 10px; align-items: center;">
        <!-- Language Switcher -->
        <div style="display: flex; gap: 4px; background: var(--bg-surface-soft); padding: 3px; border-radius: 9999px; border: 1px solid var(--border-mid);">
          <button type="button" class="lang-btn active" style="padding: 4px 10px; border-radius: 9999px; border: none; font-size: 12px; font-weight: 700; cursor: pointer; background: var(--crimson-primary); color: #FFF;" onclick="switchLanguage('te', this)">తెలుగు</button>
          <button type="button" class="lang-btn" style="padding: 4px 10px; border-radius: 9999px; border: none; font-size: 12px; font-weight: 600; cursor: pointer; background: none; color: var(--text-body);" onclick="switchLanguage('en', this)">EN</button>
          <button type="button" class="lang-btn" style="padding: 4px 10px; border-radius: 9999px; border: none; font-size: 12px; font-weight: 600; cursor: pointer; background: none; color: var(--text-body);" onclick="switchLanguage('hi', this)">हिंदी</button>
        </div>

        <button type="button" class="btn-secondary" onclick="navToView('login')" data-i18n="btn_login">
          Sign In
        </button>
        <button type="button" class="btn-crimson" onclick="navToView('app'); openAppTab('desk');" data-i18n="btn_launch">
          Open Vault →
        </button>
      </div>
    </div>
  </header>

  <!-- ============================================================
       VIEW 1: GRAND LANDING PAGE
       ============================================================ -->
  <main id="view-landing" class="app-view active">
    
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-grid">
        <div>
          <div class="hero-badge">
            <span class="hero-badge-dot"></span>
            <span data-i18n="hero_badge">Live on Android, iOS & Web • Free for Families</span>
          </div>

          <h1 class="hero-title" data-i18n="hero_h1">
            The App for Every Family <span>Celebration</span>.
          </h1>

          <p class="hero-desc" data-i18n="hero_desc">
            Organize events, manage your guest list, and record every gift — the modern, elegant way to keep the traditional family Red Notebook.
          </p>

          <div class="hero-cta-group">
            <button type="button" class="btn-crimson" onclick="navToView('app'); openAppTab('desk');" style="padding: 13px 28px; font-size: 15px;" data-i18n="hero_cta_primary">
              ⚡ Open Munshi Desk (Fast Entry)
            </button>
            <button type="button" class="btn-secondary" onclick="navToView('login')" style="padding: 13px 24px; font-size: 15px;" data-i18n="hero_cta_secondary">
              Family Login
            </button>
          </div>

          <div class="hero-social-proof">
            <span style="font-size: 18px;">🌍</span>
            <span data-i18n="hero_proof">Trusted by South Asian families worldwide • Settle gifts effortlessly</span>
          </div>
        </div>

        <!-- Hero App Showcase Mockup -->
        <div class="hero-app-mockup">
          <div class="mockup-top">
            <div class="mockup-header-info">
              <div class="mockup-avatar" id="hero-mock-icon">💍</div>
              <div>
                <div class="mockup-event-title" id="hero-mock-title">రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం</div>
                <div class="mockup-event-sub" id="hero-mock-sub">హైదరాబాద్ • లైవ్ ఖజానా</div>
              </div>
            </div>
            <span style="background: var(--emerald-bg); color: var(--emerald-accent); font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 9999px;">
              ● LIVE VAULT
            </span>
          </div>

          <!-- Quick Celebration Switcher inside Hero -->
          <div class="celebration-filter-bar">
            <button type="button" class="cel-pill active" onclick="setHeroCelebration('wedding', this)">💍 వివాహం</button>
            <button type="button" class="cel-pill" onclick="setHeroCelebration('birthday', this)">👶 బారసాల / బర్త్‌డే</button>
            <button type="button" class="cel-pill" onclick="setHeroCelebration('halfsaree', this)">🪷 హాఫ్ శారీ</button>
            <button type="button" class="cel-pill" onclick="setHeroCelebration('housewarming', this)">🏡 గృహప్రవేశం</button>
          </div>

          <div class="mockup-stat-grid">
            <div class="mockup-stat-box">
              <div class="stat-label" data-i18n="stat_inflow">మొత్తం చదివింపులు</div>
              <div class="stat-value" id="mock-inflow" style="color: var(--crimson-primary);">₹8,42,116</div>
            </div>
            <div class="mockup-stat-box">
              <div class="stat-label" data-i18n="stat_expenses">ఫంక్షన్ ఖర్చులు</div>
              <div class="stat-value" id="mock-exp" style="color: var(--text-body);">₹4,15,000</div>
            </div>
            <div class="mockup-stat-box">
              <div class="stat-label" data-i18n="stat_surplus">నికర మిగులు</div>
              <div class="stat-value" id="mock-surplus" style="color: var(--emerald-accent);">+₹4,27,116</div>
            </div>
            <div class="mockup-stat-box">
              <div class="stat-label" data-i18n="stat_jewels">బంగారం & వెండి</div>
              <div class="stat-value" id="mock-jewel">42.5g / 550g</div>
            </div>
          </div>

          <div class="mockup-feed-title" data-i18n="mockup_recent_title">తాజా ఎంట్రీలు (Live Feed)</div>
          <div class="mockup-feed-row">
            <div>
              <div class="feed-guest">వెంకట్ రావు గారు</div>
              <div class="feed-city">విజయవాడ • బంధువులు</div>
            </div>
            <div class="feed-amount">+ ₹10,116</div>
          </div>
          <div class="mockup-feed-row">
            <div>
              <div class="feed-guest">శ్రీనివాస రెడ్డి గారు</div>
              <div class="feed-city">గుంటూరు • సహోద్యోగి</div>
            </div>
            <div class="feed-amount">+ ₹5,116</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Secure Foundations Section (from Nyota) -->
    <section class="section-wrap" style="border-top: 1px solid var(--border-light); background: #FFFFFF;">
      <div class="section-header-center">
        <div class="section-pill-tag" data-i18n="found_tag">భరోసా & భద్రత</div>
        <h2 class="section-main-heading" data-i18n="found_heading">Secure Foundations for Modern Traditions</h2>
        <p class="section-main-desc" data-i18n="found_desc">శతాబ్దాల సాంప్రదాయ విలువలను ఆధునిక సాంకేతిక భద్రతతో అందిస్తున్నాము.</p>
      </div>

      <div class="foundation-grid">
        <div class="foundation-card">
          <div class="foundation-icon-circle" style="background: var(--crimson-bg); color: var(--crimson-primary);">🔒</div>
          <h3 class="foundation-h3" data-i18n="found_card1_title">Secure & Private</h3>
          <p class="foundation-p" data-i18n="found_card1_desc">మీ డేటా పూర్తిగా ఎన్‌క్రిప్ట్ చేయబడుతుంది. మీ కుటుంబ సభ్యుల అనుమతి లేకుండా ఎవరూ చూడలేరు.</p>
        </div>
        <div class="foundation-card">
          <div class="foundation-icon-circle" style="background: var(--blue-bg); color: var(--blue-accent);">🌐</div>
          <h3 class="foundation-h3" data-i18n="found_card2_title">Made for Every Family</h3>
          <p class="foundation-p" data-i18n="found_card2_desc">తెలుగు, ఇంగ్లీష్, హిందీ భాషలలో అందుబాటులో ఉంది. ప్రపంచవ్యాప్తంగా ఉన్న మీ బంధువులు అందరికీ సులభం.</p>
        </div>
        <div class="foundation-card">
          <div class="foundation-icon-circle" style="background: var(--emerald-bg); color: var(--emerald-accent);">📑</div>
          <h3 class="foundation-h3" data-i18n="found_card3_title">Easy Export</h3>
          <p class="foundation-p" data-i18n="found_card3_desc">ఒక్క క్లిక్‌తో పూర్తి ఎర్ర పుస్తకాన్ని ఎక్సెల్ లేదా పిడిఎఫ్ రూపంలో డౌన్‌లోడ్ చేసుకోవచ్చు.</p>
        </div>
      </div>
    </section>

    <!-- Built for Every Family Celebration (6 Bento Features) -->
    <section id="features-section" class="section-wrap">
      <div class="section-header-center">
        <div class="section-pill-tag" data-i18n="feat_tag">ప్రత్యేక సదుపాయాలు</div>
        <h2 class="section-main-heading" data-i18n="feat_heading">Built for Every Family Celebration</h2>
        <p class="section-main-desc" data-i18n="feat_desc">మున్షీ రద్దీ సమయంలో క్షణాల్లో ఎంట్రీలు చేయడం మొదలుకొని, తిరిగి ఇవ్వవలసిన మర్యాదల వరకు.</p>
      </div>

      <div class="feature-bento-grid">
        <div class="bento-box">
          <div>
            <div class="bento-tag">SPEED & CONVENIENCE</div>
            <h3 class="bento-title" data-i18n="bento1_title">⚡ Desk Mode (మున్షీ డెస్క్)</h3>
            <p class="bento-desc" data-i18n="bento1_desc">తీవ్రమైన రద్దీ ఉన్నప్పుడు 3 సెకన్లలో ఎంట్రీ చేయడానికి ప్రత్యేకంగా రూపొందించబడింది. +₹1 లక్కీ కాయిన్ ఆటో-రౌండింగ్ సదుపాయం.</p>
          </div>
        </div>

        <div class="bento-box">
          <div>
            <div class="bento-tag">RECIPROCITY INTELLIGENCE</div>
            <h3 class="bento-title" data-i18n="bento2_title">🔄 Smart History (మర్యాదల లెక్క)</h3>
            <p class="bento-desc" data-i18n="bento2_desc">వారు గతంలో మన ఫంక్షన్‌కు ఎంత ఇచ్చారో వెంటనే చూపిస్తుంది. భవిష్యత్తులో మనం ఎంత ఇవ్వాలో పక్కా లెక్క.</p>
          </div>
        </div>

        <div class="bento-box">
          <div>
            <div class="bento-tag">ONE-CLICK AUDIT</div>
            <h3 class="bento-title" data-i18n="bento3_title">📊 Digital Reports (ఎర్ర పుస్తకం)</h3>
            <p class="bento-desc" data-i18n="bento3_desc">అమరావతి & తెలంగాణ గ్రామీణ లెక్కల చిట్టా ఫార్మాట్. ఎప్పుడైనా ప్రింట్ లేదా ఎక్సెల్ రూపంలో సురక్షితం.</p>
          </div>
        </div>

        <div class="bento-box">
          <div>
            <div class="bento-tag">INSTANT COURTESY</div>
            <h3 class="bento-title" data-i18n="bento4_title">📲 WhatsApp Digital Receipts</h3>
            <p class="bento-desc" data-i18n="bento4_desc">ఎంట్రీ సేవ్ అయిన వెంటనే అతిథి వాట్సాప్‌కు కృతజ్ఞతలతో కూడిన అధికారిక డిజిటల్ తాంబూలం పంపవచ్చు.</p>
          </div>
        </div>

        <div class="bento-box">
          <div>
            <div class="bento-tag">DIGITAL PAYMENTS</div>
            <h3 class="bento-title" data-i18n="bento5_title">🔔 UPI QR Soundbox</h3>
            <p class="bento-desc" data-i18n="bento5_desc">డైనమిక్ QR కోడ్ స్కాన్ చేసి అతిథులు నగదు జమ చేసిన వెంటనే స్పీకర్ ద్వారా తెలుగులోనే ఆడియో ధృవీకరణ.</p>
          </div>
        </div>

        <div class="bento-box">
          <div>
            <div class="bento-tag">NET SURPLUS AUDIT</div>
            <h3 class="bento-title" data-i18n="bento6_title">💸 Expenses vs Net Savings</h3>
            <p class="bento-desc" data-i18n="bento6_desc">కల్యాణ మండపం, భోజనాలు, డెకరేషన్ ఖర్చులన్నీ పోను మొత్తం ఎంత నికర మిగులు ఉందో లైవ్‌గా ట్రాక్ చేయండి.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Events We Support Section (from Nyota) -->
    <section id="events-section" class="section-wrap" style="background: #FFFFFF; border-top: 1px solid var(--border-light);">
      <div class="section-header-center">
        <div class="section-pill-tag" data-i18n="events_tag">అన్ని వేడుకలకు అనుకూలం</div>
        <h2 class="section-main-heading" data-i18n="events_heading">Events We Support</h2>
        <p class="section-main-desc" data-i18n="events_desc">చిన్న పుట్టినరోజు నుండి వేల మంది హాజరయ్యే రాయల్ వివాహాల దాకా.</p>
      </div>

      <div class="celebrations-grid">
        <div class="celebration-item-card">
          <div class="cel-icon">💍</div>
          <div class="cel-name" data-i18n="cel_w">Wedding (వివాహం)</div>
          <div class="cel-desc" data-i18n="cel_w_d">వేల సంఖ్యలో వచ్చే అతిథుల చదివింపులు, బంగారం, వెండి లెక్కలను బహుళ రోజుల పాటు సులభంగా నిర్వహించండి.</div>
        </div>
        <div class="celebration-item-card">
          <div class="cel-icon">👶</div>
          <div class="cel-name" data-i18n="cel_b">Birthday & Barasala</div>
          <div class="cel-desc" data-i18n="cel_b_d">పాప లేదా బాబు బారసాల, నామకరణం, మరియు మొదటి పుట్టినరోజు కానుకల శాశ్వత రికార్డు.</div>
        </div>
        <div class="celebration-item-card">
          <div class="cel-icon">🏡</div>
          <div class="cel-name" data-i18n="cel_h">Housewarming (గృహప్రవేశం)</div>
          <div class="cel-desc" data-i18n="cel_h_d">కొత్త ఇంట్లోకి అడుగుపెట్టే శుభవేళ బంధుమిత్రులు అందించిన ఆశీస్సులు మరియు బహుమతుల వివరాలు.</div>
        </div>
        <div class="celebration-item-card">
          <div class="cel-icon">🪷</div>
          <div class="cel-name" data-i18n="cel_hs">Half Saree / లంగా వోణి</div>
          <div class="cel-desc" data-i18n="cel_hs_d">దక్షిణ భారతదేశ సాంప్రదాయ హాఫ్ శారీ వేడుక కానుకలను ప్రత్యేకంగా ట్రాక్ చేయండి.</div>
        </div>
        <div class="celebration-item-card">
          <div class="cel-icon">🧵</div>
          <div class="cel-name" data-i18n="cel_dh">Upanayanam / ధోతి</div>
          <div class="cel-desc" data-i18n="cel_dh_d">ఉపనయన సంస్కారానికి బంధువులు సమర్పించిన వస్త్రాలు మరియు దక్షిణల నికర వివరాలు.</div>
        </div>
        <div class="celebration-item-card">
          <div class="cel-icon">🎉</div>
          <div class="cel-name" data-i18n="cel_an">Anniversary (శాంతి మహోత్సవం)</div>
          <div class="cel-desc" data-i18n="cel_an_d">షష్టిపూర్తి, రజతోత్సవం లేదా వివాహ వార్షికోత్సవ కానుకల శాశ్వత సంస్మరణ.</div>
        </div>
        <div class="celebration-item-card">
          <div class="cel-icon">🎓</div>
          <div class="cel-name" data-i18n="cel_gr">Graduation & Success</div>
          <div class="cel-desc" data-i18n="cel_gr_d">పిల్లల ఉన్నత చదువులు లేదా విదేశీ ప్రయాణాల సందర్భంగా శ్రేయోభిలాషుల ఆశీస్సులు.</div>
        </div>
        <div class="celebration-item-card">
          <div class="cel-icon">🌸</div>
          <div class="cel-name" data-i18n="cel_di">Festive Gatherings</div>
          <div class="cel-desc" data-i18n="cel_di_d">దీపావళి, సంక్రాంతి కుటుంబ కలయికలలో పరస్పర బహుమతుల పారదర్శక రికార్డు.</div>
        </div>
      </div>
    </section>

    <!-- Comparison Matrix Section -->
    <section id="compare-section" class="section-wrap">
      <div class="section-header-center">
        <div class="section-pill-tag" data-i18n="comp_tag">పారదర్శక పోలిక</div>
        <h2 class="section-main-heading" data-i18n="comp_heading">Manual Red Book vs GiftVault</h2>
      </div>

      <div class="compare-container">
        <table class="compare-table">
          <thead>
            <tr>
              <th data-i18n="comp_col1">అంశం / ఫీచర్</th>
              <th data-i18n="comp_col2">పాత చేతిరాత ఎర్ర పుస్తకం</th>
              <th style="color: var(--crimson-primary);" data-i18n="comp_col3">GiftVault డిజిటల్ ఖజానా</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>నమోదు వేగం (Entry Speed)</strong></td>
              <td style="color: var(--text-muted);">ఆలస్యం, రద్దీ సమయంలో పొరపాట్లు</td>
              <td style="color: var(--emerald-accent); font-weight: 700;">⚡ 3 సెకన్లలో ఆటోకంప్లీట్ ఎంట్రీ</td>
            </tr>
            <tr>
              <td><strong>రికార్డు భద్రత (Record Safety)</strong></td>
              <td style="color: var(--text-muted);">పుస్తకం పోతే లెక్కలు పూర్తిగా గల్లంతు</td>
              <td style="color: var(--emerald-accent); font-weight: 700;">🔒 క్లౌడ్ & ఎక్సెల్ బ్యాకప్‌తో సురక్షితం</td>
            </tr>
            <tr>
              <td><strong>అతిథికి రశీదు (Guest Receipt)</strong></td>
              <td style="color: var(--text-muted);">ఏమీ ఉండదు (కేవలం నమ్మకం)</td>
              <td style="color: var(--emerald-accent); font-weight: 700;">📲 తక్షణ వాట్సాప్ డిజిటల్ తాంబూలం</td>
            </tr>
            <tr>
              <td><strong>తిరిగి ఎంత ఇవ్వాలి? (Reciprocity)</strong></td>
              <td style="color: var(--text-muted);">వందల పాత పేజీలు వెతుక్కోవాలి</td>
              <td style="color: var(--emerald-accent); font-weight: 700;">🔄 ఆటోమేటిక్ స్మార్ట్ రికమండేషన్</td>
            </tr>
            <tr>
              <td><strong>ఖర్చుల మిగులు (Net Surplus)</strong></td>
              <td style="color: var(--text-muted);">క్యాలిక్యులేటర్‌తో రోజుల తరబడి పని</td>
              <td style="color: var(--emerald-accent); font-weight: 700;">📊 క్షణాల్లో ఆటోమేటిక్ ఆడిట్ రిపోర్ట్</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- FAQ Accordion -->
    <section id="faq-section" class="section-wrap" style="background: #FFFFFF; border-top: 1px solid var(--border-light);">
      <div class="section-header-center">
        <div class="section-pill-tag">ప్రశ్నోత్తరాలు</div>
        <h2 class="section-main-heading">Frequently Asked Questions</h2>
        <p class="section-main-desc">GiftVault గురించి కుటుంబ సభ్యులు సాధారణంగా అడిగే సందేహాలు.</p>
      </div>

      <div class="faq-list">
        <div class="faq-item open">
          <div class="faq-question" onclick="toggleFaq(this)">
            <span>GiftVault ఉచితంగా ఉపయోగించవచ్చా?</span>
            <span class="faq-arrow">▼</span>
          </div>
          <div class="faq-answer">
            అవును! వ్యక్తిగత కుటుంబ వేడుకలకు GiftVault 100% ఉచితం. మీరు ఎన్ని ఈవెంట్లయినా క్రియేట్ చేసుకోవచ్చు మరియు ఎన్ని ఎంట్రీలైనా నమోదు చేసుకోవచ్చు.
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question" onclick="toggleFaq(this)">
            <span>మున్షీ డెస్క్ ఇంటర్నెట్ లేకపోయినా పనిచేస్తుందా?</span>
            <span class="faq-arrow">▼</span>
          </div>
          <div class="faq-answer">
            అవును. కళ్యాణ మండపాలలో నెట్‌వర్క్ సమస్యలు ఉన్నప్పటికీ లోకల్ స్టోరేజ్‌లో ఎంట్రీలు నిరంతరాయంగా సేవ్ అవుతాయి. ఎక్సెల్ లేదా CSV ఫైల్‌ను నేరుగా డౌన్‌లోడ్ చేసుకోవచ్చు.
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question" onclick="toggleFaq(this)">
            <span>మా డేటా ఎంతవరకు సురక్షితం?</span>
            <span class="faq-arrow">▼</span>
          </div>
          <div class="faq-answer">
            మీ కుటుంబ లెక్కలు అత్యాధునిక ఎన్‌క్రిప్షన్ ద్వారా భద్రపరచబడతాయి. మీ అనుమతి లేకుండా బయటి వ్యక్తులు ఎవరూ మీ ఖాతాలోకి ప్రవేశించలేరు.
          </div>
        </div>
      </div>
    </section>

    <!-- Grand CTA Banner -->
    <section class="section-wrap" style="padding: 40px 24px;">
      <div style="background: linear-gradient(135deg, #D20F1F, #991B1B); border-radius: 32px; padding: 60px 32px; text-align: center; color: #FFFFFF; box-shadow: var(--shadow-xl);">
        <h2 style="font-size: 34px; font-weight: 800; margin-bottom: 12px;">Ready to organize your family celebration?</h2>
        <p style="font-size: 16px; opacity: 0.9; max-width: 560px; margin: 0 auto 28px auto;">
          సంప్రదాయాలను కాపాడుకుంటూ, సంబంధాలను చిరస్థాయిగా నిలిపే డిజిటల్ ఎర్ర పుస్తకాన్ని ఇప్పుడే ప్రారంభించండి.
        </p>
        <button type="button" class="btn-secondary" style="background: #FFFFFF; color: #D20F1F; padding: 14px 32px; font-size: 15px; border: none;" onclick="navToView('login')">
          ఉచితంగా ప్రారంభించండి →
        </button>
      </div>
    </section>

    <!-- Site Footer -->
    <footer class="site-footer">
      <div class="footer-container">
        <div>
          <div class="brand-wrap" style="margin-bottom: 16px;">
            <div class="brand-icon-box" style="width: 32px; height: 32px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
            </div>
            <div class="brand-title" style="font-size: 18px;">Gift<span>Vault</span></div>
          </div>
          <p style="font-size: 13.5px; color: var(--text-muted); line-height: 1.6; max-width: 280px;">
            The Digital Red Notebook for South Asian families worldwide. Preserving traditions with world-class technology.
          </p>
        </div>

        <div>
          <div class="footer-col-title">PRODUCT</div>
          <a href="#" class="footer-link" onclick="navToView('app'); openAppTab('desk'); return false;">Desk Mode</a>
          <a href="#" class="footer-link" onclick="navToView('app'); openAppTab('ledger'); return false;">Digital Red Book</a>
          <a href="#" class="footer-link" onclick="navToView('app'); openAppTab('expenses'); return false;">Expense Audit</a>
        </div>

        <div>
          <div class="footer-col-title">CELEBRATIONS</div>
          <span class="footer-link">Wedding (వివాహం)</span>
          <span class="footer-link">Housewarming (గృహప్రవేశం)</span>
          <span class="footer-link">Birthday & Barasala</span>
        </div>

        <div>
          <div class="footer-col-title">LANGUAGES</div>
          <span class="footer-link" onclick="switchLanguage('te')">తెలుగు (Telugu)</span>
          <span class="footer-link" onclick="switchLanguage('en')">English</span>
          <span class="footer-link" onclick="switchLanguage('hi')">हिंदी (Hindi)</span>
        </div>
      </div>

      <div style="max-width: 1240px; margin: 0 auto; border-top: 1px solid var(--border-light); padding-top: 24px; display: flex; justify-content: space-between; font-size: 13px; color: var(--text-muted); flex-wrap: wrap; gap: 14px;">
        <div>© 2026 GiftVault Inc. All rights reserved. Zero Slop Architecture.</div>
        <div style="display: flex; gap: 20px;">
          <span>Privacy Policy</span>
          <span>Terms of Service</span>
        </div>
      </div>
    </footer>
  </main>

  <!-- ============================================================
       VIEW 2: DEDICATED FULL-PAGE SIGN-IN (LUXURY SPLIT CARD)
       ============================================================ -->
  <main id="view-login" class="app-view">
    <div class="login-wrapper">
      <div class="login-card-split">
        <!-- Left Showcase Side -->
        <div class="login-left-panel">
          <div>
            <div class="hero-badge" style="background: #FFFFFF;">
              <span class="hero-badge-dot"></span>
              <span>256-BIT ENCRYPTED</span>
            </div>
            <h2 style="font-size: 28px; font-weight: 800; color: var(--text-heading); margin-bottom: 12px; line-height: 1.25;">
              మీ కుటుంబ ఖజానాలోకి ప్రవేశించండి
            </h2>
            <p style="font-size: 14.5px; color: var(--text-body); line-height: 1.6;">
              శుభకార్య యజమానిగా పూర్తి నిర్వహణ చేయండి లేదా మున్షీగా వేగవంతమైన ఎంట్రీలను నమోదు చేయండి.
            </p>
          </div>

          <div style="border-top: 1px solid var(--crimson-border); padding-top: 20px;">
            <div style="font-size: 12px; font-weight: 700; color: var(--crimson-primary); text-transform: uppercase; margin-bottom: 4px;">పూర్తి గోప్యత</div>
            <div style="font-size: 13px; color: var(--text-muted);">మీ కుటుంబ సంప్రదాయ లెక్కలు కేవలం మీ నియంత్రణలోనే భద్రం.</div>
          </div>
        </div>

        <!-- Right Form Side -->
        <div class="login-right-panel">
          <div style="margin-bottom: 24px;">
            <h3 style="font-size: 22px; font-weight: 800; color: var(--text-heading); margin-bottom: 6px;">ఖాతా లాగిన్ (Sign In)</h3>
            <p style="font-size: 13px; color: var(--text-muted);">మొబైల్ OTP లేదా Google ద్వారా సులభంగా ప్రవేశించండి.</p>
          </div>

          <!-- Role Selector -->
          <div class="form-group">
            <label class="form-label">మీ హోదా (Select Role)</label>
            <div class="role-pills">
              <div class="role-pill active" onclick="selectLoginRole('admin', this)">👑 యజమాని</div>
              <div class="role-pill" onclick="selectLoginRole('munshi', this)">⚡ మున్షీ</div>
              <div class="role-pill" onclick="selectLoginRole('viewer', this)">👁️ బంధువు</div>
            </div>
          </div>

          <!-- Phone OTP Section -->
          <div id="login-phone-box">
            <div class="form-group">
              <label class="form-label">మొబైల్ సంఖ్య (Phone Number)</label>
              <div style="display: flex; gap: 8px;">
                <span style="background: var(--bg-surface-soft); border: 1.5px solid var(--border-mid); padding: 12px 14px; border-radius: 12px; font-weight: 600; font-size: 14px;">+91</span>
                <input type="tel" id="login-phone-input" class="form-input" placeholder="98480 12345" value="9848012345" maxlength="10">
              </div>
            </div>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 12px; margin-bottom: 16px;" onclick="handleSendOTP()">
              OTP కోడ్ పంపండి →
            </button>
          </div>

          <!-- OTP Input Step -->
          <div id="login-otp-box" style="display: none;">
            <div class="form-group">
              <label class="form-label">నమోదు చేయవలసిన OTP (టెస్ట్ కోడ్: <strong style="color: var(--crimson-primary);">1234</strong>)</label>
              <div style="display: flex; gap: 10px; justify-content: center; margin: 12px 0;">
                <input type="text" class="form-input" maxlength="1" value="1" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
                <input type="text" class="form-input" maxlength="1" value="2" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
                <input type="text" class="form-input" maxlength="1" value="3" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
                <input type="text" class="form-input" maxlength="1" value="4" style="width: 48px; text-align: center; font-size: 18px; font-weight: 700;">
              </div>
            </div>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 12px; margin-bottom: 16px;" onclick="handleVerifyLogin()">
              ధృవీకరించి ప్రవేశించండి ✓
            </button>
          </div>

          <div style="text-align: center; margin: 12px 0; font-size: 12px; color: var(--text-dim);">లేదా</div>

          <button type="button" class="btn-secondary" style="width: 100%; justify-content: center; padding: 11px; margin-bottom: 18px;" onclick="handleGoogleSignIn()">
            <svg width="16" height="16" viewBox="0 0 24 24"><path fill="#EA4335" d="M12 5c1.6 0 3 .6 4.1 1.6l3.1-3.1C17.3 1.7 14.8 1 12 1 7.5 1 3.7 3.6 1.9 7.3l3.7 2.9C6.5 7.4 9 5 12 5z"/><path fill="#4285F4" d="M23.5 12.3c0-.8-.1-1.7-.2-2.3H12v4.5h6.5c-.3 1.5-1.1 2.8-2.4 3.7l3.7 2.9c2.2-2 3.7-5.1 3.7-8.8z"/><path fill="#FBBC05" d="M5.6 14.8c-.2-.7-.4-1.5-.4-2.3 0-.8.2-1.6.4-2.3L1.9 7.3C.7 9.7 0 12.3 0 15s.7 5.3 1.9 7.7l3.7-2.9z"/><path fill="#34A853" d="M12 23c3.2 0 6-1.1 8-3l-3.7-2.9c-1.1.7-2.5 1.2-4.3 1.2-3 0-5.5-2.4-6.4-5.2L1.9 16c1.8 3.7 5.6 7 10.1 7z"/></svg>
            Google ఖాతాతో సైన్-ఇన్
          </button>

          <div style="text-align: center;">
            <button type="button" onclick="navToView('landing')" style="font-size: 13px; color: var(--text-muted); background: none; border: none; cursor: pointer;">
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
  <main id="view-app" class="app-view">
    <div class="workspace-wrap">
      
      <!-- Top Bar -->
      <div class="workspace-topbar">
        <div style="display: flex; align-items: center; gap: 14px;">
          <div class="brand-icon-box" style="width: 38px; height: 38px;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          </div>
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span id="app-active-event-name" style="font-weight: 800; font-size: 16px; color: var(--text-heading);">రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం</span>
              <span style="background: var(--emerald-bg); color: var(--emerald-accent); font-size: 10px; font-weight: 700; padding: 2px 8px; border-radius: 9999px;">లైవ్ ఖజానా</span>
            </div>
            <div style="font-size: 12px; color: var(--text-muted);">హైదరాబాద్ • జీరో డమ్మీ డేటా ఫ్రెష్ స్టేట్</div>
          </div>
        </div>

        <div style="display: flex; gap: 10px;">
          <button type="button" class="btn-secondary" onclick="navToView('landing')" style="padding: 7px 14px; font-size: 13px;">
            ← హోమ్ పేజీ
          </button>
          <button type="button" class="btn-crimson" onclick="openAppTab('desk')" style="padding: 7px 16px; font-size: 13px;">
            ⚡ ఎంట్రీ డెస్క్
          </button>
        </div>
      </div>

      <!-- App Sub-tabs -->
      <div class="tab-pills-bar">
        <button type="button" class="tab-pill-btn active" onclick="openAppTab('dashboard', this)">📊 డాష్‌బోర్డ్</button>
        <button type="button" class="tab-pill-btn" onclick="openAppTab('desk', this)">✍️ మున్షీ డెస్క్</button>
        <button type="button" class="tab-pill-btn" onclick="openAppTab('ledger', this)">📖 ఎర్ర పుస్తకం</button>
        <button type="button" class="tab-pill-btn" onclick="openAppTab('expenses', this)">💸 ఖర్చులు & సేవింగ్స్</button>
        <button type="button" class="tab-pill-btn" onclick="openAppTab('reciprocity', this)">🔄 మర్యాదలు (Reciprocity)</button>
        <button type="button" class="tab-pill-btn" onclick="openAppTab('soundbox', this)">🔔 UPI QR సౌండ్‌బాక్స్</button>
        <button type="button" class="tab-pill-btn" onclick="openAppTab('settings', this)">⚙️ సెట్టింగ్స్</button>
      </div>

      <!-- TAB 1: DASHBOARD -->
      <div id="tab-dashboard" class="tab-screen active">
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px;">
          <div class="mockup-stat-box" style="background: #FFFFFF;">
            <div class="stat-label">మొత్తం ఆదాయం</div>
            <div class="stat-value" id="dash-inflow-val" style="color: var(--crimson-primary);">₹0</div>
            <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 4px;">0 ఎంట్రీలు నమోదయ్యాయి</div>
          </div>
          <div class="mockup-stat-box" style="background: #FFFFFF;">
            <div class="stat-label">నగదు (Cash)</div>
            <div class="stat-value" id="dash-cash-val">₹0</div>
            <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 4px;">కౌంటర్ బాక్స్ నగదు</div>
          </div>
          <div class="mockup-stat-box" style="background: #FFFFFF;">
            <div class="stat-label">ఆన్‌లైన్ (UPI)</div>
            <div class="stat-value" id="dash-upi-val">₹0</div>
            <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 4px;">బ్యాంక్ ఖాతాకు జమ</div>
          </div>
          <div class="mockup-stat-box" style="background: #FFFFFF;">
            <div class="stat-label">బంగారం / వెండి</div>
            <div class="stat-value" id="dash-jewel-val">0g / 0g</div>
            <div style="font-size: 11.5px; color: var(--text-muted); margin-top: 4px;">బహుమతి ఆభరణాలు</div>
          </div>
        </div>

        <!-- Empty State Prompt -->
        <div id="dash-empty-box" style="text-align: center; padding: 60px 20px; background: #FFFFFF; border: 1.5px dashed var(--border-mid); border-radius: 20px;">
          <div style="font-size: 38px; margin-bottom: 12px;">🪙</div>
          <h3 style="font-size: 19px; font-weight: 800; margin-bottom: 6px; color: var(--text-heading);">ఖజానా ఖాళీగా ఉంది (Fresh State)</h3>
          <p style="font-size: 14px; color: var(--text-muted); max-width: 440px; margin: 0 auto 20px auto;">మొదటి చదివింపును నమోదు చేయడానికి మున్షీ డెస్క్ తెరవండి.</p>
          <button type="button" class="btn-crimson" onclick="openAppTab('desk')">+ మొదటి ఎంట్రీ నమోదు చేయండి</button>
        </div>

        <!-- Recent Records Table -->
        <div id="dash-data-box" style="display: none;" class="ledger-card-wrap">
          <table class="app-data-table">
            <thead>
              <tr>
                <th>రశీదు సంఖ్య</th>
                <th>అతిథి పేరు</th>
                <th>గ్రామం / నగరం</th>
                <th>మొత్తం</th>
                <th>రకం</th>
                <th>వాట్సాప్</th>
              </tr>
            </thead>
            <tbody id="dash-tbody"></tbody>
          </table>
        </div>
      </div>

      <!-- TAB 2: MUNSHI FAST DESK -->
      <div id="tab-desk" class="tab-screen">
        <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px;">
          <!-- Form -->
          <div style="background: #FFFFFF; border: 1.5px solid var(--border-mid); border-radius: 20px; padding: 28px;">
            <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 18px; color: var(--text-heading);">✍️ మున్షీ ఫాస్ట్ ఎంట్రీ ఫారం</h3>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
              <div class="form-group">
                <label class="form-label">అతిథి పేరు *</label>
                <input type="text" id="desk-in-name" class="form-input" placeholder="ఉదా: రామారావు గారు">
              </div>
              <div class="form-group">
                <label class="form-label">గ్రామం / నగరం</label>
                <input type="text" id="desk-in-city" class="form-input" placeholder="విజయవాడ, గుంటూరు, హైదరాబాద్">
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
              <div class="form-group">
                <label class="form-label">మొబైల్ (వాట్సాప్ కోసం)</label>
                <input type="tel" id="desk-in-phone" class="form-input" placeholder="9848012345">
              </div>
              <div class="form-group">
                <label class="form-label">సంబంధం</label>
                <select id="desk-in-rel" class="form-input">
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
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--border-mid); border-radius: 12px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="desk-gift-type" value="CASH" checked onchange="toggleDeskFields('cash')"> 💵 నగదు
                </label>
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--border-mid); border-radius: 12px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="desk-gift-type" value="UPI" onchange="toggleDeskFields('cash')"> 📲 UPI
                </label>
                <label style="flex: 1; padding: 10px; border: 1.5px solid var(--border-mid); border-radius: 12px; font-size: 13px; font-weight: 600; text-align: center; cursor: pointer;">
                  <input type="radio" name="desk-gift-type" value="GOLD" onchange="toggleDeskFields('gold')"> 🥇 బంగారం/వెండి
                </label>
              </div>
            </div>

            <div id="desk-box-cash" class="form-group">
              <label class="form-label">మొత్తం (రూపాయల్లో) *</label>
              <input type="number" id="desk-in-amount" class="form-input" style="font-size: 20px; font-weight: 800; color: var(--crimson-primary);" placeholder="₹ 1116">
              <div class="coin-wrap">
                <button type="button" class="coin-chip" onclick="setQuickCoin(516)">+ ₹516</button>
                <button type="button" class="coin-chip" onclick="setQuickCoin(1116)">+ ₹1,116</button>
                <button type="button" class="coin-chip" onclick="setQuickCoin(2116)">+ ₹2,116</button>
                <button type="button" class="coin-chip" onclick="setQuickCoin(5116)">+ ₹5,116</button>
                <button type="button" class="coin-chip" onclick="setQuickCoin(10116)">+ ₹10,116</button>
                <button type="button" class="coin-chip" onclick="addLuckyCoin()">+ ₹1 కాయిన్</button>
              </div>
            </div>

            <div id="desk-box-gold" class="form-group" style="display: none;">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
                <div>
                  <label class="form-label">బంగారం (గ్రాములు)</label>
                  <input type="number" step="0.1" id="desk-in-gold" class="form-input" placeholder="ఉదా: 8.0">
                </div>
                <div>
                  <label class="form-label">వెండి (గ్రాములు)</label>
                  <input type="number" step="1" id="desk-in-silver" class="form-input" placeholder="ఉదా: 100">
                </div>
              </div>
            </div>

            <div style="display: flex; gap: 12px; margin-top: 14px;">
              <button type="button" class="btn-crimson" style="flex: 1; justify-content: center; padding: 13px;" onclick="saveMunshiEntry()">
                💾 ఎంట్రీ భద్రపరచండి (Save)
              </button>
              <button type="button" class="btn-secondary" onclick="clearMunshiForm()">
                క్లియర్
              </button>
            </div>
          </div>

          <!-- Quick Receipts Card -->
          <div style="background: #FFFFFF; border: 1.5px solid var(--border-mid); border-radius: 20px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <h4 style="font-size: 16px; font-weight: 800; color: var(--text-heading); margin-bottom: 14px;">
                🔔 మున్షీ సౌండ్‌బాక్స్ & ఆఖరి రశీదు
              </h4>
              <p style="font-size: 13.5px; color: var(--text-muted); line-height: 1.6; margin-bottom: 18px;">
                ప్రతి ఎంట్రీ నమోదు కాగానే స్పీకర్ ద్వారా వెబ్ ఆడియో ధ్వని ధృవీకరణ వినిపిస్తుంది.
              </p>

              <div style="background: var(--crimson-bg); border: 1px solid var(--crimson-border); border-radius: 14px; padding: 16px; margin-bottom: 18px;">
                <div style="font-size: 12px; font-weight: 700; color: var(--crimson-primary); text-transform: uppercase; margin-bottom: 4px;">ఆఖరి నమోదు రసీదు:</div>
                <div id="desk-receipt-live" style="font-size: 14.5px; font-weight: 700; color: var(--text-heading);">ఇంకా ఏమీ నమోదు కాలేదు</div>
              </div>
            </div>

            <button type="button" class="btn-secondary" style="width: 100%; justify-content: center;" onclick="playAudioChime(); showAppToast('🔊 సౌండ్‌బాక్స్ టెస్ట్ ధ్వని వినిపించింది!');">
              🔊 సౌండ్‌బాక్స్ టెస్ట్ చేయండి
            </button>
          </div>
        </div>
      </div>

      <!-- TAB 3: RED BOOK LEDGER -->
      <div id="tab-ledger" class="tab-screen">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; flex-wrap: wrap; gap: 12px;">
          <div>
            <h3 style="font-size: 20px; font-weight: 800; color: var(--text-heading);">📖 ఎర్ర పుస్తకం (డిజిటల్ శగున్ లెడ్జర్)</h3>
            <p style="font-size: 13px; color: var(--text-muted);">పూర్తి చదివింపుల వివరాలు మరియు రికార్డులు</p>
          </div>
          <div style="display: flex; gap: 10px;">
            <button type="button" class="btn-secondary" onclick="exportLedgerCSV()">📥 ఎక్సెల్ (CSV) డౌన్‌లోడ్</button>
            <button type="button" class="btn-crimson" onclick="window.print()">🖨️ ప్రింట్ రిపోర్ట్</button>
          </div>
        </div>

        <div class="ledger-card-wrap">
          <table class="app-data-table">
            <thead>
              <tr>
                <th>క్రమ సంఖ్య</th>
                <th>రశీదు సంఖ్య</th>
                <th>అతిథి పేరు</th>
                <th>ఊరు</th>
                <th>సంబంధం</th>
                <th>కానుక మొత్తం</th>
                <th>బంగారం/వెండి</th>
                <th>రకం</th>
                <th>చర్య</th>
              </tr>
            </thead>
            <tbody id="ledger-full-tbody">
              <tr>
                <td colspan="9" style="text-align: center; color: var(--text-dim); padding: 32px;">ఇంకా ఎలాంటి రికార్డులు నమోదు కాలేదు.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TAB 4: EXPENSES -->
      <div id="tab-expenses" class="tab-screen">
        <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 24px;">
          <div style="background: #FFFFFF; border: 1.5px solid var(--border-mid); border-radius: 20px; padding: 28px;">
            <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 16px; color: var(--text-heading);">💸 ఫంక్షన్ ఖర్చు నమోదు</h3>
            <div class="form-group">
              <label class="form-label">ఖర్చు కేటగిరీ</label>
              <select id="exp-in-cat" class="form-input">
                <option value="కల్యాణ మండపం / వేదిక">కల్యాణ మండపం / వేదిక</option>
                <option value="క్యాటరింగ్ / భోజనాలు">క్యాటరింగ్ / భోజనాలు</option>
                <option value="డెకరేషన్ & లైటింగ్">డెకరేషన్ & లైటింగ్</option>
                <option value="ఫోటో & వీడియోగ్రఫీ">ఫోటో & వీడియోగ్రఫీ</option>
                <option value="బాజా భజంత్రీలు / సంగీతం">బాజా భజంత్రీలు / సంగీతం</option>
                <option value="ఇతర ఖర్చులు">ఇతర ఖర్చులు</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">వివరణ / నోట్స్</label>
              <input type="text" id="exp-in-notes" class="form-input" placeholder="ఉదా: క్యాటరింగ్ అడ్వాన్స్ చెల్లింపు">
            </div>
            <div class="form-group">
              <label class="form-label">మొత్తం (రూపాయల్లో) *</label>
              <input type="number" id="exp-in-amount" class="form-input" placeholder="₹ 50000">
            </div>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 12px;" onclick="saveAppExpense()">
              + ఖర్చును జోడించండి
            </button>
          </div>

          <div style="background: #FFFFFF; border: 1.5px solid var(--border-mid); border-radius: 20px; padding: 28px;">
            <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 16px; color: var(--text-heading);">📊 ఖర్చులు vs నికర మిగులు</h3>
            <div class="mockup-stat-box" style="margin-bottom: 12px; background: #FFFFFF;">
              <div class="stat-label">మొత్తం ఆదాయం</div>
              <div class="stat-value" id="exp-sum-in" style="color: var(--crimson-primary);">₹0</div>
            </div>
            <div class="mockup-stat-box" style="margin-bottom: 12px; background: #FFFFFF;">
              <div class="stat-label">మొత్తం ఖర్చులు</div>
              <div class="stat-value" id="exp-sum-out" style="color: var(--text-body);">₹0</div>
            </div>
            <div class="mockup-stat-box" style="background: #FFFFFF;">
              <div class="stat-label">నికర మిగులు ఆదా</div>
              <div class="stat-value" id="exp-sum-sur" style="color: var(--emerald-accent);">₹0</div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 5: RECIPROCITY -->
      <div id="tab-reciprocity" class="tab-screen">
        <div style="background: #FFFFFF; border: 1.5px solid var(--border-mid); border-radius: 20px; padding: 24px; margin-bottom: 20px;">
          <h3 style="font-size: 18px; font-weight: 800; margin-bottom: 8px; color: var(--text-heading);">🔄 పరస్పర మర్యాదల విశ్లేషణ (Reciprocity Tracker)</h3>
          <p style="font-size: 14px; color: var(--text-muted);">
            గతంలో మన శుభకార్యానికి ఎవరు ఎంత ఇచ్చారో, భవిష్యత్తులో మనం వారి వేడుకకు ఎంత తిరిగి ఇవ్వాలనే పక్కా సిఫార్సులు.
          </p>
        </div>
        <div class="ledger-card-wrap">
          <table class="app-data-table">
            <thead>
              <tr>
                <th>వ్యక్తి పేరు</th>
                <th>ఊరు</th>
                <th>వారు మనకిచ్చింది</th>
                <th>మనం తిరిగి ఇవ్వవలసిన సిఫార్సు (+₹1)</th>
                <th>స్థితి</th>
              </tr>
            </thead>
            <tbody id="recip-tbody-full">
              <tr>
                <td colspan="5" style="text-align: center; color: var(--text-dim); padding: 32px;">ఎంట్రీలు నమోదు కాగానే ఇక్కడ ఆటోమేటిక్‌గా విశ్లేషణ కనిపిస్తుంది.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TAB 6: SOUNDBOX QR -->
      <div id="tab-soundbox" class="tab-screen">
        <div style="max-width: 480px; margin: 0 auto; background: #FFFFFF; border: 1.5px solid var(--border-mid); border-radius: 24px; padding: 36px; text-align: center; box-shadow: var(--shadow-md);">
          <div class="hero-badge" style="margin-bottom: 14px;">
            <span class="hero-badge-dot"></span>
            <span>లైవ్ UPI కౌంటర్ సౌండ్‌బాక్స్</span>
          </div>
          <h3 style="font-size: 20px; font-weight: 800; margin-bottom: 6px; color: var(--text-heading);">స్కాన్ చేసి కానుకను పంపండి</h3>
          <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">మొబైల్ ఫోన్‌పే, గూగుల్‌పే, పేటీఎం ద్వారా నేరుగా జమ చేయవచ్చు.</p>

          <div style="background: #FFFFFF; padding: 14px; border: 1.5px solid var(--border-mid); border-radius: 16px; display: inline-block; margin-bottom: 18px;">
            <img src="https://api.qrserver.com/v1/create-qr-code/?size=180x180&data=upi://pay?pa=giftvault@hdfcbank&am=1116&cu=INR" alt="UPI QR" style="display: block; border-radius: 8px;">
          </div>

          <div style="font-weight: 700; font-size: 15px; margin-bottom: 4px; color: var(--text-heading);">UPI ID: giftvault@hdfcbank</div>
          <div style="font-size: 12.5px; color: var(--text-muted); margin-bottom: 20px;">స్కాన్ చేసి చెల్లించిన వెంటనే ఆడియో అలర్ట్ వస్తుంది</div>

          <button type="button" class="btn-crimson" style="width: 100%; justify-content: center;" onclick="playAudioChime(); showAppToast('🔔 ₹1,116 జమ అయ్యింది! వాయిస్ సౌండ్‌బాక్స్ ధృవీకరించబడింది.');">
            🔔 చెల్లింపును ధ్వనితో ధృవీకరించండి (Simulate)
          </button>
        </div>
      </div>

      <!-- TAB 7: SETTINGS -->
      <div id="tab-settings" class="tab-screen">
        <div style="max-width: 600px; margin: 0 auto; background: #FFFFFF; border: 1.5px solid var(--border-mid); border-radius: 20px; padding: 28px;">
          <h3 style="font-size: 19px; font-weight: 800; margin-bottom: 18px; color: var(--text-heading);">⚙️ ఖజానా సెట్టింగ్స్</h3>
          <div class="form-group">
            <label class="form-label">శుభకార్యం పేరు</label>
            <input type="text" class="form-input" value="రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం">
          </div>
          <div class="form-group">
            <label class="form-label">యజమాని ఫోన్ నంబర్</label>
            <input type="tel" class="form-input" value="9848012345">
          </div>
          <div style="border-top: 1px solid var(--border-light); padding-top: 20px; margin-top: 20px;">
            <button type="button" class="btn-secondary" style="color: var(--crimson-primary); border-color: var(--crimson-border);" onclick="resetAllAppData()">
              🗑️ డేటాను పూర్తిగా రీసెట్ చేయండి (Fresh ₹0 State)
            </button>
          </div>
        </div>
      </div>

    </div>
  </main>

  <!-- Global Toast -->
  <div id="app-toast" class="toast-popup"></div>

  <!-- Client-side Logic & Multi-language Dictionary -->
  <script>
    const I18N = {
      te: {
        nav_home: 'హోమ్',
        nav_features: 'ఫీచర్స్',
        nav_celebrations: 'వేడుకలు',
        nav_compare: 'ఎర్ర పుస్తకం పోలిక',
        nav_faq: 'ప్రశ్నోత్తరాలు',
        btn_login: 'లాగిన్ (Sign In)',
        btn_launch: 'ఖజానా తెరవండి →',
        hero_badge: 'ఆండ్రాయిడ్, iOS & వెబ్ లైవ్ • కుటుంబాలకు ఉచితం',
        hero_h1: 'భారతీయ కుటుంబాల <span>రాయల్ శగున్ లెడ్జర్</span>.',
        hero_desc: 'వివాహాలు, బారసాల, గృహప్రవేశాల కానుకల లెక్కలు, ఎర్ర పుస్తకం మరియు వాట్సాప్ తాంబూలం — శతాబ్దాల సాంప్రదాయాలకు ఆధునిక డిజిటల్ రూపం.',
        hero_cta_primary: '⚡ మున్షీ డెస్క్ తెరవండి (Fast Entry)',
        hero_cta_secondary: 'కుటుంబ లాగిన్',
        hero_proof: 'ప్రపంచవ్యాప్తంగా వేలాది భారతీయ కుటుంబాల నమ్మకం',
        stat_inflow: 'మొత్తం చదివింపులు',
        stat_expenses: 'ఫంక్షన్ ఖర్చులు',
        stat_surplus: 'నికర మిగులు',
        stat_jewels: 'బంగారం & వెండి',
        mockup_recent_title: 'తాజా ఎంట్రీలు (Live Feed)',
        found_tag: 'భరోసా & భద్రత',
        found_heading: 'Secure Foundations for Modern Traditions',
        found_desc: 'శతాబ్దాల సాంప్రదాయ విలువలను ఆధునిక సాంకేతిక భద్రతతో అందిస్తున్నాము.',
        found_card1_title: 'Secure & Private',
        found_card1_desc: 'మీ డేటా పూర్తిగా ఎన్‌క్రిప్ట్ చేయబడుతుంది. మీ కుటుంబ సభ్యుల అనుమతి లేకుండా ఎవరూ చూడలేరు.',
        found_card2_title: 'Made for Every Family',
        found_card2_desc: 'తెలుగు, ఇంగ్లీష్, హిందీ భాషలలో అందుబాటులో ఉంది.',
        found_card3_title: 'Easy Export',
        found_card3_desc: 'ఒక్క క్లిక్‌తో పూర్తి ఎర్ర పుస్తకాన్ని ఎక్సెల్ లేదా పిడిఎఫ్ రూపంలో డౌన్‌లోడ్ చేసుకోవచ్చు.',
        feat_tag: 'ప్రత్యేక సదుపాయాలు',
        feat_heading: 'Built for Every Family Celebration',
        feat_desc: 'మున్షీ రద్దీ సమయంలో క్షణాల్లో ఎంట్రీలు చేయడం మొదలుకొని, తిరిగి ఇవ్వవలసిన మర్యాదల వరకు.',
        bento1_title: '⚡ Desk Mode (మున్షీ డెస్క్)',
        bento1_desc: 'తీవ్రమైన రద్దీ ఉన్నప్పుడు 3 సెకన్లలో ఎంట్రీ చేయడానికి ప్రత్యేకంగా రూపొందించబడింది. +₹1 లక్కీ కాయిన్ ఆటో-రౌండింగ్ సదుపాయం.',
        bento2_title: '🔄 Smart History (మర్యాదల లెక్క)',
        bento2_desc: 'వారు గతంలో మన ఫంక్షన్‌కు ఎంత ఇచ్చారో వెంటనే చూపిస్తుంది. భవిష్యత్తులో మనం ఎంత ఇవ్వాలో పక్కా లెక్క.',
        bento3_title: '📊 Digital Reports (ఎర్ర పుస్తకం)',
        bento3_desc: 'అమరావతి & తెలంగాణ గ్రామీణ లెక్కల చిట్టా ఫార్మాట్. ఎప్పుడైనా ప్రింట్ లేదా ఎక్సెల్ రూపంలో సురక్షితం.',
        bento4_title: '📲 WhatsApp Digital Receipts',
        bento4_desc: 'ఎంట్రీ సేవ్ అయిన వెంటనే అతిథి వాట్సాప్‌కు కృతజ్ఞతలతో కూడిన అధికారిక డిజిటల్ తాంబూలం పంపవచ్చు.',
        bento5_title: '🔔 UPI QR Soundbox',
        bento5_desc: 'డైనమిక్ QR కోడ్ స్కాన్ చేసి అతిథులు నగదు జమ చేసిన వెంటనే స్పీకర్ ద్వారా తెలుగులోనే ఆడియో ధృవీకరణ.',
        bento6_title: '💸 Expenses vs Net Savings',
        bento6_desc: 'కల్యాణ మండపం, భోజనాలు, డెకరేషన్ ఖర్చులన్నీ పోను మొత్తం ఎంత నికర మిగులు ఉందో లైవ్‌గా ట్రాక్ చేయండి.',
        events_tag: 'అన్ని వేడుకలకు అనుకూలం',
        events_heading: 'Events We Support',
        events_desc: 'చిన్న పుట్టినరోజు నుండి వేల మంది హాజరయ్యే రాయల్ వివాహాల దాకా.'
      },
      en: {
        nav_home: 'Home',
        nav_features: 'Features',
        nav_celebrations: 'Celebrations',
        nav_compare: 'Comparison',
        nav_faq: 'FAQ',
        btn_login: 'Sign In',
        btn_launch: 'Open Vault →',
        hero_badge: 'Live on Android, iOS & Web • Free for Families',
        hero_h1: 'The App for Every Family <span>Celebration</span>.',
        hero_desc: 'Organize events, manage your guest list, and record every gift — the modern, elegant way to keep the traditional family Red Notebook.',
        hero_cta_primary: '⚡ Open Munshi Desk (Fast Entry)',
        hero_cta_secondary: 'Family Login',
        hero_proof: 'Trusted by South Asian families worldwide • Settle gifts effortlessly',
        stat_inflow: 'Total Blessings',
        stat_expenses: 'Event Expenses',
        stat_surplus: 'Net Surplus',
        stat_jewels: 'Gold & Silver',
        mockup_recent_title: 'Live Gift Entries',
        found_tag: 'Trust & Privacy',
        found_heading: 'Secure Foundations for Modern Traditions',
        found_desc: 'We combine centuries-old cultural values with world-class technology to ensure your blessings are always protected.',
        found_card1_title: 'Secure & Private',
        found_card1_desc: 'Your data is encrypted in transit and at rest, protected by strict access controls.',
        found_card2_title: 'Made for Every Family',
        found_card2_desc: 'Available in Telugu, English, and Hindi for families wherever they call home.',
        found_card3_title: 'Easy Export',
        found_card3_desc: 'Generate comprehensive Excel and PDF reports of all gifts received in one click.',
        feat_tag: 'Core Capabilities',
        feat_heading: 'Built for Every Family Celebration',
        feat_desc: 'From high-speed reception desk entry to automated reciprocity tracking.',
        bento1_title: '⚡ Desk Mode',
        bento1_desc: 'Enter gifts in seconds. Designed specifically for the busy Munshi at the reception counter with +₹1 lucky coin.',
        bento2_title: '🔄 Smart History',
        bento2_desc: 'Never forget what they gave you. GiftVault instantly pulls up your relationship history and recommended reciprocity.',
        bento3_title: '📊 Digital Red Notebook',
        bento3_desc: 'Export your entire event summary to Excel or PDF to settle accounts with total transparency.',
        bento4_title: '📲 WhatsApp Digital Receipts',
        bento4_desc: 'Instantly send a polite, beautiful digital acknowledgement directly to the guest’s WhatsApp.',
        bento5_title: '🔔 UPI QR Soundbox',
        bento5_desc: 'Instant audio announcement when guests scan and transfer blessings via UPI.',
        bento6_title: '💸 Expenses vs Net Surplus',
        bento6_desc: 'Track venue, catering, and floral decor expenses against total Shagun received in real-time.',
        events_tag: 'Versatile Ledger',
        events_heading: 'Events We Support',
        events_desc: 'From intimate baby showers to grand multi-day Indian weddings.'
      },
      hi: {
        nav_home: 'होम',
        nav_features: 'सुविधाएं',
        nav_celebrations: 'उत्सव',
        nav_compare: 'लाल किताब तुलना',
        nav_faq: 'सवाल-जवाब',
        btn_login: 'लॉग इन (Sign In)',
        btn_launch: 'खजाना खोलें →',
        hero_badge: 'एंड्रॉइड, iOS और वेब पर लाइव • परिवारों के लिए मुफ्त',
        hero_h1: 'हर पारिवारिक उत्सव का <span>डिजिटल शगुन लेजर</span>.',
        hero_desc: 'इवेंट्स व्यवस्थित करें, मेहमानों की सूची संभालें और हर शगुन उपहार दर्ज करें — पारंपरिक लाल डायरी का आधुनिक रूप।',
        hero_cta_primary: '⚡ मुंशी डेस्क खोलें (Fast Entry)',
        hero_cta_secondary: 'पारिवारिक लॉगिन',
        hero_proof: 'दुनिया भर में दक्षिण एशियाई परिवारों का विश्वसनीय साथी',
        stat_inflow: 'कुल शगुन',
        stat_expenses: 'उत्सव के खर्चे',
        stat_surplus: 'शुद्ध बचत',
        stat_jewels: 'सोना और चांदी',
        mockup_recent_title: 'ताज़ा शगुन प्रविष्टियां',
        found_tag: 'सुरक्षा और परंपरा',
        found_heading: 'Secure Foundations for Modern Traditions',
        found_desc: 'पारंपरिक सांस्कृतिक मूल्यों को आधुनिक डिजिटल सुरक्षा के साथ पेश करते हैं।',
        found_card1_title: 'Secure & Private',
        found_card1_desc: 'आपका डेटा पूरी तरह से एन्क्रिप्टेड है और सुरक्षित है।',
        found_card2_title: 'Made for Every Family',
        found_card2_desc: 'तेलुगु, अंग्रेजी और हिंदी में उपलब्ध।',
        found_card3_title: 'Easy Export',
        found_card3_desc: 'एक क्लिक में पूरी लाल किताब को एक्सेल या पीडीएफ में डाउनलोड करें।',
        feat_tag: 'प्रमुख विशेषताएं',
        feat_heading: 'Built for Every Family Celebration',
        feat_desc: 'रिसेप्शन काउंटर पर त्वरित प्रविष्टि से लेकर पारस्परिक उपहार गणना तक।',
        bento1_title: '⚡ Desk Mode (मुंशी डेस्क)',
        bento1_desc: 'भीड़ के समय 3 सेकंड में प्रविष्टि दर्ज करने के लिए डिज़ाइन किया गया। +₹1 लकी कॉइन ऑटो-राउंडिंग।',
        bento2_title: '🔄 Smart History (पारस्परिक हिसाब)',
        bento2_desc: 'अतीत में उन्होंने क्या उपहार दिया था, तुरंत दिखाता है।',
        bento3_title: '📊 Digital Reports (लाल डायरी)',
        bento3_desc: 'एक्सेल और पीडीएफ में डाउनलोड करें।',
        bento4_title: '📲 WhatsApp Digital Receipts',
        bento4_desc: 'व्हाट्सएप पर तुरंत डिजिटल रसीद और आभार भेजें।',
        bento5_title: '🔔 UPI QR Soundbox',
        bento5_desc: 'क्यूआर कोड स्कैन करके भुगतान करने पर ध्वनि पुष्टि।',
        bento6_title: '💸 Expenses vs Net Surplus',
        bento6_desc: 'खर्चों और कुल शगुन का रीयल-टाइम शुद्ध विश्लेषण।',
        events_tag: 'सभी समारोहों के लिए',
        events_heading: 'Events We Support',
        events_desc: 'जन्मदिन से लेकर भव्य विवाह समारोहों तक।'
      }
    };

    let APP_STATE = {
      lang: 'te',
      entries: [],
      expenses: [],
      activeRole: 'admin',
      eventName: 'రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం'
    };

    // Load Local Storage
    try {
      const s = localStorage.getItem('GIFTVAULT_NYOTA_DATA');
      if (s) {
        const p = JSON.parse(s);
        APP_STATE.entries = p.entries || [];
        APP_STATE.expenses = p.expenses || [];
      }
    } catch(e) {}

    function persistAppState() {
      try {
        localStorage.setItem('GIFTVAULT_NYOTA_DATA', JSON.stringify({
          entries: APP_STATE.entries,
          expenses: APP_STATE.expenses
        }));
      } catch(e) {}
      renderAppViews();
    }

    // Language switcher
    function switchLanguage(lang, btn) {
      APP_STATE.lang = lang;
      document.body.className = 'lang-' + lang;
      document.querySelectorAll('.lang-btn').forEach(b => {
        b.style.background = 'none';
        b.style.color = 'var(--text-body)';
      });
      if (btn) {
        btn.style.background = 'var(--crimson-primary)';
        btn.style.color = '#FFFFFF';
      }

      const dict = I18N[lang] || I18N.te;
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
          el.innerHTML = dict[key];
        }
      });
    }

    // Navigation Switcher
    function navToView(viewId) {
      document.querySelectorAll('.app-view').forEach(v => v.classList.remove('active'));
      const target = document.getElementById('view-' + viewId);
      if (target) {
        target.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    function openAppTab(tabId, el) {
      navToView('app');
      document.querySelectorAll('.tab-screen').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.tab-pill-btn').forEach(b => b.classList.remove('active'));
      const t = document.getElementById('tab-' + tabId);
      if (t) t.classList.add('active');
      if (el) el.classList.add('active');
    }

    function jumpToSection(id) {
      navToView('landing');
      setTimeout(() => {
        const el = document.getElementById(id);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 80);
    }

    function showAppToast(msg) {
      const t = document.getElementById('app-toast');
      t.innerText = msg;
      t.style.display = 'block';
      setTimeout(() => { t.style.display = 'none'; }, 2800);
    }

    function toggleFaq(el) {
      el.parentElement.classList.toggle('open');
    }

    // Audio chime
    function playAudioChime() {
      try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.frequency.setValueAtTime(587.33, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.15);
        gain.gain.setValueAtTime(0.35, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.75);
        osc.start();
        osc.stop(ctx.currentTime + 0.8);
      } catch(e) {}
    }

    // Hero celebration switcher
    const HERO_DATA = {
      wedding: { title: 'రాహుల్ & స్నిగ్ధ వివాహ మహోత్సవం', sub: 'హైదరాబాద్ • లైవ్ ఖజానా', icon: '💍', inflow: '₹8,42,116', exp: '₹4,15,000', sur: '+₹4,27,116' },
      birthday: { title: 'అద్వైత్ మొదటి పుట్టినరోజు & బారసాల', sub: 'గుంటూరు • లైవ్ ఖజానా', icon: '👶', inflow: '₹3,18,116', exp: '₹1,20,000', sur: '+₹1,98,116' },
      halfsaree: { title: 'సహస్ర లంగా వోణి (హాఫ్ శారీ) వేడుక', sub: 'విజయవాడ • లైవ్ ఖజానా', icon: '🪷', inflow: '₹5,62,116', exp: '₹2,50,000', sur: '+₹3,12,116' },
      housewarming: { title: 'శ్రీ నిలయం గృహప్రవేశ మహోత్సవం', sub: 'విశాఖపట్నం • లైవ్ ఖజానా', icon: '🏡', inflow: '₹6,75,116', exp: '₹3,10,000', sur: '+₹3,65,116' }
    };

    function setHeroCelebration(key, btn) {
      document.querySelectorAll('.cel-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      const d = HERO_DATA[key];
      if (d) {
        document.getElementById('hero-mock-title').innerText = d.title;
        document.getElementById('hero-mock-sub').innerText = d.sub;
        document.getElementById('hero-mock-icon').innerText = d.icon;
        document.getElementById('mock-inflow').innerText = d.inflow;
        document.getElementById('mock-exp').innerText = d.exp;
        document.getElementById('mock-surplus').innerText = d.sur;
      }
    }

    // Login logic
    function selectLoginRole(role, el) {
      APP_STATE.activeRole = role;
      document.querySelectorAll('.role-pill').forEach(p => p.classList.remove('active'));
      if (el) el.classList.add('active');
    }

    function handleSendOTP() {
      const p = document.getElementById('login-phone-input').value.trim();
      if (!p || p.length < 10) {
        showAppToast('దయచేసి సరైన మొబైల్ సంఖ్య నమోదు చేయండి.');
        return;
      }
      document.getElementById('login-phone-box').style.display = 'none';
      document.getElementById('login-otp-box').style.display = 'block';
      showAppToast('టెస్ట్ OTP: 1234 పంపబడింది!');
    }

    function handleVerifyLogin() {
      showAppToast('లాగిన్ విజయవంతమైంది! ఖజానాలోకి ప్రవేశిస్తున్నారు...');
      setTimeout(() => {
        openAppTab('dashboard');
      }, 400);
    }

    function handleGoogleSignIn() {
      showAppToast('Google ద్వారా విజయవంతంగా సైన్-ఇన్ అయ్యారు!');
      setTimeout(() => {
        openAppTab('dashboard');
      }, 400);
    }

    // Munshi Desk Entry
    function setQuickCoin(amt) {
      document.getElementById('desk-in-amount').value = amt;
    }

    function addLuckyCoin() {
      const f = document.getElementById('desk-in-amount');
      let val = parseInt(f.value) || 0;
      f.value = val + (val % 10 === 0 ? 1 : 16);
    }

    function toggleDeskFields(type) {
      if (type === 'gold') {
        document.getElementById('desk-box-cash').style.display = 'none';
        document.getElementById('desk-box-gold').style.display = 'block';
      } else {
        document.getElementById('desk-box-cash').style.display = 'block';
        document.getElementById('desk-box-gold').style.display = 'none';
      }
    }

    function saveMunshiEntry() {
      const name = document.getElementById('desk-in-name').value.trim();
      const city = document.getElementById('desk-in-city').value.trim() || 'స్థానిక';
      const phone = document.getElementById('desk-in-phone').value.trim();
      const rel = document.getElementById('desk-in-rel').value;
      const type = document.querySelector('input[name="desk-gift-type"]:checked').value;

      let amount = 0, gold = 0, silver = 0;
      if (type === 'GOLD') {
        gold = parseFloat(document.getElementById('desk-in-gold').value) || 0;
        silver = parseFloat(document.getElementById('desk-in-silver').value) || 0;
        if (gold <= 0 && silver <= 0) {
          showAppToast('దయచేసి బంగారం లేదా వెండి బరువు నమోదు చేయండి.');
          return;
        }
      } else {
        amount = parseInt(document.getElementById('desk-in-amount').value) || 0;
        if (amount <= 0) {
          showAppToast('దయచేసి సరైన కానుక మొత్తం నమోదు చేయండి.');
          return;
        }
      }

      if (!name) {
        showAppToast('దయచేసి అతిథి పేరు నమోదు చేయండి.');
        return;
      }

      const receiptNo = 'GV-' + (100 + APP_STATE.entries.length + 1);
      const entry = {
        id: Date.now(),
        receiptNo,
        name,
        city,
        phone,
        relation: rel,
        type,
        amount,
        gold,
        silver,
        date: new Date().toLocaleTimeString('te-IN', { hour: '2-digit', minute: '2-digit' })
      };

      APP_STATE.entries.unshift(entry);
      persistAppState();
      playAudioChime();

      document.getElementById('desk-receipt-live').innerText = `${name} (${city}) - ${amount > 0 ? '₹' + amount.toLocaleString('en-IN') : gold + 'g గోల్డ్'} [${receiptNo}]`;
      showAppToast(`రశీదు #${receiptNo} విజయవంతంగా నమోదైంది!`);
      clearMunshiForm();
    }

    function clearMunshiForm() {
      document.getElementById('desk-in-name').value = '';
      document.getElementById('desk-in-city').value = '';
      document.getElementById('desk-in-phone').value = '';
      document.getElementById('desk-in-amount').value = '';
      document.getElementById('desk-in-gold').value = '';
      document.getElementById('desk-in-silver').value = '';
    }

    // Expense Save
    function saveAppExpense() {
      const cat = document.getElementById('exp-in-cat').value;
      const notes = document.getElementById('exp-in-notes').value.trim();
      const amt = parseInt(document.getElementById('exp-in-amount').value) || 0;
      if (amt <= 0) {
        showAppToast('దయచేసి సరైన ఖర్చు మొత్తాన్ని నమోదు చేయండి.');
        return;
      }
      APP_STATE.expenses.push({ id: Date.now(), cat, notes, amt });
      persistAppState();
      showAppToast('ఖర్చు విజయవంతంగా నమోదైంది!');
      document.getElementById('exp-in-notes').value = '';
      document.getElementById('exp-in-amount').value = '';
    }

    function resetAllAppData() {
      if (confirm('మీరు ఖజానాలోని అన్ని రికార్డులను క్లియర్ చేసి ఫ్రెష్ ₹0 స్టేట్ చేయాలనుకుంటున్నారా?')) {
        APP_STATE.entries = [];
        APP_STATE.expenses = [];
        persistAppState();
        showAppToast('డేటా పూర్తిగా రీసెట్ చేయబడింది! ఫ్రెష్ ఖజానా సిద్ధం.');
      }
    }

    function exportLedgerCSV() {
      if (APP_STATE.entries.length === 0) {
        showAppToast('ఎక్స్‌పోర్ట్ చేయడానికి ఎలాంటి రికార్డులు లేవు.');
        return;
      }
      let csv = "\uFEFFరసీదు,పేరు,గ్రామం,సంబంధం,కానుక మొత్తం,బంగారం,వెండి,రకం,సమయం\n";
      APP_STATE.entries.forEach(e => {
        csv += `"${e.receiptNo}","${e.name}","${e.city}","${e.relation}",${e.amount},${e.gold},${e.silver},"${e.type}","${e.date}"\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `GiftVault_Erra_Pusthakam_${Date.now()}.csv`;
      a.click();
      showAppToast('ఎక్సెల్ (CSV) డౌన్‌లోడ్ ప్రారంభమైంది!');
    }

    // Render Function
    function renderAppViews() {
      let tot = 0, cash = 0, upi = 0, goldTot = 0, silverTot = 0;
      APP_STATE.entries.forEach(e => {
        tot += e.amount || 0;
        if (e.type === 'CASH') cash += e.amount || 0;
        if (e.type === 'UPI') upi += e.amount || 0;
        goldTot += e.gold || 0;
        silverTot += e.silver || 0;
      });

      let expTot = 0;
      APP_STATE.expenses.forEach(x => { expTot += x.amt || 0; });
      const surplus = tot - expTot;

      // Dashboard Numbers
      document.getElementById('dash-inflow-val').innerText = '₹' + tot.toLocaleString('en-IN');
      document.getElementById('dash-cash-val').innerText = '₹' + cash.toLocaleString('en-IN');
      document.getElementById('dash-upi-val').innerText = '₹' + upi.toLocaleString('en-IN');
      document.getElementById('dash-jewel-val').innerText = `${goldTot}g / ${silverTot}g`;

      // Expenses Numbers
      document.getElementById('exp-sum-in').innerText = '₹' + tot.toLocaleString('en-IN');
      document.getElementById('exp-sum-out').innerText = '₹' + expTot.toLocaleString('en-IN');
      document.getElementById('exp-sum-sur').innerText = (surplus >= 0 ? '+₹' : '-₹') + Math.abs(surplus).toLocaleString('en-IN');

      const emptyBox = document.getElementById('dash-empty-box');
      const dataBox = document.getElementById('dash-data-box');
      const dashTbody = document.getElementById('dash-tbody');
      const ledgerTbody = document.getElementById('ledger-full-tbody');
      const recipTbody = document.getElementById('recip-tbody-full');

      if (APP_STATE.entries.length === 0) {
        emptyBox.style.display = 'block';
        dataBox.style.display = 'none';
        ledgerTbody.innerHTML = '<tr><td colspan="9" style="text-align: center; color: var(--text-dim); padding: 32px;">ఇంకా ఎలాంటి రికార్డులు నమోదు కాలేదు.</td></tr>';
        recipTbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: var(--text-dim); padding: 32px;">ఎంట్రీలు నమోదు కాగానే ఇక్కడ ఆటోమేటిక్‌గా విశ్లేషణ కనిపిస్తుంది.</td></tr>';
      } else {
        emptyBox.style.display = 'none';
        dataBox.style.display = 'block';

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
              <td style="font-weight: 700;">${e.name}</td>
              <td>${e.city}</td>
              <td style="font-weight: 800; color: var(--crimson-primary);">${amtStr}</td>
              <td><span style="font-size: 11px; background: var(--crimson-bg); color: var(--crimson-primary); padding: 3px 8px; border-radius: 6px; font-weight: 600;">${e.type}</span></td>
              <td><button type="button" class="btn-secondary" style="padding: 4px 10px; font-size: 11px;" onclick="window.open('https://wa.me/91${e.phone||'9848012345'}?text=ధన్యవాదాలు', '_blank')">వాట్సాప్</button></td>
            </tr>
          `;

          ledgerHtml += `
            <tr>
              <td>${idx + 1}</td>
              <td><strong>#${e.receiptNo}</strong></td>
              <td><strong>${e.name}</strong></td>
              <td>${e.city}</td>
              <td>${e.relation}</td>
              <td style="font-weight: 800; color: var(--crimson-primary);">${amtStr}</td>
              <td>${jewelStr}</td>
              <td><span style="font-size: 11px; background: var(--crimson-bg); color: var(--crimson-primary); padding: 3px 8px; border-radius: 6px; font-weight: 600;">${e.type}</span></td>
              <td><button type="button" class="btn-secondary" style="padding: 4px 10px; font-size: 11px;" onclick="alert('రశీదు వివరాలు: ${e.name} - ${amtStr}')">వివరాలు</button></td>
            </tr>
          `;

          recipHtml += `
            <tr>
              <td><strong>${e.name}</strong></td>
              <td>${e.city}</td>
              <td style="font-weight: 700; color: var(--text-heading);">${amtStr}</td>
              <td style="font-weight: 800; color: var(--emerald-accent);">${recAmt}</td>
              <td><span style="color: var(--emerald-accent); font-size: 12px; font-weight: 700;">సిఫార్సు సిద్ధం</span></td>
            </tr>
          `;
        });

        dashTbody.innerHTML = rowsHtml;
        ledgerTbody.innerHTML = ledgerHtml;
        recipTbody.innerHTML = recipHtml;
      }
    }

    // Initial render
    renderAppViews();
  </script>
</body>
</html>
'''

# Write to web_preview/index.html, desktop.html, mobile.html, build/web/index.html, web/index.html
with open('web_preview/index.html', 'w', encoding='utf-8') as f:
    f.write(NYOTA_INSPIRED_APP)

with open('web_preview/desktop.html', 'w', encoding='utf-8') as f:
    f.write(NYOTA_INSPIRED_APP)

with open('web_preview/mobile.html', 'w', encoding='utf-8') as f:
    f.write(NYOTA_INSPIRED_APP)

with open('build/web/index.html', 'w', encoding='utf-8') as f:
    f.write(NYOTA_INSPIRED_APP)

with open('web/index.html', 'w', encoding='utf-8') as f:
    f.write(NYOTA_INSPIRED_APP)

print('Generated Nyota-grade, NO-GOLD, pristine heritage application across all targets!')
