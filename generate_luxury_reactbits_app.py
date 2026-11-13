# -*- coding: utf-8 -*-
"""
GiftVault Luxury Edition - ReactBits + Aura + Godly Design System
Generates the world-class celebration ledger with micro-interactions, spotlight cards,
shimmer buttons, animated border beams, fluid tabs, and dynamic event schemas.
"""
import os
import shutil

OUTPUT_PREVIEW = r"c:\Project\Gift Valut\web_preview\index.html"
OUTPUT_WEB = r"c:\Project\Gift Valut\web\index.html"
ARTIFACT_PREVIEW = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\giftvault_interactive_preview.html"

HTML_CONTENT = """<!DOCTYPE html>
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
    /* ============================================================
       REACTBITS & AURA DESIGN TOKENS
       ============================================================ */
    :root {
      --bg-dark: #08090D;
      --bg-surface: #0E121B;
      --bg-card: rgba(14, 18, 27, 0.75);
      --bg-glass: rgba(22, 27, 38, 0.65);
      
      --gold-primary: #E5B869;
      --gold-light: #FFDF88;
      --gold-dark: #C89B48;
      --gold-glow: rgba(229, 184, 105, 0.25);
      
      --ruby-red: #E11D48;
      --ruby-dark: #9F1239;
      --ruby-glow: rgba(225, 29, 72, 0.2);
      
      --emerald-green: #10B981;
      --emerald-glow: rgba(16, 185, 129, 0.2);
      
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --text-dim: #64748B;
      
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-glow: rgba(229, 184, 105, 0.35);
      
      --font-display: 'Clash Display', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-numbers: 'Cabinet Grotesk', -apple-system, sans-serif;
      --font-body: 'Plus Jakarta Sans', 'Noto Sans Telugu', sans-serif;
      --font-editorial: 'Instrument Serif', Georgia, serif;
      
      --ease-spring: cubic-bezier(0.16, 1, 0.3, 1);
      --ease-snappy: cubic-bezier(0.23, 1, 0.32, 1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-body);
      min-height: 100vh;
      overflow-x: hidden;
      line-height: 1.5;
    }

    /* Subtle Film Grain Noise Texture */
    body::before {
      content: '';
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.035'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 9999;
    }

    /* Ambient Aura Glow Orbs */
    .ambient-aurora {
      position: fixed;
      width: 100vw;
      height: 100vh;
      top: 0;
      left: 0;
      overflow: hidden;
      pointer-events: none;
      z-index: 0;
    }
    .aurora-orb-1 {
      position: absolute;
      top: -150px;
      left: 15%;
      width: 650px;
      height: 650px;
      background: radial-gradient(circle, rgba(229, 184, 105, 0.12) 0%, rgba(200, 155, 72, 0) 70%);
      filter: blur(80px);
      animation: float-orb-1 18s ease-in-out infinite alternate;
    }
    .aurora-orb-2 {
      position: absolute;
      top: 300px;
      right: -100px;
      width: 550px;
      height: 550px;
      background: radial-gradient(circle, rgba(225, 29, 72, 0.09) 0%, rgba(159, 18, 57, 0) 70%);
      filter: blur(90px);
      animation: float-orb-2 22s ease-in-out infinite alternate;
    }
    .aurora-orb-3 {
      position: absolute;
      bottom: -150px;
      left: 30%;
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, rgba(16, 185, 129, 0.08) 0%, rgba(5, 150, 105, 0) 70%);
      filter: blur(85px);
      animation: float-orb-1 25s ease-in-out infinite alternate;
    }
    @keyframes float-orb-1 {
      0% { transform: translate(0, 0) scale(1); }
      100% { transform: translate(50px, 80px) scale(1.1); }
    }
    @keyframes float-orb-2 {
      0% { transform: translate(0, 0) scale(1); }
      100% { transform: translate(-60px, -50px) scale(0.95); }
    }

    /* App Shell Container */
    .app-shell {
      position: relative;
      z-index: 1;
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 24px 60px 24px;
    }

    /* ============================================================
       TOP LUXURY NAVIGATION
       ============================================================ */
    .nav-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 20px 0;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 32px;
      position: sticky;
      top: 0;
      background: rgba(8, 9, 13, 0.85);
      backdrop-filter: blur(20px);
      z-index: 100;
    }

    .brand-lockup {
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
      color: inherit;
      cursor: pointer;
    }
    .brand-logo-gem {
      width: 44px;
      height: 44px;
      border-radius: 14px;
      background: linear-gradient(135deg, #1C2333 0%, #0F131D 100%);
      border: 1px solid rgba(229, 184, 105, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.15);
      transition: all 0.3s var(--ease-spring);
    }
    .brand-lockup:hover .brand-logo-gem {
      transform: translateY(-2px) scale(1.05);
      border-color: var(--gold-light);
      box-shadow: 0 8px 25px var(--gold-glow);
    }
    .brand-titles {
      display: flex;
      flex-direction: column;
    }
    .brand-name {
      font-family: var(--font-display);
      font-size: 20px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .brand-name span.vault-gold {
      background: linear-gradient(135deg, #FFDF88 0%, #E5B869 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .brand-tag {
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--text-muted);
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    /* ReactBits Style Pill Switcher */
    .view-switcher-pill {
      display: flex;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      border-radius: 100px;
      padding: 4px;
      position: relative;
    }
    .view-btn {
      padding: 6px 14px;
      border-radius: 100px;
      border: none;
      background: transparent;
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.25s var(--ease-snappy);
    }
    .view-btn.active {
      background: var(--gold-primary);
      color: #0A0D14;
      box-shadow: 0 2px 10px rgba(229, 184, 105, 0.3);
    }

    /* Language Dropdown */
    .lang-select-wrap {
      position: relative;
    }
    .lang-select {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      font-size: 13px;
      font-weight: 600;
      padding: 8px 14px;
      border-radius: 12px;
      cursor: pointer;
      outline: none;
      transition: all 0.2s ease;
      font-family: inherit;
    }
    .lang-select:hover, .lang-select:focus {
      border-color: var(--gold-primary);
      box-shadow: 0 0 15px rgba(229, 184, 105, 0.15);
    }

    /* ============================================================
       REACTBITS SIGNATURE BUTTONS & ANIMATIONS
       ============================================================ */
    /* Shimmer Button */
    .btn-shimmer {
      position: relative;
      overflow: hidden;
      background: linear-gradient(135deg, #E5B869 0%, #C89B48 100%);
      color: #08090D;
      font-family: var(--font-body);
      font-weight: 700;
      font-size: 14px;
      border-radius: 12px;
      padding: 10px 22px;
      border: 1px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 4px 20px rgba(229, 184, 105, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.4);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.25s var(--ease-spring);
    }
    .btn-shimmer::before {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: linear-gradient(
        60deg,
        transparent 20%,
        rgba(255, 255, 255, 0.6) 50%,
        transparent 80%
      );
      transform: translateX(-100%);
      animation: shimmer-sweep 4s infinite ease-in-out;
      pointer-events: none;
    }
    @keyframes shimmer-sweep {
      0% { transform: translateX(-100%) rotate(25deg); }
      30%, 100% { transform: translateX(100%) rotate(25deg); }
    }
    .btn-shimmer:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 8px 30px rgba(229, 184, 105, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.6);
    }
    .btn-shimmer:active {
      transform: translateY(1px) scale(0.97);
    }

    /* Glass Glowing Button */
    .btn-glass {
      position: relative;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--border-subtle);
      backdrop-filter: blur(14px);
      color: var(--text-main);
      font-family: var(--font-body);
      font-size: 14px;
      font-weight: 600;
      border-radius: 12px;
      padding: 10px 20px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s var(--ease-spring);
    }
    .btn-glass:hover {
      background: rgba(255, 255, 255, 0.09);
      border-color: rgba(229, 184, 105, 0.4);
      color: var(--gold-light);
      transform: translateY(-1px);
      box-shadow: 0 0 15px rgba(229, 184, 105, 0.15);
    }
    .btn-glass:active {
      transform: scale(0.97);
    }

    /* ============================================================
       REACTBITS SPOTLIGHT CARD SYSTEM
       ============================================================ */
    .spotlight-card {
      position: relative;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 20px;
      padding: 24px;
      overflow: hidden;
      backdrop-filter: blur(24px);
      transition: transform 0.25s var(--ease-spring), border-color 0.25s ease, box-shadow 0.25s ease;
    }
    .spotlight-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(600px circle at var(--mouse-x, -500px) var(--mouse-y, -500px), rgba(229, 184, 105, 0.15), transparent 60%);
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.3s ease;
      z-index: 1;
    }
    .spotlight-card:hover::before {
      opacity: 1;
    }
    .spotlight-card:hover {
      transform: translateY(-3px);
      border-color: rgba(229, 184, 105, 0.35);
      box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.6), 0 0 25px rgba(229, 184, 105, 0.08);
    }
    .spotlight-content {
      position: relative;
      z-index: 2;
    }

    /* Animated Border Beam */
    .border-beam-highlight {
      position: relative;
      border-radius: 20px;
      overflow: hidden;
    }
    .border-beam-highlight::after {
      content: '';
      position: absolute;
      inset: -1.5px;
      border-radius: inherit;
      padding: 2px;
      background: conic-gradient(from var(--beam-angle, 0deg) at 50% 50%, transparent 0deg, transparent 70deg, #E5B869 130deg, #FFDF88 180deg, transparent 240deg, transparent 360deg);
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      pointer-events: none;
      animation: beam-spin 5s linear infinite;
    }
    @property --beam-angle {
      syntax: '<angle>';
      initial-value: 0deg;
      inherits: false;
    }
    @keyframes beam-spin {
      to { --beam-angle: 360deg; }
    }

    /* ============================================================
       HERO SHOWCASE SECTION (Awwwards / Godly Quality)
       ============================================================ */
    .hero-section {
      padding: 30px 0 45px 0;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 40px;
      align-items: center;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 36px;
    }
    @media (max-width: 1024px) {
      .hero-section {
        grid-template-columns: 1fr;
      }
    }

    .hero-badge-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(229, 184, 105, 0.1);
      border: 1px solid rgba(229, 184, 105, 0.25);
      border-radius: 100px;
      padding: 6px 14px;
      font-size: 12px;
      font-weight: 700;
      color: var(--gold-light);
      margin-bottom: 18px;
    }
    .hero-badge-pill span.live-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #10B981;
      box-shadow: 0 0 10px #10B981;
      animation: pulse-dot 1.8s infinite;
    }
    @keyframes pulse-dot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.5; transform: scale(1.2); }
    }

    .hero-title {
      font-family: var(--font-display);
      font-size: 46px;
      line-height: 1.15;
      font-weight: 700;
      letter-spacing: -0.03em;
      margin-bottom: 18px;
      color: var(--text-main);
    }
    .hero-title em {
      font-family: var(--font-editorial);
      font-style: italic;
      font-weight: 400;
      background: linear-gradient(135deg, #FFDF88 0%, #E5B869 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      padding-right: 4px;
    }
    .hero-subtitle {
      font-size: 16px;
      color: var(--text-muted);
      max-width: 580px;
      margin-bottom: 28px;
      line-height: 1.6;
    }

    /* Event Mode Dynamic Selector */
    .event-type-tabs {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 28px;
      padding: 6px;
      background: rgba(255, 255, 255, 0.03);
      border-radius: 14px;
      border: 1px solid var(--border-subtle);
      width: fit-content;
    }
    .event-tab {
      padding: 8px 16px;
      border-radius: 10px;
      border: 1px solid transparent;
      background: transparent;
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s var(--ease-spring);
    }
    .event-tab.active {
      background: rgba(229, 184, 105, 0.15);
      border-color: rgba(229, 184, 105, 0.4);
      color: var(--gold-light);
      box-shadow: 0 4px 15px rgba(229, 184, 105, 0.1);
    }

    /* Hero Live Summary Card */
    .hero-preview-card {
      background: linear-gradient(135deg, rgba(22, 27, 38, 0.9) 0%, rgba(14, 18, 27, 0.95) 100%);
      border: 1px solid rgba(229, 184, 105, 0.25);
      border-radius: 24px;
      padding: 28px;
      box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.7), 0 0 30px rgba(229, 184, 105, 0.06);
      position: relative;
    }
    .preview-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-subtle);
    }
    .preview-event-badge {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .event-icon-circle {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: rgba(229, 184, 105, 0.15);
      color: var(--gold-light);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
    }

    /* Metric Grid */
    .preview-metrics {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin-bottom: 20px;
    }
    .mini-metric-box {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 14px;
      transition: border-color 0.2s ease;
    }
    .mini-metric-box:hover {
      border-color: rgba(229, 184, 105, 0.3);
    }
    .mini-label {
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
      margin-bottom: 4px;
    }
    .mini-value {
      font-family: var(--font-numbers);
      font-size: 22px;
      font-weight: 800;
      color: var(--text-main);
      letter-spacing: -0.02em;
    }
    .mini-value.gold {
      color: var(--gold-light);
    }
    .mini-value.green {
      color: var(--emerald-green);
    }

    /* ============================================================
       APPLICATION SUBTABS NAVIGATION (Framer Motion Fluid Pill)
       ============================================================ */
    .subtabs-nav-wrapper {
      position: relative;
      margin-bottom: 30px;
    }
    .subtabs-nav {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding: 6px;
      background: rgba(14, 18, 27, 0.8);
      border: 1px solid var(--border-subtle);
      border-radius: 16px;
      backdrop-filter: blur(16px);
      scrollbar-width: none;
    }
    .subtabs-nav::-webkit-scrollbar {
      display: none;
    }
    .subtab-btn {
      padding: 10px 18px;
      border-radius: 12px;
      border: none;
      background: transparent;
      color: var(--text-muted);
      font-family: var(--font-body);
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      transition: all 0.25s var(--ease-spring);
    }
    .subtab-btn:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.04);
    }
    .subtab-btn.active {
      background: linear-gradient(135deg, rgba(229, 184, 105, 0.2) 0%, rgba(200, 155, 72, 0.1) 100%);
      color: var(--gold-light);
      border: 1px solid rgba(229, 184, 105, 0.35);
      box-shadow: 0 4px 15px rgba(229, 184, 105, 0.15);
    }

    /* ============================================================
       VIEW CONTAINER (Desktop vs Mobile Chassis)
       ============================================================ */
    .main-workspace-view {
      position: relative;
      width: 100%;
    }

    /* Mobile Phone Chassis Frame */
    .mobile-chassis-wrapper {
      display: none;
      justify-content: center;
      padding: 20px 0;
    }
    .mobile-phone-frame {
      width: 390px;
      height: 844px;
      background: #090A10;
      border-radius: 50px;
      border: 10px solid #232734;
      box-shadow: 0 25px 80px rgba(0, 0, 0, 0.8), 0 0 0 2px rgba(255, 255, 255, 0.1), inset 0 0 10px rgba(0, 0, 0, 0.8);
      overflow: hidden;
      position: relative;
      display: flex;
      flex-direction: column;
    }
    .dynamic-island {
      width: 120px;
      height: 30px;
      background: #000;
      border-radius: 20px;
      position: absolute;
      top: 10px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 1000;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 10px;
    }
    .camera-lens {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #111422;
      border: 1px solid #2a3147;
    }
    .mobile-screen-scroll {
      flex: 1;
      overflow-y: auto;
      padding: 55px 16px 80px 16px;
      scrollbar-width: thin;
      scrollbar-color: rgba(229, 184, 105, 0.3) transparent;
    }

    /* Subtab Content Panes */
    .subtab-pane {
      display: none;
      animation: fadeInPane 0.35s var(--ease-spring) forwards;
    }
    .subtab-pane.active {
      display: block;
    }
    @keyframes fadeInPane {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ============================================================
       SUBTAB 1: DASHBOARD
       ============================================================ */
    .dashboard-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-bottom: 28px;
    }
    @media (max-width: 1100px) {
      .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 640px) {
      .dashboard-grid { grid-template-columns: 1fr; }
    }

    .kpi-title {
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }
    .kpi-value {
      font-family: var(--font-numbers);
      font-size: 32px;
      font-weight: 800;
      letter-spacing: -0.03em;
      margin-bottom: 8px;
      color: var(--text-main);
    }
    .kpi-trend {
      font-size: 12px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .kpi-trend.positive { color: var(--emerald-green); }
    .kpi-trend.negative { color: var(--ruby-red); }

    /* ============================================================
       SUBTAB 2: MUNSHI FAST ENTRY DESK
       ============================================================ */
    .munshi-layout {
      display: grid;
      grid-template-columns: 1.25fr 0.75fr;
      gap: 24px;
    }
    @media (max-width: 900px) {
      .munshi-layout { grid-template-columns: 1fr; }
    }

    .form-group {
      margin-bottom: 18px;
    }
    .form-label {
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 6px;
    }
    .form-input {
      width: 100%;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 12px 16px;
      color: var(--text-main);
      font-family: inherit;
      font-size: 14px;
      outline: none;
      transition: all 0.2s ease;
    }
    .form-input:focus {
      border-color: var(--gold-primary);
      box-shadow: 0 0 15px rgba(229, 184, 105, 0.2);
      background: rgba(255, 255, 255, 0.06);
    }

    /* Gift Type Switcher */
    .gift-type-chips {
      display: flex;
      gap: 8px;
      margin-top: 6px;
    }
    .gift-chip {
      flex: 1;
      padding: 10px 8px;
      border-radius: 10px;
      border: 1px solid var(--border-subtle);
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      text-align: center;
      transition: all 0.2s ease;
    }
    .gift-chip.active {
      background: rgba(229, 184, 105, 0.15);
      border-color: var(--gold-primary);
      color: var(--gold-light);
    }

    /* +₹1 Lucky Coin Toggle */
    .lucky-coin-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      background: rgba(229, 184, 105, 0.08);
      border: 1px solid rgba(229, 184, 105, 0.25);
      border-radius: 12px;
      margin-bottom: 20px;
    }

    /* ============================================================
       SUBTAB 3: RED BOOK (ERRA PUSTHAKAM) LEDGER
       ============================================================ */
    .ledger-book-container {
      background: #18090C;
      border: 2px solid #5C1D24;
      border-radius: 20px;
      padding: 30px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.8), inset 0 0 20px rgba(225, 29, 72, 0.1);
      position: relative;
    }
    .ledger-corner-bracket {
      position: absolute;
      width: 24px;
      height: 24px;
      border-color: var(--gold-primary);
      border-style: solid;
      pointer-events: none;
    }
    .ledger-corner-tl { top: 12px; left: 12px; border-width: 2px 0 0 2px; }
    .ledger-corner-tr { top: 12px; right: 12px; border-width: 2px 2px 0 0; }
    .ledger-corner-bl { bottom: 12px; left: 12px; border-width: 0 0 2px 2px; }
    .ledger-corner-br { bottom: 12px; right: 12px; border-width: 0 2px 2px 0; }

    .luxury-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 14px;
    }
    .luxury-table th {
      text-align: left;
      padding: 14px 16px;
      color: var(--gold-light);
      font-weight: 700;
      border-bottom: 1px solid rgba(229, 184, 105, 0.25);
      font-family: var(--font-display);
      letter-spacing: 0.03em;
    }
    .luxury-table td {
      padding: 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      color: var(--text-main);
    }
    .luxury-table tr:hover td {
      background: rgba(229, 184, 105, 0.05);
    }

    /* Soundbox QR Visualizer */
    .qr-chime-box {
      text-align: center;
      padding: 32px 20px;
    }
    .audio-waves {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
      height: 36px;
      margin: 20px auto;
    }
    .audio-bar {
      width: 5px;
      background: var(--gold-primary);
      border-radius: 10px;
      animation: sound-bounce 1s infinite ease-in-out;
    }
    .audio-bar:nth-child(1) { height: 12px; animation-delay: 0.1s; }
    .audio-bar:nth-child(2) { height: 26px; animation-delay: 0.2s; }
    .audio-bar:nth-child(3) { height: 36px; animation-delay: 0.3s; }
    .audio-bar:nth-child(4) { height: 18px; animation-delay: 0.4s; }
    .audio-bar:nth-child(5) { height: 30px; animation-delay: 0.15s; }
    @keyframes sound-bounce {
      0%, 100% { transform: scaleY(0.4); }
      50% { transform: scaleY(1); }
    }
  </style>
</head>
<body>

  <!-- Ambient Luxury Aurora Orbs -->
  <div class="ambient-aurora">
    <div class="aurora-orb-1"></div>
    <div class="aurora-orb-2"></div>
    <div class="aurora-orb-3"></div>
  </div>

  <div class="app-shell">

    <!-- TOP LUXURY NAVIGATION -->
    <nav class="nav-bar">
      <a class="brand-lockup" href="#dashboard">
        <div class="brand-logo-gem">
          <!-- Clean Geometric Vault Monogram SVG -->
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2L3 7V17L12 22L21 17V7L12 2Z" stroke="#E5B869" stroke-width="1.8" stroke-linejoin="round"/>
            <circle cx="12" cy="12" r="3.5" stroke="#FFDF88" stroke-width="1.6"/>
            <path d="M12 8.5V7M12 17V15.5M8.5 12H7M17 12H15.5" stroke="#E5B869" stroke-width="1.6" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="brand-titles">
          <div class="brand-name">GIFT<span class="vault-gold">VAULT</span></div>
          <div class="brand-tag" id="tag-phrase">గిఫ్ట్ వాలెట్ • ROYAL SHAGUN TREASURY</div>
        </div>
      </a>

      <div class="nav-actions">
        <!-- Viewport Switcher Pill -->
        <div class="view-switcher-pill">
          <button class="view-btn active" id="btn-view-desktop" onclick="switchViewport('desktop')">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
            Desktop
          </button>
          <button class="view-btn" id="btn-view-mobile" onclick="switchViewport('mobile')">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="3"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
            Mobile App
          </button>
        </div>

        <!-- Language Selector -->
        <div class="lang-select-wrap">
          <select class="lang-select" id="lang-selector" onchange="changeLanguage(this.value)">
            <option value="te" selected>తెలుగు (Telugu)</option>
            <option value="en">English (Global)</option>
            <option value="hi">हिंदी (Hindi)</option>
            <option value="ta">தமிழ் (Tamil)</option>
            <option value="kn">ಕನ್ನಡ (Kannada)</option>
          </select>
        </div>

        <!-- Shimmer Button Action -->
        <button class="btn-shimmer" onclick="switchSubtab('desk')">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 5v14M5 12h14"/></svg>
          <span id="txt-nav-add">+ కొత్త ఎంట్రీ (Add Shagun)</span>
        </button>
      </div>
    </nav>

    <!-- HERO SECTION (Awwwards / ReactBits Spotlight Tier) -->
    <header class="hero-section">
      <div>
        <div class="hero-badge-pill">
          <span class="live-dot"></span>
          <span id="txt-hero-pill">భారతదేశపు నంబర్ 1 రాయల్ శుభకార్య ఖజానా • 2026 EDITION</span>
        </div>
        <h1 class="hero-title" id="txt-hero-title">
          Where Royal Celebrations Meet <em>Luxury Fintech</em>.
        </h1>
        <p class="hero-subtitle" id="txt-hero-sub">
          పెళ్ళిళ్లు, గృహప్రవేశాలు, పుట్టినరోజులు మరియు వేడుకల కానుకల లెక్కలు, ఎర్ర పుస్తకం (శగున్ డైరీ), మరియు ఖర్చుల నికర లాభాలను అత్యంత సులభంగా నిర్వహించండి.
        </p>

        <!-- Dynamic Event Type Switcher -->
        <div class="event-type-tabs" id="event-type-pills">
          <button class="event-tab active" onclick="setEventMode('wedding', this)">
            💍 పెళ్లి (Wedding)
          </button>
          <button class="event-tab" onclick="setEventMode('birthday', this)">
            👶 బర్త్‌డే / ఉయ్యాల (Birthday)
          </button>
          <button class="event-tab" onclick="setEventMode('halfsaree', this)">
            🪷 హాఫ్ శారీ / వోణి (Half Saree)
          </button>
          <button class="event-tab" onclick="setEventMode('dhoti', this)">
            🧵 ధోతీ / ఉపనయనం (Upanayanam)
          </button>
          <button class="event-tab" onclick="setEventMode('housewarming', this)">
            🏡 గృహప్రవేశం (Housewarming)
          </button>
        </div>

        <div style="display: flex; gap: 14px; align-items: center;">
          <button class="btn-shimmer" onclick="switchSubtab('desk')">
            ⚡ మున్షీ డెస్క్ తెరవండి (Open Munshi)
          </button>
          <button class="btn-glass" onclick="switchSubtab('ledger')">
            📜 ఎర్ర పుస్తకం (View Red Ledger)
          </button>
        </div>
      </div>

      <!-- Live Hero Spotlight Preview Card -->
      <div class="hero-preview-card spotlight-card border-beam-highlight">
        <div class="spotlight-content">
          <div class="preview-header">
            <div class="preview-event-badge">
              <div class="event-icon-circle" id="hero-event-icon">💍</div>
              <div>
                <div style="font-weight: 700; font-size: 17px;" id="hero-event-name">రాహుల్ & స్నిగ్ధ వివాహ వేడుక</div>
                <div style="font-size: 12px; color: var(--gold-light);" id="hero-event-detail">వధూవరులు • రాయదుర్గం, హైదరాబాద్</div>
              </div>
            </div>
            <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16,185,129,0.3); color: #10B981; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 100px;">
              ● ప్రత్యక్షం (Live)
            </div>
          </div>

          <div class="preview-metrics">
            <div class="mini-metric-box">
              <div class="mini-label">మొత్తం కానుకలు (Inflow)</div>
              <div class="mini-value gold" id="hero-val-inflow">₹8,42,101</div>
            </div>
            <div class="mini-metric-box">
              <div class="mini-label">మొత్తం ఖర్చులు (Expenses)</div>
              <div class="mini-value" style="color: var(--ruby-red);" id="hero-val-expenses">₹4,15,000</div>
            </div>
            <div class="mini-metric-box">
              <div class="mini-label">నికర మిగులు (Net Surplus)</div>
              <div class="mini-value green" id="hero-val-surplus">+₹4,27,101</div>
            </div>
            <div class="mini-metric-box">
              <div class="mini-label">బంగారం & వెండి (Precious)</div>
              <div class="mini-value" id="hero-val-gold">42.5g / 550g</div>
            </div>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: var(--text-muted); border-top: 1px solid var(--border-subtle); padding-top: 14px;">
            <span>ఆఖరి ఎంట్రీ: వెంకట్ రావు గారు (విజయవాడ)</span>
            <span style="font-weight: 700; color: var(--gold-light);">₹10,116 (Cash + 1g Gold)</span>
          </div>
        </div>
      </div>
    </header>

    <!-- SUBTABS NAVIGATION (7 Complete Modules) -->
    <div class="subtabs-nav-wrapper">
      <div class="subtabs-nav" id="subtabs-bar">
        <button class="subtab-btn active" data-tab="dashboard" onclick="switchSubtab('dashboard')">
          📊 డాష్‌బోర్డ్ (Dashboard)
        </button>
        <button class="subtab-btn" data-tab="desk" onclick="switchSubtab('desk')">
          ⚡ మున్షీ డెస్క్ (Munshi Entry)
        </button>
        <button class="subtab-btn" data-tab="ledger" onclick="switchSubtab('ledger')">
          📜 ఎర్ర పుస్తకం (Red Ledger)
        </button>
        <button class="subtab-btn" data-tab="expenses" onclick="switchSubtab('expenses')">
          💸 ఈవెంట్ ఖర్చులు (Expenses)
        </button>
        <button class="subtab-btn" data-tab="reciprocity" onclick="switchSubtab('reciprocity')">
          🔄 పరస్పర లెక్కలు (Reciprocity)
        </button>
        <button class="subtab-btn" data-tab="invites" onclick="switchSubtab('invites')">
          💌 ఆహ్వానాలు & RSVP (Invites)
        </button>
        <button class="subtab-btn" data-tab="qr" onclick="switchSubtab('qr')">
          🔊 సౌండ్‌బాక్స్ & QR (UPI Audio)
        </button>
      </div>
    </div>

    <!-- MAIN WORKSPACE -->
    <main class="main-workspace-view">

      <!-- ==========================================
           DESKTOP VIEW CONTAINER
           ========================================== -->
      <div id="desktop-view-container">

        <!-- 1. DASHBOARD PANE -->
        <section class="subtab-pane active" id="pane-dashboard">
          <div class="dashboard-grid">
            <div class="spotlight-card">
              <div class="spotlight-content">
                <div class="kpi-title">
                  <span>మొత్తం కానుకలు (Total Inflow)</span>
                  <span style="font-size: 18px;">💰</span>
                </div>
                <div class="kpi-value" style="color: var(--gold-light);">₹8,42,101</div>
                <div class="kpi-trend positive">
                  <span>↑ +18.4%</span> <span>గత ఈవెంట్ కంటే ఎక్కువ</span>
                </div>
              </div>
            </div>

            <div class="spotlight-card">
              <div class="spotlight-content">
                <div class="kpi-title">
                  <span>ఫంక్షన్ ఖర్చులు (Total Expenses)</span>
                  <span style="font-size: 18px;">💸</span>
                </div>
                <div class="kpi-value" style="color: var(--ruby-red);">₹4,15,000</div>
                <div class="kpi-trend negative">
                  <span>● 8 కేటగిరీలు</span> <span>క్యాటరింగ్, కల్యాణ మండపం</span>
                </div>
              </div>
            </div>

            <div class="spotlight-card border-beam-highlight">
              <div class="spotlight-content">
                <div class="kpi-title">
                  <span>నికర నిల్వ (Net Surplus Balance)</span>
                  <span style="font-size: 18px;">💎</span>
                </div>
                <div class="kpi-value" style="color: var(--emerald-green);">+₹4,27,101</div>
                <div class="kpi-trend positive">
                  <span>✓ లాభంలో ఉంది</span> <span>ఖర్చులు పోనూ మిగులు</span>
                </div>
              </div>
            </div>

            <div class="spotlight-card">
              <div class="spotlight-content">
                <div class="kpi-title">
                  <span>బంగారం & వెండి (Precious Metals)</span>
                  <span style="font-size: 18px;">👑</span>
                </div>
                <div class="kpi-value">42.5 <span style="font-size: 16px; color: var(--gold-light);">g Gold</span></div>
                <div style="font-size: 13px; color: var(--text-muted); font-weight: 600;">
                  వెండి: 550 గ్రాములు (14 గిఫ్ట్ కప్పులు)
                </div>
              </div>
            </div>
          </div>

          <!-- Quick Recent Table in Dashboard -->
          <div class="spotlight-card" style="padding: 24px;">
            <div class="spotlight-content">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px;">
                <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700;">ఇటీవలి కానుకల ఎంట్రీలు (Recent Gifts Received)</h3>
                <button class="btn-glass" onclick="switchSubtab('ledger')">అన్నీ చూడండి (View All)</button>
              </div>
              <table class="luxury-table">
                <thead>
                  <tr>
                    <th>రశీదు సంఖ్య</th>
                    <th>అతిథి పేరు</th>
                    <th>ఊరు (City)</th>
                    <th>సంబంధం (Relation)</th>
                    <th>కానుక రూపం</th>
                    <th>మొత్తం (Amount)</th>
                    <th>చర్య</th>
                  </tr>
                </thead>
                <tbody id="dashboard-recent-tbody">
                  <!-- Dynamic JS rows inserted -->
                </tbody>
              </table>
            </div>
          </div>
        </section>

        <!-- 2. MUNSHI FAST ENTRY DESK -->
        <section class="subtab-pane" id="pane-desk">
          <div class="munshi-layout">
            <div class="spotlight-card" style="padding: 28px;">
              <div class="spotlight-content">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 22px;">
                  <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700;">
                    ⚡ మున్షీ వేగవంతమైన ఎంట్రీ (Munshi Fast Entry Desk)
                  </h2>
                  <span style="background: rgba(229,184,105,0.15); color: var(--gold-light); font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 6px;">
                    AUTO-RECEIPT ON
                  </span>
                </div>

                <form id="munshi-entry-form" onsubmit="handleMunshiSubmit(event)">
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div class="form-group">
                      <label class="form-label">అతిథి పేరు (Guest Full Name) *</label>
                      <input type="text" class="form-input" id="munshi-guest-name" placeholder="ఉదా: కొత్తపల్లి రాజశేఖర్ గారు" required>
                    </div>
                    <div class="form-group">
                      <label class="form-label">ఊరు / నగరం (AP & TG Smart Autocomplete) *</label>
                      <input type="text" class="form-input" id="munshi-city" list="telugu-cities" placeholder="విజయవాడ, హైదరాబాద్..." required>
                      <datalist id="telugu-cities">
                        <option value="హైదరాబాద్ (Hyderabad)">
                        <option value="విజయవాడ (Vijayawada)">
                        <option value="విశాఖపట్నం (Visakhapatnam)">
                        <option value="గుంటూరు (Guntur)">
                        <option value="వరంగల్ (Warangal)">
                        <option value="రాజమండ్రి (Rajahmundry)">
                        <option value="తిరుపతి (Tirupati)">
                        <option value="నెల్లూరు (Nellore)">
                        <option value="కర్నూలు (Kurnool)">
                        <option value="కరీంనగర్ (Karimnagar)">
                        <option value="ఖమ్మం (Khammam)">
                        <option value="కాకినాడ (Kakinada)">
                      </datalist>
                    </div>
                  </div>

                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                    <div class="form-group">
                      <label class="form-label">సంబంధం / తరపు (Side / Relation)</label>
                      <select class="form-input" id="munshi-side">
                        <option value="పెళ్ళికూతురు తరపు (Bride Side)">పెళ్ళికూతురు తరపు (Bride Side)</option>
                        <option value="పెళ్ళికొడుకు తరపు (Groom Side)">పెళ్ళికొడుకు తరపు (Groom Side)</option>
                        <option value="స్నేహితులు (Friends)">స్నేహితులు (Friends)</option>
                        <option value="సహోద్యోగులు (Colleagues)">సహోద్యోగులు (Colleagues)</option>
                        <option value="బంధువులు (Relatives)">బంధువులు (Relatives)</option>
                      </select>
                    </div>
                    <div class="form-group">
                      <label class="form-label">మొబైల్ సంఖ్య (WhatsApp రశీదు కోసం)</label>
                      <input type="tel" class="form-input" id="munshi-phone" placeholder="98480xxxxx">
                    </div>
                  </div>

                  <!-- Gift Type Selection -->
                  <div class="form-group">
                    <label class="form-label">కానుక రూపం (Gift Category)</label>
                    <div class="gift-type-chips">
                      <div class="gift-chip active" onclick="setGiftType('cash', this)">💵 నగదు (Cash)</div>
                      <div class="gift-chip" onclick="setGiftType('gold', this)">👑 బంగారం (Gold)</div>
                      <div class="gift-chip" onclick="setGiftType('silver', this)">🪙 వెండి (Silver)</div>
                      <div class="gift-chip" onclick="setGiftType('item', this)">🎁 వస్తువు (Item)</div>
                    </div>
                  </div>

                  <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 16px;">
                    <div class="form-group">
                      <label class="form-label">మొత్తం నగదు / విలువ (Amount ₹) *</label>
                      <input type="number" class="form-input" id="munshi-amount" value="5116" required style="font-family: var(--font-numbers); font-size: 20px; font-weight: 700; color: var(--gold-light);">
                    </div>
                    <div class="form-group" id="gram-input-group" style="display: none;">
                      <label class="form-label">బరువు (గ్రాములు) / వస్తువు వివరాలు</label>
                      <input type="text" class="form-input" id="munshi-grams" placeholder="ఉదా: 5.5 గ్రాములు">
                    </div>
                  </div>

                  <!-- Lucky +₹1 coin toggle -->
                  <div class="lucky-coin-row">
                    <div>
                      <div style="font-weight: 700; font-size: 13px;">+₹1 శుభ సూచక నాణెం (+₹1 Lucky Coin)</div>
                      <div style="font-size: 11px; color: var(--text-muted);">సంప్రదాయ 116, 516, 1116, 5116 ఆటో-రౌండింగ్</div>
                    </div>
                    <input type="checkbox" id="munshi-lucky-coin" checked style="width: 20px; height: 20px; accent-color: var(--gold-primary); cursor: pointer;" onchange="toggleLuckyCoin(this.checked)">
                  </div>

                  <button type="submit" class="btn-shimmer" style="width: 100%; justify-content: center; padding: 14px; font-size: 16px;">
                    💾 ఎంట్రీ భద్రపరచండి & వాట్సాప్ రశీదు పంపండి (Save & Send WhatsApp Receipt)
                  </button>
                </form>
              </div>
            </div>

            <!-- Quick Live Soundbox Chime & Receipt Preview -->
            <div class="spotlight-card" style="padding: 24px;">
              <div class="spotlight-content">
                <h3 style="font-family: var(--font-display); font-size: 16px; font-weight: 700; margin-bottom: 14px; color: var(--gold-light);">
                  🔊 ప్రత్యక్ష సౌండ్‌బాక్స్ (Live Audio Chime)
                </h3>
                <div style="background: rgba(0,0,0,0.3); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 16px; text-align: center; margin-bottom: 20px;">
                  <div class="audio-waves">
                    <div class="audio-bar"></div><div class="audio-bar"></div><div class="audio-bar"></div><div class="audio-bar"></div><div class="audio-bar"></div>
                  </div>
                  <button class="btn-glass" onclick="playCelebrationChime()" style="font-size: 12px;">
                    ▶ సౌండ్‌బాక్స్ చైమ్ వినండి (Test Audio Bell)
                  </button>
                </div>

                <h3 style="font-family: var(--font-display); font-size: 16px; font-weight: 700; margin-bottom: 10px;">
                  వాట్సాప్ డిజిటల్ రశీదు నమూనా (Digital Receipt)
                </h3>
                <div id="receipt-preview-card" style="background: #101622; border: 1px dashed rgba(229,184,105,0.4); border-radius: 14px; padding: 16px; font-size: 12px; line-height: 1.7; color: var(--text-muted);">
                  <div style="font-weight: 700; color: var(--gold-light); text-align: center; margin-bottom: 8px;">
                    💍 గిఫ్ట్ వాలెట్ డిజిటల్ శగున్ రశీదు #GV-8492
                  </div>
                  ఆదరణీయ <strong style="color: var(--text-main);" id="rec-name">కొత్తపల్లి రాజశేఖర్ గారు</strong>,<br>
                  రాహుల్ & స్నిగ్ధ వివాహ వేడుకలో మీరు అందించిన అపురూపమైన కానుక 
                  <strong style="color: var(--gold-light);" id="rec-amount">₹5,116</strong> కృతజ్ఞతలతో నమోదైంది.<br>
                  <em>మీ రాక మాకు పరమానందం! — కొత్తపల్లి & దాసరి కుటుంబాలు.</em>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 3. RED BOOK (ERRA PUSTHAKAM) LEDGER -->
        <section class="subtab-pane" id="pane-ledger">
          <div class="ledger-book-container">
            <div class="ledger-corner-bracket ledger-corner-tl"></div>
            <div class="ledger-corner-bracket ledger-corner-tr"></div>
            <div class="ledger-corner-bracket ledger-corner-bl"></div>
            <div class="ledger-corner-bracket ledger-corner-br"></div>

            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; border-bottom: 1px solid rgba(229, 184, 105, 0.3); padding-bottom: 16px;">
              <div>
                <h2 style="font-family: var(--font-display); font-size: 24px; font-weight: 700; color: var(--gold-light);">
                  📜 సాంప్రదాయ ఎర్ర పుస్తకం (Official Erra Pusthakam Ledger)
                </h2>
                <div style="font-size: 13px; color: var(--text-muted);">
                  పవిత్రమైన శ్రీ శుభకార్య కానుకల లెక్కల చిట్టా • అమరావతి & తెలంగాణ గ్రామీణ లెక్కల ఫార్మాట్
                </div>
              </div>
              <div style="display: flex; gap: 10px;">
                <input type="text" id="ledger-search-box" class="form-input" placeholder="🔍 పేరు లేదా ఊరు వెతకండి..." oninput="filterLedger(this.value)" style="width: 240px; padding: 8px 14px; font-size: 12px;">
                <button class="btn-shimmer" onclick="downloadLedgerPDF()" style="font-size: 12px; padding: 8px 16px;">
                  📥 PDF డౌన్‌లోడ్
                </button>
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
                  <th>బంగారం / వెండి</th>
                  <th>సమయం</th>
                </tr>
              </thead>
              <tbody id="full-ledger-tbody">
                <!-- Dynamically populated -->
              </tbody>
            </table>
          </div>
        </section>

        <!-- 4. EVENT EXPENSES & NET BALANCE -->
        <section class="subtab-pane" id="pane-expenses">
          <div class="munshi-layout">
            <div class="spotlight-card" style="padding: 24px;">
              <div class="spotlight-content">
                <h2 style="font-family: var(--font-display); font-size: 20px; font-weight: 700; margin-bottom: 18px;">
                  💸 ఫంక్షన్ ఖర్చు నమోదు (Add Event Expense)
                </h2>
                <form id="expense-add-form" onsubmit="handleExpenseSubmit(event)">
                  <div class="form-group">
                    <label class="form-label">ఖర్చు కేటగిరీ (Expense Category)</label>
                    <select class="form-input" id="exp-category">
                      <option value="క్యాటరింగ్ & భోజనాలు (Catering)">క్యాటరింగ్ & భోజనాలు (Catering)</option>
                      <option value="కల్యాణ మండపం అద్దె (Hall / Venue)">కల్యాణ మండపం అద్దె (Hall / Venue)</option>
                      <option value="ఫోటో & వీడియో గ్రఫీ (Photography)">ఫోటో & వీడియో గ్రఫీ (Photography)</option>
                      <option value="పూల అలంకరణ & డెకరేషన్ (Decoration)">పూల అలంకరణ & డెకరేషన్ (Decoration)</option>
                      <option value="బాజా భజంత్రీలు & మేళం (Music & Band)">బాజా భజంత్రీలు & మేళం (Music & Band)</option>
                      <option value="పురోహితులు & సంభావనలు (Purohit Dakshina)">పురోహితులు & సంభావనలు (Purohit Dakshina)</option>
                      <option value="వాహనాలు & ట్రాన్స్‌పోర్ట్ (Transport)">వాహనాలు & ట్రాన్స్‌పోర్ట్ (Transport)</option>
                      <option value="ఇతర ఖర్చులు (Miscellaneous)">ఇతర ఖర్చులు (Miscellaneous)</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label class="form-label">చెల్లింపు వివరాలు / వెండర్ పేరు</label>
                    <input type="text" class="form-input" id="exp-vendor" placeholder="ఉదా: సుబ్బారావు క్యాటరర్స్" required>
                  </div>
                  <div class="form-group">
                    <label class="form-label">మొత్తం ఖర్చు (Amount ₹) *</label>
                    <input type="number" class="form-input" id="exp-amount" placeholder="50000" required style="font-family: var(--font-numbers); font-size: 18px; font-weight: 700; color: var(--ruby-red);">
                  </div>
                  <button type="submit" class="btn-shimmer" style="width: 100%; justify-content: center;">
                    + ఖర్చు నమోదు చేయండి (Record Expense)
                  </button>
                </form>
              </div>
            </div>

            <!-- Expense Breakdown & Net Surplus -->
            <div class="spotlight-card border-beam-highlight" style="padding: 24px;">
              <div class="spotlight-content">
                <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 16px; color: var(--gold-light);">
                  📊 ఖర్చులు vs కానుకల నికర నిల్వ (Financial Summary)
                </h3>
                <div style="background: rgba(0,0,0,0.3); border-radius: 14px; padding: 18px; margin-bottom: 20px;">
                  <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 14px;">
                    <span>మొత్తం వసూలైన కానుకలు:</span>
                    <strong style="color: var(--gold-light); font-family: var(--font-numbers);">₹8,42,101</strong>
                  </div>
                  <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-size: 14px;">
                    <span>మొత్తం ఈవెంట్ ఖర్చులు:</span>
                    <strong style="color: var(--ruby-red); font-family: var(--font-numbers);">-₹4,15,000</strong>
                  </div>
                  <div style="border-top: 1px solid var(--border-subtle); padding-top: 10px; display: flex; justify-content: space-between; font-size: 16px;">
                    <span style="font-weight: 700;">మిగిలిన నికర లాభం (Net Surplus):</span>
                    <strong style="color: var(--emerald-green); font-family: var(--font-numbers); font-size: 20px;">+₹4,27,101</strong>
                  </div>
                </div>

                <div style="font-weight: 700; font-size: 13px; margin-bottom: 10px;">టాప్ ఖర్చులు:</div>
                <div style="font-size: 13px; line-height: 2;">
                  🍽️ క్యాటరింగ్: ₹2,40,000 (57.8%)<br>
                  🏛️ కల్యాణ మండపం: ₹1,00,000 (24.1%)<br>
                  📸 ఫోటోగ్రఫీ: ₹45,000 (10.8%)<br>
                  🌺 డెకరేషన్ & పూలు: ₹30,000 (7.2%)
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 5. RECIPROCITY TRACKER -->
        <section class="subtab-pane" id="pane-reciprocity">
          <div class="spotlight-card" style="padding: 28px;">
            <div class="spotlight-content">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                <div>
                  <h2 style="font-family: var(--font-display); font-size: 22px; font-weight: 700;">
                    🔄 పరస్పర శగున్ లెక్కింపు (Reciprocity & Return Gift Intelligence)
                  </h2>
                  <div style="font-size: 13px; color: var(--text-muted);">
                    "వారు మన వేడుకకు ఎంత ఇచ్చారు? మనం వారి వేడుకకు ఎంత ఇవ్వాలి?" — ఖచ్చితమైన విశ్లేషణ
                  </div>
                </div>
                <button class="btn-shimmer" onclick="alert('కొత్త పరస్పర రికార్డు జోడించబడింది!')">+ కొత్త రికార్డు</button>
              </div>

              <table class="luxury-table">
                <thead>
                  <tr>
                    <th>కుటుంబం / బంధువు పేరు</th>
                    <th>ఊరు</th>
                    <th>వారిచ్చిన కానుక (Inflow)</th>
                    <th>మనమిచ్చిన కానుక (Outflow)</th>
                    <th>స్థితి (Balance)</th>
                    <th>సిఫార్సు చేసిన రిటర్న్ గిఫ్ట్</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>చల్లా శ్రీనివాసరావు గారు</strong></td>
                    <td>గుంటూరు</td>
                    <td style="color: var(--gold-light); font-weight: 700;">₹5,116</td>
                    <td>₹2,116</td>
                    <td><span style="color: var(--emerald-green); font-weight: 700;">+₹3,000 (మనకు ఎక్కువ)</span></td>
                    <td>వచ్చే వారి అబ్బాయి వివాహానికి ₹5,116 లేదా వెండి పాత్ర సిఫార్సు చేయబడింది.</td>
                  </tr>
                  <tr>
                    <td><strong>బోళ్ల వేణుగోపాల్ గారు</strong></td>
                    <td>వరంగల్</td>
                    <td style="color: var(--gold-light); font-weight: 700;">₹2,116</td>
                    <td>₹5,116</td>
                    <td><span style="color: var(--ruby-red); font-weight: 700;">-₹3,000 (మనం ఎక్కువ ఇచ్చాం)</span></td>
                    <td>సరితూగిన బంధుత్వం. సంప్రదాయ వస్త్ర బహుకరణ సరిపోతుంది.</td>
                  </tr>
                  <tr>
                    <td><strong>రావిపూడి రామకృష్ణ గారు</strong></td>
                    <td>విజయవాడ</td>
                    <td style="color: var(--gold-light); font-weight: 700;">₹10,116 + 2g Gold</td>
                    <td>₹5,116</td>
                    <td><span style="color: var(--emerald-green); font-weight: 700;">+₹5,000 + 2g</span></td>
                    <td>వారి గృహప్రవేశానికి బంగారు నాణెం లేదా ₹10,116 సమర్పించడం మర్యాదపూర్వకం.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </section>

        <!-- 6. INVITES & RSVP -->
        <section class="subtab-pane" id="pane-invites">
          <div class="munshi-layout">
            <div class="spotlight-card" style="padding: 24px;">
              <div class="spotlight-content">
                <h2 style="font-family: var(--font-display); font-size: 20px; font-weight: 700; margin-bottom: 16px;">
                  💌 డిజిటల్ ఆహ్వానాలు & RSVP ట్రాకర్ (Digital Invites)
                </h2>
                <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">
                  అతిథులకు ఒకే క్లిక్‌తో వాట్సాప్ శుభలేఖ కార్డులు పంపండి మరియు వచ్చే వారి సంఖ్యను ట్రాక్ చేయండి.
                </div>
                <div class="form-group">
                  <label class="form-label">అతిథి పేరు</label>
                  <input type="text" class="form-input" placeholder="ఉదా: ఆకెళ్ళ సూర్యనారాయణ గారు">
                </div>
                <div class="form-group">
                  <label class="form-label">వాట్సాప్ నంబర్</label>
                  <input type="tel" class="form-input" placeholder="98480xxxxx">
                </div>
                <div class="form-group">
                  <label class="form-label">ఆహ్వానితుల సంఖ్య (Expected Guests)</label>
                  <input type="number" class="form-input" value="4">
                </div>
                <button class="btn-shimmer" style="width: 100%; justify-content: center;" onclick="alert('వాట్సాప్ ఆహ్వానం విజయవంతంగా షేర్ చేయబడింది!')">
                  📲 వాట్సాప్ ద్వారా శుభలేఖ పంపండి (Send WhatsApp Card)
                </button>
              </div>
            </div>

            <div class="spotlight-card" style="padding: 24px;">
              <div class="spotlight-content">
                <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 16px; color: var(--gold-light);">
                  📊 ఆహ్వానాల స్థితి (RSVP Dashboard)
                </h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 20px;">
                  <div class="mini-metric-box">
                    <div class="mini-label">మొత్తం ఆహ్వానితులు</div>
                    <div class="mini-value">450 మంది</div>
                  </div>
                  <div class="mini-metric-box">
                    <div class="mini-label">ధృవీకరించినవారు (Confirmed)</div>
                    <div class="mini-value green">385 మంది</div>
                  </div>
                  <div class="mini-metric-box">
                    <div class="mini-label">వేచి ఉన్నవారు (Pending)</div>
                    <div class="mini-value gold">65 మంది</div>
                  </div>
                  <div class="mini-metric-box">
                    <div class="mini-label">భోజనాల ఏర్పాట్లు</div>
                    <div class="mini-value">500 ప్లేట్లు</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- 7. SOUNDBOX & DYNAMIC UPI QR -->
        <section class="subtab-pane" id="pane-qr">
          <div class="munshi-layout">
            <div class="spotlight-card border-beam-highlight qr-chime-box">
              <div class="spotlight-content">
                <div style="background: rgba(229,184,105,0.15); color: var(--gold-light); font-size: 11px; font-weight: 700; padding: 4px 12px; border-radius: 100px; display: inline-block; margin-bottom: 14px;">
                  ⚡ INSTANT SOUNDBOX INTEGRATED
                </div>
                <h2 style="font-family: var(--font-display); font-size: 24px; font-weight: 700; margin-bottom: 8px;">
                  డిజిటల్ శగున్ UPI QR కోడ్
                </h2>
                <p style="font-size: 13px; color: var(--text-muted); max-width: 400px; margin: 0 auto 24px auto;">
                  అతిథులు గూగుల్ పే, ఫోన్‌పే లేదా పేటీఎం ద్వారా స్కాన్ చేయగానే వెంటనే వాయిస్ సౌండ్‌బాక్స్ తెలుగులో అనౌన్స్ చేస్తుంది.
                </p>

                <!-- High-res QR Display -->
                <div style="background: #FFF; padding: 18px; border-radius: 20px; width: 220px; height: 220px; margin: 0 auto 20px auto; box-shadow: 0 10px 30px rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center;">
                  <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi://pay?pa=giftvault.shagun@hdfcbank&pn=RahulSnigdhaWedding&am=5116&cu=INR" alt="UPI QR Code" style="width: 100%; height: 100%; border-radius: 8px;">
                </div>

                <div style="font-family: var(--font-numbers); font-size: 26px; font-weight: 800; color: var(--gold-light); margin-bottom: 12px;">
                  ₹5,116 <span style="font-size: 14px; color: var(--text-muted); font-family: var(--font-body);">ఆటో-సెట్</span>
                </div>

                <button class="btn-shimmer" onclick="simulateVoiceSoundbox('5116')" style="font-size: 14px;">
                  🔊 సౌండ్‌బాక్స్ వాయిస్ టెస్ట్ (Play Telugu Announcement)
                </button>
              </div>
            </div>

            <div class="spotlight-card" style="padding: 24px;">
              <div class="spotlight-content">
                <h3 style="font-family: var(--font-display); font-size: 18px; font-weight: 700; margin-bottom: 14px; color: var(--gold-light);">
                  లక్షణాలు & సౌండ్‌బాక్స్ ప్రయోజనాలు:
                </h3>
                <ul style="font-size: 14px; color: var(--text-muted); line-height: 2; padding-left: 20px;">
                  <li><strong>తక్షణ వాయిస్ ధృవీకరణ:</strong> <em>"గిఫ్ట్ వాలెట్ లో ₹5,116 కానుక అందింది"</em> అని స్పీకర్‌లో స్పష్టంగా వినిపిస్తుంది.</li>
                  <li><strong>నగదు రహిత శగున్:</strong> చుట్టాలు చిల్లర వెతుక్కోకుండా క్షణాల్లో చెల్లించవచ్చు.</li>
                  <li><strong>ఆటోమేటిక్ ఎర్ర పుస్తకం సింక్:</strong> QR పేమెంట్ కాగానే మున్షీ డెస్క్ లో ఆటో-ఎంట్రీ నమోదవుతుంది.</li>
                  <li><strong>WhatsApp రశీదు డెలివరీ:</strong> చెల్లించిన అతిథి మొబైల్‌కు క్షణాల్లో కృతజ్ఞతా రశీదు కార్డు చేరుతుంది.</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

      </div>

      <!-- ==========================================
           MOBILE PHONE CHASSIS VIEW CONTAINER
           ========================================== -->
      <div id="mobile-view-container" class="mobile-chassis-wrapper">
        <div class="mobile-phone-frame">
          <!-- Dynamic Island -->
          <div class="dynamic-island">
            <div class="camera-lens"></div>
            <div style="font-size: 10px; color: #FFF; font-weight: 600;">9:41</div>
          </div>

          <!-- Inside Mobile Scrollable View -->
          <div class="mobile-screen-scroll" id="mobile-viewport-content">
            <!-- Mirrored dynamically from desktop view via JS -->
          </div>
        </div>
      </div>

    </main>

  </div>

  <!-- ============================================================
       INTERACTIVE JAVASCRIPT LOGIC
       ============================================================ -->
  <script>
    // In-Memory Celebrations & Ledger Data
    const EVENT_PROFILES = {
      wedding: {
        icon: '💍',
        title: 'రాహుల్ & స్నిగ్ధ వివాహ వేడుక',
        detail: 'వధూవరులు: రాహుల్ (దాసరి) & స్నిగ్ధ (కొత్తపల్లి) • హైదరాబాద్',
        inflow: '₹8,42,101',
        expenses: '₹4,15,000',
        surplus: '+₹4,27,101',
        gold: '42.5g / 550g',
        subtext: 'పెళ్ళికూతురు & పెళ్ళికొడుకు తరపు కానుకల చిట్టా'
      },
      birthday: {
        icon: '👶',
        title: 'చిరంజీవి అన్విత్ ప్రథమ జన్మదిన వేడుక',
        detail: 'బాబు పేరు: అన్విత్ (కుమారుడు) • అమరావతి, విజయవాడ',
        inflow: '₹3,18,501',
        expenses: '₹1,20,000',
        surplus: '+₹1,98,501',
        gold: '18.0g / 220g',
        subtext: 'పుట్టినరోజు & ఉయ్యాల కానుకల పుస్తకం'
      },
      halfsaree: {
        icon: '🪷',
        title: 'కుమారి వైష్ణవి లంగాఓణీ శుభకార్యం',
        detail: 'అమ్మాయి పేరు: వైష్ణవి (శ్రీమతి & శ్రీ వెంకటేశ్వరరావు పుత్రిక)',
        inflow: '₹5,62,116',
        expenses: '₹2,40,000',
        surplus: '+₹3,22,116',
        gold: '28.5g / 380g',
        subtext: 'వోణి వేడుక శగున్ మరియు బహుమతులు'
      },
      dhoti: {
        icon: '🧵',
        title: 'చిరంజీవి సాయి ప్రణవ్ ఉపనయన మహోత్సవం',
        detail: 'అబ్బాయి పేరు: సాయి ప్రణవ్ • కౌశికస గోత్రం • తిరుపతి',
        inflow: '₹4,12,001',
        expenses: '₹1,85,000',
        surplus: '+₹2,27,001',
        gold: '12.0g / 150g',
        subtext: 'ధోతీ & బ్రహ్మోపదేశం కానుకల చిట్టా'
      },
      housewarming: {
        icon: '🏡',
        title: 'శ్రీ నిలయం గృహప్రవేశ మహోత్సవం',
        detail: 'గృహ యజమానులు: రాఘవేంద్ర రావు & సుహాసిని • విశాఖపట్నం',
        inflow: '₹6,88,116',
        expenses: '₹3,10,000',
        surplus: '+₹3,78,116',
        gold: '24.0g / 420g',
        subtext: 'నూతన గృహప్రవేశ కానుకలు & వస్తువులు'
      }
    };

    let LEDGER_DATA = [
      { id: 'GV-101', name: 'కొత్తపల్లి రాజశేఖర్ గారు', city: 'విజయవాడ', side: 'పెళ్ళికూతురు తరపు', type: 'నగదు', amount: 5116, precious: '-', time: '10:45 AM' },
      { id: 'GV-102', name: 'దాసరి సుబ్బారావు గారు', city: 'హైదరాబాద్', side: 'పెళ్ళికొడుకు తరపు', type: 'నగదు + బంగారం', amount: 10116, precious: '2g Gold', time: '11:02 AM' },
      { id: 'GV-103', name: 'యర్రంశెట్టి వెంకటేశ్వర్లు', city: 'గుంటూరు', side: 'స్నేహితులు', type: 'నగదు', amount: 2116, precious: '-', time: '11:18 AM' },
      { id: 'GV-104', name: 'పొట్లూరి నాగమల్లేశ్వరరావు', city: 'విశాఖపట్నం', side: 'బంధువులు', type: 'వెండి పాత్ర', amount: 1116, precious: '150g Silver', time: '11:35 AM' },
      { id: 'GV-105', name: 'చాగంటి శ్రీరామచంద్రమూర్తి', city: 'రాజమండ్రి', side: 'పెళ్ళికూతురు తరపు', type: 'నగదు', amount: 5116, precious: '-', time: '11:50 AM' },
      { id: 'GV-106', name: 'మందపాటి రఘునాథరాజు', city: 'భీమవరం', side: 'స్నేహితులు', type: 'నగదు + బంగారం', amount: 25116, precious: '5g Gold', time: '12:15 PM' }
    ];

    let currentEventKey = 'wedding';
    let currentGiftType = 'cash';

    // Spotlight cursor movement
    document.addEventListener('mousemove', (e) => {
      document.querySelectorAll('.spotlight-card').forEach((card) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
      });
    });

    // Subtab switching
    function switchSubtab(tabName) {
      document.querySelectorAll('.subtab-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-tab') === tabName);
      });
      document.querySelectorAll('.subtab-pane').forEach(pane => {
        pane.classList.toggle('active', pane.id === `pane-${tabName}`);
      });
      syncMobileViewport();
    }

    // Viewport switching (Desktop vs Mobile Chassis)
    function switchViewport(mode) {
      const desktopContainer = document.getElementById('desktop-view-container');
      const mobileContainer = document.getElementById('mobile-view-container');
      const btnDesk = document.getElementById('btn-view-desktop');
      const btnMob = document.getElementById('btn-view-mobile');

      if (mode === 'mobile') {
        desktopContainer.style.display = 'none';
        mobileContainer.style.display = 'flex';
        btnDesk.classList.remove('active');
        btnMob.classList.add('active');
        syncMobileViewport();
      } else {
        desktopContainer.style.display = 'block';
        mobileContainer.style.display = 'none';
        btnMob.classList.remove('active');
        btnDesk.classList.add('active');
      }
    }

    // Sync mobile chassis content
    function syncMobileViewport() {
      const activePane = document.querySelector('.subtab-pane.active');
      const mobileContent = document.getElementById('mobile-viewport-content');
      if (activePane && mobileContent) {
        mobileContent.innerHTML = activePane.innerHTML;
      }
    }

    // Event profile changer
    function setEventMode(key, element) {
      currentEventKey = key;
      document.querySelectorAll('.event-tab').forEach(t => t.classList.remove('active'));
      element.classList.add('active');

      const profile = EVENT_PROFILES[key];
      document.getElementById('hero-event-icon').innerText = profile.icon;
      document.getElementById('hero-event-name').innerText = profile.title;
      document.getElementById('hero-event-detail').innerText = profile.detail;
      document.getElementById('hero-val-inflow').innerText = profile.inflow;
      document.getElementById('hero-val-expenses').innerText = profile.expenses;
      document.getElementById('hero-val-surplus').innerText = profile.surplus;
      document.getElementById('hero-val-gold').innerText = profile.gold;

      playCelebrationChime();
    }

    // Gift Type selector
    function setGiftType(type, elem) {
      currentGiftType = type;
      document.querySelectorAll('.gift-chip').forEach(c => c.classList.remove('active'));
      elem.classList.add('active');

      const gramGroup = document.getElementById('gram-input-group');
      if (type === 'gold' || type === 'silver' || type === 'item') {
        gramGroup.style.display = 'block';
      } else {
        gramGroup.style.display = 'none';
      }
    }

    // +₹1 lucky coin toggle
    function toggleLuckyCoin(checked) {
      const amtInput = document.getElementById('munshi-amount');
      let val = parseInt(amtInput.value) || 0;
      if (checked) {
        if (val % 10 === 0) amtInput.value = val + 1;
        else if (val % 100 === 0) amtInput.value = val + 16;
      } else {
        if (val % 10 === 1) amtInput.value = val - 1;
      }
    }

    // Render Ledger tables
    function renderLedgerTables() {
      const recentTbody = document.getElementById('dashboard-recent-tbody');
      const fullTbody = document.getElementById('full-ledger-tbody');

      if (!recentTbody || !fullTbody) return;

      // Dashboard recent 4
      recentTbody.innerHTML = LEDGER_DATA.slice(0, 4).map(item => `
        <tr>
          <td><span style="font-family: var(--font-numbers); font-weight: 700; color: var(--gold-light);">${item.id}</span></td>
          <td><strong>${item.name}</strong></td>
          <td>${item.city}</td>
          <td><span style="font-size: 11px; background: rgba(255,255,255,0.06); padding: 3px 8px; border-radius: 6px;">${item.side}</span></td>
          <td>${item.type}</td>
          <td style="font-family: var(--font-numbers); font-weight: 700; color: var(--gold-light);">₹${item.amount.toLocaleString('en-IN')}</td>
          <td><button class="btn-glass" style="padding: 4px 10px; font-size: 11px;" onclick="alert('వాట్సాప్ రశీదు పంపబడింది!')">రశీదు</button></td>
        </tr>
      `).join('');

      // Full Ledger
      fullTbody.innerHTML = LEDGER_DATA.map((item, index) => `
        <tr>
          <td>${index + 1}</td>
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

    // Filter Ledger
    function filterLedger(query) {
      const q = query.toLowerCase();
      const filtered = LEDGER_DATA.filter(item => 
        item.name.toLowerCase().includes(q) || item.city.toLowerCase().includes(q) || item.id.toLowerCase().includes(q)
      );
      const fullTbody = document.getElementById('full-ledger-tbody');
      fullTbody.innerHTML = filtered.map((item, index) => `
        <tr>
          <td>${index + 1}</td>
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

    // Munshi Form Submission
    function handleMunshiSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('munshi-guest-name').value;
      const city = document.getElementById('munshi-city').value;
      const side = document.getElementById('munshi-side').value;
      const amount = parseInt(document.getElementById('munshi-amount').value) || 0;
      const grams = document.getElementById('munshi-grams').value || '-';

      const newId = `GV-${100 + LEDGER_DATA.length + 1}`;
      LEDGER_DATA.unshift({
        id: newId,
        name: name,
        city: city,
        side: side,
        type: currentGiftType === 'cash' ? 'నగదు' : (currentGiftType === 'gold' ? 'బంగారం' : 'వెండి'),
        amount: amount,
        precious: grams,
        time: 'ఇప్పుడే (Just now)'
      });

      renderLedgerTables();
      playCelebrationChime();

      // Update receipt preview
      document.getElementById('rec-name').innerText = name;
      document.getElementById('rec-amount').innerText = `₹${amount.toLocaleString('en-IN')}`;

      alert(`ధన్యవాదాలు! ${name} గారి నుండి ₹${amount} కానుక ఎర్ర పుస్తకంలో నమోదైంది. వాట్సాప్ రశీదు పంపబడింది!`);
      document.getElementById('munshi-entry-form').reset();
      document.getElementById('munshi-amount').value = 5116;
    }

    // Expense Form Submission
    function handleExpenseSubmit(e) {
      e.preventDefault();
      const vendor = document.getElementById('exp-vendor').value;
      const amt = parseInt(document.getElementById('exp-amount').value) || 0;
      playCelebrationChime();
      alert(`ఖర్చు నమోదైంది: ${vendor} వారికి ₹${amt.toLocaleString('en-IN')} చెల్లింపు విజయవంతంగా రికార్డ్ చేయబడింది!`);
      document.getElementById('expense-add-form').reset();
    }

    // Web Audio Synthesized Royal Celebration Chime
    function playCelebrationChime() {
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        
        // Bell Note 1
        const osc1 = audioCtx.createOscillator();
        const gain1 = audioCtx.createGain();
        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(587.33, audioCtx.currentTime); // D5
        gain1.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gain1.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 1.2);
        osc1.connect(gain1);
        gain1.connect(audioCtx.destination);
        osc1.start();
        osc1.stop(audioCtx.currentTime + 1.2);

        // Bell Note 2 (Harmony)
        setTimeout(() => {
          const osc2 = audioCtx.createOscillator();
          const gain2 = audioCtx.createGain();
          osc2.type = 'sine';
          osc2.frequency.setValueAtTime(880, audioCtx.currentTime); // A5
          gain2.gain.setValueAtTime(0.35, audioCtx.currentTime);
          gain2.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 1.5);
          osc2.connect(gain2);
          gain2.connect(audioCtx.destination);
          osc2.start();
          osc2.stop(audioCtx.currentTime + 1.5);
        }, 120);

      } catch (err) {
        console.log('AudioContext not allowed without gesture', err);
      }
    }

    // Simulate Voice Soundbox Announcement
    function simulateVoiceSoundbox(amount) {
      playCelebrationChime();
      if ('speechSynthesis' in window) {
        const text = `గిఫ్ట్ వాలెట్ లో ${amount} రూపాయల కానుక అందింది. ధన్యవాదాలు!`;
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'te-IN';
        utterance.rate = 0.95;
        window.speechSynthesis.speak(utterance);
      } else {
        alert(`🔊 సౌండ్‌బాక్స్: గిఫ్ట్ వాలెట్ లో ₹${amount} కానుక అందింది!`);
      }
    }

    // PDF Download Simulation
    function downloadLedgerPDF() {
      alert('ఎర్ర పుస్తకం (Erra Pusthakam) PDF జనరేట్ అవుతోంది... విజయవంతంగా డౌన్‌లోడ్ అయింది!');
    }

    // Multi-Language Dictionary
    const DICTIONARY = {
      te: {
        tag: 'గిఫ్ట్ వాలెట్ • ROYAL SHAGUN TREASURY',
        addEntry: '+ కొత్త ఎంట్రీ (Add Shagun)',
        heroPill: 'భారతదేశపు నంబర్ 1 రాయల్ శుభకార్య ఖజానా • 2026 EDITION',
        heroTitle: 'Where Royal Celebrations Meet <em>Luxury Fintech</em>.',
        heroSub: 'పెళ్ళిళ్లు, గృహప్రవేశాలు, పుట్టినరోజులు మరియు వేడుకల కానుకల లెక్కలు, ఎర్ర పుస్తకం (శగున్ డైరీ), మరియు ఖర్చుల నికర లాభాలను అత్యంత సులభంగా నిర్వహించండి.'
      },
      en: {
        tag: 'GIFTVAULT • ROYAL SHAGUN TREASURY',
        addEntry: '+ New Entry (Add Shagun)',
        heroPill: "INDIA'S #1 ROYAL CELEBRATION LEDGER • 2026 EDITION",
        heroTitle: 'Where Royal Traditions Meet <em>Luxury Fintech</em>.',
        heroSub: 'Manage wedding gifts, housewarming contributions, traditional Red Book ledgers, and event expense surplus with bespoke luxury precision.'
      },
      hi: {
        tag: 'गिफ्ट वॉल्ट • रॉयल शगुन ट्रेजरी',
        addEntry: '+ नई प्रविष्टि (Add Shagun)',
        heroPill: 'भारत का नंबर 1 रॉयल शगुन लेज़र • 2026 EDITION',
        heroTitle: 'शाही परंपरा और <em>लक्ज़री फिनटेक</em> का संगम.',
        heroSub: 'शादी, गृह प्रवेश, जन्मदिन के उपहारों, पारंपरिक लाल बही-खाता (शगुन डायरी), और खर्चों के शुद्ध लाभ को आसानी से प्रबंधित करें।'
      }
    };

    function changeLanguage(lang) {
      const data = DICTIONARY[lang] || DICTIONARY['en'];
      document.getElementById('tag-phrase').innerText = data.tag;
      document.getElementById('txt-nav-add').innerText = data.addEntry;
      document.getElementById('txt-hero-pill').innerText = data.heroPill;
      document.getElementById('txt-hero-title').innerHTML = data.heroTitle;
      document.getElementById('txt-hero-sub').innerText = data.heroSub;
    }

    // Initialization
    window.addEventListener('DOMContentLoaded', () => {
      renderLedgerTables();
    });
  </script>
</body>
</html>
"""

def main():
    print(f"Generating ReactBits & Aura Luxury Edition to: {OUTPUT_PREVIEW}")
    os.makedirs(os.path.dirname(OUTPUT_PREVIEW), exist_ok=True)
    with open(OUTPUT_PREVIEW, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    
    # Also write to flutter web/index.html
    os.makedirs(os.path.dirname(OUTPUT_WEB), exist_ok=True)
    with open(OUTPUT_WEB, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)

    # Also update artifact
    os.makedirs(os.path.dirname(ARTIFACT_PREVIEW), exist_ok=True)
    with open(ARTIFACT_PREVIEW, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)

    print("SUCCESS: ReactBits + Aura + Godly Luxury Edition generated and synchronized!")

if __name__ == "__main__":
    main()
