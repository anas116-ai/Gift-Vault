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

    /* REALISTIC ANDROID SMARTPHONE CHASSIS */
    .phone-chassis {
      width: 380px;
      height: 790px;
      border-radius: 50px;
      background: #0B0C0E;
      padding: 10px;
      box-shadow: 
        0 0 0 2px #2A2D36,
        0 25px 65px -12px rgba(0, 0, 0, 0.40),
        0 10px 25px -8px rgba(0, 0, 0, 0.25);
      position: relative;
      flex-shrink: 0;
      margin: 0 auto;
      transition: all 300ms cubic-bezier(0.23, 1, 0.32, 1);
    }

    .phone-screen {
      width: 100%;
      height: 100%;
      border-radius: 40px;
      background: #FAF9F6;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .screen-scroll::-webkit-scrollbar {
      width: 3px;
    }
    .screen-scroll::-webkit-scrollbar-thumb {
      background: rgba(197, 160, 89, 0.35);
      border-radius: 4px;
    }

    /* Page Views Switcher */
    .page-section {
      display: none;
      opacity: 0;
      transition: opacity 200ms ease-out;
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
  <!-- 1. TOP GLOBAL NAVIGATION & PROMINENT DEVICE MODE SWITCHER -->
  <!-- ============================================================== -->
  <header class="sticky top-0 z-50 glass-card border-b border-stone-200/90 px-4 lg:px-8 py-2.5">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
      
      <!-- Left: Brand Logo & Identity -->
      <div onclick="navigateToPage('landing')" class="flex items-center gap-2.5 cursor-pointer select-none">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-amber-700 via-amber-600 to-amber-900 p-0.5 shadow-md flex items-center justify-center">
          <div class="w-full h-full bg-[#0F1117] rounded-[9px] flex items-center justify-center">
            <svg class="w-5 h-5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
              <path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/>
              <path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/>
              <circle cx="12" cy="15" r="2.5" fill="#C5A059" fill-opacity="0.3" stroke="#D4AF37"/>
            </svg>
          </div>
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <span class="font-cinzel text-base font-extrabold tracking-[0.2em] text-stone-900">GIFTVAULT</span>
            <span class="text-[8px] uppercase font-bold tracking-widest px-1.5 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-300">24K Royal Pro</span>
          </div>
          <p class="text-[10px] text-stone-500 font-medium" id="header-tagline">
            రాయల్ శుభకార్య చదివింపుల డిజిటల్ ఖజానా
          </p>
        </div>
      </div>

      <!-- Center: PROMINENT DEVICE MODE SWITCHER (Mobile App vs Desktop Web) -->
      <div class="flex items-center bg-stone-100 p-1 rounded-xl border border-stone-200 text-xs font-bold shadow-2xs">
        <button id="toggle-device-mobile" onclick="setDeviceViewMode('mobile')" class="px-3.5 py-1.5 rounded-lg bg-stone-900 text-white shadow-xs transition-all flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
          <span>📱 మొబైల్ వెర్షన్ (Android Phone)</span>
        </button>
        <button id="toggle-device-desktop" onclick="setDeviceViewMode('desktop')" class="px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="14" x="2" y="3" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
          <span>🖥️ డెస్క్‌టాప్ వెర్షన్ (Full Web)</span>
        </button>
      </div>

      <!-- Right Header Actions: Temple Audio & Permanent Language Dropdown -->
      <div class="flex items-center gap-2">
        
        <!-- Sacred Temple Bell Chime -->
        <button id="btn-chime-toggle" onclick="toggleChimeAudio()" title="శుభ శంఖారావం / Temple Bell" class="w-8.5 h-8.5 rounded-lg border border-stone-200 bg-white hover:bg-amber-50 text-amber-700 flex items-center justify-center transition-all">
          <svg id="bell-icon" class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
            <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
          </svg>
        </button>

        <!-- Permanent Language Dropdown -->
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

        <!-- Auth CTAs -->
        <div id="landing-auth-ctas" class="flex items-center gap-1.5">
          <button onclick="navigateToPage('auth')" class="h-8.5 px-3 rounded-lg border border-stone-200 text-stone-700 hover:bg-stone-100 text-xs font-semibold">
            <span data-i18n="btn_login_nav">లాగిన్</span>
          </button>
          <button onclick="enterAsGuest()" class="h-8.5 px-3 rounded-lg gold-btn text-xs font-bold shadow-xs">
            <span data-i18n="btn_get_started">ప్రారంభించండి</span>
          </button>
        </div>

        <!-- User Profile Pill -->
        <div id="app-user-pill" class="hidden items-center gap-1.5">
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
  <!-- 2. MAIN CONTAINER: ADAPTS TO PHONE CHASSIS OR DESKTOP DECK -->
  <!-- ============================================================== -->
  <main class="py-6 px-3 flex-1 flex flex-col items-center justify-center">
    
    <!-- Outer Wrapper: Controls phone chassis vs desktop expansion -->
    <div id="main-viewport-wrapper" class="phone-chassis">
      
      <!-- Inner Screen / Phone Display -->
      <div id="main-viewport-screen" class="phone-screen">
        
        <!-- Native Android Status Bar (Visible in Mobile Chassis) -->
        <div id="mobile-status-bar" class="h-7 bg-stone-950 text-stone-300 px-5 flex items-center justify-between text-[11px] font-semibold select-none z-30 flex-shrink-0">
          <span id="android-clock">10:30 AM</span>
          <div class="flex items-center gap-1 px-2 py-0.5 rounded-full bg-stone-900 border border-stone-800">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            <span class="text-[9px] text-stone-400 font-bold tracking-wider">VAULT-OS</span>
          </div>
          <div class="flex items-center gap-1.5 text-[10px]">
            <span>5G</span>
            <span>📶</span>
            <span>100%</span>
          </div>
        </div>

        <!-- Scrollable Inner Body -->
        <div class="flex-1 overflow-y-auto screen-scroll p-4 space-y-4">
          
          <!-- ============================================== -->
          <!-- SCREEN A: LANDING HERO & OVERVIEW -->
          <!-- ============================================== -->
          <div id="page-landing" class="page-section active-page space-y-4">
            
            <div class="text-center space-y-3 pt-2">
              <div class="w-14 h-14 mx-auto rounded-2xl bg-[#0F1117] p-0.5 shadow-md flex items-center justify-center">
                <svg class="w-8 h-8 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                  <path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/>
                  <path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/>
                </svg>
              </div>

              <div>
                <span class="text-[9px] font-extrabold uppercase tracking-widest text-amber-800 bg-amber-100 px-2.5 py-0.5 rounded-full border border-amber-300">
                  50,000+ కుటుంబాల విశ్వాసం
                </span>
                <h1 class="font-cinzel text-xl sm:text-2xl font-black text-stone-900 mt-1" data-i18n="hero_h1">
                  ఎర్ర పుస్తకం పోయింది.<br>
                  <span class="text-amber-800 font-telugu text-lg sm:text-xl">చదివింపుల లెక్కల బాధ తీరింది.</span>
                </h1>
                <p class="text-xs text-stone-600 font-telugu mt-1 leading-relaxed px-2" data-i18n="hero_desc">
                  వివాహాలు, గృహప్రవేశాలు, లంగా ఓణీల వేడుకలు, ఒడుగులు మరియు పుట్టినరోజులలో వచ్చే ప్రతి రూపాయి, బంగారు కానుకలను క్షణాల్లో నమోదు చేయండి.
                </p>
              </div>

              <!-- Main Mobile Launch Actions -->
              <div class="space-y-2 pt-1">
                <button onclick="enterAsGuest()" class="w-full h-11 rounded-xl gold-btn font-bold text-xs flex items-center justify-center gap-2 shadow-md">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                  <span data-i18n="hero_cta_demo">డెమో చూడండి / గెస్ట్‌గా ప్రారంభించండి</span>
                </button>
                <button onclick="navigateToPage('auth')" class="w-full h-10 rounded-xl bg-white border border-stone-200 hover:bg-stone-50 text-stone-800 font-semibold text-xs flex items-center justify-center gap-2">
                  <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                  <span data-i18n="hero_cta_login">లాగిన్ (Google / OTP)</span>
                </button>
              </div>

              <!-- Mini Stats Preview -->
              <div class="grid grid-cols-3 gap-2 pt-2 text-left">
                <div class="p-2.5 rounded-xl bg-white border border-stone-200">
                  <div class="text-stone-900 font-bold text-sm font-cinzel">50,000+</div>
                  <div class="text-[9px] text-stone-500 font-medium">వేడుకలు</div>
                </div>
                <div class="p-2.5 rounded-xl bg-white border border-stone-200">
                  <div class="text-amber-800 font-bold text-sm font-cinzel">₹100 Cr+</div>
                  <div class="text-[9px] text-stone-500 font-medium">చదివింపులు</div>
                </div>
                <div class="p-2.5 rounded-xl bg-white border border-stone-200">
                  <div class="text-emerald-700 font-bold text-sm font-cinzel">100%</div>
                  <div class="text-[9px] text-stone-500 font-medium">ఆఫ్‌లైన్ వర్క్</div>
                </div>
              </div>

            </div>

          </div>

          <!-- ============================================== -->
          <!-- SCREEN B: AUTHENTICATION / LOGIN -->
          <!-- ============================================== -->
          <div id="page-auth" class="page-section space-y-4">
            <div class="p-5 rounded-2xl glass-card space-y-4 text-center">
              
              <div class="w-12 h-12 mx-auto rounded-xl bg-[#0F1117] p-0.5 shadow-md flex items-center justify-center">
                <svg class="w-6 h-6 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8">
                  <path d="M12 2C12 2 13 4 13.5 5C14 6 15 7 15 7C15 7 13.5 7.5 12 7.5C10.5 7.5 9 7 9 7C9 7 10 6 10.5 5C11 4 12 2 12 2Z" fill="#D4AF37"/>
                  <path d="M7 10C7 8.5 9.24 8 12 8C14.76 8 17 8.5 17 10C17 11 16 11.5 15.5 12C17.5 13.5 18 16.5 17 19C16 21 14 21.5 12 21.5C10 21.5 8 21 7 19C6 16.5 6.5 13.5 8.5 12C8 11.5 7 11 7 10Z" stroke="#D4AF37" stroke-width="1.6"/>
                </svg>
              </div>

              <div>
                <h2 class="font-cinzel text-lg font-bold text-stone-900" data-i18n="auth_heading">GiftVault లోకి ప్రవేశించండి</h2>
                <p class="text-[11px] text-stone-500 font-telugu" data-i18n="auth_sub">మీ కుటుంబ శుభకార్యాల లెక్కలను సురక్షితంగా నిర్వహించండి</p>
              </div>

              <button onclick="loginWithGoogle()" class="w-full h-10 px-3 rounded-xl bg-white border border-stone-300 hover:bg-stone-50 text-stone-800 font-semibold text-xs flex items-center justify-center gap-2 shadow-xs">
                <svg class="w-4 h-4" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                  <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                  <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                  <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
                </svg>
                <span data-i18n="btn_google_signin">Google ఖాతాతో సైన్ ఇన్ చేయండి</span>
              </button>

              <div class="flex items-center gap-2 text-[9px] text-stone-400 uppercase tracking-widest">
                <span class="flex-1 h-px bg-stone-200"></span>
                <span data-i18n="auth_or">లేదా</span>
                <span class="flex-1 h-px bg-stone-200"></span>
              </div>

              <div class="space-y-1.5 text-left">
                <label class="block text-[10px] font-bold text-stone-600" data-i18n="label_phone_login">మొబైల్ నెంబర్:</label>
                <div class="flex gap-1.5">
                  <input id="auth-phone-input" type="tel" placeholder="+91 98765 43210" class="flex-1 h-9 px-2.5 text-xs bg-stone-50 border border-stone-200 rounded-lg">
                  <button onclick="sendOtpSim()" class="h-9 px-3 rounded-lg bg-stone-900 text-white font-bold text-xs" data-i18n="btn_get_otp">OTP</button>
                </div>
              </div>

              <div class="pt-1">
                <button onclick="enterAsGuest()" class="w-full h-9 rounded-xl bg-amber-50 hover:bg-amber-100 border border-amber-300 text-amber-900 font-bold text-xs flex items-center justify-center gap-1.5">
                  <svg class="w-3.5 h-3.5 text-amber-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                  <span data-i18n="btn_guest_mode">గెస్ట్ మోడ్ (డెమో)</span>
                </button>
              </div>

            </div>
          </div>

          <!-- ============================================== -->
          <!-- SCREEN C: APP WORKSPACE (DASHBOARD, DESK, ETC) -->
          <!-- ============================================== -->
          <div id="page-app" class="page-section space-y-3.5">
            
            <!-- Active Event Mini Card -->
            <div class="p-3 rounded-xl bg-white border border-stone-200 shadow-2xs flex items-center justify-between">
              <div>
                <div class="flex items-center gap-1.5">
                  <h3 id="app-event-name" class="font-bold text-xs text-stone-900 leading-tight">
                    ఆనంద్ & శ్రేయ వివాహ మహోత్సవం
                  </h3>
                  <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                </div>
                <p id="app-event-meta" class="text-[10px] text-stone-500">శ్రీ కన్వెన్షన్, హైదరాబాద్ • 15 నవంబర్ 2026</p>
              </div>
              <button onclick="openModalNewEvent()" class="h-7 px-2.5 rounded-lg bg-stone-900 text-white text-[10px] font-bold flex items-center gap-1 shadow-2xs">
                <span>+</span>
                <span>ఈవెంట్</span>
              </button>
            </div>

            <!-- SUB-TAB 1: DASHBOARD -->
            <div id="subtab-dashboard" class="app-screen active-app-screen space-y-3">
              
              <!-- 3 Summary Metrics: Received, Given, Net -->
              <div class="grid grid-cols-2 gap-2">
                <div class="p-3 rounded-xl bg-emerald-50/80 border border-emerald-200">
                  <span class="text-[9px] font-bold text-emerald-800 uppercase block" data-i18n="metric_received_title">వచ్చినవి (Received)</span>
                  <div class="font-cinzel text-base font-black text-emerald-950" id="dash-received-val">₹2,45,616</div>
                  <span class="text-[9px] text-emerald-700">42 మంది అతిథులు</span>
                </div>
                <div class="p-3 rounded-xl bg-amber-50/80 border border-amber-200">
                  <span class="text-[9px] font-bold text-amber-800 uppercase block" data-i18n="metric_given_title">మనం ఇచ్చినవి (Given)</span>
                  <div class="font-cinzel text-base font-black text-amber-950" id="dash-given-val">₹1,18,500</div>
                  <span class="text-[9px] text-amber-700">గత ఫంక్షన్ల రికార్డు</span>
                </div>
              </div>

              <!-- Net Balance Card -->
              <div class="p-3 rounded-xl bg-stone-900 text-white flex items-center justify-between">
                <div>
                  <span class="text-[9px] font-bold text-amber-400 uppercase tracking-wider" data-i18n="metric_net_title">నికర బ్యాలెన్స్ (Net Balance)</span>
                  <div class="font-cinzel text-lg font-black text-white" id="dash-net-val">+₹1,27,116</div>
                </div>
                <span class="text-xs font-bold px-2 py-0.5 rounded-full bg-emerald-900 text-emerald-300 border border-emerald-700">సర్ప్లస్</span>
              </div>

              <!-- Category Breakdown Mini Grid -->
              <div class="grid grid-cols-2 gap-2 text-[11px]">
                <div class="p-2 rounded-lg bg-white border border-stone-200">
                  <span class="text-[9px] text-stone-500 font-bold block">నగదు (Cash)</span>
                  <span id="dash-cat-cash" class="font-bold text-stone-900">₹1,92,152</span>
                </div>
                <div class="p-2 rounded-lg bg-white border border-stone-200">
                  <span class="text-[9px] text-stone-500 font-bold block">బంగారం/వెండి</span>
                  <span id="dash-cat-gold" class="font-bold text-amber-800">14 గ్రాములు</span>
                </div>
                <div class="p-2 rounded-lg bg-white border border-stone-200">
                  <span class="text-[9px] text-stone-500 font-bold block">UPI / QR బదిలీలు</span>
                  <span id="dash-cat-upi" class="font-bold text-emerald-800">₹42,348</span>
                </div>
                <div class="p-2 rounded-lg bg-white border border-stone-200">
                  <span class="text-[9px] text-stone-500 font-bold block">గిఫ్ట్ వస్తువులు</span>
                  <span id="dash-cat-items" class="font-bold text-stone-900">24 వస్తువులు</span>
                </div>
              </div>

              <!-- Quick Launch Desk CTA -->
              <button onclick="switchAppTab('desk')" class="w-full h-10 rounded-xl gold-btn text-xs font-bold flex items-center justify-center gap-1.5 shadow-xs">
                <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
                <span data-i18n="btn_open_desk_counter">కౌంటర్ డెస్క్ మోడ్ తెరవండి</span>
              </button>

              <!-- Recent Feed -->
              <div class="p-3 rounded-xl bg-white border border-stone-200 space-y-2">
                <div class="flex items-center justify-between border-b border-stone-100 pb-1">
                  <span class="text-[10px] font-bold text-stone-700 uppercase" data-i18n="recent_stream_title">తాజా చదివింపులు</span>
                  <button onclick="switchAppTab('ledger')" class="text-[10px] font-semibold text-amber-800 hover:underline">మొత్తం →</button>
                </div>
                <div id="dash-recent-stream" class="space-y-1.5">
                  <!-- Populated by JS -->
                </div>
              </div>

            </div>

            <!-- SUB-TAB 2: DESK MODE -->
            <div id="subtab-desk" class="app-screen space-y-3">
              <div class="p-3 rounded-xl bg-stone-900 text-white flex items-center justify-between">
                <div>
                  <span class="text-[9px] text-amber-300 font-bold uppercase">హై-స్పీడ్ కౌంటర్ మోడ్</span>
                  <div class="font-cinzel text-base font-bold text-white" id="desk-screen-total">₹2,45,616</div>
                </div>
                <div class="text-right">
                  <span class="text-[9px] text-stone-400">నమోదులు</span>
                  <div class="text-xs font-bold text-stone-200" id="desk-screen-count">18 మంది</div>
                </div>
              </div>

              <div id="desk-continuous-card" class="p-3.5 rounded-xl bg-white border border-stone-200 space-y-2.5">
                <div class="grid grid-cols-2 gap-2">
                  <div>
                    <label class="block text-[10px] font-bold text-stone-600 mb-0.5" data-i18n="label_name">అతిథి పేరు *</label>
                    <input id="desk-input-name" type="text" placeholder="ఉదా: కొత్తపల్లి శ్రీనివాస్" class="w-full h-8 px-2 text-xs bg-stone-50 border border-stone-200 rounded-lg">
                  </div>
                  <div>
                    <label class="block text-[10px] font-bold text-stone-600 mb-0.5" data-i18n="label_city">ఊరు / గ్రామం</label>
                    <input id="desk-input-city" type="text" placeholder="ఉదా: గుంటూరు" class="w-full h-8 px-2 text-xs bg-stone-50 border border-stone-200 rounded-lg">
                  </div>
                </div>

                <div class="grid grid-cols-2 gap-2">
                  <div>
                    <label class="block text-[10px] font-bold text-stone-600 mb-0.5" data-i18n="label_relation">సంబంధం</label>
                    <select id="desk-select-relation" class="w-full h-8 px-1.5 text-xs bg-stone-50 border border-stone-200 rounded-lg">
                      <option value="దగ్గరి బంధువులు">దగ్గరి బంధువులు</option>
                      <option value="మేనమామ తరఫు">మేనమామ తరఫు</option>
                      <option value="వియ్యంకులు">వియ్యంకులు</option>
                      <option value="స్నేహితులు">స్నేహితులు</option>
                      <option value="సహోద్యోగులు">సహోద్యోగులు</option>
                    </select>
                  </div>
                  <div>
                    <label class="block text-[10px] font-bold text-stone-600 mb-0.5" data-i18n="label_gift_type">కానుక రకం</label>
                    <select id="desk-select-gift-type" class="w-full h-8 px-1.5 text-xs bg-stone-50 border border-stone-200 rounded-lg font-semibold text-amber-900">
                      <option value="నగదు">నగదు (Cash)</option>
                      <option value="బంగారం/వెండి">బంగారం/వెండి</option>
                      <option value="గిఫ్ట్ వస్తువు">గిఫ్ట్ వస్తువు</option>
                      <option value="UPI / QR">UPI / QR</option>
                    </select>
                  </div>
                </div>

                <div>
                  <label class="block text-[10px] font-bold text-stone-600 mb-0.5" data-i18n="label_amount">చదివింపు మొత్తం (₹) *</label>
                  <input id="desk-input-amount" type="number" value="1116" class="w-full h-8 px-2.5 text-sm font-bold text-stone-900 bg-stone-50 border border-stone-200 rounded-lg">
                </div>

                <!-- Presets -->
                <div class="flex flex-wrap gap-1">
                  <button onclick="setDeskAmount(516)" class="h-6 px-2 text-[10px] font-bold rounded-md bg-stone-100 border border-stone-200">₹516</button>
                  <button onclick="setDeskAmount(1116)" class="h-6 px-2 text-[10px] font-bold rounded-md bg-amber-50 text-amber-900 border border-amber-300">₹1,116</button>
                  <button onclick="setDeskAmount(2116)" class="h-6 px-2 text-[10px] font-bold rounded-md bg-stone-100 border border-stone-200">₹2,116</button>
                  <button onclick="setDeskAmount(5116)" class="h-6 px-2 text-[10px] font-bold rounded-md bg-stone-100 border border-stone-200">₹5,116</button>
                </div>

                <div class="pt-1 flex gap-2">
                  <button onclick="saveLiveDeskEntry()" class="flex-1 h-9 rounded-lg gold-btn font-bold text-xs flex items-center justify-center gap-1.5 shadow-xs">
                    <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline></svg>
                    <span data-i18n="btn_save_record">నమోదు చేయండి (Enter)</span>
                  </button>
                  <button onclick="resetLiveDeskInputs()" class="h-9 px-3 rounded-lg border border-stone-200 text-stone-600 text-xs">క్లియర్</button>
                </div>

              </div>
            </div>

            <!-- SUB-TAB 3: RECIPROCITY -->
            <div id="subtab-reciprocity" class="app-screen space-y-3">
              <div class="relative">
                <input id="search-recip-input" oninput="filterReciprocity(this.value)" type="text" placeholder="అతిథి పేరుతో వెతకండి..." class="w-full h-8 pl-3 pr-3 text-xs bg-white border border-stone-200 rounded-lg">
              </div>
              <div id="reciprocity-cards-grid" class="space-y-2"></div>
            </div>

            <!-- SUB-TAB 4: LEDGER -->
            <div id="subtab-ledger" class="app-screen space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-stone-800">ఎర్ర బాహీఖాతా లెడ్జర్</span>
                <div class="flex gap-1">
                  <button onclick="exportToCsv()" class="h-6 px-2 rounded-md bg-stone-100 text-stone-700 text-[10px] font-bold">CSV</button>
                  <button onclick="exportToPdf()" class="h-6 px-2 rounded-md bg-stone-900 text-white text-[10px] font-bold">PDF</button>
                </div>
              </div>
              <div id="ledger-table-container" class="space-y-1.5"></div>
            </div>

            <!-- SUB-TAB 5: QR STANDEE -->
            <div id="subtab-qr" class="app-screen space-y-3 text-center">
              <div class="p-4 rounded-2xl bg-white border-2 border-amber-300 space-y-3 max-w-[260px] mx-auto">
                <span class="font-cinzel text-[10px] font-bold text-amber-900">GIFTVAULT SHAGUN QR</span>
                <div class="w-36 h-36 mx-auto p-2 bg-stone-50 border border-stone-200 rounded-xl flex items-center justify-center">
                  <svg viewBox="0 0 100 100" class="w-full h-full text-stone-900" fill="currentColor">
                    <rect x="0" y="0" width="30" height="30" fill="currentColor" rx="3"/>
                    <rect x="5" y="5" width="20" height="20" fill="white" rx="2"/>
                    <rect x="9" y="9" width="12" height="12" fill="#8E1E24" rx="1"/>
                    <rect x="70" y="0" width="30" height="30" fill="currentColor" rx="3"/>
                    <rect x="75" y="5" width="20" height="20" fill="white" rx="2"/>
                    <rect x="79" y="9" width="12" height="12" fill="#8E1E24" rx="1"/>
                    <rect x="0" y="70" width="30" height="30" fill="currentColor" rx="3"/>
                    <rect x="5" y="75" width="20" height="20" fill="white" rx="2"/>
                    <rect x="9" y="79" width="12" height="12" fill="#8E1E24" rx="1"/>
                    <rect x="38" y="38" width="24" height="24" fill="#C5A059" rx="3"/>
                    <text x="50" y="54" font-size="12" text-anchor="middle" fill="white" font-weight="bold">₹</text>
                  </svg>
                </div>
                <div class="text-[11px] font-bold text-stone-900">ఆనంద్ వర్మ & శ్రేయారెడ్డి</div>
                <button onclick="simulateUpiSoundbox()" class="w-full h-8 rounded-lg bg-emerald-700 text-white font-bold text-[10px]">
                  వాయిస్ టెస్ట్ (₹2,116)
                </button>
                <p id="qr-soundbox-live" class="text-[10px] text-emerald-800 font-semibold"></p>
              </div>
            </div>

            <!-- SUB-TAB 6: EVENTS -->
            <div id="subtab-events" class="app-screen space-y-2.5">
              <div id="app-events-grid" class="space-y-2"></div>
            </div>

          </div>

        </div>

        <!-- Native Android 5-Tab Dock Bottom Navigation (Visible in Mobile Chassis) -->
        <div id="mobile-bottom-dock" class="h-13 bg-white border-t border-stone-200 px-2 flex items-center justify-around z-30 flex-shrink-0 shadow-md">
          <button onclick="switchAppTab('dashboard')" class="flex flex-col items-center py-1 text-stone-900">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            <span class="text-[9px] font-bold mt-0.5">హోమ్</span>
          </button>
          <button onclick="switchAppTab('desk')" class="flex flex-col items-center py-1 text-amber-700">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
            <span class="text-[9px] font-bold mt-0.5">డెస్క్</span>
          </button>
          <button onclick="switchAppTab('reciprocity')" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"></path></svg>
            <span class="text-[9px] font-bold mt-0.5">సరితూకం</span>
          </button>
          <button onclick="switchAppTab('qr')" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"></rect><rect width="4" height="4" x="7" y="7"></rect></svg>
            <span class="text-[9px] font-bold mt-0.5">QR పే</span>
          </button>
          <button onclick="switchAppTab('ledger')" class="flex flex-col items-center py-1 text-stone-400 hover:text-stone-900">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path></svg>
            <span class="text-[9px] font-bold mt-0.5">లెడ్జర్</span>
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
  <!-- 3. DYNAMIC EVENT CREATOR MODAL WITH CULTURAL PRECISION & CITY AUTOCOMPLETE -->
  <!-- ============================================================== -->
  <div id="modal-new-event" class="fixed inset-0 bg-stone-950/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4 overflow-y-auto">
    <div class="glass-card rounded-3xl max-w-lg w-full p-5 space-y-3.5 my-8 shadow-2xl">
      
      <div class="flex items-center justify-between border-b border-stone-200 pb-2.5">
        <div>
          <h3 class="font-bold text-stone-900 text-sm" data-i18n="modal_new_event_title">కొత్త శుభకార్యాన్ని జోడించండి</h3>
          <p class="text-[10px] text-stone-500">కేటగిరీ ఎంచుకోగానే వివరాల ఫారమ్ ఆటోమేటిక్ గా సర్దుబాటు అవుతుంది</p>
        </div>
        <button onclick="closeModalNewEvent()" class="text-stone-400 hover:text-stone-700 font-bold text-base">✕</button>
      </div>

      <!-- Quick Occasion Category Suggestions Pills -->
      <div>
        <label class="block text-[10px] font-bold text-stone-700 mb-1">త్వరిత కేటగిరీ సజెషన్స్:</label>
        <div class="flex flex-wrap gap-1">
          <button type="button" onclick="selectCategorySuggestion('wedding', 'వివాహ మహోత్సవం')" class="h-5 px-2 text-[9px] font-bold rounded bg-amber-50 text-amber-900 border border-amber-300">💍 వివాహం</button>
          <button type="button" onclick="selectCategorySuggestion('halfsaree', 'శ్రీమతి లంగా ఓణీల శుభవేడుక')" class="h-5 px-2 text-[9px] font-bold rounded bg-stone-100 text-stone-800 border border-stone-200">👗 లంగా ఓణీలు (Half Saree)</button>
          <button type="button" onclick="selectCategorySuggestion('odugu', 'చిరంజీవి ఒడుగు / ఉపనయన మహోత్సవం')" class="h-5 px-2 text-[9px] font-bold rounded bg-stone-100 text-stone-800 border border-stone-200">🪔 ఒడుగు (Upanayanam)</button>
          <button type="button" onclick="selectCategorySuggestion('panchala', 'పంచల శుభవేడుక (Dhoti Ceremony)')" class="h-5 px-2 text-[9px] font-bold rounded bg-stone-100 text-stone-800 border border-stone-200">👔 పంచల వేడుక</button>
          <button type="button" onclick="selectCategorySuggestion('pushpavathi', 'పుష్పవతి / పుష్పాలంకరణ వేడుక')" class="h-5 px-2 text-[9px] font-bold rounded bg-stone-100 text-stone-800 border border-stone-200">🌸 పుష్పవతి</button>
          <button type="button" onclick="selectCategorySuggestion('naming', 'నామకరణం & బారసాల మహోత్సవం')" class="h-5 px-2 text-[9px] font-bold rounded bg-stone-100 text-stone-800 border border-stone-200">👶 బారసాల</button>
          <button type="button" onclick="selectCategorySuggestion('mundan', 'పుట్టెంటకలు & చెవులు కుట్టించే వేడుక')" class="h-5 px-2 text-[9px] font-bold rounded bg-stone-100 text-stone-800 border border-stone-200">✂️ పుట్టెంటకలు</button>
          <button type="button" onclick="selectCategorySuggestion('housewarming', 'నూతన గృహప్రవేశ మహోత్సవం')" class="h-5 px-2 text-[9px] font-bold rounded bg-stone-100 text-stone-800 border border-stone-200">🏡 గృహప్రవేశం</button>
          <button type="button" onclick="selectCategorySuggestion('birthday', 'పుట్టినరోజు సంబరాలు')" class="h-5 px-2 text-[9px] font-bold rounded bg-stone-100 text-stone-800 border border-stone-200">🎂 పుట్టినరోజు</button>
        </div>
      </div>

      <div class="space-y-2.5 text-xs">
        
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
          <div>
            <label class="block font-bold text-stone-700 mb-0.5">శుభకార్యం రకం (Category) *</label>
            <select id="modal-select-cat" onchange="onCategoryChanged(this.value)" class="w-full h-8 px-2 bg-stone-50 border border-stone-300 rounded-lg font-bold text-amber-900 text-xs">
              <option value="wedding">వివాహం (Wedding - వధూవరులు)</option>
              <option value="halfsaree">లంగా ఓణీల వేడుక (Half Saree - అమ్మాయి మాత్రమే)</option>
              <option value="odugu">ఒడుగు / ఉపనయనం (Odugu - అబ్బాయి మాత్రమే)</option>
              <option value="panchala">పంచల వేడుక (Dhoti Ceremony - అబ్బాయి మాత్రమే)</option>
              <option value="pushpavathi">పుష్పవతి / పుష్పాలంకరణ (Mature Function - అమ్మాయి మాత్రమే)</option>
              <option value="naming">నామకరణం & బారసాల (Cradle & Naming - పాప/బాబు)</option>
              <option value="mundan">పుట్టెంటకలు / కేశఖండన (Mundan - పాప/బాబు)</option>
              <option value="birthday">పుట్టినరోజు (Birthday - బాలుడు/బాలిక)</option>
              <option value="housewarming">గృహప్రవేశం (Housewarming - గృహ యజమానులు)</option>
              <option value="custom">ఇతర ప్రత్యేక శుభకార్యం</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-stone-700 mb-0.5" data-i18n="modal_label_name">శుభకార్యం పూర్తి పేరు *</label>
            <input id="modal-input-name" type="text" placeholder="ఉదా: రోహిత్ & పూజ వివాహం" class="w-full h-8 px-2.5 bg-stone-50 border border-stone-200 rounded-lg font-semibold text-xs">
          </div>
        </div>

        <!-- DYNAMIC PARTICIPANT FIELDS CONTAINER -->
        <div id="dynamic-participant-fields" class="p-2.5 rounded-lg bg-amber-50/50 border border-amber-200/80 space-y-2"></div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block font-bold text-stone-700 mb-0.5" data-i18n="modal_label_date">తేదీ</label>
            <input id="modal-input-date" type="date" value="2026-12-15" class="w-full h-8 px-2 bg-stone-50 border border-stone-200 rounded-lg text-xs">
          </div>
          <div>
            <label class="block font-bold text-stone-700 mb-0.5">సమయం</label>
            <input id="modal-input-time" type="text" placeholder="ఉదయం 9:15 ని.లకు" class="w-full h-8 px-2 bg-stone-50 border border-stone-200 rounded-lg text-xs">
          </div>
        </div>

        <div>
          <label class="block font-bold text-stone-700 mb-0.5">కల్యాణ మండపం / వేదిక పేరు</label>
          <input id="modal-input-venue" type="text" placeholder="ఉదా: శ్రీ కన్వెన్షన్ హాల్ / స్వగృహం" class="w-full h-8 px-2.5 bg-stone-50 border border-stone-200 rounded-lg text-xs">
        </div>

        <!-- City Autocomplete Input -->
        <div class="relative">
          <label class="block font-bold text-stone-700 mb-0.5">ఊరు / సిటీ (టైప్ చేయగానే సజెషన్స్ వస్తాయి) *</label>
          <input id="modal-input-city" type="text" oninput="onCityInputTyped(this.value)" onfocus="onCityInputTyped(this.value)" placeholder="ఉదా: హైదరాబాద్, గుంటూరు, విజయవాడ..." class="w-full h-8 px-2.5 bg-stone-50 border border-stone-300 rounded-lg font-semibold text-xs text-stone-800">
          <div id="city-suggestions-dropdown" class="absolute left-0 right-0 top-full mt-1 bg-white border border-amber-300 rounded-xl shadow-xl max-h-40 overflow-y-auto z-50 hidden"></div>
        </div>

        <!-- State & Pin -->
        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block font-bold text-stone-500 mb-0.5">రాష్ట్రం (State)</label>
            <input id="modal-input-state" type="text" readonly placeholder="ఆటోమేటిక్" class="w-full h-7 px-2 bg-stone-100 border border-stone-200 rounded-lg text-stone-600 text-xs">
          </div>
          <div>
            <label class="block font-bold text-stone-500 mb-0.5">పిన్ కోడ్</label>
            <input id="modal-input-pincode" type="text" readonly placeholder="పిన్ కోడ్" class="w-full h-7 px-2 bg-stone-100 border border-stone-200 rounded-lg text-stone-600 text-xs">
          </div>
        </div>

      </div>

      <div class="flex items-center justify-end gap-2 pt-2 border-t border-stone-200">
        <button onclick="closeModalNewEvent()" class="h-8 px-3 rounded-lg border border-stone-200 text-stone-600 font-semibold text-xs" data-i18n="btn_cancel">
          రద్దు (Cancel)
        </button>
        <button onclick="saveModalNewEvent()" class="h-8 px-4 rounded-lg gold-btn font-bold text-xs" data-i18n="btn_save_event">
          ఈవెంట్ సృష్టించండి
        </button>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="max-w-7xl mx-auto px-4 py-3 text-center text-[11px] text-stone-500">
    <div class="font-cinzel font-bold text-stone-800">GIFTVAULT • 24K ROYAL SHAGUN TREASURY</div>
  </footer>

  <!-- ============================================================== -->
  <!-- 4. JAVASCRIPT MASTER ENGINE -->
  <!-- ============================================================== -->
  <script>
    // -------------------------------------------------------------
    // DEVICE VIEW SWITCHER (MOBILE CHASSIS VS DESKTOP EXPANDED)
    // -------------------------------------------------------------
    let currentDeviceMode = 'mobile'; // Default to mobile phone view so user sees it right away!

    function setDeviceViewMode(mode) {
      currentDeviceMode = mode;
      const wrapper = document.getElementById('main-viewport-wrapper');
      const screen = document.getElementById('main-viewport-screen');
      const statusBar = document.getElementById('mobile-status-bar');
      const bottomDock = document.getElementById('mobile-bottom-dock');
      const gestureBar = document.getElementById('mobile-gesture-bar');
      const btnMob = document.getElementById('toggle-device-mobile');
      const btnDesk = document.getElementById('toggle-device-desktop');

      if (mode === 'mobile') {
        // High-res realistic phone frame
        wrapper.className = "phone-chassis";
        screen.className = "phone-screen";
        statusBar.classList.remove('hidden');
        bottomDock.classList.remove('hidden');
        gestureBar.classList.remove('hidden');
        btnMob.className = "px-3.5 py-1.5 rounded-lg bg-stone-900 text-white shadow-xs transition-all flex items-center gap-1.5";
        btnDesk.className = "px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all flex items-center gap-1.5";
      } else {
        // Full desktop wide layout
        wrapper.className = "w-full max-w-5xl rounded-3xl bg-white border border-stone-200/90 shadow-lg p-0 transition-all";
        screen.className = "w-full rounded-3xl bg-[#FAF9F6] overflow-hidden flex flex-col";
        statusBar.classList.add('hidden');
        bottomDock.classList.add('hidden');
        gestureBar.classList.add('hidden');
        btnDesk.className = "px-3.5 py-1.5 rounded-lg bg-stone-900 text-white shadow-xs transition-all flex items-center gap-1.5";
        btnMob.className = "px-3.5 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition-all flex items-center gap-1.5";
      }
    }

    // -------------------------------------------------------------
    // CITY DATABASE FOR AUTOCOMPLETE
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
      { city: "బెంగళూరు (Bengaluru)", state: "కర్ణాటక", pincode: "560001" },
      { city: "చెన్నై (Chennai)", state: "తమిళనాడు", pincode: "600001" }
    ];

    const I18N = {
      te: {
        header_tagline: "రాయల్ శుభకార్య చదివింపుల డిజిటల్ ఖజానా",
        btn_login_nav: "లాగిన్",
        btn_get_started: "ప్రారంభించండి",
        tab_dashboard: "డ్యాష్‌బోర్డ్",
        tab_desk: "డెస్క్ మోడ్",
        tab_reciprocity: "సరితూకం",
        tab_ledger: "లెడ్జర్",
        hero_h1: "ఎర్ర పుస్తకం పోయింది.<br><span class='text-amber-800 font-telugu text-lg sm:text-xl'>చదివింపుల లెక్కల బాధ తీరింది.</span>",
        hero_desc: "వివాహాలు, గృహప్రవేశాలు, లంగా ఓణీల వేడుకలు, ఒడుగులు మరియు పుట్టినరోజులలో వచ్చే ప్రతి రూపాయి, బంగారు కానుకలను క్షణాల్లో నమోదు చేయండి.",
        hero_cta_demo: "డెమో చూడండి / గెస్ట్‌గా ప్రారంభించండి",
        hero_cta_login: "లాగిన్ (Google / OTP)",
        auth_heading: "GiftVault లోకి ప్రవేశించండి",
        auth_sub: "మీ కుటుంబ శుభకార్యాల లెక్కలను సురక్షితంగా నిర్వహించండి",
        btn_google_signin: "Google ఖాతాతో సైన్ ఇన్ చేయండి",
        auth_or: "లేదా",
        label_phone_login: "మొబైల్ నెంబర్:",
        btn_get_otp: "OTP",
        btn_guest_mode: "గెస్ట్ మోడ్ (డెమో)",
        metric_received_title: "వచ్చినవి (Received)",
        metric_given_title: "మనం ఇచ్చినవి (Given)",
        metric_net_title: "నికర బ్యాలెన్స్ (Net Balance)",
        btn_open_desk_counter: "కౌంటర్ డెస్క్ మోడ్ తెరవండి",
        recent_stream_title: "తాజా చదివింపులు",
        label_name: "అతిథి పేరు *",
        label_city: "ఊరు / గ్రామం",
        label_relation: "సంబంధం",
        label_gift_type: "కానుక రకం",
        label_amount: "చదివింపు మొత్తం (₹) *",
        btn_save_record: "నమోదు చేయండి (Enter)",
        modal_new_event_title: "కొత్త శుభకార్యాన్ని జోడించండి",
        modal_label_name: "శుభకార్యం పూర్తి పేరు *",
        modal_label_date: "తేదీ",
        btn_cancel: "రద్దు",
        btn_save_event: "ఈవెంట్ సృష్టించండి"
      },
      en: {
        header_tagline: "The Grand Celebration Ledger & Shagun Treasury",
        btn_login_nav: "Sign In",
        btn_get_started: "Get Started",
        tab_dashboard: "Dashboard",
        tab_desk: "Desk Mode",
        tab_reciprocity: "Reciprocity",
        tab_ledger: "Ledger",
        hero_h1: "No More Lost Envelopes.<br><span class='text-amber-800 text-lg sm:text-xl'>The Grand Celebration Ledger Reimagined.</span>",
        hero_desc: "Record every cash gift, gold coin, and UPI transfer in seconds with 100% offline reliability.",
        hero_cta_demo: "Try Interactive Demo (Guest Mode)",
        hero_cta_login: "Sign In (Google / OTP)",
        auth_heading: "Sign In to GiftVault",
        auth_sub: "Securely manage your family's celebration ledgers",
        btn_google_signin: "Continue with Google Account",
        auth_or: "OR",
        label_phone_login: "Mobile Number:",
        btn_get_otp: "Get OTP",
        btn_guest_mode: "Continue as Guest (Demo)",
        metric_received_title: "Received (In)",
        metric_given_title: "Given (Out)",
        metric_net_title: "Net Balance Status",
        btn_open_desk_counter: "Open Counter Desk Mode",
        recent_stream_title: "Recent Shagun Entries",
        label_name: "Guest Full Name *",
        label_city: "Native Town / City",
        label_relation: "Relationship Tag",
        label_gift_type: "Gift Category",
        label_amount: "Shagun Amount (₹) *",
        btn_save_record: "Save Entry (Enter)",
        modal_new_event_title: "Create New Celebration",
        modal_label_name: "Celebration Full Name *",
        modal_label_date: "Date",
        btn_cancel: "Cancel",
        btn_save_event: "Create Celebration"
      },
      hi: {
        header_tagline: "शाही शगुन डिजिटल बहीखाता एवं उपहार खजाना",
        btn_login_nav: "साइन इन",
        btn_get_started: "शुरू करें",
        tab_dashboard: "डैशबोर्ड",
        tab_desk: "डेस्क मोड",
        tab_reciprocity: "शगुन मिलान",
        tab_ledger: "बहीखाता",
        hero_h1: "लाल बहीखाता हुआ पुराना.<br><span class='text-amber-800 text-lg sm:text-xl'>डिजिटल शगुन का नया जमाना।</span>",
        hero_desc: "विवाह और मांगलिक अवसरों पर मिले हर उपहार, नकद और सोने का सेकंडों में हिसाब रखें।",
        hero_cta_demo: "डेमो देखें / अतिथि के रूप में शुरू करें",
        hero_cta_login: "साइन इन (Google / OTP)",
        auth_heading: "GiftVault में आपका स्वागत है",
        auth_sub: "पारिवारिक मांगलिक आयोजनों का सुरक्षित लेज़र",
        btn_google_signin: "Google खाते से साइन इन करें",
        auth_or: "अथवा",
        label_phone_login: "मोबाइल नंबर:",
        btn_get_otp: "OTP प्राप्त करें",
        btn_guest_mode: "गेस्ट मोड (डेमो)",
        metric_received_title: "मिला हुआ शगुन (In)",
        metric_given_title: "हमने जो दिया (Out)",
        metric_net_title: "शुद्ध संतुलन",
        btn_open_desk_counter: "काउंटर डेस्क मोड खोलें",
        recent_stream_title: "हालिया शगुन प्रविष्टियां",
        label_name: "अतिथि का नाम *",
        label_city: "मूल शहर / गांव",
        label_relation: "संबंध",
        label_gift_type: "उपहार का प्रकार",
        label_amount: "शगुन राशि (₹) *",
        btn_save_record: "दर्ज करें (Enter)",
        modal_new_event_title: "नया मांगलिक कार्यक्रम जोड़ें",
        modal_label_name: "कार्यक्रम का पूरा नाम *",
        modal_label_date: "तिथि",
        btn_cancel: "रद्द करें",
        btn_save_event: "कार्यक्रम सहेजें"
      }
    };

    let currentLang = 'te';
    let chimeEnabled = true;
    let currentUser = null;

    let state = {
      activeEventId: 'ev-1',
      events: [
        {
          id: 'ev-1',
          name: 'ఆనంద్ & శ్రేయ వివాహ మహోత్సవం',
          category: 'wedding',
          hosts: 'ఆనంద్ వర్మ & శ్రేయారెడ్డి',
          venue: 'శ్రీ కన్వెన్షన్, హైదరాబాద్',
          date: '15 నవంబర్ 2026',
          totalCash: 245616,
          totalGiven: 118500,
          entryCount: 42
        },
        {
          id: 'ev-2',
          name: 'కుమారి సాహిత్య లంగా ఓణీల శుభవేడుక (Half Saree)',
          category: 'halfsaree',
          hosts: 'సాహిత్య (అమ్మాయి) • రఘురామ్ & సుజాత',
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
          hosts: 'సాత్విక్ (వటువు) • వంశీ & హారిక',
          venue: 'గుంటూరు',
          date: '10 జనవరి 2027',
          totalCash: 45000,
          totalGiven: 22000,
          entryCount: 16
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
          notes: '4g గోల్డ్ కాయిన్',
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
          notes: 'PhonePe Ref: 4892',
          time: '10:25 AM'
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
        }
      ],
      recycleBin: [
        {
          id: 'del-1',
          name: 'గారపాటి రామారావు',
          city: 'ఖమ్మం',
          amount: 2116,
          deletedDate: 'నిన్న 4:30 PM'
        }
      ]
    };

    function playTempleChime() {
      if (!chimeEnabled) return;
      try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();
        const fundamental = 587.33;
        const frequencies = [fundamental, fundamental * 1.5, fundamental * 2.05];
        const now = ctx.currentTime;
        frequencies.forEach((freq, idx) => {
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now);
          gain.gain.setValueAtTime(0.2 / (idx + 1), now);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + 1.8);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now);
          osc.stop(now + 2.2);
        });
        const bellIcon = document.getElementById('bell-icon');
        if (bellIcon) {
          bellIcon.classList.remove('ring-active');
          void bellIcon.offsetWidth;
          bellIcon.classList.add('ring-active');
        }
      } catch (e) {}
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

      renderAllDynamicSections();
    }

    function navigateToPage(pageId) {
      document.querySelectorAll('.page-section').forEach(p => p.classList.remove('active-page'));
      const target = document.getElementById(`page-${pageId}`);
      if (target) target.classList.add('active-page');

      const landingCtas = document.getElementById('landing-auth-ctas');
      const appUser = document.getElementById('app-user-pill');

      if (pageId === 'app') {
        landingCtas.classList.add('hidden');
        appUser.classList.remove('hidden');
        appUser.classList.add('flex');
        switchAppTab('dashboard');
        renderAllDynamicSections();
      } else {
        landingCtas.classList.remove('hidden');
        appUser.classList.add('hidden');
        appUser.classList.remove('flex');
      }
    }

    function enterAsGuest() {
      currentUser = { name: "గెస్ట్ విజిటర్ (డెమో)", isGuest: true };
      document.getElementById('user-display-name').innerText = currentUser.name;
      navigateToPage('app');
      playTempleChime();
    }

    function loginWithGoogle() {
      currentUser = { name: "రఘు వర్మ (Verified)" };
      document.getElementById('user-display-name').innerText = currentUser.name;
      navigateToPage('app');
      playTempleChime();
    }

    function sendOtpSim() {
      loginWithGoogle();
    }

    function logoutToLanding() {
      currentUser = null;
      navigateToPage('landing');
    }

    function switchAppTab(tabName) {
      document.querySelectorAll('.app-screen').forEach(s => s.classList.remove('active-app-screen'));
      const target = document.getElementById(`subtab-${tabName}`);
      if (target) target.classList.add('active-app-screen');

      if (tabName === 'desk') {
        setTimeout(() => {
          const inp = document.getElementById('desk-input-name');
          if (inp) inp.focus();
        }, 100);
      }
    }

    // Dynamic Cultural Fields
    function onCategoryChanged(cat) {
      const container = document.getElementById('dynamic-participant-fields');
      const nameInput = document.getElementById('modal-input-name');

      if (cat === 'wedding') {
        nameInput.placeholder = "ఉదా: ఆనంద్ వర్మ & శ్రేయారెడ్డి వివాహం";
        container.innerHTML = `
          <div class="text-[10px] font-bold text-amber-900 border-b border-amber-200 pb-0.5">వధూవరుల వివరాలు (Bride & Groom):</div>
          <div class="grid grid-cols-2 gap-1.5">
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">వరుడి పేరు *</label>
              <input id="field-groom" type="text" placeholder="వరుడి పేరు" class="w-full h-7 px-2 bg-white border border-stone-200 rounded text-xs">
            </div>
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">వధువు పేరు *</label>
              <input id="field-bride" type="text" placeholder="వధువు పేరు" class="w-full h-7 px-2 bg-white border border-stone-200 rounded text-xs">
            </div>
          </div>
        `;
      } else if (cat === 'halfsaree' || cat === 'pushpavathi') {
        nameInput.placeholder = (cat === 'halfsaree') ? "ఉదా: కుమారి సాహితీ లంగా ఓణీల వేడుక" : "ఉదా: కుమారి అనన్య పుష్పవతి వేడుక";
        container.innerHTML = `
          <div class="text-[10px] font-bold text-rose-900 border-b border-rose-200 pb-0.5">బాలిక వివరాలు (Female Only):</div>
          <div class="grid grid-cols-2 gap-1.5">
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">అమ్మాయి పేరు *</label>
              <input id="field-girl" type="text" placeholder="అమ్మాయి పేరు" class="w-full h-7 px-2 bg-white border border-stone-200 rounded text-xs">
            </div>
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">తల్లిదండ్రుల పేర్లు</label>
              <input id="field-parents" type="text" placeholder="తల్లి & తండ్రి" class="w-full h-7 px-2 bg-white border border-stone-200 rounded text-xs">
            </div>
          </div>
        `;
      } else if (cat === 'odugu' || cat === 'panchala') {
        nameInput.placeholder = (cat === 'odugu') ? "ఉదా: చిరంజీవి సాత్విక్ ఒడుగు / ఉపనయనం" : "ఉదా: చిరంజీవి హర్ష పంచల వేడుక";
        container.innerHTML = `
          <div class="text-[10px] font-bold text-amber-900 border-b border-amber-200 pb-0.5">బాలుడి వివరాలు (Male Only):</div>
          <div class="grid grid-cols-2 gap-1.5">
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">అబ్బాయి పేరు (వటువు) *</label>
              <input id="field-boy" type="text" placeholder="అబ్బాయి పేరు" class="w-full h-7 px-2 bg-white border border-stone-200 rounded text-xs">
            </div>
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">తల్లిదండ్రుల పేర్లు</label>
              <input id="field-parents" type="text" placeholder="తల్లి & తండ్రి" class="w-full h-7 px-2 bg-white border border-stone-200 rounded text-xs">
            </div>
          </div>
        `;
      } else if (cat === 'naming' || cat === 'mundan' || cat === 'birthday') {
        nameInput.placeholder = "ఉదా: నామకరణం / పుట్టినరోజు సంబరాలు";
        container.innerHTML = `
          <div class="text-[10px] font-bold text-amber-900 border-b border-amber-200 pb-0.5">చిన్నారుల వివరాలు:</div>
          <div class="grid grid-cols-3 gap-1.5">
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">పిల్లల పేరు *</label>
              <input id="field-child" type="text" placeholder="పేరు" class="w-full h-7 px-1.5 bg-white border border-stone-200 rounded text-xs">
            </div>
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">లింగం</label>
              <select id="field-gender" class="w-full h-7 px-1 bg-white border border-stone-200 rounded text-[11px] font-semibold">
                <option value="బాబు (Boy)">బాబు</option>
                <option value="పాప (Girl)">పాప</option>
              </select>
            </div>
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">తల్లిదండ్రులు</label>
              <input id="field-parents" type="text" placeholder="తల్లిదండ్రులు" class="w-full h-7 px-1.5 bg-white border border-stone-200 rounded text-xs">
            </div>
          </div>
        `;
      } else if (cat === 'housewarming') {
        nameInput.placeholder = "ఉదా: శ్రీ వేంకటేశ్వర నిలయం గృహప్రవేశం";
        container.innerHTML = `
          <div class="text-[10px] font-bold text-amber-900 border-b border-amber-200 pb-0.5">గృహ యజమానులు:</div>
          <div class="grid grid-cols-2 gap-1.5">
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">ఇంటి పేరు / గృహ నామం</label>
              <input id="field-house" type="text" placeholder="గృహ నామం" class="w-full h-7 px-2 bg-white border border-stone-200 rounded text-xs">
            </div>
            <div>
              <label class="block font-bold text-stone-700 text-[10px] mb-0.5">యజమానుల పేర్లు *</label>
              <input id="field-owners" type="text" placeholder="దంపతుల పేర్లు" class="w-full h-7 px-2 bg-white border border-stone-200 rounded text-xs">
            </div>
          </div>
        `;
      } else {
        container.innerHTML = `
          <div>
            <label class="block font-bold text-stone-700 text-[10px] mb-0.5">ముఖ్య వ్యక్తుల పేర్లు *</label>
            <input id="field-hosts" type="text" placeholder="పేర్లు" class="w-full h-7 px-2 bg-white border border-stone-200 rounded text-xs">
          </div>
        `;
      }
    }

    function selectCategorySuggestion(cat, defaultTitle) {
      document.getElementById('modal-select-cat').value = cat;
      document.getElementById('modal-input-name').value = defaultTitle;
      onCategoryChanged(cat);
    }

    // City Autocomplete
    function onCityInputTyped(query) {
      const dropdown = document.getElementById('city-suggestions-dropdown');
      if (!dropdown) return;
      const q = query.trim().toLowerCase();
      let matches = CITY_DATABASE;
      if (q) {
        matches = CITY_DATABASE.filter(item => 
          item.city.toLowerCase().includes(q) || item.state.toLowerCase().includes(q) || item.pincode.includes(q)
        );
      }
      if (matches.length === 0) {
        dropdown.innerHTML = `<div class="p-2 text-center text-[10px] text-stone-400">సిటీ నేరుగా టైప్ చేయండి</div>`;
        dropdown.classList.remove('hidden');
        return;
      }
      dropdown.innerHTML = matches.map(item => `
        <div onclick="selectCityItem('${item.city}', '${item.state}', '${item.pincode}')" class="p-2 hover:bg-amber-50 cursor-pointer border-b border-stone-100 flex items-center justify-between">
          <div>
            <div class="font-bold text-[11px] text-stone-900">${item.city}</div>
            <div class="text-[9px] text-stone-500">${item.state}</div>
          </div>
          <span class="text-[9px] font-bold text-amber-800 bg-amber-100 px-1.5 py-0.5 rounded">${item.pincode}</span>
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

    document.addEventListener('click', (e) => {
      const cityInput = document.getElementById('modal-input-city');
      const dropdown = document.getElementById('city-suggestions-dropdown');
      if (dropdown && !dropdown.contains(e.target) && e.target !== cityInput) {
        dropdown.classList.add('hidden');
      }
    });

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

      if (!title || !city) {
        alert(currentLang === 'te' ? 'దయచేసి పేరు మరియు ఊరిని నమోదు చేయండి!' : 'Please enter event title & city!');
        return;
      }

      let hosts = 'ముఖ్య వ్యక్తులు';
      if (cat === 'wedding') {
        const groom = document.getElementById('field-groom')?.value.trim() || 'వరుడు';
        const bride = document.getElementById('field-bride')?.value.trim() || 'వధువు';
        hosts = `${groom} & ${bride}`;
      } else if (cat === 'halfsaree' || cat === 'pushpavathi') {
        hosts = document.getElementById('field-girl')?.value.trim() || 'అమ్మాయి';
      } else if (cat === 'odugu' || cat === 'panchala') {
        hosts = document.getElementById('field-boy')?.value.trim() || 'అబ్బాయి';
      } else if (cat === 'naming' || cat === 'mundan' || cat === 'birthday') {
        hosts = document.getElementById('field-child')?.value.trim() || 'పాప/బాబు';
      } else if (cat === 'housewarming') {
        hosts = document.getElementById('field-owners')?.value.trim() || 'గృహయజమానులు';
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
        document.getElementById('app-event-meta').innerText = `${ev.venue} • ${ev.date}`;
      }
      renderAllDynamicSections();
      switchAppTab('dashboard');
    }

    function setDeskAmount(val) {
      const inp = document.getElementById('desk-input-amount');
      if (inp) {
        inp.value = val;
        inp.focus();
      }
    }

    function resetLiveDeskInputs() {
      document.getElementById('desk-input-name').value = '';
      document.getElementById('desk-input-city').value = '';
      document.getElementById('desk-input-amount').value = '1116';
      document.getElementById('desk-input-name').focus();
    }

    function saveLiveDeskEntry() {
      const name = document.getElementById('desk-input-name').value.trim();
      const city = document.getElementById('desk-input-city').value.trim() || 'స్వగ్రామం';
      const relation = document.getElementById('desk-select-relation').value;
      const giftType = document.getElementById('desk-select-gift-type').value;
      const amount = parseInt(document.getElementById('desk-input-amount').value) || 1116;

      if (!name) {
        alert(currentLang === 'te' ? 'దయచేసి అతిథి పేరు రాయండి!' : 'Please enter guest name!');
        return;
      }

      const now = new Date();
      const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

      state.entries.unshift({
        id: 'ent-' + Date.now(),
        eventId: state.activeEventId,
        name: name,
        city: city,
        relation: relation,
        giftType: giftType,
        amount: amount,
        time: timeStr
      });

      playTempleChime();
      renderAllDynamicSections();
      resetLiveDeskInputs();
    }

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
      if (deskTot) deskTot.innerText = '₹' + totalReceived.toLocaleString('en-IN');
      const deskCnt = document.getElementById('desk-screen-count');
      if (deskCnt) deskCnt.innerText = `${currentEntries.length} మంది`;

      const dashStream = document.getElementById('dash-recent-stream');
      if (dashStream) {
        dashStream.innerHTML = currentEntries.slice(0, 3).map(e => `
          <div class="p-2 rounded-lg bg-stone-50 border border-stone-200 flex items-center justify-between text-xs">
            <div>
              <span class="font-bold text-stone-900 block">${e.name}</span>
              <span class="text-[9px] text-stone-500">${e.city} • ${e.relation}</span>
            </div>
            <span class="font-bold text-stone-900">₹${e.amount.toLocaleString('en-IN')}</span>
          </div>
        `).join('');
      }

      renderReciprocityList();

      const ledgerCont = document.getElementById('ledger-table-container');
      if (ledgerCont) {
        ledgerCont.innerHTML = currentEntries.map(e => `
          <div class="p-2.5 rounded-lg bg-white border border-stone-200 flex items-center justify-between text-xs">
            <div>
              <div class="font-bold text-stone-900">${e.name}</div>
              <div class="text-[9px] text-stone-500">${e.city} • ${e.relation} • ${e.giftType}</div>
            </div>
            <div class="text-right">
              <div class="font-bold text-stone-900">₹${e.amount.toLocaleString('en-IN')}</div>
              <button onclick="deleteEntry('${e.id}')" class="text-[9px] text-rose-600 hover:underline">తొలగించు</button>
            </div>
          </div>
        `).join('');
      }

      const eventsGrid = document.getElementById('app-events-grid');
      if (eventsGrid) {
        eventsGrid.innerHTML = state.events.map(ev => `
          <div onclick="setActiveEvent('${ev.id}')" class="p-2.5 rounded-xl bg-white border ${ev.id === state.activeEventId ? 'border-amber-400 ring-1 ring-amber-400/30' : 'border-stone-200'} cursor-pointer">
            <div class="flex items-center justify-between text-xs">
              <span class="font-bold text-stone-900">${ev.name}</span>
              <span class="font-bold text-amber-800">₹${(ev.totalCash || 0).toLocaleString('en-IN')}</span>
            </div>
            <p class="text-[10px] text-stone-500 mt-0.5">${ev.venue} • ${ev.date}</p>
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
      container.innerHTML = filtered.map(r => `
        <div class="p-2.5 rounded-lg bg-white border border-stone-200 space-y-1 text-xs">
          <div class="flex items-center justify-between">
            <span class="font-bold text-stone-900">${r.name}</span>
            <span class="text-[9px] font-bold text-emerald-800 bg-emerald-100 px-1.5 py-0.5 rounded">సరితూగింది</span>
          </div>
          <div class="flex justify-between text-[10px] text-stone-500">
            <span>గతంలో ఇచ్చింది: ₹${r.pastWeGave}</span>
            <span>నేడు ఇచ్చింది: ₹${r.todayTheyGave}</span>
          </div>
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

    function exportToCsv() {
      alert("CSV Export Downloaded Successfully!");
    }
    function exportToPdf() {
      window.print();
    }
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

    window.addEventListener('DOMContentLoaded', () => {
      startClock();
      setDeviceViewMode('mobile'); // Initial view is Mobile Phone!
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

print("SUCCESS: Mobile + Desktop Master written to", target_path)
