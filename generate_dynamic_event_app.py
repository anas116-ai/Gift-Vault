# -*- coding: utf-8 -*-
import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="te" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault | రాయల్ శుభకార్య చదివింపుల డిజిటల్ లెడ్జర్ (The Grand Celebration Ledger)</title>
  
  <meta name="description" content="భారతీయ వివాహాలు & సాంప్రదాయ శుభకార్యాల కోసం #1 చదివింపుల డిజిటల్ ఖజానా. ఆఫ్‌లైన్ డెస్క్ మోడ్, ఇచ్చినవి vs వచ్చినవి లెక్కల సరితూకం.">
  <meta name="keywords" content="GiftVault, wedding gift tracker, chadivimpulu ledger, shagun manager, telugu marriage gifts, bahikhata app, odugu, half saree function">
  <meta name="author" content="GiftVault Technologies">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "GiftVault",
    "operatingSystem": "Android, iOS, Windows, Web",
    "applicationCategory": "FinanceApplication",
    "offers": { "@type": "Offer", "price": "0", "priceCurrency": "INR" }
  }
  </script>

  <!-- Tailwind CSS CDN -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>

  <!-- Google Fonts: Luxury Latin & Authentic Indic Typography -->
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Ramabhadra&family=Anek+Telugu:wght@400;500;600;700;800&family=Noto+Serif+Devanagari:wght@500;600;700&family=Rozha+One&display=swap');

    :root {
      --canvas: #FAF9F6;
      --obsidian: #0F1117;
      --gold-primary: #C5A059;
      --gold-light: #DFB76C;
      --gold-deep: #8C6D2D;
      --gold-border: rgba(197, 160, 89, 0.30);
      --red-crimson: #8E1E24;
      --emerald-green: #1B6E4A;
      --glass-surface: rgba(255, 255, 255, 0.85);
      --glass-border: rgba(235, 230, 222, 0.95);
      --glass-dark: rgba(15, 17, 23, 0.88);
      --shadow-glass: 0 10px 30px 0 rgba(0, 0, 0, 0.04), 0 1px 3px 0 rgba(0, 0, 0, 0.02);
    }

    body {
      background-color: var(--canvas);
      color: #1A1D24;
      font-family: 'Plus Jakarta Sans', 'Anek Telugu', 'Noto Serif Devanagari', sans-serif;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 12% 10%, rgba(197, 160, 89, 0.05) 0%, transparent 45%),
        radial-gradient(circle at 88% 90%, rgba(142, 30, 36, 0.04) 0%, transparent 45%);
    }

    .font-cinzel { font-family: 'Cinzel', serif; }
    .font-telugu { font-family: 'Ramabhadra', 'Anek Telugu', sans-serif; }
    .font-hindi { font-family: 'Rozha One', 'Noto Serif Devanagari', serif; }

    .glass-card {
      background: var(--glass-surface);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      border: 1px solid var(--glass-border);
      box-shadow: var(--shadow-glass);
    }

    .gold-btn {
      background: linear-gradient(135deg, #DFB76C 0%, #C5A059 50%, #8C6D2D 100%);
      border: 1px solid rgba(255, 255, 255, 0.35);
      box-shadow: 0 4px 12px -2px rgba(197, 160, 89, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.35);
      color: #FFFFFF;
      transition: all 180ms cubic-bezier(0.23, 1, 0.32, 1);
    }
    .gold-btn:hover {
      background: linear-gradient(135deg, #E8C37C 0%, #D0AA62 50%, #997733 100%);
      box-shadow: 0 6px 18px -2px rgba(197, 160, 89, 0.45);
    }

    button:active, .btn-press:active {
      transform: scale(0.978);
      transition: transform 120ms cubic-bezier(0.23, 1, 0.32, 1);
    }

    .page-section {
      display: none;
      opacity: 0;
      transition: opacity 200ms ease-out;
    }
    .page-section.active-page {
      display: block;
      opacity: 1;
    }

    .app-screen {
      display: none;
      opacity: 0;
      transition: opacity 180ms ease-out;
    }
    .app-screen.active-app-screen {
      display: block;
      opacity: 1;
    }

    @keyframes entryFlash {
      0% { background-color: rgba(212, 175, 55, 0.35); transform: scale(1.015); }
      100% { background-color: transparent; transform: scale(1); }
    }
    .flash-saved {
      animation: entryFlash 450ms cubic-bezier(0.16, 1, 0.3, 1);
    }

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
<body class="min-h-screen text-stone-900 selection:bg-amber-200 flex flex-col justify-between">

  <!-- ============================================================== -->
  <!-- 1. TOP GLOBAL NAVIGATION HEADER -->
  <!-- ============================================================== -->
  <header class="sticky top-0 z-50 glass-card border-b border-stone-200/90 px-4 lg:px-8 py-3">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      
      <!-- Brand Logo & Identity (Clean Luxury Seal Vector) -->
      <div onclick="navigateToPage('landing')" class="flex items-center gap-3 cursor-pointer select-none">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-700 via-amber-600 to-amber-900 p-0.5 shadow-md flex items-center justify-center">
          <div class="w-full h-full bg-[#0F1117] rounded-[10px] flex items-center justify-center">
            <!-- Bespoke Kalasham Sacred Vector Icon -->
            <svg class="w-6 h-6 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/>
              <path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/>
              <circle cx="12" cy="15" r="2.5" fill="#C5A059" fill-opacity="0.3" stroke="#D4AF37"/>
            </svg>
          </div>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="font-cinzel text-lg font-extrabold tracking-[0.2em] text-stone-900">GIFTVAULT</span>
            <span class="text-[9px] uppercase font-bold tracking-widest px-2 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-300 hidden sm:inline-block">24K Royal Pro</span>
          </div>
          <p class="text-[11px] text-stone-500 font-medium tracking-tight" id="header-tagline">
            రాయల్ శుభకార్య చదివింపుల డిజిటల్ ఖజానా
          </p>
        </div>
      </div>

      <!-- Landing Navigation Links -->
      <nav id="nav-landing-links" class="hidden md:flex items-center gap-6 text-xs font-semibold text-stone-600">
        <a href="#features" class="hover:text-amber-800 transition-colors" data-i18n="nav_features">ఫీచర్లు</a>
        <a href="#comparison" class="hover:text-amber-800 transition-colors" data-i18n="nav_comparison">పోలిక (vs మార్కెట్)</a>
        <a href="#calculator" class="hover:text-amber-800 transition-colors" data-i18n="nav_calculator">బ్యాలెన్స్ కాలిక్యులేటర్</a>
      </nav>

      <!-- App Header Navigation (Workspace Mode) -->
      <div id="nav-app-controls" class="hidden items-center gap-1.5">
        <button onclick="switchAppTab('dashboard')" id="head-tab-dash" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-stone-900 text-white shadow-xs flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          <span data-i18n="tab_dashboard">డ్యాష్‌బోర్డ్</span>
        </button>
        <button onclick="switchAppTab('desk')" id="head-tab-desk" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-stone-700 hover:bg-stone-100 flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          <span data-i18n="tab_desk">డెస్క్ మోడ్</span>
        </button>
        <button onclick="switchAppTab('reciprocity')" id="head-tab-recip" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-stone-700 hover:bg-stone-100 hidden sm:flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"></path></svg>
          <span data-i18n="tab_reciprocity">సరితూకం</span>
        </button>
        <button onclick="switchAppTab('ledger')" id="head-tab-ledger" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-stone-700 hover:bg-stone-100 hidden sm:flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path><path d="M6 6h10"></path><path d="M6 10h10"></path></svg>
          <span data-i18n="tab_ledger">లెడ్జర్</span>
        </button>
      </div>

      <!-- Right Header Actions: Temple Audio, Prominent Language Dropdown & Auth CTAs -->
      <div class="flex items-center gap-2">
        
        <!-- Sacred Temple Bell Chime -->
        <button id="btn-chime-toggle" onclick="toggleChimeAudio()" title="శుభ శంఖారావం / Temple Bell" class="w-8.5 h-8.5 rounded-lg border border-stone-200 bg-white hover:bg-amber-50 text-amber-700 flex items-center justify-center transition-all">
          <svg id="bell-icon" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
          </svg>
        </button>

        <!-- Prominent Language Selection Dropdown (Permanently in Header as requested) -->
        <div class="relative flex items-center">
          <div class="flex items-center bg-white border border-amber-300 rounded-lg px-2 py-1 shadow-2xs hover:border-amber-500 transition-colors">
            <svg class="w-3.5 h-3.5 text-amber-700 mr-1.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="2" y1="12" x2="22" y2="12"></line>
              <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
            </svg>
            <select id="header-language-select" onchange="applyLanguage(this.value)" class="text-xs font-bold text-stone-800 bg-transparent focus:outline-hidden cursor-pointer">
              <option value="te" selected>తెలుగు (Telugu)</option>
              <option value="en">English (EN)</option>
              <option value="hi">हिन्दी (Hindi)</option>
            </select>
          </div>
        </div>

        <!-- Auth CTAs (Landing Mode) -->
        <div id="landing-auth-ctas" class="flex items-center gap-2">
          <button onclick="navigateToPage('auth')" class="h-8.5 px-3 rounded-lg border border-stone-200 text-stone-700 hover:bg-stone-100 text-xs font-semibold">
            <span data-i18n="btn_login_nav">లాగిన్</span>
          </button>
          <button onclick="enterAsGuest()" class="h-8.5 px-3.5 rounded-lg gold-btn text-xs font-bold shadow-xs">
            <span data-i18n="btn_get_started">ప్రారంభించండి</span>
          </button>
        </div>

        <!-- User Profile Pill (App Mode) -->
        <div id="app-user-pill" class="hidden items-center gap-2">
          <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-stone-100 border border-stone-200 text-xs font-semibold">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span id="user-display-name">గెస్ట్ అకౌంట్</span>
          </div>
          <button onclick="logoutToLanding()" title="లాగౌట్" class="h-8.5 px-2 text-stone-400 hover:text-rose-600 text-xs font-bold">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
          </button>
        </div>

      </div>

    </div>
  </header>

  <!-- ============================================================== -->
  <!-- 2. PAGE 1: LUXURY BRAND LANDING PAGE -->
  <!-- ============================================================== -->
  <main id="page-landing" class="page-section active-page flex-1">
    
    <!-- Hero Section -->
    <section class="max-w-7xl mx-auto px-4 lg:px-8 py-12 lg:py-20">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Hero Text -->
        <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
          
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-100/80 border border-amber-300 text-amber-900 text-xs font-bold">
            <svg class="w-3.5 h-3.5 text-amber-800" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"></circle><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"></path></svg>
            <span data-i18n="hero_badge">50,000+ భారతీయ కుటుంబాల నమ్మకమైన డిజిటల్ లెడ్జర్</span>
          </div>

          <h1 class="font-cinzel text-3xl sm:text-5xl lg:text-6xl font-black text-stone-900 tracking-tight leading-[1.15]" data-i18n="hero_h1">
            ఎర్ర పుస్తకం పోయింది.<br>
            <span class="text-amber-800 font-telugu">చదివింపుల లెక్కల బాధ తీరింది.</span>
          </h1>

          <p class="text-stone-600 text-sm sm:text-base leading-relaxed max-w-2xl font-telugu" data-i18n="hero_desc">
            వివాహాలు, గృహప్రవేశాలు, లంగా ఓణీల వేడుకలు, ఒడుగులు మరియు పుట్టినరోజులలో వచ్చే ప్రతి రూపాయి, బంగారు కానుకలను క్షణాల్లో నమోదు చేయండి. ఇంటర్నెట్ లేకపోయినా 100% ఆఫ్‌లైన్ డెస్క్ మోడ్, UPI క్యూఆర్ స్టాండీ, మరియు ఎవరికి ఎంత ఇచ్చామో తెలిపే ఆటోమేటిక్ సరితూకం!
          </p>

          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-3 pt-2">
            <button onclick="enterAsGuest()" class="w-full sm:w-auto h-11 px-6 rounded-xl gold-btn font-bold text-xs flex items-center justify-center gap-2 shadow-md">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              <span data-i18n="hero_cta_demo">డెమో చూడండి / గెస్ట్‌గా ప్రారంభించండి</span>
            </button>
            <button onclick="navigateToPage('auth')" class="w-full sm:w-auto h-11 px-5 rounded-xl bg-white border border-stone-200 hover:bg-stone-50 text-stone-800 font-semibold text-xs flex items-center justify-center gap-2">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              <span data-i18n="hero_cta_login">లాగిన్ (Google / OTP)</span>
            </button>
          </div>

          <!-- Trust Metrics Strip -->
          <div class="grid grid-cols-3 gap-4 pt-6 border-t border-stone-200/80 max-w-lg mx-auto lg:mx-0">
            <div>
              <div class="text-stone-900 font-black text-lg sm:text-xl font-cinzel">50,000+</div>
              <div class="text-[11px] text-stone-500 font-medium" data-i18n="stat_weddings">శుభకార్యాలు</div>
            </div>
            <div>
              <div class="text-amber-800 font-black text-lg sm:text-xl font-cinzel">₹100 Cr+</div>
              <div class="text-[11px] text-stone-500 font-medium" data-i18n="stat_tracked">నమోదైన చదివింపులు</div>
            </div>
            <div>
              <div class="text-emerald-700 font-black text-lg sm:text-xl font-cinzel">100%</div>
              <div class="text-[11px] text-stone-500 font-medium" data-i18n="stat_offline">ఆఫ్‌లైన్ భద్రత</div>
            </div>
          </div>

        </div>

        <!-- Hero Glassmorphic Device Showcase -->
        <div class="lg:col-span-5 flex justify-center">
          <div class="w-full max-w-[340px] rounded-[42px] bg-stone-950 p-2.5 shadow-2xl border-4 border-stone-800">
            <div class="rounded-[34px] bg-[#FAF9F6] overflow-hidden p-4 space-y-3.5">
              
              <div class="flex items-center justify-between text-[10px] font-bold text-stone-500 pb-1 border-b border-stone-100">
                <span>10:30 AM</span>
                <span class="text-amber-800 font-semibold">ఆనంద్ & శ్రేయ వివాహం</span>
                <span>🔋 100%</span>
              </div>

              <div class="grid grid-cols-2 gap-2 text-left">
                <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200/80">
                  <span class="text-[9px] font-bold text-emerald-800 uppercase block">వచ్చినవి (In)</span>
                  <span class="font-cinzel text-sm font-bold text-emerald-950">₹2,45,616</span>
                </div>
                <div class="p-2.5 rounded-xl bg-amber-50 border border-amber-200/80">
                  <span class="text-[9px] font-bold text-amber-800 uppercase block">ఇచ్చినవి (Out)</span>
                  <span class="font-cinzel text-sm font-bold text-amber-950">₹1,18,500</span>
                </div>
              </div>

              <div class="p-3 rounded-xl bg-white border border-stone-200/90 shadow-2xs space-y-2 text-left">
                <div class="text-[10px] font-bold text-stone-700 uppercase">కౌంటర్ #1 లైవ్ ఎంట్రీ</div>
                <input readonly value="కొత్తపల్లి శ్రీనివాస్ (గుంటూరు)" class="w-full h-8 px-2 text-[11px] bg-stone-50 border border-stone-200 rounded-lg text-stone-800">
                <div class="flex items-center gap-1">
                  <span class="h-6 px-2 text-[10px] font-bold rounded-md bg-amber-50 text-amber-900 border border-amber-300">₹1,116</span>
                  <span class="h-6 px-2 text-[10px] font-bold rounded-md bg-stone-100 text-stone-700">₹2,116</span>
                  <span class="h-6 px-2 text-[10px] font-bold rounded-md bg-stone-100 text-stone-700">₹5,116</span>
                </div>
                <button onclick="enterAsGuest()" class="w-full h-8 rounded-lg gold-btn text-[11px] font-bold flex items-center justify-center gap-1">
                  <span>నమోదు చేసి చూడండి →</span>
                </button>
              </div>

              <div class="text-center text-[10px] text-stone-400">
                100% ఆఫ్‌లైన్ • జీరో యాడ్స్ • తక్షణ WhatsApp రశీదు
              </div>

            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- Section 2: Comparison -->
    <section id="comparison" class="max-w-7xl mx-auto px-4 lg:px-8 py-16 border-t border-stone-200/80">
      <div class="text-center max-w-3xl mx-auto mb-12 space-y-3">
        <span class="text-xs font-bold uppercase tracking-widest px-3 py-1 rounded-full bg-amber-100 text-amber-900 border border-amber-300">
          విశ్వసనీయత & నాణ్యత
        </span>
        <h2 class="font-cinzel text-2xl sm:text-4xl font-extrabold text-stone-900" data-i18n="comp_title">
          మార్కెట్లోని యాప్‌లకు & GiftVault కి మధ్య తేడా ఏమిటి?
        </h2>
        <p class="text-xs sm:text-sm text-stone-600 font-telugu" data-i18n="comp_sub">
          Chadivimpulu, ShagunBook, లేదా పాత ఎర్ర పుస్తకాలతో ఎదురయ్యే సమస్యలను GiftVault ఎలా పరిష్కరిస్తుందో చూడండి:
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <div class="p-6 rounded-3xl glass-card space-y-3">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          </div>
          <h3 class="font-bold text-base text-stone-900" data-i18n="comp_card1_title">నెట్‌వర్క్ స్లో & యాడ్స్ సమస్య లేదు</h3>
          <p class="text-xs text-stone-600 leading-relaxed font-telugu" data-i18n="comp_card1_desc">
            కల్యాణ మండపాలలో నెట్‌వర్క్ రాక ఇతర యాప్‌లు లోడింగ్ అవుతూ ఆగిపోతాయి లేదా వీడియో యాడ్స్ వస్తాయి. GiftVault 100% ఆఫ్‌లైన్ లో కేవలం 3 సెకన్లలో ఎంట్రీ పూర్తి చేస్తుంది.
          </p>
        </div>

        <div class="p-6 rounded-3xl glass-card space-y-3">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"></path></svg>
          </div>
          <h3 class="font-bold text-base text-stone-900" data-i18n="comp_card2_title">ఇచ్చినవి vs వచ్చినవి (సరితూకం)</h3>
          <p class="text-xs text-stone-600 leading-relaxed font-telugu" data-i18n="comp_card2_desc">
            సాధారణ యాప్‌లలో కేవలం నేటి లిస్ట్ మాత్రమే ఉంటుంది. GiftVault లో గతంలో ఆ బంధువులకు మనం ఎంత ఇచ్చామో ఆటోమేటిక్ గా పోల్చి చూపిస్తుంది.
          </p>
        </div>

        <div class="p-6 rounded-3xl glass-card space-y-3">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"></path></svg>
          </div>
          <h3 class="font-bold text-base text-stone-900" data-i18n="comp_card3_title">30-రోజుల రీసైకిల్ బిన్ రక్షణ</h3>
          <p class="text-xs text-stone-600 leading-relaxed font-telugu" data-i18n="comp_card3_desc">
            ఫోన్ మార్చినా లేదా పొరపాటున ఎంట్రీ డిలీట్ చేసినా కంగారు పడక్కర్లేదు. రీసైకిల్ బిన్ మరియు గూగుల్ డ్రైవ్ ఎన్‌క్రిప్టెడ్ బ్యాకప్ ద్వారా మీ డేటా ఎప్పటికీ సురక్షితం.
          </p>
        </div>

      </div>
    </section>

    <!-- Section 3: Shagun ROI Calculator -->
    <section id="calculator" class="max-w-7xl mx-auto px-4 lg:px-8 py-16 border-t border-stone-200/80">
      <div class="p-8 sm:p-12 rounded-3xl bg-stone-900 text-white shadow-xl">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
          
          <div class="space-y-4">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-widest" data-i18n="calc_badge">
              నష్టాన్ని అరికట్టే లెక్కల సాధనం
            </span>
            <h2 class="font-cinzel text-2xl sm:text-3xl font-bold" data-i18n="calc_h2">
              మీ పెళ్ళిలో ఎంత మొత్తం మిస్ అవ్వకుండా కాపాడవచ్చు?
            </h2>
            <p class="text-xs text-stone-300 leading-relaxed font-telugu" data-i18n="calc_desc">
              సాంప్రదాయ ఎర్ర పుస్తకాలలో రద్దీ వల్ల దాదాపు 3% నుండి 5% చదివింపులు తప్పుగా రాయడం లేదా ఎన్వలప్‌లు పోవడం జరుగుతుంది.
            </p>
            
            <div class="space-y-2 pt-2">
              <label class="block text-xs font-bold text-stone-300">మీ శుభకార్యానికి హాజరయ్యే అంచనా అతిథులు:</label>
              <input id="calc-guests-input" type="range" min="100" max="2000" value="600" step="50" oninput="updateShagunCalculator(this.value)" class="w-full accent-amber-400">
              <div class="flex justify-between text-xs font-bold text-amber-300">
                <span>100 మంది</span>
                <span id="calc-guests-val" class="text-white text-sm">600 మంది అతిథులు</span>
                <span>2000 మంది</span>
              </div>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-stone-950/80 border border-amber-400/30 text-center space-y-3">
            <span class="text-xs font-bold text-stone-400 uppercase tracking-wider">GiftVault ద్వారా మీరు ఆదా చేసే మొత్తం:</span>
            <div id="calc-saved-val" class="font-cinzel text-3xl sm:text-4xl font-black text-amber-400">
              ₹42,500
            </div>
            <p class="text-[11px] text-stone-400 font-telugu">
              (లెక్కింపుల్లో దొర్లే తప్పులు, రికార్డు కాని కవర్లు, మరియు పోయిన సమాచారాన్ని 100% నివారిస్తుంది)
            </p>
            <button onclick="enterAsGuest()" class="h-10 px-6 rounded-xl gold-btn text-xs font-bold">
              ఇప్పుడే సురక్షితంగా రికార్డ్ చేయండి →
            </button>
          </div>

        </div>
      </div>
    </section>

  </main>

  <!-- ============================================================== -->
  <!-- 3. PAGE 2: AUTHENTICATION (లాగిన్ పేజ్) -->
  <!-- ============================================================== -->
  <div id="page-auth" class="page-section max-w-md mx-auto px-4 py-16 my-auto flex-1">
    <div class="p-8 rounded-3xl glass-card space-y-6 text-center">
      
      <div class="w-14 h-14 mx-auto rounded-2xl bg-[#0F1117] p-0.5 shadow-md flex items-center justify-center">
        <svg class="w-8 h-8 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
          <path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/>
          <path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/>
        </svg>
      </div>

      <div>
        <h2 class="font-cinzel text-xl font-bold text-stone-900" data-i18n="auth_heading">GiftVault లోకి ప్రవేశించండి</h2>
        <p class="text-xs text-stone-500 mt-1 font-telugu" data-i18n="auth_sub">మీ కుటుంబ శుభకార్యాల లెక్కలను సురక్షితంగా నిర్వహించండి</p>
      </div>

      <button onclick="loginWithGoogle()" class="w-full h-11 px-4 rounded-xl bg-white border border-stone-300 hover:bg-stone-50 text-stone-800 font-semibold text-xs flex items-center justify-center gap-3 shadow-xs">
        <svg class="w-4 h-4" viewBox="0 0 24 24">
          <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
          <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
          <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
          <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
        </svg>
        <span data-i18n="btn_google_signin">Google ఖాతాతో సైన్ ఇన్ చేయండి</span>
      </button>

      <div class="flex items-center gap-2 text-[10px] text-stone-400 uppercase tracking-widest">
        <span class="flex-1 h-px bg-stone-200"></span>
        <span data-i18n="auth_or">లేదా</span>
        <span class="flex-1 h-px bg-stone-200"></span>
      </div>

      <div class="space-y-2 text-left">
        <label class="block text-[11px] font-bold text-stone-600" data-i18n="label_phone_login">మొబైల్ నెంబర్:</label>
        <div class="flex gap-2">
          <input id="auth-phone-input" type="tel" placeholder="+91 98765 43210" class="flex-1 h-9 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500">
          <button onclick="sendOtpSim()" class="h-9 px-3 rounded-lg bg-stone-900 text-white font-bold text-xs" data-i18n="btn_get_otp">OTP పొందండి</button>
        </div>
      </div>

      <div class="pt-2">
        <button onclick="enterAsGuest()" class="w-full h-10 rounded-xl bg-amber-50 hover:bg-amber-100 border border-amber-300 text-amber-900 font-bold text-xs flex items-center justify-center gap-2">
          <svg class="w-4 h-4 text-amber-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          <span data-i18n="btn_guest_mode">గెస్ట్ మోడ్ (లాగిన్ లేకుండా డెమో చూడండి)</span>
        </button>
      </div>

      <p class="text-[10px] text-stone-400 font-telugu">
        100% సురక్షితం • మీ కాంటాక్ట్స్ లేదా ఫైనాన్షియల్ డేటాను మేము ఎవరికీ షేర్ చేయము.
      </p>

    </div>
  </div>

  <!-- ============================================================== -->
  <!-- 4. PAGE 3: MAIN APP WORKSPACE -->
  <!-- ============================================================== -->
  <div id="page-app" class="page-section max-w-7xl mx-auto px-4 lg:px-8 py-6 w-full flex-1">
    
    <!-- Active Event Bar -->
    <div class="mb-6 p-4 rounded-2xl glass-card flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
      <div class="flex items-center gap-3.5">
        <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-amber-500/20 to-amber-200/40 border border-amber-400/40 flex items-center justify-center text-amber-800 shadow-xs">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/><path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/></svg>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h2 id="app-event-name" class="font-bold text-stone-900 text-base sm:text-lg">
              ఆనంద్ & శ్రేయ వివాహ మహోత్సవం
            </h2>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-300">
              లైవ్ కౌంటర్ ఆన్
            </span>
          </div>
          <p id="app-event-meta" class="text-xs text-stone-500">
            శ్రీ కన్వెన్షన్ హాల్, హైదరాబాద్ • ముహూర్తం: 15 నవంబర్ 2026, ఉదయం 9:15 ని.లకు
          </p>
        </div>
      </div>

      <div class="flex items-center gap-2 self-stretch sm:self-auto justify-end">
        <button onclick="openModalNewEvent()" class="h-9 px-3.5 text-xs font-semibold rounded-lg bg-stone-900 hover:bg-stone-800 text-white flex items-center gap-1.5 shadow-sm">
          <span>+</span>
          <span data-i18n="btn_add_event">కొత్త శుభకార్యం</span>
        </button>
        <button onclick="switchAppTab('events')" class="h-9 px-3 text-xs font-semibold rounded-lg border border-stone-200 hover:bg-stone-100 text-stone-700 flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg>
          <span data-i18n="btn_all_events">ఈవెంట్లు</span>
        </button>
      </div>
    </div>

    <!-- SUB-TAB 1: EXECUTIVE DASHBOARD HOME PAGE (హోమ్ పేజ్) -->
    <div id="subtab-dashboard" class="app-screen active-app-screen space-y-6">
      
      <!-- Received, Given, and Net Balance Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        
        <!-- Total Received (వచ్చినవి) -->
        <div class="p-5 rounded-2xl glass-card space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-stone-500 uppercase tracking-wider" data-i18n="metric_received_title">మొత్తం వచ్చినవి (Received)</span>
            <span class="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>
            </span>
          </div>
          <div class="font-cinzel text-2xl sm:text-3xl font-black text-emerald-800" id="dash-received-val">
            ₹2,45,616
          </div>
          <p class="text-[11px] text-stone-500" data-i18n="metric_received_sub">ఈ ఈవెంట్ లో బంధువులు సమర్పించిన చదివింపులు</p>
        </div>

        <!-- Total Given (మనం ఇచ్చినవి) -->
        <div class="p-5 rounded-2xl glass-card space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-stone-500 uppercase tracking-wider" data-i18n="metric_given_title">మనం ఇచ్చినవి (Given)</span>
            <span class="w-8 h-8 rounded-lg bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
            </span>
          </div>
          <div class="font-cinzel text-2xl sm:text-3xl font-black text-amber-900" id="dash-given-val">
            ₹1,18,500
          </div>
          <p class="text-[11px] text-stone-500" data-i18n="metric_given_sub">గతంలో వారి ఫంక్షన్లలో మన కుటుంబం చదివించినవి</p>
        </div>

        <!-- Net Balance (సరితూకం / బ్యాలెన్స్) -->
        <div class="p-5 rounded-2xl bg-stone-900 text-white space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider" data-i18n="metric_net_title">నికర బ్యాలెన్స్ (Net Balance)</span>
            <span class="w-8 h-8 rounded-lg bg-amber-400/20 text-amber-400 flex items-center justify-center text-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"></path></svg>
            </span>
          </div>
          <div class="font-cinzel text-2xl sm:text-3xl font-black text-white" id="dash-net-val">
            +₹1,27,116
          </div>
          <p class="text-[11px] text-stone-400" data-i18n="metric_net_sub">మన కుటుంబానికి అనుకూలమైన సర్ప్లస్ బ్యాలెన్స్</p>
        </div>

      </div>

      <!-- Category Breakdown Strip -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
        <div class="p-3.5 rounded-xl glass-card">
          <span class="text-[10px] font-bold text-stone-500 uppercase block" data-i18n="cat_cash_label">నగదు చదివింపులు</span>
          <span id="dash-cat-cash" class="font-cinzel text-base font-bold text-stone-900">₹1,92,152</span>
        </div>
        <div class="p-3.5 rounded-xl glass-card">
          <span class="text-[10px] font-bold text-stone-500 uppercase block" data-i18n="cat_gold_label">బంగారం / వెండి</span>
          <span id="dash-cat-gold" class="text-base font-bold text-amber-800">14 గ్రాములు</span>
        </div>
        <div class="p-3.5 rounded-xl glass-card">
          <span class="text-[10px] font-bold text-stone-500 uppercase block" data-i18n="cat_upi_label">UPI / QR పేమెంట్స్</span>
          <span id="dash-cat-upi" class="text-base font-bold text-emerald-800">₹42,348</span>
        </div>
        <div class="p-3.5 rounded-xl glass-card">
          <span class="text-[10px] font-bold text-stone-500 uppercase block" data-i18n="cat_items_label">గిఫ్ట్ వస్తువులు</span>
          <span id="dash-cat-items" class="text-base font-bold text-stone-900">24 వస్తువులు</span>
        </div>
      </div>

      <!-- Quick Action Buttons Hub -->
      <div class="flex flex-wrap gap-2.5">
        <button onclick="switchAppTab('desk')" class="h-10 px-4 rounded-xl gold-btn text-xs font-bold flex items-center gap-2 shadow-xs">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          <span data-i18n="btn_open_desk_counter">కౌంటర్ డెస్క్ మోడ్ తెరవండి</span>
        </button>
        <button onclick="switchAppTab('reciprocity')" class="h-10 px-4 rounded-xl bg-white border border-stone-200 hover:bg-stone-50 text-stone-800 text-xs font-semibold flex items-center gap-1.5 shadow-2xs">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"></path></svg>
          <span data-i18n="btn_check_recip">సరితూకం (ఇచ్చినవి vs వచ్చినవి)</span>
        </button>
        <button onclick="switchAppTab('qr')" class="h-10 px-4 rounded-xl bg-white border border-stone-200 hover:bg-stone-50 text-stone-800 text-xs font-semibold flex items-center gap-1.5 shadow-2xs">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"></rect><rect width="4" height="4" x="7" y="7"></rect><rect width="4" height="4" x="13" y="7"></rect><rect width="4" height="4" x="7" y="13"></rect><path d="M13 13h4v4h-4z"></path></svg>
          <span data-i18n="btn_view_upi_qr">UPI QR స్టాండీ</span>
        </button>
        <button onclick="switchAppTab('ledger')" class="h-10 px-4 rounded-xl bg-white border border-stone-200 hover:bg-stone-50 text-stone-800 text-xs font-semibold flex items-center gap-1.5 shadow-2xs">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path><path d="M6 6h10"></path><path d="M6 10h10"></path></svg>
          <span data-i18n="btn_full_ledger_export">ఎర్ర బాహీఖాతా రిపోర్ట్స్ & PDF</span>
        </button>
      </div>

      <!-- Live Recent Feed -->
      <div class="p-5 rounded-2xl glass-card space-y-3">
        <div class="flex items-center justify-between border-b border-stone-100 pb-2">
          <span class="text-xs font-bold text-stone-900 uppercase tracking-wider" data-i18n="recent_stream_title">తాజా చదివింపులు (Real-time Stream)</span>
          <button onclick="switchAppTab('ledger')" class="text-xs font-semibold text-amber-800 hover:underline" data-i18n="view_all_link">మొత్తం లెడ్జర్ →</button>
        </div>
        <div id="dash-recent-stream" class="space-y-2">
          <!-- Populated by JS -->
        </div>
      </div>

    </div>

    <!-- SUB-TAB 2: HIGH-SPEED DESK CONTINUOUS MODE (డెస్క్ మోడ్) -->
    <div id="subtab-desk" class="app-screen space-y-4">
      <div class="p-4 rounded-xl bg-stone-900 text-white flex items-center justify-between shadow-xs">
        <div>
          <span class="text-xs text-amber-300 font-bold uppercase tracking-wider">హై-స్పీడ్ కౌంటర్ మోడ్ • లైవ్ రికార్డింగ్</span>
          <div class="font-bold text-lg text-white flex items-baseline gap-1 mt-0.5">
            <span class="text-xs text-amber-400">₹</span>
            <span id="desk-screen-total" class="font-cinzel text-xl">2,45,616</span>
          </div>
        </div>
        <div class="text-right">
          <span class="text-xs text-stone-400">మొత్తం చదివింపులు</span>
          <div id="desk-screen-count" class="font-bold text-base text-stone-200">18 మంది</div>
        </div>
      </div>

      <!-- Continuous Entry Form -->
      <div id="desk-continuous-card" class="p-6 rounded-2xl glass-card space-y-3.5">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_name">అతిథి పేరు *</label>
            <input id="desk-input-name" type="text" placeholder="ఉదా: కొత్తపల్లి శ్రీనివాసరావు" class="w-full h-10 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white focus:outline-hidden">
          </div>
          <div>
            <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_city">ఊరు / గ్రామం</label>
            <input id="desk-input-city" type="text" placeholder="ఉదా: గుంటూరు / తెనాలి" class="w-full h-10 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white focus:outline-hidden">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_relation">సంబంధం</label>
            <select id="desk-select-relation" class="w-full h-10 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500">
              <option value="దగ్గరి బంధువులు">దగ్గరి బంధువులు</option>
              <option value="మేనమామ తరఫు">మేనమామ తరఫు</option>
              <option value="వియ్యంకులు">వియ్యంకులు</option>
              <option value="స్నేహితులు">స్నేహితులు</option>
              <option value="సహోద్యోగులు">సహోద్యోగులు</option>
              <option value="గ్రామస్థులు">గ్రామస్థులు</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_gift_type">కానుక రకం</label>
            <select id="desk-select-gift-type" class="w-full h-10 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 font-semibold text-amber-900">
              <option value="నగదు">నగదు (Cash)</option>
              <option value="బంగారం/వెండి">బంగారం / వెండి (Gold/Silver)</option>
              <option value="గిఫ్ట్ వస్తువు">గిఫ్ట్ వస్తువు (Gift Item)</option>
              <option value="UPI / QR">UPI / QR ట్రాన్స్‌ఫర్</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_amount">చదివింపు మొత్తం (₹) *</label>
          <div class="relative">
            <span class="absolute left-3 top-2.5 text-xs font-bold text-stone-400">₹</span>
            <input id="desk-input-amount" type="number" value="1116" class="w-full h-10 pl-7 pr-3 text-sm font-bold text-stone-900 bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white focus:outline-hidden">
          </div>
        </div>

        <div>
          <span class="text-[10px] font-bold text-stone-500 uppercase tracking-wider block mb-1" data-i18n="label_quick_shagun">త్వరిత శుభ మొత్తాలు</span>
          <div class="flex flex-wrap gap-2">
            <button onclick="setDeskAmount(516)" class="h-7 px-3 text-xs font-bold rounded-lg bg-stone-100 hover:bg-amber-100 text-stone-700 border border-stone-200">₹516</button>
            <button onclick="setDeskAmount(1116)" class="h-7 px-3 text-xs font-bold rounded-lg bg-amber-50 text-amber-900 border border-amber-300">₹1,116</button>
            <button onclick="setDeskAmount(2116)" class="h-7 px-3 text-xs font-bold rounded-lg bg-stone-100 hover:bg-amber-100 text-stone-700 border border-stone-200">₹2,116</button>
            <button onclick="setDeskAmount(5116)" class="h-7 px-3 text-xs font-bold rounded-lg bg-stone-100 hover:bg-amber-100 text-stone-700 border border-stone-200">₹5,116</button>
            <button onclick="setDeskAmount(11116)" class="h-7 px-3 text-xs font-bold rounded-lg bg-stone-100 hover:bg-amber-100 text-stone-700 border border-stone-200">₹11,116</button>
          </div>
        </div>

        <div class="grid grid-cols-3 gap-2 items-center">
          <div class="col-span-2">
            <input id="desk-input-notes" type="text" placeholder="గమనిక (ఉదా: 2 గ్రాములు / కవరు నెం.12)" class="w-full h-9 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg">
          </div>
          <div>
            <button onclick="simulatePhotoCapture()" id="desk-btn-photo" class="w-full h-9 px-2 text-xs font-bold rounded-lg border border-stone-200 hover:bg-stone-50 text-stone-700 flex items-center justify-center gap-1.5">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
              <span id="desk-photo-label">ఫోటో స్నాప్</span>
            </button>
          </div>
        </div>

        <div class="pt-2 flex gap-3">
          <button onclick="saveLiveDeskEntry()" class="flex-1 h-11 rounded-xl gold-btn font-bold text-xs flex items-center justify-center gap-2 shadow-sm">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
            <span data-i18n="btn_save_record">నమోదు చేయండి (Enter)</span>
          </button>
          <button onclick="resetLiveDeskInputs()" class="h-11 px-4 rounded-xl border border-stone-200 text-stone-600 hover:bg-stone-50 text-xs font-semibold">
            <span>క్లియర్</span>
          </button>
        </div>

      </div>
    </div>

    <!-- SUB-TAB 3: RECIPROCITY ENGINE (సరితూకం) -->
    <div id="subtab-reciprocity" class="app-screen space-y-4">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
        <div>
          <h3 class="font-bold text-stone-900 text-base" data-i18n="heading_reciprocity">ఇచ్చినవి vs వచ్చినవి (సరితూకం)</h3>
          <p class="text-xs text-stone-500 font-telugu" data-i18n="sub_reciprocity">గతంలో వారి ఫంక్షన్లలో మనం ఎంత ఇచ్చామో క్షణాల్లో తెలుసుకోండి.</p>
        </div>
        <div class="relative w-full sm:w-64">
          <span class="absolute left-3 top-2.5 text-xs text-stone-400">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </span>
          <input id="search-recip-input" oninput="filterReciprocity(this.value)" type="text" placeholder="అతిథి పేరుతో వెతకండి..." class="w-full h-9 pl-8 pr-3 text-xs bg-white border border-stone-200 rounded-lg focus:border-amber-500">
        </div>
      </div>

      <div id="reciprocity-cards-grid" class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
        <!-- Dynamic Cards -->
      </div>
    </div>

    <!-- SUB-TAB 4: DIGITAL RED BAHIKHATA PASSBOOK LEDGER (లెడ్జర్) -->
    <div id="subtab-ledger" class="app-screen space-y-4">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 border-b border-stone-200 pb-3">
        <div>
          <h3 class="font-bold text-stone-900 text-base" data-i18n="heading_ledger">ఎర్ర బాహీఖాతా లెడ్జర్ & రిపోర్ట్స్</h3>
          <p class="text-xs text-stone-500 font-telugu" data-i18n="sub_ledger">ప్రతి పైసా పారదర్శక రికార్డు</p>
        </div>
        <div class="flex gap-2">
          <button onclick="exportToCsv()" class="h-8.5 px-3 rounded-lg bg-stone-100 hover:bg-stone-200 text-stone-800 text-xs font-bold flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Excel / CSV</span>
          </button>
          <button onclick="exportToPdf()" class="h-8.5 px-3.5 rounded-lg bg-stone-900 hover:bg-stone-800 text-white text-xs font-bold flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect width="12" height="8" x="6" y="14"></rect></svg>
            <span>PDF ప్రింట్</span>
          </button>
        </div>
      </div>

      <div id="ledger-table-container" class="space-y-2">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- SUB-TAB 5: DIGITAL UPI QR STANDEE -->
    <div id="subtab-qr" class="app-screen space-y-4 text-center">
      <div class="max-w-md mx-auto p-6 rounded-3xl glass-card space-y-4">
        <div class="flex items-center justify-center gap-2">
          <span class="font-cinzel text-xs font-bold text-amber-900 tracking-wider">GIFTVAULT SHAGUN QR</span>
        </div>

        <div class="w-48 h-48 mx-auto p-2 bg-stone-50 border border-stone-200 rounded-2xl flex items-center justify-center">
          <svg viewBox="0 0 100 100" class="w-full h-full text-stone-900" fill="currentColor">
            <rect x="0" y="0" width="30" height="30" fill="currentColor" rx="4"/>
            <rect x="5" y="5" width="20" height="20" fill="white" rx="2"/>
            <rect x="9" y="9" width="12" height="12" fill="#8E1E24" rx="1"/>

            <rect x="70" y="0" width="30" height="30" fill="currentColor" rx="4"/>
            <rect x="75" y="5" width="20" height="20" fill="white" rx="2"/>
            <rect x="79" y="9" width="12" height="12" fill="#8E1E24" rx="1"/>

            <rect x="0" y="70" width="30" height="30" fill="currentColor" rx="4"/>
            <rect x="5" y="75" width="20" height="20" fill="white" rx="2"/>
            <rect x="9" y="79" width="12" height="12" fill="#8E1E24" rx="1"/>

            <rect x="36" y="8" width="8" height="8" fill="currentColor"/>
            <rect x="48" y="14" width="8" height="8" fill="currentColor"/>
            <rect x="38" y="38" width="24" height="24" fill="#C5A059" rx="4"/>
            <text x="50" y="54" font-size="12" text-anchor="middle" fill="white" font-weight="bold">₹</text>
            <rect x="76" y="72" width="18" height="18" fill="currentColor"/>
          </svg>
        </div>

        <div>
          <h4 class="font-bold text-sm text-stone-900">ఆనంద్ వర్మ & శ్రేయారెడ్డి</h4>
          <p class="text-xs text-stone-500">UPI ID: anand.shreya@hdfcbank</p>
        </div>

        <button onclick="simulateUpiSoundbox()" class="h-10 px-5 rounded-xl bg-emerald-700 hover:bg-emerald-800 text-white font-bold text-xs inline-flex items-center gap-2 shadow-xs">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
          <span data-i18n="btn_soundbox_test">సౌండ్‌బాక్స్ వాయిస్ టెస్ట్ (₹2,116)</span>
        </button>
        <p id="qr-soundbox-live" class="text-xs text-emerald-800 font-semibold min-h-[16px]"></p>
      </div>
    </div>

    <!-- SUB-TAB 6: EVENTS SELECTOR & CREATOR -->
    <div id="subtab-events" class="app-screen space-y-4">
      <div class="flex items-center justify-between border-b border-stone-200 pb-3">
        <div>
          <h3 class="font-bold text-stone-900 text-base" data-i18n="heading_family_events">మీ శుభకార్యాలు</h3>
          <p class="text-xs text-stone-500 font-telugu" data-i18n="sub_select_or_create">ఈవెంట్ ఎంచుకోండి లేదా కొత్తది జోడించండి</p>
        </div>
        <button onclick="openModalNewEvent()" class="h-8.5 px-3.5 rounded-lg bg-stone-900 text-white text-xs font-bold flex items-center gap-1.5 shadow-xs">
          <span>+</span>
          <span data-i18n="btn_add_event">కొత్త శుభకార్యం</span>
        </button>
      </div>

      <div id="app-events-grid" class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- SUB-TAB 7: 30-DAY RECYCLE BIN & SETTINGS -->
    <div id="subtab-settings" class="app-screen space-y-4">
      <div>
        <h3 class="font-bold text-stone-900 text-base" data-i18n="heading_vault_security">ఖజానా భద్రత & రీసైకిల్ బిన్</h3>
        <p class="text-xs text-stone-500 font-telugu" data-i18n="sub_recycle_security">ఏ రికార్డూ మిస్ అవ్వదు</p>
      </div>

      <div class="p-5 rounded-2xl glass-card space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-stone-900 flex items-center gap-2">
            <svg class="w-4 h-4 text-stone-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
            <span data-i18n="label_recycle_bin">30 రోజుల రీసైకిల్ బిన్</span>
          </span>
          <span id="app-recycle-count" class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800">2 రికార్డులు</span>
        </div>
        <p class="text-xs text-stone-500 font-telugu" data-i18n="recycle_desc">
          పొరపాటున తొలగించిన ఏ చదివింపు అయినా 30 రోజుల పాటు ఇక్కడ భద్రంగా ఉంటుంది.
        </p>
        <div id="app-recycle-container" class="space-y-2 pt-2">
          <!-- Populated by JS -->
        </div>
      </div>
    </div>

  </div>

  <!-- ============================================================== -->
  <!-- 5. DYNAMIC EVENT CREATOR MODAL WITH CULTURAL PRECISION -->
  <!-- Dynamically changes fields based on category: -->
  <!-- - Wedding / Engagement -> Bride & Groom pair -->
  <!-- - Odugu (ఉపనయనం) / Panchala -> Boy only (Male only) -->
  <!-- - Half Saree (లంగా ఓణీలు) / Pushpavathi -> Girl only (Female only) -->
  <!-- - Birthday / Naming / Mundan -> Child Name + Gender selector + Parents -->
  <!-- - Housewarming -> House Name & Owners -->
  <!-- ============================================================== -->
  <div id="modal-new-event" class="fixed inset-0 bg-stone-950/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4 overflow-y-auto">
    <div class="glass-card rounded-3xl max-w-lg w-full p-6 space-y-4 my-8 shadow-2xl">
      
      <div class="flex items-center justify-between border-b border-stone-200 pb-3">
        <div>
          <h3 class="font-bold text-stone-900 text-base" data-i18n="modal_new_event_title">కొత్త శుభకార్యాన్ని జోడించండి</h3>
          <p class="text-[11px] text-stone-500">కేటగిరీ ఎంచుకోగానే వివరాల ఫారమ్ ఆటోమేటిక్ గా సర్దుబాటు అవుతుంది</p>
        </div>
        <button onclick="closeModalNewEvent()" class="text-stone-400 hover:text-stone-700 font-bold text-lg">✕</button>
      </div>

      <!-- Quick Occasion Category Suggestions Pills -->
      <div>
        <label class="block text-[11px] font-bold text-stone-700 mb-1.5">త్వరిత కేటగిరీ సజెషన్స్ (Quick Suggestions):</label>
        <div class="flex flex-wrap gap-1.5">
          <button type="button" onclick="selectCategorySuggestion('wedding', 'వివాహ మహోత్సవం')" class="h-6 px-2.5 text-[10px] font-bold rounded-md bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-300">💍 వివాహం (Wedding)</button>
          <button type="button" onclick="selectCategorySuggestion('halfsaree', 'శ్రీమతి లంగా ఓణీల శుభవేడుక')" class="h-6 px-2.5 text-[10px] font-bold rounded-md bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-200">👗 లంగా ఓణీల వేడుక (Half Saree)</button>
          <button type="button" onclick="selectCategorySuggestion('odugu', 'చిరంజీవి ఒడుగు / ఉపనయన మహోత్సవం')" class="h-6 px-2.5 text-[10px] font-bold rounded-md bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-200">🪔 ఒడుగు / ఉపనయనం (Odugu)</button>
          <button type="button" onclick="selectCategorySuggestion('panchala', 'పంచల శుభవేడుక (Dhoti Ceremony)')" class="h-6 px-2.5 text-[10px] font-bold rounded-md bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-200">👔 పంచల వేడుక (Dhoti)</button>
          <button type="button" onclick="selectCategorySuggestion('pushpavathi', 'పుష్పవతి / పుష్పాలంకరణ వేడుక')" class="h-6 px-2.5 text-[10px] font-bold rounded-md bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-200">🌸 పుష్పవతి (Mature Fn)</button>
          <button type="button" onclick="selectCategorySuggestion('naming', 'నామకరణం & బారసాల మహోత్సవం')" class="h-6 px-2.5 text-[10px] font-bold rounded-md bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-200">👶 బారసాల (Naming)</button>
          <button type="button" onclick="selectCategorySuggestion('mundan', 'పుట్టెంటకలు & చెవులు కుట్టించే వేడుక')" class="h-6 px-2.5 text-[10px] font-bold rounded-md bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-200">✂️ పుట్టెంటకలు (Mundan)</button>
          <button type="button" onclick="selectCategorySuggestion('housewarming', 'నూతన గృహప్రవేశ మహోత్సవం')" class="h-6 px-2.5 text-[10px] font-bold rounded-md bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-200">🏡 గృహప్రవేశం</button>
          <button type="button" onclick="selectCategorySuggestion('birthday', 'పుట్టినరోజు సంబరాలు (Birthday)')" class="h-6 px-2.5 text-[10px] font-bold rounded-md bg-stone-100 hover:bg-stone-200 text-stone-800 border border-stone-200">🎂 పుట్టినరోజు</button>
        </div>
      </div>

      <div class="space-y-3 text-xs">
        
        <!-- Occasion Category Dropdown -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
          <div>
            <label class="block font-bold text-stone-700 mb-1">శుభకార్యం రకం (Category) *</label>
            <select id="modal-select-cat" onchange="onCategoryChanged(this.value)" class="w-full h-9 px-2.5 bg-stone-50 border border-stone-300 rounded-lg font-bold text-amber-900 focus:border-amber-500">
              <option value="wedding">వివాహం (Wedding - వధూవరులు)</option>
              <option value="halfsaree">లంగా ఓణీల వేడుక (Half Saree - అమ్మాయి మాత్రమే)</option>
              <option value="odugu">ఒడుగు / ఉపనయనం (Odugu - అబ్బాయి మాత్రమే)</option>
              <option value="panchala">పంచల వేడుక (Dhoti Ceremony - అబ్బాయి మాత్రమే)</option>
              <option value="pushpavathi">పుష్పవతి / పుష్పాలంకరణ (Mature Function - అమ్మాయి మాత్రమే)</option>
              <option value="naming">నామకరణం & బారసాల (Cradle & Naming - పాప/బాబు)</option>
              <option value="mundan">పుట్టెంటకలు / కేశఖండన (Mundan - పాప/బాబు)</option>
              <option value="birthday">పుట్టినరోజు (Birthday - బాలుడు/బాలిక)</option>
              <option value="housewarming">గృహప్రవేశం (Housewarming - గృహ యజమానులు)</option>
              <option value="jubilee">షష్టిపూర్తి / శతాబ్ది (60th/80th Jubilee - దంపతులు)</option>
              <option value="custom">ఇతర ప్రత్యేక శుభకార్యం (Custom Event)</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_name">శుభకార్యం పూర్తి పేరు *</label>
            <input id="modal-input-name" type="text" placeholder="ఉదా: రోహిత్ & పూజ వివాహం" class="w-full h-9 px-3 bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 font-semibold">
          </div>
        </div>

        <!-- DYNAMIC PARTICIPANT FIELDS CONTAINER (Changes dynamically based on Category) -->
        <div id="dynamic-participant-fields" class="p-3.5 rounded-xl bg-amber-50/50 border border-amber-200/80 space-y-2.5">
          <!-- Populated by JS onCategoryChanged -->
        </div>

        <!-- Date & Time -->
        <div class="grid grid-cols-2 gap-2.5">
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_date">శుభ ముహూర్తం తేదీ</label>
            <input id="modal-input-date" type="date" value="2026-12-15" class="w-full h-9 px-2.5 bg-stone-50 border border-stone-200 rounded-lg">
          </div>
          <div>
            <label class="block font-bold text-stone-700 mb-1">ముహూర్తం సమయం</label>
            <input id="modal-input-time" type="text" placeholder="ఉదా: ఉదయం 9:15 ని.లకు" class="w-full h-9 px-2.5 bg-stone-50 border border-stone-200 rounded-lg">
          </div>
        </div>

        <!-- Venue & City Autocomplete -->
        <div>
          <label class="block font-bold text-stone-700 mb-1">కల్యాణ మండపం / వేదిక పేరు</label>
          <input id="modal-input-venue" type="text" placeholder="ఉదా: శ్రీ కన్వెన్షన్ హాల్ / స్వగృహం" class="w-full h-9 px-3 bg-stone-50 border border-stone-200 rounded-lg">
        </div>

        <!-- City Autocomplete Input with Dynamic Suggestions Dropdown -->
        <div class="relative">
          <label class="block font-bold text-stone-700 mb-1">ఊరు / సిటీ (టైప్ చేయగానే ఆటోమేటిక్ సజెషన్స్ వస్తాయి) *</label>
          <div class="relative">
            <input id="modal-input-city" type="text" oninput="onCityInputTyped(this.value)" onfocus="onCityInputTyped(this.value)" placeholder="ఉదా: హైదరాబాద్, గుంటూరు, విజయవాడ..." class="w-full h-9 pl-3 pr-8 bg-stone-50 border border-stone-300 rounded-lg focus:border-amber-500 font-semibold text-stone-800">
            <span class="absolute right-2.5 top-2 text-stone-400 text-xs">📍</span>
          </div>

          <!-- Interactive Autocomplete Dropdown List -->
          <div id="city-suggestions-dropdown" class="absolute left-0 right-0 top-full mt-1 bg-white border border-amber-300 rounded-xl shadow-xl max-h-48 overflow-y-auto z-50 hidden">
            <!-- Populated by JS -->
          </div>
        </div>

        <!-- Auto-filled State & Pin code -->
        <div class="grid grid-cols-2 gap-2.5">
          <div>
            <label class="block font-bold text-stone-500 mb-1">రాష్ట్రం (State)</label>
            <input id="modal-input-state" type="text" readonly placeholder="ఆటోమేటిక్ గా వస్తుంది" class="w-full h-8 px-2.5 bg-stone-100 border border-stone-200 rounded-lg text-stone-600">
          </div>
          <div>
            <label class="block font-bold text-stone-500 mb-1">పిన్ కోడ్ (Pincode)</label>
            <input id="modal-input-pincode" type="text" readonly placeholder="పిన్ కోడ్" class="w-full h-8 px-2.5 bg-stone-100 border border-stone-200 rounded-lg text-stone-600">
          </div>
        </div>

      </div>

      <div class="flex items-center justify-end gap-2 pt-2 border-t border-stone-200">
        <button onclick="closeModalNewEvent()" class="h-9 px-4 rounded-lg border border-stone-200 text-stone-600 font-semibold text-xs hover:bg-stone-50" data-i18n="btn_cancel">
          రద్దు (Cancel)
        </button>
        <button onclick="saveModalNewEvent()" class="h-9 px-5 rounded-lg gold-btn font-bold text-xs" data-i18n="btn_save_event">
          ఈవెంట్ సృష్టించండి
        </button>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="max-w-7xl mx-auto px-4 lg:px-8 py-6 border-t border-stone-200/80 text-center text-xs text-stone-500 space-y-1">
    <div class="font-cinzel font-bold text-stone-800 tracking-wider">GIFTVAULT • 24K ROYAL SHAGUN TREASURY</div>
    <p class="font-telugu">100% ఆఫ్‌లైన్ ఫస్ట్ • భారతీయ వివాహాలు & సంస్కృతి సాంప్రదాయాల వేదిక</p>
  </footer>

  <!-- ============================================================== -->
  <!-- 6. JAVASCRIPT MASTER ENGINE -->
  <!-- ============================================================== -->
  <script>
    // -------------------------------------------------------------
    // CITY DATABASE FOR AUTOCOMPLETE (Andhra Pradesh, Telangana & South India)
    // -------------------------------------------------------------
    const CITY_DATABASE = [
      { city: "హైదరాబాద్ (Hyderabad)", state: "తెలంగాణ (Telangana)", pincode: "500001" },
      { city: "గుంటూరు (Guntur)", state: "ఆంధ్రప్రదేశ్ (Andhra Pradesh)", pincode: "522002" },
      { city: "విజయవాడ (Vijayawada)", state: "ఆంధ్రప్రదేశ్", pincode: "520001" },
      { city: "విశాఖపట్నం (Visakhapatnam)", state: "ఆంధ్రప్రదేశ్", pincode: "530002" },
      { city: "తిరుపతి (Tirupati)", state: "ఆంధ్రప్రదేశ్", pincode: "517501" },
      { city: "రాజమండ్రి (Rajahmundry)", state: "ఆంధ్రప్రదేశ్", pincode: "533101" },
      { city: "వరంగల్ (Warangal)", state: "తెలంగాణ", pincode: "506002" },
      { city: "ఖమ్మం (Khammam)", state: "తెలంగాణ", pincode: "507001" },
      { city: "నెల్లూరు (Nellore)", state: "ఆంధ్రప్రదేశ్", pincode: "524001" },
      { city: "కర్నూలు (Kurnool)", state: "ఆంధ్రప్రదేశ్", pincode: "518001" },
      { city: "కరీంనగర్ (Karimnagar)", state: "తెలంగాణ", pincode: "505001" },
      { city: "అనంతపురం (Anantapur)", state: "ఆంధ్రప్రదేశ్", pincode: "515001" },
      { city: "ఒంగోలు (Ongole)", state: "ఆంధ్రప్రదేశ్", pincode: "523001" },
      { city: "ఏలూరు (Eluru)", state: "ఆంధ్రప్రదేశ్", pincode: "534001" },
      { city: "నిజామాబాద్ (Nizamabad)", state: "తెలంగాణ", pincode: "503001" },
      { city: "తెనాలి (Tenali)", state: "ఆంధ్రప్రదేశ్", pincode: "522201" },
      { city: "మచిలీపట్నం (Machilipatnam)", state: "ఆంధ్రప్రదేశ్", pincode: "521001" },
      { city: "నల్గొండ (Nalgonda)", state: "తెలంగాణ", pincode: "508001" },
      { city: "కడప (Kadapa)", state: "ఆంధ్రప్రదేశ్", pincode: "516001" },
      { city: "బెంగళూరు (Bengaluru)", state: "కర్ణాటక", pincode: "560001" },
      { city: "చెన్నై (Chennai)", state: "తమిళనాడు", pincode: "600001" }
    ];

    // -------------------------------------------------------------
    // MULTILINGUAL DICTIONARY
    // -------------------------------------------------------------
    const I18N = {
      te: {
        header_tagline: "రాయల్ శుభకార్య చదివింపుల డిజిటల్ ఖజానా",
        nav_features: "ఫీచర్లు",
        nav_comparison: "పోలిక",
        nav_calculator: "కాలిక్యులేటర్",
        btn_login_nav: "లాగిన్",
        btn_get_started: "ప్రారంభించండి",
        tab_dashboard: "డ్యాష్‌బోర్డ్",
        tab_desk: "డెస్క్ మోడ్",
        tab_reciprocity: "సరితూకం",
        tab_ledger: "లెడ్జర్",
        hero_badge: "50,000+ భారతీయ కుటుంబాల నమ్మకమైన డిజిటల్ లెడ్జర్",
        hero_h1: "ఎర్ర పుస్తకం పోయింది.<br><span class='text-amber-800 font-telugu'>చదివింపుల లెక్కల బాధ తీరింది.</span>",
        hero_desc: "వివాహాలు, గృహప్రవేశాలు, లంగా ఓణీల వేడుకలు, ఒడుగులు మరియు పుట్టినరోజులలో వచ్చే ప్రతి రూపాయి, బంగారు కానుకలను క్షణాల్లో నమోదు చేయండి. ఇంటర్నెట్ లేకపోయినా 100% ఆఫ్‌లైన్ డెస్క్ మోడ్, UPI క్యూఆర్ స్టాండీ, మరియు ఎవరికి ఎంత ఇచ్చామో తెలిపే ఆటోమేటిక్ సరితూకం!",
        hero_cta_demo: "డెమో చూడండి / గెస్ట్‌గా ప్రారంభించండి",
        hero_cta_login: "లాగిన్ (Google / OTP)",
        stat_weddings: "శుభకార్యాలు",
        stat_tracked: "నమోదైన చదివింపులు",
        stat_offline: "ఆఫ్‌లైన్ భద్రత",
        comp_title: "మార్కెట్లోని యాప్‌లకు & GiftVault కి మధ్య తేడా ఏమిటి?",
        comp_sub: "Chadivimpulu, ShagunBook, లేదా పాత ఎర్ర పుస్తకాలతో ఎదురయ్యే సమస్యలను GiftVault ఎలా పరిష్కరిస్తుందో చూడండి:",
        comp_card1_title: "నెట్‌వర్క్ స్లో & యాడ్స్ సమస్య లేదు",
        comp_card1_desc: "కల్యాణ మండపాలలో నెట్‌వర్క్ రాక ఇతర యాప్‌లు లోడింగ్ అవుతూ ఆగిపోతాయి లేదా వీడియో యాడ్స్ వస్తాయి. GiftVault 100% ఆఫ్‌లైన్ లో కేవలం 3 సెకన్లలో ఎంట్రీ పూర్తి చేస్తుంది.",
        comp_card2_title: "ఇచ్చినవి vs వచ్చినవి (సరితూకం)",
        comp_card2_desc: "సాధారణ యాప్‌లలో కేవలం నేటి లిస్ట్ మాత్రమే ఉంటుంది. GiftVault లో గతంలో ఆ బంధువులకు మనం ఎంత ఇచ్చామో ఆటోమేటిక్ గా పోల్చి చూపిస్తుంది.",
        comp_card3_title: "30-రోజుల రీసైకిల్ బిన్ రక్షణ",
        comp_card3_desc: "ఫోన్ మార్చినా లేదా పొరపాటున ఎంట్రీ డిలీట్ చేసినా కంగారు పడక్కర్లేదు. రీసైకిల్ బిన్ మరియు గూగుల్ డ్రైవ్ ఎన్‌క్రిప్టెడ్ బ్యాకప్ ద్వారా మీ డేటా ఎప్పటికీ సురక్షితం.",
        calc_badge: "నష్టాన్ని అరికట్టే లెక్కల సాధనం",
        calc_h2: "మీ పెళ్ళిలో ఎంత మొత్తం మిస్ అవ్వకుండా కాపాడవచ్చు?",
        calc_desc: "సాంప్రదాయ ఎర్ర పుస్తకాలలో రద్దీ వల్ల దాదాపు 3% నుండి 5% చదివింపులు తప్పుగా రాయడం లేదా ఎన్వలప్‌లు పోవడం జరుగుతుంది.",
        auth_heading: "GiftVault లోకి ప్రవేశించండి",
        auth_sub: "మీ కుటుంబ శుభకార్యాల లెక్కలను సురక్షితంగా నిర్వహించండి",
        btn_google_signin: "Google ఖాతాతో సైన్ ఇన్ చేయండి",
        auth_or: "లేదా",
        label_phone_login: "మొబైల్ నెంబర్:",
        btn_get_otp: "OTP పొందండి",
        btn_guest_mode: "గెస్ట్ మోడ్ (లాగిన్ లేకుండా డెమో చూడండి)",
        metric_received_title: "మొత్తం వచ్చినవి (Received)",
        metric_received_sub: "ఈ ఈవెంట్ లో బంధువులు సమర్పించిన చదివింపులు",
        metric_given_title: "మనం ఇచ్చినవి (Given)",
        metric_given_sub: "గతంలో వారి ఫంక్షన్లలో మన కుటుంబం చదివించినవి",
        metric_net_title: "నికర బ్యాలెన్స్ (Net Balance)",
        metric_net_sub: "మన కుటుంబానికి అనుకూలమైన సర్ప్లస్ బ్యాలెన్స్",
        cat_cash_label: "నగదు చదివింపులు",
        cat_gold_label: "బంగారం / వెండి",
        cat_upi_label: "UPI / QR పేమెంట్స్",
        cat_items_label: "గిఫ్ట్ వస్తువులు",
        btn_open_desk_counter: "కౌంటర్ డెస్క్ మోడ్ తెరవండి",
        btn_check_recip: "సరితూకం (ఇచ్చినవి vs వచ్చినవి)",
        btn_view_upi_qr: "UPI QR స్టాండీ",
        btn_full_ledger_export: "ఎర్ర బాహీఖాతా రిపోర్ట్స్ & PDF",
        recent_stream_title: "తాజా చదివింపులు (Real-time Stream)",
        view_all_link: "మొత్తం లెడ్జర్ →",
        label_name: "అతిథి పేరు *",
        label_city: "ఊరు / గ్రామం",
        label_relation: "సంబంధం",
        label_gift_type: "కానుక రకం",
        label_amount: "చదివింపు మొత్తం (₹) *",
        label_quick_shagun: "త్వరిత శుభ మొత్తాలు",
        btn_save_record: "నమోదు చేయండి (Enter)",
        heading_reciprocity: "ఇచ్చినవి vs వచ్చినవి (సరితూకం)",
        sub_reciprocity: "గతంలో వారి ఫంక్షన్లలో మనం ఎంత ఇచ్చామో క్షణాల్లో తెలుసుకోండి.",
        heading_ledger: "ఎర్ర బాహీఖాతా లెడ్జర్ & రిపోర్ట్స్",
        sub_ledger: "ప్రతి పైసా పారదర్శక రికార్డు",
        heading_family_events: "మీ శుభకార్యాలు",
        sub_select_or_create: "ఈవెంట్ ఎంచుకోండి లేదా కొత్తది జోడించండి",
        btn_add_event: "కొత్త శుభకార్యం",
        btn_all_events: "ఈవెంట్లు",
        heading_vault_security: "ఖజానా భద్రత & రీసైకిల్ బిన్",
        sub_recycle_security: "ఏ రికార్డూ మిస్ అవ్వదు",
        label_recycle_bin: "30 రోజుల రీసైకిల్ బిన్",
        recycle_desc: "పొరపాటున తొలగించిన ఏ చదివింపు అయినా 30 రోజుల పాటు ఇక్కడ భద్రంగా ఉంటుంది.",
        btn_soundbox_test: "సౌండ్‌బాక్స్ వాయిస్ టెస్ట్ (₹2,116)",
        modal_new_event_title: "కొత్త శుభకార్యాన్ని జోడించండి",
        modal_label_name: "శుభకార్యం పూర్తి పేరు *",
        modal_label_date: "శుభ ముహూర్తం తేదీ",
        btn_cancel: "రద్దు (Cancel)",
        btn_save_event: "ఈవెంట్ సృష్టించండి"
      },
      en: {
        header_tagline: "The Grand Celebration Ledger & Shagun Treasury",
        nav_features: "Features",
        nav_comparison: "Comparison",
        nav_calculator: "Calculator",
        btn_login_nav: "Sign In",
        btn_get_started: "Get Started",
        tab_dashboard: "Dashboard",
        tab_desk: "Desk Mode",
        tab_reciprocity: "Reciprocity",
        tab_ledger: "Ledger",
        hero_badge: "Trusted by 50,000+ Indian Families",
        hero_h1: "No More Lost Envelopes.<br><span class='text-amber-800'>The Grand Wedding Ledger Reimagined.</span>",
        hero_desc: "Record every cash gift, gold coin, and UPI transfer in seconds. 100% offline desk mode with sacred chime feedback, UPI standee, and instant reciprocity matching.",
        hero_cta_demo: "Try Interactive Demo (Guest Mode)",
        hero_cta_login: "Sign In (Google / OTP)",
        stat_weddings: "Celebrations",
        stat_tracked: "Shagun Tracked",
        stat_offline: "Offline Reliable",
        comp_title: "How GiftVault Outperforms Competitor Apps",
        comp_sub: "Solving real user complaints reported on Chadivimpulu, ShagunBook, and messy paper red notebooks:",
        comp_card1_title: "Zero Network Lag & Zero Ads",
        comp_card1_desc: "Wedding venues have congested cellular networks where other apps freeze with annoying video ads. GiftVault works 100% offline in 3 seconds.",
        comp_card2_title: "Given vs Received (Reciprocity)",
        comp_card2_desc: "Never wonder what to gift back. Cross-reference past events instantly to keep harmonious family balances.",
        comp_card3_title: "30-Day Safe Recycle Bin",
        comp_card3_desc: "Accidentally deleted records are never lost. Restore with 1-tap plus encrypted cloud backups in Google Drive.",
        calc_badge: "SHAGUN LOSS PREVENTION CALCULATOR",
        calc_h2: "How Much Shagun Will You Protect?",
        calc_desc: "Traditional red notebooks suffer from 3% to 5% lost gifts due to illegible handwriting, hurried entries, and misplaced envelopes.",
        auth_heading: "Sign In to GiftVault",
        auth_sub: "Securely manage your family's celebration ledgers",
        btn_google_signin: "Continue with Google Account",
        auth_or: "OR",
        label_phone_login: "Mobile Number:",
        btn_get_otp: "Get OTP",
        btn_guest_mode: "Continue as Guest (Instant Demo)",
        metric_received_title: "Total Received (In)",
        metric_received_sub: "All shagun and gifts contributed by guests at this event",
        metric_given_title: "Total Given (Out)",
        metric_given_sub: "Past gifts our family contributed to their functions",
        metric_net_title: "Net Balance Status",
        metric_net_sub: "Favorable family social exchange balance",
        cat_cash_label: "Cash Shagun",
        cat_gold_label: "Gold / Silver",
        cat_upi_label: "UPI / QR Transfers",
        cat_items_label: "Physical Gift Items",
        btn_open_desk_counter: "Open Counter Desk Mode",
        btn_check_recip: "Check Reciprocity (Given vs Received)",
        btn_view_upi_qr: "UPI QR Standee",
        btn_full_ledger_export: "Red Bahikhata Reports & PDF",
        recent_stream_title: "Recent Shagun Entries (Real-time Stream)",
        view_all_link: "View Full Ledger →",
        label_name: "Guest Full Name *",
        label_city: "Native Town / City",
        label_relation: "Relationship Tag",
        label_gift_type: "Gift Category",
        label_amount: "Shagun Amount (₹) *",
        label_quick_shagun: "Quick Shagun Presets",
        btn_save_record: "Save Entry (Enter)",
        heading_reciprocity: "We Gave vs Received (Reciprocity)",
        sub_reciprocity: "Cross-reference what our family gifted at their past events.",
        heading_ledger: "Red Bahikhata Passbook Ledger",
        sub_ledger: "Transparent line-by-line accounting",
        heading_family_events: "Your Auspicious Celebrations",
        sub_select_or_create: "Select an active celebration or create new",
        btn_add_event: "Add New Celebration",
        btn_all_events: "Celebrations",
        heading_vault_security: "Vault Security & 30-Day Recycle Bin",
        sub_recycle_security: "Zero lost entries, 100% audit log",
        label_recycle_bin: "30-Day Safe Recycle Bin",
        recycle_desc: "Any entry deleted accidentally remains safe here for 30 days. One-tap restore.",
        btn_soundbox_test: "Soundbox Voice Announcement (₹2,116)",
        modal_new_event_title: "Create New Celebration",
        modal_label_name: "Celebration Full Name *",
        modal_label_date: "Auspicious Date",
        btn_cancel: "Cancel",
        btn_save_event: "Create Celebration"
      },
      hi: {
        header_tagline: "शाही शगुन डिजिटल बहीखाता एवं उपहार खजाना",
        nav_features: "विशेषताएं",
        nav_comparison: "तुलना",
        nav_calculator: "कैलकुलेटर",
        btn_login_nav: "साइन इन",
        btn_get_started: "शुरू करें",
        tab_dashboard: "डैशबोर्ड",
        tab_desk: "डेस्क मोड",
        tab_reciprocity: "शगुन मिलान",
        tab_ledger: "बहीखाता",
        hero_badge: "50,000+ संतुष्ट परिवारों का विश्वसनीय लेज़र",
        hero_h1: "लाल बहीखाता हुआ पुराना.<br><span class='text-amber-800'>डिजिटल शगुन का नया जमाना।</span>",
        hero_desc: "विवाह और मांगलिक अवसरों पर मिले हर उपहार, नकद और सोने का सेकंडों में हिसाब रखें। बिना इंटरनेट 100% ऑफलाइन कार्य।",
        hero_cta_demo: "डेमो देखें / अतिथि के रूप में शुरू करें",
        hero_cta_login: "साइन इन (Google / OTP)",
        stat_weddings: "मांगलिक उत्सव",
        stat_tracked: "कुल दर्ज शगुन",
        stat_offline: "ऑफलाइन गारंटी",
        comp_title: "अन्य ऐप्स की तुलना में GiftVault क्यों बेहतर है?",
        comp_sub: "ShagunBook और सामान्य डायरियों की हर समस्या का समाधान:",
        comp_card1_title: "शून्य नेटवर्क समस्या व कोई विज्ञापन नहीं",
        comp_card1_desc: "मंडप में नेटवर्क न होने पर भी 3 सेकंड में तुरंत प्रविष्टि। कोई विज्ञापन रुकावट नहीं।",
        comp_card2_title: "दिया गया vs मिला हुआ शगुन",
        comp_card2_desc: "पिछली बार उनके समारोह में हमारे परिवार ने क्या दिया था, तुरंत मिलान करें।",
        comp_card3_title: "30-दिन सुरक्षित रीसायकल बिन",
        comp_card3_desc: "गलती से डिलीट हुआ रिकॉर्ड कभी गायब नहीं होता। एक क्लिक में रीस्टोर करें।",
        calc_badge: "नुकसान निवारक कैलकुलेटर",
        calc_h2: "आपकी शादी में कितना शगुन सुरक्षित रहेगा?",
        calc_desc: "हाथ से लिखे बहीखातों में अक्सर 3% से 5% शगुन लिफाफे खो जाते हैं या गलत लिखे जाते हैं।",
        auth_heading: "GiftVault में आपका स्वागत है",
        auth_sub: "पारिवारिक मांगलिक आयोजनों का सुरक्षित लेज़र",
        btn_google_signin: "Google खाते से साइन इन करें",
        auth_or: "अथवा",
        label_phone_login: "मोबाइल नंबर:",
        btn_get_otp: "OTP प्राप्त करें",
        btn_guest_mode: "गेस्ट मोड (बिना लॉगिन डेमो देखें)",
        metric_received_title: "कुल मिला हुआ शगुन (In)",
        metric_received_sub: "इस उत्सव में अतिथियों से प्राप्त कुल शगुन",
        metric_given_title: "हमने जो दिया (Out)",
        metric_given_sub: "उनके आयोजनों में हमारे परिवार द्वारा दिया गया शगुन",
        metric_net_title: "शुद्ध संतुलन (Net Balance)",
        metric_net_sub: "पारिवारिक शगुन संतुलन",
        cat_cash_label: "नकद शगुन",
        cat_gold_label: "सोना / चांदी",
        cat_upi_label: "यूपीआई / क्यूआर",
        cat_items_label: "उपहार सामग्री",
        btn_open_desk_counter: "काउंटर डेस्क मोड खोलें",
        btn_check_recip: "शगुन मिलान जांचें",
        btn_view_upi_qr: "यूपीआई स्टैंडी",
        btn_full_ledger_export: "पूर्ण लेज़र व पीडीएफ",
        recent_stream_title: "हालिया शगुन प्रविष्टियां",
        view_all_link: "पूरा बहीखाता देखें →",
        label_name: "अतिथि का नाम *",
        label_city: "मूल शहर / गांव",
        label_relation: "संबंध",
        label_gift_type: "उपहार का प्रकार",
        label_amount: "शगुन राशि (₹) *",
        label_quick_shagun: "त्वरित बटन",
        btn_save_record: "दर्ज करें (Enter)",
        heading_reciprocity: "दिया गया vs मिला शगुन",
        sub_reciprocity: "पिछली बार उनके यहां हमने क्या दिया था, जानें।",
        heading_ledger: "लाल बहीखाता लेज़र",
        sub_ledger: "हर पाई का पारदर्शी हिसाब",
        heading_family_events: "आपके मांगलिक कार्यक्रम",
        sub_select_or_create: "कार्यक्रम चुनें या नया जोड़ें",
        btn_add_event: "नया कार्यक्रम",
        btn_all_events: "कार्यक्रम",
        heading_vault_security: "खजाना सुरक्षा एवं रीसायकल बिन",
        sub_recycle_security: "कोई रिकॉर्ड नहीं खोएगा",
        label_recycle_bin: "30-दिन रीसायकल बिन",
        recycle_desc: "हटाया गया रिकॉर्ड 30 दिनों तक सुरक्षित रहता है।",
        btn_soundbox_test: "साउंडबॉक्स वॉयस टेस्ट (₹2,116)",
        modal_new_event_title: "नया मांगलिक कार्यक्रम जोड़ें",
        modal_label_name: "कार्यक्रम का पूरा नाम *",
        modal_label_date: "शुभ मुहूर्त तिथि",
        btn_cancel: "रद्द करें",
        btn_save_event: "कार्यक्रम सहेजें"
      }
    };

    let currentLang = 'te';
    let chimeEnabled = true;
    let currentUser = null;

    // -------------------------------------------------------------
    // DATA STATE
    // -------------------------------------------------------------
    let state = {
      activeEventId: 'ev-1',
      events: [
        {
          id: 'ev-1',
          name: 'ఆనంద్ & శ్రేయ వివాహ మహోత్సవం',
          category: 'wedding',
          hosts: 'ఆనంద్ వర్మ (వరుడు) & శ్రేయారెడ్డి (వధువు)',
          venue: 'శ్రీ కన్వెన్షన్ హాల్, హైదరాబాద్',
          date: '15 నవంబర్ 2026',
          totalCash: 245616,
          totalGiven: 118500,
          entryCount: 42
        },
        {
          id: 'ev-2',
          name: 'కుమారి సాహిత్య లంగా ఓణీల శుభవేడుక (Half Saree)',
          category: 'halfsaree',
          hosts: 'సాహిత్య (అమ్మాయి) • తల్లిదండ్రులు: రఘురామ్ & సుజాత',
          venue: 'విజయవాడ',
          date: '02 డిసెంబర్ 2026',
          totalCash: 84500,
          totalGiven: 45000,
          entryCount: 28
        },
        {
          id: 'ev-3',
          name: 'చిరంజీవి సాత్విక్ ఒడుగు / ఉపనయన మహోత్సవం',
          category: 'odugu',
          hosts: 'సాత్విక్ (వటువు) • తల్లిదండ్రులు: వంశీకృష్ణ & హారిక',
          venue: 'గుంటూరు',
          date: '10 జనవరి 2027',
          totalCash: 45000,
          totalGiven: 22000,
          entryCount: 16
        },
        {
          id: 'ev-4',
          name: 'రామకృష్ణ నిలయం నూతన గృహప్రవేశం',
          category: 'housewarming',
          hosts: 'రామకృష్ణ & లలితమ్మ దంపతులు',
          venue: 'విశాఖపట్నం',
          date: '28 ఫిబ్రవరి 2027',
          totalCash: 112000,
          totalGiven: 65000,
          entryCount: 35
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
          time: '10:15 AM'
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
          time: '10:20 AM'
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
          time: '10:25 AM'
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
          time: '10:28 AM'
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
    // TEMPLE CHIME AUDIO SYNTHESIZER
    // -------------------------------------------------------------
    function playTempleChime() {
      if (!chimeEnabled) return;
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();
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

        const bellIcon = document.getElementById('bell-icon');
        if (bellIcon) {
          bellIcon.classList.remove('ring-active');
          void bellIcon.offsetWidth;
          bellIcon.classList.add('ring-active');
        }
      } catch (e) {
        console.log("Audio muted");
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
    // PERMANENT LANGUAGE SWITCHER
    // -------------------------------------------------------------
    function applyLanguage(lang) {
      if (!I18N[lang]) return;
      currentLang = lang;
      localStorage.setItem('giftvault_preferred_lang', lang);

      const sel = document.getElementById('header-language-select');
      if (sel) sel.value = lang;

      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (I18N[lang][key]) {
          el.innerHTML = I18N[lang][key];
        }
      });

      const headerTag = document.getElementById('header-tagline');
      if (headerTag && I18N[lang].header_tagline) {
        headerTag.innerText = I18N[lang].header_tagline;
      }

      renderAllDynamicSections();
    }

    // -------------------------------------------------------------
    // PAGE ROUTING
    // -------------------------------------------------------------
    function navigateToPage(pageId) {
      document.querySelectorAll('.page-section').forEach(p => p.classList.remove('active-page'));
      const target = document.getElementById(`page-${pageId}`);
      if (target) target.classList.add('active-page');

      const landingLinks = document.getElementById('nav-landing-links');
      const landingCtas = document.getElementById('landing-auth-ctas');
      const appControls = document.getElementById('nav-app-controls');
      const appUser = document.getElementById('app-user-pill');

      if (pageId === 'app') {
        landingLinks.classList.add('hidden');
        landingCtas.classList.add('hidden');
        appControls.classList.remove('hidden');
        appControls.classList.add('flex');
        appUser.classList.remove('hidden');
        appUser.classList.add('flex');
        switchAppTab('dashboard');
        renderAllDynamicSections();
      } else {
        landingLinks.classList.remove('hidden');
        landingCtas.classList.remove('hidden');
        appControls.classList.add('hidden');
        appControls.classList.remove('flex');
        appUser.classList.add('hidden');
        appUser.classList.remove('flex');
      }

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function enterAsGuest() {
      currentUser = { name: (currentLang === 'te' ? "గెస్ట్ విజిటర్ (డెమో)" : currentLang === 'hi' ? "अतिथि यूजर (डेमो)" : "Guest User (Demo)"), isGuest: true };
      document.getElementById('user-display-name').innerText = currentUser.name;
      navigateToPage('app');
      playTempleChime();
    }

    function loginWithGoogle() {
      currentUser = { name: "రఘు వర్మ (Verified)", email: "raghu.varma@gmail.com" };
      document.getElementById('user-display-name').innerText = currentUser.name;
      navigateToPage('app');
      playTempleChime();
    }

    function sendOtpSim() {
      const num = document.getElementById('auth-phone-input').value.trim();
      if (!num) {
        alert(currentLang === 'te' ? 'దయచేసి మొబైల్ నెంబర్ రాయండి!' : 'Please enter mobile number!');
        return;
      }
      alert(`OTP 7391 పంపబడింది (+91 ${num})`);
      loginWithGoogle();
    }

    function logoutToLanding() {
      currentUser = null;
      navigateToPage('landing');
    }

    // -------------------------------------------------------------
    // SUB-TAB NAVIGATION
    // -------------------------------------------------------------
    function switchAppTab(tabName) {
      document.querySelectorAll('.app-screen').forEach(s => s.classList.remove('active-app-screen'));
      const target = document.getElementById(`subtab-${tabName}`);
      if (target) target.classList.add('active-app-screen');

      const tabs = ['dash', 'desk', 'recip', 'ledger'];
      tabs.forEach(t => {
        const btn = document.getElementById(`head-tab-${t}`);
        if (btn) {
          const map = { 'dash': 'dashboard', 'desk': 'desk', 'recip': 'reciprocity', 'ledger': 'ledger' };
          if (map[t] === tabName) {
            btn.className = "px-3 py-1.5 rounded-lg text-xs font-bold bg-stone-900 text-white shadow-xs flex items-center gap-1.5";
          } else {
            btn.className = "px-3 py-1.5 rounded-lg text-xs font-semibold text-stone-700 hover:bg-stone-100 flex items-center gap-1.5";
          }
        }
      });

      if (tabName === 'desk') {
        setTimeout(() => {
          const inp = document.getElementById('desk-input-name');
          if (inp) inp.focus();
        }, 150);
      }
    }

    // -------------------------------------------------------------
    // DYNAMIC EVENT CATEGORY FIELDS (CULTURAL PRECISION)
    // -------------------------------------------------------------
    function onCategoryChanged(cat) {
      const container = document.getElementById('dynamic-participant-fields');
      const nameInput = document.getElementById('modal-input-name');

      if (cat === 'wedding') {
        nameInput.placeholder = "ఉదా: ఆనంద్ వర్మ & శ్రేయారెడ్డి వివాహం";
        container.innerHTML = `
          <div class="text-[11px] font-bold text-amber-900 border-b border-amber-200/60 pb-1">వధూవరుల వివరాలు (Both Bride & Groom):</div>
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block font-bold text-stone-700 mb-1">వరుడి పేరు (Groom Name) *</label>
              <input id="field-groom" type="text" placeholder="వరుడి పేరు" class="w-full h-8 px-2.5 bg-white border border-stone-200 rounded-lg">
            </div>
            <div>
              <label class="block font-bold text-stone-700 mb-1">వధువు పేరు (Bride Name) *</label>
              <input id="field-bride" type="text" placeholder="వధువు పేరు" class="w-full h-8 px-2.5 bg-white border border-stone-200 rounded-lg">
            </div>
          </div>
        `;
      } else if (cat === 'halfsaree' || cat === 'pushpavathi') {
        nameInput.placeholder = (cat === 'halfsaree') ? "ఉదా: కుమారి సాహితీ లంగా ఓణీల వేడుక" : "ఉదా: కుమారి అనన్య పుష్పవతి శుభకార్యం";
        container.innerHTML = `
          <div class="text-[11px] font-bold text-rose-900 border-b border-rose-200/60 pb-1">బాలిక వివరాలు (Female Only):</div>
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block font-bold text-stone-700 mb-1">అమ్మాయి పేరు (Girl Name) *</label>
              <input id="field-girl" type="text" placeholder="అమ్మాయి పేరు" class="w-full h-8 px-2.5 bg-white border border-stone-200 rounded-lg">
            </div>
            <div>
              <label class="block font-bold text-stone-700 mb-1">తల్లిదండ్రుల పేర్లు (Parents)</label>
              <input id="field-parents" type="text" placeholder="ఉదా: వెంకట్రావు & కృష్ణవేణి" class="w-full h-8 px-2.5 bg-white border border-stone-200 rounded-lg">
            </div>
          </div>
        `;
      } else if (cat === 'odugu' || cat === 'panchala') {
        nameInput.placeholder = (cat === 'odugu') ? "ఉదా: చిరంజీవి సాత్విక్ ఒడుగు / ఉపనయనం" : "ఉదా: చిరంజీవి హర్షవర్ధన్ పంచల వేడుక";
        container.innerHTML = `
          <div class="text-[11px] font-bold text-amber-900 border-b border-amber-200/60 pb-1">బాలుడి వివరాలు (Male Only):</div>
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block font-bold text-stone-700 mb-1">అబ్బాయి పేరు (Boy Name / వటువు) *</label>
              <input id="field-boy" type="text" placeholder="అబ్బాయి పేరు" class="w-full h-8 px-2.5 bg-white border border-stone-200 rounded-lg">
            </div>
            <div>
              <label class="block font-bold text-stone-700 mb-1">తల్లిదండ్రుల పేర్లు (Parents)</label>
              <input id="field-parents" type="text" placeholder="ఉదా: రామారావు & శాంతమ్మ" class="w-full h-8 px-2.5 bg-white border border-stone-200 rounded-lg">
            </div>
          </div>
        `;
      } else if (cat === 'naming' || cat === 'mundan' || cat === 'birthday') {
        nameInput.placeholder = (cat === 'naming') ? "ఉదా: నామకరణం & బారసాల మహోత్సవం" : (cat === 'mundan') ? "ఉదా: పుట్టెంటకల వేడుక" : "ఉదా: పుట్టినరోజు సంబరాలు";
        container.innerHTML = `
          <div class="text-[11px] font-bold text-amber-900 border-b border-amber-200/60 pb-1">చిన్నారుల వివరాలు (Child Details):</div>
          <div class="grid grid-cols-3 gap-2">
            <div>
              <label class="block font-bold text-stone-700 mb-1">పాప / బాబు పేరు *</label>
              <input id="field-child" type="text" placeholder="పిల్లల పేరు" class="w-full h-8 px-2 bg-white border border-stone-200 rounded-lg">
            </div>
            <div>
              <label class="block font-bold text-stone-700 mb-1">లింగం (Gender)</label>
              <select id="field-gender" class="w-full h-8 px-1.5 bg-white border border-stone-200 rounded-lg font-semibold">
                <option value="బాబు (Boy)">బాబు (Boy)</option>
                <option value="పాప (Girl)">పాప (Girl)</option>
              </select>
            </div>
            <div>
              <label class="block font-bold text-stone-700 mb-1">తల్లిదండ్రుల పేర్లు</label>
              <input id="field-parents" type="text" placeholder="తల్లి & తండ్రి" class="w-full h-8 px-2 bg-white border border-stone-200 rounded-lg">
            </div>
          </div>
        `;
      } else if (cat === 'housewarming') {
        nameInput.placeholder = "ఉదా: శ్రీ లక్ష్మీ నిలయం గృహప్రవేశం";
        container.innerHTML = `
          <div class="text-[11px] font-bold text-amber-900 border-b border-amber-200/60 pb-1">గృహ యజమానుల వివరాలు (House Owners):</div>
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block font-bold text-stone-700 mb-1">ఇంటి పేరు / గృహ నామం</label>
              <input id="field-house" type="text" placeholder="ఉదా: శ్రీ వేంకటేశ్వర నిలయం" class="w-full h-8 px-2.5 bg-white border border-stone-200 rounded-lg">
            </div>
            <div>
              <label class="block font-bold text-stone-700 mb-1">గృహ యజమానుల పేర్లు *</label>
              <input id="field-owners" type="text" placeholder="ఉదా: రామకృష్ణ & లలిత దంపతులు" class="w-full h-8 px-2.5 bg-white border border-stone-200 rounded-lg">
            </div>
          </div>
        `;
      } else {
        nameInput.placeholder = "ఉదా: ప్రత్యేక కుటుంబ శుభకార్యం";
        container.innerHTML = `
          <div class="text-[11px] font-bold text-amber-900 border-b border-amber-200/60 pb-1">ముఖ్య వ్యక్తుల వివరాలు:</div>
          <div>
            <label class="block font-bold text-stone-700 mb-1">హోస్ట్ / ముఖ్య వ్యక్తుల పేర్లు *</label>
            <input id="field-hosts" type="text" placeholder="వ్యక్తుల పేర్లు" class="w-full h-8 px-2.5 bg-white border border-stone-200 rounded-lg">
          </div>
        `;
      }
    }

    function selectCategorySuggestion(cat, defaultTitle) {
      document.getElementById('modal-select-cat').value = cat;
      document.getElementById('modal-input-name').value = defaultTitle;
      onCategoryChanged(cat);
    }

    // -------------------------------------------------------------
    // INTERACTIVE CITY AUTOCOMPLETE (Suggestions Dropdown)
    // -------------------------------------------------------------
    function onCityInputTyped(query) {
      const dropdown = document.getElementById('city-suggestions-dropdown');
      if (!dropdown) return;

      const q = query.trim().toLowerCase();
      let matches = CITY_DATABASE;
      if (q) {
        matches = CITY_DATABASE.filter(item => 
          item.city.toLowerCase().includes(q) || 
          item.state.toLowerCase().includes(q) || 
          item.pincode.includes(q)
        );
      }

      if (matches.length === 0) {
        dropdown.innerHTML = `<div class="p-2.5 text-center text-xs text-stone-400">సిటీ కనిపించలేదు (మీరే నేరుగా టైప్ చేయవచ్చు)</div>`;
        dropdown.classList.remove('hidden');
        return;
      }

      dropdown.innerHTML = matches.map(item => `
        <div onclick="selectCityItem('${item.city}', '${item.state}', '${item.pincode}')" class="p-2.5 hover:bg-amber-50 cursor-pointer border-b border-stone-100 flex items-center justify-between transition-colors">
          <div>
            <div class="font-bold text-xs text-stone-900">${item.city}</div>
            <div class="text-[10px] text-stone-500">${item.state}</div>
          </div>
          <span class="text-[10px] font-bold text-amber-800 bg-amber-100 px-2 py-0.5 rounded-full">${item.pincode}</span>
        </div>
      `).join('');

      dropdown.classList.remove('hidden');
    }

    function selectCityItem(city, stateName, pincode) {
      document.getElementById('modal-input-city').value = city;
      document.getElementById('modal-input-state').value = stateName;
      document.getElementById('modal-input-pincode').value = pincode;
      document.getElementById('city-suggestions-dropdown').classList.add('hidden');
    }

    // Close suggestions dropdown when clicking outside
    document.addEventListener('click', (e) => {
      const cityInput = document.getElementById('modal-input-city');
      const dropdown = document.getElementById('city-suggestions-dropdown');
      if (dropdown && !dropdown.contains(e.target) && e.target !== cityInput) {
        dropdown.classList.add('hidden');
      }
    });

    // -------------------------------------------------------------
    // SAVE NEW DYNAMIC EVENT
    // -------------------------------------------------------------
    function openModalNewEvent() {
      document.getElementById('modal-new-event').classList.remove('hidden');
      onCategoryChanged(document.getElementById('modal-select-cat').value);
    }

    function closeModalNewEvent() {
      document.getElementById('modal-new-event').classList.add('hidden');
    }

    function saveModalNewEvent() {
      const title = document.getElementById('modal-input-name').value.trim();
      const cat = document.getElementById('modal-select-cat').value;
      const date = document.getElementById('modal-input-date').value;
      const time = document.getElementById('modal-input-time').value.trim() || 'ఉదయం 9:15 ని.లకు';
      const venue = document.getElementById('modal-input-venue').value.trim() || 'కల్యాణ మండపం';
      const city = document.getElementById('modal-input-city').value.trim();

      if (!title) {
        alert(currentLang === 'te' ? 'దయచేసి శుభకార్యం పేరు రాయండి!' : 'Please enter celebration name!');
        return;
      }
      if (!city) {
        alert(currentLang === 'te' ? 'దయచేసి ఊరు / సిటీని ఎంచుకోండి!' : 'Please select native town / city!');
        return;
      }

      // Collect dynamic participant details
      let hosts = 'ముఖ్య వ్యక్తులు';
      if (cat === 'wedding') {
        const groom = document.getElementById('field-groom')?.value.trim() || 'వరుడు';
        const bride = document.getElementById('field-bride')?.value.trim() || 'వధువు';
        hosts = `${groom} & ${bride}`;
      } else if (cat === 'halfsaree' || cat === 'pushpavathi') {
        const girl = document.getElementById('field-girl')?.value.trim() || 'అమ్మాయి';
        const parents = document.getElementById('field-parents')?.value.trim() || '';
        hosts = parents ? `${girl} • తల్లిదండ్రులు: ${parents}` : girl;
      } else if (cat === 'odugu' || cat === 'panchala') {
        const boy = document.getElementById('field-boy')?.value.trim() || 'అబ్బాయి';
        const parents = document.getElementById('field-parents')?.value.trim() || '';
        hosts = parents ? `${boy} • తల్లిదండ్రులు: ${parents}` : boy;
      } else if (cat === 'naming' || cat === 'mundan' || cat === 'birthday') {
        const child = document.getElementById('field-child')?.value.trim() || 'పాప/బాబు';
        const gender = document.getElementById('field-gender')?.value || '';
        const parents = document.getElementById('field-parents')?.value.trim() || '';
        hosts = parents ? `${child} (${gender}) • తల్లిదండ్రులు: ${parents}` : `${child} (${gender})`;
      } else if (cat === 'housewarming') {
        const house = document.getElementById('field-house')?.value.trim() || 'నూతన నిలయం';
        const owners = document.getElementById('field-owners')?.value.trim() || 'గృహయజమానులు';
        hosts = `${house} • ${owners}`;
      } else {
        hosts = document.getElementById('field-hosts')?.value.trim() || 'కుటుంబ సభ్యులు';
      }

      const newEv = {
        id: 'ev-' + Date.now(),
        name: title,
        category: cat,
        hosts: hosts,
        venue: `${venue}, ${city}`,
        date: date,
        time: time,
        totalCash: 0,
        totalGiven: 0,
        entryCount: 0
      };

      state.events.unshift(newEv);
      setActiveEvent(newEv.id);
      closeModalNewEvent();
      playTempleChime();
    }

    function setActiveEvent(id) {
      state.activeEventId = id;
      const ev = state.events.find(e => e.id === id);
      if (ev) {
        document.getElementById('app-event-name').innerText = ev.name;
        document.getElementById('app-event-meta').innerText = `${ev.venue} • ముహూర్తం: ${ev.date}`;
      }
      renderAllDynamicSections();
      switchAppTab('dashboard');
    }

    // -------------------------------------------------------------
    // DESK ENTRY EXECUTION
    // -------------------------------------------------------------
    function setDeskAmount(val) {
      const inp = document.getElementById('desk-input-amount');
      if (inp) {
        inp.value = val;
        inp.focus();
      }
    }

    function simulatePhotoCapture() {
      const btn = document.getElementById('desk-btn-photo');
      const label = document.getElementById('desk-photo-label');
      label.innerText = "✓ స్నాప్!";
      btn.classList.add('bg-emerald-100', 'text-emerald-800', 'border-emerald-300');
      setTimeout(() => {
        label.innerText = "ఫోటో స్నాప్";
        btn.classList.remove('bg-emerald-100', 'text-emerald-800', 'border-emerald-300');
      }, 1500);
    }

    function resetLiveDeskInputs() {
      document.getElementById('desk-input-name').value = '';
      document.getElementById('desk-input-city').value = '';
      document.getElementById('desk-input-notes').value = '';
      document.getElementById('desk-input-amount').value = '1116';
      document.getElementById('desk-input-name').focus();
    }

    function saveLiveDeskEntry() {
      const nameInput = document.getElementById('desk-input-name');
      const name = nameInput.value.trim();
      const city = document.getElementById('desk-input-city').value.trim() || 'స్వగ్రామం';
      const relation = document.getElementById('desk-select-relation').value;
      const giftType = document.getElementById('desk-select-gift-type').value;
      const amount = parseInt(document.getElementById('desk-input-amount').value) || 1116;
      const notes = document.getElementById('desk-input-notes').value.trim() || 'కవరు సమర్పణ';

      if (!name) {
        alert(currentLang === 'te' ? 'దయచేసి అతిథి పేరు రాయండి!' : 'Please enter guest name!');
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
        time: timeStr
      };

      state.entries.unshift(newEntry);
      playTempleChime();

      const card = document.getElementById('desk-continuous-card');
      if (card) {
        card.classList.remove('flash-saved');
        void card.offsetWidth;
        card.classList.add('flash-saved');
      }

      renderAllDynamicSections();
      resetLiveDeskInputs();
    }

    // -------------------------------------------------------------
    // RENDER METRICS & FEEDS
    // -------------------------------------------------------------
    function renderAllDynamicSections() {
      const currentEntries = state.entries.filter(e => e.eventId === state.activeEventId);
      const totalReceived = currentEntries.reduce((acc, curr) => acc + (curr.amount || 0), 0);
      const activeEv = state.events.find(e => e.id === state.activeEventId) || state.events[0];
      const totalGiven = activeEv.totalGiven || 118500;
      const netBalance = totalReceived - totalGiven;

      const recVal = document.getElementById('dash-received-val');
      if (recVal) recVal.innerText = '₹' + totalReceived.toLocaleString('en-IN');
      const givVal = document.getElementById('dash-given-val');
      if (givVal) givVal.innerText = '₹' + totalGiven.toLocaleString('en-IN');
      const netVal = document.getElementById('dash-net-val');
      if (netVal) {
        netVal.innerText = (netBalance >= 0 ? '+' : '') + '₹' + netBalance.toLocaleString('en-IN');
      }

      const deskTot = document.getElementById('desk-screen-total');
      if (deskTot) deskTot.innerText = totalReceived.toLocaleString('en-IN');
      const deskCnt = document.getElementById('desk-screen-count');
      if (deskCnt) deskCnt.innerText = `${currentEntries.length} మంది`;

      const dashStream = document.getElementById('dash-recent-stream');
      if (dashStream) {
        dashStream.innerHTML = currentEntries.slice(0, 4).map(e => `
          <div class="p-3 rounded-xl bg-white border border-stone-200/80 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <span class="w-8 h-8 rounded-lg bg-amber-50 text-amber-900 border border-amber-200/70 flex items-center justify-center font-bold text-xs">
                ${e.giftType.includes('బంగారం') ? 'GLD' : e.giftType.includes('UPI') ? 'UPI' : 'INR'}
              </span>
              <div>
                <span class="font-bold text-xs text-stone-900 block leading-tight">${e.name}</span>
                <span class="text-[10px] text-stone-500">${e.city} • <span class="text-amber-800 font-semibold">${e.relation}</span> • ${e.giftType}</span>
              </div>
            </div>
            <div class="text-right">
              <span class="font-bold text-xs text-stone-900 block">₹${e.amount.toLocaleString('en-IN')}</span>
              <span class="text-[10px] text-stone-400">${e.time}</span>
            </div>
          </div>
        `).join('');
      }

      renderReciprocityList();

      const ledgerCont = document.getElementById('ledger-table-container');
      if (ledgerCont) {
        ledgerCont.innerHTML = currentEntries.map(e => `
          <div class="p-3.5 rounded-xl bg-white border border-stone-200/90 shadow-2xs flex items-center justify-between">
            <div>
              <div class="font-bold text-xs text-stone-900">${e.name}</div>
              <div class="text-[10px] text-stone-500">${e.city} • <span class="text-amber-800 font-medium">${e.relation}</span> • ${e.giftType}</div>
              ${e.notes ? `<div class="text-[10px] text-stone-400 mt-0.5">📝 ${e.notes}</div>` : ''}
            </div>
            <div class="text-right">
              <div class="font-bold text-xs text-stone-900">₹${e.amount.toLocaleString('en-IN')}</div>
              <div class="text-[9px] text-stone-400">${e.time}</div>
              <button onclick="deleteEntry('${e.id}')" class="text-[9px] text-rose-600 hover:underline mt-0.5">తొలగించు (Delete)</button>
            </div>
          </div>
        `).join('');
      }

      const eventsGrid = document.getElementById('app-events-grid');
      if (eventsGrid) {
        eventsGrid.innerHTML = state.events.map(ev => `
          <div onclick="setActiveEvent('${ev.id}')" class="p-4 rounded-2xl bg-white border ${ev.id === state.activeEventId ? 'border-amber-400 ring-2 ring-amber-400/20' : 'border-stone-200'} shadow-2xs cursor-pointer hover:border-amber-400 transition-all space-y-1.5">
            <div class="flex items-center justify-between">
              <h4 class="font-bold text-xs text-stone-900">${ev.name}</h4>
              <span class="text-xs font-bold text-amber-800">₹${(ev.totalCash || 0).toLocaleString('en-IN')}</span>
            </div>
            <p class="text-[10px] text-amber-900 font-semibold">${ev.hosts}</p>
            <p class="text-[10px] text-stone-500">${ev.venue} • ${ev.date}</p>
          </div>
        `).join('');
      }

      const recycleCont = document.getElementById('app-recycle-container');
      const recycleBadge = document.getElementById('app-recycle-count');
      if (recycleCont && recycleBadge) {
        recycleBadge.innerText = `${state.recycleBin.length} రికార్డులు`;
        recycleCont.innerHTML = state.recycleBin.map(r => `
          <div class="p-2.5 rounded-lg bg-stone-50 border border-stone-200 flex items-center justify-between text-xs">
            <div>
              <span class="font-bold text-stone-800">${r.name}</span>
              <span class="text-[10px] text-stone-500 block">₹${r.amount.toLocaleString('en-IN')} • ${r.deletedDate}</span>
            </div>
            <button onclick="restoreRecycleItem('${r.id}')" class="h-6 px-2 rounded-md bg-stone-900 text-white font-bold text-[10px]">
              పునరుద్ధరించు (Restore)
            </button>
          </div>
        `).join('');
      }
    }

    function filterReciprocity(q) {
      renderReciprocityList(q.toLowerCase());
    }

    function renderReciprocityList(filter = '') {
      const container = document.getElementById('reciprocity-cards-grid');
      if (!container) return;

      const filtered = state.reciprocityLedger.filter(r => 
        r.name.toLowerCase().includes(filter) || r.city.toLowerCase().includes(filter)
      );

      container.innerHTML = filtered.map(r => {
        let badge = `<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-emerald-100 text-emerald-800 border border-emerald-300">✅ సరితూగింది (Balanced)</span>`;
        if (r.status === 'they_gave_more') {
          badge = `<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-amber-100 text-amber-900 border border-amber-300">🟢 వారు ఎక్కువ ఇచ్చారు</span>`;
        } else if (r.status === 'we_gave_more') {
          badge = `<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-rose-100 text-rose-800 border border-rose-300">🔴 మనం ఎక్కువ ఇచ్చాం</span>`;
        }

        return `
          <div class="p-4 rounded-xl bg-white border border-stone-200 shadow-2xs space-y-2">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-stone-900">${r.name}</span>
              ${badge}
            </div>
            <p class="text-[11px] text-stone-500">${r.city} • గత రికార్డు: ${r.pastEvent}</p>
            <div class="grid grid-cols-2 gap-2 pt-1 border-t border-stone-100 text-xs">
              <div>
                <span class="text-[10px] text-stone-400 block">గతంలో మనం ఇచ్చింది:</span>
                <span class="font-bold text-stone-700">₹${r.pastWeGave.toLocaleString('en-IN')}</span>
              </div>
              <div class="text-right">
                <span class="text-[10px] text-stone-400 block">నేడు వారు ఇచ్చింది:</span>
                <span class="font-bold text-amber-800">₹${r.todayTheyGave.toLocaleString('en-IN')}</span>
              </div>
            </div>
          </div>
        `;
      }).join('');
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
        renderAllDynamicSections();
      }
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
          time: 'ఇప్పుడే'
        });
        playTempleChime();
        renderAllDynamicSections();
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

    function simulateUpiSoundbox() {
      playTempleChime();
      const msg = document.getElementById('qr-soundbox-live');
      msg.innerText = (currentLang === 'te')
        ? "ఫోన్‌పే ద్వారా ₹2,116 రూపాయలు ప్రాప్తించినవి! ధన్యవాదాలు!" 
        : (currentLang === 'hi')
        ? "फोनपे पर ₹2,116 रुपये प्राप्त हुए! धन्यवाद!" 
        : "PhonePe received ₹2,116! Payment Successful!";
    }

    function updateShagunCalculator(val) {
      document.getElementById('calc-guests-val').innerText = `${val} మంది అతిథులు`;
      const saved = Math.round(val * 70.83);
      document.getElementById('calc-saved-val').innerText = '₹' + saved.toLocaleString('en-IN');
    }

    // Initialize on Page Load
    window.addEventListener('DOMContentLoaded', () => {
      const savedLang = localStorage.getItem('giftvault_preferred_lang') || 'te';
      applyLanguage(savedLang);
      renderAllDynamicSections();
    });
  </script>

</body>
</html>
'''

target_path = r"c:\Project\Gift Valut\web_preview\index.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("SUCCESS: Dynamic Cultural Precision Edition written to", target_path)
