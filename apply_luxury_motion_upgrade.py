import re

# 1. CSS to inject into <style>
css_to_inject = '''
    /* ==========================================================================
       ETALE 52 & THREEUI LUXURY MOTION & NUMBER PLATE SYSTEM
       ========================================================================== */
    /* Ambient Fixed Canvas */
    #ambient-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 0;
      opacity: 0.65;
    }

    /* 3D Perspective Card Tilt & Specular Follow */
    .tilt-card {
      transition: transform 0.22s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.22s ease;
      transform-style: preserve-3d;
      position: relative;
    }
    .tilt-card::before {
      content: "";
      position: absolute;
      inset: 0;
      background: radial-gradient(circle 380px at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(248, 51, 60, 0.05), transparent 70%);
      pointer-events: none;
      border-radius: inherit;
      z-index: 1;
    }

    /* Etale 52 Mechanical Rolling Number Plates */
    .number-plate-cluster {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: #000411;
      padding: 10px 16px;
      border-radius: 12px;
      border: 1.5px solid #1E293B;
      box-shadow: 0 8px 24px rgba(0, 4, 17, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.12);
    }
    .plate-currency-symbol {
      color: #E5A93C;
      font-family: var(--font-serif);
      font-size: 28px;
      font-weight: 800;
      margin-right: 3px;
    }
    .plate-digit-slot {
      position: relative;
      width: 26px;
      height: 44px;
      background: linear-gradient(180deg, #111827 0%, #030712 100%);
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid rgba(229, 169, 60, 0.35);
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.8), 0 2px 4px rgba(0,0,0,0.3);
    }
    .plate-digit-slot::after {
      content: "";
      position: absolute;
      top: 50%;
      left: 0;
      right: 0;
      height: 1px;
      background: rgba(255, 255, 255, 0.14);
      box-shadow: 0 1px 1px rgba(0,0,0,0.9);
      z-index: 2;
    }
    .plate-digit-ribbon {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      transition: transform 0.45s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .plate-digit-item {
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      font-family: var(--font-sans);
      font-size: 24px;
      font-weight: 800;
      font-feature-settings: 'tnum';
      font-variant-numeric: tabular-nums;
      text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    .plate-separator {
      color: #E5A93C;
      font-size: 24px;
      font-weight: 800;
      padding: 0 2px;
      line-height: 44px;
    }

    /* Emil Kowalski Tactile Button Compression */
    .btn-crimson:active,
    .btn-emerald:active,
    .btn-outline-dark:active,
    .lucky-coin-chip:active,
    .mode-btn:active,
    .ws-tab-btn:active {
      transform: scale(0.97) !important;
    }

    /* Coin Sparkle Particle */
    .sparkle-particle {
      position: fixed;
      pointer-events: none;
      border-radius: 50%;
      z-index: 99999;
      transform: translate(-50%, -50%);
      animation: sparkleFloat 0.7s cubic-bezier(0.23, 1, 0.32, 1) forwards;
    }
    @keyframes sparkleFloat {
      0% {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1);
      }
      100% {
        opacity: 0;
        transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(0.3);
      }
    }
'''

# 2. Canvas HTML tag to inject right after <body>
canvas_html = '  <!-- Fixed Ambient Celestial Canvas Shader Background -->\n  <canvas id="ambient-canvas"></canvas>\n'

