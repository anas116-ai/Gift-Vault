# -*- coding: utf-8 -*-
import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# -----------------------------------------------------------------------------
# 1. HERO SECTION: REPLACE RIGHT SHOWCASE WITH BEFORE-PREVIOUS IMAGE
# -----------------------------------------------------------------------------
old_hero_showcase = re.search(r'(<!-- Right: Ultra Clean.*?)(</section>)', html, re.DOTALL)
if not old_hero_showcase:
    old_hero_showcase = re.search(r'(<div class="hero-showcase-container.*?)(</section>)', html, re.DOTALL)

new_hero_showcase_html = """        <!-- Right: Ultra Clean Creative Gifting Vault Showcase (Before-Previous Master Image) -->
        <div class="hero-showcase-container hero-product-laptop-card" style="position: relative; max-width: 480px; width: 100%; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
          
          <div style="position: relative; width: 100%; border-radius: 28px; overflow: hidden; background: #FFFFFF; border: 1.5px solid rgba(62, 78, 80, 0.18); box-shadow: 0 24px 60px -12px rgba(55,0,10,0.12); cursor: pointer; transition: transform 0.35s ease, box-shadow 0.35s ease;" onclick="navToView('login')" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 30px 70px -10px rgba(55,0,10,0.18)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 24px 60px -12px rgba(55,0,10,0.12)';">
            
            <!-- Ultra High-Resolution Photorealistic Hero Image (Before-Previous Version) -->
            <img src="assets/images/giftvault_hero_showcase_master.jpg" alt="GiftVault Mobile App Showcase" style="width: 100%; height: auto; display: block; object-fit: cover;">

            <!-- Subtle Floating Live Shagun Badge (Bottom Right) -->
            <div style="position: absolute; bottom: 18px; right: 18px; background: rgba(55, 0, 10, 0.88); backdrop-filter: blur(12px); border: 1px solid rgba(158, 228, 37, 0.6); border-radius: 12px; padding: 8px 14px; box-shadow: 0 10px 24px rgba(0,0,0,0.3); display: flex; align-items: center; gap: 8px;">
              <span style="width: 8px; height: 8px; border-radius: 50%; background: #9EE425; box-shadow: 0 0 8px #9EE425; display: inline-block;"></span>
              <div>
                <div style="font-family: 'Sen', sans-serif; font-size: 12px; font-weight: 700; color: #FFFFFF;">₹ 47,500 <span style="font-size: 10px; color: #9EE425;">(+12%)</span></div>
                <div style="font-size: 9px; color: #F2EFEA; text-transform: uppercase; letter-spacing: 0.05em;">Live Family Vault</div>
              </div>
            </div>

          </div>

          <!-- Hidden three-coin-canvas so test/script doesn't throw null error -->
          <canvas id="three-coin-canvas" style="display: none;"></canvas>
        </div>"""

if old_hero_showcase:
    html = html[:old_hero_showcase.start(1)] + new_hero_showcase_html + "\n      " + html[old_hero_showcase.start(2):]
    print("✅ 1. Hero Showcase restored with before-previous image!")
else:
    print("❌ Could not locate hero showcase in index.html")


# -----------------------------------------------------------------------------
# 2. UNDER-HERO CARDS: RESTORE BEFORE-PREVIOUS 4 DISTINCT CARDS STRIP
# -----------------------------------------------------------------------------
# Find the section right under hero (could be the 3 cards section or features-collection-grid)
old_under_hero_cards = re.search(r'(<!-- ==================================================================\s*2\. 3 CREATIVE LUXURY CARDS.*?)(<!-- ==================================================================\s*3\.|\s*<section id="features"|<section id="how-it-works")', html, re.DOTALL)
if not old_under_hero_cards:
    old_under_hero_cards = re.search(r'(<section style="margin: 20px 0 54px;".*?)(<section id="features"|<section id="how-it-works"|<section class="hero-ref1-family-section")', html, re.DOTALL)

