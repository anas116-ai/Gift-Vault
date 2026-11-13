import os

fix_css = """
/* Ensure perfect viewport centering for #view-login.active */
#view-login.active {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100vw !important;
  min-height: 100vh !important;
  height: 100vh !important;
  overflow-y: auto !important;
  background: radial-gradient(circle at 10% 20%, rgba(212, 160, 23, 0.05) 0%, transparent 40%),
              radial-gradient(circle at 90% 80%, rgba(138, 21, 38, 0.04) 0%, transparent 40%),
              #FAF8F5 !important;
  padding: 30px 20px !important;
  box-sizing: border-box !important;
}

.login-topbar-wrapper {
  width: 100% !important;
  max-width: 1060px !important;
  margin: 0 auto 14px auto !important;
  display: flex !important;
  justify-content: flex-start !important;
}

.login-master-frame {
  width: 100% !important;
  max-width: 1060px !important;
  margin: 0 auto !important;
  box-sizing: border-box !important;
}
"""

for p in ['assets/css/layout.css', 'web_preview/assets/css/layout.css', 'build/web/assets/css/layout.css', 'web/assets/css/layout.css']:
    if os.path.exists(p):
        with open(p, 'a', encoding='utf-8') as f:
            f.write(fix_css)
        print("Updated CSS in", p)

print("Centering CSS applied!")
