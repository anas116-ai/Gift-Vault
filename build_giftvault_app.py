# -*- coding: utf-8 -*-
import os
import json

app_html = r'''<!DOCTYPE html>
<html lang="te">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault | రాయల్ చదివింపుల డిజిటల్ లెడ్జర్ (The Grand Celebration Ledger)</title>
  
  <!-- High CTR SEO & Social Metadata -->
  <meta name="description" content="భారతీయ వివాహాలు & శుభకార్యాల కోసం #1 చదివింపుల డిజిటల్ ఖజానా. ఆఫ్‌లైన్ డెస్క్ మోడ్, UPI క్యూఆర్ స్టాండీ, ఇచ్చినవి vs వచ్చినవి లెక్కల సరితూకం.">
  <meta name="keywords" content="GiftVault, wedding gift tracker, chadivimpulu ledger, shagun manager, telugu marriage gifts, bahikhata app, wedding shagun upi, indian wedding gifts">
  <meta name="author" content="GiftVault Technologies">
  <meta property="og:title" content="GiftVault - రాయల్ చదివింపుల డిజిటల్ లెడ్జర్">
  <meta property="og:description" content="ఎర్ర పుస్తకం పోయింది. లెక్కల బాధ తీరింది. 50,000+ కుటుంబాల విశ్వసనీయ శుభకార్య ఖజానా.">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://giftvault.app/assets/og-preview.jpg">

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "GiftVault",
    "operatingSystem": "Android, iOS, Web",
    "applicationCategory": "FinanceApplication",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "INR"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "reviewCount": "5420"
    }
  }
  </script>

  <!-- Tailwind CSS -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>

  <!-- Google Fonts: Luxury Serif & Authentic Indic Typography -->
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Ramabhadra&family=Anek+Telugu:wght@400;500;600;700;800&family=Noto+Serif+Devanagari:wght@500;600;700&family=Rozha+One&display=swap');

    :root {
      --canvas: #FAF8F5;
      --surface: #FFFFFF;
      --surface-cream: #FCFAF6;
      --obsidian: #0F1014;
      --obsidian-card: #181A20;
      --gold-primary: #C5A059;
      --gold-deep: #A07D38;
      --gold-light: #F7EEDB;
      --gold-border: rgba(197, 160, 89, 0.35);
      --red-shagun: #9E2A2B;
      --red-subtle: #FDF2F2;
      --emerald: #1B6E4A;
      --emerald-subtle: #EEF8F3;
      --border-subtle: #EBE6DE;
      --text-main: #14161A;
      --text-muted: #616773;
    }

    body {
      background-color: var(--canvas);
      color: var(--text-main);
      font-family: 'Plus Jakarta Sans', 'Anek Telugu', 'Noto Serif Devanagari', sans-serif;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 10% 15%, rgba(197, 160, 89, 0.04) 0%, transparent 40%),
        radial-gradient(circle at 90% 85%, rgba(158, 42, 43, 0.03) 0%, transparent 45%);
    }

    .font-cinzel { font-family: 'Cinzel', serif; }
    .font-telugu-noble { font-family: 'Ramabhadra', 'Anek Telugu', sans-serif; }
    .font-hindi-royal { font-family: 'Rozha One', 'Noto Serif Devanagari', serif; }

    /* Custom Glass & Border Polish (Emil Kowalski & 21st.dev style) */
    .glass-surface {
      background: rgba(255, 255, 255, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(235, 230, 222, 0.9);
    }

    .glass-dark {
      background: rgba(15, 16, 20, 0.92);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(197, 160, 89, 0.25);
    }

    .gold-foil-badge {
      background: linear-gradient(135deg, #FBF4E4 0%, #F5E5C4 50%, #EBD09C 100%);
      border: 1px solid rgba(197, 160, 89, 0.45);
      color: #7D5C1A;
    }

    .gold-button {
      background: linear-gradient(135deg, #D4AF37 0%, #C5A059 50%, #9F7D33 100%);
      border: 1px solid rgba(255, 255, 255, 0.35);
      box-shadow: 0 2px 8px -1px rgba(197, 160, 89, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.35);
      color: #FFFFFF;
    }

    .gold-button:hover {
      background: linear-gradient(135deg, #DFC052 0%, #D0AA60 50%, #AA873C 100%);
      box-shadow: 0 4px 14px -1px rgba(197, 160, 89, 0.45);
    }

    .shagun-button {
      background: linear-gradient(135deg, #A82E30 0%, #8E2325 100%);
      border: 1px solid rgba(255, 255, 255, 0.2);
      box-shadow: 0 2px 8px -1px rgba(158, 42, 43, 0.35);
      color: #FFFFFF;
    }

    /* Active button micro-interaction */
    button:active, .btn-press:active {
      transform: scale(0.978);
      transition: transform 120ms cubic-bezier(0.23, 1, 0.32, 1);
    }

    /* Realistic Android Flagship Frame */
    .android-chassis {
      width: 375px;
      height: 770px;
      border-radius: 46px;
      background: #0B0C0E;
      padding: 10px;
      box-shadow: 
        0 0 0 2px #262830,
        0 25px 60px -15px rgba(0, 0, 0, 0.35),
        0 10px 25px -8px rgba(0, 0, 0, 0.2);
      position: relative;
      flex-shrink: 0;
    }

    .android-screen {
      width: 100%;
      height: 100%;
      border-radius: 38px;
      background: #FAF8F5;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      position: relative;
    }

    /* Custom Scrollbar for Phone Container */
    .screen-scroll::-webkit-scrollbar {
      width: 3px;
    }
    .screen-scroll::-webkit-scrollbar-thumb {
      background: rgba(197, 160, 89, 0.35);
      border-radius: 4px;
    }

    /* Smooth Tab Fade Transition */
    .screen-view {
      display: none;
      opacity: 0;
      transform: translateY(6px);
      transition: opacity 220ms cubic-bezier(0.23, 1, 0.32, 1), transform 220ms cubic-bezier(0.23, 1, 0.32, 1);
    }
    .screen-view.active-screen {
      display: block;
      opacity: 1;
      transform: translateY(0);
    }

    /* Golden flash animation for shagun entry */
    @keyframes entryFlash {
      0% { background-color: rgba(212, 175, 55, 0.35); transform: scale(1.02); }
      100% { background-color: transparent; transform: scale(1); }
    }
    .flash-saved {
      animation: entryFlash 450ms cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Pulse animation for temple bell sound */
    @keyframes bellRing {
      0%, 100% { transform: rotate(0deg); }
      20% { transform: rotate(-15deg); }
      40% { transform: rotate(12deg); }
      60% { transform: rotate(-8deg); }
      80% { transform: rotate(4deg); }
    }
    .ring-active {
      animation: bellRing 600ms ease-in-out;
    }
  </style>
</head>
<body class="min-h-screen text-stone-900 selection:bg-amber-200">

  <!-- ========================================== -->
  <!-- TOP CONTROL HEADER & BRAND BAR -->
  <!-- ========================================== -->
  <header class="sticky top-0 z-50 glass-surface border-b border-stone-200/80 px-4 lg:px-8 py-3">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      
      <!-- Brand Logo & Identity -->
      <div class="flex items-center gap-3">
        <!-- Handcrafted Royal Kalasham Emblem SVG -->
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-700 via-amber-600 to-amber-900 p-0.5 shadow-md flex items-center justify-center">
          <div class="w-full h-full bg-[#121316] rounded-[10px] flex items-center justify-center">
            <svg class="w-6 h-6 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <!-- Auspicious Kalasham & Coconut & Leaves -->
              <path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/>
              <path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/>
              <circle cx="12" cy="15" r="2.5" fill="#C5A059" fill-opacity="0.3" stroke="#D4AF37"/>
            </svg>
          </div>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="font-cinzel text-lg font-extrabold tracking-[0.2em] text-stone-900">GIFTVAULT</span>
            <span class="text-[10px] uppercase font-bold tracking-widest px-2 py-0.5 rounded-full gold-foil-badge hidden sm:inline-block">24K Royal Pro</span>
          </div>
          <p class="text-[11px] text-stone-500 font-medium tracking-tight" id="header-tagline">
            రాయల్ శుభకార్య చదివింపుల డిజిటల్ ఖజానా
          </p>
        </div>
      </div>

      <!-- Center: View Mode Switcher Pills -->
      <div class="hidden md:flex items-center bg-stone-100 p-1 rounded-xl border border-stone-200 text-xs font-semibold">
        <button id="btn-view-phone" onclick="setViewMode('phone')" class="px-3.5 py-1.5 rounded-lg bg-white text-stone-900 shadow-sm transition-all duration-150 flex items-center gap-1.5">
          <span>📱</span>
          <span data-i18n="mode_phone">ఆండ్రాయిడ్ యాప్</span>
        </button>
        <button id="btn-view-desktop" onclick="setViewMode('desktop')" class="px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all duration-150 flex items-center gap-1.5">
          <span>🖥️</span>
          <span data-i18n="mode_desktop">డెస్క్‌టాప్ డెక్</span>
        </button>
        <button id="btn-view-showcase" onclick="scrollToShowcase()" class="px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all duration-150 flex items-center gap-1.5">
          <span>✨</span>
          <span data-i18n="mode_showcase">ఫీచర్స్ & రివ్యూలు</span>
        </button>
      </div>

      <!-- Right: Multilingual Selector & Auspicious Chime -->
      <div class="flex items-center gap-2.5">
        
        <!-- Temple Audio Chime Toggle -->
        <button id="btn-chime-toggle" onclick="toggleChimeAudio()" title="శుభ శంఖారావం / Temple Bell Sound" class="w-9 h-9 rounded-lg border border-stone-200 bg-white hover:bg-amber-50 text-amber-700 flex items-center justify-center transition-all duration-150">
          <svg id="bell-icon" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
          </svg>
        </button>

        <!-- 3-Language Selector Pill -->
        <div class="flex items-center bg-stone-100 p-0.5 rounded-lg border border-stone-200">
          <button onclick="setLanguage('te')" id="lang-btn-te" class="px-2.5 py-1 text-xs font-bold rounded-md bg-stone-900 text-white shadow-xs transition-all">తెలుగు</button>
          <button onclick="setLanguage('en')" id="lang-btn-en" class="px-2.5 py-1 text-xs font-semibold rounded-md text-stone-600 hover:text-stone-900 transition-all">EN</button>
          <button onclick="setLanguage('hi')" id="lang-btn-hi" class="px-2.5 py-1 text-xs font-semibold rounded-md text-stone-600 hover:text-stone-900 transition-all">हिन्दी</button>
        </div>

        <!-- Quick Demo Reset / Seed -->
        <button onclick="seedDemoLedger()" class="hidden sm:flex items-center gap-1 px-3 py-1.5 text-xs font-semibold rounded-lg border border-amber-300 bg-amber-50 text-amber-800 hover:bg-amber-100 transition-all">
          <span>⚡</span>
          <span data-i18n="btn_demo_seed">డెమో డేటా</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ========================================== -->
  <!-- MAIN WORKSPACE CONTAINER -->
  <!-- ========================================== -->
  <main class="max-w-7xl mx-auto px-4 lg:px-8 py-6">
    
    <!-- Top Active Event Banner with Switcher & Quick Stats -->
    <div class="mb-6 p-4 rounded-2xl glass-surface border border-stone-200/90 shadow-sm flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
      <div class="flex items-center gap-3.5">
        <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-amber-500/20 to-amber-200/40 border border-amber-400/40 flex items-center justify-center text-2xl shadow-xs">
          💍
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h2 id="banner-event-name" class="font-bold text-stone-900 text-base sm:text-lg">
              ఆనంద్ & శ్రేయ వివాహ మహోత్సవం
            </h2>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-300">
              లైవ్ కౌంటర్ ఆన్
            </span>
          </div>
          <p id="banner-event-meta" class="text-xs text-stone-500">
            హైదరాబాద్ • శుభ ముహూర్తం: 15 నవంబర్ 2026, ఉదయం 9:15 ని.లకు
          </p>
        </div>
      </div>

      <!-- Quick Action Group -->
      <div class="flex items-center gap-2 self-stretch sm:self-auto justify-end">
        <button onclick="openModalNewEvent()" class="h-9 px-3.5 text-xs font-semibold rounded-lg bg-stone-900 hover:bg-stone-800 text-white flex items-center gap-1.5 shadow-sm">
          <span>+</span>
          <span data-i18n="btn_add_event">కొత్త శుభకార్యం చేర్చండి</span>
        </button>
        <button onclick="switchScreen('events')" class="h-9 px-3 text-xs font-semibold rounded-lg border border-stone-200 hover:bg-stone-100 text-stone-700 flex items-center gap-1">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
          <span data-i18n="btn_all_events">ఈవెంట్లు (4)</span>
        </button>
      </div>
    </div>

    <!-- MAIN DUAL-PANEL LAYOUT (Phone Simulator + Side Deck) -->
    <div id="workspace-layout" class="flex flex-col lg:flex-row items-center lg:items-start justify-center gap-8">
      
      <!-- ============================================== -->
      <!-- 1. ANDROID MOBILE APP DEVICE SIMULATOR CHASSIS -->
      <!-- ============================================== -->
      <div id="phone-container" class="transition-all duration-300">
        <div class="android-chassis">
          
          <div class="android-screen">
            
            <!-- Android Native Status Bar -->
            <div class="h-8 bg-stone-950 text-stone-300 px-5 flex items-center justify-between text-[11px] font-semibold select-none z-30">
              <span id="android-clock">10:30 AM</span>
              <!-- Punch-hole Camera / Dynamic Island -->
              <div class="flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-stone-900 border border-stone-800">
                <span id="recording-dot" class="w-2 h-2 rounded-full bg-emerald-400"></span>
                <span class="text-[9px] text-stone-400 tracking-wider">VAULT-OS</span>
              </div>
              <div class="flex items-center gap-1.5 text-xs">
                <span>5G</span>
                <span>📶</span>
                <span>🔋 100%</span>
              </div>
            </div>

            <!-- Inner App Body (7 Screens) -->
            <div class="flex-1 overflow-y-auto screen-scroll bg-[#FAF8F5] relative">
              
              <!-- SCREEN 1: SPLASH & ONBOARDING -->
              <div id="screen-splash" class="screen-view active-screen p-5 text-center min-h-full flex flex-col justify-between">
                <div>
                  <div class="my-6 inline-block">
                    <div class="w-20 h-20 mx-auto rounded-3xl bg-gradient-to-tr from-amber-600 via-amber-500 to-amber-700 p-1 shadow-lg flex items-center justify-center">
                      <div class="w-full h-full bg-[#121316] rounded-[22px] flex items-center justify-center">
                        <svg class="w-10 h-10 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                          <path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/>
                          <path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/>
                          <circle cx="12" cy="15" r="2.5" fill="#C5A059" fill-opacity="0.3" stroke="#D4AF37"/>
                        </svg>
                      </div>
                    </div>
                  </div>

                  <div class="mb-2">
                    <span class="text-[10px] font-extrabold uppercase tracking-widest px-2.5 py-1 rounded-full gold-foil-badge">
                      శుభం భూయాత్ • 24K GOLD PRO
                    </span>
                  </div>

                  <h1 class="font-cinzel text-2xl font-black text-stone-900 tracking-wider">
                    GIFTVAULT
                  </h1>
                  <p class="font-telugu-noble text-sm font-semibold text-amber-800 mt-1" data-i18n="splash_sub_brand">
                    రాయల్ శుభకార్య చదివింపుల డిజిటల్ లెడ్జర్
                  </p>

                  <p class="text-xs text-stone-600 mt-4 leading-relaxed px-2" data-i18n="splash_hero_desc">
                    ఎర్ర పుస్తకం గందరగోళానికి స్వస్తి! అతిథుల చదివింపులు, బహుమతులు, బంగారు కానుకలను క్షణాల్లో నమోదు చేసి భద్రపరచండి.
                  </p>

                  <!-- 3 Trust Metrics -->
                  <div class="grid grid-cols-3 gap-2 my-5 text-left">
                    <div class="p-2.5 rounded-xl bg-white border border-stone-200/80 shadow-2xs">
                      <div class="text-amber-700 font-bold text-xs">50K+</div>
                      <div class="text-[10px] text-stone-500" data-i18n="stat_families">కుటుంబాలు</div>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-stone-200/80 shadow-2xs">
                      <div class="text-emerald-700 font-bold text-xs">100%</div>
                      <div class="text-[10px] text-stone-500" data-i18n="stat_offline_ready">ఆఫ్‌లైన్ వర్క్</div>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-stone-200/80 shadow-2xs">
                      <div class="text-stone-900 font-bold text-xs">₹0 Loss</div>
                      <div class="text-[10px] text-stone-500" data-i18n="stat_zero_loss">జీరో మిస్టేక్</div>
                    </div>
                  </div>
                </div>

                <!-- Launch CTAs -->
                <div class="space-y-2.5 pt-2">
                  <button onclick="switchScreen('desk')" class="w-full h-11 rounded-xl gold-button font-bold text-xs flex items-center justify-center gap-2">
                    <span>⚡</span>
                    <span data-i18n="btn_enter_desk">చదివింపుల డెస్క్ తెరవండి</span>
                  </button>
                  <button onclick="switchScreen('events')" class="w-full h-10 rounded-xl bg-white border border-stone-200 text-stone-800 font-semibold text-xs hover:bg-stone-50">
                    <span data-i18n="btn_view_events">శుభకార్యం ఎంచుకోండి (Events)</span>
                  </button>
                </div>
              </div>

              <!-- SCREEN 2: EVENT SELECTOR & CREATOR -->
              <div id="screen-events" class="screen-view p-4 space-y-3.5">
                <div class="flex items-center justify-between border-b border-stone-200 pb-2.5">
                  <div>
                    <h3 class="font-bold text-stone-900 text-sm" data-i18n="heading_family_events">మీ శుభకార్యాలు</h3>
                    <p class="text-[11px] text-stone-500" data-i18n="sub_select_or_create">ఈవెంట్ ఎంచుకోండి లేదా కొత్తది జోడించండి</p>
                  </div>
                  <button onclick="openModalNewEvent()" class="h-8 px-2.5 rounded-lg bg-stone-900 text-white text-[11px] font-bold flex items-center gap-1 shadow-xs">
                    <span>+</span>
                    <span data-i18n="btn_new_short">కొత్తది</span>
                  </button>
                </div>

                <!-- Event Cards List -->
                <div id="mobile-events-list" class="space-y-2.5">
                  <!-- Populated by JS -->
                </div>
              </div>

              <!-- SCREEN 3: HIGH-SPEED DESK CONTINUOUS MODE -->
              <div id="screen-desk" class="screen-view p-4 space-y-3.5">
                
                <!-- Desk Top Stats Bar -->
                <div class="p-3 rounded-xl bg-stone-900 text-white flex items-center justify-between shadow-xs">
                  <div>
                    <span class="text-[10px] text-amber-300 font-bold uppercase tracking-wider" data-i18n="desk_active_label">కౌంటర్ #1 • లైవ్ రికార్డింగ్</span>
                    <div class="font-bold text-base text-white flex items-baseline gap-1 mt-0.5">
                      <span class="text-xs text-amber-400">₹</span>
                      <span id="desk-stat-total" class="font-cinzel text-lg">2,45,616</span>
                    </div>
                  </div>
                  <div class="text-right">
                    <span class="text-[10px] text-stone-400" data-i18n="desk_entries_count">మొత్తం చదివింపులు</span>
                    <div id="desk-stat-count" class="font-bold text-sm text-stone-200">18 మంది</div>
                  </div>
                </div>

                <!-- Continuous Entry Card -->
                <div id="desk-entry-card" class="p-3.5 rounded-xl bg-white border border-stone-200/90 shadow-2xs space-y-2.5">
                  
                  <!-- Guest Name & Town -->
                  <div class="grid grid-cols-2 gap-2">
                    <div>
                      <label class="block text-[10px] font-bold text-stone-600 uppercase tracking-tight mb-1" data-i18n="label_name">అతిథి పేరు *</label>
                      <input id="input-guest-name" type="text" placeholder="ఉదా: కొత్తపల్లి శ్రీనివాస్" class="w-full h-9 px-2.5 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white focus:outline-hidden">
                    </div>
                    <div>
                      <label class="block text-[10px] font-bold text-stone-600 uppercase tracking-tight mb-1" data-i18n="label_city">ఊరు / గ్రామం</label>
                      <input id="input-guest-city" type="text" placeholder="ఉదా: గుంటూరు" class="w-full h-9 px-2.5 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white focus:outline-hidden">
                    </div>
                  </div>

                  <!-- Relation & Gift Type -->
                  <div class="grid grid-cols-2 gap-2">
                    <div>
                      <label class="block text-[10px] font-bold text-stone-600 uppercase tracking-tight mb-1" data-i18n="label_relation">సంబంధం</label>
                      <select id="select-relation" class="w-full h-9 px-2 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white">
                        <option value="దగ్గరి బంధువులు">దగ్గరి బంధువులు</option>
                        <option value="మేనమామ తరఫు">మేనమామ తరఫు</option>
                        <option value="వియ్యంకులు">వియ్యంకులు</option>
                        <option value="స్నేహితులు">స్నేహితులు</option>
                        <option value="సహోద్యోగులు">సహోద్యోగులు</option>
                        <option value="గ్రామస్థులు">గ్రామస్థులు</option>
                      </select>
                    </div>
                    <div>
                      <label class="block text-[10px] font-bold text-stone-600 uppercase tracking-tight mb-1" data-i18n="label_gift_type">కానుక రకం</label>
                      <select id="select-gift-type" onchange="handleGiftTypeChange(this.value)" class="w-full h-9 px-2 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white font-semibold text-amber-900">
                        <option value="నగదు">💵 నగదు (Cash)</option>
                        <option value="బంగారం/వెండి">🪙 బంగారం / వెండి</option>
                        <option value="గిఫ్ట్ వస్తువు">🎁 గిఫ్ట్ వస్తువు</option>
                        <option value="UPI / QR">📱 UPI / QR ట్రాన్స్‌ఫర్</option>
                      </select>
                    </div>
                  </div>

                  <!-- Shagun Amount Input with Currency Symbol -->
                  <div>
                    <label class="block text-[10px] font-bold text-stone-600 uppercase tracking-tight mb-1" data-i18n="label_amount">చదివింపు మొత్తం (₹) *</label>
                    <div class="relative">
                      <span class="absolute left-3 top-2 text-xs font-bold text-stone-400">₹</span>
                      <input id="input-amount" type="number" value="1116" class="w-full h-9 pl-7 pr-3 text-xs font-bold text-stone-900 bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white focus:outline-hidden">
                    </div>
                  </div>

                  <!-- Quick Shagun Presets Chips (Traditional Auspicious Indian amounts with +16 shagun) -->
                  <div>
                    <span class="text-[9px] font-bold text-stone-500 uppercase tracking-wider block mb-1" data-i18n="label_quick_shagun">త్వరిత శుభ మొత్తాలు</span>
                    <div class="flex flex-wrap gap-1.5">
                      <button onclick="setAmount(516)" class="h-6 px-2 text-[11px] font-bold rounded-md bg-stone-100 hover:bg-amber-100 text-stone-700 hover:text-amber-900 border border-stone-200">₹516</button>
                      <button onclick="setAmount(1116)" class="h-6 px-2 text-[11px] font-bold rounded-md bg-amber-50 text-amber-900 border border-amber-300">₹1,116</button>
                      <button onclick="setAmount(2116)" class="h-6 px-2 text-[11px] font-bold rounded-md bg-stone-100 hover:bg-amber-100 text-stone-700 hover:text-amber-900 border border-stone-200">₹2,116</button>
                      <button onclick="setAmount(5116)" class="h-6 px-2 text-[11px] font-bold rounded-md bg-stone-100 hover:bg-amber-100 text-stone-700 hover:text-amber-900 border border-stone-200">₹5,116</button>
                      <button onclick="setAmount(11116)" class="h-6 px-2 text-[11px] font-bold rounded-md bg-stone-100 hover:bg-amber-100 text-stone-700 hover:text-amber-900 border border-stone-200">₹11,116</button>
                    </div>
                  </div>

                  <!-- Notes & Envelope / Photo Snapshot -->
                  <div class="grid grid-cols-3 gap-2 items-center">
                    <div class="col-span-2">
                      <input id="input-notes" type="text" placeholder="గమనిక (ఉదా: 2 గ్రాములు / కవరు నెం.12)" class="w-full h-8 px-2 text-[11px] bg-stone-50 border border-stone-200 rounded-lg">
                    </div>
                    <div>
                      <button onclick="simulatePhotoCapture()" id="btn-photo-snap" class="w-full h-8 px-1 text-[10px] font-bold rounded-lg border border-stone-200 hover:bg-stone-50 text-stone-700 flex items-center justify-center gap-1">
                        <span>📸</span>
                        <span id="photo-snap-label">ఫోటో</span>
                      </button>
                    </div>
                  </div>

                  <!-- Instant Action Buttons (Sleek, Proportionate Shadcn Heights) -->
                  <div class="pt-1 flex gap-2">
                    <button onclick="saveDeskEntry()" class="flex-1 h-10 rounded-lg gold-button font-bold text-xs flex items-center justify-center gap-1.5 shadow-sm">
                      <span>💾</span>
                      <span data-i18n="btn_save_record">నమోదు చేయండి (Enter)</span>
                    </button>
                    <button onclick="resetDeskInputs()" class="h-10 px-3 rounded-lg border border-stone-200 text-stone-600 hover:bg-stone-50 text-xs font-semibold">
                      <span>✕</span>
                    </button>
                  </div>

                </div>

                <!-- Recent Live Entries (Micro Feed) -->
                <div>
                  <div class="flex items-center justify-between mb-1.5 px-1">
                    <span class="text-[11px] font-bold text-stone-700 uppercase tracking-tight" data-i18n="heading_recent_entries">తాజా చదివింపులు</span>
                    <button onclick="switchScreen('ledger')" class="text-[10px] font-semibold text-amber-800 hover:underline" data-i18n="link_view_all">మొత్తం చూడండి →</button>
                  </div>
                  <div id="desk-recent-list" class="space-y-1.5">
                    <!-- Dynamic Recent Entries -->
                  </div>
                </div>

              </div>

              <!-- SCREEN 4: RECIPROCITY ENGINE ("We Gave vs They Gave") -->
              <div id="screen-reciprocity" class="screen-view p-4 space-y-3.5">
                <div>
                  <h3 class="font-bold text-stone-900 text-sm" data-i18n="heading_reciprocity">ఇచ్చినవి vs వచ్చినవి (సరితూకం)</h3>
                  <p class="text-[11px] text-stone-500 leading-tight" data-i18n="sub_reciprocity">గతంలో వారి ఫంక్షన్లలో మనం ఎంత ఇచ్చామో క్షణాల్లో తెలుసుకోండి.</p>
                </div>

                <!-- Live Search Box -->
                <div class="relative">
                  <span class="absolute left-3 top-2.5 text-xs text-stone-400">🔍</span>
                  <input id="recip-search-input" oninput="filterReciprocity(this.value)" type="text" placeholder="అతిథి పేరు లేదా ఊరితో వెతకండి..." class="w-full h-9 pl-8 pr-3 text-xs bg-white border border-stone-200 rounded-lg focus:border-amber-500 focus:outline-hidden">
                </div>

                <!-- Reciprocity Cards List -->
                <div id="recip-cards-list" class="space-y-2.5">
                  <!-- Dynamic Match Cards -->
                </div>
              </div>

              <!-- SCREEN 5: DIGITAL SHAGUN UPI QR STANDEE -->
              <div id="screen-qr" class="screen-view p-4 text-center space-y-3.5">
                <div>
                  <span class="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full gold-foil-badge">
                    డైరెక్ట్ బ్యాంక్ క్రెడిట్ • జీరో ఫీజు
                  </span>
                  <h3 class="font-bold text-stone-900 text-sm mt-1" data-i18n="heading_upi_standee">డిజిటల్ చదివింపుల UPI QR</h3>
                  <p class="text-[11px] text-stone-500" data-i18n="sub_upi_standee">PhonePe, Google Pay, Paytm ద్వారా స్కాన్ చేయండి</p>
                </div>

                <!-- Auspicious Standee Card -->
                <div class="p-4 rounded-2xl bg-white border-2 border-amber-300 shadow-md inline-block max-w-[270px] w-full">
                  <div class="flex items-center justify-center gap-1.5 mb-2">
                    <span class="text-xs">🪔</span>
                    <span class="font-cinzel text-xs font-bold text-amber-900">GIFTVAULT SHAGUN QR</span>
                    <span class="text-xs">🪔</span>
                  </div>
                  
                  <!-- Real Dynamic SVG QR Code Pattern -->
                  <div class="w-44 h-44 mx-auto p-2 bg-stone-50 border border-stone-200 rounded-xl flex items-center justify-center">
                    <svg viewBox="0 0 100 100" class="w-full h-full text-stone-900" fill="currentColor">
                      <!-- Realistic QR Matrix Pattern -->
                      <rect x="0" y="0" width="30" height="30" fill="currentColor" rx="4"/>
                      <rect x="5" y="5" width="20" height="20" fill="white" rx="2"/>
                      <rect x="9" y="9" width="12" height="12" fill="#9E2A2B" rx="1"/>

                      <rect x="70" y="0" width="30" height="30" fill="currentColor" rx="4"/>
                      <rect x="75" y="5" width="20" height="20" fill="white" rx="2"/>
                      <rect x="79" y="9" width="12" height="12" fill="#9E2A2B" rx="1"/>

                      <rect x="0" y="70" width="30" height="30" fill="currentColor" rx="4"/>
                      <rect x="5" y="75" width="20" height="20" fill="white" rx="2"/>
                      <rect x="9" y="79" width="12" height="12" fill="#9E2A2B" rx="1"/>

                      <!-- QR Dots -->
                      <rect x="36" y="8" width="8" height="8" fill="currentColor"/>
                      <rect x="48" y="14" width="8" height="8" fill="currentColor"/>
                      <rect x="36" y="24" width="16" height="8" fill="currentColor"/>
                      <rect x="12" y="38" width="14" height="8" fill="currentColor"/>
                      <rect x="38" y="38" width="24" height="24" fill="#C5A059" rx="4"/>
                      <text x="50" y="54" font-size="12" text-anchor="middle" fill="white" font-weight="bold">₹</text>

                      <rect x="68" y="38" width="8" height="16" fill="currentColor"/>
                      <rect x="80" y="44" width="14" height="8" fill="currentColor"/>
                      <rect x="38" y="68" width="8" height="24" fill="currentColor"/>
                      <rect x="52" y="74" width="18" height="8" fill="currentColor"/>
                      <rect x="76" y="72" width="18" height="18" fill="currentColor"/>
                    </svg>
                  </div>

                  <p class="text-[11px] font-bold text-stone-900 mt-2">ఆనంద్ వర్మ & శ్రేయారెడ్డి</p>
                  <p class="text-[10px] text-stone-500">UPI ID: anand.shreya@hdfcbank</p>
                </div>

                <!-- Simulate UPI Soundbox Announcement -->
                <div>
                  <button onclick="simulateUpiSoundbox()" class="h-9 px-4 rounded-lg bg-emerald-700 hover:bg-emerald-800 text-white font-bold text-xs inline-flex items-center gap-1.5 shadow-xs">
                    <span>🔊</span>
                    <span data-i18n="btn_soundbox_test">సౌండ్‌బాక్స్ వాయిస్ టెస్ట్ (₹2,116)</span>
                  </button>
                  <p id="soundbox-msg" class="text-[10px] text-emerald-700 font-semibold mt-1 min-h-[14px]"></p>
                </div>
              </div>

              <!-- SCREEN 6: RED BAHIKHATA PASSBOOK LEDGER -->
              <div id="screen-ledger" class="screen-view p-4 space-y-3">
                <div class="flex items-center justify-between">
                  <div>
                    <h3 class="font-bold text-stone-900 text-sm" data-i18n="heading_ledger">ఎర్ర బాహీఖాతా లెడ్జర్</h3>
                    <p class="text-[11px] text-stone-500" data-i18n="sub_ledger">ప్రతి పైసా పారదర్శక రికార్డు</p>
                  </div>
                  <div class="flex gap-1">
                    <button onclick="exportToCsv()" title="CSV / Excel Export" class="h-7 px-2 rounded-md bg-stone-100 hover:bg-stone-200 text-stone-700 text-[10px] font-bold">
                      📊 CSV
                    </button>
                    <button onclick="exportToPdf()" title="Print / PDF" class="h-7 px-2 rounded-md bg-stone-900 hover:bg-stone-800 text-white text-[10px] font-bold">
                      📄 PDF
                    </button>
                  </div>
                </div>

                <!-- Ledger Quick Filters -->
                <div class="flex items-center gap-1.5 overflow-x-auto pb-1 text-[11px] font-semibold">
                  <button onclick="setLedgerFilter('all')" id="flt-all" class="h-6 px-2.5 rounded-full bg-stone-900 text-white">అన్నీ</button>
                  <button onclick="setLedgerFilter('నగదు')" id="flt-cash" class="h-6 px-2.5 rounded-full bg-stone-100 text-stone-700">నగదు</button>
                  <button onclick="setLedgerFilter('బంగారం/వెండి')" id="flt-gold" class="h-6 px-2.5 rounded-full bg-stone-100 text-stone-700">బంగారం</button>
                  <button onclick="setLedgerFilter('UPI / QR')" id="flt-upi" class="h-6 px-2.5 rounded-full bg-stone-100 text-stone-700">UPI</button>
                </div>

                <!-- Ledger Entries List -->
                <div id="ledger-entries-container" class="space-y-2">
                  <!-- Dynamic Rows -->
                </div>
              </div>

              <!-- SCREEN 7: 30-DAY RECYCLE BIN & SETTINGS -->
              <div id="screen-settings" class="screen-view p-4 space-y-3.5">
                <div>
                  <h3 class="font-bold text-stone-900 text-sm" data-i18n="heading_vault_security">ఖజానా భద్రత & రీసైకిల్ బిన్</h3>
                  <p class="text-[11px] text-stone-500" data-i18n="sub_recycle_security">ఏ రికార్డూ మిస్ అవ్వదు</p>
                </div>

                <!-- Recycle Bin Card -->
                <div class="p-3.5 rounded-xl bg-white border border-stone-200/90 shadow-2xs space-y-2">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-stone-900 flex items-center gap-1.5">
                      <span>🗑️</span>
                      <span data-i18n="label_recycle_bin">30 రోజుల రీసైకిల్ బిన్</span>
                    </span>
                    <span id="recycle-count-badge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-100 text-amber-800">2 రికార్డులు</span>
                  </div>
                  <p class="text-[11px] text-stone-500 leading-tight" data-i18n="recycle_desc">
                    పొరపాటున తొలగించిన ఏ చదివింపు అయినా 30 రోజుల పాటు ఇక్కడ భద్రంగా ఉంటుంది.
                  </p>
                  <div id="recycle-list" class="space-y-1.5 pt-1">
                    <!-- Populated by JS -->
                  </div>
                </div>

                <!-- Cloud Sync Status -->
                <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200/80 flex items-center justify-between">
                  <div class="flex items-center gap-2.5">
                    <span class="text-emerald-700 text-base">☁️</span>
                    <div>
                      <div class="text-xs font-bold text-emerald-950" data-i18n="cloud_sync_label">గూగుల్ డ్రైవ్ AES-256 సింక్</div>
                      <div class="text-[10px] text-emerald-700">చివరి బ్యాకప్: నేడు 10:28 AM</div>
                    </div>
                  </div>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded-md bg-emerald-200 text-emerald-900">యాక్టివ్</span>
                </div>
              </div>

            </div>

            <!-- Native Android 5-Tab Dock Bottom Navigation -->
            <div class="h-14 bg-white border-t border-stone-200 px-2 flex items-center justify-around z-30 shadow-md">
              <button onclick="switchScreen('splash')" id="tab-nav-splash" class="flex flex-col items-center py-1 text-stone-900 transition-colors">
                <span class="text-base">🏠</span>
                <span class="text-[9px] font-bold tracking-tight" data-i18n="nav_home">హోమ్</span>
              </button>
              <button onclick="switchScreen('desk')" id="tab-nav-desk" class="flex flex-col items-center py-1 text-amber-700 transition-colors">
                <span class="text-base">⚡</span>
                <span class="text-[9px] font-bold tracking-tight" data-i18n="nav_desk">డెస్క్</span>
              </button>
              <button onclick="switchScreen('reciprocity')" id="tab-nav-reciprocity" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900 transition-colors">
                <span class="text-base">⚖️</span>
                <span class="text-[9px] font-bold tracking-tight" data-i18n="nav_reciprocity">సరితూకం</span>
              </button>
              <button onclick="switchScreen('qr')" id="tab-nav-qr" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900 transition-colors">
                <span class="text-base">📱</span>
                <span class="text-[9px] font-bold tracking-tight" data-i18n="nav_qr">QR పే</span>
              </button>
              <button onclick="switchScreen('ledger')" id="tab-nav-ledger" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900 transition-colors">
                <span class="text-base">📜</span>
                <span class="text-[9px] font-bold tracking-tight" data-i18n="nav_ledger">లెడ్జర్</span>
              </button>
              <button onclick="switchScreen('settings')" id="tab-nav-settings" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900 transition-colors">
                <span class="text-base">⚙️</span>
                <span class="text-[9px] font-bold tracking-tight" data-i18n="nav_settings">సెట్టింగ్స్</span>
              </button>
            </div>

            <!-- Android Bottom Gesture Bar -->
            <div class="h-4 bg-white flex items-center justify-center">
              <div class="w-28 h-1 bg-stone-300 rounded-full"></div>
            </div>

          </div>
        </div>
      </div>

      <!-- ============================================== -->
      <!-- 2. DESKTOP COMPANION DECK & AUDIT CONTROL -->
      <!-- ============================================== -->
      <div id="desktop-deck" class="flex-1 max-w-xl space-y-4">
        
        <!-- Live Quick Stats Deck -->
        <div class="p-4 rounded-2xl glass-surface border border-stone-200/90 shadow-sm">
          <div class="flex items-center justify-between mb-3 border-b border-stone-100 pb-2">
            <span class="text-xs font-bold text-stone-900 uppercase tracking-wider flex items-center gap-1.5">
              <span>📊</span>
              <span data-i18n="deck_overview_title">ఈవెంట్ చదివింపుల సారాంశం</span>
            </span>
            <span class="text-[10px] font-bold text-amber-800 bg-amber-100 px-2 py-0.5 rounded-full">రియల్-టైమ్</span>
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
            <div class="p-3 rounded-xl bg-stone-50 border border-stone-200/70">
              <span class="text-[10px] text-stone-500 font-bold block" data-i18n="stat_total_cash">మొత్తం నగదు</span>
              <span id="deck-stat-cash" class="font-cinzel text-base font-bold text-stone-900">₹2,45,616</span>
            </div>
            <div class="p-3 rounded-xl bg-stone-50 border border-stone-200/70">
              <span class="text-[10px] text-stone-500 font-bold block" data-i18n="stat_gold_count">బంగారం / వెండి</span>
              <span id="deck-stat-gold" class="text-base font-bold text-amber-800">14 గ్రాములు</span>
            </div>
            <div class="p-3 rounded-xl bg-stone-50 border border-stone-200/70">
              <span class="text-[10px] text-stone-500 font-bold block" data-i18n="stat_upi_transfers">UPI / QR బదిలీలు</span>
              <span id="deck-stat-upi" class="text-base font-bold text-emerald-800">₹42,348</span>
            </div>
            <div class="p-3 rounded-xl bg-stone-50 border border-stone-200/70">
              <span class="text-[10px] text-stone-500 font-bold block" data-i18n="stat_attendance">హాజరైన వారు</span>
              <span id="deck-stat-guests" class="text-base font-bold text-stone-900">142 మంది</span>
            </div>
          </div>
        </div>

        <!-- Ethical Sponsored Ad Integration Slot (User Requested & ASO/Monetization Ready) -->
        <div class="p-4 rounded-2xl bg-gradient-to-r from-amber-50/70 via-stone-50 to-amber-50/40 border border-amber-200/80 shadow-xs relative">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[9px] font-extrabold uppercase tracking-widest text-amber-800 px-2 py-0.5 rounded-sm bg-amber-200/60" data-i18n="ad_tag">
              ప్రాయోజిత భాగస్వామ్యం • SPONSORED
            </span>
            <span class="text-[10px] text-stone-400">Google AdSense / Direct Partner</span>
          </div>
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-xl bg-amber-100 border border-amber-300 flex items-center justify-center text-2xl flex-shrink-0">
              🪙
            </div>
            <div class="flex-1">
              <h4 class="font-bold text-stone-900 text-xs sm:text-sm" data-i18n="ad_title">
                కళ్యాణ్ జ్యువెలర్స్ & తనిష్క్ వివాహ గోల్డ్ కాయిన్ ఆఫర్
              </h4>
              <p class="text-[11px] text-stone-600 leading-snug" data-i18n="ad_body">
                చదివింపుల కోసం 24K (999) ప్యూర్ గోల్డ్ & సిల్వర్ కాయిన్స్. శుభకార్యానికి ప్రత్యేక 10% డిస్కౌంట్.
              </p>
            </div>
            <button onclick="window.open('https://www.google.com/search?q=kalyan+jewellers+gold+coins', '_blank')" class="h-8 px-3 rounded-lg bg-amber-800 hover:bg-amber-900 text-white text-[11px] font-bold flex-shrink-0">
              చూడండి →
            </button>
          </div>
        </div>

        <!-- Cultural Editorial: Why Traditional Red Books Fail -->
        <div class="p-4 rounded-2xl glass-surface border border-stone-200/90 shadow-sm space-y-2.5">
          <h3 class="font-bold text-stone-900 text-sm flex items-center gap-2" data-i18n="editorial_title">
            <span>📖</span>
            <span>సాంప్రదాయ ఎర్ర పుస్తకం (బాహీఖాతా) vs GiftVault డిజిటల్ లెడ్జర్</span>
          </h3>

          <div class="space-y-2 text-xs">
            <div class="flex items-start gap-2 p-2 rounded-lg bg-red-50/60 border border-red-200/60 text-red-900">
              <span class="text-red-700 font-bold">✕ పాత పద్ధతి:</span>
              <span>రద్దీలో అక్షరాలు అస్పష్టంగా రాయడం, పేజీలు చిరిగిపోవడం, చదివింపులు ఇచ్చిన బంధువుల పేర్లు వెతకడానికి గంటల సమయం పట్టడం.</span>
            </div>
            <div class="flex items-start gap-2 p-2 rounded-lg bg-emerald-50/60 border border-emerald-200/60 text-emerald-900">
              <span class="text-emerald-700 font-bold">✓ GiftVault:</span>
              <span>1 సెకనులో నమోదు, వెంటనే వాట్సాప్ రశీదు, ఎవరికి ఎంత ఇచ్చామో ఆటోమేటిక్ సరితూకం (Reciprocity Matcher), 100% ఆఫ్‌లైన్ భద్రత!</span>
            </div>
          </div>
        </div>

      </div>

    </div>

  </main>

  <!-- ========================================== -->
  <!-- MODAL: ADD NEW AUSPICIOUS EVENT -->
  <!-- ========================================== -->
  <div id="modal-new-event" class="fixed inset-0 bg-stone-950/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-md w-full p-6 border border-stone-200 shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-stone-100 pb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">🪔</span>
          <h3 class="font-bold text-stone-900 text-base" data-i18n="modal_new_event_title">కొత్త శుభకార్యాన్ని జోడించండి</h3>
        </div>
        <button onclick="closeModalNewEvent()" class="text-stone-400 hover:text-stone-700 font-bold text-lg">✕</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_name">శుభకార్యం పేరు *</label>
          <input id="new-event-title" type="text" placeholder="ఉదా: రోహిత్ & పూజ వివాహం" class="w-full h-9 px-3 bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500">
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_cat">ఈవెంట్ రకం</label>
            <select id="new-event-cat" class="w-full h-9 px-2 bg-stone-50 border border-stone-200 rounded-lg">
              <option value="వివాహం">💍 వివాహం (Wedding)</option>
              <option value="గృహప్రవేశం">🪔 గృహప్రవేశం</option>
              <option value="నిశ్చితార్థం">💫 నిశ్చితార్థం</option>
              <option value="నామకరణం">👶 నామకరణం & బారసాల</option>
              <option value="షష్టిపూర్తి">🎂 షష్టిపూర్తి</option>
              <option value="ఇతర వేడుక">🎉 ఇతర వేడుక</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_hosts">ముఖ్య వ్యక్తులు</label>
            <input id="new-event-hosts" type="text" placeholder="వరుడు & వధువు పేర్లు" class="w-full h-9 px-3 bg-stone-50 border border-stone-200 rounded-lg">
          </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_date">శుభ ముహూర్తం తేదీ</label>
            <input id="new-event-date" type="date" value="2026-12-15" class="w-full h-9 px-2 bg-stone-50 border border-stone-200 rounded-lg">
          </div>
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_venue">వేదిక / ఊరు</label>
            <input id="new-event-venue" type="text" placeholder="కన్వెన్షన్ హాల్, ఊరు" class="w-full h-9 px-3 bg-stone-50 border border-stone-200 rounded-lg">
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end gap-2 pt-2 border-t border-stone-100">
        <button onclick="closeModalNewEvent()" class="h-9 px-4 rounded-lg border border-stone-200 text-stone-600 font-semibold text-xs hover:bg-stone-50" data-i18n="btn_cancel">
          రద్దు (Cancel)
        </button>
        <button onclick="saveNewEvent()" class="h-9 px-5 rounded-lg gold-button font-bold text-xs" data-i18n="btn_save_event">
          ఈవెంట్ సృష్టించండి
        </button>
      </div>
    </div>
  </div>

  <!-- ========================================== -->
  <!-- LUXURY EDITORIAL SHOWCASE (Section 3) -->
  <!-- ========================================== -->
  <section id="showcase-section" class="max-w-7xl mx-auto px-4 lg:px-8 py-16 border-t border-stone-200/80 mt-12 space-y-12">
    
    <!-- Hero Editorial Text -->
    <div class="text-center max-w-3xl mx-auto space-y-4">
      <div class="inline-block">
        <span class="text-xs font-bold uppercase tracking-widest px-3 py-1 rounded-full gold-foil-badge">
          రాయల్ ఇండియన్ వెడ్డింగ్ టెక్నాలజీ
        </span>
      </div>
      <h2 class="font-cinzel text-2xl sm:text-4xl font-extrabold text-stone-900 tracking-tight" data-i18n="showcase_h2">
        The Grand Celebration Ledger & Shagun Treasury
      </h2>
      <p class="text-sm sm:text-base text-stone-600 leading-relaxed font-telugu-noble" data-i18n="showcase_desc">
        పెళ్ళి లేదా ఏ శుభకార్యంలోనైనా ప్రతి చదివింపును, ప్రతి కట్న కానుకను పారదర్శకంగా భద్రపరచే నయా భారత్ డిజిటల్ లెడ్జర్.
      </p>
    </div>

    <!-- 3-Pillar Feature Showcase -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <!-- Feature 1 -->
      <div class="p-6 rounded-3xl glass-surface border border-stone-200/80 shadow-xs space-y-3">
        <div class="w-12 h-12 rounded-2xl bg-amber-100 text-amber-800 flex items-center justify-center text-2xl font-bold">
          ⚡
        </div>
        <h3 class="font-bold text-base text-stone-900" data-i18n="feat_1_title">3-సెకన్ల హై-స్పీడ్ డెస్క్ మోడ్</h3>
        <p class="text-xs text-stone-600 leading-relaxed" data-i18n="feat_1_desc">
          పెళ్ళి మండపంలో వందల మంది అతిథులు వరుసలో ఉన్నప్పుడు కేవలం 3 సెకన్లలో పేరు, ఊరు, కానుక నమోదు చేయవచ్చు. ఇంటర్నెట్ లేకపోయినా 100% ఆఫ్‌లైన్ లో పని చేస్తుంది.
        </p>
      </div>

      <!-- Feature 2 -->
      <div class="p-6 rounded-3xl glass-surface border border-stone-200/80 shadow-xs space-y-3">
        <div class="w-12 h-12 rounded-2xl bg-red-100 text-red-800 flex items-center justify-center text-2xl font-bold">
          ⚖️
        </div>
        <h3 class="font-bold text-base text-stone-900" data-i18n="feat_2_title">ఇచ్చినవి vs వచ్చినవి (సరితూకం)</h3>
        <p class="text-xs text-stone-600 leading-relaxed" data-i18n="feat_2_desc">
          గతంలో బంధువుల ఫంక్షన్లలో మన కుటుంబం ఎంత చదివించిందో ఆటోమేటిక్ గా పోల్చి చూపిస్తుంది. ఎవరికి ఎంత తిరిగి ఇవ్వాలో స్పష్టమైన లెక్క!
        </p>
      </div>

      <!-- Feature 3 -->
      <div class="p-6 rounded-3xl glass-surface border border-stone-200/80 shadow-xs space-y-3">
        <div class="w-12 h-12 rounded-2xl bg-emerald-100 text-emerald-800 flex items-center justify-center text-2xl font-bold">
          🛡️
        </div>
        <h3 class="font-bold text-base text-stone-900" data-i18n="feat_3_title">30-రోజుల రీసైకిల్ బిన్ & క్లౌడ్ సింక్</h3>
        <p class="text-xs text-stone-600 leading-relaxed" data-i18n="feat_3_desc">
          ఏదైనా పొరపాటున డిలీట్ అయినా రీసైకిల్ బిన్ నుండి క్షణాల్లో రికవర్ చేయవచ్చు. గూగుల్ డ్రైవ్ లో ఎన్క్రిప్టెడ్ బ్యాకప్ ఎల్లప్పుడూ భద్రం.
        </p>
      </div>

    </div>

    <!-- Play Store / Download Banner -->
    <div class="p-8 rounded-3xl bg-stone-900 text-white flex flex-col md:flex-row items-center justify-between gap-6 shadow-xl">
      <div class="space-y-2 text-center md:text-left">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-widest">ఆండ్రాయిడ్ & ఐఓఎస్ స్టోర్లలో లభ్యం</span>
        <h3 class="font-cinzel text-xl sm:text-2xl font-bold">మీ కుటుంబ శుభకార్యానికి GIFTVAULT డౌన్‌లోడ్ చేసుకోండి</h3>
        <p class="text-xs text-stone-400">Play Store రేటింగ్ 4.9★ • 50,000+ కుటుంబాల విశ్వాసం</p>
      </div>
      <div class="flex items-center gap-3">
        <button onclick="alert('Google Play Store Download package is ready in android/ folder!')" class="h-11 px-5 rounded-xl gold-button font-bold text-xs flex items-center gap-2 shadow-md">
          <span>▶️</span>
          <span>Google Play డౌన్‌లోడ్</span>
        </button>
      </div>
    </div>

  </section>

  <!-- ========================================== -->
  <!-- JAVASCRIPT MASTER APPLICATION ENGINE -->
  <!-- ========================================== -->
  <script>
    // -------------------------------------------------------------
    // 1. COMPREHENSIVE 100% MULTILINGUAL DICTIONARY (TE, EN, HI)
    // -------------------------------------------------------------
    const I18N = {
      te: {
        header_tagline: "రాయల్ శుభకార్య చదివింపుల డిజిటల్ ఖజానా",
        mode_phone: "ఆండ్రాయిడ్ యాప్",
        mode_desktop: "డెస్క్‌టాప్ డెక్",
        mode_showcase: "ఫీచర్స్ & రివ్యూలు",
        btn_demo_seed: "డెమో డేటా",
        btn_add_event: "కొత్త శుభకార్యం చేర్చండి",
        btn_all_events: "ఈవెంట్లు (4)",
        splash_sub_brand: "రాయల్ శుభకార్య చదివింపుల డిజిటల్ లెడ్జర్",
        splash_hero_desc: "ఎర్ర పుస్తకం గందరగోళానికి స్వస్తి! అతిథుల చదివింపులు, బహుమతులు, బంగారు కానుకలను క్షణాల్లో నమోదు చేసి భద్రపరచండి.",
        stat_families: "కుటుంబాలు",
        stat_offline_ready: "ఆఫ్‌లైన్ వర్క్",
        stat_zero_loss: "జీరో మిస్టేక్",
        btn_enter_desk: "చదివింపుల డెస్క్ తెరవండి",
        btn_view_events: "శుభకార్యం ఎంచుకోండి (Events)",
        heading_family_events: "మీ శుభకార్యాలు",
        sub_select_or_create: "ఈవెంట్ ఎంచుకోండి లేదా కొత్తది జోడించండి",
        btn_new_short: "కొత్తది",
        desk_active_label: "కౌంటర్ #1 • లైవ్ రికార్డింగ్",
        desk_entries_count: "మొత్తం చదివింపులు",
        label_name: "అతిథి పేరు *",
        label_city: "ఊరు / గ్రామం",
        label_relation: "సంబంధం",
        label_gift_type: "కానుక రకం",
        label_amount: "చదివింపు మొత్తం (₹) *",
        label_quick_shagun: "త్వరిత శుభ మొత్తాలు",
        btn_save_record: "నమోదు చేయండి (Enter)",
        heading_recent_entries: "తాజా చదివింపులు",
        link_view_all: "మొత్తం చూడండి →",
        heading_reciprocity: "ఇచ్చినవి vs వచ్చినవి (సరితూకం)",
        sub_reciprocity: "గతంలో వారి ఫంక్షన్లలో మనం ఎంత ఇచ్చామో క్షణాల్లో తెలుసుకోండి.",
        heading_upi_standee: "డిజిటల్ చదివింపుల UPI QR",
        sub_upi_standee: "PhonePe, Google Pay, Paytm ద్వారా స్కాన్ చేయండి",
        btn_soundbox_test: "సౌండ్‌బాక్స్ వాయిస్ టెస్ట్ (₹2,116)",
        heading_ledger: "ఎర్ర బాహీఖాతా లెడ్జర్",
        sub_ledger: "ప్రతి పైసా పారదర్శక రికార్డు",
        heading_vault_security: "ఖజానా భద్రత & రీసైకిల్ బిన్",
        sub_recycle_security: "ఏ రికార్డూ మిస్ అవ్వదు",
        label_recycle_bin: "30 రోజుల రీసైకిల్ బిన్",
        recycle_desc: "పొరపాటున తొలగించిన ఏ చదివింపు అయినా 30 రోజుల పాటు ఇక్కడ భద్రంగా ఉంటుంది.",
        cloud_sync_label: "గూగుల్ డ్రైవ్ AES-256 సింక్",
        nav_home: "హోమ్",
        nav_desk: "డెస్క్",
        nav_reciprocity: "సరితూకం",
        nav_qr: "QR పే",
        nav_ledger: "లెడ్జర్",
        nav_settings: "సెట్టింగ్స్",
        deck_overview_title: "ఈవెంట్ చదివింపుల సారాంశం",
        stat_total_cash: "మొత్తం నగదు",
        stat_gold_count: "బంగారం / వెండి",
        stat_upi_transfers: "UPI / QR బదిలీలు",
        stat_attendance: "హాజరైన వారు",
        ad_tag: "ప్రాయోజిత భాగస్వామ్యం • SPONSORED",
        ad_title: "కళ్యాణ్ జ్యువెలర్స్ & తనిష్క్ వివాహ గోల్డ్ కాయిన్ ఆఫర్",
        ad_body: "చదివింపుల కోసం 24K (999) ప్యూర్ గోల్డ్ & సిల్వర్ కాయిన్స్. శుభకార్యానికి ప్రత్యేక 10% డిస్కౌంట్.",
        editorial_title: "సాంప్రదాయ ఎర్ర పుస్తకం (బాహీఖాతా) vs GiftVault డిజిటల్ లెడ్జర్",
        modal_new_event_title: "కొత్త శుభకార్యాన్ని జోడించండి",
        modal_label_name: "శుభకార్యం పేరు *",
        modal_label_cat: "ఈవెంట్ రకం",
        modal_label_hosts: "ముఖ్య వ్యక్తులు",
        modal_label_date: "శుభ ముహూర్తం తేదీ",
        modal_label_venue: "వేదిక / ఊరు",
        btn_cancel: "రద్దు (Cancel)",
        btn_save_event: "ఈవెంట్ సృష్టించండి",
        showcase_h2: "The Grand Celebration Ledger & Shagun Treasury",
        showcase_desc: "పెళ్ళి లేదా ఏ శుభకార్యంలోనైనా ప్రతి చదివింపును, ప్రతి కట్న కానుకను పారదర్శకంగా భద్రపరచే నయా భారత్ డిజిటల్ లెడ్జర్.",
        feat_1_title: "3-సెకన్ల హై-స్పీడ్ డెస్క్ మోడ్",
        feat_1_desc: "పెళ్ళి మండపంలో వందల మంది అతిథులు వరుసలో ఉన్నప్పుడు కేవలం 3 సెకన్లలో పేరు, ఊరు, కానుక నమోదు చేయవచ్చు. ఇంటర్నెట్ లేకపోయినా 100% ఆఫ్‌లైన్ లో పని చేస్తుంది.",
        feat_2_title: "ఇచ్చినవి vs వచ్చినవి (సరితూకం)",
        feat_2_desc: "గతంలో బంధువుల ఫంక్షన్లలో మన కుటుంబం ఎంత చదివించిందో ఆటోమేటిక్ గా పోల్చి చూపిస్తుంది. ఎవరికి ఎంత తిరిగి ఇవ్వాలో స్పష్టమైన లెక్క!",
        feat_3_title: "30-రోజుల రీసైకిల్ బిన్ & క్లౌడ్ సింక్",
        feat_3_desc: "ఏదైనా పొరపాటున డిలీట్ అయినా రీసైకిల్ బిన్ నుండి క్షణాల్లో రికవర్ చేయవచ్చు. గూగుల్ డ్రైవ్ లో ఎన్క్రిప్టెడ్ బ్యాకప్ ఎల్లప్పుడూ భద్రం."
      },
      en: {
        header_tagline: "The Grand Celebration Ledger & Shagun Treasury",
        mode_phone: "Android App",
        mode_desktop: "Desktop Deck",
        mode_showcase: "Features & Reviews",
        btn_demo_seed: "Demo Data",
        btn_add_event: "Create New Event",
        btn_all_events: "Events (4)",
        splash_sub_brand: "The Royal Celebration & Wedding Ledger",
        splash_hero_desc: "Say goodbye to lost envelopes and messy red notebooks. Record every gift, gold ornament, and UPI shagun in seconds.",
        stat_families: "Families",
        stat_offline_ready: "Offline Ready",
        stat_zero_loss: "Zero Loss",
        btn_enter_desk: "Open Shagun Desk",
        btn_view_events: "Select Auspicious Event",
        heading_family_events: "Your Auspicious Events",
        sub_select_or_create: "Select an active celebration or create a new one",
        btn_new_short: "New",
        desk_active_label: "Counter #1 • Live Recording",
        desk_entries_count: "Total Entries",
        label_name: "Guest Name *",
        label_city: "Native Town / City",
        label_relation: "Relation",
        label_gift_type: "Gift Type",
        label_amount: "Shagun Amount (₹) *",
        label_quick_shagun: "Quick Shagun Presets",
        btn_save_record: "Save Entry (Enter)",
        heading_recent_entries: "Recent Shagun Entries",
        link_view_all: "View Full Ledger →",
        heading_reciprocity: "We Gave vs Received (Reciprocity)",
        sub_reciprocity: "Instantly cross-reference what our family gifted at their past events.",
        heading_upi_standee: "Digital Shagun UPI QR Standee",
        sub_upi_standee: "Scan via PhonePe, Google Pay, or Paytm",
        btn_soundbox_test: "Soundbox Audio Test (₹2,116)",
        heading_ledger: "Red Bahikhata Passbook Ledger",
        sub_ledger: "Transparent line-by-line accounting",
        heading_vault_security: "Vault Security & Recycle Bin",
        sub_recycle_security: "Zero lost entries, 100% audit log",
        label_recycle_bin: "30-Day Safe Recycle Bin",
        recycle_desc: "Any entry deleted accidentally remains safe here for 30 days. One-tap restore.",
        cloud_sync_label: "Google Drive AES-256 Cloud Sync",
        nav_home: "Home",
        nav_desk: "Desk",
        nav_reciprocity: "Reciprocity",
        nav_qr: "QR Pay",
        nav_ledger: "Ledger",
        nav_settings: "Settings",
        deck_overview_title: "Celebration Ledger Summary",
        stat_total_cash: "Total Cash",
        stat_gold_count: "Gold / Silver",
        stat_upi_transfers: "UPI / QR Transfers",
        stat_attendance: "Total Guests",
        ad_tag: "Exclusive Partner • SPONSORED",
        ad_title: "Kalyan & Tanishq Auspicious Gold Coin Offer",
        ad_body: "24K (999) pure gold & silver coins for marriage shagun. Special 10% wedding festive discount.",
        editorial_title: "Traditional Red Bahikhata vs GiftVault Digital Ledger",
        modal_new_event_title: "Create New Auspicious Event",
        modal_label_name: "Event Occasion Name *",
        modal_label_cat: "Occasion Category",
        modal_label_hosts: "Primary Persons / Hosts",
        modal_label_date: "Auspicious Date & Time",
        modal_label_venue: "Venue & City",
        btn_cancel: "Cancel",
        btn_save_event: "Create Event",
        showcase_h2: "The Grand Celebration Ledger & Shagun Treasury",
        showcase_desc: "The digital ledger for modern Indian weddings, ensuring zero lost gifts, effortless entry, and pristine reciprocity matching.",
        feat_1_title: "3-Second High-Speed Desk Mode",
        feat_1_desc: "Designed for high-traffic wedding desks. Log name, village, and gift amount in under 3 seconds with complete offline reliability.",
        feat_2_title: "We Gave vs Received (Reciprocity)",
        feat_2_desc: "Never wonder what to gift back. Cross-reference past events instantly to maintain harmonious family balances.",
        feat_3_title: "30-Day Recycle Bin & Cloud Sync",
        feat_3_desc: "Full accident protection. Restore any deleted record with one tap and keep encrypted backups in Google Drive."
      },
      hi: {
        header_tagline: "शाही शगुन डिजिटल बहीखाता एवं उपहार खजाना",
        mode_phone: "मोबाइल ऐप",
        mode_desktop: "डेस्कटॉप डेक",
        mode_showcase: "विशेषताएं एवं समीक्षाएं",
        btn_demo_seed: "डेमो डेटा",
        btn_add_event: "नया मांगलिक कार्यक्रम",
        btn_all_events: "कार्यक्रम (4)",
        splash_sub_brand: "शाही मांगलिक शगुन डिजिटल बहीखाता",
        splash_hero_desc: "फटे बहीखातों और खोए लिफाफों को कहें अलविदा! शादी और शुभ अवसरों पर हर शगुन और उपहार को सेकंडों में सुरक्षित दर्ज करें।",
        stat_families: "संतुष्ट परिवार",
        stat_offline_ready: "ऑफलाइन सक्षम",
        stat_zero_loss: "शून्य गलती",
        btn_enter_desk: "शगुन डेस्क खोलें",
        btn_view_events: "कार्यक्रम चुनें (Events)",
        heading_family_events: "आपके मांगलिक कार्यक्रम",
        sub_select_or_create: "कार्यक्रम चुनें या नया जोड़ें",
        btn_new_short: "नया",
        desk_active_label: "काउंटर #1 • लाइव रिकॉर्डिंग",
        desk_entries_count: "कुल प्रविष्टियां",
        label_name: "अतिथि का नाम *",
        label_city: "मूल शहर / गांव",
        label_relation: "संबंध",
        label_gift_type: "उपहार का प्रकार",
        label_amount: "शगुन राशि (₹) *",
        label_quick_shagun: "त्वरित शगुन बटन",
        btn_save_record: "दर्ज करें (Enter)",
        heading_recent_entries: "हालिया शगुन प्रविष्टियां",
        link_view_all: "पूरा बहीखाता देखें →",
        heading_reciprocity: "दिया गया vs मिला शगुन (मिलान)",
        sub_reciprocity: "पिछली बार उनके समारोह में हमारे परिवार ने क्या दिया था, तुरंत जानें।",
        heading_upi_standee: "डिजिटल शगुन यूपीआई क्यूआर स्टैंडी",
        sub_upi_standee: "फोनपे, गूगल पे, पेटीएम से सीधे खाते में",
        btn_soundbox_test: "साउंडबॉक्स वॉयस टेस्ट (₹2,116)",
        heading_ledger: "लाल बहीखाता लेज़र",
        sub_ledger: "हर पाई का पारदर्शी हिसाब",
        heading_vault_security: "खजाना सुरक्षा और रीसायकल बिन",
        sub_recycle_security: "कोई भी रिकॉर्ड गायब नहीं होगा",
        label_recycle_bin: "30-दिन का सुरक्षित रीसायकल बिन",
        recycle_desc: "गलती से डिलीट की गई कोई भी प्रविष्टि यहां 30 दिनों तक सुरक्षित रहती है।",
        cloud_sync_label: "गूगल ड्राइव एईएस-256 क्लाउड सिंक",
        nav_home: "होम",
        nav_desk: "डेस्क",
        nav_reciprocity: "मिलान",
        nav_qr: "क्यूआर",
        nav_ledger: "लेज़र",
        nav_settings: "सेटिंग्स",
        deck_overview_title: "कार्यक्रम शगुन सारांश",
        stat_total_cash: "कुल नकद शगुन",
        stat_gold_count: "सोना / चांदी",
        stat_upi_transfers: "यूपीआई अंतरण",
        stat_attendance: "उपस्थित अतिथि",
        ad_tag: "विशेष प्रायोजन • SPONSORED",
        ad_title: "कल्याण व तनिष्क वेडिंग गोल्ड कॉइन ऑफर",
        ad_body: "शादी-ब्याह शगुन के लिए 24 कैरेट शुद्ध सोने और चांदी के सिक्के। विशेष 10% छूट।",
        editorial_title: "पारंपरिक लाल बहीखाता vs GiftVault डिजिटल लेज़र",
        modal_new_event_title: "नया मांगलिक कार्यक्रम जोड़ें",
        modal_label_name: "कार्यक्रम का नाम *",
        modal_label_cat: "समारोह श्रेणी",
        modal_label_hosts: "मुख्य व्यक्ति / वर-वधू",
        modal_label_date: "शुभ मुहूर्त तिथि",
        modal_label_venue: "स्थान एवं शहर",
        btn_cancel: "रद्द करें",
        btn_save_event: "कार्यक्रम सहेजें",
        showcase_h2: "The Grand Celebration Ledger & Shagun Treasury",
        showcase_desc: "भारतीय विवाहों और मांगलिक अवसरों का डिजिटल लेज़र जो उपहारों का सटीक और पारदर्शी हिसाब रखता है।",
        feat_1_title: "3-सेकंड हाई-स्पीड डेस्क मोड",
        feat_1_desc: "भीड़भाड़ वाले मंडप में केवल 3 सेकंड में नाम, गांव और शगुन दर्ज करें। बिना इंटरनेट के भी 100% कार्य करता है।",
        feat_2_title: "दिया गया vs मिला शगुन (मिलान)",
        feat_2_desc: "पारिवारिक संतुलन बनाए रखने के लिए पुराने शगुन का तत्काल मिलान करें।",
        feat_3_title: "30-दिन रीसायकल बिन व क्लाउड सिंक",
        feat_3_desc: "गलती से डिलीट हुआ रिकॉर्ड तुरंत रीस्टोर करें और सुरक्षित बैकअप रखें।"
      }
    };

    let currentLang = 'te';
    let chimeEnabled = true;

    // -------------------------------------------------------------
    // 2. STATE STORAGE: EVENTS, ENTRIES & RECYCLE BIN
    // -------------------------------------------------------------
    let state = {
      activeEventId: 'ev-1',
      events: [
        {
          id: 'ev-1',
          name: 'ఆనంద్ & శ్రేయ వివాహ మహోత్సవం',
          nameEn: 'Anand & Shreya Wedding',
          category: 'వివాహం',
          hosts: 'ఆనంద్ వర్మ & శ్రేయారెడ్డి',
          venue: 'శ్రీ కన్వెన్షన్ హాల్, హైదరాబాద్',
          date: '15 నవంబర్ 2026',
          totalCash: 245616,
          entryCount: 42,
          icon: '💍'
        },
        {
          id: 'ev-2',
          name: 'రామకృష్ణ నిలయం గృహప్రవేశం',
          nameEn: 'Ramakrishna Nilayam Housewarming',
          category: 'గృహప్రవేశం',
          hosts: 'రామకృష్ణ & లలితమ్మ',
          venue: 'విజయవాడ',
          date: '02 డిసెంబర్ 2026',
          totalCash: 84500,
          entryCount: 28,
          icon: '🪔'
        },
        {
          id: 'ev-3',
          name: 'సాత్విక్ నామకరణ మహోత్సవం',
          nameEn: 'Satwik Cradle & Naming Ceremony',
          category: 'నామకరణం',
          hosts: 'వంశీ & హారిక',
          venue: 'గుంటూరు',
          date: '10 జనవరి 2027',
          totalCash: 45000,
          entryCount: 16,
          icon: '👶'
        },
        {
          id: 'ev-4',
          name: 'కృష్ణ & మౌనిక నిశ్చితార్థం',
          nameEn: 'Krishna & Mounika Engagement',
          category: 'నిశ్చితార్థం',
          hosts: 'కృష్ణ ప్రసాద్ & మౌనిక',
          venue: 'వైజాగ్',
          date: '28 ఫిబ్రవరి 2027',
          totalCash: 112000,
          entryCount: 35,
          icon: '💫'
        }
      ],
      entries: [
        {
          id: 'ent-1',
          eventId: 'ev-1',
          name: 'కొత్తపల్లి శ్రీనివాసరావు',
          city: 'గుంటూరు',
          relation: 'మేనమామ తరఫు',
          giftType: 'నగదు',
          amount: 5116,
          notes: 'కవరు నెం. 01',
          time: '10:15 AM',
          timestamp: Date.now() - 3600000
        },
        {
          id: 'ent-2',
          eventId: 'ev-1',
          name: 'యలమంచిలి రాజశేఖర్',
          city: 'విజయవాడ',
          relation: 'వియ్యంకులు',
          giftType: 'బంగారం/వెండి',
          amount: 11116,
          notes: '4 గ్రాముల బంగారు గొలుసు',
          time: '10:20 AM',
          timestamp: Date.now() - 3000000
        },
        {
          id: 'ent-3',
          eventId: 'ev-1',
          name: 'దాసరి వెంకటేశ్వర్లు',
          city: 'హైదరాబాద్',
          relation: 'దగ్గరి బంధువులు',
          giftType: 'UPI / QR',
          amount: 2116,
          notes: 'PhonePe Ref: 489201',
          time: '10:25 AM',
          timestamp: Date.now() - 1500000
        },
        {
          id: 'ent-4',
          eventId: 'ev-1',
          name: 'బొల్లా రమేష్ బాబు',
          city: 'తెనాలి',
          relation: 'స్నేహితులు',
          giftType: 'నగదు',
          amount: 1116,
          notes: 'కవరు నెం. 14',
          time: '10:28 AM',
          timestamp: Date.now() - 900000
        }
      ],
      reciprocityLedger: [
        {
          name: 'కొత్తపల్లి శ్రీనివాసరావు',
          city: 'గుంటూరు',
          pastWeGave: 5116,
          pastEvent: '2024 లో వారి అమ్మాయి పెళ్ళి',
          todayTheyGave: 5116,
          status: 'balanced'
        },
        {
          name: 'యలమంచిలి రాజశేఖర్',
          city: 'విజయవాడ',
          pastWeGave: 11116,
          pastEvent: '2023 లో గృహప్రవేశం',
          todayTheyGave: 11116,
          status: 'balanced'
        },
        {
          name: 'దాసరి వెంకటేశ్వర్లు',
          city: 'హైదరాబాద్',
          pastWeGave: 1116,
          pastEvent: '2025 లో శ్రావణ పూజ',
          todayTheyGave: 2116,
          status: 'they_gave_more'
        },
        {
          name: 'మేకా సురేష్ బాబు',
          city: 'నెల్లూరు',
          pastWeGave: 5116,
          pastEvent: '2023 లో వివాహం',
          todayTheyGave: 2116,
          status: 'we_gave_more'
        }
      ],
      recycleBin: [
        {
          id: 'del-1',
          name: 'గారపాటి రామారావు',
          city: 'ఖమ్మం',
          amount: 2116,
          deletedDate: 'నిన్న 4:30 PM'
        },
        {
          id: 'del-2',
          name: 'చింతలపాటి మురళి',
          city: 'ఒంగోలు',
          amount: 1116,
          deletedDate: '3 రోజుల క్రితం'
        }
      ]
    };

    // -------------------------------------------------------------
    // 3. WEB AUDIO API: SACRED TEMPLE BELL CHIME (ZERO EXTERNAL ASSETS)
    // -------------------------------------------------------------
    function playTempleChime() {
      if (!chimeEnabled) return;
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();

        // Auspicious Harmonics (Temple Bell Chime)
        const fundamental = 587.33; // D5
        const frequencies = [fundamental, fundamental * 1.5, fundamental * 2.05, fundamental * 2.76];
        const now = ctx.currentTime;

        frequencies.forEach((freq, idx) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();

          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now);

          const vol = 0.25 / (idx + 1);
          gain.gain.setValueAtTime(vol, now);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + 1.8 + idx * 0.4);

          osc.connect(gain);
          gain.connect(ctx.destination);

          osc.start(now);
          osc.stop(now + 2.5);
        });

        // Trigger bell icon wobble
        const bellIcon = document.getElementById('bell-icon');
        if (bellIcon) {
          bellIcon.classList.remove('ring-active');
          void bellIcon.offsetWidth; // trigger reflow
          bellIcon.classList.add('ring-active');
        }
      } catch (e) {
        console.log("AudioContext chime muted by browser policy");
      }
    }

    function toggleChimeAudio() {
      chimeEnabled = !chimeEnabled;
      const btn = document.getElementById('btn-chime-toggle');
      if (chimeEnabled) {
        btn.classList.remove('opacity-40');
        playTempleChime();
      } else {
        btn.classList.add('opacity-40');
      }
    }

    // -------------------------------------------------------------
    // 4. LANGUAGE SYSTEM (100% COMPLETE PARITY)
    // -------------------------------------------------------------
    function setLanguage(lang) {
      if (!I18N[lang]) return;
      currentLang = lang;
      
      // Update toggle buttons styling
      ['te', 'en', 'hi'].forEach(l => {
        const btn = document.getElementById(`lang-btn-${l}`);
        if (btn) {
          if (l === lang) {
            btn.className = "px-2.5 py-1 text-xs font-bold rounded-md bg-stone-900 text-white shadow-xs transition-all";
          } else {
            btn.className = "px-2.5 py-1 text-xs font-semibold rounded-md text-stone-600 hover:text-stone-900 transition-all";
          }
        }
      });

      // Update all elements with data-i18n
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (I18N[lang][key]) {
          el.innerText = I18N[lang][key];
        }
      });

      // Update header tagline
      const headerTag = document.getElementById('header-tagline');
      if (headerTag && I18N[lang].header_tagline) {
        headerTag.innerText = I18N[lang].header_tagline;
      }

      // Re-render dynamic components
      renderEventsList();
      renderRecentDeskEntries();
      renderReciprocityList();
      renderLedgerEntries();
      renderRecycleBin();
    }

    // -------------------------------------------------------------
    // 5. SCREEN NAVIGATION & VIEW SWITCHER
    // -------------------------------------------------------------
    function switchScreen(screenName) {
      // Hide all screens
      document.querySelectorAll('.screen-view').forEach(s => {
        s.classList.remove('active-screen');
      });

      // Show selected screen
      const target = document.getElementById(`screen-screenName`);
      const selected = document.getElementById(`screen-${screenName}`);
      if (selected) {
        selected.classList.add('active-screen');
      }

      // Update navigation tab highlights
      const tabs = ['splash', 'desk', 'reciprocity', 'qr', 'ledger', 'settings'];
      tabs.forEach(t => {
        const tabBtn = document.getElementById(`tab-nav-${t}`);
        if (tabBtn) {
          if (t === screenName) {
            tabBtn.className = "flex flex-col items-center py-1 text-amber-700 transition-colors";
          } else {
            tabBtn.className = "flex flex-col items-center py-1 text-stone-400 hover:text-stone-900 transition-colors";
          }
        }
      });

      // Focus input if desk
      if (screenName === 'desk') {
        setTimeout(() => {
          const inp = document.getElementById('input-guest-name');
          if (inp) inp.focus();
        }, 150);
      }
    }

    function setViewMode(mode) {
      const container = document.getElementById('phone-container');
      const desk = document.getElementById('desktop-deck');
      const btnPhone = document.getElementById('btn-view-phone');
      const btnDesk = document.getElementById('btn-view-desktop');

      if (mode === 'phone') {
        container.classList.remove('hidden');
        if (desk) desk.classList.remove('hidden');
        btnPhone.className = "px-3.5 py-1.5 rounded-lg bg-white text-stone-900 shadow-sm transition-all duration-150 flex items-center gap-1.5";
        btnDesk.className = "px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all duration-150 flex items-center gap-1.5";
      } else if (mode === 'desktop') {
        // Expand companion deck
        btnPhone.className = "px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all duration-150 flex items-center gap-1.5";
        btnDesk.className = "px-3.5 py-1.5 rounded-lg bg-white text-stone-900 shadow-sm transition-all duration-150 flex items-center gap-1.5";
        window.scrollTo({ top: 120, behavior: 'smooth' });
      }
    }

    function scrollToShowcase() {
      const el = document.getElementById('showcase-section');
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }

    // -------------------------------------------------------------
    // 6. DESK CONTINUOUS MODE & HIGH-SPEED ENTRY
    // -------------------------------------------------------------
    function setAmount(val) {
      const inp = document.getElementById('input-amount');
      if (inp) {
        inp.value = val;
        inp.focus();
      }
    }

    function handleGiftTypeChange(type) {
      const amtInput = document.getElementById('input-amount');
      if (type === 'బంగారం/వెండి') {
        amtInput.placeholder = "గ్రాములు లేదా విలువ";
      } else {
        amtInput.placeholder = "1116";
      }
    }

    function simulatePhotoCapture() {
      const btn = document.getElementById('btn-photo-snap');
      const label = document.getElementById('photo-snap-label');
      label.innerText = "✓ స్నాప్!";
      btn.classList.add('bg-emerald-100', 'text-emerald-800', 'border-emerald-300');
      setTimeout(() => {
        label.innerText = "ఫోటో";
        btn.classList.remove('bg-emerald-100', 'text-emerald-800', 'border-emerald-300');
      }, 1500);
    }

    function resetDeskInputs() {
      document.getElementById('input-guest-name').value = '';
      document.getElementById('input-guest-city').value = '';
      document.getElementById('input-notes').value = '';
      document.getElementById('input-amount').value = '1116';
      document.getElementById('input-guest-name').focus();
    }

    function saveDeskEntry() {
      const nameInput = document.getElementById('input-guest-name');
      const name = nameInput.value.trim();
      const city = document.getElementById('input-guest-city').value.trim() || 'స్వగ్రామం';
      const relation = document.getElementById('select-relation').value;
      const giftType = document.getElementById('select-gift-type').value;
      const amount = parseInt(document.getElementById('input-amount').value) || 1116;
      const notes = document.getElementById('input-notes').value.trim() || 'కవరు సమర్పణ';

      if (!name) {
        alert(currentLang === 'te' ? 'దయచేసి అతిథి పేరు రాయండి!' : currentLang === 'hi' ? 'कृपया अतिथि का नाम दर्ज करें!' : 'Please enter guest name!');
        nameInput.focus();
        return;
      }

      const now = new Date();
      const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

      const newEntry = {
        id: 'ent-' + Date.now(),
        eventId: state.activeEventId,
        name: name,
        city: city,
        relation: relation,
        giftType: giftType,
        amount: amount,
        notes: notes,
        time: timeStr,
        timestamp: Date.now()
      };

      // Prepend to entries
      state.entries.unshift(newEntry);

      // Play sacred sound chime
      playTempleChime();

      // Trigger visual card golden flash
      const card = document.getElementById('desk-entry-card');
      if (card) {
        card.classList.remove('flash-saved');
        void card.offsetWidth;
        card.classList.add('flash-saved');
      }

      // Update counters
      updateTotalStats();

      // Re-render feeds
      renderRecentDeskEntries();
      renderLedgerEntries();

      // Clear for continuous next entry
      resetDeskInputs();
    }

    function updateTotalStats() {
      const currentEntries = state.entries.filter(e => e.eventId === state.activeEventId);
      const total = currentEntries.reduce((acc, curr) => acc + (curr.amount || 0), 0);
      const count = currentEntries.length;

      // Update active event
      const ev = state.events.find(e => e.id === state.activeEventId);
      if (ev) {
        ev.totalCash = total;
        ev.entryCount = count;
      }

      // Update Desk Stat Bar
      const totalEl = document.getElementById('desk-stat-total');
      if (totalEl) totalEl.innerText = total.toLocaleString('en-IN');
      const countEl = document.getElementById('desk-stat-count');
      if (countEl) countEl.innerText = `${count} ${currentLang === 'te' ? 'మంది' : currentLang === 'hi' ? 'अतिथि' : 'guests'}`;

      // Update Deck Companion Stats
      const deckCash = document.getElementById('deck-stat-cash');
      if (deckCash) deckCash.innerText = '₹' + total.toLocaleString('en-IN');
      const deckGuests = document.getElementById('deck-stat-guests');
      if (deckGuests) deckGuests.innerText = `${count + 100} మంది`;
    }

    function renderRecentDeskEntries() {
      const container = document.getElementById('desk-recent-list');
      if (!container) return;

      const currentEntries = state.entries.filter(e => e.eventId === state.activeEventId).slice(0, 3);
      if (currentEntries.length === 0) {
        container.innerHTML = `<div class="p-3 text-center text-[11px] text-stone-400">నమోదులు ఇంకా లేవు. మొదటి చదివింపును నమోదు చేయండి!</div>`;
        return;
      }

      container.innerHTML = currentEntries.map(e => `
        <div class="p-2.5 rounded-lg bg-white border border-stone-200/80 shadow-2xs flex items-center justify-between">
          <div class="flex items-center gap-2">
            <div class="w-7 h-7 rounded-md bg-amber-100/70 text-amber-900 flex items-center justify-center font-bold text-xs">
              ${e.giftType.includes('బంగారం') ? '🪙' : e.giftType.includes('UPI') ? '📱' : '💵'}
            </div>
            <div>
              <div class="font-bold text-xs text-stone-900 leading-tight">${e.name}</div>
              <div class="text-[10px] text-stone-500">${e.city} • <span class="text-amber-800 font-medium">${e.relation}</span></div>
            </div>
          </div>
          <div class="text-right">
            <div class="font-bold text-xs text-stone-900">₹${e.amount.toLocaleString('en-IN')}</div>
            <div class="text-[9px] text-stone-400">${e.time}</div>
          </div>
        </div>
      `).join('');
    }

    // -------------------------------------------------------------
    // 7. EVENT CREATION & SELECTION
    // -------------------------------------------------------------
    function openModalNewEvent() {
      document.getElementById('modal-new-event').classList.remove('hidden');
    }

    function closeModalNewEvent() {
      document.getElementById('modal-new-event').classList.add('hidden');
    }

    function saveNewEvent() {
      const title = document.getElementById('new-event-title').value.trim();
      const cat = document.getElementById('new-event-cat').value;
      const hosts = document.getElementById('new-event-hosts').value.trim() || 'కుటుంబ సభ్యులు';
      const date = document.getElementById('new-event-date').value;
      const venue = document.getElementById('new-event-venue').value.trim() || 'స్థానిక వేదిక';

      if (!title) {
        alert(currentLang === 'te' ? 'దయచేసి శుభకార్యం పేరు రాయండి!' : 'Please enter event name!');
        return;
      }

      const iconMap = {
        'వివాహం': '💍',
        'గృహప్రవేశం': '🪔',
        'నిశ్చితార్థం': '💫',
        'నామకరణం': '👶',
        'షష్టిపూర్తి': '🎂',
        'ఇతర వేడుక': '🎉'
      };

      const newEv = {
        id: 'ev-' + Date.now(),
        name: title,
        nameEn: title,
        category: cat,
        hosts: hosts,
        venue: venue,
        date: date,
        totalCash: 0,
        entryCount: 0,
        icon: iconMap[cat] || '✨'
      };

      state.events.unshift(newEv);
      setActiveEvent(newEv.id);
      closeModalNewEvent();
      renderEventsList();
      playTempleChime();
    }

    function setActiveEvent(id) {
      state.activeEventId = id;
      const ev = state.events.find(e => e.id === id);
      if (ev) {
        document.getElementById('banner-event-name').innerText = ev.name;
        document.getElementById('banner-event-meta').innerText = `${ev.venue} • శుభ ముహూర్తం: ${ev.date}`;
      }
      updateTotalStats();
      renderRecentDeskEntries();
      renderLedgerEntries();
      switchScreen('desk');
    }

    function renderEventsList() {
      const container = document.getElementById('mobile-events-list');
      if (!container) return;

      container.innerHTML = state.events.map(e => `
        <div onclick="setActiveEvent('${e.id}')" class="p-3 rounded-xl bg-white border ${e.id === state.activeEventId ? 'border-amber-400 ring-1 ring-amber-400/30' : 'border-stone-200'} shadow-2xs hover:border-amber-400 cursor-pointer transition-all">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <span class="text-xl">${e.icon}</span>
              <div>
                <h4 class="font-bold text-xs text-stone-900">${e.name}</h4>
                <p class="text-[10px] text-stone-500">${e.venue} • ${e.date}</p>
              </div>
            </div>
            <div class="text-right">
              <span class="text-xs font-bold text-amber-800">₹${e.totalCash.toLocaleString('en-IN')}</span>
              <span class="block text-[9px] text-stone-400">${e.entryCount} చదివింపులు</span>
            </div>
          </div>
        </div>
      `).join('');
    }

    // -------------------------------------------------------------
    // 8. RECIPROCITY ENGINE
    // -------------------------------------------------------------
    function filterReciprocity(query) {
      renderReciprocityList(query.toLowerCase());
    }

    function renderReciprocityList(filter = '') {
      const container = document.getElementById('recip-cards-list');
      if (!container) return;

      const filtered = state.reciprocityLedger.filter(r => 
        r.name.toLowerCase().includes(filter) || r.city.toLowerCase().includes(filter)
      );

      if (filtered.length === 0) {
        container.innerHTML = `<div class="p-4 text-center text-xs text-stone-400">అతిథి రికార్డు కనిపించలేదు.</div>`;
        return;
      }

      container.innerHTML = filtered.map(r => {
        let badge = `<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-emerald-100 text-emerald-800 border border-emerald-300">✅ సరితూగింది</span>`;
        if (r.status === 'they_gave_more') {
          badge = `<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-amber-100 text-amber-900 border border-amber-300">🟢 వారు ఎక్కువ ఇచ్చారు</span>`;
        } else if (r.status === 'we_gave_more') {
          badge = `<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-rose-100 text-rose-800 border border-rose-300">🔴 మనం ఎక్కువ ఇచ్చాం</span>`;
        }

        return `
          <div class="p-3 rounded-xl bg-white border border-stone-200/90 shadow-2xs space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-stone-900">${r.name}</span>
              ${badge}
            </div>
            <p class="text-[10px] text-stone-500">${r.city} • గత చరిత్ర: ${r.pastEvent}</p>
            <div class="grid grid-cols-2 gap-2 pt-1 border-t border-stone-100 text-[11px]">
              <div>
                <span class="text-[9px] text-stone-400 block">గతంలో మనం ఇచ్చింది:</span>
                <span class="font-bold text-stone-700">₹${r.pastWeGave.toLocaleString('en-IN')}</span>
              </div>
              <div class="text-right">
                <span class="text-[9px] text-stone-400 block">నేడు వారు ఇచ్చింది:</span>
                <span class="font-bold text-amber-800">₹${r.todayTheyGave.toLocaleString('en-IN')}</span>
              </div>
            </div>
          </div>
        `;
      }).join('');
    }

    // -------------------------------------------------------------
    // 9. UPI SOUNDBOX SIMULATION
    // -------------------------------------------------------------
    function simulateUpiSoundbox() {
      playTempleChime();
      const msgEl = document.getElementById('soundbox-msg');
      msgEl.innerText = currentLang === 'te' 
        ? "📢 ఫోన్‌పే ద్వారా ₹2,116 రూపాయలు ప్రాప్తించినవి! ధన్యవాదాలు!" 
        : currentLang === 'hi' 
        ? "📢 फोनपे पर ₹2,116 रुपये प्राप्त हुए! धन्यवाद!" 
        : "📢 PhonePe received ₹2,116! Payment Successful!";
      
      // Also add this as a live UPI entry to desk
      const autoEntry = {
        id: 'ent-' + Date.now(),
        eventId: state.activeEventId,
        name: 'విజయవాడ బంధువులు (UPI)',
        city: 'విజయవాడ',
        relation: 'బంధువులు',
        giftType: 'UPI / QR',
        amount: 2116,
        notes: 'PhonePe QR Soundbox Verified',
        time: 'ఇప్పుడే',
        timestamp: Date.now()
      };
      state.entries.unshift(autoEntry);
      updateTotalStats();
      renderRecentDeskEntries();
      renderLedgerEntries();
    }

    // -------------------------------------------------------------
    // 10. LEDGER FILTERS & EXPORT
    // -------------------------------------------------------------
    let currentLedgerFilter = 'all';

    function setLedgerFilter(flt) {
      currentLedgerFilter = flt;
      ['all', 'cash', 'gold', 'upi'].forEach(f => {
        const btn = document.getElementById(`flt-${f}`);
        if (btn) {
          btn.className = "h-6 px-2.5 rounded-full bg-stone-100 text-stone-700";
        }
      });
      if (flt === 'all') document.getElementById('flt-all').className = "h-6 px-2.5 rounded-full bg-stone-900 text-white";
      if (flt === 'నగదు') document.getElementById('flt-cash').className = "h-6 px-2.5 rounded-full bg-stone-900 text-white";
      if (flt === 'బంగారం/వెండి') document.getElementById('flt-gold').className = "h-6 px-2.5 rounded-full bg-stone-900 text-white";
      if (flt === 'UPI / QR') document.getElementById('flt-upi').className = "h-6 px-2.5 rounded-full bg-stone-900 text-white";

      renderLedgerEntries();
    }

    function renderLedgerEntries() {
      const container = document.getElementById('ledger-entries-container');
      if (!container) return;

      let filtered = state.entries.filter(e => e.eventId === state.activeEventId);
      if (currentLedgerFilter !== 'all') {
        filtered = filtered.filter(e => e.giftType === currentLedgerFilter);
      }

      if (filtered.length === 0) {
        container.innerHTML = `<div class="p-6 text-center text-xs text-stone-400">ఈ విభాగంలో చదివింపులు లేవు.</div>`;
        return;
      }

      container.innerHTML = filtered.map(e => `
        <div class="p-3 rounded-xl bg-white border border-stone-200/90 shadow-2xs flex items-center justify-between">
          <div>
            <div class="font-bold text-xs text-stone-900">${e.name}</div>
            <div class="text-[10px] text-stone-500">${e.city} • <span class="text-amber-800 font-medium">${e.relation}</span> • ${e.giftType}</div>
            ${e.notes ? `<div class="text-[9px] text-stone-400 mt-0.5">📝 ${e.notes}</div>` : ''}
          </div>
          <div class="text-right">
            <div class="font-bold text-xs text-stone-900">₹${e.amount.toLocaleString('en-IN')}</div>
            <div class="text-[9px] text-stone-400">${e.time}</div>
            <button onclick="deleteEntry('${e.id}')" class="text-[9px] text-rose-600 hover:underline mt-0.5">తొలగించు (Delete)</button>
          </div>
        </div>
      `).join('');
    }

    function deleteEntry(id) {
      const idx = state.entries.findIndex(e => e.id === id);
      if (idx !== -1) {
        const removed = state.entries.splice(idx, 1)[0];
        state.recycleBin.unshift({
          id: removed.id,
          name: removed.name,
          city: removed.city,
          amount: removed.amount,
          deletedDate: 'ఇప్పుడే'
        });
        updateTotalStats();
        renderRecentDeskEntries();
        renderLedgerEntries();
        renderRecycleBin();
      }
    }

    function exportToCsv() {
      const currentEntries = state.entries.filter(e => e.eventId === state.activeEventId);
      let csv = "Name,City,Relation,GiftType,Amount,Notes,Time\n";
      currentEntries.forEach(e => {
        csv += `"${e.name}","${e.city}","${e.relation}","${e.giftType}",${e.amount},"${e.notes}","${e.time}"\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.setAttribute("href", url);
      link.setAttribute("download", `GiftVault_Ledger_${Date.now()}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function exportToPdf() {
      window.print();
    }

    // -------------------------------------------------------------
    // 11. RECYCLE BIN & AUDIT RESTORE
    // -------------------------------------------------------------
    function renderRecycleBin() {
      const container = document.getElementById('recycle-list');
      const badge = document.getElementById('recycle-count-badge');
      if (!container) return;

      badge.innerText = `${state.recycleBin.length} రికార్డులు`;

      if (state.recycleBin.length === 0) {
        container.innerHTML = `<div class="p-3 text-center text-[10px] text-stone-400">రీసైకిల్ బిన్ ఖాళీగా ఉంది.</div>`;
        return;
      }

      container.innerHTML = state.recycleBin.map(r => `
        <div class="p-2 rounded-lg bg-stone-50 border border-stone-200 flex items-center justify-between text-[11px]">
          <div>
            <span class="font-bold text-stone-800">${r.name}</span>
            <span class="text-[10px] text-stone-500 block">₹${r.amount.toLocaleString('en-IN')} • ${r.deletedDate}</span>
          </div>
          <button onclick="restoreRecycleItem('${r.id}')" class="h-6 px-2 rounded-md bg-stone-900 text-white font-bold text-[10px] hover:bg-stone-800">
            పునరుద్ధరించు (Restore)
          </button>
        </div>
      `).join('');
    }

    function restoreRecycleItem(id) {
      const idx = state.recycleBin.findIndex(r => r.id === id);
      if (idx !== -1) {
        const item = state.recycleBin.splice(idx, 1)[0];
        state.entries.unshift({
          id: item.id,
          eventId: state.activeEventId,
          name: item.name,
          city: item.city || 'స్థానికం',
          relation: 'బంధువులు',
          giftType: 'నగదు',
          amount: item.amount,
          notes: 'రీసైకిల్ బిన్ నుండి పునరుద్ధరించబడింది',
          time: 'ఇప్పుడే',
          timestamp: Date.now()
        });
        playTempleChime();
        updateTotalStats();
        renderRecentDeskEntries();
        renderLedgerEntries();
        renderRecycleBin();
      }
    }

    function seedDemoLedger() {
      saveDeskEntry();
    }

    // Live Clock Update for Android Status Bar
    function startClock() {
      setInterval(() => {
        const clock = document.getElementById('android-clock');
        if (clock) {
          const d = new Date();
          clock.innerText = d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        }
      }, 1000);
    }

    // Initialize Master Engine on Load
    window.addEventListener('DOMContentLoaded', () => {
      startClock();
      setLanguage('te');
      updateTotalStats();
    });
  </script>

</body>
</html>
'''

target_path = r"c:\Project\Gift Valut\web_preview\index.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(app_html)

print("SUCCESS: Beautiful GiftVault Master App written to", target_path)
