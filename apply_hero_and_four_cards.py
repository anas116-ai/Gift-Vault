import re

# New Hero Right-side Showcase HTML
new_hero_right_showcase = '''        <!-- Right: Ultra Clean Creative Gifting Vault Showcase (No Messy Lines, Photorealistic Luxury) -->
        <div class="hero-showcase-container hero-product-laptop-card" style="position: relative; max-width: 480px; width: 100%; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
          
          <div style="position: relative; width: 100%; border-radius: 28px; overflow: hidden; background: #FFFFFF; border: 1.5px solid rgba(62, 78, 80, 0.18); box-shadow: 0 24px 60px -12px rgba(55,0,10,0.12); cursor: pointer; transition: transform 0.35s ease, box-shadow 0.35s ease;" onclick="navToView('login')" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 30px 70px -10px rgba(55,0,10,0.18)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 24px 60px -12px rgba(55,0,10,0.12)';">
            
            <!-- Ultra High-Resolution Photorealistic Hero Image -->
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
        </div>'''

# New 4 Distinct Cards Strip HTML (Using the 5 colors distinctly with luxury bespoke SVG icons)
new_four_cards_strip = '''      <!-- ==================================================================
           2. FOUR CORE FEATURE CARDS STRIP (Beside/Under Hero - Distinct Colors & Custom Icons)
           ================================================================== -->
      <div class="hero-four-cards-strip" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin: 10px 0 44px;">
        
        <!-- Card 1: Rich Mahogany & Strawberry Red Luxury (#37000A + #FF1F3D) -->
        <div style="background: linear-gradient(145deg, #37000A 0%, #200006 100%); border: 1.5px solid rgba(255,31,61,0.45); border-radius: 16px; padding: 20px 18px; box-shadow: 0 10px 28px rgba(55,0,10,0.22); transition: transform 0.25s ease, box-shadow 0.25s ease; display: flex; flex-direction: column; justify-content: space-between;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 36px rgba(55,0,10,0.35)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 28px rgba(55,0,10,0.22)';">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
              <div style="width: 42px; height: 42px; border-radius: 12px; background: rgba(255,31,61,0.2); border: 1.5px solid #FF1F3D; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px rgba(255,31,61,0.35);">
                <!-- Luxury Gift Vault Chest SVG -->
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
            <div style="font-size: 12.5px; color: rgba(242, 239, 234, 0.82); line-height: 1.45;">Cash, Gold, Silver & custom blessings logged in seconds.</div>
          </div>
          <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 11px; font-weight: 700; color: #FF7084;">Cash • Gold • Silver</span>
            <span style="font-size: 11px; color: #F2EFEA; opacity: 0.6;">01</span>
          </div>
        </div>

        <!-- Card 2: Warm Parchment & Iron Grey Deep Tradition (#F2EFEA + #3E4E50) -->
        <div style="background: linear-gradient(145deg, #FAF8F5 0%, #EFEBE4 100%); border: 1.5px solid #3E4E50; border-radius: 16px; padding: 20px 18px; box-shadow: 0 10px 24px rgba(62,78,80,0.1); transition: transform 0.25s ease, box-shadow 0.25s ease; display: flex; flex-direction: column; justify-content: space-between;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 34px rgba(62,78,80,0.18)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 24px rgba(62,78,80,0.1)';">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
              <div style="width: 42px; height: 42px; border-radius: 12px; background: #3E4E50; border: 1.5px solid #37000A; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px rgba(62,78,80,0.25);">
                <!-- Sacred Mandap & Pillars SVG -->
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F2EFEA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 21h18"/>
                  <path d="M5 21V10l7-6 7 6v11"/>
                  <path d="M9 21v-5a3 3 0 0 1 6 0v5"/>
                  <circle cx="12" cy="7" r="1" fill="#F2EFEA"/>
                </svg>
              </div>
              <span style="font-size: 10px; font-weight: 800; color: #37000A; background: #FFFFFF; border: 1px solid rgba(62,78,80,0.25); padding: 3px 8px; border-radius: 20px; letter-spacing: 0.05em;">◆ EVENTS</span>
            </div>
            <div style="font-family: 'Sen', sans-serif; font-size: 16px; font-weight: 700; color: #37000A; margin-bottom: 6px;">Manage Family Events</div>
            <div style="font-size: 12.5px; color: #3E4E50; line-height: 1.45;">Weddings, Griha Pravesham & milestone gatherings.</div>
          </div>
          <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(62,78,80,0.14); display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 11px; font-weight: 700; color: #3E4E50;">Weddings • Milestones</span>
            <span style="font-size: 11px; color: #3E4E50; opacity: 0.6;">02</span>
          </div>
        </div>

        <!-- Card 3: Radiant Strawberry Red Blush & Memories (#FF1F3D + #FFFFFF) -->
        <div style="background: linear-gradient(145deg, #FFF6F7 0%, #FFE9EC 100%); border: 1.5px solid #FF1F3D; border-radius: 16px; padding: 20px 18px; box-shadow: 0 10px 24px rgba(255,31,61,0.12); transition: transform 0.25s ease, box-shadow 0.25s ease; display: flex; flex-direction: column; justify-content: space-between;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 34px rgba(255,31,61,0.22)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 24px rgba(255,31,61,0.12)';">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
              <div style="width: 42px; height: 42px; border-radius: 12px; background: #FF1F3D; border: 1.5px solid #FFFFFF; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px rgba(255,31,61,0.35);">
                <!-- Sacred Heart Memoir SVG -->
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
                </svg>
              </div>
              <span style="font-size: 10px; font-weight: 800; color: #FF1F3D; background: rgba(255,31,61,0.1); border: 1px solid rgba(255,31,61,0.3); padding: 3px 8px; border-radius: 20px; letter-spacing: 0.05em;">♥ MEMORIES</span>
            </div>
            <div style="font-family: 'Sen', sans-serif; font-size: 16px; font-weight: 700; color: #37000A; margin-bottom: 6px;">Keep Precious Memories</div>
            <div style="font-size: 12.5px; color: #3E4E50; line-height: 1.45;">Special moments, return gift notes & auspicious memories.</div>
          </div>
          <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(255,31,61,0.15); display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 11px; font-weight: 700; color: #FF1F3D;">Photos • Return Gifts</span>
            <span style="font-size: 11px; color: #FF1F3D; opacity: 0.7;">03</span>
          </div>
        </div>

        <!-- Card 4: Energetic Slime Lime & Obsidian Intelligence (#9EE425 + #37000A) -->
        <div style="background: linear-gradient(145deg, #F5FBEA 0%, #E7F6CD 100%); border: 1.5px solid #9EE425; border-radius: 16px; padding: 20px 18px; box-shadow: 0 10px 24px rgba(158,228,37,0.18); transition: transform 0.25s ease, box-shadow 0.25s ease; display: flex; flex-direction: column; justify-content: space-between;" onmouseenter="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 16px 34px rgba(158,228,37,0.28)';" onmouseleave="this.style.transform='translateY(0)'; this.style.boxShadow='0 10px 24px rgba(158,228,37,0.18)';">
          <div>
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px;">
              <div style="width: 42px; height: 42px; border-radius: 12px; background: #9EE425; border: 1.5px solid #37000A; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 14px rgba(158,228,37,0.35);">
                <!-- Analytics Sheet & Thermal Slip SVG -->
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#37000A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                  <polyline points="14 2 14 8 20 8"/>
                  <line x1="16" y1="13" x2="8" y2="13"/>
                  <line x1="16" y1="17" x2="8" y2="17"/>
                  <polyline points="10 9 9 9 8 9"/>
                </svg>
              </div>
              <span style="font-size: 10px; font-weight: 800; color: #37000A; background: #9EE425; border: 1px solid #37000A; padding: 3px 8px; border-radius: 20px; letter-spacing: 0.05em;">⚡ REPORTS</span>
            </div>
            <div style="font-family: 'Sen', sans-serif; font-size: 16px; font-weight: 700; color: #37000A; margin-bottom: 6px;">Get Detailed Reports</div>
            <div style="font-size: 12.5px; color: #3E4E50; line-height: 1.45;">Instant Excel sheets, filtered PDFs & 2-inch thermal slips.</div>
          </div>
          <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(55,0,10,0.12); display: flex; align-items: center; justify-content: space-between;">
            <span style="font-size: 11px; font-weight: 800; color: #37000A;">Excel • PDF • 2" Slips</span>
            <span style="font-size: 11px; color: #37000A; opacity: 0.7;">04</span>
          </div>
        </div>

      </div>'''

files_to_update = [
    'index.html',
    'web_preview/index.html',
    'build/web/index.html',
    'web/index.html'
]

hero_pattern = re.compile(
    r'<div class="hero-showcase-container hero-product-laptop-card".*?</section>',
    re.DOTALL
)

four_cards_pattern = re.compile(
    r'<!-- ==================================================================\s+2\. FOUR CORE FEATURE CARDS STRIP.*?</div>\s+</div>',
    re.DOTALL
)

for file_path in files_to_update:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace hero right-side showcase
    # Find start of hero-showcase-container up to </section>
    content, count_hero = hero_pattern.subn(new_hero_right_showcase + '\n      </section>', content)

    # Replace the 4 cards strip
    content, count_cards = four_cards_pattern.subn(new_four_cards_strip, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file_path}: hero={count_hero}, cards={count_cards}")