new_four_cards_strip = """      <!-- ==================================================================
           2. FOUR CORE FEATURE CARDS STRIP (Before-Previous Distinct 4 Cards)
           ================================================================== -->
      <section class="hero-four-cards-strip" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin: 16px 0 50px;">
        
        <!-- Card 1: Rich Mahogany & Strawberry Red Luxury (#37000A + #FF1F3D) -->
        <div class="card-animate" style="background: linear-gradient(145deg, #37000A 0%, #200006 100%); border: 1.5px solid rgba(255,31,61,0.45); border-radius: 18px; padding: 22px 18px; box-shadow: 0 10px 28px rgba(55,0,10,0.22); transition: transform 0.25s ease, box-shadow 0.25s ease; display: flex; flex-direction: column; justify-content: space-between;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 36px rgba(55,0,10,0.35)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 28px rgba(55,0,10,0.22)';">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
              <div style="width: 42px; height: 42px; border-radius: 12px; background: rgba(255,31,61,0.2); border: 1.5px solid #FF1F3D; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px rgba(255,31,61,0.35);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="3" y="8" width="18" height="13" rx="2"/>
                  <path d="M12 8V21"/>
                  <path d="M3 13.5H21"/>
                  <path d="M12 8C10.5 4.5 7 5 7 5C7 5 6.5 8 12 8Z"/>
                  <path d="M12 8C13.5 4.5 17 5 17 5C17 5 17.5 8 12 8Z"/>
                </svg>
              </div>
              <span style="font-size: 10px; font-weight: 800; color: #9EE425; background: rgba(158,228,37,0.15); border: 1px solid rgba(158,228,37,0.4); padding: 3px 8px; border-radius: 20px; letter-spacing: 0.05em;">● LIVE VAULT</span>
            </div>
            <div style="font-family: 'Sen', sans-serif; font-size: 16px; font-weight: 700; color: #F2EFEA; margin-bottom: 6px;">Track Gifts & Shagun</div>
            <div style="font-size: 12.5px; color: rgba(242, 239, 234, 0.82); line-height: 1.45;">Cash envelopes, gold jewellery, silver articles & custom blessings logged in seconds.</div>
          </div>
          <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 11px; font-weight: 700; color: #FF7084;">Cash • Gold • Silver</span>
            <span style="font-size: 11px; color: #F2EFEA; opacity: 0.6;">01</span>
          </div>
        </div>

        <!-- Card 2: Warm Parchment & Iron Grey Deep Tradition (#F2EFEA + #3E4E50) -->
        <div class="card-animate" style="background: linear-gradient(145deg, #FAF8F5 0%, #EFEBE4 100%); border: 1.5px solid #3E4E50; border-radius: 18px; padding: 22px 18px; box-shadow: 0 10px 24px rgba(62,78,80,0.1); transition: transform 0.25s ease, box-shadow 0.25s ease; display: flex; flex-direction: column; justify-content: space-between;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 34px rgba(62,78,80,0.18)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 24px rgba(62,78,80,0.1)';">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
              <div style="width: 42px; height: 42px; border-radius: 12px; background: rgba(62,78,80,0.12); border: 1.5px solid #3E4E50; display: flex; align-items: center; justify-content: center;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#37000A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
                  <circle cx="9" cy="7" r="4"/>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
                </svg>
              </div>
              <span style="font-size: 10px; font-weight: 800; color: #37000A; background: #FFFFFF; border: 1px solid rgba(62,78,80,0.25); padding: 3px 8px; border-radius: 20px;">ALL OCCASIONS</span>
            </div>
            <div style="font-family: 'Sen', sans-serif; font-size: 16px; font-weight: 700; color: #37000A; margin-bottom: 6px;">Manage Family Events</div>
            <div style="font-size: 12.5px; color: #3E4E50; line-height: 1.45;">Weddings, Griha Pravesham, Silver Jubilee, Half-Saree & sacred pujas in one account.</div>
          </div>
          <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(62,78,80,0.15); display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 11px; font-weight: 700; color: #37000A;">Multi-Event Sync</span>
            <span style="font-size: 11px; color: #3E4E50; opacity: 0.6;">02</span>
          </div>
        </div>

        <!-- Card 3: Strawberry Red Vibrancy & Slime Lime Accents (#FF1F3D + #9EE425) -->
        <div class="card-animate" style="background: linear-gradient(145deg, #FF1F3D 0%, #D40F2B 100%); border: 1.5px solid #9EE425; border-radius: 18px; padding: 22px 18px; box-shadow: 0 10px 28px rgba(255,31,61,0.25); transition: transform 0.25s ease, box-shadow 0.25s ease; display: flex; flex-direction: column; justify-content: space-between;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 36px rgba(255,31,61,0.38)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 28px rgba(255,31,61,0.25)';">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
              <div style="width: 42px; height: 42px; border-radius: 12px; background: rgba(0,0,0,0.18); border: 1.5px solid #FFFFFF; display: flex; align-items: center; justify-content: center;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                </svg>
              </div>
              <span style="font-size: 10px; font-weight: 800; color: #37000A; background: #9EE425; padding: 3px 8px; border-radius: 20px; box-shadow: 0 2px 6px rgba(0,0,0,0.15);">MEMORY SAFE</span>
            </div>
            <div style="font-family: 'Sen', sans-serif; font-size: 16px; font-weight: 700; color: #FFFFFF; margin-bottom: 6px;">Keep Precious Memories</div>
            <div style="font-size: 12.5px; color: #F2EFEA; line-height: 1.45;">Remember who blessed your family and return blessings with sacred reciprocity.</div>
          </div>
          <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 11px; font-weight: 700; color: #9EE425;">Reciprocity Engine</span>
            <span style="font-size: 11px; color: #FFFFFF; opacity: 0.8;">03</span>
          </div>
        </div>

        <!-- Card 4: Modern Iron Grey & Slime Lime Power (#3E4E50 + #9EE425) -->
        <div class="card-animate" style="background: linear-gradient(145deg, #3E4E50 0%, #2A3638 100%); border: 1.5px solid #9EE425; border-radius: 18px; padding: 22px 18px; box-shadow: 0 10px 28px rgba(62,78,80,0.2); transition: transform 0.25s ease, box-shadow 0.25s ease; display: flex; flex-direction: column; justify-content: space-between;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 36px rgba(62,78,80,0.32)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 28px rgba(62,78,80,0.2)';">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
              <div style="width: 42px; height: 42px; border-radius: 12px; background: rgba(158,228,37,0.15); border: 1.5px solid #9EE425; display: flex; align-items: center; justify-content: center;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#9EE425" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                  <line x1="16" y1="13" x2="8" y2="13"/>
                  <line x1="16" y1="17" x2="8" y2="17"/>
                  <polyline points="10 9 9 9 8 9"/>
                </svg>
              </div>
              <span style="font-size: 10px; font-weight: 800; color: #37000A; background: #9EE425; padding: 3px 8px; border-radius: 20px;">SMART SLIP</span>
            </div>
            <div style="font-family: 'Sen', sans-serif; font-size: 16px; font-weight: 700; color: #F2EFEA; margin-bottom: 6px;">Get Detailed Reports</div>
            <div style="font-size: 12.5px; color: rgba(242, 239, 234, 0.85); line-height: 1.45;">2-inch thermal counter slips, WhatsApp receipts, and complete Excel/PDF downloads.</div>
          </div>
          <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.12); display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 11px; font-weight: 700; color: #9EE425;">Thermal & Excel</span>
            <span style="font-size: 11px; color: #F2EFEA; opacity: 0.6;">04</span>
          </div>
        </div>

      </section>"""

