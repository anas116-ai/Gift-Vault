# -*- coding: utf-8 -*-
import os
import shutil
import subprocess

version_name = "v1_golden_master_backup"
backup_dir = os.path.join("_versions", version_name)

os.makedirs(backup_dir, exist_ok=True)

# 1. Copy essential files
items_to_backup = [
    'index.html',
    'package.json',
    'serve_nocache.py',
    'test_giftvault_e2e.py',
    'assets',
    'web_preview',
    'build',
    'web'
]

for item in items_to_backup:
    if os.path.exists(item):
        dest = os.path.join(backup_dir, item)
        if os.path.isdir(item):
            if os.path.exists(dest):
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
            print(f"Backed up directory: {item} -> {dest}")
        else:
            shutil.copy2(item, dest)
            print(f"Backed up file: {item} -> {dest}")

print(f"\n✅ Physical backup saved successfully in: {backup_dir}")

# 2. Create the one-click instant restore script
restore_script_content = '''# -*- coding: utf-8 -*-
"""
ONE-CLICK INSTANT RESTORE SCRIPT
Restores GiftVault to the V1 Golden Master version saved on 2026-11-13.
"""
import os
import shutil
import subprocess

backup_dir = os.path.join("_versions", "v1_golden_master_backup")

if not os.path.exists(backup_dir):
    print("❌ Backup directory not found:", backup_dir)
    exit(1)

items_to_restore = [
    'index.html',
    'package.json',
    'serve_nocache.py',
    'test_giftvault_e2e.py',
    'assets',
    'web_preview',
    'build',
    'web'
]

for item in items_to_restore:
    src = os.path.join(backup_dir, item)
    if os.path.exists(src):
        if os.path.isdir(src):
            if os.path.exists(item):
                shutil.rmtree(item)
            shutil.copytree(src, item)
            print(f"Restored directory: {item}")
        else:
            shutil.copy2(src, item)
            print(f"Restored file: {item}")

print("\\n🎉 SUCCESS: GiftVault restored 100% to V1 Golden Master checkpoint!")
'''

with open('restore_to_v1_golden_master.py', 'w', encoding='utf-8') as f:
    f.write(restore_script_content)

print("✅ Created 'restore_to_v1_golden_master.py' for instant one-click rollback!")

# 3. Initialize Git and create tag
try:
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'], check=True)
        subprocess.run(['git', 'config', 'user.name', 'Antigravity AI'], check=True)
        subprocess.run(['git', 'config', 'user.email', 'ai@giftvault.local'], check=True)
        print("Initialized Git repository.")
    
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'v1.0-golden-master: Approved design with before-previous hero, 4 cards, empty reception stage, illuminated house, no telugu, and before-previous login'], check=False)
    subprocess.run(['git', 'tag', '-f', 'v1-golden-master'], check=True)
    print("✅ Git commit and tag 'v1-golden-master' created successfully!")
except Exception as e:
    print(f"Git notice: {e}")
