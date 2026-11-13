import shutil, os

# 1. Sync index.html
targets = ['web_preview/index.html', 'build/web/index.html', 'web/index.html']
for t in targets:
    shutil.copyfile('index.html', t)
    print(f"Copied index.html to {t}")

# 2. Sync all assets
for root, dirs, files in os.walk('assets'):
    rel = os.path.relpath(root, 'assets')
    for dest_base in ['web_preview/assets', 'build/web/assets', 'web/assets']:
        dest_dir = os.path.join(dest_base, rel)
        os.makedirs(dest_dir, exist_ok=True)
        for f in files:
            src_path = os.path.join(root, f)
            dest_path = os.path.join(dest_dir, f)
            shutil.copy2(src_path, dest_path)

print("All HTML and assets synchronized perfectly!")
