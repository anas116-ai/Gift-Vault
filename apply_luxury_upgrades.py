# -*- coding: utf-8 -*-
import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. UPGRADE HERO SHOWCASE CONTAINER TO MATCH REFERENCE IMAGE 4
old_hero_showcase = re.search(r'(<!-- Right: Ultra Clean Creative Gifting Vault Showcase.*?)(</section>)', html, re.DOTALL)
if not old_hero_showcase:
    # Try alternative search
    old_hero_showcase = re.search(r'(<div class="hero-showcase-container.*?)(</section>)', html, re.DOTALL)

new_hero_showcase_html = """<!-- Right: Ultra Clean Luxury Gifting Deck Showcase (Matching User Reference Image 4) -->
        <div class="hero-showcase-container hero-product-laptop-card" style="position: relative; max-width: 500px; width: 100%; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
          
          <!-- Outer Reference 4 Master Frame with Soft Radial Glow & Crisp Border -->
          <div style="position: relative; width: 100%; border-radius: 28px; background: linear-gradient(145deg, #FFFFFF 0%, #FAF8F5 100%); border: 1.5px solid rgba(62, 78, 80, 0.16); box-shadow: 0 24px 60px -12px rgba(55,0,10,0.12), 0 0 0 1px rgba(255,255,255,0.8) inset; padding: 22px 22px 24px; overflow: hidden; cursor: pointer; transition: transform 0.35s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.35s ease;" onclick="navToView('login')" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 32px 75px -10px rgba(55,0,10,0.18)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 24px 60px -12px rgba(55,0,10,0.12)';">
            
            <!-- Reference 4 Top Navigation Micro-Bar -->
            <div style="display: flex; align-items: center; justify-content: space-between; padding-bottom: 14px; border-bottom: 1px solid rgba(62,78,80,0.08); margin-bottom: 18px;">
              <div style="display: flex; align-items: center; gap: 4px; color: #3E4E50; opacity: 0.7;">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <circle cx="5" cy="5" r="1.5" fill="currentColor"/><circle cx="12" cy="5" r="1.5" fill="currentColor"/><circle cx="19" cy="5" r="1.5" fill="currentColor"/>
                  <circle cx="5" cy="12" r="1.5" fill="currentColor"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/><circle cx="19" cy="12" r="1.5" fill="currentColor"/>
                </svg>
              </div>
              <div style="display: flex; align-items: center; gap: 16px; font-size: 11px; font-weight: 600; color: #3E4E50; font-family: 'Sen', sans-serif;">
                <span style="color: #37000A; font-weight: 700;">Home</span>
                <span>Events</span>
                <span>Shagun</span>
                <span>Vault</span>
              </div>
              <div style="color: #3E4E50; opacity: 0.7;">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              </div>
            </div>

            <!-- Reference 4 Vertical Stepper Dots on Left Edge -->
            <div style="position: absolute; left: 10px; top: 50%; transform: translateY(-50%); display: flex; flex-direction: column; gap: 6px; z-index: 4;">
              <span style="width: 4px; height: 4px; border-radius: 50%; background: #37000A;"></span>
              <span style="width: 4px; height: 4px; border-radius: 50%; background: #FF1F3D;"></span>
              <span style="width: 4px; height: 4px; border-radius: 50%; background: rgba(62,78,80,0.3);"></span>
              <span style="width: 4px; height: 4px; border-radius: 50%; background: rgba(62,78,80,0.3);"></span>
            </div>

            <!-- Central Visual Container: Sacred Leather Digital Vault Deck -->
            <div style="position: relative; width: 100%; min-height: 290px; display: flex; align-items: center; justify-content: center; padding: 10px 0 20px;">
              
              <!-- Ambient Warm Sacred Glow Behind Deck -->
              <div style="position: absolute; width: 220px; height: 220px; border-radius: 50%; background: radial-gradient(circle, rgba(158,228,37,0.18) 0%, rgba(255,31,61,0.08) 50%, transparent 70%); filter: blur(28px); pointer-events: none;"></div>

              <!-- Photorealistic Sacred Digital Vault Deck SVG -->
              <div style="position: relative; z-index: 2; width: 260px; height: 185px; background: linear-gradient(135deg, #37000A 0%, #1F0005 100%); border-radius: 20px; border: 2px solid #FF1F3D; box-shadow: 0 18px 40px rgba(55,0,10,0.35), 0 0 0 1px rgba(158,228,37,0.4); padding: 16px; display: flex; flex-direction: column; justify-content: space-between; transform: rotate(-2deg); transition: transform 0.3s ease;">
                <!-- Header inside Deck -->
                <div style="display: flex; justify-content: space-between; align-items: center;">
                  <div style="display: flex; align-items: center; gap: 6px;">
                    <span style="width: 7px; height: 7px; border-radius: 50%; background: #9EE425; box-shadow: 0 0 8px #9EE425;"></span>
                    <span style="font-size: 10px; font-weight: 800; color: #FFFFFF; letter-spacing: 0.1em; font-family: 'Sen', sans-serif;">GIFTVAULT • LIVE</span>
                  </div>
                  <!-- Sacred Gold Auspicious Emblem -->
                  <div style="width: 24px; height: 24px; border-radius: 50%; background: linear-gradient(135deg, #9EE425 0%, #76B413 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 6px rgba(0,0,0,0.3);">
                    <span style="font-size: 11px; font-weight: 900; color: #37000A;">శ్రీ</span>
                  </div>
                </div>

                <!-- Ledger Pool Amount -->
                <div>
                  <div style="font-size: 9.5px; color: #F2EFEA; opacity: 0.8; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 2px;">Sacred Shagun Balance</div>
                  <div style="font-size: 28px; font-weight: 800; color: #FFFFFF; font-family: 'Sen', sans-serif; letter-spacing: -0.02em; display: flex; align-items: baseline; gap: 6px;">
                    <span>₹ 47,500</span>
                    <span style="font-size: 11px; font-weight: 700; color: #9EE425; background: rgba(158,228,37,0.18); padding: 1px 6px; border-radius: 4px;">+12%</span>
                  </div>
                </div>

                <!-- Micro Status Footnote -->
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 9px; color: #F2EFEA; opacity: 0.85; border-top: 1px solid rgba(255,255,255,0.12); pt: 6px; margin-top: 6px;">
                  <span>Chirala Beach Mandapam</span>
                  <span style="color: #9EE425; font-weight: 700;">● 100% Verified</span>
                </div>
              </div>

              <!-- REFERENCE IMAGE 4 CALLOUT 1 (Top-Right): Shagun Pool Active -->
              <div style="position: absolute; right: 0; top: 18px; z-index: 5; display: flex; align-items: center; gap: 6px; background: rgba(255,255,255,0.92); backdrop-filter: blur(8px); border: 1.5px solid #9EE425; padding: 6px 12px; border-radius: 999px; box-shadow: 0 8px 20px rgba(55,0,10,0.08); transition: transform 0.25s ease;" onmouseenter="this.style.transform='scale(1.05)'" onmouseleave="this.style.transform='scale(1)'">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #9EE425; box-shadow: 0 0 8px #9EE425;"></span>
                <div style="font-size: 11px; font-family: 'Sen', sans-serif; color: #37000A; font-weight: 700;">
                  <span>Shagun Pool: </span><span style="color: #37000A;">₹ 51,116</span>
                </div>
              </div>

              <!-- REFERENCE IMAGE 4 CALLOUT 2 (Middle-Right): Instant 2" Thermal Slip -->
              <div style="position: absolute; right: -6px; top: 92px; z-index: 5; display: flex; align-items: center; gap: 6px; background: rgba(255,255,255,0.92); backdrop-filter: blur(8px); border: 1.5px solid #FF1F3D; padding: 6px 12px; border-radius: 999px; box-shadow: 0 8px 20px rgba(55,0,10,0.08); transition: transform 0.25s ease;" onmouseenter="this.style.transform='scale(1.05)'" onmouseleave="this.style.transform='scale(1)'">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #FF1F3D; box-shadow: 0 0 8px #FF1F3D;"></span>
                <div style="font-size: 11px; font-family: 'Sen', sans-serif; color: #37000A; font-weight: 700;">
                  <span>Slip: </span><span style="color: #FF1F3D;">2" Thermal + WA</span>
                </div>
              </div>

              <!-- REFERENCE IMAGE 4 CALLOUT 3 (Lower-Right): Offline Ready -->
              <div style="position: absolute; right: 8px; bottom: 32px; z-index: 5; display: flex; align-items: center; gap: 6px; background: rgba(255,255,255,0.92); backdrop-filter: blur(8px); border: 1.5px solid #3E4E50; padding: 6px 12px; border-radius: 999px; box-shadow: 0 8px 20px rgba(55,0,10,0.08); transition: transform 0.25s ease;" onmouseenter="this.style.transform='scale(1.05)'" onmouseleave="this.style.transform='scale(1)'">
                <span style="width: 8px; height: 8px; border-radius: 50%; background: #3E4E50;"></span>
                <div style="font-size: 11px; font-family: 'Sen', sans-serif; color: #37000A; font-weight: 700;">
                  <span>Offline: </span><span style="color: #3E4E50;">100% Active</span>
                </div>
              </div>

            </div>

            <!-- REFERENCE IMAGE 4 FLOATING CARD (Bottom-Left, like '02 Orange Fun') -->
            <div style="position: relative; z-index: 6; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(14px); border: 1.5px solid rgba(62, 78, 80, 0.16); border-radius: 16px; padding: 12px 14px; box-shadow: 0 12px 30px rgba(55,0,10,0.08); display: flex; align-items: center; justify-content: space-between; margin-top: -10px;">
              <div style="display: flex; align-items: center; gap: 10px;">
                <!-- Step Number Thumbnail Badge -->
                <div style="width: 32px; height: 32px; border-radius: 10px; background: #37000A; color: #9EE425; font-size: 12px; font-weight: 800; display: flex; align-items: center; justify-content: center; font-family: 'Sen', sans-serif;">
                  01
                </div>
                <div>
                  <div style="font-family: 'Sen', sans-serif; font-size: 12.5px; font-weight: 700; color: #37000A;">Chirala Mandapam</div>
                  <div style="font-size: 10.5px; color: #3E4E50; white-space: nowrap;">+ ₹5,116 Shagun logged</div>
                </div>
              </div>
              <div style="font-size: 10px; font-weight: 700; color: #37000A; background: #9EE425; padding: 4px 10px; border-radius: 999px; border: 1px solid #37000A; white-space: nowrap;">
                Printed Slip
              </div>
            </div>

          </div>

          <!-- Hidden canvas for Three.js hooks if required -->
          <canvas id="three-coin-canvas" style="display: none;"></canvas>
        </div>
      </section>"""