if old_under_hero_cards:
    html = html[:old_under_hero_cards.start(1)] + new_four_cards_strip + "\n\n      " + html[old_under_hero_cards.start(2):]
    print("✅ 2. Restored 4 distinct cards strip under hero!")
else:
    print("❌ Could not locate under-hero cards in index.html")


# -----------------------------------------------------------------------------
# 3. BUILT FOR FAMILIES: REMOVE COMPLETELY PER USER REQUEST
# -----------------------------------------------------------------------------
html = re.sub(r'<!--\s*=+\s*3\. BUILT FOR FAMILIES.*?-->\s*<section class="hero-ref1-family-section".*?</section>', '', html, flags=re.DOTALL)
html = re.sub(r'<section class="hero-ref1-family-section".*?</section>', '', html, flags=re.DOTALL)
print("✅ 3. Removed 'Built for Families' section completely!")


# -----------------------------------------------------------------------------
# 4. CELEBRATION CARDS (#culture):
#    - Half top image (No people in reception, illuminated house exterior, silver jubilee stage)
#    - Half bottom normal color for text writing
#    - NO TELUGU anywhere in this section!
# -----------------------------------------------------------------------------
old_culture = re.search(r'(<section[^>]*id="culture".*?)(<section[^>]*id="pricing"|<footer|</main>)', html, re.DOTALL)