# 3. Interactive Calculator HTML to inject after hero section
calculator_section_html = '''
    <!-- ==========================================================================
         INTERACTIVE AUSPICIOUS SHAGUN ESTIMATOR (ETALE 52 NUMBER PLATES)
         ========================================================================== -->
    <section id="calculator-section" class="section-wrap" style="background: linear-gradient(180deg, rgba(250,249,246,0.7) 0%, #FFFFFF 100%); border-top: 1.5px solid var(--c-border); position: relative; z-index: 2;">
      <div class="section-header-center" style="margin-bottom: 32px;">
        <span class="section-eyebrow">✦ SHAGUN PRAAPTI ESTIMATOR • ఎర్ర బహీఖాతా అంచనా ✦</span>
        <h2 class="section-title">Interactive Celebration Inflow Calculator</h2>
        <p class="section-desc">
          Estimate your auspicious shagun blessings in real-time with kinetic rolling number plates engineered for Indian weddings, housewarmings, and cradle celebrations.
        </p>
      </div>

      <div class="calculator-card tilt-card" style="max-width: 920px; margin: 0 auto; background: #FFFFFF; border: 2px solid var(--c-border); border-radius: 24px; padding: 36px 32px; box-shadow: 0 16px 40px -8px rgba(0, 4, 17, 0.08);">
        <div style="display: grid; grid-template-columns: 1fr 1.2fr; gap: 32px; align-items: center;" class="calc-grid-inner">
          
          <!-- Left: Controls -->
          <div>
            <div style="margin-bottom: 20px;">
              <label class="form-label-txt" style="font-size: 13px; font-weight: 800; color: var(--c-night);">Celebration Milestone *</label>
              <select id="calc-event-type" class="form-input-field" onchange="updateLiveCalculator()" style="font-size: 14.5px; padding: 12px 14px; font-weight: 700; border-radius: 10px;">
                <option value="wedding">💍 Royal Wedding (వివాహ మహోత్సవం - ₹3,000/guest)</option>
                <option value="tonsure">✂️ Tonsure & Haircut (కేశఖండన / పుట్టెంటకలు - ₹1,800/guest)</option>
                <option value="housewarming">🏡 Housewarming (గృహప్రవేశం - ₹2,500/guest)</option>
                <option value="birthday">🎂 Barasala & Birthday (బారసాల / పుట్టినరోజు - ₹1,500/guest)</option>
              </select>
            </div>

            <div style="margin-bottom: 24px;">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <label class="form-label-txt" style="font-size: 13px; font-weight: 800; color: var(--c-night);">Expected Family Guests</label>
                <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF; font-size: 12px; font-weight: 800; padding: 4px 10px; border-radius: 6px;">
                  <span id="calc-guest-lbl">500</span> Guests
                </span>
              </div>
              <input type="range" id="calc-guest-slider" min="50" max="2000" step="25" value="500" oninput="updateLiveCalculator()" style="width: 100%; accent-color: var(--c-crimson); cursor: pointer; height: 8px;">
              <div style="display: flex; justify-content: space-between; font-size: 11px; color: var(--c-muted); margin-top: 6px;">
                <span>50 Guests</span>
                <span>500 Standard</span>
                <span>2,000 Royal Scale</span>
              </div>
            </div>

            <div style="display: flex; align-items: center; gap: 10px; background: var(--c-base); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--c-border);">
              <span style="font-size: 18px;">💡</span>
              <span id="calc-avg-txt" style="font-size: 12.5px; font-weight: 700; color: var(--c-night);">Avg ₹3,000/guest based on regional cultural averages</span>
            </div>
          </div>

          <!-- Right: Animated Kinetic Number Plates -->
          <div style="background: var(--c-night); border-radius: 18px; padding: 28px 24px; text-align: center; border: 1.5px solid #1E293B; box-shadow: 0 12px 32px rgba(0,4,17,0.35);">
            <div style="font-size: 11px; font-weight: 800; color: var(--c-gold); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 12px;">
              ✦ ESTIMATED AUSPICIOUS INFLOW ✦
            </div>

            <!-- Kinetic Mechanical Number Plates -->
            <div id="calc-plate-mount" class="number-plate-cluster" style="justify-content: center; margin-bottom: 14px;"></div>

            <!-- Legacy fallback element for automated assertions & screenreaders -->
            <div id="calc-total-shagun" class="num-currency" style="display: none;">₹15,00,000</div>

            <div style="font-size: 12px; color: #94A3B8; margin-bottom: 20px;">
              Projected Blessings & Gold in Indian Rupees
            </div>

            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 13px; font-size: 14px;" onclick="triggerLuckySparkle(event); navToView('login');">
              <span>✍️ Open Desk for this Celebration →</span>
            </button>
          </div>

        </div>
      </div>
    </section>
'''

