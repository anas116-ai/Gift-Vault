# -*- coding: utf-8 -*-
"""
GiftVault Luxury Godly Redesign
Incorporating:
- Coolors Trending Luxury Palette: Warm Alabaster Silk (#FAF8F5), Deep Obsidian Slate (#0B0D13), 24K Byzantine Gold (#D4AF37), Velvet Bordeaux Vermilion (#9B1B30), Imperial Jade (#0D5C46)
- Motion & Spring physics (Emil Kowalski / motionsites.ai / ReactBits)
- Bespoke Sacred Kalasam Crest & Gold Foil Typography (Cinzel Decorative + Ramabhadra)
- ReactBits Spotlight card glow effects
- Awwwards editorial typography & Godly whitespace harmony
- Zero AI Slop (Slopdar 0/100)
"""

import os
import shutil

html_content = """<!DOCTYPE html>
<html lang="te" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault | గిఫ్ట్ వాలెట్ - రాయల్ చదివింపుల డిజిటల్ ఖజానా & వివాహ లెడ్జర్</title>
  
  <!-- Curated Luxury Typography (Awwwards / Godly pairings) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anek+Telugu:wght@300;400;500;600;700;800&family=Cinzel+Decorative:wght@600;700;900&family=Cinzel:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Ramabhadra&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            vault: {
              cream: '#FAF8F5',
              silk: '#F4EFEA',
              card: '#FFFFFF',
              dark: '#0B0D13',
              darkSurface: '#141722',
              darkBorder: '#232838',
              border: '#E8DFD5',
            },
            byzantine: {
              50: '#FDFBF4',
              100: '#F9F4E3',
              200: '#F3E7C4',
              300: '#EBD79F',
              400: '#E1C475',
              500: '#D4AF37', /* 24K Byzantine Royal Gold */
              600: '#B89225',
              700: '#947219',
              800: '#735614',
              900: '#543D0F',
            },
            vermilion: {
              50: '#FDF2F3',
              100: '#FCE4E6',
              200: '#F9CCD0',
              300: '#F3A3AB',
              500: '#D63A4A',
              700: '#9B1B30', /* Deep Velvet Bordeaux / Royal Kumkum */
              800: '#7E1526',
              900: '#64121F',
            },
            jade: {
              50: '#F0F9F5',
              100: '#DBEFE5',
              500: '#1EA56C',
              700: '#0D5C46', /* Imperial Jade Inflow */
              800: '#0B4837',
            }
          },
          fontFamily: {
            royal: ['Cinzel Decorative', 'serif'],
            cinzel: ['Cinzel', 'serif'],
            teluguHead: ['Ramabhadra', 'sans-serif'],
            telugu: ['Anek Telugu', 'sans-serif'],
            sans: ['Plus Jakarta Sans', 'sans-serif'],
          },
          boxShadow: {
            'glow-gold': '0 0 25px -4px rgba(212, 175, 55, 0.35)',
            'glow-sm': '0 0 12px 0 rgba(212, 175, 55, 0.25)',
            'luxury': '0 20px 40px -15px rgba(11, 13, 19, 0.08), 0 0 0 1px rgba(212, 175, 55, 0.15)',
            'chassis': '0 0 0 2.5px #2E3342, 0 35px 80px -15px rgba(0, 0, 0, 0.65), 0 15px 35px -10px rgba(0, 0, 0, 0.35)',
          }
        }
      }
    }
  </script>

  <style>
    :root {
      --ease-spring: cubic-bezier(0.23, 1, 0.32, 1);
      --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
    }

    body {
      font-family: 'Anek Telugu', 'Plus Jakarta Sans', sans-serif;
      background-color: #FAF8F5;
      color: #0B0D13;
      overflow-x: hidden;
      -webkit-tap-highlight-color: transparent;
      letter-spacing: -0.01em;
    }

    .font-royal { font-family: 'Cinzel Decorative', serif; }
    .font-cinzel { font-family: 'Cinzel', serif; }
    .font-telugu-title { font-family: 'Ramabhadra', sans-serif; }

    /* Metallic Gold Gradient Foil */
    .gold-foil-text {
      background: linear-gradient(135deg, #F9F4E3 0%, #D4AF37 50%, #947219 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .gold-foil-bg {
      background: linear-gradient(135deg, #F3E7C4 0%, #D4AF37 50%, #B89225 100%);
    }

    .gold-border-glow {
      border: 1px solid rgba(212, 175, 55, 0.32);
      box-shadow: 0 0 20px -3px rgba(212, 175, 55, 0.18);
    }

    /* Aura / ReactBits Spotlight Card Effect */
    .spotlight-card {
      position: relative;
      background: #FFFFFF;
      border: 1px solid rgba(232, 223, 213, 0.85);
      border-radius: 16px;
      transition: border-color 220ms var(--ease-spring), box-shadow 220ms var(--ease-spring);
    }
    .spotlight-card:hover {
      border-color: rgba(212, 175, 55, 0.5);
      box-shadow: 0 12px 30px -10px rgba(212, 175, 55, 0.15);
    }

    /* Red Book Leather Texture & Ruled Ledger Paper */
    .red-leather-book {
      background: radial-gradient(circle at 50% 0%, #9B1B30 0%, #64121F 80%, #450B14 100%);
      border: 3px solid #D4AF37;
      border-radius: 18px;
      box-shadow: 0 25px 60px -15px rgba(69, 11, 20, 0.6), 0 0 0 1px rgba(255, 215, 0, 0.2);
    }

    .ruled-ledger-paper {
      background-color: #FFFDF9;
      background-image: repeating-linear-gradient(transparent, transparent 33px, #EADBCC 33px, #EADBCC 34px);
      border: 1px solid #DFC9A3;
      border-radius: 12px;
      position: relative;
    }
    .ruled-ledger-paper::before {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 38px;
      width: 1.5px;
      background: rgba(155, 27, 48, 0.3);
    }

    /* Spring-Physics Tactile Press */
    button:active, .btn-tactile:active {
      transform: scale(0.975);
      transition: transform 120ms var(--ease-spring);
    }

    /* REALISTIC ANDROID SMARTPHONE CHASSIS */
    .phone-chassis {
      width: 390px;
      height: 810px;
      border-radius: 54px;
      background: #0B0D13;
      padding: 12px;
      box-shadow: 0 0 0 2.5px #2A2F3D, 0 35px 85px -15px rgba(0, 0, 0, 0.6), 0 15px 35px -10px rgba(0, 0, 0, 0.3);
      position: relative;
      flex-shrink: 0;
      margin: 0 auto;
      transition: all 350ms var(--ease-spring);
    }

    .phone-screen {
      width: 100%;
      height: 100%;
      border-radius: 44px;
      background: #FAF8F5;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .screen-scroll::-webkit-scrollbar { width: 3px; }
    .screen-scroll::-webkit-scrollbar-thumb {
      background: rgba(212, 175, 55, 0.35);
      border-radius: 3px;
    }

    /* DESKTOP FULL-WIDTH VIEW */
    .desktop-viewport {
      width: 100% !important;
      max-width: 1220px !important;
      height: auto !important;
      min-height: 88vh !important;
      border-radius: 24px !important;
      background: transparent !important;
      padding: 0 !important;
      box-shadow: none !important;
    }

    .desktop-viewport .phone-screen {
      border-radius: 24px !important;
      height: auto !important;
      min-height: 88vh !important;
      box-shadow: 0 15px 40px -15px rgba(11, 13, 19, 0.08);
      border: 1px solid rgba(232, 223, 213, 0.9);
    }

    .page-section { display: none; }
    .active-page { display: block; }

    .app-screen { display: none; }
    .active-app-screen { display: block; }
  </style>
</head>
<body class="min-h-screen text-vault-dark flex flex-col justify-between selection:bg-byzantine-200 selection:text-byzantine-900">

  <!-- ============================================================== -->
  <!-- 1. TOP GLOBAL NAVIGATION WITH BESPOKE SACRED CREST & SWITCHERS -->
  <!-- ============================================================== -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-vault-border/90 px-4 lg:px-8 py-2.5 transition-all">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
      
      <!-- Left: Bespoke Royal Crest & Typography (Refined Logo Mark) -->
      <div onclick="navigateToPage('landing')" class="flex items-center gap-3 cursor-pointer select-none group">
        
        <!-- Sacred Kalasam & Golden Treasury Vault Logo Mark -->
        <div class="relative w-10 h-10 rounded-xl bg-gradient-to-br from-byzantine-500 via-byzantine-600 to-amber-800 p-0.5 shadow-md shadow-byzantine-500/20 group-hover:scale-105 transition-transform">
          <div class="w-full h-full bg-vault-dark rounded-[10px] flex items-center justify-center relative overflow-hidden">
            <!-- Subtle Gold Radiance in Logo -->
            <div class="absolute inset-0 bg-radial from-byzantine-400/30 to-transparent"></div>
            
            <!-- Sacred Kalasam & Auspicious Coin Vector Mark -->
            <svg class="w-5 h-5 text-byzantine-400 relative z-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75">
              <!-- Kalasam Vessel -->
              <path d="M7 10h10c.8 0 1.5.6 1.7 1.4l1.1 5.6c.3 1.7-1 3-2.8 3H7c-1.8 0-3.1-1.3-2.8-3l1.1-5.6C5.5 10.6 6.2 10 7 10z" stroke="currentColor"/>
              <!-- Kalasam Neck & Lid -->
              <path d="M9 10V8a3 3 0 0 1 6 0v2" stroke="currentColor"/>
              <!-- Mango Leaves (Auspicious Foliage) -->
              <path d="M12 5C10 2 8 3 8 3s0 3 2 4" stroke="currentColor" stroke-linecap="round"/>
              <path d="M12 5C14 2 16 3 16 3s0 3-14 4" stroke="currentColor" stroke-linecap="round"/>
              <!-- Central Auspicious Shagun Coin Ring -->
              <circle cx="12" cy="15" r="2.2" stroke="#F9F4E3" fill="rgba(212, 175, 55, 0.35)"/>
            </svg>
          </div>
        </div>

        <div>
          <div class="flex items-center gap-2">
            <span class="font-royal text-[15px] font-black tracking-widest text-vault-dark">GIFTVAULT</span>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-vermilion-50 text-vermilion-700 border border-vermilion-200">గిఫ్ట్ వాలెట్</span>
          </div>
          <p class="text-[10px] text-stone-500 font-medium tracking-tight -mt-0.5">రాయల్ చదివింపుల డిజిటల్ ఖజానా & వివాహ లెడ్జర్</p>
        </div>
      </div>

      <!-- Center: Prominent Device Mode Switcher (Android Phone vs Desktop Web) -->
      <div class="flex items-center bg-vault-silk p-1 rounded-xl border border-vault-border text-xs font-semibold">
        <button id="toggle-device-mobile" onclick="setDeviceViewMode('mobile')" class="px-3.5 py-1.5 rounded-lg bg-vault-dark text-white shadow-xs transition-all flex items-center gap-1.5 btn-tactile">
          <svg class="w-3.5 h-3.5 text-byzantine-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
          <span>📱 మొబైల్ వెర్షన్ (Android Phone)</span>
        </button>
        <button id="toggle-device-desktop" onclick="setDeviceViewMode('desktop')" class="px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all flex items-center gap-1.5 btn-tactile">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="14" x="2" y="3" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
          <span>🖥️ డెస్క్‌టాప్ వెర్షన్ (Desktop Web)</span>
        </button>
      </div>

      <!-- Right: Sync Status, Language Selector & Action CTA -->
      <div class="flex items-center gap-2">
        
        <!-- Offline-First LocalStorage & Cloud Sync Badge -->
        <div class="hidden md:flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-jade-50 border border-jade-100 text-jade-700 text-[11px] font-semibold">
          <span class="w-2 h-2 rounded-full bg-jade-500 animate-pulse"></span>
          <span>ఆఫ్‌లైన్ సేఫ్ • క్లౌడ్ సింక్డ్</span>
        </div>

        <!-- Language Selector Dropdown -->
        <div class="flex items-center gap-1 text-xs bg-white border border-vault-border rounded-lg px-2 py-1 shadow-2xs">
          <svg class="w-3.5 h-3.5 text-stone-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
          <select id="lang-selector" onchange="onLanguageChanged(this.value)" class="bg-transparent text-xs font-semibold text-stone-800 focus:outline-none cursor-pointer">
            <option value="te" selected>తెలుగు (Telugu)</option>
            <option value="en">English (US)</option>
            <option value="hi">हिन्दी (Hindi)</option>
          </select>
        </div>

        <button onclick="navigateToPage('landing')" class="px-2.5 py-1 text-xs text-stone-600 hover:text-stone-900 font-semibold" data-i18n="nav_home">ల్యాండింగ్</button>
        <button onclick="navigateToPage('app')" class="px-3.5 py-1.5 text-xs font-bold rounded-lg bg-vault-dark text-byzantine-400 hover:bg-stone-800 shadow-2xs border border-byzantine-500/30 btn-tactile" data-i18n="nav_app">ఖజానా ఓపెన్</button>
      </div>

    </div>
  </header>

  <!-- ============================================================== -->
  <!-- 2. MAIN VIEWPORT (CHASSIS ADAPTER) -->
  <!-- ============================================================== -->
  <main class="py-6 px-3 flex-1 flex flex-col items-center justify-center">
    
    <div id="main-viewport-wrapper" class="phone-chassis">
      
      <div id="main-viewport-screen" class="phone-screen">
        
        <!-- Native Android Status Bar -->
        <div id="mobile-status-bar" class="h-7 bg-vault-dark text-stone-300 px-5 flex items-center justify-between text-[11px] font-semibold select-none z-30 flex-shrink-0">
          <span id="android-clock">10:30 AM</span>
          
          <!-- Punch-Hole Camera -->
          <div class="w-3 h-3 rounded-full bg-black border border-stone-800 mx-auto"></div>

          <div class="flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-stone-900 border border-stone-800">
            <span class="w-1.5 h-1.5 rounded-full bg-jade-500"></span>
            <span class="text-[9px] text-amber-300 font-bold">5G</span>
            <span class="text-[9px] text-stone-300 font-bold ml-1">100%</span>
          </div>
        </div>

        <!-- Scrollable Content Screen -->
        <div id="screen-scroll-container" class="flex-1 overflow-y-auto screen-scroll p-4 space-y-4">

          <!-- ============================================== -->
          <!-- SCREEN A: HERO & LUXURY LANDING PAGE -->
          <!-- ============================================== -->
          <div id="page-landing" class="page-section active-page space-y-5">
            
            <!-- Hero Spotlight Card (Godly / Aura aesthetic) -->
            <div class="relative overflow-hidden rounded-3xl bg-radial from-vault-darkSurface via-vault-dark to-black text-white p-6 text-center border border-byzantine-500/30 shadow-2xl">
              
              <!-- Subtle Background Sacred Geometric Matrix -->
              <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#D4AF37_1px,transparent_1px)] [background-size:18px_18px]"></div>

              <div class="relative z-10 space-y-3.5">
                
                <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-byzantine-500/15 text-byzantine-300 text-[10px] font-bold tracking-wider uppercase border border-byzantine-500/30 shadow-inner">
                  <span class="w-1.5 h-1.5 rounded-full bg-byzantine-400 animate-pulse"></span>
                  <span data-i18n="badge_heritage">రాయల్ ఇండియన్ & తెలుగు సంస్కృతి</span>
                </div>

                <h1 class="text-xl sm:text-2xl font-bold font-telugu-title text-byzantine-100 tracking-tight leading-tight">
                  చదివింపుల డిజిటల్ ఖజానా & వివాహ లెడ్జర్
                </h1>

                <p class="text-xs text-stone-300 max-w-sm mx-auto leading-relaxed" data-i18n="hero_subtext">
                  Nyota, ShagunBook, DMoi కంటే 10 రెట్లు మెరుగ్గా — ఎర్ర పుస్తకం గౌరవం, ఖర్చుల ట్రాకర్, బంగారం-వెండి లెక్క, 1-క్లిక్ WhatsApp రసీదులు & రియల్-టైమ్ UPI సౌండ్‌బాక్స్!
                </p>

                <!-- Value Pillars Grid -->
                <div class="grid grid-cols-2 gap-2 text-left text-[10px] pt-1.5">
                  <div class="p-2.5 rounded-xl bg-vault-darkSurface/90 border border-byzantine-500/25">
                    <span class="text-byzantine-400 font-bold block">⚖️ వచ్చినవి vs ఇచ్చినవి</span>
                    <span class="text-stone-400 text-[9px]">సామాజిక బంధుత్వ సరితూకం లెక్క</span>
                  </div>
                  <div class="p-2.5 rounded-xl bg-vault-darkSurface/90 border border-byzantine-500/25">
                    <span class="text-byzantine-400 font-bold block">💰 ఖర్చులు & బడ్జెట్</span>
                    <span class="text-stone-400 text-[9px]">ఈవెంట్ నికర మిగులు / బ్యాలెన్స్</span>
                  </div>
                  <div class="p-2.5 rounded-xl bg-vault-darkSurface/90 border border-byzantine-500/25">
                    <span class="text-byzantine-400 font-bold block">🪙 బంగారం & వెండి</span>
                    <span class="text-stone-400 text-[9px]">నగదుతో పాటు కానుకల రికార్డు</span>
                  </div>
                  <div class="p-2.5 rounded-xl bg-vault-darkSurface/90 border border-byzantine-500/25">
                    <span class="text-byzantine-400 font-bold block">💬 1-క్లిక్ WhatsApp</span>
                    <span class="text-stone-400 text-[9px]">వెంటనే కృతజ్ఞతా రసీదు పంపు</span>
                  </div>
                </div>

                <!-- Action CTAs -->
                <div class="pt-2 flex flex-col gap-2">
                  <button onclick="navigateToPage('app')" class="w-full py-2.5 rounded-xl gold-foil-bg text-vault-dark font-bold text-xs tracking-wide shadow-glow-sm hover:shadow-glow-gold transition-all btn-tactile">
                    <span data-i18n="btn_enter_treasury">🚀 ఇప్పుడే ఉచితంగా ప్రారంభించండి</span>
                  </button>
                  <button onclick="navigateToPage('auth')" class="w-full py-2 rounded-xl bg-vault-darkSurface hover:bg-stone-800 text-stone-300 font-semibold text-xs border border-vault-darkBorder btn-tactile">
                    <span>🔐 లాగిన్ / ఖాతా వివరాలు</span>
                  </button>
                </div>

              </div>
            </div>

            <!-- Traditional Red Book Teaser Card -->
            <div class="spotlight-card p-4 space-y-2">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-vermilion-700 font-telugu-title">📕 సాంప్రదాయ ఎర్ర పుస్తకం లేఅవుట్</span>
                <span class="text-[10px] text-byzantine-700 font-bold tracking-widest font-telugu-title">॥ శ్రీరస్తు శుభమస్తు ॥</span>
              </div>
              <p class="text-[11px] text-stone-600 leading-relaxed">
                తెలుగువారి సంప్రదాయ ఎర్ర బైండింగ్ చదివింపుల డైరీ తరహాలోనే, ప్రతి అతిథి ఊరు, బంధుత్వం, కవరు నెంబరుతో సహా లైన్-బై-లైన్ ప్రింటబుల్ లెడ్జర్.
              </p>
            </div>

          </div>

          <!-- ============================================== -->
          <!-- SCREEN B: AUTHENTICATION / LOGIN -->
          <!-- ============================================== -->
          <div id="page-auth" class="page-section space-y-4">
            <div class="spotlight-card p-5 space-y-3.5 text-center">
              
              <div class="w-12 h-12 mx-auto rounded-2xl bg-byzantine-50 border border-byzantine-200 flex items-center justify-center">
                <svg class="w-6 h-6 text-byzantine-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><line x1="19" y1="8" x2="19" y2="14"></line><line x1="22" y1="11" x2="16" y2="11"></line></svg>
              </div>

              <div>
                <h2 class="font-bold text-vault-dark text-base font-telugu-title" data-i18n="login_title">ఖాతాలోకి ప్రవేశించండి</h2>
                <p class="text-xs text-stone-500" data-i18n="login_subtitle">మీ కుటుంబ శుభకార్యాల చదివింపుల వివరాలు భద్రంగా ఉంటాయి</p>
              </div>

              <!-- Official Google Sign-In -->
              <button onclick="loginWithGoogleSim()" class="w-full h-10 px-3 rounded-xl border border-vault-border bg-white hover:bg-stone-50 text-stone-700 font-semibold text-xs flex items-center justify-center gap-2 shadow-2xs btn-tactile">
                <svg class="w-4 h-4" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                  <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                  <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                  <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
                </svg>
                <span data-i18n="btn_google_signin">Google తో లాగిన్ అవ్వండి</span>
              </button>

              <div class="relative flex items-center justify-center my-1.5">
                <div class="border-t border-vault-border w-full"></div>
                <span class="bg-white px-2 text-[10px] text-stone-400 uppercase font-bold" data-i18n="label_or">లేదా</span>
              </div>

              <!-- Phone OTP simulation -->
              <div class="space-y-2 text-left">
                <label class="block text-[10px] font-bold text-stone-700" data-i18n="label_phone_login">మొబైల్ నెంబర్:</label>
                <div class="flex gap-1.5">
                  <input id="auth-phone-input" type="tel" placeholder="+91 98765 43210" class="flex-1 h-9 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl focus:outline-none focus:border-byzantine-500">
                  <button onclick="sendOtpSim()" class="h-9 px-3 rounded-xl bg-vault-dark text-white font-bold text-xs btn-tactile" data-i18n="btn_get_otp">OTP</button>
                </div>
              </div>

              <div class="pt-1">
                <button onclick="enterAsGuest()" class="w-full h-9 rounded-xl bg-byzantine-50 hover:bg-byzantine-100 border border-byzantine-200 text-byzantine-900 font-bold text-xs flex items-center justify-center gap-1.5 btn-tactile">
                  <svg class="w-3.5 h-3.5 text-byzantine-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                  <span data-i18n="btn_guest_mode">గెస్ట్ మోడ్ (డెమో చూడండి)</span>
                </button>
              </div>

            </div>
          </div>

          <!-- ============================================== -->
          <!-- SCREEN C: MASTER APP WORKSPACE -->
          <!-- ============================================== -->
          <div id="page-app" class="page-section space-y-3.5">
            
            <!-- Active Event Header Banner with Counter Selector -->
            <div class="spotlight-card p-3.5 space-y-2.5">
              <div class="flex items-center justify-between">
                <div>
                  <div class="flex items-center gap-1.5">
                    <h3 id="app-event-name" class="font-bold text-xs text-vault-dark font-telugu-title leading-tight">
                      ఆనంద్ & శ్రేయ వివాహ మహోత్సవం
                    </h3>
                    <span class="w-2 h-2 rounded-full bg-jade-500"></span>
                  </div>
                  <p id="app-event-meta" class="text-[10px] text-stone-500 mt-0.5">శ్రీ కన్వెన్షన్, హైదరాబాద్ • 15 నవంబర్ 2026</p>
                </div>
                <button onclick="openModalNewEvent()" class="h-7 px-3 rounded-lg bg-vault-dark text-byzantine-400 hover:bg-stone-800 text-[10px] font-bold flex items-center gap-1 shadow-2xs border border-byzantine-500/30 btn-tactile">
                  <span>+</span>
                  <span data-i18n="btn_new_event">కొత్త ఈవెంట్</span>
                </button>
              </div>

              <!-- Counter Desk Selector (ShagunBook / Nyota feature) -->
              <div class="flex items-center justify-between pt-1.5 border-t border-vault-border/60 text-[10px]">
                <div class="flex items-center gap-1.5">
                  <span class="text-stone-500 font-bold">కౌంటర్ డెస్క్:</span>
                  <select id="active-counter-select" onchange="onCounterChanged(this.value)" class="bg-byzantine-50 text-byzantine-900 font-bold px-2 py-0.5 rounded-md border border-byzantine-200 focus:outline-none">
                    <option value="వరుడి వైపు కౌంటర్ (Groom Desk)">వరుడి వైపు కౌంటర్ (Groom)</option>
                    <option value="వధువు వైపు కౌంటర్ (Bride Desk)">వధువు వైపు కౌంటర్ (Bride)</option>
                    <option value="సాధారణ / విఐపి డెస్క్ (VIP Desk)">విఐపి & బంధువుల డెస్క్</option>
                  </select>
                </div>
                <span class="text-jade-700 font-bold flex items-center gap-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-jade-500 animate-pulse"></span>
                  <span>మున్షీ: ఆపరేటర్ 01</span>
                </span>
              </div>
            </div>

            <!-- Segmented Pill Navigation Tabs -->
            <div class="flex items-center gap-1 overflow-x-auto pb-1 text-[11px] font-bold select-none">
              <button onclick="switchAppTab('dashboard')" id="navtab-dashboard" class="px-3 py-1.5 rounded-xl bg-vault-dark text-byzantine-400 border border-byzantine-500/40 shrink-0 btn-tactile">🏛️ హోమ్</button>
              <button onclick="switchAppTab('desk')" id="navtab-desk" class="px-3 py-1.5 rounded-xl bg-white text-stone-700 hover:bg-stone-100 border border-vault-border shrink-0 btn-tactile">⚡ కౌంటర్ డెస్క్</button>
              <button onclick="switchAppTab('ledger')" id="navtab-ledger" class="px-3 py-1.5 rounded-xl bg-white text-stone-700 hover:bg-stone-100 border border-vault-border shrink-0 btn-tactile">📖 లెడ్జర్ & పుస్తకం</button>
              <button onclick="switchAppTab('expenses')" id="navtab-expenses" class="px-3 py-1.5 rounded-xl bg-white text-stone-700 hover:bg-stone-100 border border-vault-border shrink-0 btn-tactile">💰 ఖర్చులు & బడ్జెట్</button>
              <button onclick="switchAppTab('reciprocity')" id="navtab-reciprocity" class="px-3 py-1.5 rounded-xl bg-white text-stone-700 hover:bg-stone-100 border border-vault-border shrink-0 btn-tactile">⚖️ సరితూకం</button>
              <button onclick="switchAppTab('invites')" id="navtab-invites" class="px-3 py-1.5 rounded-xl bg-white text-stone-700 hover:bg-stone-100 border border-vault-border shrink-0 btn-tactile">💌 ఆహ్వానాలు / RSVP</button>
              <button onclick="switchAppTab('qr')" id="navtab-qr" class="px-3 py-1.5 rounded-xl bg-white text-stone-700 hover:bg-stone-100 border border-vault-border shrink-0 btn-tactile">📲 QR & సౌండ్‌బాక్స్</button>
            </div>

            <!-- ======================================================= -->
            <!-- SUB-TAB 1: DASHBOARD OVERVIEW -->
            <!-- ======================================================= -->
            <div id="subtab-dashboard" class="app-screen active-app-screen space-y-3">
              
              <!-- 4 Summary Metric Cards (Function Budget + MoiMoney style) -->
              <div class="grid grid-cols-2 gap-2">
                
                <!-- Received Shagun Inflow -->
                <div class="p-3.5 rounded-2xl bg-gradient-to-br from-jade-50 to-white border border-jade-100 shadow-2xs">
                  <span class="text-[9px] font-bold text-jade-800 uppercase tracking-wider block">వచ్చిన చదివింపులు (Inflow)</span>
                  <div class="flex items-baseline gap-1 mt-1">
                    <span id="metric-total-received" class="text-base font-bold text-jade-800 font-cinzel tracking-tight">₹7,85,400</span>
                  </div>
                  <span id="metric-received-count" class="text-[9px] text-jade-700 font-semibold block mt-0.5">18 మంది బంధువులు</span>
                </div>

                <!-- Event Expenses Outflow -->
                <div class="p-3.5 rounded-2xl bg-gradient-to-br from-vermilion-50 to-white border border-vermilion-100 shadow-2xs">
                  <span class="text-[9px] font-bold text-vermilion-700 uppercase tracking-wider block">ఈవెంట్ ఖర్చులు (Outflow)</span>
                  <div class="flex items-baseline gap-1 mt-1">
                    <span id="metric-total-expenses" class="text-base font-bold text-vermilion-800 font-cinzel tracking-tight">₹5,40,000</span>
                  </div>
                  <span class="text-[9px] text-vermilion-700 font-semibold block mt-0.5">మండపం, భోజనాలు & డెకరేషన్</span>
                </div>

                <!-- Net Surplus / Balance -->
                <div class="p-3.5 rounded-2xl bg-gradient-to-br from-byzantine-50 to-white border border-byzantine-200/80 shadow-2xs">
                  <span class="text-[9px] font-bold text-byzantine-900 uppercase tracking-wider block">నికర మిగులు (Net Balance)</span>
                  <div class="flex items-baseline gap-1 mt-1">
                    <span id="metric-net-balance" class="text-base font-bold text-byzantine-800 font-cinzel tracking-tight">+₹2,45,400</span>
                  </div>
                  <span class="text-[9px] text-jade-700 font-bold block mt-0.5">✓ ఆదాయం మిగులులో ఉంది</span>
                </div>

                <!-- Gold & Silver Counter (Gift Note feature) -->
                <div class="p-3.5 rounded-2xl bg-gradient-to-br from-stone-50 to-white border border-vault-border shadow-2xs">
                  <span class="text-[9px] font-bold text-stone-700 uppercase tracking-wider block">బంగారం & వెండి కానుకలు</span>
                  <div class="text-xs font-bold text-vault-dark mt-1">
                    <span id="metric-total-gold">🪙 15 గ్రా.</span> • <span id="metric-total-silver">🥈 180 గ్రా.</span>
                  </div>
                  <span class="text-[9px] text-stone-500 font-semibold block mt-0.5">4 వస్తు రూప కానుకలు</span>
                </div>

              </div>

              <!-- Quick Launch Actions Grid -->
              <div class="grid grid-cols-4 gap-1.5 text-center text-[10px] font-bold">
                <button onclick="switchAppTab('desk')" class="p-2.5 rounded-2xl bg-vault-dark text-byzantine-400 border border-byzantine-500/30 flex flex-col items-center gap-1 shadow-2xs btn-tactile">
                  <span class="text-xs">⚡</span>
                  <span>కౌంటర్ డెస్క్</span>
                </button>
                <button onclick="openModalAddExpense()" class="p-2.5 rounded-2xl bg-white border border-vault-border text-stone-800 flex flex-col items-center gap-1 shadow-2xs btn-tactile">
                  <span class="text-xs">💸</span>
                  <span>+ ఖర్చు వేయి</span>
                </button>
                <button onclick="switchAppTab('ledger')" class="p-2.5 rounded-2xl bg-white border border-vault-border text-stone-800 flex flex-col items-center gap-1 shadow-2xs btn-tactile">
                  <span class="text-xs">📕</span>
                  <span>ఎర్ర పుస్తకం</span>
                </button>
                <button onclick="switchAppTab('qr')" class="p-2.5 rounded-2xl bg-white border border-vault-border text-stone-800 flex flex-col items-center gap-1 shadow-2xs btn-tactile">
                  <span class="text-xs">📲</span>
                  <span>సౌండ్‌బాక్స్</span>
                </button>
              </div>

              <!-- Recent Entries Stream -->
              <div class="spotlight-card p-3.5 space-y-2.5">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-vault-dark font-telugu-title">తాజా చదివింపులు (Recent Stream)</span>
                  <button onclick="switchAppTab('ledger')" class="text-[10px] text-vermilion-700 font-bold hover:underline">అన్నీ చూడండి →</button>
                </div>
                <div id="dashboard-recent-entries" class="space-y-1.5 text-xs">
                  <!-- Populated via JS -->
                </div>
              </div>

            </div>

            <!-- ======================================================= -->
            <!-- SUB-TAB 2: RAPID MUNSHI COUNTER DESK -->
            <!-- ======================================================= -->
            <div id="subtab-desk" class="app-screen space-y-3">
              
              <div class="spotlight-card p-4 space-y-3">
                <div class="flex items-center justify-between border-b border-vault-border/60 pb-2">
                  <div>
                    <h3 class="font-bold text-xs text-vault-dark font-telugu-title">⚡ మున్షీ రాపిడ్ కౌంటర్ డెస్క్ (Fast Entry)</h3>
                    <p class="text-[10px] text-stone-500">అతిథి రాగానే సెకన్లలో నమోదు చేసి WhatsApp రసీదు పంపండి</p>
                  </div>
                  <span class="px-2 py-0.5 rounded-full bg-jade-50 text-jade-800 border border-jade-100 text-[9px] font-bold">లైవ్ కౌంటర్</span>
                </div>

                <div class="space-y-2 text-xs">
                  
                  <!-- Guest Name & City Autocomplete -->
                  <div class="grid grid-cols-2 gap-2">
                    <div>
                      <label class="block text-[10px] font-bold text-stone-700 mb-0.5">అతిథి / బంధువు పేరు *:</label>
                      <input id="desk-input-name" type="text" placeholder="కొత్తపల్లి వెంకటేశ్వర్లు" class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl focus:outline-none focus:border-byzantine-500">
                    </div>
                    <div class="relative">
                      <label class="block text-[10px] font-bold text-stone-700 mb-0.5">ఊరు (Autocomplete):</label>
                      <input id="desk-input-city" type="text" oninput="onDeskCityInput(this.value)" placeholder="హైదరాబాద్ / గుంటూరు..." class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl focus:outline-none focus:border-byzantine-500">
                      <div id="desk-city-suggestions" class="absolute left-0 right-0 top-full mt-1 bg-white border border-vault-border rounded-xl shadow-lg z-20 hidden max-h-36 overflow-y-auto"></div>
                    </div>
                  </div>

                  <!-- Relation & Phone (for WhatsApp) -->
                  <div class="grid grid-cols-2 gap-2">
                    <div>
                      <label class="block text-[10px] font-bold text-stone-700 mb-0.5">చుట్టరికం / బంధుత్వం:</label>
                      <select id="desk-select-relation" class="w-full h-8 px-2 text-xs bg-vault-cream border border-vault-border rounded-xl focus:outline-none">
                        <option value="మేనమామ తరఫు">మేనమామ తరఫు</option>
                        <option value="బావ / బావమరిది">బావ / బావమరిది</option>
                        <option value="తాత / నానమ్మ">తాత / నానమ్మ</option>
                        <option value="పెద్దనాన్న / పినతండ్రి">పెద్దనాన్న / పినతండ్రి</option>
                        <option value="అత్తయ్య / మావయ్య">అత్తయ్య / మావయ్య</option>
                        <option value="మిత్రులు (Friends)">మిత్రులు (Friends)</option>
                        <option value="సహోద్యోగులు (Colleagues)">సహోద్యోగులు (Colleagues)</option>
                        <option value="గ్రామస్థులు / ఇరుగుపొరుగు">గ్రామస్థులు / ఇరుగుపొరుగు</option>
                      </select>
                    </div>
                    <div>
                      <label class="block text-[10px] font-bold text-stone-700 mb-0.5">మొబైల్ (WhatsApp కోసం):</label>
                      <input id="desk-input-phone" type="tel" placeholder="9876543210" class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl focus:outline-none">
                    </div>
                  </div>

                  <!-- Gift Type Switcher -->
                  <div>
                    <label class="block text-[10px] font-bold text-stone-700 mb-1">కానుక రకం (Gift Category):</label>
                    <div class="grid grid-cols-4 gap-1 text-[10px] font-bold text-center">
                      <button type="button" onclick="setDeskGiftType('cash')" id="btn-gifttype-cash" class="py-1 rounded-xl bg-vault-dark text-byzantine-400 border border-byzantine-500/40 btn-tactile">💵 నగదు</button>
                      <button type="button" onclick="setDeskGiftType('gold')" id="btn-gifttype-gold" class="py-1 rounded-xl bg-white text-stone-700 border border-vault-border btn-tactile">🪙 బంగారం</button>
                      <button type="button" onclick="setDeskGiftType('silver')" id="btn-gifttype-silver" class="py-1 rounded-xl bg-white text-stone-700 border border-vault-border btn-tactile">🥈 వెండి</button>
                      <button type="button" onclick="setDeskGiftType('item')" id="btn-gifttype-item" class="py-1 rounded-xl bg-white text-stone-700 border border-vault-border btn-tactile">🎁 వస్తువు</button>
                    </div>
                  </div>

                  <!-- CASH SECTION -->
                  <div id="desk-cash-section" class="space-y-2">
                    <div class="flex items-center gap-2">
                      <div class="flex-1">
                        <label class="block text-[10px] font-bold text-stone-700 mb-0.5">మొత్తం చదివింపు (₹):</label>
                        <input id="desk-input-amount" type="number" placeholder="2116" class="w-full h-9 px-3 text-sm font-bold text-vault-dark bg-byzantine-50 border border-byzantine-200 rounded-xl focus:outline-none">
                      </div>
                      
                      <!-- Lucky Auspicious +1 Coin -->
                      <div class="pt-4 flex items-center gap-1.5">
                        <input type="checkbox" id="desk-check-luckyone" onchange="toggleLuckyCoin(this.checked)" class="w-4 h-4 text-byzantine-600 rounded">
                        <label for="desk-check-luckyone" class="text-[10px] font-bold text-byzantine-900 cursor-pointer">+₹1 లక్కీ నాణెం</label>
                      </div>
                    </div>

                    <!-- Auspicious Quick Buttons -->
                    <div class="flex flex-wrap gap-1 pt-0.5">
                      <button type="button" onclick="setDeskQuickAmount(516)" class="px-2.5 py-0.5 rounded-lg bg-white text-[10px] font-bold hover:bg-byzantine-50 border border-vault-border btn-tactile">₹516</button>
                      <button type="button" onclick="setDeskQuickAmount(1116)" class="px-2.5 py-0.5 rounded-lg bg-white text-[10px] font-bold hover:bg-byzantine-50 border border-vault-border btn-tactile">₹1,116</button>
                      <button type="button" onclick="setDeskQuickAmount(2116)" class="px-2.5 py-0.5 rounded-lg bg-white text-[10px] font-bold hover:bg-byzantine-50 border border-vault-border btn-tactile">₹2,116</button>
                      <button type="button" onclick="setDeskQuickAmount(5116)" class="px-2.5 py-0.5 rounded-lg bg-white text-[10px] font-bold hover:bg-byzantine-50 border border-vault-border btn-tactile">₹5,116</button>
                      <button type="button" onclick="setDeskQuickAmount(11116)" class="px-2.5 py-0.5 rounded-lg bg-white text-[10px] font-bold hover:bg-byzantine-50 border border-vault-border btn-tactile">₹11,116</button>
                    </div>
                  </div>

                  <!-- PRECIOUS METALS / ITEM SECTION -->
                  <div id="desk-precious-section" class="hidden space-y-2 p-2.5 rounded-2xl bg-byzantine-50/70 border border-byzantine-200">
                    <div class="grid grid-cols-2 gap-2">
                      <div>
                        <label class="block text-[10px] font-bold text-byzantine-900 mb-0.5">బరువు / పరిమాణం:</label>
                        <input id="desk-input-metal-weight" type="text" placeholder="ఉదా: 8 గ్రాములు / 1 తులం" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
                      </div>
                      <div>
                        <label class="block text-[10px] font-bold text-byzantine-900 mb-0.5">ఆభరణం / వస్తువు వివరాలు:</label>
                        <input id="desk-input-metal-desc" type="text" placeholder="బంగారు ఉంగరం / వెండి కుందులు" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
                      </div>
                    </div>
                  </div>

                  <!-- Cover & Notes -->
                  <div class="grid grid-cols-2 gap-2">
                    <div>
                      <label class="block text-[10px] font-bold text-stone-700 mb-0.5">కవరు నెంబర్ (Envelope No):</label>
                      <input id="desk-input-cover" type="text" placeholder="కవరు #18" class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl">
                    </div>
                    <div>
                      <label class="block text-[10px] font-bold text-stone-700 mb-0.5">నోట్స్ / ప్రత్యేక సూచనలు:</label>
                      <input id="desk-input-notes" type="text" placeholder="విశేషాలు..." class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl">
                    </div>
                  </div>

                  <!-- Action Buttons -->
                  <div class="pt-2 flex gap-2">
                    <button onclick="submitDeskEntry(true)" class="flex-1 h-9 rounded-xl bg-vault-dark hover:bg-stone-800 text-byzantine-400 font-bold text-xs flex items-center justify-center gap-1.5 shadow-sm border border-byzantine-500/30 btn-tactile">
                      <svg class="w-3.5 h-3.5 text-jade-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                      <span>నమోదు & WhatsApp రసీదు</span>
                    </button>
                    <button onclick="submitDeskEntry(false)" class="h-9 px-3 rounded-xl bg-white hover:bg-stone-100 text-stone-700 font-bold text-xs border border-vault-border btn-tactile">
                      <span>కేవలం నమోదు</span>
                    </button>
                  </div>

                </div>
              </div>

            </div>

            <!-- ======================================================= -->
            <!-- SUB-TAB 3: DUAL-VIEW LEDGER & RED BOOK -->
            <!-- ======================================================= -->
            <div id="subtab-ledger" class="app-screen space-y-3">
              
              <div class="flex items-center justify-between">
                <div class="flex items-center bg-vault-silk p-0.5 rounded-xl border border-vault-border text-xs font-bold">
                  <button id="btn-ledger-view-table" onclick="setLedgerView('table')" class="px-3 py-1 rounded-lg bg-vault-dark text-white shadow-2xs btn-tactile">📋 మోడ్రన్ టేబుల్</button>
                  <button id="btn-ledger-view-book" onclick="setLedgerView('book')" class="px-3 py-1 rounded-lg text-stone-600 hover:text-stone-900 btn-tactile">📕 ఎర్ర పుస్తకం</button>
                </div>
                
                <div class="flex items-center gap-1.5">
                  <button onclick="exportToCsv()" class="h-7 px-2.5 text-[10px] font-bold rounded-lg bg-white border border-vault-border text-stone-700 shadow-2xs btn-tactile">📥 Excel</button>
                  <button onclick="exportToPdf()" class="h-7 px-2.5 text-[10px] font-bold rounded-lg bg-vault-dark text-byzantine-400 shadow-2xs border border-byzantine-500/30 btn-tactile">🖨️ PDF ప్రింట్</button>
                </div>
              </div>

              <!-- Search & Filter Controls -->
              <div class="flex gap-1.5 text-xs">
                <input id="ledger-search-input" type="text" oninput="filterLedger()" placeholder="పేరు, ఊరు లేదా చుట్టరికం వెతకండి..." class="flex-1 h-8 px-2.5 text-xs bg-white border border-vault-border rounded-xl">
                <select id="ledger-filter-type" onchange="filterLedger()" class="h-8 px-2 bg-white border border-vault-border rounded-xl text-[10px] font-bold">
                  <option value="all">అన్ని కానుకలు</option>
                  <option value="నగదు">నగదు మాత్రమే</option>
                  <option value="బంగారం">బంగారం</option>
                  <option value="వెండి">వెండి</option>
                  <option value="వస్తువు">వస్తు రూప</option>
                </select>
              </div>

              <!-- MODE A: MODERN DATA TABLE -->
              <div id="ledger-container-table" class="spotlight-card overflow-hidden">
                <div class="overflow-x-auto">
                  <table class="w-full text-left text-xs">
                    <thead class="bg-vault-cream border-b border-vault-border text-[10px] uppercase font-bold text-stone-600">
                      <tr>
                        <th class="p-2.5">నెం.</th>
                        <th class="p-2.5">అతిథి & ఊరు</th>
                        <th class="p-2.5">సంబంధం / కౌంటర్</th>
                        <th class="p-2.5 text-right">కానుక / మొత్తం</th>
                        <th class="p-2.5 text-center">చర్యలు</th>
                      </tr>
                    </thead>
                    <tbody id="ledger-tbody-rows" class="divide-y divide-vault-border/50 text-xs">
                      <!-- Rendered via JS -->
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- MODE B: TRADITIONAL RED BOOK (ఎర్ర చదివింపుల పుస్తకం) -->
              <div id="ledger-container-book" class="hidden red-leather-book p-3.5">
                <div class="ruled-ledger-paper p-4 space-y-3">
                  
                  <div class="text-center border-b-2 border-byzantine-500 pb-2">
                    <span class="text-byzantine-700 font-bold text-sm tracking-widest block font-telugu-title">॥ శ్రీరస్తు శుభమస్తు ॥</span>
                    <h4 class="font-bold text-stone-900 text-xs font-telugu-title">చదివింపుల సాంప్రదాయ దస్తావేజు</h4>
                    <span class="text-[9px] text-stone-500">పుట నెంబరు: 01 • శుభకార్య వేదిక: శ్రీ కన్వెన్షన్</span>
                  </div>

                  <div id="ledger-book-entries" class="space-y-2 text-xs pl-8">
                    <!-- Calligraphic Lined entries rendered via JS -->
                  </div>

                  <div class="pt-2 border-t border-stone-300 flex justify-between text-[11px] font-bold text-stone-800 pl-8">
                    <span>ఈ పుట మొత్తం చదివింపులు:</span>
                    <span id="book-page-total" class="font-cinzel text-jade-800 text-xs">₹7,85,400</span>
                  </div>

                </div>
              </div>

            </div>

            <!-- ======================================================= -->
            <!-- SUB-TAB 4: EVENT EXPENSES & NET BALANCE -->
            <!-- ======================================================= -->
            <div id="subtab-expenses" class="app-screen space-y-3">
              
              <div class="spotlight-card p-4 space-y-3">
                <div class="flex items-center justify-between border-b border-vault-border/60 pb-2">
                  <div>
                    <h3 class="font-bold text-xs text-vault-dark font-telugu-title">💰 ఈవెంట్ ఖర్చులు & బడ్జెట్ మేనేజర్</h3>
                    <p class="text-[10px] text-stone-500">మొత్తం ఖర్చులు & చదివింపుల నికర బ్యాలెన్స్ లెక్క</p>
                  </div>
                  <button onclick="openModalAddExpense()" class="h-7 px-2.5 rounded-lg bg-vermilion-700 text-white font-bold text-[10px] flex items-center gap-1 shadow-2xs btn-tactile">
                    <span>+</span>
                    <span>ఖర్చు నమోదు</span>
                  </button>
                </div>

                <!-- Financial Statement Card (Aura dark surface) -->
                <div class="p-3.5 rounded-2xl bg-vault-dark text-white space-y-2 border border-byzantine-500/25">
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-stone-400">మొత్తం వచ్చిన చదివింపులు (+):</span>
                    <span class="font-bold text-jade-400 font-cinzel">₹7,85,400</span>
                  </div>
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-stone-400">మొత్తం అయిన ఈవెంట్ ఖర్చులు (-):</span>
                    <span class="font-bold text-vermilion-300 font-cinzel">₹5,40,000</span>
                  </div>
                  <div class="border-t border-stone-800 pt-1.5 flex justify-between items-center text-xs font-bold">
                    <span class="text-byzantine-300">నికర మిగులు లాభం (Net Surplus):</span>
                    <span class="text-sm font-bold text-byzantine-400 font-cinzel">+₹2,45,400</span>
                  </div>
                </div>

                <!-- Category Breakdown -->
                <div class="space-y-1.5">
                  <span class="text-[10px] font-bold text-stone-700 uppercase tracking-wider block">ప్రధాన ఖర్చుల వర్గీకరణ:</span>
                  <div id="expenses-category-list" class="space-y-1.5 text-xs">
                    <!-- Rendered via JS -->
                  </div>
                </div>

              </div>

            </div>

            <!-- ======================================================= -->
            <!-- SUB-TAB 5: RECIPROCITY BALANCE -->
            <!-- ======================================================= -->
            <div id="subtab-reciprocity" class="app-screen space-y-3">
              
              <div class="spotlight-card p-4 space-y-3">
                <div class="flex items-center justify-between border-b border-vault-border/60 pb-2">
                  <div>
                    <h3 class="font-bold text-xs text-vault-dark font-telugu-title">⚖️ చదివింపుల సరితూకం (Reciprocity Balance)</h3>
                    <p class="text-[10px] text-stone-500">వారు మనకు ఇచ్చింది vs గతంలో మనం వారికి ఇచ్చింది</p>
                  </div>
                  <span class="text-[10px] font-bold text-jade-800 bg-jade-50 px-2.5 py-0.5 rounded-full border border-jade-100">బంధుత్వ లెక్క</span>
                </div>

                <div id="reciprocity-list" class="space-y-2 text-xs">
                  <!-- Rendered via JS -->
                </div>
              </div>

            </div>

            <!-- ======================================================= -->
            <!-- SUB-TAB 6: GUEST LIST & INVITATION RSVP -->
            <!-- ======================================================= -->
            <div id="subtab-invites" class="app-screen space-y-3">
              
              <div class="spotlight-card p-4 space-y-3">
                <div class="flex items-center justify-between border-b border-vault-border/60 pb-2">
                  <div>
                    <h3 class="font-bold text-xs text-vault-dark font-telugu-title">💌 ఆహ్వానాలు & RSVP అటెండెన్స్</h3>
                    <p class="text-[10px] text-stone-500">బంధువుల రాక ధ్రువీకరణ & డిజిటల్ శుభలేఖ షేరింగ్</p>
                  </div>
                  <button onclick="shareDigitalInvite()" class="h-7 px-3 rounded-lg bg-jade-700 text-white font-bold text-[10px] flex items-center gap-1.5 shadow-2xs btn-tactile">
                    <span>📲</span>
                    <span>WhatsApp శుభలేఖ</span>
                  </button>
                </div>

                <!-- Stats Grid -->
                <div class="grid grid-cols-3 gap-2 text-center text-xs">
                  <div class="p-2.5 rounded-2xl bg-vault-cream border border-vault-border">
                    <span class="text-[9px] text-stone-500 block">ఆహ్వానించినవి</span>
                    <span class="font-bold text-stone-900 text-sm font-cinzel">150</span>
                  </div>
                  <div class="p-2.5 rounded-2xl bg-jade-50 border border-jade-100">
                    <span class="text-[9px] text-jade-700 block">ధ్రువీకరించినవి</span>
                    <span class="font-bold text-jade-800 text-sm font-cinzel">118</span>
                  </div>
                  <div class="p-2.5 rounded-2xl bg-byzantine-50 border border-byzantine-200">
                    <span class="text-[9px] text-byzantine-900 block">చదివించినవారు</span>
                    <span class="font-bold text-byzantine-800 text-sm font-cinzel">18</span>
                  </div>
                </div>

                <!-- Digital Wedding Invitation Card Preview -->
                <div class="p-4 rounded-2xl bg-radial from-vermilion-900 via-vault-dark to-black text-white border border-byzantine-500/40 text-center space-y-1.5 shadow-lg">
                  <span class="text-[9px] text-byzantine-300 font-bold uppercase tracking-widest block font-telugu-title">॥ శుభలేఖ ॥</span>
                  <h4 class="font-bold text-byzantine-200 text-xs font-telugu-title">ఆనంద్ & శ్రేయ వివాహ మహోత్సవం</h4>
                  <p class="text-[10px] text-stone-300">తేదీ: 15 నవంబర్ 2026 • శ్రీ కన్వెన్షన్, హైదరాబాద్</p>
                  <p class="text-[9px] text-stone-400">మీ అమూల్యమైన కుటుంబ సమేత రాకను కోరుకుంటున్నాము.</p>
                </div>

                <div id="invites-guest-list" class="space-y-1.5 text-xs">
                  <!-- Rendered via JS -->
                </div>

              </div>

            </div>

            <!-- ======================================================= -->
            <!-- SUB-TAB 7: UPI QR & LIVE SOUNDBOX -->
            <!-- ======================================================= -->
            <div id="subtab-qr" class="app-screen space-y-3 text-center">
              
              <div class="spotlight-card p-4 space-y-3">
                <div>
                  <h3 class="font-bold text-vault-dark text-sm font-telugu-title">📲 డిజిటల్ శుభ శగున్ QR & సౌండ్‌బాక్స్</h3>
                  <p class="text-xs text-stone-500">Google Pay, PhonePe, Paytm ద్వారా నేరుగా బ్యాంక్ ఖాతాకు</p>
                </div>

                <!-- Royal Byzantine Gold Framed QR -->
                <div class="p-3 bg-gradient-to-b from-byzantine-100 to-amber-50 rounded-2xl border-2 border-byzantine-500 inline-block shadow-inner">
                  <div class="w-44 h-44 bg-white rounded-xl p-2.5 flex flex-col items-center justify-center border border-vault-border shadow-xs mx-auto">
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=upi://pay?pa=giftvault.treasury@icici%26pn=AnandWedding%26cu=INR" alt="GiftVault Shagun QR" class="w-36 h-36">
                    <span class="text-[8px] font-bold text-stone-500 mt-1">UPI ID: giftvault.treasury@icici</span>
                  </div>
                </div>

                <!-- Live Voice Soundbox -->
                <div class="p-3.5 rounded-2xl bg-vault-dark text-white space-y-2 text-left border border-byzantine-500/30">
                  <div class="flex items-center justify-between">
                    <span class="text-[10px] text-byzantine-400 font-bold uppercase tracking-wider">🔊 స్మార్ట్ సౌండ్‌బాక్స్ అనౌన్స్‌మెంట్:</span>
                    <span class="w-2 h-2 rounded-full bg-jade-400 animate-ping"></span>
                  </div>
                  <p id="qr-soundbox-live" class="text-xs text-byzantine-200 font-semibold font-telugu-title">
                    "📢 ఫోన్‌పే ద్వారా శ్రీ యలమంచిలి రాజశేఖర్ గారి నుంచి ₹2,116 రూపాయలు ప్రాప్తించినవి!"
                  </p>
                  <button onclick="simulateUpiSoundbox()" class="w-full py-1.5 rounded-xl gold-foil-bg text-vault-dark font-bold text-xs flex items-center justify-center gap-1 shadow-glow-sm btn-tactile">
                    <span>🔔</span>
                    <span>టెస్ట్ సౌండ్‌బాక్స్ వాయిస్ బీప్</span>
                  </button>
                </div>

                <!-- Charity Option -->
                <div class="p-3 rounded-2xl bg-amber-50 border border-amber-200 text-left text-xs space-y-1">
                  <span class="text-amber-900 font-bold block">🕊️ అన్నదానం / స్వచ్ఛంద సేవా ఎంపిక:</span>
                  <p class="text-[10px] text-amber-800 leading-relaxed">
                    కానుకలకు బదులుగా అన్నదానం లేదా ట్రస్ట్‌కు విరాళం ఇవ్వాలనుకునే అతిథుల కోసం ప్రత్యేక చారిటీ లింక్ జోడించబడింది.
                  </p>
                </div>

              </div>

            </div>

          </div>

        </div>

        <!-- Native 5-Tab Bottom Dock (Android Flagship Feel) -->
        <div id="mobile-bottom-dock" class="h-14 bg-white border-t border-vault-border grid grid-cols-5 items-center px-1 z-30 flex-shrink-0 shadow-lg">
          <button onclick="switchAppTab('dashboard')" class="flex flex-col items-center py-1 text-vault-dark btn-tactile">
            <svg class="w-4 h-4 text-byzantine-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            <span class="text-[9px] font-bold mt-0.5">హోమ్</span>
          </button>
          <button onclick="switchAppTab('desk')" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900 btn-tactile">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
            <span class="text-[9px] font-bold mt-0.5">డెస్క్</span>
          </button>
          <button onclick="switchAppTab('ledger')" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900 btn-tactile">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path></svg>
            <span class="text-[9px] font-bold mt-0.5">లెడ్జర్</span>
          </button>
          <button onclick="switchAppTab('expenses')" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900 btn-tactile">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"></path><path d="M12 18V6"></path></svg>
            <span class="text-[9px] font-bold mt-0.5">ఖర్చులు</span>
          </button>
          <button onclick="switchAppTab('qr')" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900 btn-tactile">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"></rect><rect width="4" height="4" x="7" y="7"></rect></svg>
            <span class="text-[9px] font-bold mt-0.5">QR పే</span>
          </button>
        </div>

        <!-- Android Gesture Bar -->
        <div id="mobile-gesture-bar" class="h-3.5 bg-white flex items-center justify-center flex-shrink-0">
          <div class="w-24 h-1 bg-stone-300 rounded-full"></div>
        </div>

      </div>
    </div>

  </main>

  <!-- ============================================================== -->
  <!-- 3. DYNAMIC EVENT CREATOR MODAL -->
  <!-- ============================================================== -->
  <div id="modal-new-event" class="fixed inset-0 bg-vault-dark/70 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4 overflow-y-auto">
    <div class="spotlight-card rounded-3xl max-w-lg w-full p-5 space-y-3.5 my-8 shadow-2xl border border-byzantine-500/30">
      
      <div class="flex items-center justify-between border-b border-vault-border/60 pb-2.5">
        <div>
          <h3 class="font-bold text-vault-dark text-sm font-telugu-title">కొత్త శుభకార్యాన్ని జోడించండి</h3>
          <p class="text-[10px] text-stone-500">కేటగిరీ ఎంచుకోగానే వివరాల ఫారమ్ ఆటోమేటిక్ గా సర్దుబాటు అవుతుంది</p>
        </div>
        <button onclick="closeModalNewEvent()" class="text-stone-400 hover:text-stone-700 font-bold text-base btn-tactile">✕</button>
      </div>

      <!-- Quick Occasion Category Suggestions -->
      <div>
        <label class="block text-[10px] font-bold text-stone-700 mb-1">త్వరిత కేటగిరీ సజెషన్స్:</label>
        <div class="flex flex-wrap gap-1">
          <button type="button" onclick="selectCategorySuggestion('wedding', 'వివాహ మహోత్సవం')" class="h-5 px-2 text-[9px] font-bold rounded-md bg-byzantine-50 text-byzantine-900 border border-byzantine-300 btn-tactile">💍 వివాహం</button>
          <button type="button" onclick="selectCategorySuggestion('halfsaree', 'శ్రీమతి లంగా ఓణీల శుభవేడుక')" class="h-5 px-2 text-[9px] font-bold rounded-md bg-vault-cream text-stone-800 border border-vault-border btn-tactile">👗 లంగా ఓణీలు</button>
          <button type="button" onclick="selectCategorySuggestion('odugu', 'చిరంజీవి ఒడుగు / ఉపనయన మహోత్సవం')" class="h-5 px-2 text-[9px] font-bold rounded-md bg-vault-cream text-stone-800 border border-vault-border btn-tactile">🪔 ఒడుగు</button>
          <button type="button" onclick="selectCategorySuggestion('panchala', 'పంచల శుభవేడుక (Dhoti Ceremony)')" class="h-5 px-2 text-[9px] font-bold rounded-md bg-vault-cream text-stone-800 border border-vault-border btn-tactile">👔 పంచల వేడుక</button>
          <button type="button" onclick="selectCategorySuggestion('pushpavathi', 'పుష్పవతి / పుష్పాలంకరణ వేడుక')" class="h-5 px-2 text-[9px] font-bold rounded-md bg-vault-cream text-stone-800 border border-vault-border btn-tactile">🌸 పుష్పవతి</button>
          <button type="button" onclick="selectCategorySuggestion('naming', 'నామకరణం & బారసాల మహోత్సవం')" class="h-5 px-2 text-[9px] font-bold rounded-md bg-vault-cream text-stone-800 border border-vault-border btn-tactile">👶 బారసాల</button>
          <button type="button" onclick="selectCategorySuggestion('housewarming', 'నూతన గృహప్రవేశ మహోత్సవం')" class="h-5 px-2 text-[9px] font-bold rounded-md bg-vault-cream text-stone-800 border border-vault-border btn-tactile">🏡 గృహప్రవేశం</button>
        </div>
      </div>

      <form id="form-new-event" onsubmit="handleCreateEvent(event)" class="space-y-3 text-xs">
        
        <div>
          <label class="block text-[10px] font-bold text-stone-700 mb-0.5">శుభకార్యం కేటగిరీ:</label>
          <select id="event-select-cat" onchange="onCategoryChanged(this.value)" class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl focus:outline-none">
            <option value="wedding">వివాహం (Wedding - వధూవరులు)</option>
            <option value="halfsaree">లంగా ఓణీల వేడుక (Half Saree - అమ్మాయి మాత్రమే)</option>
            <option value="odugu">ఒడుగు / ఉపనయనం (Upanayanam - వటువు మాత్రమే)</option>
            <option value="panchala">పంచల వేడుక (Dhoti Ceremony - అబ్బాయి మాత్రమే)</option>
            <option value="pushpavathi">పుష్పవతి / పుష్పాలంకరణ (Girl Ceremony)</option>
            <option value="naming">బారసాల & నామకరణం (Naming - బాబు/పాప & తల్లిదండ్రులు)</option>
            <option value="birthday">పుట్టినరోజు వేడుక (Birthday)</option>
            <option value="housewarming">గృహప్రవేశం (Housewarming - గృహ నామం & యజమానులు)</option>
          </select>
        </div>

        <div>
          <label class="block text-[10px] font-bold text-stone-700 mb-0.5">ఈవెంట్ శీర్షిక / పేరు:</label>
          <input id="event-input-title" type="text" required placeholder="ఆనంద్ & శ్రేయ వివాహ మహోత్సవం" class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl focus:outline-none focus:border-byzantine-500">
        </div>

        <!-- DYNAMIC PARTICIPANT FIELDS -->
        <div id="dynamic-participant-fields" class="p-3 rounded-2xl bg-byzantine-50/70 border border-byzantine-200 space-y-2">
          <!-- Populated dynamically via JS onCategoryChanged -->
        </div>

        <!-- Date & Venue -->
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block text-[10px] font-bold text-stone-700 mb-0.5">తేదీ:</label>
            <input id="event-input-date" type="date" required class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl">
          </div>
          <div>
            <label class="block text-[10px] font-bold text-stone-700 mb-0.5">కళ్యాణ మండపం / వేదిక:</label>
            <input id="event-input-venue" type="text" required placeholder="శ్రీ కన్వెన్షన్ హాల్" class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl">
          </div>
        </div>

        <!-- CITY AUTOCOMPLETE -->
        <div class="grid grid-cols-3 gap-2">
          <div class="relative col-span-1">
            <label class="block text-[10px] font-bold text-stone-700 mb-0.5">ఊరు / సిటీ:</label>
            <input id="event-input-city" type="text" required oninput="onEventCityInput(this.value)" placeholder="హైదరాబాద్..." class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl">
            <div id="event-city-suggestions" class="absolute left-0 right-0 top-full mt-1 bg-white border border-vault-border rounded-xl shadow-lg z-30 hidden max-h-36 overflow-y-auto"></div>
          </div>
          <div>
            <label class="block text-[10px] font-bold text-stone-700 mb-0.5">రాష్ట్రం:</label>
            <input id="event-input-state" type="text" readonly value="తెలంగాణ" class="w-full h-8 px-2 text-xs bg-stone-100 border border-vault-border rounded-xl text-stone-600">
          </div>
          <div>
            <label class="block text-[10px] font-bold text-stone-700 mb-0.5">పిన్‌కోడ్:</label>
            <input id="event-input-pincode" type="text" placeholder="500001" class="w-full h-8 px-2 text-xs bg-vault-cream border border-vault-border rounded-xl">
          </div>
        </div>

        <div class="pt-2 flex justify-end gap-2">
          <button type="button" onclick="closeModalNewEvent()" class="px-3.5 py-1.5 rounded-xl border border-vault-border text-stone-600 font-bold text-xs btn-tactile">రద్దు</button>
          <button type="submit" class="px-4 py-1.5 rounded-xl bg-vault-dark text-byzantine-400 font-bold text-xs shadow-sm border border-byzantine-500/30 btn-tactile">ఈవెంట్‌ను సృష్టించండి</button>
        </div>

      </form>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- 4. ADD EXPENSE MODAL -->
  <!-- ============================================================== -->
  <div id="modal-add-expense" class="fixed inset-0 bg-vault-dark/70 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="spotlight-card rounded-3xl max-w-sm w-full p-4 space-y-3 shadow-2xl border border-byzantine-500/30">
      <div class="flex items-center justify-between border-b border-vault-border/60 pb-2">
        <h3 class="font-bold text-xs text-vault-dark font-telugu-title">💸 ఈవెంట్ ఖర్చు నమోదు</h3>
        <button onclick="closeModalAddExpense()" class="text-stone-400 hover:text-stone-700 font-bold btn-tactile">✕</button>
      </div>

      <form id="form-add-expense" onsubmit="handleAddExpense(event)" class="space-y-2.5 text-xs">
        <div>
          <label class="block text-[10px] font-bold text-stone-700 mb-0.5">ఖర్చు వర్గం (Category):</label>
          <select id="exp-category" class="w-full h-8 px-2 text-xs bg-vault-cream border border-vault-border rounded-xl focus:outline-none">
            <option value="కళ్యాణ మండపం & హాల్ అద్దె">కళ్యాణ మండపం & హాల్ అద్దె</option>
            <option value="క్యాటరింగ్ & భోజనాలు">క్యాటరింగ్ & భోజనాలు</option>
            <option value="ఫోటోగ్రఫీ & వీడియో">ఫోటోగ్రఫీ & వీడియో</option>
            <option value="పూల డెకరేషన్ & లైటింగ్">పూల డెకరేషన్ & లైటింగ్</option>
            <option value="వస్త్రాలు & బంగారం కానుకలు">వస్త్రాలు & బంగారం కానుకలు</option>
            <option value="పూజారులు & బాజా భజంత్రీలు">పూజారులు & బాజా భజంత్రీలు</option>
            <option value="రవాణా & ఇతర ఖర్చులు">రవాణా & ఇతర ఖర్చులు</option>
          </select>
        </div>

        <div>
          <label class="block text-[10px] font-bold text-stone-700 mb-0.5">వివరాలు / ఎవరికి చెల్లించారు:</label>
          <input id="exp-paidto" type="text" required placeholder="శ్రీనివాస క్యాటరర్స్ అడ్వాన్స్" class="w-full h-8 px-2.5 text-xs bg-vault-cream border border-vault-border rounded-xl">
        </div>

        <div>
          <label class="block text-[10px] font-bold text-stone-700 mb-0.5">మొత్తం (₹):</label>
          <input id="exp-amount" type="number" required placeholder="50000" class="w-full h-8 px-2.5 text-xs font-bold text-vermilion-700 bg-vermilion-50 border border-vermilion-200 rounded-xl">
        </div>

        <div class="pt-2 flex justify-end gap-2">
          <button type="button" onclick="closeModalAddExpense()" class="px-3.5 py-1.5 rounded-xl border border-vault-border text-stone-600 font-bold text-xs btn-tactile">రద్దు</button>
          <button type="submit" class="px-4 py-1.5 rounded-xl bg-vermilion-700 text-white font-bold text-xs shadow-sm btn-tactile">ఖర్చు జోడించు</button>
        </div>
      </form>
    </div>
  </div>

  <!-- Audio Chime Generator for Soundbox (Temple Bell Web Audio API) -->
  <script>
    function playTempleChime() {
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(587.33, audioCtx.currentTime); // D5
        osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.3);
        gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 1.2);
        osc.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 1.2);
      } catch(e) {
        console.log("Audio ctx init error", e);
      }
    }
  </script>

  <!-- ============================================================== -->
  <!-- 5. JAVASCRIPT STATE ENGINE & INTERACTIVE LOGIC -->
  <!-- ============================================================== -->
  <script>
    const AP_TG_CITIES = [
      { name: "హైదరాబాద్ (Hyderabad)", state: "తెలంగాణ", pin: "500001" },
      { name: "విశాఖపట్నం (Visakhapatnam)", state: "ఆంధ్రప్రదేశ్", pin: "530001" },
      { name: "విజయవాడ (Vijayawada)", state: "ఆంధ్రప్రదేశ్", pin: "520001" },
      { name: "గుంటూరు (Guntur)", state: "ఆంధ్రప్రదేశ్", pin: "522002" },
      { name: "వరంగల్ (Warangal)", state: "తెలంగాణ", pin: "506001" },
      { name: "రాజమండ్రి (Rajahmundry)", state: "ఆంధ్రప్రదేశ్", pin: "533101" },
      { name: "తిరుపతి (Tirupati)", state: "ఆంధ్రప్రదేశ్", pin: "517501" },
      { name: "నెల్లూరు (Nellore)", state: "ఆంధ్రప్రదేశ్", pin: "524001" },
      { name: "కర్నూలు (Kurnool)", state: "ఆంధ్రప్రదేశ్", pin: "518001" },
      { name: "కరీంనగర్ (Karimnagar)", state: "తెలంగాణ", pin: "505001" },
      { name: "ఖమ్మం (Khammam)", state: "తెలంగాణ", pin: "507001" },
      { name: "నిజామాబాద్ (Nizamabad)", state: "తెలంగాణ", pin: "503001" },
      { name: "కడప (Kadapa)", state: "ఆంధ్రప్రదేశ్", pin: "516001" },
      { name: "కాకినాడ (Kakinada)", state: "ఆంధ్రప్రదేశ్", pin: "533001" },
      { name: "అనంతపురం (Anantapur)", state: "ఆంధ్రప్రదేశ్", pin: "515001" }
    ];

    const state = {
      currentLang: 'te',
      currentDeviceMode: 'mobile',
      activeCounter: 'వరుడి వైపు కౌంటర్ (Groom Desk)',
      activeDeskGiftType: 'cash',
      activeEvent: {
        id: 'ev-1',
        title: 'ఆనంద్ & శ్రేయ వివాహ మహోత్సవం',
        category: 'wedding',
        date: '2026-11-15',
        venue: 'శ్రీ కన్వెన్షన్, హైదరాబాద్',
        city: 'హైదరాబాద్',
        state: 'తెలంగాణ',
        budget: 600000
      },
      entries: [
        {
          id: 'ent-1',
          name: 'కొత్తపల్లి శ్రీనివాసరావు',
          city: 'గుంటూరు',
          relation: 'మేనమామ తరఫు',
          giftType: 'నగదు',
          amount: 5116,
          metalInfo: '',
          phone: '9848012345',
          counter: 'వరుడి వైపు కౌంటర్',
          cover: 'కవరు #01',
          time: '10:15 AM'
        },
        {
          id: 'ent-2',
          name: 'యలమంచిలి రాజశేఖర్',
          city: 'విజయవాడ',
          relation: 'బావ / బావమరిది',
          giftType: 'నగదు',
          amount: 2116,
          metalInfo: '',
          phone: '9848023456',
          counter: 'వరుడి వైపు కౌంటర్',
          cover: 'కవరు #02',
          time: '10:22 AM'
        },
        {
          id: 'ent-3',
          name: 'రాఘవరాజు మురళీకృష్ణ',
          city: 'హైదరాబాద్',
          relation: 'పెద్దనాన్న తరఫు',
          giftType: 'బంగారం',
          amount: 0,
          metalInfo: '🪙 1 తులం బంగారు గొలుసు (10 గ్రాములు)',
          phone: '9848034567',
          counter: 'వధువు వైపు కౌంటర్',
          cover: 'బాక్స్ #A1',
          time: '10:30 AM'
        },
        {
          id: 'ent-4',
          name: 'డా. కావూరి సుబ్బారావు',
          city: 'విశాఖపట్నం',
          relation: 'తాతయ్య తరఫు',
          giftType: 'వెండి',
          amount: 0,
          metalInfo: '🥈 100 గ్రాముల వెండి దీపపు కుందులు',
          phone: '9848045678',
          counter: 'వధువు వైపు కౌంటర్',
          cover: 'బాక్స్ #B2',
          time: '10:45 AM'
        },
        {
          id: 'ent-5',
          name: 'పొట్లూరి సాయికుమార్',
          city: 'వరంగల్',
          relation: 'మిత్రులు (Friends)',
          giftType: 'నగదు',
          amount: 1116,
          metalInfo: '',
          phone: '9848056789',
          counter: 'వరుడి వైపు కౌంటర్',
          cover: 'కవరు #05',
          time: '11:00 AM'
        }
      ],
      expenses: [
        { id: 'exp-1', category: 'కళ్యాణ మండపం & హాల్ అద్దె', paidTo: 'శ్రీ కన్వెన్షన్ హాల్ మేనేజర్', amount: 250000, date: '2026-11-10' },
        { id: 'exp-2', category: 'క్యాటరింగ్ & భోజనాలు', paidTo: 'అన్నపూర్ణ క్యాటరింగ్ సర్వీసెస్', amount: 180000, date: '2026-11-14' },
        { id: 'exp-3', category: 'పూల డెకరేషన్ & లైటింగ్', paidTo: 'రాయల్ ఫ్లవర్ డెకరేటర్స్', amount: 65000, date: '2026-11-14' },
        { id: 'exp-4', category: 'పూజారులు & బాజా భజంత్రీలు', paidTo: 'వేదపండితులు & మంగళవాయిద్యం', amount: 45000, date: '2026-11-15' }
      ],
      reciprocity: [
        { name: 'కొత్తపల్లి శ్రీనివాసరావు (గుంటూరు)', relation: 'మేనమామ', weGavePast: 5116, theyGaveToday: 5116, status: 'సరితూగింది (Balanced)' },
        { name: 'యలమంచిలి రాజశేఖర్ (విజయవాడ)', relation: 'బావ', weGavePast: 1116, theyGaveToday: 2116, status: 'వారి కానుక అధికం (+₹1,000)' },
        { name: 'చలసాని రమేష్ బాబు (తెనాలి)', relation: 'స్నేహితుడు', weGavePast: 2116, theyGaveToday: 0, status: 'ఇంకా రాలేదు (Pending)' }
      ],
      guests: [
        { name: 'కొత్తపల్లి శ్రీనివాసరావు', city: 'గుంటూరు', rsvp: 'హాజరయ్యారు ✓', phone: '9848012345' },
        { name: 'యలమంచిలి రాజశేఖర్', city: 'విజయవాడ', rsvp: 'హాజరయ్యారు ✓', phone: '9848023456' },
        { name: 'రాఘవరాజు మురళీకృష్ణ', city: 'హైదరాబాద్', rsvp: 'హాజరయ్యారు ✓', phone: '9848034567' },
        { name: 'నండూరి ప్రసాద్', city: 'రాజమండ్రి', rsvp: 'ధ్రువీకరించారు (Coming)', phone: '9848099999' }
      ]
    };

    function setDeviceViewMode(mode) {
      state.currentDeviceMode = mode;
      const wrapper = document.getElementById('main-viewport-wrapper');
      const screen = document.getElementById('main-viewport-screen');
      const statusBar = document.getElementById('mobile-status-bar');
      const bottomDock = document.getElementById('mobile-bottom-dock');
      const gestureBar = document.getElementById('mobile-gesture-bar');
      const btnMob = document.getElementById('toggle-device-mobile');
      const btnDesk = document.getElementById('toggle-device-desktop');

      if (mode === 'mobile') {
        wrapper.className = "phone-chassis";
        screen.className = "phone-screen";
        statusBar.classList.remove('hidden');
        bottomDock.classList.remove('hidden');
        gestureBar.classList.remove('hidden');

        btnMob.className = "px-3.5 py-1.5 rounded-lg bg-vault-dark text-white shadow-xs transition-all flex items-center gap-1.5 btn-tactile";
        btnDesk.className = "px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all flex items-center gap-1.5 btn-tactile";
      } else {
        wrapper.className = "desktop-viewport";
        screen.className = "phone-screen";
        statusBar.classList.add('hidden');
        bottomDock.classList.add('hidden');
        gestureBar.classList.add('hidden');

        btnDesk.className = "px-3.5 py-1.5 rounded-lg bg-vault-dark text-white shadow-xs transition-all flex items-center gap-1.5 btn-tactile";
        btnMob.className = "px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all flex items-center gap-1.5 btn-tactile";
      }
    }

    function navigateToPage(pageId) {
      document.querySelectorAll('.page-section').forEach(el => el.classList.remove('active-page'));
      const target = document.getElementById(`page-${pageId}`);
      if (target) {
        target.classList.add('active-page');
        document.getElementById('screen-scroll-container').scrollTop = 0;
      }
    }

    function switchAppTab(tabName) {
      document.querySelectorAll('.app-screen').forEach(s => s.classList.remove('active-app-screen'));
      const target = document.getElementById(`subtab-${tabName}`);
      if (target) target.classList.add('active-app-screen');

      ['dashboard', 'desk', 'ledger', 'expenses', 'reciprocity', 'invites', 'qr'].forEach(t => {
        const btn = document.getElementById(`navtab-${t}`);
        if (btn) {
          if (t === tabName) {
            btn.className = "px-3 py-1.5 rounded-xl bg-vault-dark text-byzantine-400 border border-byzantine-500/40 shrink-0 btn-tactile";
          } else {
            btn.className = "px-3 py-1.5 rounded-xl bg-white text-stone-700 hover:bg-stone-100 border border-vault-border shrink-0 btn-tactile";
          }
        }
      });

      if (tabName === 'desk') {
        setTimeout(() => {
          const inp = document.getElementById('desk-input-name');
          if (inp) inp.focus();
        }, 100);
      }
    }

    function onCounterChanged(counterName) {
      state.activeCounter = counterName;
    }

    function setDeskGiftType(type) {
      state.activeDeskGiftType = type;
      ['cash', 'gold', 'silver', 'item'].forEach(t => {
        const b = document.getElementById(`btn-gifttype-${t}`);
        if (b) {
          if (t === type) {
            b.className = "py-1 rounded-xl bg-vault-dark text-byzantine-400 border border-byzantine-500/40 btn-tactile";
          } else {
            b.className = "py-1 rounded-xl bg-white text-stone-700 border border-vault-border btn-tactile";
          }
        }
      });

      const cashSec = document.getElementById('desk-cash-section');
      const metalSec = document.getElementById('desk-precious-section');
      if (type === 'cash') {
        cashSec.classList.remove('hidden');
        metalSec.classList.add('hidden');
      } else {
        cashSec.classList.add('hidden');
        metalSec.classList.remove('hidden');
        document.getElementById('desk-input-metal-desc').placeholder = 
          type === 'gold' ? 'ఉదా: బంగారు ఉంగరం / గొలుసు' : 
          type === 'silver' ? 'ఉదా: వెండి కుందులు / కలశం' : 'ఉదా: పట్టుచీర / వాషింగ్ మెషీన్';
      }
    }

    function setDeskQuickAmount(amt) {
      const isLucky = document.getElementById('desk-check-luckyone').checked;
      const finalAmt = isLucky && (amt % 10 === 0) ? amt + 1 : amt;
      document.getElementById('desk-input-amount').value = finalAmt;
    }

    function toggleLuckyCoin(checked) {
      const inp = document.getElementById('desk-input-amount');
      let val = parseInt(inp.value) || 0;
      if (checked) {
        if (val > 0 && val % 10 === 0) inp.value = val + 1;
      } else {
        if (val > 0 && val % 10 === 1) inp.value = val - 1;
      }
    }

    function submitDeskEntry(sendWhatsApp) {
      const name = document.getElementById('desk-input-name').value.trim();
      const city = document.getElementById('desk-input-city').value.trim() || 'హైదరాబాద్';
      const relation = document.getElementById('desk-select-relation').value;
      const phone = document.getElementById('desk-input-phone').value.trim();
      const cover = document.getElementById('desk-input-cover').value.trim() || 'కవరు';
      const notes = document.getElementById('desk-input-notes').value.trim();
      
      let amount = 0;
      let metalInfo = '';

      if (state.activeDeskGiftType === 'cash') {
        amount = parseInt(document.getElementById('desk-input-amount').value) || 1116;
      } else {
        const weight = document.getElementById('desk-input-metal-weight').value.trim();
        const desc = document.getElementById('desk-input-metal-desc').value.trim() || 'కానుక';
        metalInfo = `${state.activeDeskGiftType === 'gold' ? '🪙' : state.activeDeskGiftType === 'silver' ? '🥈' : '🎁'} ${desc} (${weight})`;
      }

      if (!name) {
        alert("దయచేసి అతిథి లేదా బంధువు పేరు నమోదు చేయండి.");
        return;
      }

      const newEntry = {
        id: 'ent-' + Date.now(),
        name,
        city,
        relation,
        giftType: state.activeDeskGiftType === 'cash' ? 'నగదు' : state.activeDeskGiftType === 'gold' ? 'బంగారం' : state.activeDeskGiftType === 'silver' ? 'వెండి' : 'వస్తువు',
        amount,
        metalInfo,
        phone,
        counter: state.activeCounter,
        cover,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };

      state.entries.unshift(newEntry);
      playTempleChime();
      renderAllDynamicSections();

      if (sendWhatsApp && phone) {
        sendWhatsAppReceipt(newEntry);
      } else {
        alert(`✅ చదివింపు నమోదైంది: ${name} (${amount ? '₹' + amount : metalInfo})`);
      }

      document.getElementById('desk-input-name').value = '';
      document.getElementById('desk-input-amount').value = '';
      document.getElementById('desk-input-phone').value = '';
      document.getElementById('desk-input-metal-weight').value = '';
      document.getElementById('desk-input-metal-desc').value = '';
    }

    function sendWhatsAppReceipt(entry) {
      const giftText = entry.amount ? `₹${entry.amount}/-` : entry.metalInfo;
      const message = `శ్రీ/శ్రీమతి ${entry.name} గారికి నమస్కారములు.\n\nమా "${state.activeEvent.title}" శుభకార్యానికి విచ్చేసి, నూతన దంపతులను ఆశీర్వదించి మీ అమూల్యమైన చదివింపులు (${giftText}) సమర్పించినందుకు మా కుటుంబ సభ్యుల తరపున హృదయపూర్వక ధన్యవాదాలు! 🙏✨\n\n- ${state.activeEvent.title} కుటుంబం`;
      
      const cleanPhone = (entry.phone || '').replace(/[^0-9]/g, '');
      const waUrl = cleanPhone.length >= 10 
        ? `https://api.whatsapp.com/send?phone=91${cleanPhone.slice(-10)}&text=${encodeURIComponent(message)}`
        : `https://api.whatsapp.com/send?text=${encodeURIComponent(message)}`;

      window.open(waUrl, '_blank');
    }

    function shareDigitalInvite() {
      const inviteMsg = `॥ శ్రీరస్తు శుభమస్తు ॥\n\nమా కుటుంబంలో జరగబోవు "${state.activeEvent.title}" కు తామెల్లరూ సకుటుంబ సపరివార సమేతంగా విచ్చేసి, నూతన దంపతులను ఆశీర్వదించవలసిందిగా కోరుచున్నాము.\n\n📅 తేదీ: ${state.activeEvent.date}\n🏛️ వేదిక: ${state.activeEvent.venue}\n\nఆహ్వానించువారు:\nకుటుంబ సభ్యులు`;
      window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(inviteMsg)}`, '_blank');
    }

    function onCategoryChanged(cat) {
      const container = document.getElementById('dynamic-participant-fields');
      const titleInput = document.getElementById('event-input-title');

      if (cat === 'wedding') {
        titleInput.value = "ఆనంద్ & శ్రేయ వివాహ మహోత్సవం";
        container.innerHTML = `
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[10px] font-bold text-byzantine-900 mb-0.5">వరుడి పేరు (Groom):</label>
              <input type="text" value="చి. ఆనంద్ వర్మ" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
            </div>
            <div>
              <label class="block text-[10px] font-bold text-byzantine-900 mb-0.5">వధువు పేరు (Bride):</label>
              <input type="text" value="చి.ల.సౌ. శ్రేయ" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
            </div>
          </div>
        `;
      } else if (cat === 'halfsaree' || cat === 'pushpavathi') {
        titleInput.value = cat === 'halfsaree' ? "చి.ల.సౌ. తేజస్విని లంగా ఓణీల శుభవేడుక" : "పుష్పాలంకరణ మహోత్సవం";
        container.innerHTML = `
          <div class="space-y-1.5">
            <span class="text-[9px] font-bold text-byzantine-900 block">🌸 బాలిక / యువతి వివరాలు (Female Only):</span>
            <div class="grid grid-cols-2 gap-2">
              <div>
                <label class="block text-[10px] font-bold text-stone-700 mb-0.5">అమ్మాయి పేరు:</label>
                <input type="text" value="చి.ల.సౌ. తేజస్విని" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
              </div>
              <div>
                <label class="block text-[10px] font-bold text-stone-700 mb-0.5">తల్లిదండ్రుల పేర్లు:</label>
                <input type="text" placeholder="రాఘవరావు & ఉమాదేవి" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
              </div>
            </div>
          </div>
        `;
      } else if (cat === 'odugu' || cat === 'panchala') {
        titleInput.value = cat === 'odugu' ? "చిరంజీవి సిద్ధార్థ ఒడుగు / ఉపనయన మహోత్సవం" : "పంచల శుభవేడుక";
        container.innerHTML = `
          <div class="space-y-1.5">
            <span class="text-[9px] font-bold text-byzantine-900 block">🪔 వటువు / అబ్బాయి వివరాలు (Male Only):</span>
            <div class="grid grid-cols-2 gap-2">
              <div>
                <label class="block text-[10px] font-bold text-stone-700 mb-0.5">వటువు / అబ్బాయి పేరు:</label>
                <input type="text" value="చి. సిద్ధార్థ శర్మ" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
              </div>
              <div>
                <label class="block text-[10px] font-bold text-stone-700 mb-0.5">గోత్రం & తండ్రి పేరు:</label>
                <input type="text" placeholder="కౌండిన్యస గోత్రం • శ్రీనివాస్" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
              </div>
            </div>
          </div>
        `;
      } else if (cat === 'housewarming') {
        titleInput.value = "శ్రీ నిలయం నూతన గృహప్రవేశ మహోత్సవం";
        container.innerHTML = `
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[10px] font-bold text-byzantine-900 mb-0.5">గృహ నామం (House Name):</label>
              <input type="text" value="శ్రీ లక్ష్మీ నిలయం" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
            </div>
            <div>
              <label class="block text-[10px] font-bold text-byzantine-900 mb-0.5">గృహ యజమానులు:</label>
              <input type="text" placeholder="సురేష్ & సుజాత దంపతులు" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
            </div>
          </div>
        `;
      } else {
        titleInput.value = "నామకరణం & బారసాల మహోత్సవం";
        container.innerHTML = `
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[10px] font-bold text-byzantine-900 mb-0.5">శిశువు పేరు / జెండర్:</label>
              <input type="text" placeholder="చిరునామధేయం (బాబు/పాప)" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
            </div>
            <div>
              <label class="block text-[10px] font-bold text-byzantine-900 mb-0.5">తల్లిదండ్రుల పేర్లు:</label>
              <input type="text" placeholder="సతీష్ & మాధవి" class="w-full h-8 px-2 text-xs bg-white border border-byzantine-300 rounded-xl">
            </div>
          </div>
        `;
      }
    }

    function selectCategorySuggestion(catKey, defaultTitle) {
      document.getElementById('event-select-cat').value = catKey;
      onCategoryChanged(catKey);
    }

    function onDeskCityInput(query) {
      const box = document.getElementById('desk-city-suggestions');
      if (!query.trim()) { box.classList.add('hidden'); return; }
      const matches = AP_TG_CITIES.filter(c => c.name.toLowerCase().includes(query.toLowerCase()));
      if (matches.length === 0) { box.classList.add('hidden'); return; }
      box.innerHTML = matches.map(c => `
        <div onclick="selectDeskCity('${c.name.split(' ')[0]}')" class="px-2.5 py-1.5 hover:bg-byzantine-50 cursor-pointer text-xs border-b border-vault-border flex justify-between">
          <span class="font-bold text-stone-800">${c.name}</span>
          <span class="text-[10px] text-stone-400">${c.state}</span>
        </div>
      `).join('');
      box.classList.remove('hidden');
    }

    function selectDeskCity(cityName) {
      document.getElementById('desk-input-city').value = cityName;
      document.getElementById('desk-city-suggestions').classList.add('hidden');
    }

    function onEventCityInput(query) {
      const box = document.getElementById('event-city-suggestions');
      if (!query.trim()) { box.classList.add('hidden'); return; }
      const matches = AP_TG_CITIES.filter(c => c.name.toLowerCase().includes(query.toLowerCase()));
      if (matches.length === 0) { box.classList.add('hidden'); return; }
      box.innerHTML = matches.map(c => `
        <div onclick="selectEventCity('${c.name.split(' ')[0]}', '${c.state}', '${c.pin}')" class="px-2.5 py-1.5 hover:bg-byzantine-50 cursor-pointer text-xs border-b border-vault-border flex justify-between">
          <span class="font-bold text-stone-800">${c.name}</span>
          <span class="text-[10px] text-stone-400">${c.pin}</span>
        </div>
      `).join('');
      box.classList.remove('hidden');
    }

    function selectEventCity(city, stateName, pin) {
      document.getElementById('event-input-city').value = city;
      document.getElementById('event-input-state').value = stateName;
      document.getElementById('event-input-pincode').value = pin;
      document.getElementById('event-city-suggestions').classList.add('hidden');
    }

    function setLedgerView(mode) {
      const tableDiv = document.getElementById('ledger-container-table');
      const bookDiv = document.getElementById('ledger-container-book');
      const btnTable = document.getElementById('btn-ledger-view-table');
      const btnBook = document.getElementById('btn-ledger-view-book');

      if (mode === 'table') {
        tableDiv.classList.remove('hidden');
        bookDiv.classList.add('hidden');
        btnTable.className = "px-3 py-1 rounded-lg bg-vault-dark text-white shadow-2xs btn-tactile";
        btnBook.className = "px-3 py-1 rounded-lg text-stone-600 hover:text-stone-900 btn-tactile";
      } else {
        tableDiv.classList.add('hidden');
        bookDiv.classList.remove('hidden');
        btnBook.className = "px-3 py-1 rounded-lg bg-vault-dark text-white shadow-2xs btn-tactile";
        btnTable.className = "px-3 py-1 rounded-lg text-stone-600 hover:text-stone-900 btn-tactile";
      }
    }

    function renderAllDynamicSections() {
      const totalCash = state.entries.reduce((sum, e) => sum + (e.amount || 0), 0);
      const totalExpenses = state.expenses.reduce((sum, e) => sum + (e.amount || 0), 0);
      const netBalance = totalCash - totalExpenses;

      document.getElementById('metric-total-received').innerText = '₹' + totalCash.toLocaleString('en-IN');
      document.getElementById('metric-total-expenses').innerText = '₹' + totalExpenses.toLocaleString('en-IN');
      document.getElementById('metric-net-balance').innerText = (netBalance >= 0 ? '+' : '') + '₹' + netBalance.toLocaleString('en-IN');
      document.getElementById('metric-received-count').innerText = `${state.entries.length} మంది బంధువులు`;

      // Recent Dashboard Stream
      document.getElementById('dashboard-recent-entries').innerHTML = state.entries.slice(0, 4).map(e => `
        <div class="flex items-center justify-between p-2.5 rounded-xl bg-vault-cream border border-vault-border">
          <div>
            <span class="font-bold text-vault-dark block">${e.name}</span>
            <span class="text-[10px] text-stone-500">${e.city} • ${e.relation}</span>
          </div>
          <div class="text-right">
            <span class="font-bold text-jade-800 text-xs font-cinzel">${e.amount ? '₹' + e.amount.toLocaleString('en-IN') : e.metalInfo}</span>
            <span class="text-[9px] text-stone-400 block">${e.time}</span>
          </div>
        </div>
      `).join('');

      // Table View
      document.getElementById('ledger-tbody-rows').innerHTML = state.entries.map((e, idx) => `
        <tr class="hover:bg-byzantine-50/40 transition-colors">
          <td class="p-2.5 font-bold text-stone-400 text-[10px]">${idx + 1}</td>
          <td class="p-2.5">
            <span class="font-bold text-vault-dark block">${e.name}</span>
            <span class="text-[10px] text-stone-500">${e.city} • ${e.cover || ''}</span>
          </td>
          <td class="p-2.5">
            <span class="text-stone-700 font-semibold block">${e.relation}</span>
            <span class="text-[9px] text-byzantine-800 bg-byzantine-50 px-1.5 py-0.2 rounded-md border border-byzantine-200 inline-block font-bold">${e.counter || 'కౌంటర్'}</span>
          </td>
          <td class="p-2.5 text-right">
            <span class="font-bold text-jade-800 text-xs font-cinzel">${e.amount ? '₹' + e.amount.toLocaleString('en-IN') : e.metalInfo}</span>
          </td>
          <td class="p-2.5 text-center space-x-1">
            <button onclick='sendWhatsAppReceipt(${JSON.stringify(e)})' title="WhatsApp రసీదు పంపు" class="p-1 rounded-md bg-jade-50 text-jade-700 hover:bg-jade-100 border border-jade-200 btn-tactile">
              💬
            </button>
            <button onclick="deleteEntry('${e.id}')" title="తొలగించు" class="p-1 rounded-md bg-vermilion-50 text-vermilion-700 hover:bg-vermilion-100 border border-vermilion-200 btn-tactile">
              🗑️
            </button>
          </td>
        </tr>
      `).join('');

      // Red Book Entries
      document.getElementById('ledger-book-entries').innerHTML = state.entries.map((e, idx) => `
        <div class="flex items-baseline justify-between border-b border-stone-200 pb-1 pt-0.5">
          <div class="flex items-baseline gap-2">
            <span class="font-bold text-stone-400 text-[10px] font-cinzel">${String(idx + 1).padStart(2, '0')}.</span>
            <div>
              <span class="font-bold text-vault-dark">${e.name}</span>
              <span class="text-[10px] text-stone-500">(${e.city} • ${e.relation})</span>
            </div>
          </div>
          <span class="font-bold text-jade-800 font-cinzel">${e.amount ? '₹' + e.amount.toLocaleString('en-IN') : e.metalInfo}</span>
        </div>
      `).join('');
      document.getElementById('book-page-total').innerText = '₹' + totalCash.toLocaleString('en-IN');

      // Expenses
      document.getElementById('expenses-category-list').innerHTML = state.expenses.map(exp => `
        <div class="flex items-center justify-between p-2.5 rounded-xl bg-vault-cream border border-vault-border">
          <div>
            <span class="font-bold text-stone-800 block">${exp.category}</span>
            <span class="text-[10px] text-stone-500">${exp.paidTo}</span>
          </div>
          <span class="font-bold text-vermilion-700 font-cinzel text-xs">₹${exp.amount.toLocaleString('en-IN')}</span>
        </div>
      `).join('');

      // Reciprocity
      document.getElementById('reciprocity-list').innerHTML = state.reciprocity.map(r => `
        <div class="p-3 rounded-2xl bg-vault-cream border border-vault-border space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-bold text-vault-dark">${r.name}</span>
            <span class="text-[9px] font-bold px-2 py-0.5 rounded-md bg-byzantine-100 text-byzantine-900">${r.status}</span>
          </div>
          <div class="flex items-center justify-between text-[11px] text-stone-600">
            <span>గతంలో మనం ఇచ్చింది: ₹${r.weGavePast}</span>
            <span class="font-bold text-jade-800">నేడు వారు ఇచ్చింది: ₹${r.theyGaveToday}</span>
          </div>
        </div>
      `).join('');

      // Invites
      document.getElementById('invites-guest-list').innerHTML = state.guests.map(g => `
        <div class="flex items-center justify-between p-2.5 rounded-xl bg-vault-cream border border-vault-border">
          <div>
            <span class="font-bold text-vault-dark block">${g.name}</span>
            <span class="text-[10px] text-stone-500">${g.city}</span>
          </div>
          <span class="px-2 py-0.5 rounded-md bg-jade-50 text-jade-800 border border-jade-100 text-[10px] font-bold">${g.rsvp}</span>
        </div>
      `).join('');
    }

    function deleteEntry(id) {
      const idx = state.entries.findIndex(e => e.id === id);
      if (idx !== -1) {
        state.entries.splice(idx, 1);
        renderAllDynamicSections();
      }
    }

    function openModalAddExpense() {
      document.getElementById('modal-add-expense').classList.remove('hidden');
    }
    function closeModalAddExpense() {
      document.getElementById('modal-add-expense').classList.add('hidden');
    }
    function handleAddExpense(e) {
      e.preventDefault();
      const cat = document.getElementById('exp-category').value;
      const paidTo = document.getElementById('exp-paidto').value.trim();
      const amt = parseInt(document.getElementById('exp-amount').value) || 0;
      if (amt <= 0) return;

      state.expenses.unshift({
        id: 'exp-' + Date.now(),
        category: cat,
        paidTo,
        amount: amt,
        date: new Date().toISOString().split('T')[0]
      });

      closeModalAddExpense();
      renderAllDynamicSections();
      alert(`✅ ఖర్చు నమోదైంది: ₹${amt}`);
    }

    function openModalNewEvent() {
      document.getElementById('modal-new-event').classList.remove('hidden');
      onCategoryChanged(document.getElementById('event-select-cat').value);
    }
    function closeModalNewEvent() {
      document.getElementById('modal-new-event').classList.add('hidden');
    }
    function handleCreateEvent(e) {
      e.preventDefault();
      const title = document.getElementById('event-input-title').value.trim();
      const date = document.getElementById('event-input-date').value;
      const venue = document.getElementById('event-input-venue').value.trim();
      const city = document.getElementById('event-input-city').value.trim() || 'హైదరాబాద్';

      state.activeEvent.title = title;
      state.activeEvent.date = date;
      state.activeEvent.venue = venue;
      state.activeEvent.city = city;

      document.getElementById('app-event-name').innerText = title;
      document.getElementById('app-event-meta').innerText = `${venue}, ${city} • ${date}`;

      closeModalNewEvent();
      alert(`🎉 శుభకార్యం సృష్టించబడింది: ${title}`);
    }

    function exportToCsv() {
      let csvContent = "data:text/csv;charset=utf-8,ID,Name,City,Relation,GiftType,Amount,Notes\\n";
      state.entries.forEach(e => {
        csvContent += `${e.id},"${e.name}","${e.city}","${e.relation}","${e.giftType}",${e.amount || 0},"${e.notes || ''}"\\n`;
      });
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", `GiftVault_${state.activeEvent.title}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function exportToPdf() { window.print(); }

    function simulateUpiSoundbox() {
      playTempleChime();
      document.getElementById('qr-soundbox-live').innerText = "📢 ఫోన్‌పే ద్వారా ₹2,116 రూపాయలు ప్రాప్తించినవి!";
    }

    function startClock() {
      setInterval(() => {
        const el = document.getElementById('android-clock');
        if (el) el.innerText = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
      }, 1000);
    }

    const I18N = {
      te: {
        badge_heritage: "రాయల్ ఇండియన్ & తెలుగు సంస్కృతి",
        hero_subtext: "Nyota, ShagunBook, DMoi కంటే 10 రెట్లు మెరుగ్గా — ఎర్ర పుస్తకం గౌరవం, ఖర్చుల ట్రాకర్, బంగారం-వెండి లెక్క, 1-క్లిక్ WhatsApp రసీదులు & రియల్-టైమ్ UPI సౌండ్‌బాక్స్!",
        btn_enter_treasury: "🚀 ఇప్పుడే ఉచితంగా ప్రారంభించండి",
        nav_home: "ల్యాండింగ్",
        nav_app: "ఖజానా ఓపెన్",
        btn_new_event: "కొత్త ఈవెంట్"
      },
      en: {
        badge_heritage: "Royal Indian & Telugu Heritage",
        hero_subtext: "10x Better than Nyota, ShagunBook & DMoi — Traditional Red Book, Event Expenses, Gold/Silver Tracking, 1-Click WhatsApp Receipts & Real-time UPI Soundbox!",
        btn_enter_treasury: "🚀 Start Free Treasury Now",
        nav_home: "Landing",
        nav_app: "Open Treasury",
        btn_new_event: "New Event"
      },
      hi: {
        badge_heritage: "भारतीय एवं तेलुगु सांस्कृतिक विरासत",
        hero_subtext: "Nyota और ShagunBook से 10 गुना बेहतर — लाल बहीखाता, खर्च ट्रैкер, सोना-चांदी का हिसाब, 1-क्लिक WhatsApp रसीदें और लाइव UPI साउंडबॉक्स!",
        btn_enter_treasury: "🚀 अभी नि:शुल्क शुरू करें",
        nav_home: "मुख्य पृष्ठ",
        nav_app: "खजाना खोलें",
        btn_new_event: "नया उत्सव"
      }
    };

    function onLanguageChanged(lang) {
      state.currentLang = lang;
      localStorage.setItem('giftvault_preferred_lang', lang);
      applyLanguage(lang);
    }

    function applyLanguage(lang) {
      const dict = I18N[lang] || I18N.te;
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) el.innerText = dict[key];
      });
      document.getElementById('lang-selector').value = lang;
    }

    function loginWithGoogleSim() {
      alert("✅ Google తో లాగిన్ విజయవంతమైంది! మీ ఖాతా సింక్ చేయబడింది.");
      navigateToPage('app');
    }

    function sendOtpSim() {
      const p = document.getElementById('auth-phone-input').value.trim();
      if (!p) { alert("దయచేసి మొబైల్ నెంబర్ నమోదు చేయండి"); return; }
      alert(`OTP 123456 మీ మొబైల్ ${p} కు పంపబడింది.`);
      setTimeout(() => { navigateToPage('app'); }, 500);
    }

    function enterAsGuest() { navigateToPage('app'); }

    function filterLedger() {
      const q = document.getElementById('ledger-search-input').value.toLowerCase();
      const type = document.getElementById('ledger-filter-type').value;

      const filtered = state.entries.filter(e => {
        const matchesQuery = e.name.toLowerCase().includes(q) || e.city.toLowerCase().includes(q) || e.relation.toLowerCase().includes(q);
        const matchesType = type === 'all' || e.giftType === type;
        return matchesQuery && matchesType;
      });

      document.getElementById('ledger-tbody-rows').innerHTML = filtered.map((e, idx) => `
        <tr class="hover:bg-byzantine-50/40 transition-colors">
          <td class="p-2.5 font-bold text-stone-400 text-[10px]">${idx + 1}</td>
          <td class="p-2.5">
            <span class="font-bold text-vault-dark block">${e.name}</span>
            <span class="text-[10px] text-stone-500">${e.city} • ${e.cover || ''}</span>
          </td>
          <td class="p-2.5">
            <span class="text-stone-700 font-semibold block">${e.relation}</span>
            <span class="text-[9px] text-byzantine-800 bg-byzantine-50 px-1.5 py-0.2 rounded-md border border-byzantine-200 inline-block font-bold">${e.counter || 'కౌంటర్'}</span>
          </td>
          <td class="p-2.5 text-right">
            <span class="font-bold text-jade-800 text-xs font-cinzel">${e.amount ? '₹' + e.amount.toLocaleString('en-IN') : e.metalInfo}</span>
          </td>
          <td class="p-2.5 text-center space-x-1">
            <button onclick='sendWhatsAppReceipt(${JSON.stringify(e)})' class="p-1 rounded-md bg-jade-50 text-jade-700 border border-jade-200 btn-tactile">💬</button>
            <button onclick="deleteEntry('${e.id}')" class="p-1 rounded-md bg-vermilion-50 text-vermilion-700 border border-vermilion-200 btn-tactile">🗑️</button>
          </td>
        </tr>
      `).join('');
    }

    window.addEventListener('DOMContentLoaded', () => {
      startClock();
      setDeviceViewMode('mobile');
      const savedLang = localStorage.getItem('giftvault_preferred_lang') || 'te';
      applyLanguage(savedLang);
      renderAllDynamicSections();
      onCategoryChanged('wedding');
    });
  </script>

</body>
</html>
"""

with open(r"c:\Project\Gift Valut\web_preview\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open(r"c:\Project\Gift Valut\web\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

artifact_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"
with open(os.path.join(artifact_dir, "giftvault_interactive_preview.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("SUCCESS: Godly Luxury Redesign Generated and Synced across all files!")
