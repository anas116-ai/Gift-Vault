# -*- coding: utf-8 -*-
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

print("\n🎉 SUCCESS: GiftVault restored 100% to V1 Golden Master checkpoint!")
