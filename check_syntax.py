import subprocess

scripts = [
    'assets/js/shader-buttons.js',
    'assets/js/app.js',
    'assets/js/components/hero3d.js',
    'assets/js/store.js',
    'assets/js/i18n.js'
]

for s in scripts:
    res = subprocess.run(['node', '-c', s], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ Syntax Error in {s}:\n{res.stderr}")
    else:
        print(f"✅ {s} is clean")