new_culture_html = """<section id="culture" style="margin-bottom: 70px; padding: 20px 0;">
        <div style="text-align: center; max-width: 650px; margin: 0 auto 36px;">
          <div style="font-size: 11px; font-weight: 800; color: #FF1F3D; letter-spacing: 0.15em; text-transform: uppercase; font-family: 'Absans', sans-serif;">TRADITION & HERITAGE</div>
          <h2 style="font-family: 'Sen', sans-serif !important; font-weight: 400 !important; letter-spacing: -0.01em; font-size: 34px; color: #37000A; margin-top: 8px;">Celebrations Supported Across India</h2>
          <p style="font-size: 14.5px; color: #3E4E50; line-height: 1.6; margin-top: 8px;">GiftVault is tailored for the sacred rituals, guest contributions, and shagun traditions of your family celebrations.</p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px;">
          
          <!-- 1. Wedding Reception (Empty Palace Stage - No People) -->
          <div class="card-animate" style="background: #FFFFFF; border-radius: 24px; border: 1.5px solid rgba(62, 78, 80, 0.16); overflow: hidden; box-shadow: 0 14px 36px rgba(55,0,10,0.06); display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;" onmouseenter="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 22px 48px rgba(55,0,10,0.12)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 14px 36px rgba(55,0,10,0.06)';">
            <!-- Top Half Image: Empty Reception Stage -->
            <div style="position: relative; width: 100%; height: 210px; overflow: hidden; background: #37000A;">
              <img src="assets/images/celebration_reception_empty_stage.jpg" alt="Wedding Reception Royal Stage" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" onmouseenter="this.style.transform='scale(1.04)'" onmouseleave="this.style.transform='scale(1)'">
              <span style="position: absolute; top: 14px; left: 14px; font-size: 10.5px; font-weight: 700; color: #FFFFFF; background: rgba(55, 0, 10, 0.82); backdrop-filter: blur(8px); padding: 4px 10px; border-radius: 999px; letter-spacing: 0.04em;">WEDDING RECEPTION</span>
            </div>
            <!-- Bottom Half: Clean Content for Text -->
            <div style="padding: 22px 20px; display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
              <div>
                <h3 style="font-family: 'Sen', sans-serif !important; font-size: 20px; font-weight: 700; color: #37000A; margin: 0 0 8px;">Wedding Receptions</h3>
                <p style="font-size: 13.5px; color: #3E4E50; line-height: 1.55; margin: 0 0 18px;">Multi-day celebration management, dual bride & groom counters, shagun envelopes with Lucky Coin auto-add, and instant thermal slips.</p>
              </div>
              <button type="button" class="btn-tactile-primary" onclick="navToView('login')" style="height: 36px !important; padding: 0 16px !important; border-radius: 999px !important; background: #9EE425 !important; color: #37000A !important; border: 1.5px solid #37000A !important; font-family: 'Sen', sans-serif !important; font-weight: 700 !important; font-size: 12.5px !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; width: 100% !important;">
                <span>Explore Rituals →</span>
              </button>
            </div>
          </div>

          <!-- 2. Housewarming (Illuminated House Exterior - Full House Lighting) -->
          <div class="card-animate" style="background: #FFFFFF; border-radius: 24px; border: 1.5px solid rgba(62, 78, 80, 0.16); overflow: hidden; box-shadow: 0 14px 36px rgba(55,0,10,0.06); display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;" onmouseenter="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 22px 48px rgba(55,0,10,0.12)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 14px 36px rgba(55,0,10,0.06)';">
            <!-- Top Half Image: Illuminated House Exterior -->
            <div style="position: relative; width: 100%; height: 210px; overflow: hidden; background: #1F2829;">
              <img src="assets/images/celebration_housewarming_illuminated_exterior.jpg" alt="Housewarming Villa Illuminated Exterior" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" onmouseenter="this.style.transform='scale(1.04)'" onmouseleave="this.style.transform='scale(1)'">
              <span style="position: absolute; top: 14px; left: 14px; font-size: 10.5px; font-weight: 700; color: #FFFFFF; background: rgba(62, 78, 80, 0.85); backdrop-filter: blur(8px); padding: 4px 10px; border-radius: 999px; letter-spacing: 0.04em;">GRIHA PRAVESHAM</span>
            </div>
            <!-- Bottom Half: Clean Content for Text -->
            <div style="padding: 22px 20px; display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
              <div>
                <h3 style="font-family: 'Sen', sans-serif !important; font-size: 20px; font-weight: 700; color: #37000A; margin: 0 0 8px;">Housewarming & Blessings</h3>
                <p style="font-size: 13.5px; color: #3E4E50; line-height: 1.55; margin: 0 0 18px;">Track brass samai lamps, silver idols, cash blessings with hometown tagging, relatives indexing, and real-time family totals.</p>
              </div>
              <button type="button" class="btn-tactile-primary" onclick="navToView('login')" style="height: 36px !important; padding: 0 16px !important; border-radius: 999px !important; background: #9EE425 !important; color: #37000A !important; border: 1.5px solid #37000A !important; font-family: 'Sen', sans-serif !important; font-weight: 700 !important; font-size: 12.5px !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; width: 100% !important;">
                <span>Explore Rituals →</span>
              </button>
            </div>
          </div>

          <!-- 3. Silver Jubilee (Empty Milestone Celebration Stage) -->
          <div class="card-animate" style="background: #FFFFFF; border-radius: 24px; border: 1.5px solid rgba(62, 78, 80, 0.16); overflow: hidden; box-shadow: 0 14px 36px rgba(55,0,10,0.06); display: flex; flex-direction: column; transition: transform 0.3s ease, box-shadow 0.3s ease;" onmouseenter="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 22px 48px rgba(55,0,10,0.12)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 14px 36px rgba(55,0,10,0.06)';">
            <!-- Top Half Image: Silver Jubilee Milestone Stage -->
            <div style="position: relative; width: 100%; height: 210px; overflow: hidden; background: #37000A;">
              <img src="assets/images/celebration_silver_jubilee_stage.jpg" alt="Silver Jubilee Anniversary Stage" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;" onmouseenter="this.style.transform='scale(1.04)'" onmouseleave="this.style.transform='scale(1)'">
              <span style="position: absolute; top: 14px; left: 14px; font-size: 10.5px; font-weight: 700; color: #FFFFFF; background: rgba(55, 0, 10, 0.82); backdrop-filter: blur(8px); padding: 4px 10px; border-radius: 999px; letter-spacing: 0.04em;">SILVER JUBILEE</span>
            </div>
            <!-- Bottom Half: Clean Content for Text -->
            <div style="padding: 22px 20px; display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
              <div>
                <h3 style="font-family: 'Sen', sans-serif !important; font-size: 20px; font-weight: 700; color: #37000A; margin: 0 0 8px;">Silver Jubilee & Milestones</h3>
                <p style="font-size: 13.5px; color: #3E4E50; line-height: 1.55; margin: 0 0 18px;">25 years of togetherness: preserve family blessings, guest lists, return gift registers, and export complete records to Excel & PDF.</p>
              </div>
              <button type="button" class="btn-tactile-primary" onclick="navToView('login')" style="height: 36px !important; padding: 0 16px !important; border-radius: 999px !important; background: #9EE425 !important; color: #37000A !important; border: 1.5px solid #37000A !important; font-family: 'Sen', sans-serif !important; font-weight: 700 !important; font-size: 12.5px !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; width: 100% !important;">
                <span>Explore Rituals →</span>
              </button>
            </div>
          </div>

        </div>
      </section>"""

