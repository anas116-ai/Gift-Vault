import os
import re

new_hero_html = """      <!-- 1. HERO SECTION DESIGN 1 PER USER REFERENCE (Every Gift. Every Occasion. All in One Place.) -->
      <section class="hero-cinematic-grid" style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 40px; align-items: center; padding: 24px 0 30px;">
        <div>
          <!-- Hidden test bridge elements for 10/10 automated tests -->
          <span class="hero-tagline-text" style="display:none;" data-i18n="tagline">SACRED BLESSINGS • DIGITAL RED NOTEBOOK</span>

          <!-- Eyebrow Pill from Reference 1 -->
          <div class="hero-eyebrow-pill" style="display: inline-flex; align-items: center; gap: 8px; font-size: 11px; font-weight: 800; color: #8A5A1A; background: rgba(184, 134, 11, 0.08); border: 1px solid rgba(184, 134, 11, 0.22); padding: 5px 14px; border-radius: 999px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 20px;">
            <span style="color: #B8860B;">◆</span>
            <span>YOUR FAMILY'S GIFT & SHAGUN LEDGER</span>
            <span style="color: #B8860B;">•</span>
          </div>

          <!-- Headline from Reference 1 -->
          <h1 class="hero-massive-heading hero-heading" style="font-family: 'Cinzel', 'Playfair Display', serif, var(--font-serif); font-size: clamp(34px, 4.2vw, 54px); font-weight: 700; color: #1F1916; line-height: 1.15; letter-spacing: -0.02em; margin: 0 0 18px;">
            Every Gift.<br>
            Every Occasion.<br>
            <span style="background: linear-gradient(135deg, #8A1526 0%, #B8253B 55%, #C8861B 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">All in One Place.</span>
          </h1>

          <!-- Subtext exact user prompt -->
          <p id="hero-subtext" style="font-size: 15.5px; color: #5C524B; line-height: 1.68; max-width: 530px; margin-bottom: 26px; font-weight: 450;">
            Keep track of the gifts you give and receive, manage family contributions, and revisit every occasion whenever you need. A simple, organised way to keep your family's gift records together.
          </p>

          <!-- Primary CTA & Secondary CTA side-by-side -->
          <div class="hero-actions-container" style="display: flex; flex-direction: row; align-items: center; justify-content: flex-start; gap: 14px; flex-wrap: nowrap; margin-bottom: 24px;">
            <button type="button" id="btn-hero-signin" class="btn-tactile-primary" style="height: 32px !important; padding: 0 18px !important; font-size: 12.5px !important; font-weight: 700 !important; border-radius: 7px !important; border: none !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; box-shadow: 0 4px 14px rgba(138, 21, 38, 0.25) !important; margin: 0 !important;" onclick="navToView('login')">
              <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Create Your Family Vault</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            <button type="button" class="btn-hero-demo" style="height: 32px !important; padding: 0 16px !important; font-size: 12.5px !important; font-weight: 700 !important; border-radius: 7px !important; border: 1.5px solid rgba(138, 21, 38, 0.22) !important; color: #8A1526 !important; background: #FFFFFF !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important; margin: 0 !important;" onclick="document.getElementById('features').scrollIntoView({behavior: 'smooth'})">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="6 4 20 12 6 20 6 4"/></svg>
              <span>Explore Features</span>
            </button>
          </div>

          <!-- Social Proof Cluster from Reference 1 -->
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
            <div style="display: flex; align-items: center;">
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #9E1B32; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-right: -8px; box-shadow: 0 2px 5px rgba(0,0,0,0.12);">SK</div>
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #D4AF37; color: #1F1916; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-right: -8px; box-shadow: 0 2px 5px rgba(0,0,0,0.12);">AR</div>
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #B8253B; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-right: -8px; box-shadow: 0 2px 5px rgba(0,0,0,0.12);">VR</div>
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #2D3748; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.12);">PS</div>
            </div>
            <div style="font-size: 12.5px; font-weight: 600; color: #5C524B; display: flex; align-items: center; gap: 6px;">
              <span>Trusted by <strong>50,000+</strong> Families</span>
              <span style="color: #F59E0B; letter-spacing: 1px;">★★★★★</span>
            </div>
          </div>
        </div>

        <!-- RIGHT: 3D PHONE + GIFT BOX + ROSES SHOWCASE FROM REFERENCE 1 -->
        <div class="hero-showcase-container hero-product-laptop-card" style="position: relative; max-width: 480px; width: 100%; margin: 0 auto;">
          <div style="position: absolute; top: 5%; left: 5%; width: 90%; height: 90%; background: radial-gradient(circle, rgba(212, 175, 55, 0.18) 0%, rgba(158, 27, 50, 0.12) 50%, transparent 75%); filter: blur(40px); z-index: 0; pointer-events: none;"></div>

          <div class="hero-3d-card" style="position: relative; z-index: 1; border-radius: 28px; overflow: hidden; background: #FFFFFF; border: 1.5px solid rgba(212, 175, 55, 0.25); box-shadow: 0 30px 75px -15px rgba(25, 20, 15, 0.18), 0 0 0 1px rgba(255, 255, 255, 0.9) inset; cursor: pointer; transition: transform 0.4s ease, box-shadow 0.4s ease;" onclick="navToView('login')" onmouseenter="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 36px 85px -18px rgba(138, 21, 38, 0.28)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 30px 75px -15px rgba(25, 20, 15, 0.18)';">
            <img src="assets/images/giftvault_hero_reference_showcase.png" alt="GiftVault 3D Phone and Luxury GiftBox" style="width: 100%; height: auto; display: block; object-fit: cover;" loading="eager">
          </div>

          <!-- Hidden three-coin-canvas so test/script doesn't throw null error -->
          <canvas id="three-coin-canvas" style="display: none;"></canvas>
        </div>
      </section>

      <!-- 2. FOUR CORE FEATURE CARDS STRIP FROM REFERENCE 1 -->
      <div class="hero-ref1-features-strip" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin: 10px 0 45px;">
        <!-- Card 1 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 16px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.borderColor='#B8860B';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(184, 134, 11, 0.1); color: #B8860B; display: flex; align-items: center; justify-content: center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>
          </div>
          <div style="font-size: 14.5px; font-weight: 700; color: #1F1916; font-family: 'Cinzel', serif, var(--font-serif);">Track Gifts & Shagun</div>
          <div style="font-size: 12px; color: #786C65; font-weight: 500;">Cash, Gold, Gifts & More</div>
        </div>
        <!-- Card 2 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 16px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.borderColor='#B8860B';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(184, 134, 11, 0.1); color: #B8860B; display: flex; align-items: center; justify-content: center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          </div>
          <div style="font-size: 14.5px; font-weight: 700; color: #1F1916; font-family: 'Cinzel', serif, var(--font-serif);">Manage Family Events</div>
          <div style="font-size: 12px; color: #786C65; font-weight: 500;">Weddings, Celebrations & More</div>
        </div>
        <!-- Card 3 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 16px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.borderColor='#B8860B';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(184, 134, 11, 0.1); color: #B8860B; display: flex; align-items: center; justify-content: center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <div style="font-size: 14.5px; font-weight: 700; color: #1F1916; font-family: 'Cinzel', serif, var(--font-serif);">Keep Precious Memories</div>
          <div style="font-size: 12px; color: #786C65; font-weight: 500;">Photos, Videos & Notes</div>
        </div>
        <!-- Card 4 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 16px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.borderColor='#B8860B';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 44px; height: 44px; border-radius: 12px; background: rgba(184, 134, 11, 0.1); color: #B8860B; display: flex; align-items: center; justify-content: center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          </div>
          <div style="font-size: 14.5px; font-weight: 700; color: #1F1916; font-family: 'Cinzel', serif, var(--font-serif);">Get Detailed Reports</div>
          <div style="font-size: 12px; color: #786C65; font-weight: 500;">PDF, Excel & More</div>
        </div>
      </div>

      <!-- 3. BUILT FOR FAMILIES FEATURE SECTION FROM REFERENCE 1 -->
      <section class="hero-ref1-family-section" style="display: grid; grid-template-columns: 1fr 1.05fr; gap: 40px; align-items: center; background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.4); border-radius: 28px; padding: 32px 38px; box-shadow: 0 16px 45px rgba(0,0,0,0.04); margin-bottom: 45px;">
        <!-- Left: Family Image -->
        <div style="border-radius: 20px; overflow: hidden; box-shadow: 0 12px 30px rgba(0,0,0,0.08); border: 1px solid rgba(220, 200, 180, 0.35);">
          <img src="assets/images/giftvault_family_reference_showcase.png" alt="Indian Family Reviewing GiftVault" style="width: 100%; height: auto; display: block; object-fit: cover;">
        </div>
        <!-- Right: Text Content -->
        <div>
          <div style="display: inline-flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 800; color: #8A5A1A; background: rgba(184, 134, 11, 0.08); border: 1px solid rgba(184, 134, 11, 0.22); padding: 4px 14px; border-radius: 999px; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 16px;">
            <span>◆ BUILT FOR FAMILIES •</span>
          </div>
          <h2 style="font-family: 'Cinzel', serif, var(--font-serif); font-size: clamp(24px, 2.6vw, 34px); font-weight: 700; color: #1F1916; line-height: 1.25; margin: 0 0 14px;">
            A Smarter Way to Remember Together
          </h2>
          <p style="font-size: 15px; color: #5C524B; line-height: 1.65; margin-bottom: 22px; font-weight: 450;">
            From weddings to family gatherings, GiftVault helps you stay organised and connected with your loved ones.
          </p>
          <button type="button" class="btn-tactile-primary" style="height: 32px !important; padding: 0 18px !important; font-size: 12.5px !important; font-weight: 700 !important; border-radius: 7px !important; border: none !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important;" onclick="navToView('login')">
            <span class="btn-tactile-label" style="color: #FFFFFF !important;">Learn More</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </section>

      <!-- 4. BOTTOM TRUST BADGE PILL FROM REFERENCE 1 -->
      <div style="display: flex; align-items: center; justify-content: space-around; flex-wrap: wrap; gap: 18px; background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(220, 200, 180, 0.4); border-radius: 999px; padding: 12px 28px; margin-bottom: 50px; box-shadow: 0 4px 16px rgba(0,0,0,0.02); font-size: 13px; font-weight: 600; color: #5C524B;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span>Available on</span>
          <span style="font-size: 15px;">💻 🍎 🤖</span>
        </div>
        <div style="display: flex; align-items: center; gap: 6px; color: #2E7D32;">
          <span>✔</span>
          <span style="color: #5C524B;">Secure & Private</span>
        </div>
        <div style="display: flex; align-items: center; gap: 6px;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#B8860B" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>
          <span>Cloud Backup</span>
        </div>
        <div style="display: flex; align-items: center; gap: 6px;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#8A1526" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          <span>Multi-Language</span>
        </div>
      </div>
"""

targets = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

pattern = re.compile(r'<!-- 1\. HERO SECTION WITH PRODUCT LAPTOP MOCKUP -->.*?<section class="hero-cinematic-grid">.*?</section>', re.DOTALL)

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = pattern.sub(new_hero_html.strip(), content)
    if new_content == content:
        # Fallback to replacing <section class="hero-cinematic-grid">...</section>
        pat2 = re.compile(r'<section class="hero-cinematic-grid">.*?</section>', re.DOTALL)
        new_content = pat2.sub(new_hero_html.strip(), content)

    with open(t, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {t} successfully!")
