import os

clean_styles_css = '''
/* ==========================================================================
   NORMAL INLINE NAVBAR (No Oval Box Container) & TACTILE THREEUI BUTTONS
   ========================================================================== */
.header-glass {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: blur(18px) saturate(180%);
  -webkit-backdrop-filter: blur(18px) saturate(180%);
  border-bottom: 1px solid rgba(226, 218, 205, 0.7);
  padding: 0;
  box-shadow: 0 2px 12px rgba(15, 23, 42, 0.04);
}

.nav-container-luxury {
  max-width: 1360px;
  width: 100%;
  height: 68px;
  margin: 0 auto;
  padding: 0 32px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Normal Inline Navigation (Zero Oval Box, Clean Typography) */
.nav-links-normal {
  display: flex;
  align-items: center;
  gap: 32px;
}

.nav-clean-link {
  color: #1E293B;
  text-decoration: none;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: -0.01em;
  transition: color 0.18s ease;
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.nav-clean-link:hover {
  color: #9E1B32;
}

.nav-counter-link {
  position: relative;
}

.nav-live-dot {
  width: 6.5px;
  height: 6.5px;
  border-radius: 50%;
  background: #10B981;
  box-shadow: 0 0 0 2.5px rgba(16, 185, 129, 0.2);
}

.nav-right-actions {
  display: flex;
  align-items: center;
  gap: 14px;
}

/* ==========================================================================
   THREEUI EXACT TACTILE BUTTON SYSTEM (Single Layer, Smooth Ambient Fluid)
   Source: SHA-256 6f56c4f91814 nexus-tactile
   ========================================================================== */
.btn-tactile-primary,
.threeui-tactile-btn,
.btn-nav-signin,
.btn-enter-vault {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-family: 'Outfit', sans-serif;
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.02em;
  border-radius: 999px;
  border: 0 !important; /* No double borders */
  padding: 10px 22px;
  cursor: pointer;
  outline: none;
  user-select: none;
  overflow: hidden;
  background: linear-gradient(135deg, #A81B34 0%, #881427 100%) !important;
  color: #FFFFFF !important;
  box-shadow: 
    0 16px 32px -4px rgba(158, 27, 50, 0.42),
    0 3px 8px rgba(15, 23, 42, 0.12),
    inset 0 1px 0 rgba(255, 255, 255, 0.22) !important;
  transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1),
              box-shadow 0.22s cubic-bezier(0.16, 1, 0.3, 1),
              filter 0.22s ease !important;
  will-change: transform, box-shadow;
}

/* Ambient Fluid Sheen on ThreeUI Button */
.btn-tactile-primary::before,
.threeui-tactile-btn::before,
.btn-nav-signin::before,
.btn-enter-vault::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 200%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.25) 50%,
    transparent 100%
  );
  transform: skewX(-20deg);
  transition: left 0.5s ease;
  pointer-events: none;
}

.btn-tactile-primary:hover::before,
.threeui-tactile-btn:hover::before,
.btn-nav-signin:hover::before,
.btn-enter-vault:hover::before {
  left: 100%;
}

/* Smooth Fluid Hover Lift */
.btn-tactile-primary:hover,
.threeui-tactile-btn:hover,
.btn-nav-signin:hover,
.btn-enter-vault:hover {
  transform: translateY(-2px);
  filter: brightness(1.06);
  box-shadow: 
    0 22px 42px -4px rgba(158, 27, 50, 0.52),
    0 4px 10px rgba(15, 23, 42, 0.16),
    inset 0 1px 0 rgba(255, 255, 255, 0.3) !important;
}

/* Tactile Active Press */
.btn-tactile-primary:active,
.threeui-tactile-btn:active,
.btn-nav-signin:active,
.btn-enter-vault:active {
  transform: translateY(1px) scale(0.985) !important;
  box-shadow: 
    0 4px 12px rgba(158, 27, 50, 0.3),
    inset 0 2px 4px rgba(0, 0, 0, 0.25) !important;
  filter: brightness(0.97);
}


/* ==========================================================================
   RESTORED PREVIOUS FOOTER (Clean Ivory & Light Warmth)
   ========================================================================== */
.footer-master {
  background: #FAF7F2 !important;
  color: #475569 !important;
  padding: 54px 0 30px !important;
  margin-top: 60px;
  border-top: 1px solid rgba(226, 218, 205, 0.9) !important;
}

.footer-master .footer-brand-name {
  color: #8B1528 !important;
}

.footer-master a {
  color: #64748B !important;
  transition: color 0.16s ease;
}

.footer-master a:hover {
  color: #8B1528 !important;
}
'''

# Update layout.css
for path in ['assets/css/layout.css', 'web_preview/assets/css/layout.css', 'build/web/assets/css/layout.css', 'web/assets/css/layout.css']:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        start = content.find('/* ==========================================================================\n   NORMAL INLINE NAVBAR')
        if start != -1:
            content = content[:start]
            
        content = content.rstrip() + '\n\n' + clean_styles_css.strip() + '\n'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")

# Update landing-sections.css
for path in ['assets/css/landing-sections.css', 'web_preview/assets/css/landing-sections.css', 'build/web/assets/css/landing-sections.css', 'web/assets/css/landing-sections.css']:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(r'\.footer-master\s*\{[^}]*\}', '''.footer-master {
  background: #FAF7F2 !important;
  color: #475569 !important;
  padding: 54px 0 30px !important;
  margin-top: 60px;
  border-top: 1px solid rgba(226, 218, 205, 0.9) !important;
}''', content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")

print("Clean styles successfully applied!")