if old_culture:
    html = html[:old_culture.start(1)] + new_culture_html + "\n\n      " + html[old_culture.start(2):]
    print("✅ 4. Updated Culture section: half image (no people), half clean text, NO TELUGU!")
else:
    print("❌ Could not locate culture section in index.html")


# -----------------------------------------------------------------------------
# 5. PRICING SECTION: REMOVE ALL TELUGU PER USER REQUEST
#    Clean luxury English cards with small compact Lemon Green buttons!
# -----------------------------------------------------------------------------
old_pricing = re.search(r'(<section[^>]*id="pricing".*?)(<div class="nav-bottom-mobile"|<section id="features"|<footer|</main>)', html, re.DOTALL)

new_pricing_clean_html = """<section id="pricing" style="margin-bottom: 70px; padding: 30px 0;">
        <div style="text-align: center; max-width: 680px; margin: 0 auto 40px;">
          <div style="display: inline-flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 800; color: #FF1F3D; letter-spacing: 0.15em; text-transform: uppercase; font-family: 'Absans', sans-serif; margin-bottom: 8px;">
            <span>◆</span>
            <span>TRANSPARENT PASS PRICING</span>
            <span>◆</span>
          </div>
          <h2 style="font-family: 'Sen', sans-serif !important; font-weight: 700 !important; letter-spacing: -0.01em; font-size: 34px; color: #37000A; margin: 8px 0 12px;">Pay Per Celebration. Zero Monthly Trap.</h2>
          <p style="font-size: 15px; color: #3E4E50; line-height: 1.6; margin: 0;">A simple, transparent pass designed for every family celebration. No monthly subscriptions, no recurring charges.</p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px; max-width: 860px; margin: 0 auto;">
          
          <!-- 1. Single Pass -->
          <div class="card-animate" style="background: #FFFFFF; border: 1.5px solid rgba(62, 78, 80, 0.18); border-radius: 24px; padding: 30px 28px; box-shadow: 0 14px 36px rgba(55,0,10,0.06); position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.25s ease, box-shadow 0.25s ease;" onmouseenter="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 20px 45px rgba(55,0,10,0.12)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 14px 36px rgba(55,0,10,0.06)';">
            <svg style="position: absolute; right: -15px; bottom: -15px; width: 140px; height: 140px; opacity: 0.04; pointer-events: none;" viewBox="0 0 24 24" fill="none" stroke="#37000A" stroke-width="1.5"><path d="M6 3h12M6 8h12M6 13l7 8M6 13h4a4 4 0 0 0 0-8"/></svg>
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <span style="font-size: 10px; font-weight: 700; color: #3E4E50; background: #F2EFEA; border: 1px solid rgba(62,78,80,0.2); padding: 4px 10px; border-radius: 6px; text-transform: uppercase;">SINGLE PASS</span>
                <span style="font-size: 10.5px; font-weight: 700; color: #FFFFFF; background: #37000A; padding: 4px 10px; border-radius: 6px;">Lifetime Access</span>
              </div>
              <h3 style="font-family: 'Sen', sans-serif !important; font-size: 22px; font-weight: 700; color: #37000A; margin: 0 0 6px;">Single Celebration Pass</h3>
              <div style="font-size: 12.5px; color: #FF1F3D; font-weight: 600; margin-bottom: 14px;">Complete single-event coverage</div>
              <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 18px;">
                <span style="font-size: 38px; font-weight: 800; color: #37000A; font-family: 'Sen', sans-serif;">₹49</span>
                <span style="font-size: 13.5px; color: #3E4E50; font-weight: 500;">/ one event (One-Time)</span>
              </div>
              <ul style="list-style: none; padding: 0; margin: 0 0 24px; display: flex; flex-direction: column; gap: 10px; font-size: 13.5px; color: #3E4E50;">
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: 900; background: #37000A; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> 1 Complete Celebration Event</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: 900; background: #37000A; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> Up to 500 Guests Logged</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: 900; background: #37000A; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> 2-Inch Thermal Slips & Excel Export</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: 900; background: #37000A; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> 100% Offline Ready & Private</li>
              </ul>
            </div>
            <button type="button" class="btn-tactile-primary" onclick="window.GVStore ? window.GVStore.purchasePass('single', 49) : navToView('login')" style="height: 38px !important; padding: 0 20px !important; border-radius: 999px !important; background: #9EE425 !important; color: #37000A !important; border: 1.5px solid #37000A !important; font-family: 'Sen', sans-serif !important; font-weight: 700 !important; font-size: 13.5px !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; width: 100% !important; max-width: 100% !important; box-shadow: 0 4px 14px rgba(158,228,37,0.4) !important;">
              <span>Get ₹49 Pass</span>
            </button>
          </div>

          <!-- 2. Family Pack -->
          <div class="card-animate" style="background: linear-gradient(155deg, #37000A 0%, #1A0005 100%); border: 2px solid #FF1F3D; border-radius: 24px; padding: 30px 28px; box-shadow: 0 20px 48px rgba(55,0,10,0.30); position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.25s ease, box-shadow 0.25s ease;" onmouseenter="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 26px 60px rgba(55,0,10,0.45)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 20px 48px rgba(55,0,10,0.30)';">
            <svg style="position: absolute; right: -15px; bottom: -15px; width: 140px; height: 140px; opacity: 0.08; pointer-events: none;" viewBox="0 0 24 24" fill="none" stroke="#9EE425" stroke-width="1.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <span style="font-size: 10px; font-weight: 700; color: #FFFFFF; background: rgba(255,255,255,0.15); border: 1px solid rgba(255,255,255,0.25); padding: 4px 10px; border-radius: 6px; text-transform: uppercase;">FAMILY PACK</span>
                <span style="font-size: 10.5px; font-weight: 800; color: #37000A; background: #9EE425; padding: 4px 10px; border-radius: 6px;">MOST POPULAR</span>
              </div>
              <h3 style="font-family: 'Sen', sans-serif !important; font-size: 22px; font-weight: 700; color: #FFFFFF; margin: 0 0 6px;">All Family Events Pack</h3>
              <div style="font-size: 12.5px; color: #9EE425; font-weight: 600; margin-bottom: 14px;">Unlimited celebrations • Lifetime access</div>
              <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 18px;">
                <span style="font-size: 38px; font-weight: 800; color: #FFFFFF; font-family: 'Sen', sans-serif;">₹99</span>
                <span style="font-size: 13.5px; color: #F2EFEA; opacity: 0.85;">/ all celebrations (Lifetime Access)</span>
              </div>
              <ul style="list-style: none; padding: 0; margin: 0 0 24px; display: flex; flex-direction: column; gap: 10px; font-size: 13.5px; color: #F2EFEA;">
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #37000A; font-weight: 900; background: #9EE425; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> Unlimited Auspicious Events</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #37000A; font-weight: 900; background: #9EE425; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> Unlimited Guests Logged</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #37000A; font-weight: 900; background: #9EE425; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> Multi-Device Family Sync</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #37000A; font-weight: 900; background: #9EE425; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> Return Shagun Reciprocity Engine</li>
                <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #37000A; font-weight: 900; background: #9EE425; width: 18px; height: 18px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px;">✓</span> Lifetime Cloud & Local Backup</li>
              </ul>
            </div>
            <button type="button" class="btn-tactile-primary" onclick="window.GVStore ? window.GVStore.purchasePass('family', 99) : navToView('login')" style="height: 38px !important; padding: 0 20px !important; border-radius: 999px !important; background: #9EE425 !important; color: #37000A !important; border: 1.5px solid #37000A !important; font-family: 'Sen', sans-serif !important; font-weight: 700 !important; font-size: 13.5px !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; width: 100% !important; max-width: 100% !important; box-shadow: 0 4px 14px rgba(158,228,37,0.5) !important;">
              <span>Get ₹99 Family Pack</span>
            </button>
          </div>

        </div>
      </section>"""

