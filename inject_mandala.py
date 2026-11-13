import os
import re

mandala_svg = '''
        <!-- Creative Background Elements -->
        <div class="login-bg-lattice"></div>
        <svg class="login-bg-mandala" viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="200" cy="200" r="180" stroke="#8B1528" stroke-width="2"/>
          <circle cx="200" cy="200" r="150" stroke="#B38438" stroke-width="1.5" stroke-dasharray="4 4"/>
          <circle cx="200" cy="200" r="120" stroke="#8B1528" stroke-width="2"/>
          <circle cx="200" cy="200" r="80" stroke="#B38438" stroke-width="1.5"/>
          <circle cx="200" cy="200" r="40" stroke="#8B1528" stroke-width="2"/>
          <path d="M200 20 L200 380 M20 200 L380 200 M72 72 L328 328 M72 328 L328 72" stroke="#B38438" stroke-width="1.2" stroke-dasharray="3 3"/>
          <polygon points="200,60 220,160 320,180 220,200 200,300 180,200 80,180 180,160" stroke="#8B1528" stroke-width="1.8" fill="rgba(158, 27, 50, 0.03)"/>
        </svg>
'''

target_files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Inject into .login-edge-right if not already there
        if 'login-bg-mandala' not in content:
            content = content.replace(
                '<div class="login-edge-right">',
                '<div class="login-edge-right">' + mandala_svg
            )
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Injected into {fpath}")
        else:
            print(f"Already in {fpath}")

print("Mandala injection complete!")