if old_hero_showcase:
    html = html[:old_hero_showcase.start(1)] + new_hero_showcase_html + html[old_hero_showcase.end(2):]
    print("✅ Hero Showcase updated to match Reference Image 4!")
else:
    print("❌ Could not locate old hero showcase in index.html")


# 2. UPGRADE PRICING SECTION WITH PROMINENT TELUGU MENTIONS & LUXURY CARDS
old_pricing = re.search(r'(<section[^>]*id="pricing".*?)(<div class="nav-bottom-mobile"|<section id="features"|<footer|</main>)', html, re.DOTALL)

new_pricing_html = """<section id="pricing" style="margin-bottom: 70px; padding: 30px 0;">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 40px;">
          <div style="display: inline-flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 800; color: #FF1F3D; letter-spacing: 0.15em; text-transform: uppercase; font-family: 'Absans', sans-serif; margin-bottom: 8px;">
            <span>◆</span>
            <span>పారదర్శక పాస్ ధరలు • TRANSPARENT PASS PRICING</span>
            <span>◆</span>
          </div>
          <h2 style="font-family: 'Sen', sans-serif !important; font-weight: 700 !important; letter-spacing: -0.01em; font-size: 34px; color: #37000A; margin: 8px 0 12px;">Pay Per Celebration. Zero Monthly Trap.</h2>
          <p style="font-size: 15px; color: #3E4E50; line-height: 1.6; margin: 0;">ప్రతి పవిత్ర కుటుంబ వేడుకకు అందుబాటులో ఉండే పారదర్శక పాస్. ఎలాంటి నెలవారీ చందా రుసుములు లేవు.</p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px; max-width: 860px; margin: 0 auto;">
          
          <!-- 1. Single Pass (సింగిల్ కార్యం పాస్) -->
          <div class="card-animate" style="background: #FFFFFF; border: 1.5px solid rgba(62, 78, 80, 0.18); border-radius: 24px; padding: 30px 28px; box-shadow: 0 14px 36px rgba(55,0,10,0.06); position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.25s ease, box-shadow 0.25s ease;" onmouseenter="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 20px 45px rgba(55,0,10,0.12)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 14px 36px rgba(55,0,10,0.06)';">
            <svg style="position: absolute; right: -15px; bottom: -15px; width: 140px; height: 140px; opacity: 0.04; pointer-events: none;" viewBox="0 0 24 24" fill="none" stroke="#37000A" stroke-width="1.5"><path d="M6 3h12M6 8h12M6 13l7 8M6 13h4a4 4 0 0 0 0-8"/></svg>
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <span style="font-size: 10px; font-weight: 700; color: #3E4E50; background: #F2EFEA; border: 1px solid rgba(62,78,80,0.2); padding: 4px 10px; border-radius: 6px; text-transform: uppercase;">సింగిల్ పాస్ • SINGLE PASS</span>
                <span style="font-size: 10.5px; font-weight: 700; color: #FFFFFF; background: #37000A; padding: 4px 10px; border-radius: 6px;">జీవితకాల యాక్సెస్</span>
              </div>
              <h3 style="font-family: 'Sen', sans-serif !important; font-size: 22px; font-weight: 700; color: #37000A; margin: 0 0 6px;">Single Celebration Pass</h3>
              <div style="font-size: 12.5px; color: #FF1F3D; font-weight: 600; margin-bottom: 14px;">ఒక్క శుభకార్యానికి సంపూర్ణ నిర్వహణ</div>
              <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 18px;">
                <span style="font-size: 38px; font-weight: 800; color: #37000A; font-family: 'Sen', sans-serif;">₹49</span>
                <span style="font-size: 13.5px; color: #3E4E50; font-weight: 500;">/ ఒక్క శుభకార్యానికి (One-Time)</span>
              </div>
              <ul style="list-style: none; padding: 0; margin: 0 0 24px; display: flex; flex-direction: column; gap: 10px; font-size: 13.5px; color: #3E4E50;">
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: 900; background: #37000A; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> 1 సంపూర్ణ శుభకార్యం (1 Complete Event)</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: 900; background: #37000A; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> 500 మంది వరకు అతిథుల లెక్కలు (Up to 500 Guests)</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: 900; background: #37000A; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> 2-అంగుళాల థర్మల్ రసీదులు & ఎక్సెల్ రిపోర్ట్ (Thermal Slips)</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: 900; background: #37000A; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> 100% ఆఫ్‌లైన్ రక్షణ & డేటా గోప్యత (Offline Ready)</li>
              </ul>
            </div>
            <button type="button" class="btn-tactile-primary" onclick="window.GVStore ? window.GVStore.purchasePass('single', 49) : navToView('login')" style="height: 38px !important; padding: 0 20px !important; border-radius: 999px !important; background: #9EE425 !important; color: #37000A !important; border: 1.5px solid #37000A !important; font-family: 'Sen', sans-serif !important; font-weight: 700 !important; font-size: 13.5px !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; width: 100% !important; max-width: 100% !important; box-shadow: 0 4px 14px rgba(158,228,37,0.4) !important;">
              <span>Get ₹49 Pass</span>
            </button>
          </div>

          <!-- 2. Family Pack (ఫ్యామిలీ ప్యాక్ - అత్యంత ప్రజాదరణ పొందినది) -->
          <div class="card-animate" style="background: linear-gradient(155deg, #37000A 0%, #1A0005 100%); border: 2px solid #FF1F3D; border-radius: 24px; padding: 30px 28px; box-shadow: 0 20px 48px rgba(55,0,10,0.30); position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.25s ease, box-shadow 0.25s ease;" onmouseenter="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 26px 60px rgba(55,0,10,0.45)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 48px rgba(55,0,10,0.30)';">
            <svg style="position: absolute; right: -15px; bottom: -15px; width: 140px; height: 140px; opacity: 0.08; pointer-events: none;" viewBox="0 0 24 24" fill="none" stroke="#9EE425" stroke-width="1.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <span style="font-size: 10px; font-weight: 700; color: #FFFFFF; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25); padding: 4px 10px; border-radius: 6px; text-transform: uppercase;">ఫ్యామిలీ ప్యాక్ • FAMILY PACK</span>
                <span style="font-size: 10.5px; font-weight: 800; color: #37000A; background: #9EE425; padding: 4px 10px; border-radius: 6px;">అత్యంత ప్రజాదరణ పొందినది</span>
              </div>
              <h3 style="font-family: 'Sen', sans-serif !important; font-size: 22px; font-weight: 700; color: #FFFFFF; margin: 0 0 6px;">All Family Events Pack</h3>
              <div style="font-size: 12.5px; color: #9EE425; font-weight: 600; margin-bottom: 14px;">సంపూర్ణ కుటుంబ వేడుకలు • అపరిమిత యాక్సెస్</div>
              <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 18px;">
                <span style="font-size: 38px; font-weight: 800; color: #FFFFFF; font-family: 'Sen', sans-serif;">₹99</span>
                <span style="font-size: 13.5px; color: #F2EFEA; opacity: 0.85;">/ అపరిమిత వేడుకలు (Lifetime All Events)</span>
              </div>
              <ul style="list-style: none; padding: 0; margin: 0 0 24px; display: flex; flex-direction: column; gap: 10px; font-size: 13.5px; color: #F2EFEA;">
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #37000A; font-weight: 900; background: #9EE425; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> అపరిమిత శుభకార్యాలు (Unlimited Auspicious Events)</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #37000A; font-weight: 900; background: #9EE425; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> అపరిమిత అతిథుల లెక్కలు (Unlimited Guests Logged)</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #37000A; font-weight: 900; background: #9EE425; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> బహుళ పరికరాల ఫ్యామిలీ సింక్ (Multi-Device Sync)</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #37000A; font-weight: 900; background: #9EE425; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> రిటర్న్ శagun రిసిప్రోసిటీ ట్రాకింగ్ (Reciprocity Engine)</li>
              </ul>
            </div>
            <button type="button" class="btn-tactile-primary" onclick="window.GVStore ? window.GVStore.purchasePass('family', 99) : navToView('login')" style="height: 38px !important; padding: 0 20px !important; border-radius: 999px !important; background: #9EE425 !important; color: #37000A !important; border: 1.5px solid #37000A !important; font-family: 'Sen', sans-serif !important; font-weight: 700 !important; font-size: 13.5px !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; width: 100% !important; max-width: 100% !important; box-shadow: 0 4px 14px rgba(158,228,37,0.5) !important;">
              <span>Get ₹99 Family Pack</span>
            </button>
          </div>

        </div>
      </section>"""

if old_pricing:
    html = html[:old_pricing.start(1)] + new_pricing_html + html[old_pricing.start(2):]
    print("✅ Pricing Section updated with Telugu mentions & luxury cards!")
else:
    print("❌ Could not locate pricing section in index.html")

# Write updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully.")
