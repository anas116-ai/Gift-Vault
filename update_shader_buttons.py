# -*- coding: utf-8 -*-
import os
import shutil

with open('assets/js/shader-buttons.js', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace the liq calculation with the luxury maroon-lime fluid mixing wave
old_liq = "vec3 liq = mix(vec3(0.68, 0.95, 0.18), vec3(0.45, 0.72, 0.08), depth);"
new_liq = """vec3 limeWave = mix(vec3(0.62, 0.89, 0.15), vec3(0.52, 0.82, 0.10), depth);
    vec3 maroonWave = vec3(0.216, 0.0, 0.039);
    vec3 liq = mix(limeWave, maroonWave, clamp(depth * 0.38 + u_slosh * 0.32, 0.0, 0.55));"""

if old_liq in code:
    code = code.replace(old_liq, new_liq)
    print("✅ Replaced liq in shader-buttons.js with maroon-lime fluid wave!")
else:
    print("Notice: old_liq not found as exact match, checking current FS...")

with open('assets/js/shader-buttons.js', 'w', encoding='utf-8') as f:
    f.write(code)

# Sync to all 4 destinations
targets = [
    'web_preview/assets/js/shader-buttons.js',
    'build/web/assets/js/shader-buttons.js',
    'web/assets/js/shader-buttons.js'
]
for t in targets:
    shutil.copyfile('assets/js/shader-buttons.js', t)
    print(f"Synced shader-buttons.js to {t}")
