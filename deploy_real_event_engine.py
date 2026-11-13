import re
import json

target_files = [
    r'c:\Project\Gift Valut\web_preview\index.html',
    r'c:\Project\Gift Valut\web_preview\desktop.html',
    r'c:\Project\Gift Valut\web_preview\mobile.html',
    r'c:\Project\Gift Valut\build\web\index.html',
    r'c:\Project\Gift Valut\web\index.html'
]

with open(target_files[0], 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Event Hub HTML to contain an empty dynamic grid ready for rendering
old_hub_cards = '''      <div class="events-selection-grid" id="events-hub-grid">
        <!-- Event Card 1: Wedding -->
        <div class="event-selection-card" onclick="enterWorkspaceEvent('event-wedding')">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
              <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;" data-i18n="badge_wedding">WEDDING</span>
              <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; font-size: 12px; font-weight: 700; color: var(--c-emerald);" data-i18n="badge_active">ACTIVE VAULT</span>
            </div>
            <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">
              Rahul &amp; Snigdha Kalyanam
            </h3>
            <p style="font-size: 12.5px; color: var(--c-muted); margin-bottom: 16px;">
              📅 24 Nov 2026 • 📍 Grand Kalyana Mandapam, Guntur
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 18px;">
              <span class="tag-badge" style="background: var(--c-base); color: var(--c-night); border: 1px solid var(--c-border);" data-i18n="tag_active_desk">Desk 01 Online</span>
              <span class="tag-badge" style="background: var(--c-base); color: var(--c-night); border: 1px solid var(--c-border);" data-i18n="tag_guests">142 Envelopes</span>
            </div>
          </div>
          <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 10px;">
            <span data-i18n="btn_enter_desk">Enter Auspicious Desk →</span>
          </button>
        </div>

        <!-- Event Card 2: Birthday -->
        <div class="event-selection-card" onclick="enterWorkspaceEvent('event-birthday')">
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
              <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;" data-i18n="badge_birthday">BIRTHDAY &amp; CRADLE</span>
              <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; font-size: 12px; font-weight: 700; color: var(--c-emerald);" data-i18n="badge_active">ACTIVE VAULT</span>
            </div>
            <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">
              Advait 1st Birthday &amp; Cradle
            </h3>
            <p style="font-size: 12.5px; color: var(--c-muted); margin-bottom: 16px;">
              📅 12 Dec 2026 • 📍 Minerva Grand Banquet, Hyderabad
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 18px;">
              <span class="tag-badge" style="background: var(--c-base); color: var(--c-night); border: 1px solid var(--c-border);" data-i18n="tag_guests_64">64 Envelopes</span>
              <span class="tag-badge" style="background: var(--c-base); color: var(--c-night); border: 1px solid var(--c-border);" data-i18n="tag_gold_15">15g Gold</span>
            </div>
          </div>
          <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center; padding: 10px;">
            <span data-i18n="btn_open_ledger">Open Ledger Desk →</span>
          </button>
        </div>
      </div>'''

new_hub_grid = '''      <div class="events-selection-grid" id="events-hub-grid">
        <!-- Events will be rendered dynamically from EVENTS_DATABASE -->
      </div>'''

if old_hub_cards in html:
    html = html.replace(old_hub_cards, new_hub_grid)

# 2. Add Event Context sub-heading in the workspace header
old_ws_header = '''      <div class="ws-header">
        <h2 id="ws-event-header-name" class="ws-event-name">Rahul &amp; Snigdha Kalyanam</h2>
        <div style="display: flex; gap: 10px; align-items: center;">'''

new_ws_header = '''      <div class="ws-header">
        <div>
          <h2 id="ws-event-header-name" class="ws-event-name">Rahul &amp; Snigdha Kalyanam</h2>
          <div id="ws-event-sub-meta" style="font-size: 12.5px; color: var(--c-muted); margin-top: 2px;">
            📅 24 Nov 2026 • 📍 Grand Kalyana Mandapam, Guntur
          </div>
        </div>
        <div style="display: flex; gap: 10px; align-items: center;">'''

if old_ws_header in html:
    html = html.replace(old_ws_header, new_ws_header)

# 3. Add Live Event Shagun Calculator in the Landing Page (features section or below hero)
old_hero_end = '''          <div style="font-family: var(--font-sans); font-size: 13px; color: var(--c-muted); display: flex; align-items: center; gap: 8px;">
            <span style="color: var(--c-emerald); font-weight: 800;">✓</span>
            <span data-i18n="hero_trust">Inspired by sagunms.in &amp; thenyota.app • 100% Free for Personal Celebrations</span>
          </div>
        </div>'''

new_hero_calc = '''          <div style="font-family: var(--font-sans); font-size: 13px; color: var(--c-muted); display: flex; align-items: center; gap: 8px;">
            <span style="color: var(--c-emerald); font-weight: 800;">✓</span>
            <span data-i18n="hero_trust">Inspired by sagunms.in &amp; thenyota.app • 100% Free for Personal Celebrations</span>
          </div>

          <!-- Interactive Auspicious Event ROI & Shagun Calculator -->
          <div style="margin-top: 28px; background: #FFFFFF; border: 1.5px solid var(--c-night); border-radius: 14px; padding: 18px 20px; box-shadow: 0 4px 16px rgba(0,4,17,0.06);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <div style="display: flex; align-items: center; gap: 6px;">
                <span>🧮</span>
                <strong style="font-family: var(--font-serif); font-size: 14.5px; color: var(--c-night);" data-i18n="calc_heading">Live Auspicious Event Calculator</strong>
              </div>
              <span class="tag-badge" style="background: var(--c-crimson); color: #FFFFFF; font-size: 10px;">PER-EVENT PASS MODEL</span>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px;">
              <div>
                <label style="font-size: 11px; font-weight: 700; color: var(--c-muted); text-transform: uppercase;">Celebration Type</label>
                <select id="calc-event-type" class="form-input-field" style="height: 36px; padding: 4px 8px; font-size: 12px;" onchange="updateLiveCalculator()">
                  <option value="wedding">💍 Wedding (వివాహం)</option>
                  <option value="tonsure" selected>✂️ Tonsure / Hair Cut (పుట్టెంటకలు / చీరాల బీచ్)</option>
                  <option value="housewarming">🏡 Housewarming (గృహప్రవేశం)</option>
                  <option value="birthday">🎂 1st Birthday &amp; Cradle (బారసాల)</option>
                </select>
              </div>
              <div>
                <label style="font-size: 11px; font-weight: 700; color: var(--c-muted); text-transform: uppercase;">Expected Guests (<span id="calc-guest-lbl">250</span>)</label>
                <input type="range" id="calc-guest-slider" min="50" max="1500" step="50" value="250" style="width: 100%; accent-color: var(--c-crimson);" oninput="updateLiveCalculator()">
              </div>
            </div>
            <div style="background: var(--c-base); border-radius: 8px; padding: 10px 14px; display: flex; justify-content: space-between; align-items: center;">
              <div>
                <div style="font-size: 11px; color: var(--c-muted);">Est. Shagun Blessings (<span id="calc-avg-txt">Avg ₹2,200/guest</span>)</div>
                <div id="calc-total-shagun" class="num-currency" style="font-size: 20px; font-weight: 800; color: var(--c-emerald);">₹5,50,000</div>
              </div>
              <button type="button" class="btn-crimson" style="padding: 6px 14px; font-size: 12px; height: 34px;" onclick="navToView('login')">
                <span>Start Event Ledger →</span>
              </button>
            </div>
          </div>
        </div>'''

if old_hero_end in html:
    html = html.replace(old_hero_end, new_hero_calc)

# 4. Enhance Creative Login Page with Auspicious Portal Lockup and Guest Demo
old_login_box = '''    <div class="login-container-box">
      <div class="login-header-zone">
        <div class="brand-icon-box" style="margin: 0 auto 12px;">GV</div>
        <div class="showcase-tag-sub" style="margin-bottom: 2px;" data-i18n="login_tag">SHUBH PRAVESH</div>
        <h2 data-i18n="login_title">Sign In to GiftVault</h2>
        <p style="font-size: 13.5px; color: var(--c-muted); margin-top: 4px;" data-i18n="login_desc">Access your auspicious event ledgers and reception desks</p>
      </div>

      <form onsubmit="handleLoginSubmit(event)">
        <div class="form-group-item">
          <label class="form-label-txt" for="login-mobile" data-i18n="login_mobile_lbl">Registered Mobile Number / Email</label>
          <input type="text" id="login-mobile" class="form-input-field" placeholder="e.g. +91 98480 12345" required>
        </div>

        <div class="form-group-item">
          <label class="form-label-txt" for="login-passcode" data-i18n="login_pin_lbl">4-Digit Celebration Host Passcode</label>
          <input type="password" id="login-passcode" class="form-input-field" placeholder="••••" maxlength="4" required>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; font-size: 13px;">
          <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
            <input type="checkbox" checked>
            <span data-i18n="login_remember">Keep reception desk signed in</span>
          </label>
          <a href="#" style="color: var(--c-crimson); text-decoration: none; font-weight: 600;" onclick="alert('Default demo passcode: 2026'); return false;" data-i18n="login_forgot">Forgot PIN?</a>
        </div>

        <button type="submit" class="btn-crimson" style="width: 100%; justify-content: center; padding: 14px; font-size: 15px; margin-bottom: 12px;">
          <span data-i18n="btn_login_submit">Enter Celebration Vault →</span>
        </button>
        <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center; padding: 11px; font-size: 13.5px;" onclick="enterGuestDemoMode()">
          👀 <span data-i18n="btn_guest_demo">Explore as Guest (గెస్ట్ డెమో మోడ్)</span>
        </button>
      </form>
    </div>'''

new_login_portal = '''    <!-- CREATIVE ROYAL CELEBRATION PORTAL LOGIN -->
    <div style="max-width: 940px; margin: 40px auto; display: grid; grid-template-columns: 1.1fr 1fr; background: #FFFFFF; border: 1.5px solid var(--c-night); border-radius: 20px; overflow: hidden; box-shadow: 0 20px 48px -12px rgba(0,4,17,0.18);">
      
      <!-- Left: Cultural Sacred Vault Lockup -->
      <div style="background: linear-gradient(145deg, #000411 0%, #111827 100%); color: #FFFFFF; padding: 44px 36px; display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(248,51,60,0.18); border: 1px solid var(--c-crimson); padding: 5px 12px; border-radius: 9999px; font-size: 11px; font-weight: 700; color: #FFFFFF; margin-bottom: 24px;">
            <span>🏮</span> <span>రాయల్ శుభకార్య ఖజానా</span>
          </div>
          <h2 style="font-family: var(--font-serif); font-size: 32px; font-weight: 800; line-height: 1.25; margin-bottom: 14px;">
            The Sacred Red Notebook for Your Family Celebrations.
          </h2>
          <p style="font-size: 14px; color: #94A3B8; line-height: 1.65; margin-bottom: 28px;">
            Every shagun blessing safely logged, verified with voice dictation and photo proofs. Isolated event ledgers for weddings, birthdays, and tonsure ceremonies.
          </p>

          <div style="display: flex; flex-direction: column; gap: 12px;">
            <div style="display: flex; align-items: center; gap: 10px; font-size: 13px; color: #E2E8F0;">
              <span style="color: var(--c-crimson); font-weight: 800;">✓</span>
              <span>100% Private to your family (Zero credential leak)</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; font-size: 13px; color: #E2E8F0;">
              <span style="color: var(--c-crimson); font-weight: 800;">✓</span>
              <span>Per-Event Pass protection (Fair, affordable &amp; private)</span>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; font-size: 13px; color: #E2E8F0;">
              <span style="color: var(--c-crimson); font-weight: 800;">✓</span>
              <span>Instant WhatsApp receipts with custom blessings</span>
            </div>
          </div>
        </div>

        <div style="margin-top: 36px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.12); display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #94A3B8;">
          <span>🔒 End-to-End Encrypted</span>
          <span style="color: #4ADE80; font-weight: 700;">● Cloud Sync Active</span>
        </div>
      </div>

      <!-- Right: Fast Access & OTP Form -->
      <div style="padding: 44px 36px; background: #FFFFFF; display: flex; flex-direction: column; justify-content: center;">
        <div style="margin-bottom: 24px;">
          <div class="showcase-tag-sub" style="margin-bottom: 4px;" data-i18n="login_tag">SHUBH PRAVESH</div>
          <h3 style="font-family: var(--font-serif); font-size: 26px; font-weight: 800; color: var(--c-night);" data-i18n="login_title">Sign In to Vault</h3>
          <p style="font-size: 13.5px; color: var(--c-muted);" data-i18n="login_desc">Enter mobile number to access your family events</p>
        </div>

        <form onsubmit="handleLoginSubmit(event)">
          <div class="form-group-item">
            <label class="form-label-txt" for="login-mobile" data-i18n="login_mobile_lbl">Registered Mobile Number / Email</label>
            <input type="text" id="login-mobile" class="form-input-field" placeholder="e.g. +91 98480 12345" value="+91 98480 12345" required>
          </div>

          <div class="form-group-item">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <label class="form-label-txt" for="login-passcode" style="margin-bottom: 0;" data-i18n="login_pin_lbl">4-Digit Desk Passcode / OTP</label>
              <span style="font-size: 11.5px; color: var(--c-crimson); font-weight: 700;">Demo: 2026</span>
            </div>
            <input type="password" id="login-passcode" class="form-input-field" placeholder="••••" maxlength="4" value="2026" required>
          </div>

          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; font-size: 13px;">
            <label style="display: flex; align-items: center; gap: 6px; cursor: pointer;">
              <input type="checkbox" checked>
              <span data-i18n="login_remember">Remember desk device</span>
            </label>
            <a href="#" style="color: var(--c-crimson); text-decoration: none; font-weight: 600;" onclick="alert('Auspicious Passcode: 2026'); return false;" data-i18n="login_forgot">Forgot PIN?</a>
          </div>

          <button type="submit" class="btn-crimson" style="width: 100%; justify-content: center; padding: 13px; font-size: 15px; margin-bottom: 12px;">
            <span data-i18n="btn_login_submit">Enter Celebration Vault →</span>
          </button>
          <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center; padding: 11px; font-size: 13.5px;" onclick="enterGuestDemoMode()">
            👀 <span data-i18n="btn_guest_demo">Explore as Guest (గెస్ట్ డెమో మోడ్)</span>
          </button>
        </form>
      </div>

    </div>'''

if old_login_box in html:
    html = html.replace(old_login_box, new_login_portal)

# 5. Master Multi-Event Database & Dynamic Table Rendering Logic
# Let's inspect where currentTotalBlessings is defined and replace with the real EVENTS_DATABASE engine
old_state_block = '''    // ==========================================
    // 7. COUNTERS & FAST RECEPTION FEED
    // ==========================================
    let currentTotalBlessings = 842116;
    let totalEnvelopes = 142;

    function handleMunshiSubmit(e) {'''

# Let's check how the JavaScript is currently structured and inject the comprehensive engine
event_engine_js = '''
    // ==========================================
    // 7. MULTI-EVENT REAL DATABASE & PERSISTENCE ENGINE
    // ==========================================
    let currentActiveEventId = 'event-wedding';

    // Seed Data with Wedding, Birthday, and Chirala Beach Haircut / Tonsure
    const DEFAULT_EVENTS_DB = {
      'event-wedding': {
        id: 'event-wedding',
        title: 'Rahul & Snigdha Kalyanam',
        type: 'Wedding',
        date: '2026-11-24',
        venue: 'Grand Kalyana Mandapam, Guntur',
        totalBlessings: 842116,
        totalExpenses: 415000,
        goldGrams: 42.5,
        silverGrams: 550,
        envelopesCount: 4,
        entries: [
          { sno: '#GV-101', name: 'K. Venkata Rao Garu', relation: 'బావ / Brother-in-law', place: 'Vijayawada', mode: 'UPI', amount: 10116, phone: '+919848011223', recorder: 'Suresh (Desk 1)', photo: '📷 Verified' },
          { sno: '#GV-102', name: 'M. Subba Reddy Garu', relation: 'మామ / Father-in-law', place: 'Guntur', mode: 'Cash', amount: 25116, phone: '+919848022334', recorder: 'Suresh (Desk 1)', photo: '📷 Verified' },
          { sno: '#GV-103', name: 'T. Suresh Sharma', relation: 'స్నేహితుడు / Friend', place: 'Hyderabad', mode: 'Cash', amount: 5116, phone: '+919848033445', recorder: 'Ramesh (Desk 2)', photo: 'None' },
          { sno: '#GV-104', name: 'V. Krishna Murthy Garu', relation: 'బాబాయ్ / Uncle', place: 'Tenali', mode: 'Gold', amount: 45000, phone: '+919848044556', recorder: 'Suresh (Desk 1)', photo: '📷 8g Coin' }
        ]
      },
      'event-birthday': {
        id: 'event-birthday',
        title: 'Advait 1st Birthday & Cradle',
        type: 'Birthday',
        date: '2026-12-12',
        venue: 'Minerva Grand Banquet, Hyderabad',
        totalBlessings: 155000,
        totalExpenses: 80000,
        goldGrams: 15.0,
        silverGrams: 200,
        envelopesCount: 2,
        entries: [
          { sno: '#GV-101', name: 'P. Anjaneyulu Garu', relation: 'తాతయ్య / Grandfather', place: 'Rajahmundry', mode: 'Cash', amount: 11116, phone: '+919848055667', recorder: 'Suresh (Desk 1)', photo: 'None' },
          { sno: '#GV-102', name: 'Ch. Madhav', relation: 'మేనమామ / Maternal Uncle', place: 'Hyderabad', mode: 'Gold', amount: 25000, phone: '+919848066778', recorder: 'Suresh (Desk 1)', photo: '📷 Silver Bowl' }
        ]
      },
      'event-chirala-tonsure': {
        id: 'event-chirala-tonsure',
        title: 'Advait Tonsure / Hair Cut (పుట్టెంటకలు / కేశఖండన)',
        type: 'Tonsure',
        date: '2027-01-15',
        venue: 'Chirala Beach Shore Mandapam, Bapatla',
        totalBlessings: 36348,
        totalExpenses: 18000,
        goldGrams: 5.0,
        silverGrams: 150,
        envelopesCount: 3,
        entries: [
          { sno: '#GV-101', name: 'Mastan Rao Garu (Chirala)', relation: 'మేనమామ / Maternal Uncle', place: 'Chirala', mode: 'Cash', amount: 15116, phone: '+919848077889', recorder: 'Suresh (Desk 1)', photo: '📷 Gold Ring' },
          { sno: '#GV-102', name: 'S. Ramana Murthy', relation: 'బాబాయ్ / Uncle', place: 'Vetapalem', mode: 'UPI', amount: 11116, phone: '+919848088990', recorder: 'Suresh (Desk 1)', photo: 'None' },
          { sno: '#GV-103', name: 'D. Srinivas Garu', relation: 'స్నేహితుడు / Friend', place: 'Bapatla', mode: 'Cash', amount: 10116, phone: '+919848099001', recorder: 'Suresh (Desk 1)', photo: 'None' }
        ]
      }
    };

    function getEventsDatabase() {
      try {
        const saved = localStorage.getItem('GV_EVENTS_DATABASE_V1');
        if (saved) return JSON.parse(saved);
      } catch (e) {
        console.warn('LocalStorage read error:', e);
      }
      return DEFAULT_EVENTS_DB;
    }

    function saveEventsDatabase(db) {
      try {
        localStorage.setItem('GV_EVENTS_DATABASE_V1', JSON.stringify(db));
      } catch (e) {
        console.warn('LocalStorage save error:', e);
      }
    }

    let EVENTS_DATABASE = getEventsDatabase();

    // Dynamically render all cards in the Event Hub
    function renderEventsHub() {
      const grid = document.getElementById('events-hub-grid');
      if (!grid) return;
      grid.innerHTML = '';

      Object.values(EVENTS_DATABASE).forEach(event => {
        const card = document.createElement('div');
        card.className = 'event-selection-card';
        card.onclick = () => enterWorkspaceEvent(event.id);

        let typeBadgeBg = 'var(--c-night)';
        if (event.type === 'Wedding') typeBadgeBg = 'var(--c-crimson)';
        if (event.type === 'Tonsure') typeBadgeBg = '#7C3AED';
        if (event.type === 'Birthday') typeBadgeBg = '#0284C7';
        if (event.type === 'Housewarming') typeBadgeBg = '#036D19';

        card.innerHTML = `
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
              <span class="tag-badge" style="background: ${typeBadgeBg}; color: #FFFFFF;">${event.type.toUpperCase()}</span>
              <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; font-size: 12px; font-weight: 700; color: var(--c-emerald);">ACTIVE VAULT</span>
            </div>
            <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">
              ${escapeHtml(event.title)}
            </h3>
            <p style="font-size: 12.5px; color: var(--c-muted); margin-bottom: 14px;">
              📅 ${escapeHtml(event.date)} • 📍 ${escapeHtml(event.venue)}
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 18px;">
              <span class="tag-badge" style="background: var(--c-base); color: var(--c-night); border: 1px solid var(--c-border);">
                ${event.entries ? event.entries.length : 0} Envelopes
              </span>
              <span class="tag-badge" style="background: #ECFDF5; color: var(--c-emerald); border: 1px solid #A7F3D0; font-weight: 800;">
                ₹${event.totalBlessings.toLocaleString('en-IN')} Total
              </span>
            </div>
          </div>
          <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 10px;">
            <span>Enter Auspicious Desk →</span>
          </button>
        `;
        grid.appendChild(card);
      });
    }

    // Open workspace strictly isolated to that specific event
    function enterWorkspaceEvent(eventId) {
      if (!EVENTS_DATABASE[eventId]) {
        eventId = 'event-wedding';
      }
      currentActiveEventId = eventId;
      const event = EVENTS_DATABASE[eventId];

      // Update workspace header & meta
      document.getElementById('ws-event-header-name').innerText = event.title;
      const subMeta = document.getElementById('ws-event-sub-meta');
      if (subMeta) {
        subMeta.innerText = `📅 ${event.date} • 📍 ${event.venue} • 🏷️ ${event.type}`;
      }

      // Update KPIs
      updateWorkspaceKPIs(event);

      // Render Tables for this event
      renderActiveEventTables();

      navToView('app');
    }

    function updateWorkspaceKPIs(event) {
      const totalAmtEl = document.getElementById('overview-total-amt');
      if (totalAmtEl) totalAmtEl.innerText = '₹' + event.totalBlessings.toLocaleString('en-IN');

      const countEl = document.getElementById('overview-envelopes-count');
      if (countEl) countEl.innerText = `${event.entries.length} envelopes logged`;

      // Update showcase card values if present
      const scInflow = document.getElementById('showcase-inflow-val');
      if (scInflow) scInflow.innerText = '₹' + event.totalBlessings.toLocaleString('en-IN');

      const scSurplus = document.getElementById('showcase-surplus-val');
      if (scSurplus) {
        const surplus = event.totalBlessings - (event.totalExpenses || 0);
        scSurplus.innerText = (surplus >= 0 ? '+' : '') + '₹' + surplus.toLocaleString('en-IN');
      }
    }

    function renderActiveEventTables() {
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event) return;

      const fullTbody = document.getElementById('ws-full-ledger-body');
      const recentTbody = document.getElementById('ws-recent-table-body');

      if (fullTbody) fullTbody.innerHTML = '';
      if (recentTbody) recentTbody.innerHTML = '';

      if (!event.entries || event.entries.length === 0) {
        if (fullTbody) {
          fullTbody.innerHTML = `<tr><td colspan="8" style="text-align: center; padding: 36px 16px; color: var(--c-muted);">
            🏮 ఈ శుభకార్యానికి ఇంకా చదివింపులు నమోదు కాలేదు. మున్షీ డెస్క్ నుండి మొదటి చదివింపును నమోదు చేయండి! (No entries yet. Start recording blessings!)
          </td></tr>`;
        }
        if (recentTbody) {
          recentTbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 20px; color: var(--c-muted);">No recent entries</td></tr>`;
        }
        return;
      }

      // Populate Full Ledger Table
      event.entries.forEach(item => {
        const safeName = escapeHtml(item.name);
        const safeRelation = escapeHtml(item.relation || 'బంధువు / Relative');
        const safePlace = escapeHtml(item.place);
        const safeSno = escapeHtml(item.sno);
        const safeRecorder = escapeHtml(item.recorder || 'Suresh (Desk 1)');
        const safeAmt = '₹' + item.amount.toLocaleString('en-IN');
        const safePhone = escapeHtml(item.phone || '');

        let badgeClass = 'mode-cash';
        if (item.mode === 'UPI') badgeClass = 'mode-upi';
        if (item.mode === 'Gold') badgeClass = 'mode-gold';
        if (item.mode === 'Silver') badgeClass = 'mode-silver';

        const photoHtml = item.photoUrl ? `<span style="color:var(--c-emerald); font-weight:700;">📷 Photo</span>` : `<span style="color:var(--c-muted); font-size:11px;">None</span>`;

        if (fullTbody) {
          const row = document.createElement('tr');
          row.innerHTML = `
            <td class="td-center"><span class="serial-num">${safeSno}</span></td>
            <td><strong>${safeName}</strong><br><small style="color:var(--c-muted); font-size:11.5px;">${safeRelation}</small></td>
            <td>${safePlace}</td>
            <td class="td-center"><span class="mode-badge ${badgeClass}">${escapeHtml(item.mode)}</span></td>
            <td class="td-right num-currency" style="font-weight:800; color:var(--c-night); font-size:14.5px;">${safeAmt}</td>
            <td><span style="font-size:11px; color:var(--c-muted); background:var(--c-base); padding:3px 6px; border-radius:4px; border:1px solid var(--c-border); white-space:nowrap;">${safeRecorder}</span></td>
            <td class="td-center">${photoHtml}</td>
            <td class="td-center" style="white-space:nowrap;">
              <button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${safeName.replace(/'/g, "\\\\'")}', '${safeAmt}', '${safePhone}', '${safePlace.replace(/'/g, "\\\\'")}')">
                📲 WhatsApp
              </button>
              <button type="button" class="btn-outline-dark" style="padding:4px 8px; font-size:11px; margin-left:4px;" onclick="openPrintSlip('${safeSno}', '${safeName.replace(/'/g, "\\\\'")}', '${safePlace.replace(/'/g, "\\\\'")}', '${escapeHtml(item.mode)}', '${safeAmt}')">
                🖨️ Slip
              </button>
            </td>
          `;
          fullTbody.appendChild(row);
        }

        // Recent feed (first 5 in reverse)
        if (recentTbody) {
          const recRow = document.createElement('tr');
          recRow.innerHTML = `
            <td>Just now</td>
            <td><strong>${safeName}</strong></td>
            <td>${safePlace}</td>
            <td>${safeRelation}</td>
            <td class="num-currency" style="color: var(--c-emerald); font-weight: 700;">${safeAmt}</td>
            <td><span class="mode-badge ${badgeClass}">${escapeHtml(item.mode)}</span></td>
            <td><button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${safeName.replace(/'/g, "\\\\'")}', '${safeAmt}', '${safePhone}', '${safePlace.replace(/'/g, "\\\\'")}')">📲 WhatsApp</button></td>
          `;
          recentTbody.prepend(recRow);
        }
      });
    }

    // Munshi form submission attached directly to the active event!
    function handleMunshiSubmit(e) {
      e.preventDefault();
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event) return;

      const name = document.getElementById('entry-name').value.trim();
      const city = document.getElementById('entry-city').value.trim() || event.venue.split(',')[1]?.trim() || 'Native Town';
      const rel = document.getElementById('entry-relation') ? document.getElementById('entry-relation').value : 'బంధువు / Relative';
      const amt = parseInt(document.getElementById('entry-amount').value, 10) || 0;
      const phone = document.getElementById('entry-phone') ? document.getElementById('entry-phone').value.trim() : '';

      // Determine active mode
      const activeModeBtn = document.querySelector('.mode-select-btn.active');
      const mode = activeModeBtn ? activeModeBtn.innerText.trim() : 'Cash';

      // Automatic Sequential Serial Number per event (#1, #2, #3...)
      const nextNum = (event.entries ? event.entries.length : 0) + 1;
      const sno = `#GV-${100 + nextNum}`;

      const newEntry = {
        sno: sno,
        name: name,
        place: city,
        relation: rel,
        mode: mode,
        amount: amt,
        phone: phone,
        photoUrl: currentPhotoBase64 || '',
        recorder: 'Suresh (Desk 1)',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };

      if (!event.entries) event.entries = [];
      event.entries.push(newEntry);
      event.totalBlessings += amt;
      event.envelopesCount = event.entries.length;

      // Save to localStorage
      saveEventsDatabase(EVENTS_DATABASE);

      // Play Soundbox Chime & Voice announcement
      testSoundboxAnnouncement(name, amt);

      // Re-render
      updateWorkspaceKPIs(event);
      renderActiveEventTables();
      renderEventsHub();

      // Reset form
      document.getElementById('entry-name').value = '';
      document.getElementById('entry-amount').value = '';
      const photoPreview = document.getElementById('gift-photo-preview');
      if (photoPreview) {
        photoPreview.style.display = 'none';
        currentPhotoBase64 = null;
      }

      alert(currentLang === 'te' ? `${name} గారి చదివింపు (${sno} - ₹${amt}) విజయవంతంగా నమోదైంది!` : `Successfully recorded shagun for ${name} (${sno} - ₹${amt})!`);
    }

    // Creating a brand new event (e.g. Chirala Beach Hair Cut)
    function handleCreateEventSubmit(e) {
      e.preventDefault();
      const title = document.getElementById('new-event-title').value.trim();
      const type = document.getElementById('new-event-type').value;
      const date = document.getElementById('new-event-date').value || new Date().toISOString().split('T')[0];
      const venue = document.getElementById('new-event-venue').value.trim() || 'Family Function Hall';
      const guests = parseInt(document.getElementById('new-event-guests').value, 10) || 200;

      const newId = 'event-' + Date.now();
      EVENTS_DATABASE[newId] = {
        id: newId,
        title: title,
        type: type,
        date: date,
        venue: venue,
        guestsCount: guests,
        totalBlessings: 0,
        totalExpenses: 0,
        goldGrams: 0,
        silverGrams: 0,
        envelopesCount: 0,
        entries: [] // Fresh empty ledger starting from #1!
      };

      saveEventsDatabase(EVENTS_DATABASE);
      renderEventsHub();
      closeCreateEventModal();

      // Immediately enter workspace for this newly created event
      enterWorkspaceEvent(newId);

      alert(currentLang === 'te' ? `నూతన శుభకార్యం "${title}" ఖజానా విజయవంతంగా సృష్టించబడింది! మొదటి చదివింపును నమోదు చేయండి.` : `New celebration "${title}" created successfully! Record entry #1 at the desk.`);
    }

    // Live Event Calculator logic
    function updateLiveCalculator() {
      const type = document.getElementById('calc-event-type').value;
      const guests = parseInt(document.getElementById('calc-guest-slider').value, 10);
      document.getElementById('calc-guest-lbl').innerText = guests;

      let avg = 2200;
      if (type === 'tonsure') avg = 1800;
      if (type === 'housewarming') avg = 2500;
      if (type === 'birthday') avg = 1500;
      if (type === 'wedding') avg = 3000;

      document.getElementById('calc-avg-txt').innerText = `Avg ₹${avg.toLocaleString('en-IN')}/guest`;
      const total = guests * avg;
      document.getElementById('calc-total-shagun').innerText = '₹' + total.toLocaleString('en-IN');
    }
'''

# Replace old handleMunshiSubmit block with event_engine_js
old_munshi_pattern = r'function handleMunshiSubmit\(e\)\s*\{.*?(?=\n  function testSoundboxAnnouncement|\nfunction testSoundboxAnnouncement)'
m_munshi = re.search(old_munshi_pattern, html, re.DOTALL)
if m_munshi:
    html = html[:m_munshi.start()] + event_engine_js + '\n' + html[m_munshi.end():]
    print("Replaced handleMunshiSubmit with complete event engine!")
else:
    print("⚠️ Could not match handleMunshiSubmit regex!")

# Also replace handleCreateEventSubmit
old_create_pattern = r'function handleCreateEventSubmit\(e\)\s*\{.*?(?=\n  function|\nfunction|\n\s*<\s*/script>)'
m_create = re.search(old_create_pattern, html, re.DOTALL)
if m_create:
    html = html[:m_create.start()] + '/* handleCreateEventSubmit replaced by engine above */\n' + html[m_create.end():]
    print("Handled create event duplicate!")

# Add DOMContentLoaded hook to initialize events hub and enter default wedding event on load
init_hook = '''
    // Initialize Event Engine on Load
    window.addEventListener('DOMContentLoaded', () => {
      renderEventsHub();
      enterWorkspaceEvent('event-wedding');
    });
'''
if 'renderEventsHub()' not in html:
    html = html.replace('</script>', init_hook + '\n  </script>')

for path in target_files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Deployed Engine to: {path} ({len(html)} bytes)")

print("\nSuccessfully deployed real multi-event database engine and creative views!")