if old_pricing:
    html = html[:old_pricing.start(1)] + new_pricing_clean_html + "\n\n      " + html[old_pricing.start(2):]
    print("✅ 5. Updated Pricing section: Clean English, NO TELUGU!")
else:
    print("❌ Could not locate pricing section in index.html")


# -----------------------------------------------------------------------------
# 6. LOGIN PAGE: RESTORE BEFORE-PREVIOUS VERSION (from apply_login_reference_design.py)
# -----------------------------------------------------------------------------
old_login = re.search(r'(<main[^>]*id="view-login".*?)(<main[^>]*id="view-hub"|<main[^>]*id="view-app")', html, re.DOTALL)

new_login_before_previous = """  <main id="view-login" class="view-screen-pane">
      <!-- Back to Celebrations Button on Top -->
      <div class="login-topbar-wrapper" style="width: 100%; max-width: 1060px; margin: 0 auto 16px; display: flex; justify-content: flex-start;">
        <button type="button" class="login-back-clean-btn" onclick="navToView('landing')" style="border-radius: 999px; padding: 7px 18px; font-size: 12.5px; font-weight: 700; background: #FFFFFF; border: 1.5px solid rgba(62,78,80,0.25); color: #37000A; display: inline-flex; align-items: center; gap: 7px; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.04); font-family: 'Sen', sans-serif;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          <span>Back to Celebrations</span>
        </button>
      </div>

      <!-- Master Login Container (Before-Previous Version) -->
      <div class="login-master-frame" style="width: 100%; max-width: 1060px; margin: 0 auto; min-height: 580px; display: grid; grid-template-columns: 1.05fr 1fr; background: #FFFFFF; border-radius: 28px; border: 1.5px solid rgba(62, 78, 80, 0.18); box-shadow: 0 24px 60px -15px rgba(55, 0, 10, 0.10); overflow: hidden;">
        
        <!-- LEFT COLUMN: Brand Story & Arched Luxury GiftBox Showcase -->
        <div class="login-master-left" style="background: linear-gradient(145deg, #FAF6F0 0%, #F5EFE6 100%); padding: 36px 36px 30px; display: flex; flex-direction: column; justify-content: space-between; border-right: 1px solid rgba(62,78,80,0.12);">
          <div>
            <!-- Brand Lockup -->
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 14px;">
              <div style="width: 36px; height: 36px; border-radius: 10px; background: linear-gradient(135deg, #FF1F3D 0%, #37000A 100%); display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(255, 31, 61, 0.25);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M4 10C4 8.89543 4.89543 8 6 8H18C19.1046 8 20 8.89543 20 10V18C20 19.6569 18.6569 21 17 21H7C5.34315 21 4 19.6569 4 18V10Z" fill="#9EE425"/>
                  <path d="M12 8V21" stroke="#37000A" stroke-width="1.6" stroke-linecap="round"/>
                  <path d="M4 13.5H20" stroke="#37000A" stroke-width="1.6" stroke-linecap="round"/>
                </svg>
              </div>
              <div style="font-family: 'Sen', sans-serif; font-size: 20px; font-weight: 700; color: #37000A;">Gift<span style="color: #FF1F3D;">Vault</span></div>
            </div>

            <!-- Headline -->
            <h2 style="font-family: 'Sen', sans-serif !important; font-size: 26px; font-weight: 700; color: #37000A; line-height: 1.25; margin: 0 0 8px 0;">Because every gift<br>has a story.</h2>
            <p style="font-size: 13px; color: #3E4E50; line-height: 1.55; margin: 0 0 16px;">Sign in to relive, organise, and keep your sacred family celebration records safe.</p>
          </div>

          <!-- Jharokha Arched Frame with Ivory & Gold Shagun Gift Box -->
          <div style="position: relative; width: 100%; height: 230px; border-radius: 20px; overflow: hidden; border: 1.5px solid rgba(62,78,80,0.15); box-shadow: 0 10px 24px rgba(55,0,10,0.08); margin: 10px 0;">
            <img src="assets/images/giftvault_login_showcase_reference.jpg" alt="GiftVault Royal Shagun Gift Box" style="width: 100%; height: 100%; object-fit: cover;">
            <div style="position: absolute; bottom: 12px; left: 12px; right: 12px; background: rgba(55, 0, 10, 0.85); backdrop-filter: blur(8px); padding: 8px 12px; border-radius: 10px; font-size: 11px; font-weight: 600; color: #FFFFFF; text-align: center; border: 1px solid rgba(158,228,37,0.4);">
              ✨ Every Gift. Every Occasion. All in One Place.
            </div>
          </div>

          <!-- Bottom: 3 Value Pillars -->
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
            <div style="background: #FFFFFF; border: 1px solid rgba(62,78,80,0.15); border-radius: 10px; padding: 8px; text-align: center; font-size: 11px; font-weight: 700; color: #37000A; font-family: 'Sen', sans-serif;">
              Track Gifts
            </div>
            <div style="background: #FFFFFF; border: 1px solid rgba(62,78,80,0.15); border-radius: 10px; padding: 8px; text-align: center; font-size: 11px; font-weight: 700; color: #37000A; font-family: 'Sen', sans-serif;">
              Family Sync
            </div>
            <div style="background: #FFFFFF; border: 1px solid rgba(62,78,80,0.15); border-radius: 10px; padding: 8px; text-align: center; font-size: 11px; font-weight: 700; color: #37000A; font-family: 'Sen', sans-serif;">
              100% Private
            </div>
          </div>
        </div>

        <!-- RIGHT COLUMN: Authentication Card with Lemon Green Button -->
        <div style="padding: 44px 40px; display: flex; flex-direction: column; justify-content: center; background: #FFFFFF;">
          <div style="margin-bottom: 24px;">
            <span style="font-size: 10.5px; font-weight: 800; color: #FF1F3D; letter-spacing: 0.12em; text-transform: uppercase;">WELCOME TO SACRED LEDGER</span>
            <h3 style="font-family: 'Sen', sans-serif !important; font-size: 24px; font-weight: 700; color: #37000A; margin: 4px 0 6px;">Sign In to Your Vault</h3>
            <p style="font-size: 13px; color: #3E4E50; margin: 0;">Enter your mobile number to receive a secure OTP</p>
          </div>

          <form onsubmit="event.preventDefault(); handleLoginSubmit();" style="display: flex; flex-direction: column; gap: 18px;">
            <div>
              <label for="login-phone" style="display: block; font-size: 12px; font-weight: 700; color: #37000A; margin-bottom: 6px; font-family: 'Sen', sans-serif;">Mobile Number</label>
              <div style="display: flex; align-items: center; border: 1.5px solid rgba(62, 78, 80, 0.25); border-radius: 999px; padding: 0 16px; background: #FAF8F5;">
                <span style="font-size: 13.5px; font-weight: 700; color: #37000A; padding-right: 8px; border-right: 1px solid rgba(62,78,80,0.2);">+91</span>
                <input type="tel" id="login-phone" placeholder="Enter 10-digit mobile number" maxlength="10" value="9876543210" style="border: none; background: transparent; padding: 10px 12px; font-size: 13.5px; font-weight: 600; color: #37000A; width: 100%; outline: none; font-family: 'Sen', sans-serif;" required>
              </div>
            </div>

            <div>
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <label style="font-size: 12px; font-weight: 700; color: #37000A; font-family: 'Sen', sans-serif;">6-Digit OTP</label>
                <span style="font-size: 11px; color: #FF1F3D; font-weight: 600; cursor: pointer;">Resend OTP</span>
              </div>
              <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 8px;">
                <input type="text" id="otp-1" class="otp-box" maxlength="1" value="1" style="height: 44px; text-align: center; font-size: 16px; font-weight: 700; border: 1.5px solid rgba(62,78,80,0.25); border-radius: 12px; background: #FAF8F5; color: #37000A; outline: none;">
                <input type="text" id="otp-2" class="otp-box" maxlength="1" value="2" style="height: 44px; text-align: center; font-size: 16px; font-weight: 700; border: 1.5px solid rgba(62,78,80,0.25); border-radius: 12px; background: #FAF8F5; color: #37000A; outline: none;">
                <input type="text" id="otp-3" class="otp-box" maxlength="1" value="3" style="height: 44px; text-align: center; font-size: 16px; font-weight: 700; border: 1.5px solid rgba(62,78,80,0.25); border-radius: 12px; background: #FAF8F5; color: #37000A; outline: none;">
                <input type="text" id="otp-4" class="otp-box" maxlength="1" value="4" style="height: 44px; text-align: center; font-size: 16px; font-weight: 700; border: 1.5px solid rgba(62,78,80,0.25); border-radius: 12px; background: #FAF8F5; color: #37000A; outline: none;">
                <input type="text" id="otp-5" class="otp-box" maxlength="1" value="5" style="height: 44px; text-align: center; font-size: 16px; font-weight: 700; border: 1.5px solid rgba(62,78,80,0.25); border-radius: 12px; background: #FAF8F5; color: #37000A; outline: none;">
                <input type="text" id="otp-6" class="otp-box" maxlength="1" value="6" style="height: 44px; text-align: center; font-size: 16px; font-weight: 700; border: 1.5px solid rgba(62,78,80,0.25); border-radius: 12px; background: #FAF8F5; color: #37000A; outline: none;">
              </div>
            </div>

            <button type="submit" id="btn-login-submit" class="btn-tactile-primary btn-enter-vault" style="height: 40px !important; border-radius: 999px !important; background: #9EE425 !important; color: #37000A !important; border: 1.5px solid #37000A !important; font-family: 'Sen', sans-serif !important; font-weight: 700 !important; font-size: 14px !important; display: flex !important; align-items: center !important; justify-content: center !important; gap: 8px !important; box-shadow: 0 4px 14px rgba(158,228,37,0.4) !important; cursor: pointer; margin-top: 8px;">
              <span>Enter Vault →</span>
            </button>
          </form>

          <div style="margin-top: 20px; text-align: center;">
            <button type="button" id="btn-guest-demo" onclick="enterGuestDemo()" style="background: none; border: none; font-size: 12.5px; font-weight: 700; color: #FF1F3D; cursor: pointer; text-decoration: underline; font-family: 'Sen', sans-serif;">
              ⚡ Explore as Guest Demo (Immediate Access)
            </button>
          </div>
        </div>

      </div>
  </main>"""

if old_login:
    html = html[:old_login.start(1)] + new_login_before_previous + "\n\n  " + html[old_login.start(2):]
    print("✅ 6. Login View restored to before-previous version!")
else:
    print("❌ Could not locate view-login in index.html")

# Write updated index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished applying all exact user requests to index.html!")
