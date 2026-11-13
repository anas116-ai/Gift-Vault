import os
import re

# 1. Update layout.css
with open('assets/css/layout.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .login-edge-right background to be pure luxury radial ivory without any weird circles
css = re.sub(
    r'\.login-edge-right\s*\{[^}]*\}',
    '''.login-edge-right {
  position: relative;
  width: 100%;
  height: 100vh;
  background: radial-gradient(circle at 50% 45%, #FFFFFF 0%, #FAF7F2 65%, #F4EFE6 100%);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  padding: 24px 32px 20px;
  overflow-y: auto;
  overflow-x: hidden;
}''',
    css
)

# Remove .login-bg-mandala and .login-bg-lattice rules, replace with clean subtle styling
mandala_css = '''/* Subtle ambient glow behind card - ZERO circular lines */
.login-card-backdrop-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 500px;
  height: 600px;
  background: radial-gradient(ellipse at center, rgba(245, 230, 211, 0.5) 0%, rgba(250, 247, 242, 0) 70%);
  pointer-events: none;
  z-index: 1;
}

.login-narrative-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 232, 163, 0.35);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  padding: 6px 14px;
  border-radius: 999px;
  font-family: 'Cinzel', serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: #FFE8A3;
  margin-bottom: 14px;
}

.login-narrative-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 20px;
}

.narrative-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(20, 5, 8, 0.65);
  border: 1px solid rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 6px 14px;
  border-radius: 999px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 12px;
  font-weight: 600;
  color: #F8FAFC;
}
'''

if '.login-card-backdrop-glow' not in css:
    css += '\n\n' + mandala_css

with open('assets/css/layout.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated layout.css')

# 2. Update index.html and replicas
html_files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

old_narrative_pattern = re.compile(
    r'<div class="login-edge-narrative">.*?<h2 class="login-edge-heading">Every Sacred Blessing, Preserved</h2>.*?</div>',
    re.DOTALL
)

new_narrative = '''<div class="login-edge-narrative">
          <div class="login-narrative-tag">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#FFE8A3" stroke-width="2.2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <span>THE SACRED SHAGUN SANCTUARY</span>
          </div>
          <h2 class="login-edge-heading">Timeless Blessings, Preserved in High-Fidelity</h2>
          <p class="login-edge-subtext">The sovereign digital ledger for royal weddings, housewarmings, and prestigious Indian ceremonies. 100% offline vault architecture with instant thermal printing.</p>
          <div class="login-narrative-pills">
            <span class="narrative-pill"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> 256-Bit Vault Security</span>
            <span class="narrative-pill"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg> 0.2s Slip Printing</span>
            <span class="narrative-pill"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg> 100% Offline Ledger</span>
          </div>
        </div>'''

for fn in html_files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace narrative (removes carousel pills)
    html = old_narrative_pattern.sub(new_narrative, html)

    # Remove the SVG mandala circles completely and lattice
    html = re.sub(
        r'<!-- Creative Background Elements -->\s*<div class="login-bg-lattice"></div>\s*<svg class="login-bg-mandala".*?</svg>',
        '<!-- Soft ambient warmth behind card (No circular lines) -->\n        <div class="login-card-backdrop-glow"></div>',
        html,
        flags=re.DOTALL
    )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated: {fn}')

print('HTML files updated successfully.')
