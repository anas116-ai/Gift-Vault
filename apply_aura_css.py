import os

aura_and_threeui_css = '''
/* ==========================================================================
   THREEUI TACTILE BUTTON SYSTEM & CHROMATIC TEXT SHIMMER
   ========================================================================== */
.threeui-tactile-btn, 
.btn-nav-signin, 
.btn-enter-vault, 
.btn-primary-pill,
.btn-footer-secondary,
.footer-action-btn {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  font-family: 'Outfit', sans-serif;
  font-weight: 700;
  letter-spacing: 0.02em;
  border-radius: 999px;
  cursor: pointer;
  border: none;
  outline: none;
  user-select: none;
  overflow: hidden;
  transition: transform 0.16s cubic-bezier(0.16, 1, 0.3, 1),
              box-shadow 0.16s cubic-bezier(0.16, 1, 0.3, 1),
              filter 0.16s ease;
  will-change: transform, box-shadow;
}

/* ThreeUI Tactile Crimson Specular Highlights */
.threeui-tactile-btn,
.btn-nav-signin,
.btn-enter-vault,
.footer-action-btn {
  background: linear-gradient(180deg, #B5223C 0%, #8E1529 60%, #700E1E 100%);
  color: #FFFFFF;
  border: 1px solid rgba(255, 232, 163, 0.45);
  box-shadow: 
    0 2px 0 #540814,
    0 4px 14px rgba(158, 27, 50, 0.38),
    0 12px 28px -4px rgba(158, 27, 50, 0.28),
    inset 0 1px 1px rgba(255, 255, 255, 0.45),
    inset 0 -1.5px 0 rgba(0, 0, 0, 0.3);
}

.threeui-tactile-btn::before,
.btn-nav-signin::before,
.btn-enter-vault::before,
.footer-action-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 200%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.22) 50%,
    transparent 100%
  );
  transform: skewX(-20deg);
  transition: left 0.6s ease;
  pointer-events: none;
}

.threeui-tactile-btn:hover::before,
.btn-nav-signin:hover::before,
.btn-enter-vault:hover::before,
.footer-action-btn:hover::before {
  left: 100%;
}

.threeui-tactile-btn:hover,
.btn-nav-signin:hover,
.btn-enter-vault:hover,
.footer-action-btn:hover {
  transform: translateY(-1.5px);
  filter: brightness(1.05);
  box-shadow: 
    0 3px 0 #540814,
    0 6px 18px rgba(158, 27, 50, 0.45),
    0 16px 32px -4px rgba(158, 27, 50, 0.35),
    inset 0 1px 1px rgba(255, 255, 255, 0.55),
    inset 0 -1.5px 0 rgba(0, 0, 0, 0.3);
}

.threeui-tactile-btn:active,
.btn-nav-signin:active,
.btn-enter-vault:active,
.footer-action-btn:active {
  transform: translateY(2px) scale(0.985);
  box-shadow: 
    0 0 0 #540814,
    0 2px 6px rgba(158, 27, 50, 0.3),
    inset 0 2px 4px rgba(0, 0, 0, 0.35);
  filter: brightness(0.96);
}

/* Secondary Tactile Button */
.btn-footer-secondary {
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  color: #FFFFFF;
  padding: 10px 20px;
  font-size: 13px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.2), inset 0 1px 1px rgba(255,255,255,0.2);
}
.btn-footer-secondary:hover {
  background: rgba(255, 255, 255, 0.16);
  transform: translateY(-1px);
}
.btn-footer-secondary:active {
  transform: translateY(1.5px);
}

/* ThreeUI Intro Chromatic Wordmark Motion */
@keyframes threeuiChromaticShimmer {
  0% {
    background-position: -200% center;
    filter: drop-shadow(0 0 0px rgba(229, 195, 101, 0));
  }
  50% {
    filter: drop-shadow(0 2px 14px rgba(212, 175, 55, 0.28));
  }
  100% {
    background-position: 200% center;
    filter: drop-shadow(0 0 0px rgba(229, 195, 101, 0));
  }
}

.section-title-tactile {
  background: linear-gradient(
    115deg,
    #0F172A 0%,
    #8B1528 35%,
    #D4AF37 50%,
    #8B1528 65%,
    #0F172A 100%
  );
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: threeuiChromaticShimmer 8s linear infinite;
}


/* ==========================================================================
   AURA.BUILD + THREEUI FILMSTRIP EDITORIAL CARDS
   ========================================================================== */
.aura-filmstrip-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.aura-editorial-card {
  position: relative;
  background: #FFFDF9;
  border: 1.5px solid rgba(226, 218, 205, 0.85);
  border-radius: 20px;
  padding: 26px 24px 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 4px 16px -2px rgba(15, 23, 42, 0.04), 0 1px 3px rgba(0, 0, 0, 0.02);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
}

.aura-editorial-card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #9E1B32 0%, #D4AF37 100%);
  opacity: 0;
  transition: opacity 0.25s ease;
}

.aura-editorial-card:hover {
  transform: translateY(-4px);
  border-color: rgba(181, 34, 60, 0.45);
  box-shadow: 
    0 20px 40px -15px rgba(158, 27, 50, 0.12),
    0 0 0 1px rgba(198, 146, 60, 0.35);
}

.aura-editorial-card:hover::after {
  opacity: 1;
}

.card-identity-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.card-icon-emblem {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.22s ease;
}
.aura-editorial-card:hover .card-icon-emblem {
  transform: scale(1.08);
}

.card-icon-emblem.crimson-theme {
  background: #FFF5F6;
  color: #9E1B32;
  border: 1.5px solid rgba(158, 27, 50, 0.2);
}

.card-icon-emblem.gold-theme {
  background: #FEFBF0;
  color: #B45309;
  border: 1.5px solid rgba(217, 119, 6, 0.22);
}

.card-icon-emblem.emerald-theme {
  background: #F0FDF4;
  color: #059669;
  border: 1.5px solid rgba(5, 150, 105, 0.2);
}

.card-number-badge {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  color: #64748B;
  background: #F8FAFC;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid #E2E8F0;
  letter-spacing: 0.05em;
}

.card-title {
  font-family: 'Outfit', sans-serif;
  font-size: 17.5px;
  font-weight: 800;
  color: #0F172A;
  margin-bottom: 8px;
  line-height: 1.3;
}

.card-description {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 13px;
  color: #475569;
  line-height: 1.55;
  margin-bottom: 18px;
  flex: 1;
}

.card-footer-status {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-top: 1px solid rgba(15, 23, 42, 0.06);
  padding-top: 12px;
  font-size: 11.5px;
  font-weight: 700;
}

.status-pill-green {
  color: #059669;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.status-pill-gold {
  color: #B45309;
  display: inline-flex;
  align-items: center;
  gap: 4px;
}

.status-code {
  font-family: 'JetBrains Mono', monospace;
  color: #64748B;
  font-size: 11px;
}


/* ==========================================================================
   AURA.BUILD LUXURY 4-COLUMN FOOTER
   ========================================================================== */
.footer-master {
  background: #0E1217;
  color: #CBD5E1;
  padding: 60px 0 32px;
  border-top: 1px solid rgba(198, 146, 60, 0.25);
  position: relative;
  overflow: hidden;
}

.footer-master::before {
  content: '';
  position: absolute;
  top: 0;
  left: 20%;
  width: 60%;
  height: 1px;
  background: linear-gradient(90deg, transparent 0%, #D4AF37 50%, transparent 100%);
}

.footer-grid-luxury {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1fr 1.1fr;
  gap: 40px;
  margin-bottom: 48px;
}

.footer-brand-lockup {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 14px;
  cursor: pointer;
  user-select: none;
}

.footer-emblem-box {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: linear-gradient(135deg, #9E1B32 0%, #680E1C 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(245, 208, 97, 0.45);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
}

.footer-brand-name {
  font-family: 'Outfit', sans-serif;
  font-size: 20px;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.01em;
  line-height: 1.1;
}

.footer-brand-tagline {
  font-family: 'Cinzel', serif;
  font-size: 9px;
  font-weight: 700;
  color: #B38438;
  letter-spacing: 0.12em;
  margin-top: 2px;
}

.footer-brand-desc {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 13px;
  color: #94A3B8;
  line-height: 1.6;
  max-width: 340px;
  margin-bottom: 18px;
}

.footer-trust-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.footer-chip {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 11px;
  font-weight: 600;
  color: #E2E8F0;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 4px 10px;
  border-radius: 999px;
}

.footer-heading {
  font-family: 'Cinzel', serif;
  font-size: 12px;
  font-weight: 700;
  color: #D4AF37;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 16px;
}

.footer-links-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-nav-link {
  color: #94A3B8;
  text-decoration: none;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 13px;
  font-weight: 500;
  transition: all 0.18s ease;
  display: inline-block;
}
.footer-nav-link:hover {
  color: #FFFFFF;
  transform: translateX(3px);
}

.footer-actions-wrap {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-action-btn {
  padding: 10px 18px;
  font-size: 13px;
  width: 100%;
}

.footer-audit-note {
  font-size: 11px;
  color: #64748B;
  margin-top: 6px;
  text-align: center;
}

.footer-bottom-bar {
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 12px;
  color: #64748B;
}

.footer-legal-links {
  display: flex;
  align-items: center;
  gap: 12px;
}

.dot-sep {
  color: #475569;
}

@media (max-width: 960px) {
  .aura-filmstrip-grid {
    grid-template-columns: 1fr;
  }
  .footer-grid-luxury {
    grid-template-columns: 1fr;
    gap: 32px;
  }
}
'''

target_css_files = [
    'assets/css/layout.css',
    'web_preview/assets/css/layout.css',
    'build/web/assets/css/layout.css',
    'web/assets/css/layout.css'
]

for css_file in target_css_files:
    if os.path.exists(css_file):
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Strip old aura block if present
        start = content.find('/* ==========================================================================\n   THREEUI TACTILE BUTTON SYSTEM & CHROMATIC TEXT SHIMMER')
        if start != -1:
            content = content[:start]
            
        content = content.rstrip() + '\n\n' + aura_and_threeui_css.strip() + '\n'
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated CSS in: {css_file}")

print("CSS updates completed successfully!")