# 4. JavaScript functions for canvas, number plates, 3D tilt, and sparkles
js_to_inject = '''
    // ==========================================================================
    // ETALE 52 LUXURY MOTION ENGINE (CANVAS, NUMBER PLATES, 3D TILT, SPARKLES)
    // ==========================================================================
    // 1. Ambient Celestial Canvas Shader
    function initAmbientCanvas() {
      const cvs = document.getElementById('ambient-canvas');
      if (!cvs) return;
      const c = cvs.getContext('2d');
      let w = cvs.width = window.innerWidth;
      let h = cvs.height = window.innerHeight;

      window.addEventListener('resize', () => {
        w = cvs.width = window.innerWidth;
        h = cvs.height = window.innerHeight;
      });

      const pts = [];
      const COUNT = 36;
      let m = { x: w / 2, y: h / 2, tx: w / 2, ty: h / 2 };

      window.addEventListener('mousemove', (e) => {
        m.tx = e.clientX;
        m.ty = e.clientY;
      });

      for (let i = 0; i < COUNT; i++) {
        pts.push({
          x: Math.random() * w,
          y: Math.random() * h,
          vx: (Math.random() - 0.5) * 0.4,
          vy: (Math.random() - 0.5) * 0.4,
          r: Math.random() * 2 + 1,
          col: Math.random() > 0.35 ? 'rgba(229, 169, 60, ' : 'rgba(248, 51, 60, ',
          a: Math.random() * 0.4 + 0.15,
          phase: Math.random() * Math.PI * 2
        });
      }

      function loop() {
        if (document.hidden) {
          requestAnimationFrame(loop);
          return;
        }
        c.clearRect(0, 0, w, h);
        m.x += (m.tx - m.x) * 0.05;
        m.y += (m.ty - m.y) * 0.05;

        pts.forEach((p, idx) => {
          p.phase += 0.015;
          p.x += p.vx + Math.sin(p.phase) * 0.15;
          p.y += p.vy + Math.cos(p.phase) * 0.15;

          const dx = p.x - m.x;
          const dy = p.y - m.y;
          const dist = Math.sqrt(dx * dx + dy * dy);
          if (dist < 160) {
            const f = (160 - dist) / 160;
            p.x += (dx / dist) * f * 1.2;
            p.y += (dy / dist) * f * 1.2;
          }

          if (p.x < 0) p.x = w;
          if (p.x > w) p.x = 0;
          if (p.y < 0) p.y = h;
          if (p.y > h) p.y = 0;

          c.beginPath();
          c.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          c.fillStyle = p.col + p.a + ')';
          c.fill();

          for (let j = idx + 1; j < pts.length; j++) {
            const p2 = pts[j];
            const ldx = p.x - p2.x;
            const ldy = p.y - p2.y;
            const ldist = Math.sqrt(ldx * ldx + ldy * ldy);
            if (ldist < 85) {
              c.beginPath();
              c.moveTo(p.x, p.y);
              c.lineTo(p2.x, p2.y);
              c.strokeStyle = `rgba(229, 169, 60, ${(1 - ldist / 85) * 0.12})`;
              c.lineWidth = 0.6;
              c.stroke();
            }
          }
        });

        requestAnimationFrame(loop);
      }
      loop();
    }

    // 2. Rolling Number Plates Renderer (Etale 52 mechanical flip emulation)
    function renderNumberPlates(containerId, value) {
      const container = document.getElementById(containerId);
      if (!container) return;

      const num = parseInt(value, 10) || 0;
      const formatted = num.toLocaleString('en-IN');
      container.innerHTML = '<span class="plate-currency-symbol">₹</span>';

      for (let i = 0; i < formatted.length; i++) {
        const char = formatted[i];
        if (char === ',') {
          const comma = document.createElement('span');
          comma.className = 'plate-separator';
          comma.innerText = ',';
          container.appendChild(comma);
        } else {
          const slot = document.createElement('div');
          slot.className = 'plate-digit-slot';

          const ribbon = document.createElement('div');
          ribbon.className = 'plate-digit-ribbon';

          for (let d = 0; d <= 9; d++) {
            const item = document.createElement('div');
            item.className = 'plate-digit-item';
            item.innerText = d;
            ribbon.appendChild(item);
          }

          slot.appendChild(ribbon);
          container.appendChild(slot);

          const targetDigit = parseInt(char, 10) || 0;
          setTimeout(() => {
            ribbon.style.transform = `translateY(-${targetDigit * 44}px)`;
          }, i * 35);
        }
      }
    }

    // 3. 3D Tilt & Specular Follow Initialization
    function init3DTiltCards() {
      const cards = document.querySelectorAll('.tilt-card, .hero-showcase-box, .kpi-card');
      cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left - rect.width / 2;
          const y = e.clientY - rect.top - rect.height / 2;
          const rotX = -(y / rect.height) * 8;
          const rotY = (x / rect.width) * 8;
          card.style.transform = `perspective(1000px) rotateX(${rotX}deg) rotateY(${rotY}deg) translateY(-3px)`;
          card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
          card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
        });
        card.addEventListener('mouseleave', () => {
          card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
        });
      });
    }

    // 4. Golden Coin Sparkle Burst Effect
    function triggerLuckySparkle(e) {
      const x = (e && e.clientX) ? e.clientX : window.innerWidth / 2;
      const y = (e && e.clientY) ? e.clientY : window.innerHeight / 2;
      const count = 12;

      for (let i = 0; i < count; i++) {
        const p = document.createElement('div');
        p.className = 'sparkle-particle';
        const size = Math.random() * 5 + 3.5;
        p.style.width = `${size}px`;
        p.style.height = `${size}px`;
        p.style.left = `${x}px`;
        p.style.top = `${y}px`;

        const angle = Math.random() * Math.PI * 2;
        const velocity = Math.random() * 65 + 25;
        const dx = Math.cos(angle) * velocity;
        const dy = Math.sin(angle) * velocity - 25;

        p.style.setProperty('--dx', `${dx}px`);
        p.style.setProperty('--dy', `${dy}px`);
        p.style.background = Math.random() > 0.35 ? '#E5A93C' : '#F8333C';
        p.style.boxShadow = `0 0 6px ${p.style.background}`;

        document.body.appendChild(p);
        setTimeout(() => p.remove(), 700);
      }
    }
'''

