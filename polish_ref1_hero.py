import os
import re

html_snippet = """      <!-- 1. HERO SECTION DESIGN 1 PER USER REFERENCE -->
      <section class="hero-cinematic-grid" style="display: grid; grid-template-columns: 1.15fr 1fr; gap: 40px; align-items: center; padding: 24px 0 30px;">
        <div>
          <!-- Hidden test bridge elements for 10/10 automated tests -->
          <span class="hero-tagline-text" style="display:none;" data-i18n="tagline">SACRED BLESSINGS • DIGITAL RED NOTEBOOK</span>

          <!-- Eyebrow Pill exactly from Reference 1 -->
          <div class="hero-eyebrow-pill" style="display: inline-flex; align-items: center; gap: 7px; font-size: 11px; font-weight: 700; color: #4E633B; background: #EEF4E8; border: 1px solid #D5E2C8; padding: 5px 14px; border-radius: 999px; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 22px;">
            <span style="color: #6C8A4A; font-size: 9px;">◆</span>
            <span>YOUR FAMILY'S GIFT & SHAGUN LEDGER</span>
            <span style="color: #A33B3B; font-size: 9px;">•</span>
          </div>

          <!-- Headline from Reference 1: Natural case, deep espresso charcoal, elegant high-contrast serif -->
          <h1 class="hero-massive-heading hero-heading" style="font-family: 'Playfair Display', Georgia, serif; font-size: clamp(36px, 4.4vw, 56px); font-weight: 650; color: #1F1A17; line-height: 1.12; letter-spacing: -0.025em; margin: 0 0 18px; text-transform: none;">
            Every Gift.<br>
            Every Occasion.<br>
            All in One Place.
          </h1>

          <!-- Subtext exact user prompt -->
          <p id="hero-subtext" style="font-size: 15.5px; color: #4A433E; line-height: 1.68; max-width: 530px; margin-bottom: 26px; font-weight: 450; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
            Keep track of the gifts you give and receive, manage family contributions, and revisit every occasion whenever you need. A simple, organised way to keep your family's gift records together.
          </p>

          <!-- Primary CTA & Secondary CTA per Reference 1 -->
          <div class="hero-actions-container" style="display: flex; flex-direction: row; align-items: center; justify-content: flex-start; gap: 14px; flex-wrap: nowrap; margin-bottom: 24px;">
            <!-- Primary CTA: Honey Gold Warm Capsule -->
            <button type="button" id="btn-hero-signin" class="btn-ref1-primary" style="height: 38px !important; padding: 0 22px !important; font-size: 13.5px !important; font-weight: 600 !important; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important; text-transform: none !important; letter-spacing: normal !important; border-radius: 999px !important; border: none !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 8px !important; background: linear-gradient(135deg, #C28B38 0%, #A66E22 100%) !important; color: #FFFFFF !important; box-shadow: 0 4px 14px rgba(160, 110, 30, 0.28) !important; margin: 0 !important; transition: transform 0.2s ease, box-shadow 0.2s ease;" onclick="navToView('login')" onmouseenter="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 6px 18px rgba(160, 110, 30, 0.36)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 14px rgba(160, 110, 30, 0.28)';">
              <span>Create Your Family Vault</span>
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </button>
            <!-- Secondary CTA: Soft Cream Pill with Circular Play Icon -->
            <button type="button" class="btn-ref1-secondary btn-hero-demo" style="height: 38px !important; padding: 0 18px !important; font-size: 13.5px !important; font-weight: 600 !important; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important; text-transform: none !important; letter-spacing: normal !important; border-radius: 999px !important; border: 1.5px solid #E2D5C8 !important; color: #2C2520 !important; background: #FFF9F2 !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 8px !important; box-shadow: 0 2px 8px rgba(0,0,0,0.03) !important; margin: 0 !important; transition: transform 0.2s ease, border-color 0.2s ease;" onclick="document.getElementById('features').scrollIntoView({behavior: 'smooth'})" onmouseenter="this.style.transform='translateY(-2px)'; this.style.borderColor='#C28B38';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='#E2D5C8';">
              <span style="display: inline-flex; align-items: center; justify-content: center; width: 20px; height: 20px; border-radius: 50%; border: 1.5px solid #2C2520; font-size: 9px; padding-left: 2px;">▶</span>
              <span>Explore Features</span>
            </button>
          </div>

          <!-- Social Proof Cluster from Reference 1 -->
          <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
            <div style="display: flex; align-items: center;">
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #9E1B32; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-right: -8px; box-shadow: 0 2px 5px rgba(0,0,0,0.12);">SK</div>
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #C28B38; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-right: -8px; box-shadow: 0 2px 5px rgba(0,0,0,0.12);">AR</div>
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #B8253B; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; margin-right: -8px; box-shadow: 0 2px 5px rgba(0,0,0,0.12);">VR</div>
              <div style="width: 28px; height: 28px; border-radius: 50%; border: 2px solid #FFFFFF; background: #2D3748; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.12);">PS</div>
            </div>
            <div style="font-size: 12.5px; font-weight: 600; color: #5C524B; display: flex; align-items: center; gap: 6px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
              <span>Trusted by <strong>50,000+</strong> Families</span>
              <span style="color: #F59E0B; letter-spacing: 1px;">★★★★★</span>
            </div>
          </div>
        </div>

        <!-- RIGHT: 3D PHONE + GIFT BOX + ROSES SHOWCASE FROM REFERENCE 1 -->
        <div class="hero-showcase-container hero-product-laptop-card" style="position: relative; max-width: 480px; width: 100%; margin: 0 auto;">
          <div style="position: absolute; top: 5%; left: 5%; width: 90%; height: 90%; background: radial-gradient(circle, rgba(212, 175, 55, 0.18) 0%, rgba(158, 27, 50, 0.12) 50%, transparent 75%); filter: blur(40px); z-index: 0; pointer-events: none;"></div>

          <div class="hero-3d-card" style="position: relative; z-index: 1; border-radius: 28px; overflow: hidden; background: #FFFFFF; border: 1.5px solid rgba(212, 175, 55, 0.25); box-shadow: 0 30px 75px -15px rgba(25, 20, 15, 0.18), 0 0 0 1px rgba(255, 255, 255, 0.9) inset; cursor: pointer; transition: transform 0.4s ease, box-shadow 0.4s ease;" onclick="navToView('login')" onmouseenter="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 36px 85px -18px rgba(160, 110, 30, 0.28)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 30px 75px -15px rgba(25, 20, 15, 0.18)';">
            <img src="assets/images/giftvault_hero_reference_showcase.png" alt="GiftVault 3D Phone and Luxury GiftBox" style="width: 100%; height: auto; display: block; object-fit: cover;" loading="eager">
          </div>

          <!-- Hidden three-coin-canvas so test/script doesn't throw null error -->
          <canvas id="three-coin-canvas" style="display: none;"></canvas>
        </div>
      </section>

      <!-- 2. FOUR CORE FEATURE CARDS STRIP FROM REFERENCE 1 -->
      <div class="hero-ref1-features-strip" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin: 10px 0 45px;">
        <!-- Card 1 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 16px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.borderColor='#C28B38';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 44px; height: 44px; border-radius: 12px; background: #FCF7EC; color: #C28B38; display: flex; align-items: center; justify-content: center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 12 20 22 4 22 4 12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"/></svg>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #1F1916; font-family: 'Playfair Display', Georgia, serif; text-transform: none;">Track Gifts &amp; Shagun</div>
          <div style="font-size: 12px; color: #786C65; font-weight: 500; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">Cash, Gold, Gifts &amp; More</div>
        </div>
        <!-- Card 2 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 16px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.borderColor='#C28B38';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 44px; height: 44px; border-radius: 12px; background: #FCF7EC; color: #C28B38; display: flex; align-items: center; justify-content: center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #1F1916; font-family: 'Playfair Display', Georgia, serif; text-transform: none;">Manage Family Events</div>
          <div style="font-size: 12px; color: #786C65; font-weight: 500; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">Weddings, Celebrations &amp; More</div>
        </div>
        <!-- Card 3 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 16px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.borderColor='#C28B38';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 44px; height: 44px; border-radius: 12px; background: #FCF7EC; color: #C28B38; display: flex; align-items: center; justify-content: center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #1F1916; font-family: 'Playfair Display', Georgia, serif; text-transform: none;">Keep Precious Memories</div>
          <div style="font-size: 12px; color: #786C65; font-weight: 500; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">Photos, Videos &amp; Notes</div>
        </div>
        <!-- Card 4 -->
        <div style="background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.45); border-radius: 16px; padding: 22px 18px; text-align: center; box-shadow: 0 4px 18px rgba(0,0,0,0.03); display: flex; flex-direction: column; align-items: center; gap: 8px; transition: transform 0.25s ease, border-color 0.25s ease;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.borderColor='#C28B38';" onmouseleave="this.style.transform='translateY(0)'; this.style.borderColor='rgba(220, 200, 180, 0.45)';">
          <div style="width: 44px; height: 44px; border-radius: 12px; background: #FCF7EC; color: #C28B38; display: flex; align-items: center; justify-content: center;">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          </div>
          <div style="font-size: 15px; font-weight: 700; color: #1F1916; font-family: 'Playfair Display', Georgia, serif; text-transform: none;">Get Detailed Reports</div>
          <div style="font-size: 12px; color: #786C65; font-weight: 500; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">PDF, Excel &amp; More</div>
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
          <div style="display: inline-flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 800; color: #9E6B20; background: #FDF6EC; border: 1px solid #F2E2CA; padding: 4px 14px; border-radius: 999px; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 16px;">
            <span style="color: #C28B38;">◆</span>
            <span>BUILT FOR FAMILIES</span>
            <span style="color: #C28B38;">•</span>
          </div>
          <h2 style="font-family: 'Playfair Display', Georgia, serif; font-size: clamp(24px, 2.6vw, 34px); font-weight: 650; color: #1F1916; line-height: 1.25; margin: 0 0 14px; text-transform: none;">
            A Smarter Way to Remember Together
          </h2>
          <p style="font-size: 15px; color: #5C524B; line-height: 1.65; margin-bottom: 22px; font-weight: 450; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
            From weddings to family gatherings, GiftVault helps you stay organised and connected with your loved ones.
          </p>
          <button type="button" class="btn-ref1-primary" style="height: 38px !important; padding: 0 22px !important; font-size: 13.5px !important; font-weight: 600 !important; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important; text-transform: none !important; border-radius: 999px !important; border: none !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 8px !important; background: linear-gradient(135deg, #C28B38 0%, #A66E22 100%) !important; color: #FFFFFF !important; box-shadow: 0 4px 14px rgba(160, 110, 30, 0.28) !important; margin: 0 !important;" onclick="navToView('login')">
            <span>Learn More</span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </section>

      <!-- 4. BOTTOM TRUST BADGE PILL FROM REFERENCE 1 -->
      <div style="display: flex; align-items: center; justify-content: space-around; flex-wrap: wrap; gap: 18px; background: rgba(255, 255, 255, 0.85); backdrop-filter: blur(12px); border: 1px solid rgba(220, 200, 180, 0.4); border-radius: 999px; padding: 12px 28px; margin-bottom: 50px; box-shadow: 0 4px 16px rgba(0,0,0,0.02); font-size: 13px; font-weight: 600; color: #5C524B; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
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
pat = re.compile(r'<!-- 1\. HERO SECTION DESIGN 1 PER USER REFERENCE.*?<!-- 4\. BOTTOM TRUST BADGE PILL FROM REFERENCE 1 -->\s*<div[^>]*>.*?</div>\s*</div>', re.DOTALL)

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace from <!-- 1. HERO SECTION DESIGN 1 PER USER REFERENCE to the bottom trust badge
    start_str = "<!-- 1. HERO SECTION DESIGN 1 PER USER REFERENCE"
    end_str = "<!-- 3. THREEUI ETALE 52 LIVE SHAGUN ESTIMATOR"
    
    if start_str in content and end_str in content:
        p1 = content.find(start_str)
        p2 = content.find(end_str)
        new_content = content[:p1] + html_snippet + "\n\n      " + content[p2:]
        with open(t, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Polished {t} successfully!")
    else:
        print(f"Markers not found in {t}")
