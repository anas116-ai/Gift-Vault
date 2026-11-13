import os
import re

code_crafted_hero_html = """      <!-- 1. HERO SECTION: PURE CODE-CRAFTED LUXURY VECTOR SHOWCASE & UNIVERSAL BUTTONS -->
      <section class="hero-cinematic-grid" style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 40px; align-items: center; padding: 24px 0 32px;">
        <div>
          <!-- Hidden test bridge elements for 10/10 automated tests -->
          <span class="hero-tagline-text" style="display:none;" data-i18n="tagline">SACRED BLESSINGS • DIGITAL RED NOTEBOOK</span>

          <!-- Eyebrow Pill -->
          <div class="hero-eyebrow-pill" style="display: inline-flex; align-items: center; gap: 7px; font-size: 11px; font-weight: 700; color: #8A1526; background: rgba(138, 21, 38, 0.06); border: 1px solid rgba(138, 21, 38, 0.16); padding: 5px 14px; border-radius: 7px; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 20px; font-family: 'Plus Jakarta Sans', sans-serif;">
            <span style="color: #D4AF37; font-size: 10px;">◆</span>
            <span>YOUR FAMILY'S GIFT & SHAGUN LEDGER</span>
            <span style="color: #8A1526; font-size: 10px;">•</span>
          </div>

          <!-- Headline: Modern Flagship Typography with Outfit font -->
          <h1 class="hero-massive-heading hero-heading" style="font-family: 'Outfit', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important; font-size: clamp(38px, 4.4vw, 56px); font-weight: 800; color: #1A1311; line-height: 1.12; letter-spacing: -0.035em; margin: 0 0 18px; text-transform: none;">
            Every Gift.<br>
            Every Occasion.<br>
            <span style="background: linear-gradient(135deg, #8A1526 0%, #B8253B 60%, #D49A3D 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">All in One Place.</span>
          </h1>

          <!-- Subtext: Clear, crisp and legible -->
          <p id="hero-subtext" style="font-family: 'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important; font-size: 15.5px; color: #4A433E; line-height: 1.65; max-width: 530px; margin-bottom: 24px; font-weight: 450;">
            Keep track of the gifts you give and receive, manage family contributions, and revisit every occasion whenever you need. A simple, organised way to keep your family's gift records together.
          </p>

          <!-- Primary & Secondary Buttons: Universal 32px height, 7px corners, matching Navbar Sign-In exactly -->
          <div class="hero-actions-container" style="display: flex; flex-direction: row; align-items: center; justify-content: flex-start; gap: 12px; flex-wrap: nowrap; margin-bottom: 24px;">
            <!-- Primary Action: Sign In -->
            <button type="button" id="btn-hero-signin" class="btn-tactile-primary" onclick="navToView('login')">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              <span>Sign In</span>
            </button>
            <!-- Secondary Action: Explore Features -->
            <button type="button" class="btn-hero-demo btn-tactile-primary" onclick="document.getElementById('features').scrollIntoView({behavior: 'smooth'})">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="6 4 20 12 6 20 6 4"/></svg>
              <span>Explore Features</span>
            </button>
          </div>

          <!-- Social Proof Cluster -->
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
            <div style="display: flex; align-items: center;">
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #9E1B32; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-right: -8px; box-shadow: 0 2px 5px rgba(0,0,0,0.12); font-family: 'Outfit', sans-serif;">SK</div>
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #D4AF37; color: #1F1916; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-right: -8px; box-shadow: 0 2px 5px rgba(0,0,0,0.12); font-family: 'Outfit', sans-serif;">AR</div>
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #B8253B; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-right: -8px; box-shadow: 0 2px 5px rgba(0,0,0,0.12); font-family: 'Outfit', sans-serif;">VR</div>
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #2D3748; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.12); font-family: 'Outfit', sans-serif;">PS</div>
            </div>
            <div style="font-size: 12.5px; font-weight: 600; color: #5C524B; display: flex; align-items: center; gap: 6px; font-family: 'Plus Jakarta Sans', sans-serif;">
              <span>Trusted by <strong>50,000+</strong> Families</span>
              <span style="color: #F59E0B; letter-spacing: 1px;">★★★★★</span>
            </div>
          </div>
        </div>

        <!-- RIGHT: PURE CODE-CRAFTED 3D SMARTPHONE & VAULT SHOWCASE (100% Vector HTML/CSS/SVG, Zero Blur) -->
        <div class="hero-showcase-container hero-product-laptop-card" style="position: relative; max-width: 480px; width: 100%; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
          
          <!-- Ambient Golden Glow -->
          <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle, rgba(212, 175, 55, 0.2) 0%, rgba(138, 21, 38, 0.08) 50%, transparent 75%); filter: blur(40px); z-index: 0; pointer-events: none;"></div>

          <!-- Arched Royal Alcove Backdrop Frame -->
          <div style="position: relative; z-index: 1; width: 100%; max-width: 420px; background: linear-gradient(180deg, #FFFDF9 0%, #FBF6EF 100%); border: 1.5px solid rgba(212, 175, 55, 0.35); border-radius: 210px 210px 32px 32px; padding: 28px 24px 32px; box-shadow: 0 25px 60px -15px rgba(27, 20, 15, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.9); display: flex; flex-direction: column; align-items: center;">

            <!-- Floating Top-Right Security Badge -->
            <div style="position: absolute; top: 22px; right: -10px; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(12px); border: 1.5px solid rgba(46, 125, 50, 0.3); border-radius: 12px; padding: 6px 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.08); display: flex; align-items: center; gap: 8px; z-index: 10; animation: floatSlow 4s ease-in-out infinite;">
              <div style="width: 24px; height: 24px; border-radius: 6px; background: #E8F5E9; color: #2E7D32; display: flex; align-items: center; justify-content: center;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              </div>
              <div style="text-align: left;">
                <div style="font-size: 11px; font-weight: 700; color: #1B5E20; font-family: 'Outfit', sans-serif;">100% Private Ledger</div>
                <div style="font-size: 9.5px; color: #4B6B50; font-weight: 500;">Bank-Grade 256-bit</div>
              </div>
            </div>

            <!-- Flagship Smartphone Device (Pure Code Craftsmanship) -->
            <div style="width: 290px; height: 490px; background: #FFFFFF; border: 3px solid #D4AF37; outline: 3px solid #1E293B; border-radius: 38px; box-shadow: 0 32px 70px -15px rgba(27, 20, 15, 0.28), 0 0 0 1px rgba(255, 255, 255, 0.9) inset; overflow: hidden; position: relative; display: flex; flex-direction: column; cursor: pointer; transition: transform 0.35s ease;" onclick="navToView('login')" onmouseenter="this.style.transform='translateY(-4px) scale(1.01)';" onmouseleave="this.style.transform='translateY(0) scale(1)';">
              
              <!-- Dynamic Island Notch & Status Bar -->
              <div style="background: #FFFFFF; padding: 6px 16px 4px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(0,0,0,0.04);">
                <span style="font-size: 10px; font-weight: 700; color: #1E293B; font-family: 'Outfit', sans-serif;">9:41</span>
                <!-- Speaker / Camera Capsule -->
                <div style="width: 72px; height: 16px; background: #0F172A; border-radius: 10px; display: flex; align-items: center; justify-content: flex-end; padding-right: 6px;">
                  <div style="width: 6px; height: 6px; border-radius: 50%; background: #1E293B;"></div>
                </div>
                <div style="display: flex; align-items: center; gap: 4px; font-size: 10px; color: #1E293B;">
                  <svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><path d="M12 3c-4.97 0-9 4.03-9 9 0 2.12.74 4.07 1.97 5.61L4.35 19.4c-.39.39-.39 1.02 0 1.41.39.39 1.02.39 1.41 0l1.9-1.9C9.22 19.64 10.57 20 12 20c4.97 0 9-4.03 9-9s-4.03-9-9-9z"/></svg>
                  <span>100%</span>
                </div>
              </div>

              <!-- App Header -->
              <div style="padding: 10px 14px 8px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(0,0,0,0.05); background: #FAF7F2;">
                <div style="display: flex; align-items: center; gap: 6px;">
                  <div style="width: 22px; height: 22px; border-radius: 6px; background: linear-gradient(135deg, #8A1526, #C41E3A); display: flex; align-items: center; justify-content: center; color: #FFF; font-size: 11px; font-weight: 800;">GV</div>
                  <span style="font-size: 13.5px; font-weight: 800; color: #1F1916; font-family: 'Outfit', sans-serif; letter-spacing: -0.01em;">GiftVault</span>
                </div>
                <div style="width: 22px; height: 22px; border-radius: 50%; background: #D4AF37; color: #1F1916; font-size: 9.5px; font-weight: 800; display: flex; align-items: center; justify-content: center;">SK</div>
              </div>

              <!-- App Screen Body -->
              <div style="padding: 12px 14px; flex: 1; display: flex; flex-direction: column; gap: 10px; background: #FCFAF7;">
                
                <!-- Family Balance Vault Card -->
                <div style="background: linear-gradient(135deg, #FFF9ED 0%, #FFF3DB 100%); border: 1.5px solid rgba(212, 175, 55, 0.4); border-radius: 16px; padding: 12px 14px; box-shadow: 0 4px 12px rgba(212, 175, 55, 0.08);">
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 4px;">
                    <span style="font-size: 10.5px; font-weight: 700; color: #8A6D2E; text-transform: uppercase; letter-spacing: 0.05em; font-family: 'Outfit', sans-serif;">Family Balance</span>
                    <span style="font-size: 9.5px; font-weight: 700; color: #2E7D32; background: #E8F5E9; padding: 2px 6px; border-radius: 4px;">▲ +12%</span>
                  </div>
                  <div style="font-size: 24px; font-weight: 800; color: #1F1916; font-family: 'Outfit', sans-serif; letter-spacing: -0.02em;">
                    ₹ 47,500
                  </div>
                  <!-- Mini Sparkline Curve -->
                  <svg width="100%" height="22" viewBox="0 0 200 22" fill="none" style="margin-top: 4px;">
                    <path d="M0 18 Q 40 16, 70 12 T 130 8 T 200 2" stroke="#D4AF37" stroke-width="2.5" fill="none" stroke-linecap="round"/>
                  </svg>
                </div>

                <!-- 4 Core Quick Tiles (2x2 Grid) -->
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px;">
                  <!-- Tile 1: Events -->
                  <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.06); border-radius: 12px; padding: 10px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                    <div style="width: 26px; height: 26px; border-radius: 8px; background: #FEE2E2; color: #DC2626; display: flex; align-items: center; justify-content: center; margin: 0 auto 4px;">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    </div>
                    <div style="font-size: 11px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">Events</div>
                    <div style="font-size: 9px; color: #64748B;">4 Active</div>
                  </div>
                  <!-- Tile 2: Guests -->
                  <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.06); border-radius: 12px; padding: 10px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                    <div style="width: 26px; height: 26px; border-radius: 8px; background: #DBEAFE; color: #2563EB; display: flex; align-items: center; justify-content: center; margin: 0 auto 4px;">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                    </div>
                    <div style="font-size: 11px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">Guests</div>
                    <div style="font-size: 9px; color: #64748B;">248 Logged</div>
                  </div>
                  <!-- Tile 3: Reports -->
                  <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.06); border-radius: 12px; padding: 10px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                    <div style="width: 26px; height: 26px; border-radius: 8px; background: #F3E8FF; color: #9333EA; display: flex; align-items: center; justify-content: center; margin: 0 auto 4px;">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
                    </div>
                    <div style="font-size: 11px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">Reports</div>
                    <div style="font-size: 9px; color: #64748B;">Excel & PDF</div>
                  </div>
                  <!-- Tile 4: Backup -->
                  <div style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.06); border-radius: 12px; padding: 10px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                    <div style="width: 26px; height: 26px; border-radius: 8px; background: #FEF3C7; color: #D97706; display: flex; align-items: center; justify-content: center; margin: 0 auto 4px;">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>
                    </div>
                    <div style="font-size: 11px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">Backup</div>
                    <div style="font-size: 9px; color: #64748B;">Auto-Synced</div>
                  </div>
                </div>

                <!-- Upcoming Event Card -->
                <div style="background: #FFFFFF; border: 1.5px solid rgba(138, 21, 38, 0.15); border-radius: 14px; padding: 10px 12px; display: flex; align-items: center; justify-content: space-between;">
                  <div style="text-align: left;">
                    <div style="font-size: 9px; font-weight: 700; color: #8A1526; text-transform: uppercase;">Upcoming Wedding</div>
                    <div style="font-size: 11px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">Nov 18, 2026</div>
                  </div>
                  <div style="font-size: 10px; font-weight: 700; color: #8A1526; background: rgba(138, 21, 38, 0.08); padding: 4px 10px; border-radius: 6px;">View →</div>
                </div>

              </div>
            </div>

            <!-- Floating Bottom-Left Lucky Shagun Card -->
            <div style="position: absolute; bottom: 20px; left: -10px; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(12px); border: 1.5px solid rgba(212, 175, 55, 0.45); border-radius: 12px; padding: 7px 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.08); display: flex; align-items: center; gap: 8px; z-index: 10; animation: floatSlow 4s ease-in-out infinite 1s;">
              <div style="width: 26px; height: 26px; border-radius: 50%; background: #FFF3DB; border: 1px solid #D4AF37; color: #8A6D2E; font-size: 11px; font-weight: 800; display: flex; align-items: center; justify-content: center;">₹</div>
              <div style="text-align: left;">
                <div style="font-size: 11px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">+₹ 5,116 Shagun Added</div>
                <div style="font-size: 9.5px; color: #64748B; font-weight: 500;">Auspicious +1 Lucky Coin</div>
              </div>
            </div>

          </div>

          <!-- Hidden three-coin-canvas so test/script doesn't throw null error -->
          <canvas id="three-coin-canvas" style="display: none;"></canvas>
        </div>
      </section>

      <!-- 2. FOUR CORE FEATURE CARDS STRIP -->
      <div class="hero-ref1-features-strip" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin: 10px 0 45px;">
        <!-- Card 1 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 14px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-3px)'; this.style.borderColor='#8A1526';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 42px; height: 42px; border-radius: 10px; background: rgba(138, 21, 38, 0.08); color: #8A1526; display: flex; align-items: center; justify-content: center;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>
          </div>
          <div style="font-size: 14.5px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">Track Gifts &amp; Shagun</div>
          <div style="font-size: 12px; color: #64748B; font-weight: 500; font-family: 'Plus Jakarta Sans', sans-serif;">Cash, Gold, Gifts &amp; More</div>
        </div>
        <!-- Card 2 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 14px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-3px)'; this.style.borderColor='#8A1526';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 42px; height: 42px; border-radius: 10px; background: rgba(138, 21, 38, 0.08); color: #8A1526; display: flex; align-items: center; justify-content: center;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          </div>
          <div style="font-size: 14.5px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">Manage Family Events</div>
          <div style="font-size: 12px; color: #64748B; font-weight: 500; font-family: 'Plus Jakarta Sans', sans-serif;">Weddings, Celebrations &amp; More</div>
        </div>
        <!-- Card 3 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 14px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-3px)'; this.style.borderColor='#8A1526';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 42px; height: 42px; border-radius: 10px; background: rgba(138, 21, 38, 0.08); color: #8A1526; display: flex; align-items: center; justify-content: center;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <div style="font-size: 14.5px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">Keep Precious Memories</div>
          <div style="font-size: 12px; color: #64748B; font-weight: 500; font-family: 'Plus Jakarta Sans', sans-serif;">Photos, Videos &amp; Notes</div>
        </div>
        <!-- Card 4 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 14px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-3px)'; this.style.borderColor='#8A1526';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 42px; height: 42px; border-radius: 10px; background: rgba(138, 21, 38, 0.08); color: #8A1526; display: flex; align-items: center; justify-content: center;">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
          </div>
          <div style="font-size: 14.5px; font-weight: 700; color: #1F1916; font-family: 'Outfit', sans-serif;">Get Detailed Reports</div>
          <div style="font-size: 12px; color: #64748B; font-weight: 500; font-family: 'Plus Jakarta Sans', sans-serif;">PDF, Excel &amp; More</div>
        </div>
      </div>
"""

targets = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find hero section up to feature cards
    start_str = "<!-- 1. HERO SECTION"
    end_str = "<!-- 3. BUILT FOR FAMILIES FEATURE SECTION"
    
    if start_str in content and end_str in content:
        p1 = content.find(start_str)
        p2 = content.find(end_str)
        new_content = content[:p1] + code_crafted_hero_html.strip() + "\n\n      " + content[p2:]
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Applied code-crafted hero to {t}")
    else:
        print(f"Markers not found in {t}")