# 5. Replacement for updateLiveCalculator to also trigger rolling number plates
update_calc_old = '''    function updateLiveCalculator() {
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
    }'''

update_calc_new = '''    function updateLiveCalculator() {
      const typeEl = document.getElementById('calc-event-type');
      const sliderEl = document.getElementById('calc-guest-slider');
      if (!typeEl || !sliderEl) return;

      const type = typeEl.value;
      const guests = parseInt(sliderEl.value, 10);
      const guestLbl = document.getElementById('calc-guest-lbl');
      if (guestLbl) guestLbl.innerText = guests;

      let avg = 2200;
      if (type === 'tonsure') avg = 1800;
      if (type === 'housewarming') avg = 2500;
      if (type === 'birthday') avg = 1500;
      if (type === 'wedding') avg = 3000;

      const avgTxt = document.getElementById('calc-avg-txt');
      if (avgTxt) avgTxt.innerText = `Avg ₹${avg.toLocaleString('en-IN')}/guest`;

      const total = guests * avg;
      const totalEl = document.getElementById('calc-total-shagun');
      if (totalEl) totalEl.innerText = '₹' + total.toLocaleString('en-IN');

      // Update mechanical rolling number plates (Etale 52)
      renderNumberPlates('calc-plate-mount', total);
    }'''

files = ['web_preview/index.html', 'web_preview/desktop.html', 'web_preview/mobile.html', 'build/web/index.html', 'web/index.html']

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject CSS if not already present
    if 'ETALE 52 & THREEUI LUXURY MOTION' not in content:
        content = content.replace('  </style>', css_to_inject + '\n  </style>')
        print(f'{path}: injected CSS')

    # 2. Inject Canvas after <body> if not present
    if 'id="ambient-canvas"' not in content:
        content = content.replace('<body>', '<body>\n' + canvas_html)
        print(f'{path}: injected Canvas')

    # 3. Inject Calculator Section right before Core Capabilities Section
    if 'id="calculator-section"' not in content:
        target_features = '    <!-- Core Capabilities Section -->'
        if target_features in content:
            content = content.replace(target_features, calculator_section_html + '\n' + target_features)
            print(f'{path}: injected Calculator Section before Features')
        else:
            print(f'{path}: WARNING target_features not found')

    # 4. Inject JS if not already present
    if 'ETALE 52 LUXURY MOTION ENGINE' not in content:
        target_js = '    // ==========================================\n    // 1. NAVIGATION & ROUTING'
        if target_js in content:
            content = content.replace(target_js, js_to_inject + '\n' + target_js)
            print(f'{path}: injected JS engine')
        else:
            # Fallback
            content = content.replace('    let currentLang', js_to_inject + '\n    let currentLang')
            print(f'{path}: injected JS engine fallback')

    # 5. Update updateLiveCalculator
    if update_calc_old in content:
        content = content.replace(update_calc_old, update_calc_new)
        print(f'{path}: updated updateLiveCalculator')

    # 6. Ensure initialization calls inside DOMContentLoaded
    init_hook = '      initAmbientCanvas();\n      init3DTiltCards();\n      updateLiveCalculator();\n'
    if 'initAmbientCanvas();' not in content:
        content = content.replace('renderEventsHub();', 'renderEventsHub();\n' + init_hook)
        print(f'{path}: added init hooks to DOMContentLoaded')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('All 5 files upgraded with ThreeUI / Etale 52 Luxury Motion Engine.')
