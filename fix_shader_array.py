with open('assets/js/shader-buttons.js', 'r', encoding='utf-8') as f:
    text = f.read()

bad = """    '  '  vec3 limeWave = mix(vec3(0.62, 0.89, 0.15), vec3(0.52, 0.82, 0.10), depth);',
    '  vec3 maroonWave = vec3(0.216, 0.0, 0.039);',
    '  vec3 liq = mix(limeWave, maroonWave, clamp(depth * 0.38 + u_slosh * 0.32, 0.0, 0.55));',',"""

good = """    '  vec3 limeWave = mix(vec3(0.62, 0.89, 0.15), vec3(0.52, 0.82, 0.10), depth);',
    '  vec3 maroonWave = vec3(0.216, 0.0, 0.039);',
    '  vec3 liq = mix(limeWave, maroonWave, clamp(depth * 0.38 + u_slosh * 0.32, 0.0, 0.55));',"""

text = text.replace(bad, good)

with open('assets/js/shader-buttons.js', 'w', encoding='utf-8') as f:
    f.write(text)

import shutil
for t in ['web_preview/assets/js/shader-buttons.js', 'build/web/assets/js/shader-buttons.js', 'web/assets/js/shader-buttons.js']:
    shutil.copyfile('assets/js/shader-buttons.js', t)
    print(f"Copied to {t}")
