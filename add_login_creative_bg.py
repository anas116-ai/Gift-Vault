import os

login_bg_css = '''
/* Creative Background Mandala & Jali Lattice for Login Page */
.login-edge-right {
  width: 100%;
  height: 100vh;
  background: #FAF7F2;
  padding: 28px 44px 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  overflow-y: auto;
  position: relative;
}

.login-bg-mandala {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 600px;
  height: 600px;
  opacity: 0.055;
  pointer-events: none;
  z-index: 1;
}

.login-bg-lattice {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(rgba(198, 146, 60, 0.15) 1px, transparent 1px),
                    radial-gradient(rgba(158, 27, 50, 0.1) 1px, transparent 1px);
  background-size: 24px 24px;
  background-position: 0 0, 12px 12px;
  opacity: 0.55;
  pointer-events: none;
  z-index: 1;
}

.exact-auth-card-edge {
  position: relative;
  z-index: 5;
}

.login-right-top,
.login-bottom-trust-edge {
  position: relative;
  z-index: 5;
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
        
        content = content.rstrip() + '\n\n' + login_bg_css.strip() + '\n'
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {css_file}")

print("Login creative bg CSS added!")
