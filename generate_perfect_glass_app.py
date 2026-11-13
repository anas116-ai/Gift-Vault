# -*- coding: utf-8 -*-
import os

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault | The Royal Celebration Ledger & Shagun Treasury</title>
  
  <!-- High CTR SEO & Social Metadata -->
  <meta name="description" content="India's #1 digital celebration ledger & wedding shagun manager. Offline desk mode, UPI QR standee, and Given vs Received reciprocity ledger.">
  <meta name="keywords" content="GiftVault, wedding gift tracker, chadivimpulu ledger, shagun manager, telugu marriage gifts, bahikhata app, wedding shagun upi, indian wedding gifts">
  <meta name="author" content="GiftVault Technologies">

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "GiftVault",
    "operatingSystem": "Android, iOS, Windows, Web",
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

  <!-- Tailwind CSS CDN -->
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>

  <!-- Google Fonts: Luxury Serif & Authentic Indic Typography -->
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Ramabhadra&family=Anek+Telugu:wght@400;500;600;700;800&family=Noto+Serif+Devanagari:wght@500;600;700&family=Rozha+One&display=swap');

    /* Coolors.co Luxury Heritage Palette Tokens */
    :root {
      --canvas: #FAF9F6;
      --canvas-mesh-1: rgba(197, 160, 89, 0.05);
      --canvas-mesh-2: rgba(142, 30, 36, 0.04);
      --obsidian: #0F1117;
      --midnight-blue: #161B26;
      --gold-primary: #C5A059;
      --gold-light: #DFB76C;
      --gold-deep: #8C6D2D;
      --gold-border: rgba(197, 160, 89, 0.28);
      --red-crimson: #8E1E24;
      --emerald-green: #1B6E4A;
      --glass-surface: rgba(255, 255, 255, 0.78);
      --glass-border: rgba(255, 255, 255, 0.65);
      --glass-dark: rgba(15, 17, 23, 0.82);
      --glass-dark-border: rgba(197, 160, 89, 0.25);
      --shadow-glass: 0 10px 30px 0 rgba(0, 0, 0, 0.05), 0 1px 3px 0 rgba(0, 0, 0, 0.02);
      --shadow-float: 0 20px 40px -10px rgba(15, 17, 23, 0.12), 0 1px 3px 0 rgba(0, 0, 0, 0.04);
    }

    body {
      background-color: var(--canvas);
      color: #1A1D24;
      font-family: 'Plus Jakarta Sans', 'Anek Telugu', 'Noto Serif Devanagari', sans-serif;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
      background-image: 
        radial-gradient(circle at 15% 10%, var(--canvas-mesh-1) 0%, transparent 45%),
        radial-gradient(circle at 85% 90%, var(--canvas-mesh-2) 0%, transparent 45%);
    }

    .font-cinzel { font-family: 'Cinzel', serif; }
    .font-telugu { font-family: 'Ramabhadra', 'Anek Telugu', sans-serif; }
    .font-hindi { font-family: 'Rozha One', 'Noto Serif Devanagari', serif; }

    /* Authentic Glassmorphic Layering */
    .glass-card {
      background: var(--glass-surface);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--glass-border);
      box-shadow: var(--shadow-glass);
    }

    .glass-dark-card {
      background: var(--glass-dark);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid var(--glass-dark-border);
      box-shadow: var(--shadow-float);
    }

    .gold-foil-badge {
      background: linear-gradient(135deg, #FBF4E4 0%, #F5E5C4 50%, #EBD09C 100%);
      border: 1px solid rgba(197, 160, 89, 0.45);
      color: #7D5C1A;
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

    /* Page Views Switcher */
    .page-section {
      display: none;
      opacity: 0;
      transition: opacity 220ms ease-out;
    }
    .page-section.active-page {
      display: block;
      opacity: 1;
    }

    /* Sub-tabs inside Workspace */
    .app-screen {
      display: none;
      opacity: 0;
      transition: opacity 180ms ease-out;
    }
    .app-screen.active-app-screen {
      display: block;
      opacity: 1;
    }

    /* Golden flash feedback for Desk entry */
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
  <!-- 0. MANDATORY FIRST-TIME LANGUAGE SELECTION OVERLAY / MODAL -->
  <!-- Appears prominently when user has not yet chosen their language -->
  <!-- ============================================================== -->
  <div id="first-language-modal" class="fixed inset-0 z-[100] bg-stone-950/70 backdrop-blur-md flex items-center justify-center p-4">
    <div class="glass-dark-card rounded-3xl max-w-lg w-full p-7 border border-amber-500/30 text-white space-y-6 text-center shadow-2xl relative">
      
      <!-- Crown / Sacred Emblem Vector SVG (No emoji) -->
      <div class="w-14 h-14 mx-auto rounded-2xl bg-gradient-to-br from-amber-600 to-amber-900 p-0.5 shadow-lg flex items-center justify-center">
        <div class="w-full h-full bg-[#0F1117] rounded-[14px] flex items-center justify-center">
          <svg class="w-7 h-7 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
            <path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/>
            <path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/>
            <circle cx="12" cy="15" r="2.5" fill="#C5A059" fill-opacity="0.3" stroke="#D4AF37"/>
          </svg>
        </div>
      </div>

      <div class="space-y-1.5">
        <span class="text-[10px] font-extrabold uppercase tracking-widest text-amber-400 px-3 py-1 rounded-full bg-amber-400/10 border border-amber-400/30">
          SELECT YOUR PREFERRED LANGUAGE • భాషను ఎంచుకోండి
        </span>
        <h2 class="font-cinzel text-xl sm:text-2xl font-bold tracking-wide text-white pt-1">
          Welcome to GIFTVAULT
        </h2>
        <p class="text-xs text-stone-300 max-w-sm mx-auto">
          Please select your language to customize your ledger, reports, and wedding shagun entries.
        </p>
      </div>

      <!-- 3 Language Selection Cards (No Emojis, Pure SVG Flags/Indic Seals) -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-left">
        
        <!-- Telugu Card -->
        <button onclick="selectPrimaryLanguage('te')" class="p-4 rounded-2xl bg-white/5 hover:bg-white/10 border border-amber-400/30 hover:border-amber-400 transition-all group flex flex-col justify-between h-28">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-amber-400 font-cinzel">TE</span>
            <span class="w-2.5 h-2.5 rounded-full bg-amber-400 group-hover:scale-125 transition-transform"></span>
          </div>
          <div>
            <div class="font-telugu text-lg font-bold text-white">తెలుగు</div>
            <div class="text-[10px] text-stone-400 font-telugu">ఆంధ్ర & తెలంగాణ</div>
          </div>
        </button>

        <!-- English Card -->
        <button onclick="selectPrimaryLanguage('en')" class="p-4 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/20 hover:border-amber-400 transition-all group flex flex-col justify-between h-28">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-stone-300 font-cinzel">EN</span>
            <span class="w-2.5 h-2.5 rounded-full bg-stone-500 group-hover:scale-125 transition-transform"></span>
          </div>
          <div>
            <div class="text-base font-bold text-white">English</div>
            <div class="text-[10px] text-stone-400">Standard / Pan-India</div>
          </div>
        </button>

        <!-- Hindi Card -->
        <button onclick="selectPrimaryLanguage('hi')" class="p-4 rounded-2xl bg-white/5 hover:bg-white/10 border border-white/20 hover:border-amber-400 transition-all group flex flex-col justify-between h-28">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-stone-300 font-cinzel">HI</span>
            <span class="w-2.5 h-2.5 rounded-full bg-stone-500 group-hover:scale-125 transition-transform"></span>
          </div>
          <div>
            <div class="font-hindi text-base font-bold text-white">हिन्दी</div>
            <div class="text-[10px] text-stone-400 font-hindi">उत्तर भारत एवं देश भर</div>
          </div>
        </button>

      </div>

      <p class="text-[11px] text-stone-400">
        You can easily change the language anytime from the top navigation bar.
      </p>

    </div>
  </div>

  <!-- ============================================================== -->
  <!-- 1. TOP GLOBAL NAVIGATION HEADER (GLASSMORPHIC & SLEEK) -->
  <!-- ============================================================== -->
  <header class="sticky top-0 z-50 glass-card border-b border-stone-200/80 px-4 lg:px-8 py-3">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
      
      <!-- Brand Logo & Identity -->
      <div onclick="navigateToPage('landing')" class="flex items-center gap-3 cursor-pointer select-none">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-amber-700 via-amber-600 to-amber-900 p-0.5 shadow-md flex items-center justify-center">
          <div class="w-full h-full bg-[#0F1117] rounded-[10px] flex items-center justify-center">
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
            <span class="text-[9px] uppercase font-bold tracking-widest px-2 py-0.5 rounded-full gold-foil-badge hidden sm:inline-block">24K Royal Pro</span>
          </div>
          <p class="text-[11px] text-stone-500 font-medium tracking-tight" id="header-tagline">
            The Royal Celebration Ledger & Shagun Treasury
          </p>
        </div>
      </div>

      <!-- Navigation Links (Landing Mode) -->
      <nav id="nav-landing-links" class="hidden md:flex items-center gap-6 text-xs font-semibold text-stone-600">
        <a href="#features" class="hover:text-amber-800 transition-colors" data-i18n="nav_features">Features</a>
        <a href="#comparison" class="hover:text-amber-800 transition-colors" data-i18n="nav_comparison">Comparison</a>
        <a href="#calculator" class="hover:text-amber-800 transition-colors" data-i18n="nav_calculator">Calculator</a>
      </nav>

      <!-- App Header Navigation (Workspace Mode) -->
      <div id="nav-app-controls" class="hidden items-center gap-1.5">
        <button onclick="switchAppTab('dashboard')" id="head-tab-dash" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-stone-900 text-white shadow-xs flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
          <span data-i18n="tab_dashboard">Dashboard</span>
        </button>
        <button onclick="switchAppTab('desk')" id="head-tab-desk" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-stone-700 hover:bg-stone-100 flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          <span data-i18n="tab_desk">Desk Mode</span>
        </button>
        <button onclick="switchAppTab('reciprocity')" id="head-tab-recip" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-stone-700 hover:bg-stone-100 hidden sm:flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"></path></svg>
          <span data-i18n="tab_reciprocity">Reciprocity</span>
        </button>
        <button onclick="switchAppTab('ledger')" id="head-tab-ledger" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-stone-700 hover:bg-stone-100 hidden sm:flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path><path d="M6 6h10"></path><path d="M6 10h10"></path></svg>
          <span data-i18n="tab_ledger">Ledger</span>
        </button>
      </div>

      <!-- Right Controls: Audio Bell & Prominent Language Switcher Button -->
      <div class="flex items-center gap-2">
        
        <!-- Temple Bell Chime -->
        <button id="btn-chime-toggle" onclick="toggleChimeAudio()" title="Sacred Temple Chime" class="w-8.5 h-8.5 rounded-lg border border-stone-200 bg-white hover:bg-amber-50 text-amber-700 flex items-center justify-center transition-all">
          <svg id="bell-icon" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
          </svg>
        </button>

        <!-- Prominent Language Selector Trigger (Always Visible) -->
        <button onclick="openLanguageModal()" class="h-8.5 px-3 rounded-lg border border-amber-400/50 bg-amber-50/80 hover:bg-amber-100 text-amber-900 font-bold text-xs flex items-center gap-1.5 shadow-2xs">
          <svg class="w-3.5 h-3.5 text-amber-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
          <span id="current-lang-label">తెలుగు / EN / हिन्दी</span>
        </button>

        <!-- Auth Buttons (Landing Mode) -->
        <div id="landing-auth-ctas" class="flex items-center gap-2">
          <button onclick="navigateToPage('auth')" class="h-8.5 px-3 rounded-lg border border-stone-200 text-stone-700 hover:bg-stone-100 text-xs font-semibold">
            <span data-i18n="btn_login_nav">Sign In</span>
          </button>
          <button onclick="enterAsGuest()" class="h-8.5 px-3.5 rounded-lg gold-btn text-xs font-bold shadow-xs">
            <span data-i18n="btn_get_started">Get Started</span>
          </button>
        </div>

        <!-- User Profile Pill (App Mode) -->
        <div id="app-user-pill" class="hidden items-center gap-2">
          <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-stone-100 border border-stone-200 text-xs font-semibold">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            <span id="user-display-name">Guest Account</span>
          </div>
          <button onclick="logoutToLanding()" title="Sign Out" class="h-8.5 px-2 text-stone-400 hover:text-rose-600 text-xs font-bold">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
          </button>
        </div>

      </div>

    </div>
  </header>

  <!-- ============================================================== -->
  <!-- 2. PAGE 1: LUXURY BRAND LANDING PAGE (GLASSMORPHIC) -->
  <!-- ============================================================== -->
  <main id="page-landing" class="page-section active-page flex-1">
    
    <!-- Hero Section -->
    <section class="max-w-7xl mx-auto px-4 lg:px-8 py-12 lg:py-20">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        
        <!-- Hero Text -->
        <div class="lg:col-span-7 space-y-6 text-center lg:text-left">
          
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full gold-foil-badge text-xs font-bold">
            <svg class="w-3.5 h-3.5 text-amber-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"></circle><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"></path></svg>
            <span data-i18n="hero_badge">Trusted by 50,000+ Indian Families</span>
          </div>

          <h1 class="font-cinzel text-3xl sm:text-5xl lg:text-6xl font-black text-stone-900 tracking-tight leading-[1.15]" data-i18n="hero_h1">
            No More Lost Envelopes.<br>
            <span class="text-amber-800 font-telugu">The Grand Wedding Ledger Reimagined.</span>
          </h1>

          <p class="text-stone-600 text-sm sm:text-base leading-relaxed max-w-2xl font-telugu" data-i18n="hero_desc">
            Record every cash gift, gold coin, and UPI transfer in seconds. 100% offline desk mode with sacred chime feedback, UPI standee, and instant reciprocity matching.
          </p>

          <div class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-3 pt-2">
            <button onclick="enterAsGuest()" class="w-full sm:w-auto h-11 px-6 rounded-xl gold-btn font-bold text-xs flex items-center justify-center gap-2 shadow-md">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              <span data-i18n="hero_cta_demo">Try Interactive Demo (Guest Mode)</span>
            </button>
            <button onclick="navigateToPage('auth')" class="w-full sm:w-auto h-11 px-5 rounded-xl bg-white border border-stone-200 hover:bg-stone-50 text-stone-800 font-semibold text-xs flex items-center justify-center gap-2">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              <span data-i18n="hero_cta_login">Sign In (Google / OTP)</span>
            </button>
          </div>

          <!-- Trust Metrics Strip -->
          <div class="grid grid-cols-3 gap-4 pt-6 border-t border-stone-200/80 max-w-lg mx-auto lg:mx-0">
            <div>
              <div class="text-stone-900 font-black text-lg sm:text-xl font-cinzel">50,000+</div>
              <div class="text-[11px] text-stone-500 font-medium" data-i18n="stat_weddings">Celebrations</div>
            </div>
            <div>
              <div class="text-amber-800 font-black text-lg sm:text-xl font-cinzel">₹100 Cr+</div>
              <div class="text-[11px] text-stone-500 font-medium" data-i18n="stat_tracked">Shagun Tracked</div>
            </div>
            <div>
              <div class="text-emerald-700 font-black text-lg sm:text-xl font-cinzel">100%</div>
              <div class="text-[11px] text-stone-500 font-medium" data-i18n="stat_offline">Offline Reliable</div>
            </div>
          </div>

        </div>

        <!-- Hero Glassmorphic Device Showcase -->
        <div class="lg:col-span-5 flex justify-center">
          <div class="w-full max-w-[340px] rounded-[42px] bg-stone-950 p-2.5 shadow-2xl border-4 border-stone-800">
            <div class="rounded-[34px] bg-[#FAF9F6] overflow-hidden p-4 space-y-3.5">
              
              <div class="flex items-center justify-between text-[10px] font-bold text-stone-500 pb-1 border-b border-stone-100">
                <span>10:30 AM</span>
                <span class="text-amber-800 font-semibold">Anand & Shreya Wedding</span>
                <span>100%</span>
              </div>

              <!-- Mini Received vs Given Balance Preview -->
              <div class="grid grid-cols-2 gap-2 text-left">
                <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200/80">
                  <span class="text-[9px] font-bold text-emerald-800 uppercase block">Received (In)</span>
                  <span class="font-cinzel text-sm font-bold text-emerald-950">₹2,45,616</span>
                </div>
                <div class="p-2.5 rounded-xl bg-amber-50 border border-amber-200/80">
                  <span class="text-[9px] font-bold text-amber-800 uppercase block">Given (Out)</span>
                  <span class="font-cinzel text-sm font-bold text-amber-950">₹1,18,500</span>
                </div>
              </div>

              <!-- Mini Live Entry Card -->
              <div class="p-3 rounded-xl bg-white border border-stone-200/90 shadow-2xs space-y-2 text-left">
                <div class="text-[10px] font-bold text-stone-700 uppercase">Counter #1 Live Entry</div>
                <input readonly value="K. Srinivas Rao (Guntur)" class="w-full h-8 px-2 text-[11px] bg-stone-50 border border-stone-200 rounded-lg text-stone-800">
                <div class="flex items-center gap-1">
                  <span class="h-6 px-2 text-[10px] font-bold rounded-md bg-amber-50 text-amber-900 border border-amber-300">₹1,116</span>
                  <span class="h-6 px-2 text-[10px] font-bold rounded-md bg-stone-100 text-stone-700">₹2,116</span>
                  <span class="h-6 px-2 text-[10px] font-bold rounded-md bg-stone-100 text-stone-700">₹5,116</span>
                </div>
                <button onclick="enterAsGuest()" class="w-full h-8 rounded-lg gold-btn text-[11px] font-bold flex items-center justify-center gap-1">
                  <span>Record & Experience →</span>
                </button>
              </div>

              <div class="text-center text-[10px] text-stone-400">
                100% Offline • Zero Intrusive Ads • Instant WhatsApp Receipt
              </div>

            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- Section 2: Competitor Flaws vs GiftVault Advantage -->
    <section id="comparison" class="max-w-7xl mx-auto px-4 lg:px-8 py-16 border-t border-stone-200/80">
      <div class="text-center max-w-3xl mx-auto mb-12 space-y-3">
        <span class="text-xs font-bold uppercase tracking-widest px-3 py-1 rounded-full gold-foil-badge">
          CRAFTSMANSHIP & SUPERIORITY
        </span>
        <h2 class="font-cinzel text-2xl sm:text-4xl font-extrabold text-stone-900" data-i18n="comp_title">
          How GiftVault Outperforms Competitor Apps
        </h2>
        <p class="text-xs sm:text-sm text-stone-600 font-telugu" data-i18n="comp_sub">
          Solving real user complaints reported on Chadivimpulu, ShagunBook, and messy paper red notebooks:
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <div class="p-6 rounded-3xl glass-card space-y-3">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          </div>
          <h3 class="font-bold text-base text-stone-900" data-i18n="comp_card1_title">Zero Network Lag & Zero Ads</h3>
          <p class="text-xs text-stone-600 leading-relaxed font-telugu" data-i18n="comp_card1_desc">
            Wedding venues have congested cellular networks where other apps freeze with annoying video ads. GiftVault works 100% offline in 3 seconds.
          </p>
        </div>

        <div class="p-6 rounded-3xl glass-card space-y-3">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"></path></svg>
          </div>
          <h3 class="font-bold text-base text-stone-900" data-i18n="comp_card2_title">Given vs Received (Reciprocity)</h3>
          <p class="text-xs text-stone-600 leading-relaxed font-telugu" data-i18n="comp_card2_desc">
            Never wonder what to gift back. Cross-reference past events instantly to keep harmonious family balances.
          </p>
        </div>

        <div class="p-6 rounded-3xl glass-card space-y-3">
          <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"></path></svg>
          </div>
          <h3 class="font-bold text-base text-stone-900" data-i18n="comp_card3_title">30-Day Safe Recycle Bin</h3>
          <p class="text-xs text-stone-600 leading-relaxed font-telugu" data-i18n="comp_card3_desc">
            Accidentally deleted records are never lost. Restore with 1-tap plus encrypted cloud backups in Google Drive.
          </p>
        </div>

      </div>
    </section>

    <!-- Section 3: Shagun ROI Calculator -->
    <section id="calculator" class="max-w-7xl mx-auto px-4 lg:px-8 py-16 border-t border-stone-200/80">
      <div class="p-8 sm:p-12 rounded-3xl glass-dark-card text-white shadow-xl">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
          
          <div class="space-y-4">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-widest" data-i18n="calc_badge">
              SHAGUN LOSS PREVENTION CALCULATOR
            </span>
            <h2 class="font-cinzel text-2xl sm:text-3xl font-bold" data-i18n="calc_h2">
              How Much Shagun Will You Protect?
            </h2>
            <p class="text-xs text-stone-300 leading-relaxed font-telugu" data-i18n="calc_desc">
              Traditional red notebooks suffer from 3% to 5% lost gifts due to illegible handwriting, hurried entries, and misplaced envelopes.
            </p>
            
            <div class="space-y-2 pt-2">
              <label class="block text-xs font-bold text-stone-300">Estimated Wedding Guests Attending:</label>
              <input id="calc-guests-input" type="range" min="100" max="2000" value="600" step="50" oninput="updateShagunCalculator(this.value)" class="w-full accent-amber-400">
              <div class="flex justify-between text-xs font-bold text-amber-300">
                <span>100 Guests</span>
                <span id="calc-guests-val" class="text-white text-sm">600 Guests</span>
                <span>2,000 Guests</span>
              </div>
            </div>
          </div>

          <div class="p-6 rounded-2xl bg-stone-900/90 border border-amber-400/30 text-center space-y-3">
            <span class="text-xs font-bold text-stone-400 uppercase tracking-wider">Amount Safeguarded via GiftVault:</span>
            <div id="calc-saved-val" class="font-cinzel text-3xl sm:text-4xl font-black text-amber-400">
              ₹42,500
            </div>
            <p class="text-[11px] text-stone-400 font-telugu">
              (Eliminates miscalculations, untracked envelopes, and lost records 100%)
            </p>
            <button onclick="enterAsGuest()" class="h-10 px-6 rounded-xl gold-btn text-xs font-bold">
              Safeguard Your Celebration Now →
            </button>
          </div>

        </div>
      </div>
    </section>

  </main>

  <!-- ============================================================== -->
  <!-- 3. PAGE 2: CLEAN & ELEGANT AUTHENTICATION (లాగిన్ పేజ్) -->
  <!-- ============================================================== -->
  <div id="page-auth" class="page-section max-w-md mx-auto px-4 py-16 my-auto flex-1">
    <div class="p-8 rounded-3xl glass-card space-y-6 text-center">
      
      <!-- Brand Seal Vector SVG -->
      <div class="w-14 h-14 mx-auto rounded-2xl bg-[#0F1117] p-0.5 shadow-md flex items-center justify-center">
        <svg class="w-8 h-8 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
          <path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/>
          <path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/>
        </svg>
      </div>

      <div>
        <h2 class="font-cinzel text-xl font-bold text-stone-900" data-i18n="auth_heading">Sign In to GiftVault</h2>
        <p class="text-xs text-stone-500 mt-1 font-telugu" data-i18n="auth_sub">Securely manage your family's celebration ledgers</p>
      </div>

      <!-- One-Tap Google Sign-In -->
      <button onclick="loginWithGoogle()" class="w-full h-11 px-4 rounded-xl bg-white border border-stone-300 hover:bg-stone-50 text-stone-800 font-semibold text-xs flex items-center justify-center gap-3 shadow-xs">
        <svg class="w-4 h-4" viewBox="0 0 24 24">
          <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
          <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
          <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
          <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
        </svg>
        <span data-i18n="btn_google_signin">Continue with Google Account</span>
      </button>

      <div class="flex items-center gap-2 text-[10px] text-stone-400 uppercase tracking-widest">
        <span class="flex-1 h-px bg-stone-200"></span>
        <span data-i18n="auth_or">OR</span>
        <span class="flex-1 h-px bg-stone-200"></span>
      </div>

      <!-- Mobile Number OTP Option -->
      <div class="space-y-2 text-left">
        <label class="block text-[11px] font-bold text-stone-600" data-i18n="label_phone_login">Mobile Number:</label>
        <div class="flex gap-2">
          <input id="auth-phone-input" type="tel" placeholder="+91 98765 43210" class="flex-1 h-9 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500">
          <button onclick="sendOtpSim()" class="h-9 px-3 rounded-lg bg-stone-900 text-white font-bold text-xs" data-i18n="btn_get_otp">Get OTP</button>
        </div>
      </div>

      <!-- Instant Guest Mode -->
      <div class="pt-2">
        <button onclick="enterAsGuest()" class="w-full h-10 rounded-xl bg-amber-50 hover:bg-amber-100 border border-amber-300 text-amber-900 font-bold text-xs flex items-center justify-center gap-2">
          <svg class="w-4 h-4 text-amber-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          <span data-i18n="btn_guest_mode">Continue as Guest (Instant Demo)</span>
        </button>
      </div>

      <p class="text-[10px] text-stone-400 font-telugu">
        100% Secure • We never share your family records or contacts.
      </p>

    </div>
  </div>

  <!-- ============================================================== -->
  <!-- 4. PAGE 3: MAIN APP WORKSPACE (RESPONSIVE ON MOBILE & DESKTOP) -->
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
              Anand & Shreya Wedding
            </h2>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 border border-emerald-300">
              Live Counter Active
            </span>
          </div>
          <p id="app-event-meta" class="text-xs text-stone-500">
            Sri Convention Hall, Hyderabad • Muhurtham: 15 Nov 2026, 9:15 AM
          </p>
        </div>
      </div>

      <div class="flex items-center gap-2 self-stretch sm:self-auto justify-end">
        <button onclick="openModalNewEvent()" class="h-9 px-3.5 text-xs font-semibold rounded-lg bg-stone-900 hover:bg-stone-800 text-white flex items-center gap-1.5 shadow-sm">
          <span>+</span>
          <span data-i18n="btn_add_event">Add New Celebration</span>
        </button>
        <button onclick="switchAppTab('events')" class="h-9 px-3 text-xs font-semibold rounded-lg border border-stone-200 hover:bg-stone-100 text-stone-700 flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg>
          <span data-i18n="btn_all_events">Celebrations</span>
        </button>
      </div>
    </div>

    <!-- SUB-TAB 1: EXECUTIVE DASHBOARD HOME PAGE (హోమ్ పేజ్) -->
    <div id="subtab-dashboard" class="app-screen active-app-screen space-y-6">
      
      <!-- Received, Given, and Net Balance Cards (As explicitly requested by user) -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        
        <!-- Total Received (వచ్చినవి) -->
        <div class="p-5 rounded-2xl glass-card space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-stone-500 uppercase tracking-wider" data-i18n="metric_received_title">Total Received (In)</span>
            <span class="w-8 h-8 rounded-lg bg-emerald-100 text-emerald-800 flex items-center justify-center font-bold text-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>
            </span>
          </div>
          <div class="font-cinzel text-2xl sm:text-3xl font-black text-emerald-800" id="dash-received-val">
            ₹2,45,616
          </div>
          <p class="text-[11px] text-stone-500" data-i18n="metric_received_sub">All shagun and gifts contributed by guests at this event</p>
        </div>

        <!-- Total Given (మనం ఇచ్చినవి) -->
        <div class="p-5 rounded-2xl glass-card space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-stone-500 uppercase tracking-wider" data-i18n="metric_given_title">Total Given (Out)</span>
            <span class="w-8 h-8 rounded-lg bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
            </span>
          </div>
          <div class="font-cinzel text-2xl sm:text-3xl font-black text-amber-900" id="dash-given-val">
            ₹1,18,500
          </div>
          <p class="text-[11px] text-stone-500" data-i18n="metric_given_sub">Past gifts our family contributed to their functions</p>
        </div>

        <!-- Net Balance (సరితూకం / బ్యాలెన్స్) -->
        <div class="p-5 rounded-2xl glass-dark-card text-white space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider" data-i18n="metric_net_title">Net Balance Status</span>
            <span class="w-8 h-8 rounded-lg bg-amber-400/20 text-amber-400 flex items-center justify-center text-sm">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"></path></svg>
            </span>
          </div>
          <div class="font-cinzel text-2xl sm:text-3xl font-black text-white" id="dash-net-val">
            +₹1,27,116
          </div>
          <p class="text-[11px] text-stone-400" data-i18n="metric_net_sub">Favorable family social exchange balance</p>
        </div>

      </div>

      <!-- Category Breakdown Strip (No random emojis) -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
        <div class="p-3.5 rounded-xl glass-card">
          <span class="text-[10px] font-bold text-stone-500 uppercase block" data-i18n="cat_cash_label">Cash Shagun</span>
          <span id="dash-cat-cash" class="font-cinzel text-base font-bold text-stone-900">₹1,92,152</span>
        </div>
        <div class="p-3.5 rounded-xl glass-card">
          <span class="text-[10px] font-bold text-stone-500 uppercase block" data-i18n="cat_gold_label">Gold / Silver</span>
          <span id="dash-cat-gold" class="text-base font-bold text-amber-800">14 Grams</span>
        </div>
        <div class="p-3.5 rounded-xl glass-card">
          <span class="text-[10px] font-bold text-stone-500 uppercase block" data-i18n="cat_upi_label">UPI / QR Transfers</span>
          <span id="dash-cat-upi" class="text-base font-bold text-emerald-800">₹42,348</span>
        </div>
        <div class="p-3.5 rounded-xl glass-card">
          <span class="text-[10px] font-bold text-stone-500 uppercase block" data-i18n="cat_items_label">Physical Gift Items</span>
          <span id="dash-cat-items" class="text-base font-bold text-stone-900">24 Items</span>
        </div>
      </div>

      <!-- Quick Action Buttons Hub -->
      <div class="flex flex-wrap gap-2.5">
        <button onclick="switchAppTab('desk')" class="h-10 px-4 rounded-xl gold-btn text-xs font-bold flex items-center gap-2 shadow-xs">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          <span data-i18n="btn_open_desk_counter">Open Counter Desk Mode</span>
        </button>
        <button onclick="switchAppTab('reciprocity')" class="h-10 px-4 rounded-xl bg-white border border-stone-200 hover:bg-stone-50 text-stone-800 text-xs font-semibold flex items-center gap-1.5 shadow-2xs">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="M7 21h10"></path><path d="M12 3v18"></path><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"></path></svg>
          <span data-i18n="btn_check_recip">Check Reciprocity (Given vs Received)</span>
        </button>
        <button onclick="switchAppTab('qr')" class="h-10 px-4 rounded-xl bg-white border border-stone-200 hover:bg-stone-50 text-stone-800 text-xs font-semibold flex items-center gap-1.5 shadow-2xs">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"></rect><rect width="4" height="4" x="7" y="7"></rect><rect width="4" height="4" x="13" y="7"></rect><rect width="4" height="4" x="7" y="13"></rect><path d="M13 13h4v4h-4z"></path></svg>
          <span data-i18n="btn_view_upi_qr">UPI QR Standee</span>
        </button>
        <button onclick="switchAppTab('ledger')" class="h-10 px-4 rounded-xl bg-white border border-stone-200 hover:bg-stone-50 text-stone-800 text-xs font-semibold flex items-center gap-1.5 shadow-2xs">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path><path d="M6 6h10"></path><path d="M6 10h10"></path></svg>
          <span data-i18n="btn_full_ledger_export">Red Bahikhata Reports & PDF</span>
        </button>
      </div>

      <!-- Live Recent Feed on Dashboard -->
      <div class="p-5 rounded-2xl glass-card space-y-3">
        <div class="flex items-center justify-between border-b border-stone-100 pb-2">
          <span class="text-xs font-bold text-stone-900 uppercase tracking-wider" data-i18n="recent_stream_title">Recent Shagun Entries (Real-time Stream)</span>
          <button onclick="switchAppTab('ledger')" class="text-xs font-semibold text-amber-800 hover:underline" data-i18n="view_all_link">View Full Ledger →</button>
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
          <span class="text-xs text-amber-300 font-bold uppercase tracking-wider">High-Speed Counter Desk • Live Recording</span>
          <div class="font-bold text-lg text-white flex items-baseline gap-1 mt-0.5">
            <span class="text-xs text-amber-400">₹</span>
            <span id="desk-screen-total" class="font-cinzel text-xl">2,45,616</span>
          </div>
        </div>
        <div class="text-right">
          <span class="text-xs text-stone-400">Total Entries</span>
          <div id="desk-screen-count" class="font-bold text-base text-stone-200">18 Guests</div>
        </div>
      </div>

      <!-- Continuous Entry Form -->
      <div id="desk-continuous-card" class="p-6 rounded-2xl glass-card space-y-3.5">
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_name">Guest Full Name *</label>
            <input id="desk-input-name" type="text" placeholder="e.g. K. Srinivas Rao" class="w-full h-10 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white focus:outline-hidden">
          </div>
          <div>
            <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_city">Native Town / City</label>
            <input id="desk-input-city" type="text" placeholder="e.g. Guntur / Tenali" class="w-full h-10 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white focus:outline-hidden">
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_relation">Relationship Tag</label>
            <select id="desk-select-relation" class="w-full h-10 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500">
              <option value="Close Family">Close Family</option>
              <option value="Maternal Uncle">Maternal Uncle</option>
              <option value="In-laws">In-laws</option>
              <option value="Friends">Friends</option>
              <option value="Colleagues">Colleagues</option>
              <option value="Villagers">Villagers</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_gift_type">Gift Category</label>
            <select id="desk-select-gift-type" class="w-full h-10 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 font-semibold text-amber-900">
              <option value="Cash">Cash (నగదు)</option>
              <option value="Gold/Silver">Gold / Silver (బంగారం)</option>
              <option value="Gift Item">Physical Gift (కానుక)</option>
              <option value="UPI / QR">UPI / QR Transfer</option>
            </select>
          </div>
        </div>

        <div>
          <label class="block text-xs font-bold text-stone-700 mb-1" data-i18n="label_amount">Shagun Amount (₹) *</label>
          <div class="relative">
            <span class="absolute left-3 top-2.5 text-xs font-bold text-stone-400">₹</span>
            <input id="desk-input-amount" type="number" value="1116" class="w-full h-10 pl-7 pr-3 text-sm font-bold text-stone-900 bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500 focus:bg-white focus:outline-hidden">
          </div>
        </div>

        <!-- Auspicious Shagun Presets Chips -->
        <div>
          <span class="text-[10px] font-bold text-stone-500 uppercase tracking-wider block mb-1" data-i18n="label_quick_shagun">Quick Shagun Presets</span>
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
            <input id="desk-input-notes" type="text" placeholder="Notes (e.g. 2g gold coin / Envelope #12)" class="w-full h-9 px-3 text-xs bg-stone-50 border border-stone-200 rounded-lg">
          </div>
          <div>
            <button onclick="simulatePhotoCapture()" id="desk-btn-photo" class="w-full h-9 px-2 text-xs font-bold rounded-lg border border-stone-200 hover:bg-stone-50 text-stone-700 flex items-center justify-center gap-1.5">
              <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
              <span id="desk-photo-label">Photo Snap</span>
            </button>
          </div>
        </div>

        <div class="pt-2 flex gap-3">
          <button onclick="saveLiveDeskEntry()" class="flex-1 h-11 rounded-xl gold-btn font-bold text-xs flex items-center justify-center gap-2 shadow-sm">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
            <span data-i18n="btn_save_record">Save Entry (Enter)</span>
          </button>
          <button onclick="resetLiveDeskInputs()" class="h-11 px-4 rounded-xl border border-stone-200 text-stone-600 hover:bg-stone-50 text-xs font-semibold">
            <span>Clear</span>
          </button>
        </div>

      </div>
    </div>

    <!-- SUB-TAB 3: RECIPROCITY ENGINE (సరితూకం) -->
    <div id="subtab-reciprocity" class="app-screen space-y-4">
      <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
        <div>
          <h3 class="font-bold text-stone-900 text-base" data-i18n="heading_reciprocity">We Gave vs Received (Reciprocity)</h3>
          <p class="text-xs text-stone-500 font-telugu" data-i18n="sub_reciprocity">Cross-reference what our family gifted at their past events.</p>
        </div>
        <div class="relative w-full sm:w-64">
          <span class="absolute left-3 top-2.5 text-xs text-stone-400">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          </span>
          <input id="search-recip-input" oninput="filterReciprocity(this.value)" type="text" placeholder="Search relative by name..." class="w-full h-9 pl-8 pr-3 text-xs bg-white border border-stone-200 rounded-lg focus:border-amber-500">
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
          <h3 class="font-bold text-stone-900 text-base" data-i18n="heading_ledger">Red Bahikhata Passbook Ledger</h3>
          <p class="text-xs text-stone-500 font-telugu" data-i18n="sub_ledger">Transparent line-by-line accounting</p>
        </div>
        <div class="flex gap-2">
          <button onclick="exportToCsv()" class="h-8.5 px-3 rounded-lg bg-stone-100 hover:bg-stone-200 text-stone-800 text-xs font-bold flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Excel / CSV</span>
          </button>
          <button onclick="exportToPdf()" class="h-8.5 px-3.5 rounded-lg bg-stone-900 hover:bg-stone-800 text-white text-xs font-bold flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect width="12" height="8" x="6" y="14"></rect></svg>
            <span>PDF Print</span>
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
          <h4 class="font-bold text-sm text-stone-900">Anand Varma & Shreya Reddy</h4>
          <p class="text-xs text-stone-500">UPI ID: anand.shreya@hdfcbank</p>
        </div>

        <button onclick="simulateUpiSoundbox()" class="h-10 px-5 rounded-xl bg-emerald-700 hover:bg-emerald-800 text-white font-bold text-xs inline-flex items-center gap-2 shadow-xs">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
          <span data-i18n="btn_soundbox_test">Soundbox Voice Announcement (₹2,116)</span>
        </button>
        <p id="qr-soundbox-live" class="text-xs text-emerald-800 font-semibold min-h-[16px]"></p>
      </div>
    </div>

    <!-- SUB-TAB 6: EVENTS SELECTOR & CREATOR -->
    <div id="subtab-events" class="app-screen space-y-4">
      <div class="flex items-center justify-between border-b border-stone-200 pb-3">
        <div>
          <h3 class="font-bold text-stone-900 text-base" data-i18n="heading_family_events">Your Auspicious Celebrations</h3>
          <p class="text-xs text-stone-500 font-telugu" data-i18n="sub_select_or_create">Select an active celebration or create new</p>
        </div>
        <button onclick="openModalNewEvent()" class="h-8.5 px-3.5 rounded-lg bg-stone-900 text-white text-xs font-bold flex items-center gap-1.5 shadow-xs">
          <span>+</span>
          <span data-i18n="btn_add_event">Add New Celebration</span>
        </button>
      </div>

      <div id="app-events-grid" class="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
        <!-- Rendered by JS -->
      </div>
    </div>

    <!-- SUB-TAB 7: 30-DAY RECYCLE BIN & SETTINGS -->
    <div id="subtab-settings" class="app-screen space-y-4">
      <div>
        <h3 class="font-bold text-stone-900 text-base" data-i18n="heading_vault_security">Vault Security & 30-Day Recycle Bin</h3>
        <p class="text-xs text-stone-500 font-telugu" data-i18n="sub_recycle_security">Zero lost entries, 100% audit log</p>
      </div>

      <div class="p-5 rounded-2xl glass-card space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold text-stone-900 flex items-center gap-2">
            <svg class="w-4 h-4 text-stone-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
            <span data-i18n="label_recycle_bin">30-Day Safe Recycle Bin</span>
          </span>
          <span id="app-recycle-count" class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-800">2 Records</span>
        </div>
        <p class="text-xs text-stone-500 font-telugu" data-i18n="recycle_desc">
          Any entry deleted accidentally remains safe here for 30 days. One-tap restore.
        </p>
        <div id="app-recycle-container" class="space-y-2 pt-2">
          <!-- Populated by JS -->
        </div>
      </div>
    </div>

  </div>

  <!-- ============================================================== -->
  <!-- 5. MODAL: ADD NEW AUSPICIOUS EVENT -->
  <!-- ============================================================== -->
  <div id="modal-new-event" class="fixed inset-0 bg-stone-950/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="glass-card rounded-3xl max-w-md w-full p-6 space-y-4">
      <div class="flex items-center justify-between border-b border-stone-100 pb-3">
        <h3 class="font-bold text-stone-900 text-base" data-i18n="modal_new_event_title">Create New Celebration</h3>
        <button onclick="closeModalNewEvent()" class="text-stone-400 hover:text-stone-700 font-bold text-lg">✕</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_name">Event Occasion Name *</label>
          <input id="modal-input-name" type="text" placeholder="e.g. Rohit & Pooja Wedding" class="w-full h-9 px-3 bg-stone-50 border border-stone-200 rounded-lg focus:border-amber-500">
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_cat">Category</label>
            <select id="modal-select-cat" class="w-full h-9 px-2 bg-stone-50 border border-stone-200 rounded-lg">
              <option value="Wedding">Wedding (వివాహం)</option>
              <option value="Housewarming">Housewarming (గృహప్రవేశం)</option>
              <option value="Engagement">Engagement (నిశ్చితార్థం)</option>
              <option value="Naming">Naming Ceremony (నామకరణం)</option>
              <option value="Jubilee">60th Jubilee (షష్టిపూర్తి)</option>
              <option value="Other">Other Celebration</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_hosts">Primary Persons / Hosts</label>
            <input id="modal-input-hosts" type="text" placeholder="Groom & Bride Names" class="w-full h-9 px-3 bg-stone-50 border border-stone-200 rounded-lg">
          </div>
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_date">Auspicious Date</label>
            <input id="modal-input-date" type="date" value="2026-12-15" class="w-full h-9 px-2 bg-stone-50 border border-stone-200 rounded-lg">
          </div>
          <div>
            <label class="block font-bold text-stone-700 mb-1" data-i18n="modal_label_venue">Venue & City</label>
            <input id="modal-input-venue" type="text" placeholder="Convention Hall, City" class="w-full h-9 px-3 bg-stone-50 border border-stone-200 rounded-lg">
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end gap-2 pt-2 border-t border-stone-100">
        <button onclick="closeModalNewEvent()" class="h-9 px-4 rounded-lg border border-stone-200 text-stone-600 font-semibold text-xs hover:bg-stone-50" data-i18n="btn_cancel">
          Cancel
        </button>
        <button onclick="saveModalNewEvent()" class="h-9 px-5 rounded-lg gold-btn font-bold text-xs" data-i18n="btn_save_event">
          Create Celebration
        </button>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="max-w-7xl mx-auto px-4 lg:px-8 py-6 border-t border-stone-200/80 text-center text-xs text-stone-500 space-y-1">
    <div class="font-cinzel font-bold text-stone-800 tracking-wider">GIFTVAULT • 24K ROYAL SHAGUN TREASURY</div>
    <p class="font-telugu">100% Offline-First • Designed for Indian Celebration Traditions</p>
  </footer>

  <!-- ============================================================== -->
  <!-- 6. JAVASCRIPT MASTER ENGINE -->
  <!-- ============================================================== -->
  <script>
    // -------------------------------------------------------------
    // MULTILINGUAL DICTIONARY (NO CASUAL EMOJIS IN TEXT)
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
        hero_desc: "వివాహాలు, గృహప్రవేశాలు, మరియు శుభకార్యాలలో వచ్చే ప్రతి రూపాయి, బంగారు కానుకలను క్షణాల్లో నమోదు చేయండి. ఇంటర్నెట్ లేకపోయినా 100% ఆఫ్‌లైన్ డెస్క్ మోడ్, UPI క్యూఆర్ స్టాండీ, మరియు ఎవరికి ఎంత ఇచ్చామో తెలిపే ఆటోమేటిక్ సరితూకం!",
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
        modal_label_name: "శుభకార్యం పేరు *",
        modal_label_cat: "ఈవెంట్ రకం",
        modal_label_hosts: "ముఖ్య వ్యక్తులు",
        modal_label_date: "శుభ ముహూర్తం తేదీ",
        modal_label_venue: "వేదిక / ఊరు",
        btn_cancel: "రద్దు (Cancel)",
        btn_save_event: "ఈవెంట్ సృష్టించండి"
      },
      en: {
        header_tagline: "The Royal Celebration Ledger & Shagun Treasury",
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
        modal_label_name: "Event Occasion Name *",
        modal_label_cat: "Category",
        modal_label_hosts: "Primary Persons / Hosts",
        modal_label_date: "Auspicious Date",
        modal_label_venue: "Venue & City",
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
        modal_label_name: "कार्यक्रम का नाम *",
        modal_label_cat: "श्रेणी",
        modal_label_hosts: "वर-वधू या मेजबान",
        modal_label_date: "शुभ मुहूर्त तिथि",
        modal_label_venue: "स्थान एवं शहर",
        btn_cancel: "रद्द करें",
        btn_save_event: "कार्यक्रम सहेजें"
      }
    };

    let currentLang = 'en'; // Defaults to English initially until user explicitly picks
    let chimeEnabled = true;
    let currentUser = null;

    // -------------------------------------------------------------
    // DATA STATE (EVENTS, ENTRIES, RECIPROCITY, RECYCLE)
    // -------------------------------------------------------------
    let state = {
      activeEventId: 'ev-1',
      events: [
        {
          id: 'ev-1',
          name: 'Anand & Shreya Wedding',
          hosts: 'Anand Varma & Shreya Reddy',
          venue: 'Sri Convention Hall, Hyderabad',
          date: '15 Nov 2026',
          totalCash: 245616,
          totalGiven: 118500,
          entryCount: 42
        },
        {
          id: 'ev-2',
          name: 'Ramakrishna Nilayam Housewarming',
          hosts: 'Ramakrishna & Lalithamma',
          venue: 'Vijayawada',
          date: '02 Dec 2026',
          totalCash: 84500,
          totalGiven: 45000,
          entryCount: 28
        },
        {
          id: 'ev-3',
          name: 'Satwik Naming Ceremony',
          hosts: 'Vamsi & Harika',
          venue: 'Guntur',
          date: '10 Jan 2027',
          totalCash: 45000,
          totalGiven: 22000,
          entryCount: 16
        },
        {
          id: 'ev-4',
          name: 'Krishna & Mounika Engagement',
          hosts: 'Krishna Prasad & Mounika',
          venue: 'Visakhapatnam',
          date: '28 Feb 2027',
          totalCash: 112000,
          totalGiven: 65000,
          entryCount: 35
        }
      ],
      entries: [
        {
          id: 'ent-1',
          eventId: 'ev-1',
          name: 'Kottapalli Srinivas Rao',
          city: 'Guntur',
          relation: 'Maternal Uncle',
          giftType: 'Cash',
          amount: 5116,
          notes: 'Envelope #01',
          time: '10:15 AM'
        },
        {
          id: 'ent-2',
          eventId: 'ev-1',
          name: 'Yalamanchili Rajasekhar',
          city: 'Vijayawada',
          relation: 'In-laws',
          giftType: 'Gold/Silver',
          amount: 11116,
          notes: '4g Gold Chain',
          time: '10:20 AM'
        },
        {
          id: 'ent-3',
          eventId: 'ev-1',
          name: 'Dasari Venkateswarlu',
          city: 'Hyderabad',
          relation: 'Close Family',
          giftType: 'UPI / QR',
          amount: 2116,
          notes: 'PhonePe Ref: 489201',
          time: '10:25 AM'
        },
        {
          id: 'ent-4',
          eventId: 'ev-1',
          name: 'Bolla Ramesh Babu',
          city: 'Tenali',
          relation: 'Friends',
          giftType: 'Cash',
          amount: 1116,
          notes: 'Envelope #14',
          time: '10:28 AM'
        }
      ],
      reciprocityLedger: [
        {
          name: 'Kottapalli Srinivas Rao',
          city: 'Guntur',
          pastWeGave: 5116,
          pastEvent: "2024 Daughter's Marriage",
          todayTheyGave: 5116,
          status: 'balanced'
        },
        {
          name: 'Yalamanchili Rajasekhar',
          city: 'Vijayawada',
          pastWeGave: 11116,
          pastEvent: '2023 Housewarming',
          todayTheyGave: 11116,
          status: 'balanced'
        },
        {
          name: 'Dasari Venkateswarlu',
          city: 'Hyderabad',
          pastWeGave: 1116,
          pastEvent: '2025 Sravana Puja',
          todayTheyGave: 2116,
          status: 'they_gave_more'
        },
        {
          name: 'Meka Suresh Babu',
          city: 'Nellore',
          pastWeGave: 5116,
          pastEvent: '2023 Wedding',
          todayTheyGave: 2116,
          status: 'we_gave_more'
        }
      ],
      recycleBin: [
        {
          id: 'del-1',
          name: 'Garapati Rama Rao',
          city: 'Khammam',
          amount: 2116,
          deletedDate: 'Yesterday 4:30 PM'
        },
        {
          id: 'del-2',
          name: 'Chintalapati Murali',
          city: 'Ongole',
          amount: 1116,
          deletedDate: '3 days ago'
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
    // FIRST-TIME LANGUAGE SELECTION LOGIC
    // -------------------------------------------------------------
    function selectPrimaryLanguage(lang) {
      currentLang = lang;
      localStorage.setItem('giftvault_preferred_lang', lang);
      document.getElementById('first-language-modal').classList.add('hidden');
      applyLanguage(lang);
      playTempleChime();
    }

    function openLanguageModal() {
      document.getElementById('first-language-modal').classList.remove('hidden');
    }

    function applyLanguage(lang) {
      if (!I18N[lang]) return;
      currentLang = lang;

      const langMap = { 'te': 'తెలుగు (Telugu)', 'en': 'English', 'hi': 'हिन्दी (Hindi)' };
      const curLbl = document.getElementById('current-lang-label');
      if (curLbl) curLbl.innerText = langMap[lang] || 'Language';

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
    // PAGE ROUTING (LANDING -> AUTH -> APP)
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
      currentUser = { name: "Raghu Varma (Verified)", email: "raghu.varma@gmail.com" };
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
      alert(`OTP 7391 sent to +91 ${num}`);
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
    // DESK CONTINUOUS ENTRY
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
      label.innerText = "✓ Snapped!";
      btn.classList.add('bg-emerald-100', 'text-emerald-800', 'border-emerald-300');
      setTimeout(() => {
        label.innerText = "Photo Snap";
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
      const city = document.getElementById('desk-input-city').value.trim() || 'Town';
      const relation = document.getElementById('desk-select-relation').value;
      const giftType = document.getElementById('desk-select-gift-type').value;
      const amount = parseInt(document.getElementById('desk-input-amount').value) || 1116;
      const notes = document.getElementById('desk-input-notes').value.trim() || 'Envelope Contribution';

      if (!name) {
        alert(currentLang === 'te' ? 'దయచేసి అతిథి పేరు రాయండి!' : 'Please enter guest full name!');
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
      if (deskCnt) deskCnt.innerText = `${currentEntries.length} Guests`;

      const dashStream = document.getElementById('dash-recent-stream');
      if (dashStream) {
        dashStream.innerHTML = currentEntries.slice(0, 4).map(e => `
          <div class="p-3 rounded-xl bg-white border border-stone-200/80 flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <span class="w-8 h-8 rounded-lg bg-amber-50 text-amber-900 border border-amber-200/70 flex items-center justify-center font-bold text-xs">
                ${e.giftType.includes('Gold') || e.giftType.includes('బంగారం') ? 'GLD' : e.giftType.includes('UPI') ? 'UPI' : 'INR'}
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
              ${e.notes ? `<div class="text-[10px] text-stone-400 mt-0.5">Note: ${e.notes}</div>` : ''}
            </div>
            <div class="text-right">
              <div class="font-bold text-xs text-stone-900">₹${e.amount.toLocaleString('en-IN')}</div>
              <div class="text-[9px] text-stone-400">${e.time}</div>
              <button onclick="deleteEntry('${e.id}')" class="text-[9px] text-rose-600 hover:underline mt-0.5">Delete</button>
            </div>
          </div>
        `).join('');
      }

      const eventsGrid = document.getElementById('app-events-grid');
      if (eventsGrid) {
        eventsGrid.innerHTML = state.events.map(ev => `
          <div onclick="setActiveEvent('${ev.id}')" class="p-4 rounded-2xl bg-white border ${ev.id === state.activeEventId ? 'border-amber-400 ring-2 ring-amber-400/20' : 'border-stone-200'} shadow-2xs cursor-pointer hover:border-amber-400 transition-all space-y-2">
            <div class="flex items-center justify-between">
              <h4 class="font-bold text-xs text-stone-900">${ev.name}</h4>
              <span class="text-xs font-bold text-amber-800">₹${(ev.totalCash || 0).toLocaleString('en-IN')}</span>
            </div>
            <p class="text-[11px] text-stone-500">${ev.venue} • ${ev.date}</p>
          </div>
        `).join('');
      }

      const recycleCont = document.getElementById('app-recycle-container');
      const recycleBadge = document.getElementById('app-recycle-count');
      if (recycleCont && recycleBadge) {
        recycleBadge.innerText = `${state.recycleBin.length} Records`;
        recycleCont.innerHTML = state.recycleBin.map(r => `
          <div class="p-2.5 rounded-lg bg-stone-50 border border-stone-200 flex items-center justify-between text-xs">
            <div>
              <span class="font-bold text-stone-800">${r.name}</span>
              <span class="text-[10px] text-stone-500 block">₹${r.amount.toLocaleString('en-IN')} • ${r.deletedDate}</span>
            </div>
            <button onclick="restoreRecycleItem('${r.id}')" class="h-6 px-2 rounded-md bg-stone-900 text-white font-bold text-[10px]">
              Restore
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
        let badge = `<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-emerald-100 text-emerald-800 border border-emerald-300">Balanced (సరితూగింది)</span>`;
        if (r.status === 'they_gave_more') {
          badge = `<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-amber-100 text-amber-900 border border-amber-300">They Gave More</span>`;
        } else if (r.status === 'we_gave_more') {
          badge = `<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-rose-100 text-rose-800 border border-rose-300">We Gave More</span>`;
        }

        return `
          <div class="p-4 rounded-xl bg-white border border-stone-200 shadow-2xs space-y-2">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-stone-900">${r.name}</span>
              ${badge}
            </div>
            <p class="text-[11px] text-stone-500">${r.city} • Past Record: ${r.pastEvent}</p>
            <div class="grid grid-cols-2 gap-2 pt-1 border-t border-stone-100 text-xs">
              <div>
                <span class="text-[10px] text-stone-400 block">We Previously Gave:</span>
                <span class="font-bold text-stone-700">₹${r.pastWeGave.toLocaleString('en-IN')}</span>
              </div>
              <div class="text-right">
                <span class="text-[10px] text-stone-400 block">Today They Contributed:</span>
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
          deletedDate: 'Just now'
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
          city: item.city || 'Town',
          relation: 'Relatives',
          giftType: 'Cash',
          amount: item.amount,
          notes: 'Restored from Recycle Bin',
          time: 'Just now'
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
      document.getElementById('calc-guests-val').innerText = `${val} Guests`;
      const saved = Math.round(val * 70.83);
      document.getElementById('calc-saved-val').innerText = '₹' + saved.toLocaleString('en-IN');
    }

    function openModalNewEvent() {
      document.getElementById('modal-new-event').classList.remove('hidden');
    }
    function closeModalNewEvent() {
      document.getElementById('modal-new-event').classList.add('hidden');
    }
    function saveModalNewEvent() {
      const title = document.getElementById('modal-input-name').value.trim();
      const cat = document.getElementById('modal-select-cat').value;
      const hosts = document.getElementById('modal-input-hosts').value.trim() || 'Hosts';
      const date = document.getElementById('modal-input-date').value;
      const venue = document.getElementById('modal-input-venue').value.trim() || 'Venue';

      if (!title) {
        alert(currentLang === 'te' ? 'దయచేసి శుభకార్యం పేరు రాయండి!' : 'Please enter celebration name!');
        return;
      }

      const newEv = {
        id: 'ev-' + Date.now(),
        name: title,
        hosts: hosts,
        venue: venue,
        date: date,
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
        document.getElementById('app-event-meta').innerText = `${ev.venue} • Muhurtham: ${ev.date}`;
      }
      renderAllDynamicSections();
      switchAppTab('dashboard');
    }

    // Initialize on Page Load: Check saved language or show selector
    window.addEventListener('DOMContentLoaded', () => {
      const savedLang = localStorage.getItem('giftvault_preferred_lang');
      if (savedLang) {
        document.getElementById('first-language-modal').classList.add('hidden');
        applyLanguage(savedLang);
      } else {
        // Show language selection first!
        document.getElementById('first-language-modal').classList.remove('hidden');
        applyLanguage('en');
      }
      renderAllDynamicSections();
    });
  </script>

</body>
</html>
'''

target_path = r"c:\Project\Gift Valut\web_preview\index.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("SUCCESS: GiftVault Royal Glassmorphism written to", target_path)
