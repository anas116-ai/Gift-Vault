import os

targets = [
    'assets/js/shader-buttons.js',
    'web_preview/assets/js/shader-buttons.js',
    'build/web/assets/js/shader-buttons.js',
    'web/assets/js/shader-buttons.js'
]

for t in targets:
    if os.path.exists(t):
        with open(t, 'r', encoding='utf-8') as f:
            code = f.read()
        # Remove '#btn-hero-signin', from selectors
        code = code.replace("      '#btn-hero-signin',\n", "")
        # Also in initTactileButton, return early if btn has class btn-ref1-primary or id btn-hero-signin
        if "if (btn.classList && btn.classList.contains('btn-ref1-primary')) return;" not in code:
            code = code.replace("function initTactileButton(btn) {", "function initTactileButton(btn) {\n    if (!btn || btn.id === 'btn-hero-signin' || (btn.classList && btn.classList.contains('btn-ref1-primary'))) return;")
        with open(t, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"Updated {t}")
