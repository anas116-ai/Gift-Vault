# -*- coding: utf-8 -*-
"""
GiftVault - Clean, Simple, Modern Luxury Redesign
Zero clutter, clean universal typography (Inter + Plus Jakarta Sans + Noto Sans Telugu),
Minimalist iconic logo mark, clean uncluttered UI, perfectly proportional buttons and cards.
"""

import os
import shutil

html_template = """<!DOCTYPE html>
<html lang="te" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GiftVault | గిఫ్ట్ వాలెట్ - చదివింపుల డిజిటల్ లెడ్జర్</title>
  
  <!-- Clean, Modern, World-Class Typography (Inter + Plus Jakarta Sans + Noto Sans Telugu) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+Telugu:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              gold: '#D4AF37',
              goldDark: '#B38F26',
              goldLight: '#FDFBF4',
              goldBorder: '#E6D5A7',
              dark: '#0F172A',
              darkSurface: '#1E293B',
              slate: '#334155',
              crimson: '#991B1B',
              crimsonLight: '#FEF2F2',
              emerald: '#059669',
              emeraldLight: '#ECFDF5',
              canvas: '#F8FAFC',
            }
          },
          fontFamily: {
            sans: ['Inter', 'Plus Jakarta Sans', 'sans-serif'],
            telugu: ['Noto Sans Telugu', 'Inter', 'sans-serif'],
          }
        }
      }
    }
  </script>

  <style>
    body {
      font-family: 'Inter', 'Noto Sans Telugu', sans-serif;
      background-color: #F8FAFC;
      color: #0F172A;
      overflow-x: hidden;
      -webkit-tap-highlight-color: transparent;
      letter-spacing: -0.01em;
    }

    .font-brand {
      font-family: 'Plus Jakarta Sans', 'Inter', sans-serif;
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    /* Clean Card Elevation */
    .clean-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 16px;
      box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05);
      transition: all 180ms cubic-bezier(0.23, 1, 0.32, 1);
    }
    .clean-card:hover {
      border-color: #CBD5E1;
      box-shadow: 0 4px 12px -2px rgba(0, 0, 0, 0.07);
    }

    /* Spring-Physics Tactile Press */
    button:active, .btn-press:active {
      transform: scale(0.98);
      transition: transform 100ms cubic-bezier(0.23, 1, 0.32, 1);
    }

    /* REALISTIC ANDROID SMARTPHONE CHASSIS */
    .phone-chassis {
      width: 390px;
      height: 810px;
      border-radius: 52px;
      background: #0F172A;
      padding: 12px;
      box-shadow: 0 0 0 2px #334155, 0 25px 60px -15px rgba(15, 23, 42, 0.4), 0 10px 25px -8px rgba(0, 0, 0, 0.2);
      position: relative;
      flex-shrink: 0;
      margin: 0 auto;
      transition: all 300ms cubic-bezier(0.23, 1, 0.32, 1);
    }

    .phone-screen {
      width: 100%;
      height: 100%;
      border-radius: 42px;
      background: #F8FAFC;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      position: relative;
    }

    .screen-scroll::-webkit-scrollbar { width: 3px; }
    .screen-scroll::-webkit-scrollbar-thumb {
      background: #CBD5E1;
      border-radius: 3px;
    }

    /* DESKTOP FULL-WIDTH VIEW */
    .desktop-viewport {
      width: 100% !important;
      max-width: 1200px !important;
      height: auto !important;
      min-height: 85vh !important;
      border-radius: 20px !important;
      background: transparent !important;
      padding: 0 !important;
      box-shadow: none !important;
    }

    .desktop-viewport .phone-screen {
      border-radius: 20px !important;
      height: auto !important;
      min-height: 85vh !important;
      box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.06);
      border: 1px solid #E2E8F0;
    }

    /* Simple Clean Red Book Lined Layout */
    .simple-red-book {
      background: #7F1D1D;
      border: 2px solid #D4AF37;
      border-radius: 16px;
      padding: 14px;
    }
    .simple-lined-paper {
      background: #FFFFFF;
      background-image: repeating-linear-gradient(transparent, transparent 31px, #F1F5F9 31px, #F1F5F9 32px);
      border-radius: 10px;
      border: 1px solid #E2E8F0;
      padding: 16px;
    }

    .page-section { display: none; }
    .active-page { display: block; }

    .app-screen { display: none; }
    .active-app-screen { display: block; }
  </style>
</head>
<body class="min-h-screen text-slate-900 flex flex-col justify-between selection:bg-amber-100">

  <!-- ============================================================== -->
  <!-- 1. TOP GLOBAL NAVIGATION: CLEAN, MINIMAL & INTUITIVE -->
  <!-- ============================================================== -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 px-4 lg:px-8 py-3">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
      
      <!-- Left: Simple, Iconic Logo & Clean Modern Wordmark -->
      <div onclick="navigateToPage('landing')" class="flex items-center gap-3 cursor-pointer select-none">
        
        <!-- Minimalist Modern Geometric Emblem -->
        <div class="w-9 h-9 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-center shadow-xs">
          <!-- Sleek Modern Geometric GV Vault Mark -->
          <svg class="w-5 h-5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <!-- Modern interlocking G & V Vault Motif -->
            <path d="M12 2L3 7v6c0 5.5 3.8 10.7 9 12 5.2-1.3 9-6.5 9-12V7l-9-5z"/>
            <path d="M12 8v8"/>
            <path d="M9 11l3 3 3-3"/>
          </svg>
        </div>

        <div>
          <div class="flex items-center gap-2">
            <span class="font-brand text-base tracking-tight text-slate-950 font-bold">GiftVault</span>
            <span class="text-[10px] font-semibold px-2 py-0.5 rounded-md bg-amber-50 text-amber-800 border border-amber-200">గిఫ్ట్ వాలెట్</span>
          </div>
          <p class="text-[11px] text-slate-500 font-normal">చదివింపుల డిజిటల్ లెడ్జర్ & ఈవెంట్ ఖజానా</p>
        </div>
      </div>

      <!-- Center: Device Mode Switcher (Android Phone vs Desktop Web) -->
      <div class="flex items-center bg-slate-100 p-1 rounded-xl border border-slate-200 text-xs font-medium">
        <button id="toggle-device-mobile" onclick="setDeviceViewMode('mobile')" class="px-3 py-1.5 rounded-lg bg-slate-900 text-white shadow-xs transition-all flex items-center gap-1.5 btn-press">
          <svg class="w-3.5 h-3.5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12.01" y2="18"></line></svg>
          <span>మొబైల్ వెర్షన్</span>
        </button>
        <button id="toggle-device-desktop" onclick="setDeviceViewMode('desktop')" class="px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition-all flex items-center gap-1.5 btn-press">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="14" x="2" y="3" rx="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
          <span>డెస్క్‌టాప్ వెర్షన్</span>
        </button>
      </div>

      <!-- Right: Clean Language Selector & Direct Action -->
      <div class="flex items-center gap-2">
        
        <!-- Offline-First LocalStorage & Cloud Sync Badge -->
        <div class="hidden md:flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-800 text-[11px] font-medium">
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
          <span>ఆఫ్‌లైన్ సేఫ్ • సింక్డ్</span>
        </div>

        <!-- Language Dropdown -->
        <div class="flex items-center gap-1 text-xs bg-white border border-slate-200 rounded-lg px-2.5 py-1 shadow-2xs">
          <svg class="w-3.5 h-3.5 text-slate-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
          <select id="lang-selector" onchange="onLanguageChanged(this.value)" class="bg-transparent text-xs font-semibold text-slate-700 focus:outline-none cursor-pointer">
            <option value="te" selected>తెలుగు</option>
            <option value="en">English</option>
            <option value="hi">हिन्दी</option>
          </select>
        </div>

        <button onclick="navigateToPage('landing')" class="px-2.5 py-1 text-xs text-slate-600 hover:text-slate-900 font-medium" data-i18n="nav_home">హోమ్</button>
        <button onclick="navigateToPage('app')" class="px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-slate-900 text-amber-400 hover:bg-slate-800 shadow-2xs btn-press" data-i18n="nav_app">లెడ్జర్ ఓపెన్</button>
      </div>

    </div>
  </header>

  <!-- ============================================================== -->
  <!-- 2. MAIN CONTAINER: REALISTIC CHASSIS OR CLEAN DESKTOP -->
  <!-- ============================================================== -->
  <main class="py-6 px-3 flex-1 flex flex-col items-center justify-center">
    
    <div id="main-viewport-wrapper" class="phone-chassis">
      
      <div id="main-viewport-screen" class="phone-screen">
        
        <!-- Native Android Status Bar -->
        <div id="mobile-status-bar" class="h-7 bg-slate-900 text-slate-300 px-5 flex items-center justify-between text-[11px] font-semibold select-none z-30 flex-shrink-0">
          <span id="android-clock">10:30 AM</span>
          <div class="w-3 h-3 rounded-full bg-black border border-slate-800 mx-auto"></div>
          <div class="flex items-center gap-1 px-2 py-0.5 rounded-full bg-slate-800 border border-slate-700 text-[9px]">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            <span class="text-amber-300 font-bold">5G</span>
            <span class="text-slate-300 ml-1">100%</span>
          </div>
        </div>

        <!-- Scrollable Content Screen -->
        <div id="screen-scroll-container" class="flex-1 overflow-y-auto screen-scroll p-4 space-y-4">

          <!-- ============================================== -->
          <!-- SCREEN A: CLEAN, REFINED LANDING PAGE -->
          <!-- ============================================== -->
          <div id="page-landing" class="page-section active-page space-y-4">
            
            <!-- Hero Card: Clean, Modern, Not Overwhelming -->
            <div class="rounded-2xl bg-white border border-slate-200 p-5 text-center shadow-xs space-y-3">
              
              <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-50 text-amber-800 text-[11px] font-medium border border-amber-200">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
                <span>డిజిటల్ చదివింపుల ఖజానా</span>
              </div>

              <h1 class="text-xl sm:text-2xl font-bold text-slate-950 tracking-tight leading-snug">
                చదివింపుల లెడ్జర్ & ఈవెంట్ ఖర్చుల మేనేజర్
              </h1>

              <p class="text-xs text-slate-600 max-w-sm mx-auto leading-relaxed">
                వివాహాలు, గృహప్రవేశాలు & శుభకార్యాల చదివింపుల రికార్డు, ఈవెంట్ ఖర్చులు, బంగారం-వెండి కానుకల లెక్క మరియు 1-క్లిక్ WhatsApp రసీదులు.
              </p>

              <!-- Clean 4-Metric Pillars -->
              <div class="grid grid-cols-2 gap-2 text-left text-xs pt-1">
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                  <span class="text-slate-900 font-semibold block text-[11px]">వచ్చినవి vs ఇచ్చినవి</span>
                  <span class="text-slate-500 text-[10px]">సామాజిక బంధుత్వ సరితూకం</span>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                  <span class="text-slate-900 font-semibold block text-[11px]">ఖర్చులు & బడ్జెట్</span>
                  <span class="text-slate-500 text-[10px]">ఈవెంట్ నికర మిగులు లెక్క</span>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                  <span class="text-slate-900 font-semibold block text-[11px]">బంగారం & వెండి</span>
                  <span class="text-slate-500 text-[10px]">నగదుతో పాటు కానుకల లెక్క</span>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                  <span class="text-slate-900 font-semibold block text-[11px]">WhatsApp రసీదు</span>
                  <span class="text-slate-500 text-[10px]">వెంటనే కృతజ్ఞతా సందేశం</span>
                </div>
              </div>

              <!-- Clean CTAs -->
              <div class="pt-2 flex flex-col gap-2">
                <button onclick="navigateToPage('app')" class="w-full py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-amber-400 font-semibold text-xs shadow-xs btn-press">
                  <span>ఉచితంగా ప్రారంభించండి →</span>
                </button>
                <button onclick="navigateToPage('auth')" class="w-full py-2 rounded-xl bg-white hover:bg-slate-50 text-slate-700 font-medium text-xs border border-slate-200 btn-press">
                  <span>లాగిన్ / ఖాతా వివరాలు</span>
                </button>
              </div>

            </div>

            <!-- Traditional Red Book Clean Preview -->
            <div class="clean-card p-3.5 space-y-1.5 text-left">
              <div class="flex items-center justify-between">
                <span class="text-xs font-semibold text-red-900">సాంప్రదాయ ఎర్ర పుస్తకం మోడ్</span>
                <span class="text-[10px] text-slate-500 font-medium">॥ శ్రీరస్తు శుభమస్తు ॥</span>
              </div>
              <p class="text-[11px] text-slate-600 leading-normal">
                తెలుగువారి సంప్రదాయ ఎర్ర బైండింగ్ చదివింపుల డైరీ తరహాలోనే, ప్రతి అతిథి ఊరు, బంధుత్వం, కవరు నెంబరుతో కూడిన డిజిటల్ లెడ్జర్.
              </p>
            </div>

          </div>

          <!-- ============================================== -->
          <!-- SCREEN B: AUTHENTICATION / LOGIN -->
          <!-- ============================================== -->
          <div id="page-auth" class="page-section space-y-4">
            <div class="clean-card p-5 space-y-3.5 text-center">
              
              <div class="w-11 h-11 mx-auto rounded-xl bg-slate-100 border border-slate-200 flex items-center justify-center">
                <svg class="w-5 h-5 text-slate-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><line x1="19" y1="8" x2="19" y2="14"></line><line x1="22" y1="11" x2="16" y2="11"></line></svg>
              </div>

              <div>
                <h2 class="font-bold text-slate-900 text-base">ఖాతాలోకి ప్రవేశించండి</h2>
                <p class="text-xs text-slate-500">మీ కుటుంబ శుభకార్యాల చదివింపుల వివరాలు భద్రంగా ఉంటాయి</p>
              </div>

              <!-- Official Google Sign-In -->
              <button onclick="loginWithGoogleSim()" class="w-full h-10 px-3 rounded-xl border border-slate-200 bg-white hover:bg-slate-50 text-slate-700 font-medium text-xs flex items-center justify-center gap-2 shadow-2xs btn-press">
                <svg class="w-4 h-4" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                  <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                  <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                  <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
                </svg>
                <span>Google తో లాగిన్ అవ్వండి</span>
              </button>

              <div class="relative flex items-center justify-center my-1.5">
                <div class="border-t border-slate-200 w-full"></div>
                <span class="bg-white px-2 text-[10px] text-slate-400 uppercase font-semibold">లేదా</span>
              </div>

              <!-- Phone OTP -->
              <div class="space-y-1.5 text-left">
                <label class="block text-[11px] font-medium text-slate-700">మొబైల్ నెంబర్:</label>
                <div class="flex gap-1.5">
                  <input id="auth-phone-input" type="tel" placeholder="+91 98765 43210" class="flex-1 h-9 px-3 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:border-slate-400">
                  <button onclick="sendOtpSim()" class="h-9 px-3 rounded-lg bg-slate-900 text-white font-medium text-xs btn-press">OTP</button>
                </div>
              </div>

              <div class="pt-1">
                <button onclick="enterAsGuest()" class="w-full h-9 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 font-medium text-xs flex items-center justify-center gap-1.5 btn-press">
                  <span>డెమో చూడండి (గెస్ట్ మోడ్)</span>
                </button>
              </div>

            </div>
          </div>

          <!-- ============================================== -->
          <!-- SCREEN C: MASTER APP WORKSPACE -->
          <!-- ============================================== -->
          <div id="page-app" class="page-section space-y-3.5">
            
            <!-- Active Event Header Banner -->
            <div class="clean-card p-3.5 space-y-2">
              <div class="flex items-center justify-between">
                <div>
                  <div class="flex items-center gap-1.5">
                    <h3 id="app-event-name" class="font-bold text-xs text-slate-900 leading-tight">
                      ఆనంద్ & శ్రేయ వివాహ మహోత్సవం
                    </h3>
                    <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                  </div>
                  <p id="app-event-meta" class="text-[10px] text-slate-500 mt-0.5">శ్రీ కన్వెన్షన్, హైదరాబాద్ • 15 నవంబర్ 2026</p>
                </div>
                <button onclick="openModalNewEvent()" class="h-7 px-2.5 rounded-lg bg-slate-900 text-amber-400 hover:bg-slate-800 text-[10px] font-semibold flex items-center gap-1 shadow-2xs btn-press">
                  <span>+</span>
                  <span>కొత్త ఈవెంట్</span>
                </button>
              </div>

              <!-- Counter Desk Selector -->
              <div class="flex items-center justify-between pt-1.5 border-t border-slate-100 text-[10px]">
                <div class="flex items-center gap-1.5">
                  <span class="text-slate-500 font-medium">కౌంటర్:</span>
                  <select id="active-counter-select" onchange="onCounterChanged(this.value)" class="bg-slate-100 text-slate-800 font-medium px-2 py-0.5 rounded border border-slate-200 focus:outline-none">
                    <option value="వరుడి వైపు కౌంటర్ (Groom Desk)">వరుడి వైపు కౌంటర్</option>
                    <option value="వధువు వైపు కౌంటర్ (Bride Desk)">వధువు వైపు కౌంటర్</option>
                    <option value="విఐపి డెస్క్">విఐపి & బంధువుల డెస్క్</option>
                  </select>
                </div>
                <span class="text-emerald-700 font-medium">ఆపరేటర్ 01</span>
              </div>
            </div>

            <!-- Segmented Pill Navigation Tabs: Simple & Clean -->
            <div class="flex items-center gap-1 overflow-x-auto pb-1 text-[11px] font-medium select-none">
              <button onclick="switchAppTab('dashboard')" id="navtab-dashboard" class="px-3 py-1.5 rounded-lg bg-slate-900 text-white shrink-0 btn-press">హోమ్</button>
              <button onclick="switchAppTab('desk')" id="navtab-desk" class="px-3 py-1.5 rounded-lg bg-white text-slate-700 hover:bg-slate-100 border border-slate-200 shrink-0 btn-press">కౌంటర్ డెస్క్</button>
              <button onclick="switchAppTab('ledger')" id="navtab-ledger" class="px-3 py-1.5 rounded-lg bg-white text-slate-700 hover:bg-slate-100 border border-slate-200 shrink-0 btn-press">లెడ్జర్</button>
              <button onclick="switchAppTab('expenses')" id="navtab-expenses" class="px-3 py-1.5 rounded-lg bg-white text-slate-700 hover:bg-slate-100 border border-slate-200 shrink-0 btn-press">ఖర్చులు</button>
              <button onclick="switchAppTab('reciprocity')" id="navtab-reciprocity" class="px-3 py-1.5 rounded-lg bg-white text-slate-700 hover:bg-slate-100 border border-slate-200 shrink-0 btn-press">సరితూకం</button>
              <button onclick="switchAppTab('invites')" id="navtab-invites" class="px-3 py-1.5 rounded-lg bg-white text-slate-700 hover:bg-slate-100 border border-slate-200 shrink-0 btn-press">ఆహ్వానాలు</button>
              <button onclick="switchAppTab('qr')" id="navtab-qr" class="px-3 py-1.5 rounded-lg bg-white text-slate-700 hover:bg-slate-100 border border-slate-200 shrink-0 btn-press">QR పే</button>
            </div>

            <!-- ======================================================= -->
            <!-- SUB-TAB 1: DASHBOARD OVERVIEW -->
            <!-- ======================================================= -->
            <div id="subtab-dashboard" class="app-screen active-app-screen space-y-3">
              
              <!-- 4 Summary Metric Cards -->
              <div class="grid grid-cols-2 gap-2">
                
                <!-- Received -->
                <div class="p-3.5 rounded-xl bg-white border border-slate-200 shadow-2xs">
                  <span class="text-[10px] font-medium text-slate-500 uppercase tracking-wide block">వచ్చిన చదివింపులు</span>
                  <div class="flex items-baseline gap-1 mt-1">
                    <span id="metric-total-received" class="text-lg font-bold text-emerald-700 font-brand">₹7,85,400</span>
                  </div>
                  <span id="metric-received-count" class="text-[10px] text-slate-500 block mt-0.5">18 మంది బంధువులు</span>
                </div>

                <!-- Expenses -->
                <div class="p-3.5 rounded-xl bg-white border border-slate-200 shadow-2xs">
                  <span class="text-[10px] font-medium text-slate-500 uppercase tracking-wide block">ఈవెంట్ ఖర్చులు</span>
                  <div class="flex items-baseline gap-1 mt-1">
                    <span id="metric-total-expenses" class="text-lg font-bold text-red-700 font-brand">₹5,40,000</span>
                  </div>
                  <span class="text-[10px] text-slate-500 block mt-0.5">మండపం, భోజనాలు & డెకరేషన్</span>
                </div>

                <!-- Net Surplus -->
                <div class="p-3.5 rounded-xl bg-white border border-slate-200 shadow-2xs">
                  <span class="text-[10px] font-medium text-slate-500 uppercase tracking-wide block">నికర మిగులు</span>
                  <div class="flex items-baseline gap-1 mt-1">
                    <span id="metric-net-balance" class="text-lg font-bold text-slate-900 font-brand">+₹2,45,400</span>
                  </div>
                  <span class="text-[10px] text-emerald-700 font-medium block mt-0.5">✓ మిగులు బ్యాలెన్స్</span>
                </div>

                <!-- Gold & Silver -->
                <div class="p-3.5 rounded-xl bg-white border border-slate-200 shadow-2xs">
                  <span class="text-[10px] font-medium text-slate-500 uppercase tracking-wide block">బంగారం & వెండి</span>
                  <div class="text-xs font-bold text-slate-800 mt-1 font-brand">
                    <span id="metric-total-gold">🪙 15 గ్రా.</span> • <span id="metric-total-silver">🥈 180 గ్రా.</span>
                  </div>
                  <span class="text-[10px] text-slate-500 block mt-0.5">4 కానుకలు</span>
                </div>

              </div>

              <!-- Quick Launch Actions -->
              <div class="grid grid-cols-4 gap-1.5 text-center text-[10px] font-medium">
                <button onclick="switchAppTab('desk')" class="p-2.5 rounded-xl bg-slate-900 text-white flex flex-col items-center gap-1 btn-press">
                  <span class="text-xs">⚡</span>
                  <span>కౌంటర్ డెస్క్</span>
                </button>
                <button onclick="openModalAddExpense()" class="p-2.5 rounded-xl bg-white border border-slate-200 text-slate-800 flex flex-col items-center gap-1 btn-press">
                  <span class="text-xs">💸</span>
                  <span>+ ఖర్చు వేయి</span>
                </button>
                <button onclick="switchAppTab('ledger')" class="p-2.5 rounded-xl bg-white border border-slate-200 text-slate-800 flex flex-col items-center gap-1 btn-press">
                  <span class="text-xs">📖</span>
                  <span>లెడ్జర్ పుస్తకం</span>
                </button>
                <button onclick="switchAppTab('qr')" class="p-2.5 rounded-xl bg-white border border-slate-200 text-slate-800 flex flex-col items-center gap-1 btn-press">
                  <span class="text-xs">📲</span>
                  <span>సౌండ్‌బాక్స్</span>
                </button>
              </div>

              <!-- Recent Entries Stream -->
              <div class="clean-card p-3.5 space-y-2">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-slate-900">తాజా చదివింపులు</span>
                  <button onclick="switchAppTab('ledger')" class="text-[10px] text-slate-600 hover:text-slate-900 font-medium">అన్నీ చూడండి →</button>
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
              
              <div class="clean-card p-4 space-y-3">
                <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                  <div>
                    <h3 class="font-bold text-xs text-slate-900">కౌంటర్ డెస్క్ (Fast Entry)</h3>
                    <p class="text-[10px] text-slate-500">అతిథి రాగానే వివరాలు నమోదు చేసి WhatsApp రసీదు పంపండి</p>
                  </div>
                  <span class="px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200 text-[9px] font-medium">లైవ్</span>
                </div>

                <div class="space-y-2.5 text-xs">
                  
                  <!-- Guest Name & City -->
                  <div class="grid grid-cols-2 gap-2">
                    <div>
                      <label class="block text-[11px] font-medium text-slate-700 mb-0.5">అతిథి పేరు *:</label>
                      <input id="desk-input-name" type="text" placeholder="కొత్తపల్లి వెంకటేశ్వర్లు" class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:border-slate-400">
                    </div>
                    <div class="relative">
                      <label class="block text-[11px] font-medium text-slate-700 mb-0.5">ఊరు (Autocomplete):</label>
                      <input id="desk-input-city" type="text" oninput="onDeskCityInput(this.value)" placeholder="హైదరాబాద్ / గుంటూరు..." class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:border-slate-400">
                      <div id="desk-city-suggestions" class="absolute left-0 right-0 top-full mt-1 bg-white border border-slate-200 rounded-lg shadow-lg z-20 hidden max-h-36 overflow-y-auto"></div>
                    </div>
                  </div>

                  <!-- Relation & Phone -->
                  <div class="grid grid-cols-2 gap-2">
                    <div>
                      <label class="block text-[11px] font-medium text-slate-700 mb-0.5">చుట్టరికం:</label>
                      <select id="desk-select-relation" class="w-full h-8 px-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none">
                        <option value="మేనమామ తరఫు">మేనమామ తరఫు</option>
                        <option value="బావ / బావమరిది">బావ / బావమరిది</option>
                        <option value="తాత / నానమ్మ">తాత / నానమ్మ</option>
                        <option value="పెద్దనాన్న / పినతండ్రి">పెద్దనాన్న / పినతండ్రి</option>
                        <option value="అత్తయ్య / మావయ్య">అత్తయ్య / మావయ్య</option>
                        <option value="మిత్రులు">మిత్రులు (Friends)</option>
                        <option value="సహోద్యోగులు">సహోద్యోగులు</option>
                        <option value="ఇరుగుపొరుగు">ఇరుగుపొరుగు</option>
                      </select>
                    </div>
                    <div>
                      <label class="block text-[11px] font-medium text-slate-700 mb-0.5">మొబైల్ (WhatsApp కోసం):</label>
                      <input id="desk-input-phone" type="tel" placeholder="9876543210" class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none">
                    </div>
                  </div>

                  <!-- Gift Type Switcher -->
                  <div>
                    <label class="block text-[11px] font-medium text-slate-700 mb-1">కానుక రకం:</label>
                    <div class="grid grid-cols-4 gap-1 text-[10px] font-medium text-center">
                      <button type="button" onclick="setDeskGiftType('cash')" id="btn-gifttype-cash" class="py-1 rounded-lg bg-slate-900 text-white btn-press">💵 నగదు</button>
                      <button type="button" onclick="setDeskGiftType('gold')" id="btn-gifttype-gold" class="py-1 rounded-lg bg-slate-100 text-slate-700 border border-slate-200 btn-press">🪙 బంగారం</button>
                      <button type="button" onclick="setDeskGiftType('silver')" id="btn-gifttype-silver" class="py-1 rounded-lg bg-slate-100 text-slate-700 border border-slate-200 btn-press">🥈 వెండి</button>
                      <button type="button" onclick="setDeskGiftType('item')" id="btn-gifttype-item" class="py-1 rounded-lg bg-slate-100 text-slate-700 border border-slate-200 btn-press">🎁 వస్తువు</button>
                    </div>
                  </div>

                  <!-- CASH SECTION -->
                  <div id="desk-cash-section" class="space-y-2">
                    <div class="flex items-center gap-2">
                      <div class="flex-1">
                        <label class="block text-[11px] font-medium text-slate-700 mb-0.5">మొత్తం చదివింపు (₹):</label>
                        <input id="desk-input-amount" type="number" placeholder="2116" class="w-full h-9 px-3 text-sm font-bold text-slate-900 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:border-slate-400">
                      </div>
                      
                      <div class="pt-4 flex items-center gap-1.5">
                        <input type="checkbox" id="desk-check-luckyone" onchange="toggleLuckyCoin(this.checked)" class="w-4 h-4 text-slate-900 rounded">
                        <label for="desk-check-luckyone" class="text-[11px] font-medium text-slate-700 cursor-pointer">+₹1 లక్కీ నాణెం</label>
                      </div>
                    </div>

                    <!-- Quick Buttons -->
                    <div class="flex flex-wrap gap-1 pt-0.5">
                      <button type="button" onclick="setDeskQuickAmount(516)" class="px-2.5 py-0.5 rounded bg-slate-100 text-[10px] font-medium hover:bg-slate-200 border border-slate-200 btn-press">₹516</button>
                      <button type="button" onclick="setDeskQuickAmount(1116)" class="px-2.5 py-0.5 rounded bg-slate-100 text-[10px] font-medium hover:bg-slate-200 border border-slate-200 btn-press">₹1,116</button>
                      <button type="button" onclick="setDeskQuickAmount(2116)" class="px-2.5 py-0.5 rounded bg-slate-100 text-[10px] font-medium hover:bg-slate-200 border border-slate-200 btn-press">₹2,116</button>
                      <button type="button" onclick="setDeskQuickAmount(5116)" class="px-2.5 py-0.5 rounded bg-slate-100 text-[10px] font-medium hover:bg-slate-200 border border-slate-200 btn-press">₹5,116</button>
                      <button type="button" onclick="setDeskQuickAmount(11116)" class="px-2.5 py-0.5 rounded bg-slate-100 text-[10px] font-medium hover:bg-slate-200 border border-slate-200 btn-press">₹11,116</button>
                    </div>
                  </div>

                  <!-- PRECIOUS METALS SECTION -->
                  <div id="desk-precious-section" class="hidden space-y-2 p-2.5 rounded-xl bg-slate-50 border border-slate-200">
                    <div class="grid grid-cols-2 gap-2">
                      <div>
                        <label class="block text-[11px] font-medium text-slate-700 mb-0.5">బరువు / పరిమాణం:</label>
                        <input id="desk-input-metal-weight" type="text" placeholder="8 గ్రాములు / 1 తులం" class="w-full h-8 px-2 text-xs bg-white border border-slate-200 rounded-lg">
                      </div>
                      <div>
                        <label class="block text-[11px] font-medium text-slate-700 mb-0.5">ఆభరణం / వస్తువు:</label>
                        <input id="desk-input-metal-desc" type="text" placeholder="బంగారు ఉంగరం / వెండి కుందులు" class="w-full h-8 px-2 text-xs bg-white border border-slate-200 rounded-lg">
                      </div>
                    </div>
                  </div>

                  <!-- Cover & Notes -->
                  <div class="grid grid-cols-2 gap-2">
                    <div>
                      <label class="block text-[11px] font-medium text-slate-700 mb-0.5">కవరు నెంబర్:</label>
                      <input id="desk-input-cover" type="text" placeholder="కవరు #18" class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg">
                    </div>
                    <div>
                      <label class="block text-[11px] font-medium text-slate-700 mb-0.5">నోట్స్:</label>
                      <input id="desk-input-notes" type="text" placeholder="విశేషాలు..." class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg">
                    </div>
                  </div>

                  <!-- Action Buttons -->
                  <div class="pt-2 flex gap-2">
                    <button onclick="submitDeskEntry(true)" class="flex-1 h-9 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-medium text-xs flex items-center justify-center gap-1.5 shadow-xs btn-press">
                      <svg class="w-3.5 h-3.5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                      <span>నమోదు చేసి WhatsApp రసీదు పంపు</span>
                    </button>
                    <button onclick="submitDeskEntry(false)" class="h-9 px-3 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium text-xs border border-slate-200 btn-press">
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
                <div class="flex items-center bg-slate-100 p-0.5 rounded-lg border border-slate-200 text-xs font-medium">
                  <button id="btn-ledger-view-table" onclick="setLedgerView('table')" class="px-3 py-1 rounded-md bg-slate-900 text-white shadow-2xs btn-press">పట్టిక వ్యూ</button>
                  <button id="btn-ledger-view-book" onclick="setLedgerView('book')" class="px-3 py-1 rounded-md text-slate-600 hover:text-slate-900 btn-press">ఎర్ర పుస్తకం</button>
                </div>
                
                <div class="flex items-center gap-1.5">
                  <button onclick="exportToCsv()" class="h-7 px-2.5 text-[10px] font-medium rounded-lg bg-white border border-slate-200 text-slate-700 shadow-2xs btn-press">Excel</button>
                  <button onclick="exportToPdf()" class="h-7 px-2.5 text-[10px] font-medium rounded-lg bg-slate-900 text-white shadow-2xs btn-press">PDF ప్రింట్</button>
                </div>
              </div>

              <!-- Search & Filter Controls -->
              <div class="flex gap-1.5 text-xs">
                <input id="ledger-search-input" type="text" oninput="filterLedger()" placeholder="పేరు, ఊరు లేదా చుట్టరికం వెతకండి..." class="flex-1 h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
                <select id="ledger-filter-type" onchange="filterLedger()" class="h-8 px-2 bg-white border border-slate-200 rounded-lg text-[10px] font-medium">
                  <option value="all">అన్నీ</option>
                  <option value="నగదు">నగదు మాత్రమే</option>
                  <option value="బంగారం">బంగారం</option>
                  <option value="వెండి">వెండి</option>
                  <option value="వస్తువు">వస్తు రూప</option>
                </select>
              </div>

              <!-- MODE A: CLEAN DATA TABLE -->
              <div id="ledger-container-table" class="clean-card overflow-hidden">
                <div class="overflow-x-auto">
                  <table class="w-full text-left text-xs">
                    <thead class="bg-slate-50 border-b border-slate-200 text-[10px] uppercase font-semibold text-slate-500">
                      <tr>
                        <th class="p-2.5">నెం.</th>
                        <th class="p-2.5">అతిథి & ఊరు</th>
                        <th class="p-2.5">సంబంధం</th>
                        <th class="p-2.5 text-right">కానుక</th>
                        <th class="p-2.5 text-center">చర్యలు</th>
                      </tr>
                    </thead>
                    <tbody id="ledger-tbody-rows" class="divide-y divide-slate-100 text-xs">
                      <!-- Rendered via JS -->
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- MODE B: TRADITIONAL RED BOOK -->
              <div id="ledger-container-book" class="hidden simple-red-book">
                <div class="simple-lined-paper space-y-2.5">
                  <div class="text-center border-b border-slate-200 pb-2">
                    <span class="text-red-900 font-bold text-xs tracking-wider block">॥ శ్రీరస్తు శుభమస్తు ॥</span>
                    <h4 class="font-bold text-slate-900 text-xs mt-0.5">చదివింపుల దస్తావేజు</h4>
                    <span class="text-[9px] text-slate-500">శ్రీ కన్వెన్షన్, హైదరాబాద్</span>
                  </div>

                  <div id="ledger-book-entries" class="space-y-2 text-xs">
                    <!-- Rendered via JS -->
                  </div>

                  <div class="pt-2 border-t border-slate-200 flex justify-between text-xs font-bold text-slate-800">
                    <span>ఈ పుట మొత్తం చదివింపులు:</span>
                    <span id="book-page-total" class="font-brand text-emerald-700">₹7,85,400</span>
                  </div>
                </div>
              </div>

            </div>

            <!-- ======================================================= -->
            <!-- SUB-TAB 4: EVENT EXPENSES & NET BALANCE -->
            <!-- ======================================================= -->
            <div id="subtab-expenses" class="app-screen space-y-3">
              
              <div class="clean-card p-4 space-y-3">
                <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                  <div>
                    <h3 class="font-bold text-xs text-slate-900">ఈవెంట్ ఖర్చులు & బడ్జెట్</h3>
                    <p class="text-[10px] text-slate-500">మొత్తం ఖర్చులు & చదివింపుల నికర బ్యాలెన్స్ లెక్క</p>
                  </div>
                  <button onclick="openModalAddExpense()" class="h-7 px-2.5 rounded-lg bg-slate-900 text-white font-medium text-[10px] flex items-center gap-1 btn-press">
                    <span>+ ఖర్చు వేయి</span>
                  </button>
                </div>

                <!-- Clean Financial Statement Card -->
                <div class="p-3.5 rounded-xl bg-slate-900 text-white space-y-2">
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-slate-400">మొత్తం వచ్చిన చదివింపులు (+):</span>
                    <span class="font-bold text-emerald-400 font-brand">₹7,85,400</span>
                  </div>
                  <div class="flex justify-between items-center text-xs">
                    <span class="text-slate-400">మొత్తం అయిన ఈవెంట్ ఖర్చులు (-):</span>
                    <span class="font-bold text-red-400 font-brand">₹5,40,000</span>
                  </div>
                  <div class="border-t border-slate-800 pt-1.5 flex justify-between items-center text-xs font-bold">
                    <span class="text-slate-200">నికర మిగులు లాభం:</span>
                    <span class="text-sm font-bold text-emerald-400 font-brand">+₹2,45,400</span>
                  </div>
                </div>

                <!-- Category Breakdown -->
                <div class="space-y-1.5">
                  <span class="text-[10px] font-semibold text-slate-500 uppercase tracking-wide block">ఖర్చుల వర్గీకరణ:</span>
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
              
              <div class="clean-card p-4 space-y-3">
                <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                  <div>
                    <h3 class="font-bold text-xs text-slate-900">చదివింపుల సరితూకం</h3>
                    <p class="text-[10px] text-slate-500">వారు మనకు ఇచ్చింది vs గతంలో మనం వారికి ఇచ్చింది</p>
                  </div>
                  <span class="text-[10px] font-medium text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">సరితూకం</span>
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
              
              <div class="clean-card p-4 space-y-3">
                <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                  <div>
                    <h3 class="font-bold text-xs text-slate-900">ఆహ్వానాలు & హాజరు</h3>
                    <p class="text-[10px] text-slate-500">బంధువుల రాక ధ్రువీకరణ & డిజిటల్ శుభలేఖ</p>
                  </div>
                  <button onclick="shareDigitalInvite()" class="h-7 px-3 rounded-lg bg-emerald-600 text-white font-medium text-[10px] flex items-center gap-1 btn-press">
                    <span>📲 WhatsApp లో పంపు</span>
                  </button>
                </div>

                <div class="grid grid-cols-3 gap-2 text-center text-xs">
                  <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="text-[9px] text-slate-500 block">ఆహ్వానించినవి</span>
                    <span class="font-bold text-slate-900 text-sm font-brand">150</span>
                  </div>
                  <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200">
                    <span class="text-[9px] text-emerald-700 block">ధ్రువీకరించినవి</span>
                    <span class="font-bold text-emerald-900 text-sm font-brand">118</span>
                  </div>
                  <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="text-[9px] text-slate-700 block">చదివించినవారు</span>
                    <span class="font-bold text-slate-900 text-sm font-brand">18</span>
                  </div>
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
              
              <div class="clean-card p-4 space-y-3">
                <div>
                  <h3 class="font-bold text-slate-900 text-sm">డిజిటల్ శగున్ QR & సౌండ్‌బాక్స్</h3>
                  <p class="text-xs text-slate-500">Google Pay, PhonePe ద్వారా నేరుగా బ్యాంక్ ఖాతాకు</p>
                </div>

                <div class="p-3 bg-slate-50 rounded-2xl border border-slate-200 inline-block">
                  <div class="w-40 h-40 bg-white rounded-xl p-2 flex flex-col items-center justify-center border border-slate-200 mx-auto">
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=upi://pay?pa=giftvault.treasury@icici%26pn=AnandWedding%26cu=INR" alt="QR" class="w-32 h-32">
                    <span class="text-[9px] font-semibold text-slate-500 mt-1">UPI: giftvault.treasury@icici</span>
                  </div>
                </div>

                <div class="p-3.5 rounded-xl bg-slate-900 text-white space-y-2 text-left">
                  <div class="flex items-center justify-between">
                    <span class="text-[10px] text-slate-400 font-semibold uppercase">స్మార్ట్ సౌండ్‌బాక్స్:</span>
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                  </div>
                  <p id="qr-soundbox-live" class="text-xs text-amber-200 font-medium">
                    "📢 ఫోన్‌పే ద్వారా శ్రీ యలమంచిలి రాజశేఖర్ గారి నుంచి ₹2,116 రూపాయలు ప్రాప్తించినవి!"
                  </p>
                  <button onclick="simulateUpiSoundbox()" class="w-full py-1.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 font-semibold text-xs flex items-center justify-center gap-1 btn-press">
                    <span>🔔</span>
                    <span>టెస్ట్ సౌండ్‌బాక్స్ వాయిస్ బీప్</span>
                  </button>
                </div>

              </div>

            </div>

          </div>

        </div>

        <!-- Native 5-Tab Bottom Dock (Android Feel) -->
        <div id="mobile-bottom-dock" class="h-14 bg-white border-t border-slate-200 grid grid-cols-5 items-center px-1 z-30 flex-shrink-0">
          <button onclick="switchAppTab('dashboard')" class="flex flex-col items-center py-1 text-slate-900 btn-press">
            <svg class="w-4 h-4 text-amber-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
            <span class="text-[9px] font-medium mt-0.5">హోమ్</span>
          </button>
          <button onclick="switchAppTab('desk')" class="flex flex-col items-center py-1 text-slate-400 hover:text-slate-900 btn-press">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
            <span class="text-[9px] font-medium mt-0.5">డెస్క్</span>
          </button>
          <button onclick="switchAppTab('ledger')" class="flex flex-col items-center py-1 text-slate-400 hover:text-slate-900 btn-press">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path></svg>
            <span class="text-[9px] font-medium mt-0.5">లెడ్జర్</span>
          </button>
          <button onclick="switchAppTab('expenses')" class="flex flex-col items-center py-1 text-slate-400 hover:text-slate-900 btn-press">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"></path><path d="M12 18V6"></path></svg>
            <span class="text-[9px] font-medium mt-0.5">ఖర్చులు</span>
          </button>
          <button onclick="switchAppTab('qr')" class="flex flex-col items-center py-1 text-slate-400 hover:text-slate-900 btn-press">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="18" height="18" x="3" y="3" rx="2"></rect><rect width="4" height="4" x="7" y="7"></rect></svg>
            <span class="text-[9px] font-medium mt-0.5">QR పే</span>
          </button>
        </div>

        <div id="mobile-gesture-bar" class="h-3.5 bg-white flex items-center justify-center flex-shrink-0">
          <div class="w-24 h-1 bg-slate-300 rounded-full"></div>
        </div>

      </div>
    </div>

  </main>

  <!-- ============================================================== -->
  <!-- 3. DYNAMIC EVENT CREATOR MODAL -->
  <!-- ============================================================== -->
  <div id="modal-new-event" class="fixed inset-0 bg-slate-950/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4 overflow-y-auto">
    <div class="bg-white rounded-2xl max-w-lg w-full p-5 space-y-3.5 my-8 shadow-xl border border-slate-200">
      
      <div class="flex items-center justify-between border-b border-slate-100 pb-2.5">
        <div>
          <h3 class="font-bold text-slate-900 text-sm">కొత్త శుభకార్యాన్ని జోడించండి</h3>
          <p class="text-[10px] text-slate-500">కేటగిరీ ఎంచుకోగానే వివరాల ఫారమ్ ఆటోమేటిక్ గా సర్దుబాటు అవుతుంది</p>
        </div>
        <button onclick="closeModalNewEvent()" class="text-slate-400 hover:text-slate-700 font-bold text-base btn-press">✕</button>
      </div>

      <!-- Category Suggestions -->
      <div>
        <label class="block text-[11px] font-medium text-slate-700 mb-1">త్వరిత కేటగిరీ:</label>
        <div class="flex flex-wrap gap-1">
          <button type="button" onclick="selectCategorySuggestion('wedding', 'వివాహ మహోత్సవం')" class="h-6 px-2.5 text-[10px] font-medium rounded-md bg-slate-100 text-slate-800 border border-slate-200 btn-press">💍 వివాహం</button>
          <button type="button" onclick="selectCategorySuggestion('halfsaree', 'శ్రీమతి లంగా ఓణీల శుభవేడుక')" class="h-6 px-2.5 text-[10px] font-medium rounded-md bg-slate-100 text-slate-800 border border-slate-200 btn-press">👗 లంగా ఓణీలు</button>
          <button type="button" onclick="selectCategorySuggestion('odugu', 'చిరంజీవి ఒడుగు / ఉపనయన మహోత్సవం')" class="h-6 px-2.5 text-[10px] font-medium rounded-md bg-slate-100 text-slate-800 border border-slate-200 btn-press">🪔 ఒడుగు</button>
          <button type="button" onclick="selectCategorySuggestion('panchala', 'పంచల శుభవేడుక (Dhoti Ceremony)')" class="h-6 px-2.5 text-[10px] font-medium rounded-md bg-slate-100 text-slate-800 border border-slate-200 btn-press">👔 పంచల వేడుక</button>
          <button type="button" onclick="selectCategorySuggestion('pushpavathi', 'పుష్పవతి / పుష్పాలంకరణ వేడుక')" class="h-6 px-2.5 text-[10px] font-medium rounded-md bg-slate-100 text-slate-800 border border-slate-200 btn-press">🌸 పుష్పవతి</button>
          <button type="button" onclick="selectCategorySuggestion('naming', 'నామకరణం & బారసాల మహోత్సవం')" class="h-6 px-2.5 text-[10px] font-medium rounded-md bg-slate-100 text-slate-800 border border-slate-200 btn-press">👶 బారసాల</button>
          <button type="button" onclick="selectCategorySuggestion('housewarming', 'నూతన గృహప్రవేశ మహోత్సవం')" class="h-6 px-2.5 text-[10px] font-medium rounded-md bg-slate-100 text-slate-800 border border-slate-200 btn-press">🏡 గృహప్రవేశం</button>
        </div>
      </div>

      <form id="form-new-event" onsubmit="handleCreateEvent(event)" class="space-y-3 text-xs">
        
        <div>
          <label class="block text-[11px] font-medium text-slate-700 mb-0.5">కేటగిరీ:</label>
          <select id="event-select-cat" onchange="onCategoryChanged(this.value)" class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none">
            <option value="wedding">వివాహం (Wedding - వధూవరులు)</option>
            <option value="halfsaree">లంగా ఓణీల వేడుక (Half Saree - అమ్మాయి మాత్రమే)</option>
            <option value="odugu">ఒడుగు / ఉపనయనం (Upanayanam - వటువు మాత్రమే)</option>
            <option value="panchala">పంచల వేడుక (Dhoti Ceremony - అబ్బాయి మాత్రమే)</option>
            <option value="pushpavathi">పుష్పవతి / పుష్పాలంకరణ</option>
            <option value="naming">బారసాల & నామకరణం</option>
            <option value="birthday">పుట్టినరోజు వేడుక</option>
            <option value="housewarming">గృహప్రవేశం</option>
          </select>
        </div>

        <div>
          <label class="block text-[11px] font-medium text-slate-700 mb-0.5">ఈవెంట్ శీర్షిక:</label>
          <input id="event-input-title" type="text" required placeholder="ఆనంద్ & శ్రేయ వివాహ మహోత్సవం" class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none">
        </div>

        <!-- DYNAMIC PARTICIPANT FIELDS -->
        <div id="dynamic-participant-fields" class="p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-2">
          <!-- Populated dynamically via JS onCategoryChanged -->
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div>
            <label class="block text-[11px] font-medium text-slate-700 mb-0.5">తేదీ:</label>
            <input id="event-input-date" type="date" required class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg">
          </div>
          <div>
            <label class="block text-[11px] font-medium text-slate-700 mb-0.5">వేదిక / హాల్:</label>
            <input id="event-input-venue" type="text" required placeholder="శ్రీ కన్వెన్షన్ హాల్" class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg">
          </div>
        </div>

        <!-- CITY AUTOCOMPLETE -->
        <div class="grid grid-cols-3 gap-2">
          <div class="relative col-span-1">
            <label class="block text-[11px] font-medium text-slate-700 mb-0.5">ఊరు / సిటీ:</label>
            <input id="event-input-city" type="text" required oninput="onEventCityInput(this.value)" placeholder="హైదరాబాద్..." class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg">
            <div id="event-city-suggestions" class="absolute left-0 right-0 top-full mt-1 bg-white border border-slate-200 rounded-lg shadow-lg z-30 hidden max-h-36 overflow-y-auto"></div>
          </div>
          <div>
            <label class="block text-[11px] font-medium text-slate-700 mb-0.5">రాష్ట్రం:</label>
            <input id="event-input-state" type="text" readonly value="తెలంగాణ" class="w-full h-8 px-2 text-xs bg-slate-100 border border-slate-200 rounded-lg text-slate-600">
          </div>
          <div>
            <label class="block text-[11px] font-medium text-slate-700 mb-0.5">పిన్‌కోడ్:</label>
            <input id="event-input-pincode" type="text" placeholder="500001" class="w-full h-8 px-2 text-xs bg-slate-50 border border-slate-200 rounded-lg">
          </div>
        </div>

        <div class="pt-2 flex justify-end gap-2">
          <button type="button" onclick="closeModalNewEvent()" class="px-3.5 py-1.5 rounded-lg border border-slate-200 text-slate-600 font-medium text-xs btn-press">రద్దు</button>
          <button type="submit" class="px-4 py-1.5 rounded-lg bg-slate-900 text-white font-medium text-xs shadow-xs btn-press">ఈవెంట్‌ను సృష్టించండి</button>
        </div>

      </form>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- 4. ADD EXPENSE MODAL -->
  <!-- ============================================================== -->
  <div id="modal-add-expense" class="fixed inset-0 bg-slate-950/60 backdrop-blur-xs z-50 hidden flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl max-w-sm w-full p-4 space-y-3 shadow-xl border border-slate-200">
      <div class="flex items-center justify-between border-b border-slate-100 pb-2">
        <h3 class="font-bold text-xs text-slate-900">ఈవెంట్ ఖర్చు నమోదు</h3>
        <button onclick="closeModalAddExpense()" class="text-slate-400 hover:text-slate-700 font-bold btn-press">✕</button>
      </div>

      <form id="form-add-expense" onsubmit="handleAddExpense(event)" class="space-y-2.5 text-xs">
        <div>
          <label class="block text-[11px] font-medium text-slate-700 mb-0.5">ఖర్చు వర్గం:</label>
          <select id="exp-category" class="w-full h-8 px-2 text-xs bg-slate-50 border border-slate-200 rounded-lg focus:outline-none">
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
          <label class="block text-[11px] font-medium text-slate-700 mb-0.5">ఎవరికి చెల్లించారు:</label>
          <input id="exp-paidto" type="text" required placeholder="శ్రీనివాస క్యాటరర్స్ అడ్వాన్స్" class="w-full h-8 px-2.5 text-xs bg-slate-50 border border-slate-200 rounded-lg">
        </div>

        <div>
          <label class="block text-[11px] font-medium text-slate-700 mb-0.5">మొత్తం (₹):</label>
          <input id="exp-amount" type="number" required placeholder="50000" class="w-full h-8 px-2.5 text-xs font-bold text-red-700 bg-red-50 border border-red-200 rounded-lg">
        </div>

        <div class="pt-2 flex justify-end gap-2">
          <button type="button" onclick="closeModalAddExpense()" class="px-3 py-1.5 rounded-lg border border-slate-200 text-slate-600 font-medium text-xs btn-press">రద్దు</button>
          <button type="submit" class="px-4 py-1.5 rounded-lg bg-red-700 text-white font-medium text-xs shadow-xs btn-press">ఖర్చు జోడించు</button>
        </div>
      </form>
    </div>
  </div>

  <!-- Audio Chime Generator for Soundbox -->
  <script>
    function playTempleChime() {
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(587.33, audioCtx.currentTime);
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
  <!-- 5. MASTER STATE ENGINE & SCRIPTS -->
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

        btnMob.className = "px-3 py-1.5 rounded-lg bg-slate-900 text-white shadow-xs transition-all flex items-center gap-1.5 btn-press";
        btnDesk.className = "px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition-all flex items-center gap-1.5 btn-press";
      } else {
        wrapper.className = "desktop-viewport";
        screen.className = "phone-screen";
        statusBar.classList.add('hidden');
        bottomDock.classList.add('hidden');
        gestureBar.classList.add('hidden');

        btnDesk.className = "px-3 py-1.5 rounded-lg bg-slate-900 text-white shadow-xs transition-all flex items-center gap-1.5 btn-press";
        btnMob.className = "px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition-all flex items-center gap-1.5 btn-press";
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
            btn.className = "px-3 py-1.5 rounded-lg bg-slate-900 text-white shrink-0 btn-press";
          } else {
            btn.className = "px-3 py-1.5 rounded-lg bg-white text-slate-700 hover:bg-slate-100 border border-slate-200 shrink-0 btn-press";
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
            b.className = "py-1 rounded-lg bg-slate-900 text-white btn-press";
          } else {
            b.className = "py-1 rounded-lg bg-slate-100 text-slate-700 border border-slate-200 btn-press";
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
          type === 'gold' ? 'బంగారు ఉంగరం / గొలుసు' : 
          type === 'silver' ? 'వెండి కుందులు / కలశం' : 'పట్టుచీర / వాషింగ్ మెషీన్';
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
      const message = `శ్రీ/శ్రీమతి ${entry.name} గారికి నమస్కారములు.\n\nమా "${state.activeEvent.title}" శుభకార్యానికి విచ్చేసి, ఆశీర్వదించి మీ అమూల్యమైన చదివింపులు (${giftText}) సమర్పించినందుకు మా కుటుంబ సభ్యుల తరపున హృదయపూర్వక ధన్యవాదాలు! 🙏\n\n- ${state.activeEvent.title} కుటుంబం`;
      
      const cleanPhone = (entry.phone || '').replace(/[^0-9]/g, '');
      const waUrl = cleanPhone.length >= 10 
        ? `https://api.whatsapp.com/send?phone=91${cleanPhone.slice(-10)}&text=${encodeURIComponent(message)}`
        : `https://api.whatsapp.com/send?text=${encodeURIComponent(message)}`;

      window.open(waUrl, '_blank');
    }

    function shareDigitalInvite() {
      const inviteMsg = `॥ శ్రీరస్తు శుభమస్తు ॥\n\nమా కుటుంబంలో జరగబోవు "${state.activeEvent.title}" కు తామెల్లరూ సకుటుంబ సపరివార సమేతంగా విచ్చేసి ఆశీర్వదించవలసిందిగా కోరుచున్నాము.\n\n📅 తేదీ: ${state.activeEvent.date}\n🏛️ వేదిక: ${state.activeEvent.venue}\n\nఆహ్వానించువారు:\nకుటుంబ సభ్యులు`;
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
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">వరుడి పేరు:</label>
              <input type="text" value="చి. ఆనంద్ వర్మ" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
            </div>
            <div>
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">వధువు పేరు:</label>
              <input type="text" value="చి.ల.సౌ. శ్రేయ" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
            </div>
          </div>
        `;
      } else if (cat === 'halfsaree' || cat === 'pushpavathi') {
        titleInput.value = cat === 'halfsaree' ? "చి.ల.సౌ. తేజస్విని లంగా ఓణీల శుభవేడుక" : "పుష్పాలంకరణ వేడుక";
        container.innerHTML = `
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">అమ్మాయి పేరు:</label>
              <input type="text" value="చి.ల.సౌ. తేజస్విని" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
            </div>
            <div>
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">తల్లిదండ్రుల పేర్లు:</label>
              <input type="text" placeholder="రాఘవరావు & ఉమాదేవి" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
            </div>
          </div>
        `;
      } else if (cat === 'odugu' || cat === 'panchala') {
        titleInput.value = cat === 'odugu' ? "చిరంజీవి సిద్ధార్థ ఒడుగు మహోత్సవం" : "పంచల వేడుక";
        container.innerHTML = `
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">వటువు / అబ్బాయి పేరు:</label>
              <input type="text" value="చి. సిద్ధార్థ శర్మ" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
            </div>
            <div>
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">తండ్రి పేరు:</label>
              <input type="text" placeholder="శ్రీనివాస్" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
            </div>
          </div>
        `;
      } else if (cat === 'housewarming') {
        titleInput.value = "శ్రీ లక్ష్మీ నిలయం నూతన గృహప్రవేశం";
        container.innerHTML = `
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">గృహ నామం:</label>
              <input type="text" value="శ్రీ లక్ష్మీ నిలయం" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
            </div>
            <div>
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">యజమానుల పేర్లు:</label>
              <input type="text" placeholder="సురేష్ & సుజాత దంపతులు" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
            </div>
          </div>
        `;
      } else {
        titleInput.value = "నామకరణం & బారసాల మహోత్సవం";
        container.innerHTML = `
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">శిశువు పేరు:</label>
              <input type="text" placeholder="బాబు / పాప" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
            </div>
            <div>
              <label class="block text-[11px] font-medium text-slate-700 mb-0.5">తల్లిదండ్రుల పేర్లు:</label>
              <input type="text" placeholder="సతీష్ & మాధవి" class="w-full h-8 px-2.5 text-xs bg-white border border-slate-200 rounded-lg">
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
        <div onclick="selectDeskCity('${c.name.split(' ')[0]}')" class="px-2.5 py-1.5 hover:bg-slate-100 cursor-pointer text-xs border-b border-slate-100 flex justify-between">
          <span class="font-medium text-slate-800">${c.name}</span>
          <span class="text-[10px] text-slate-400">${c.state}</span>
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
        <div onclick="selectEventCity('${c.name.split(' ')[0]}', '${c.state}', '${c.pin}')" class="px-2.5 py-1.5 hover:bg-slate-100 cursor-pointer text-xs border-b border-slate-100 flex justify-between">
          <span class="font-medium text-slate-800">${c.name}</span>
          <span class="text-[10px] text-slate-400">${c.pin}</span>
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
        btnTable.className = "px-3 py-1 rounded-md bg-slate-900 text-white shadow-2xs btn-press";
        btnBook.className = "px-3 py-1 rounded-md text-slate-600 hover:text-slate-900 btn-press";
      } else {
        tableDiv.classList.add('hidden');
        bookDiv.classList.remove('hidden');
        btnBook.className = "px-3 py-1 rounded-md bg-slate-900 text-white shadow-2xs btn-press";
        btnTable.className = "px-3 py-1 rounded-md text-slate-600 hover:text-slate-900 btn-press";
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
        <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-50 border border-slate-100">
          <div>
            <span class="font-semibold text-slate-900 block">${e.name}</span>
            <span class="text-[10px] text-slate-500">${e.city} • ${e.relation}</span>
          </div>
          <div class="text-right">
            <span class="font-bold text-emerald-700 text-xs font-brand">${e.amount ? '₹' + e.amount.toLocaleString('en-IN') : e.metalInfo}</span>
            <span class="text-[9px] text-slate-400 block">${e.time}</span>
          </div>
        </div>
      `).join('');

      // Table View
      document.getElementById('ledger-tbody-rows').innerHTML = state.entries.map((e, idx) => `
        <tr class="hover:bg-slate-50 transition-colors">
          <td class="p-2.5 font-medium text-slate-400 text-[10px]">${idx + 1}</td>
          <td class="p-2.5">
            <span class="font-semibold text-slate-900 block">${e.name}</span>
            <span class="text-[10px] text-slate-500">${e.city} • ${e.cover || ''}</span>
          </td>
          <td class="p-2.5">
            <span class="text-slate-700 block">${e.relation}</span>
            <span class="text-[9px] text-slate-500 bg-slate-100 px-1.5 py-0.2 rounded border border-slate-200 inline-block">${e.counter || 'కౌంటర్'}</span>
          </td>
          <td class="p-2.5 text-right">
            <span class="font-bold text-emerald-700 text-xs font-brand">${e.amount ? '₹' + e.amount.toLocaleString('en-IN') : e.metalInfo}</span>
          </td>
          <td class="p-2.5 text-center space-x-1">
            <button onclick='sendWhatsAppReceipt(${JSON.stringify(e)})' class="p-1 rounded bg-slate-100 hover:bg-emerald-50 text-slate-600 hover:text-emerald-700 border border-slate-200 btn-press">💬</button>
            <button onclick="deleteEntry('${e.id}')" class="p-1 rounded bg-slate-100 hover:bg-red-50 text-slate-600 hover:text-red-700 border border-slate-200 btn-press">🗑️</button>
          </td>
        </tr>
      `).join('');

      // Red Book Entries
      document.getElementById('ledger-book-entries').innerHTML = state.entries.map((e, idx) => `
        <div class="flex items-baseline justify-between border-b border-slate-100 pb-1.5 pt-0.5">
          <div class="flex items-baseline gap-2">
            <span class="font-bold text-slate-400 text-[10px]">${String(idx + 1).padStart(2, '0')}.</span>
            <div>
              <span class="font-semibold text-slate-900">${e.name}</span>
              <span class="text-[10px] text-slate-500">(${e.city} • ${e.relation})</span>
            </div>
          </div>
          <span class="font-bold text-emerald-700 font-brand">${e.amount ? '₹' + e.amount.toLocaleString('en-IN') : e.metalInfo}</span>
        </div>
      `).join('');
      document.getElementById('book-page-total').innerText = '₹' + totalCash.toLocaleString('en-IN');

      // Expenses
      document.getElementById('expenses-category-list').innerHTML = state.expenses.map(exp => `
        <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-50 border border-slate-100">
          <div>
            <span class="font-semibold text-slate-800 block">${exp.category}</span>
            <span class="text-[10px] text-slate-500">${exp.paidTo}</span>
          </div>
          <span class="font-bold text-red-700 font-brand text-xs">₹${exp.amount.toLocaleString('en-IN')}</span>
        </div>
      `).join('');

      // Reciprocity
      document.getElementById('reciprocity-list').innerHTML = state.reciprocity.map(r => `
        <div class="p-3 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-semibold text-slate-900">${r.name}</span>
            <span class="text-[9px] font-medium px-2 py-0.5 rounded bg-slate-200 text-slate-800">${r.status}</span>
          </div>
          <div class="flex items-center justify-between text-[11px] text-slate-600">
            <span>గతంలో మనం ఇచ్చింది: ₹${r.weGavePast}</span>
            <span class="font-bold text-emerald-700">నేడు వారు ఇచ్చింది: ₹${r.theyGaveToday}</span>
          </div>
        </div>
      `).join('');

      // Invites
      document.getElementById('invites-guest-list').innerHTML = state.guests.map(g => `
        <div class="flex items-center justify-between p-2.5 rounded-lg bg-slate-50 border border-slate-100">
          <div>
            <span class="font-semibold text-slate-900 block">${g.name}</span>
            <span class="text-[10px] text-slate-500">${g.city}</span>
          </div>
          <span class="px-2 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200 text-[10px] font-medium">${g.rsvp}</span>
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
        nav_home: "హోమ్",
        nav_app: "లెడ్జర్ ఓపెన్",
        btn_new_event: "కొత్త ఈవెంట్"
      },
      en: {
        nav_home: "Home",
        nav_app: "Open Ledger",
        btn_new_event: "New Event"
      },
      hi: {
        nav_home: "मुख्य पृष्ठ",
        nav_app: "लेज़र खोलें",
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
      alert("✅ Google తో లాగిన్ విజయవంతమైంది!");
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
        <tr class="hover:bg-slate-50 transition-colors">
          <td class="p-2.5 font-medium text-slate-400 text-[10px]">${idx + 1}</td>
          <td class="p-2.5">
            <span class="font-semibold text-slate-900 block">${e.name}</span>
            <span class="text-[10px] text-slate-500">${e.city} • ${e.cover || ''}</span>
          </td>
          <td class="p-2.5">
            <span class="text-slate-700 block">${e.relation}</span>
            <span class="text-[9px] text-slate-500 bg-slate-100 px-1.5 py-0.2 rounded border border-slate-200 inline-block">${e.counter || 'కౌంటర్'}</span>
          </td>
          <td class="p-2.5 text-right">
            <span class="font-bold text-emerald-700 text-xs font-brand">${e.amount ? '₹' + e.amount.toLocaleString('en-IN') : e.metalInfo}</span>
          </td>
          <td class="p-2.5 text-center space-x-1">
            <button onclick='sendWhatsAppReceipt(${JSON.stringify(e)})' class="p-1 rounded bg-slate-100 hover:bg-emerald-50 text-slate-600 hover:text-emerald-700 border border-slate-200 btn-press">💬</button>
            <button onclick="deleteEntry('${e.id}')" class="p-1 rounded bg-slate-100 hover:bg-red-50 text-slate-600 hover:text-red-700 border border-slate-200 btn-press">🗑️</button>
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

# Write to target files
with open(r"c:\Project\Gift Valut\web_preview\index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

with open(r"c:\Project\Gift Valut\web\index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

artifact_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"
with open(os.path.join(artifact_dir, "giftvault_interactive_preview.html"), "w", encoding="utf-8") as f:
    f.write(html_template)

print("SUCCESS: Clean, simple, minimalist redesign generated and synced!")
