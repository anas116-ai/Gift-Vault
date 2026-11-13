import re
from bs4 import BeautifulSoup

def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # =========================================================================
    # 1. HERO 4 CARDS STRIP (Track Gifts, Manage Family Events, Keep Memories, Detailed Reports)
    # =========================================================================
    hero_strip_html = """
    <div class="hero-four-cards-strip" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin: 28px 0 44px;">
      <!-- Card 1 -->
      <div style="background: #FFFFFF; border: 1.5px solid rgba(62,78,80,0.18); border-radius: 14px; padding: 18px 16px; box-shadow: 0 4px 16px rgba(55,0,10,0.04); transition: transform 0.25s ease;" onmouseenter="this.style.transform='translateY(-3px)'" onmouseleave="this.style.transform='translateY(0)'">
        <div style="width: 38px; height: 38px; border-radius: 10px; background: rgba(255,31,61,0.08); border: 1px solid rgba(255,31,61,0.22); display: flex; align-items: center; justify-content: center; margin-bottom: 12px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#FF1F3D" stroke-width="2"><rect x="3" y="8" width="18" height="13" rx="2"/><path d="M12 8V21"/><path d="M3 13.5H21"/><circle cx="12" cy="5.5" r="2.5"/></svg>
        </div>
        <div style="font-family: 'Sen', sans-serif; font-size: 15px; font-weight: 700; color: #37000A; margin-bottom: 4px;">Track Gifts & Shagun</div>
        <div style="font-size: 12px; color: #3E4E50; line-height: 1.4;">Cash, Gold, Silver & custom blessings logged in seconds.</div>
      </div>
      <!-- Card 2 -->
      <div style="background: #FFFFFF; border: 1.5px solid rgba(62,78,80,0.18); border-radius: 14px; padding: 18px 16px; box-shadow: 0 4px 16px rgba(55,0,10,0.04); transition: transform 0.25s ease;" onmouseenter="this.style.transform='translateY(-3px)'" onmouseleave="this.style.transform='translateY(0)'">
        <div style="width: 38px; height: 38px; border-radius: 10px; background: rgba(55,0,10,0.08); border: 1px solid rgba(55,0,10,0.22); display: flex; align-items: center; justify-content: center; margin-bottom: 12px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#37000A" stroke-width="2"><path d="M3 21h18M5 21V10l7-5 7 5v11M9 21v-6h6v6"/></svg>
        </div>
        <div style="font-family: 'Sen', sans-serif; font-size: 15px; font-weight: 700; color: #37000A; margin-bottom: 4px;">Manage Family Events</div>
        <div style="font-size: 12px; color: #3E4E50; line-height: 1.4;">Weddings, Griha Pravesham & milestone gatherings.</div>
      </div>
      <!-- Card 3 -->
      <div style="background: #FFFFFF; border: 1.5px solid rgba(62,78,80,0.18); border-radius: 14px; padding: 18px 16px; box-shadow: 0 4px 16px rgba(55,0,10,0.04); transition: transform 0.25s ease;" onmouseenter="this.style.transform='translateY(-3px)'" onmouseleave="this.style.transform='translateY(0)'">
        <div style="width: 38px; height: 38px; border-radius: 10px; background: rgba(158,228,37,0.15); border: 1px solid rgba(158,228,37,0.4); display: flex; align-items: center; justify-content: center; margin-bottom: 12px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#37000A" stroke-width="2"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
        </div>
        <div style="font-family: 'Sen', sans-serif; font-size: 15px; font-weight: 700; color: #37000A; margin-bottom: 4px;">Keep Precious Memories</div>
        <div style="font-size: 12px; color: #3E4E50; line-height: 1.4;">Special moments, return gift notes & auspicious memories.</div>
      </div>
      <!-- Card 4 -->
      <div style="background: #FFFFFF; border: 1.5px solid rgba(62,78,80,0.18); border-radius: 14px; padding: 18px 16px; box-shadow: 0 4px 16px rgba(55,0,10,0.04); transition: transform 0.25s ease;" onmouseenter="this.style.transform='translateY(-3px)'" onmouseleave="this.style.transform='translateY(0)'">
        <div style="width: 38px; height: 38px; border-radius: 10px; background: rgba(62,78,80,0.08); border: 1px solid rgba(62,78,80,0.22); display: flex; align-items: center; justify-content: center; margin-bottom: 12px;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#3E4E50" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
        </div>
        <div style="font-family: 'Sen', sans-serif; font-size: 15px; font-weight: 700; color: #37000A; margin-bottom: 4px;">Get Detailed Reports</div>
        <div style="font-size: 12px; color: #3E4E50; line-height: 1.4;">Instant Excel sheets, filtered PDFs & 2-inch thermal slips.</div>
      </div>
    </div>
    """

    # Check if hero section exists and insert strip right after it
    hero_section = soup.find('section', class_='hero-cinematic-grid')
    if hero_section:
        # Check if existing strip is present
        existing_strip = soup.find('div', class_='hero-four-cards-strip')
        if not existing_strip:
            hero_section.insert_after(BeautifulSoup(hero_strip_html, 'html.parser'))

    # =========================================================================
    # 2. "BUILT FOR FAMILIES" SECTION: REPLACE STOCK IMAGE WITH BESPOKE CODE GRAPHIC
    # =========================================================================
    family_section = soup.find('section', class_='hero-ref1-family-section')
    if family_section:
        bespoke_code_graphic_html = """
        <div class="family-heritage-code-graphic" style="position: relative; width: 100%; height: 320px; background: radial-gradient(circle at center, #FFFFFF 0%, #F2EFEA 100%); border: 1.5px solid rgba(55,0,10,0.15); border-radius: 16px; overflow: hidden; display: flex; align-items: center; justify-content: center; box-shadow: 0 14px 34px -10px rgba(55,0,10,0.08);">
          <!-- Auspicious Sacred Mandala Pattern SVG -->
          <svg style="position: absolute; width: 280px; height: 280px; opacity: 0.12;" viewBox="0 0 200 200">
            <circle cx="100" cy="100" r="90" fill="none" stroke="#37000A" stroke-width="1.5" stroke-dasharray="4 4"/>
            <circle cx="100" cy="100" r="70" fill="none" stroke="#FF1F3D" stroke-width="1.5"/>
            <circle cx="100" cy="100" r="50" fill="none" stroke="#9EE425" stroke-width="1.5"/>
            <polygon points="100,15 125,80 190,100 125,120 100,185 75,120 10,100 75,80" fill="none" stroke="#37000A" stroke-width="1.2"/>
          </svg>
          
          <!-- Central Sacred Shagun Kalash/Diya Emblem -->
          <div style="position: relative; z-index: 2; width: 78px; height: 78px; border-radius: 50%; background: #37000A; border: 2.5px solid #FF1F3D; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 8px 24px rgba(255,31,61,0.35);">
            <svg width="34" height="34" viewBox="0 0 24 24" fill="none">
              <path d="M12 2C12 2 7 7 7 11C7 13.76 9.24 16 12 16C14.76 16 17 13.76 17 11C17 7 12 2 12 2Z" fill="#9EE425"/>
              <path d="M12 6C12 6 9 9.5 9 12C9 13.66 10.34 15 12 15C13.66 15 15 13.66 15 12C15 9.5 12 6 12 6Z" fill="#FF1F3D"/>
              <rect x="4" y="16" width="16" height="4" rx="2" fill="#F2EFEA"/>
            </svg>
            <span style="font-family: 'Sen', sans-serif; font-size: 8px; font-weight: 700; color: #9EE425; letter-spacing: 0.1em; margin-top: 2px;">VAULT</span>
          </div>

          <!-- Floating Kinship Nodes -->
          <!-- Top Node: Grandparents -->
          <div style="position: absolute; top: 22px; left: 40px; background: #FFFFFF; border: 1.5px solid #37000A; border-radius: 10px; padding: 6px 12px; display: flex; align-items: center; gap: 8px; box-shadow: 0 6px 16px rgba(0,0,0,0.06); z-index: 3;">
            <div style="width: 20px; height: 20px; border-radius: 50%; background: #FF1F3D; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; font-family: 'Absans', sans-serif;">త</div>
            <div style="font-family: 'Sen', sans-serif; font-size: 11px; font-weight: 700; color: #37000A;">తాతయ్య & బామ్మ <span style="font-size: 9px; color: #3E4E50; display: block; font-weight: 400;">Senior Blessings</span></div>
          </div>

          <!-- Right Node: Active Shagun Pill -->
          <div style="position: absolute; top: 40px; right: 28px; background: #37000A; border: 1.5px solid #9EE425; border-radius: 10px; padding: 7px 14px; box-shadow: 0 8px 20px rgba(55,0,10,0.25); z-index: 3;">
            <div style="display: flex; align-items: center; gap: 6px;">
              <span style="width: 7px; height: 7px; border-radius: 50%; background: #9EE425; display: inline-block;"></span>
              <span style="font-family: 'Sen', sans-serif; font-size: 12px; font-weight: 700; color: #9EE425;">+₹ 25,116</span>
            </div>
            <span style="font-size: 9px; color: #F2EFEA; display: block; font-family: 'Absans', sans-serif;">VERIFIED SHAGUN</span>
          </div>

          <!-- Bottom Left: 100% Offline Vault Badge -->
          <div style="position: absolute; bottom: 26px; left: 32px; background: #FFFFFF; border: 1.5px solid #3E4E50; border-radius: 9px; padding: 6px 12px; display: flex; align-items: center; gap: 7px; box-shadow: 0 6px 16px rgba(0,0,0,0.06); z-index: 3;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#FF1F3D" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            <span style="font-family: 'Sen', sans-serif; font-size: 11px; font-weight: 700; color: #37000A;">100% Offline Ledger</span>
          </div>

          <!-- Bottom Right: Core Family -->
          <div style="position: absolute; bottom: 22px; right: 40px; background: #FFFFFF; border: 1.5px solid #FF1F3D; border-radius: 10px; padding: 6px 12px; display: flex; align-items: center; gap: 8px; box-shadow: 0 6px 16px rgba(0,0,0,0.06); z-index: 3;">
            <div style="width: 20px; height: 20px; border-radius: 50%; background: #9EE425; color: #37000A; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; font-family: 'Absans', sans-serif;">అ</div>
            <div style="font-family: 'Sen', sans-serif; font-size: 11px; font-weight: 700; color: #37000A;">అమ్మా & నాన్న <span style="font-size: 9px; color: #FF1F3D; display: block; font-weight: 700;">Multi-Desk Synced</span></div>
          </div>
        </div>
        """
        # Replace the left image div with bespoke code graphic
        img_container = family_section.find('div')
        if img_container and img_container.find('img'):
            img_container.replace_with(BeautifulSoup(bespoke_code_graphic_html, 'html.parser'))

    # =========================================================================
    # 3. REMOVE BOTTOM TRUST BADGE PILL ("Available on 💻 🍎 🤖 ...")
    # =========================================================================
    for div in soup.find_all('div'):
        if div.string and 'Available on' in div.string:
            div.decompose()
        elif 'Available on' in div.get_text():
            if '💻' in div.get_text() or '🍎' in div.get_text():
                div.decompose()

    # =========================================================================
    # 4. CELEBRATIONS SECTION (#culture): 3 REAL HIGH-CREATIVE IMAGES
    # =========================================================================
    culture_section = soup.find(id='culture')
    if culture_section:
        culture_cards_html = """
        <section id="culture" style="margin-bottom: 60px;">
          <div style="text-align: center; max-width: 650px; margin: 0 auto 36px;">
            <div style="font-size: 11px; font-weight: 800; color: #FF1F3D; letter-spacing: 0.15em; text-transform: uppercase; font-family: 'Absans', sans-serif;">MADE FOR INDIAN FAMILIES</div>
            <h2 style="font-family: 'Sen', sans-serif !important; font-weight: 400 !important; letter-spacing: -0.01em; font-size: 34px; color: #37000A; margin-top: 8px;">Celebrations Supported Across India</h2>
            <p style="font-size: 14.5px; color: #3E4E50; line-height: 1.6; margin-top: 8px;">GiftVault is tailored for the rituals, contributions, and shagun traditions of your family celebrations.</p>
          </div>
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;">
            <!-- 1. Weddings -->
            <div class="card-culture-celebration" style="background: #FFFFFF; border: 1.5px solid rgba(62,78,80,0.18); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 28px rgba(55,0,10,0.06); transition: transform 0.3s ease;" onmouseenter="this.style.transform='translateY(-4px)'" onmouseleave="this.style.transform='translateY(0)'">
              <div style="position: relative; height: 180px; overflow: hidden;">
                <img src="assets/images/celebration_wedding_mandap.jpg" alt="Auspicious Wedding Mandap" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
                <div style="position: absolute; top: 12px; left: 12px; background: rgba(55,0,10,0.85); backdrop-filter: blur(8px); border: 1px solid #FF1F3D; border-radius: 6px; padding: 4px 10px; font-size: 10px; font-weight: 700; color: #F2EFEA; font-family: 'Absans', sans-serif; letter-spacing: 0.08em; text-transform: uppercase;">AUSPICIOUS UNION</div>
              </div>
              <div style="padding: 20px;">
                <h3 style="font-family: 'Sen', sans-serif !important; font-size: 20px; font-weight: 400 !important; color: #37000A; margin: 0 0 8px;">Weddings (వివాహం)</h3>
                <p style="font-size: 13.5px; color: #3E4E50; line-height: 1.6; margin: 0;">Multi-day ceremonies, bride & groom dual reception counters, shagun envelopes with Lucky Coin auto-add, and instant thermal acknowledgment slips.</p>
              </div>
            </div>
            <!-- 2. Housewarming -->
            <div class="card-culture-celebration" style="background: #FFFFFF; border: 1.5px solid rgba(62,78,80,0.18); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 28px rgba(55,0,10,0.06); transition: transform 0.3s ease;" onmouseenter="this.style.transform='translateY(-4px)'" onmouseleave="this.style.transform='translateY(0)'">
              <div style="position: relative; height: 180px; overflow: hidden;">
                <img src="assets/images/celebration_griha_pravesham.jpg" alt="Luxury Housewarming Ceremony" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
                <div style="position: absolute; top: 12px; left: 12px; background: rgba(55,0,10,0.85); backdrop-filter: blur(8px); border: 1px solid #9EE425; border-radius: 6px; padding: 4px 10px; font-size: 10px; font-weight: 700; color: #9EE425; font-family: 'Absans', sans-serif; letter-spacing: 0.08em; text-transform: uppercase;">GRIHA PRAVESHAM</div>
              </div>
              <div style="padding: 20px;">
                <h3 style="font-family: 'Sen', sans-serif !important; font-size: 20px; font-weight: 400 !important; color: #37000A; margin: 0 0 8px;">Housewarming (గృహప్రవేశం)</h3>
                <p style="font-size: 13.5px; color: #3E4E50; line-height: 1.6; margin: 0;">Track brass lamps, silver idols, home contributions, and cash blessings with hometown tagging, relatives indexing, and family-wise totals.</p>
              </div>
            </div>
            <!-- 3. Silver Jubilee -->
            <div class="card-culture-celebration" style="background: #FFFFFF; border: 1.5px solid rgba(62,78,80,0.18); border-radius: 16px; overflow: hidden; box-shadow: 0 10px 28px rgba(55,0,10,0.06); transition: transform 0.3s ease;" onmouseenter="this.style.transform='translateY(-4px)'" onmouseleave="this.style.transform='translateY(0)'">
              <div style="position: relative; height: 180px; overflow: hidden;">
                <img src="assets/images/celebration_silver_jubilee.jpg" alt="Silver Jubilee Celebration Stage" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
                <div style="position: absolute; top: 12px; left: 12px; background: rgba(55,0,10,0.85); backdrop-filter: blur(8px); border: 1px solid #FF1F3D; border-radius: 6px; padding: 4px 10px; font-size: 10px; font-weight: 700; color: #F2EFEA; font-family: 'Absans', sans-serif; letter-spacing: 0.08em; text-transform: uppercase;">MILESTONE CELEBRATION</div>
              </div>
              <div style="padding: 20px;">
                <h3 style="font-family: 'Sen', sans-serif !important; font-size: 20px; font-weight: 400 !important; color: #37000A; margin: 0 0 8px;">Silver Jubilee (రజతోత్సవం)</h3>
                <p style="font-size: 13.5px; color: #3E4E50; line-height: 1.6; margin: 0;">25 years of togetherness: preserve family blessings, guest lists, return gift registers, and export full archival records to Excel & PDF.</p>
              </div>
            </div>
          </div>
        </section>
        """
        culture_section.replace_with(BeautifulSoup(culture_cards_html, 'html.parser'))

    # =========================================================================
    # 5. PRICING SECTION (#pricing): INCREASE SPACING (gap: 52px), DECREASE LENGTH, CREATIVE WATERMARK
    # =========================================================================
    pricing_section = soup.find(id='pricing')
    if pricing_section:
        pricing_html = """
        <section id="pricing" style="margin-bottom: 60px;">
          <div style="text-align: center; max-width: 600px; margin: 0 auto 36px;">
            <div style="font-size: 11px; font-weight: 800; color: #FF1F3D; letter-spacing: 0.15em; text-transform: uppercase; font-family: 'Absans', sans-serif;">TRANSPARENT PASS PRICING</div>
            <h2 style="font-family: 'Sen', sans-serif !important; font-weight: 400 !important; letter-spacing: -0.01em; font-size: 32px; color: #37000A; margin-top: 6px;">Pay Per Celebration. Zero Monthly Trap.</h2>
            <p style="font-size: 14px; color: #3E4E50;">A clean, affordable pass designed for every sacred celebration.</p>
          </div>
          <!-- Grid with generous 52px gap, compact height, and bespoke watermark -->
          <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 52px; max-width: 860px; margin: 0 auto;">
            <!-- Plan 1: Single Celebration Pass -->
            <div style="background: #FFFFFF; border: 1.5px solid rgba(62,78,80,0.2); border-radius: 18px; padding: 26px 28px; position: relative; overflow: hidden; box-shadow: 0 12px 30px rgba(55,0,10,0.05); display: flex; flex-direction: column; justify-content: space-between;">
              <!-- Subtle Auspicious Currency Watermark -->
              <svg style="position: absolute; right: -20px; bottom: -20px; width: 140px; height: 140px; opacity: 0.05; pointer-events: none;" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="45" fill="none" stroke="#37000A" stroke-width="2"/>
                <text x="50" y="65" font-size="44" text-anchor="middle" fill="#37000A" font-weight="bold">₹</text>
              </svg>
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                  <span style="font-size: 11px; font-weight: 800; color: #3E4E50; background: #F2EFEA; border: 1px solid rgba(62,78,80,0.2); padding: 4px 10px; border-radius: 6px; font-family: 'Absans', sans-serif;">SINGLE PASS</span>
                  <span style="font-size: 12px; font-weight: 600; color: #9EE425; background: #37000A; padding: 3px 8px; border-radius: 4px;">Lifetime Access</span>
                </div>
                <h3 style="font-family: 'Sen', sans-serif !important; font-size: 20px; font-weight: 400 !important; color: #37000A; margin: 0 0 8px;">Single Celebration Pass</h3>
                <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 14px;">
                  <span style="font-size: 32px; font-weight: 700; color: #37000A; font-family: 'Sen', sans-serif;">₹49</span>
                  <span style="font-size: 13px; color: #3E4E50;">/ one event</span>
                </div>
                <ul style="list-style: none; padding: 0; margin: 0 0 20px; display: flex; flex-direction: column; gap: 8px; font-size: 13px; color: #3E4E50;">
                  <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: bold;">✔</span> 1 Complete Celebration Event</li>
                  <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: bold;">✔</span> Up to 500 Guests Logged</li>
                  <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: bold;">✔</span> 2-Inch Thermal Slips & Excel Export</li>
                </ul>
              </div>
              <button type="button" class="btn-tactile-primary" onclick="window.GVStore ? window.GVStore.purchasePass('single', 49) : navToView('login')" style="width: 140px !important;">
                <span>Get ₹49 Pass</span>
              </button>
            </div>

            <!-- Plan 2: Family All-Access Pass -->
            <div style="background: #37000A; border: 1.5px solid #FF1F3D; border-radius: 18px; padding: 26px 28px; position: relative; overflow: hidden; box-shadow: 0 16px 36px rgba(255,31,61,0.2); display: flex; flex-direction: column; justify-content: space-between;">
              <!-- Radial Glow and Star Watermark -->
              <div style="position: absolute; top: 0; right: 0; width: 150px; height: 150px; background: radial-gradient(circle, rgba(255,31,61,0.25) 0%, transparent 70%); pointer-events: none;"></div>
              <div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                  <span style="font-size: 11px; font-weight: 800; color: #37000A; background: #9EE425; padding: 4px 10px; border-radius: 6px; font-family: 'Absans', sans-serif;">RECOMMENDED</span>
                  <span style="font-size: 12px; font-weight: 700; color: #FF1F3D; background: rgba(255,31,61,0.15); border: 1px solid rgba(255,31,61,0.3); padding: 3px 8px; border-radius: 4px;">Unlimited Events</span>
                </div>
                <h3 style="font-family: 'Sen', sans-serif !important; font-size: 20px; font-weight: 400 !important; color: #F2EFEA; margin: 0 0 8px;">Family Pack (3 Events)</h3>
                <div style="display: flex; align-items: baseline; gap: 6px; margin-bottom: 14px;">
                  <span style="font-size: 32px; font-weight: 700; color: #F2EFEA; font-family: 'Sen', sans-serif;">₹99</span>
                  <span style="font-size: 13px; color: #F2EFEA; opacity: 0.8;">/ 3 major events</span>
                </div>
                <ul style="list-style: none; padding: 0; margin: 0 0 20px; display: flex; flex-direction: column; gap: 8px; font-size: 13px; color: #F2EFEA; opacity: 0.9;">
                  <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: bold;">✔</span> 3 Sacred Celebrations (Any Rituals)</li>
                  <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: bold;">✔</span> Multi-Desk Family Sync (4 Counters)</li>
                  <li style="display: flex; align-items: center; gap: 8px;"><span style="color: #9EE425; font-weight: bold;">✔</span> Priority WhatsApp Support & Backups</li>
                </ul>
              </div>
              <button type="button" class="btn-tactile-primary" onclick="window.GVStore ? window.GVStore.purchasePass('family', 99) : navToView('login')" style="width: 140px !important;">
                <span>Get ₹99 Pack</span>
              </button>
            </div>
          </div>
        </section>
        """
        pricing_section.replace_with(BeautifulSoup(pricing_html, 'html.parser'))

    # Save changes
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Master redesign applied to {filepath}")

for path in ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']:
    update_html(path)
