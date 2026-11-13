# -*- coding: utf-8 -*-
"""
Update web_preview/index.html with the Official Logo-Design Skill Vector Suite
"""

with open(r"c:\Project\Gift Valut\web_preview\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update header logo to use the new vector SVG Concept A by default
old_img = 'src="/logos/concept_1_kalasam_crest.jpg"'
new_img = 'src="/logos/vector/concept-a-symbol.png"'
if old_img in html:
    html = html.replace(old_img, new_img)

# Update the showcase banner with the Official Vector Logo Suite + Photorealistic variations
vector_banner_code = '''<!-- ============================================================== -->
  <!-- 1.5 LOGO DESIGN SKILL: OFFICIAL VECTOR & CRAFTSMANSHIP SUITE -->
  <!-- ============================================================== -->
  <section class="max-w-7xl mx-auto px-4 lg:px-8 pt-4 pb-2 w-full">
    <div class="spotlight-card p-5 border-2 border-byzantine-500/50 bg-gradient-to-r from-vault-card via-byzantine-50/60 to-vault-card shadow-lg space-y-4">
      
      <!-- Banner Header -->
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-3 border-b border-vault-border/80 pb-3">
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-black px-3 py-1 rounded-full bg-byzantine-500 text-vault-dark font-telugu-title shadow-sm">🎯 LOGO-DESIGN SKILL OUTPUT</span>
            <h3 class="font-bold text-base text-vault-dark font-telugu-title">ప్రొఫెషనల్ వెక్టర్ లోగో మాస్టర్ సూట్</h3>
          </div>
          <p class="text-xs text-stone-600 mt-1">
            <strong>Logo-Design Skill</strong> సూత్రాల ప్రకారం (16px టెస్ట్, వన్-కలర్ ప్రెసిషన్, ప్యూర్ జామెట్రిక్ ఆర్స్ & లాకప్స్) రూపొందించబడిన <strong>అఫీషియల్ వెక్టర్ మార్క్స్</strong> + <strong>3D ఫిజికల్ మెటల్ వేరియేషన్స్</strong>.
          </p>
        </div>
        
        <div class="flex items-center gap-2">
          <a href="/logo_test_sheet.html" target="_blank" class="px-3 py-1.5 rounded-xl bg-vault-dark text-byzantine-400 font-bold text-xs hover:bg-stone-800 shadow-2xs border border-byzantine-500/30 flex items-center gap-1.5 btn-tactile">
            <span>🔬</span>
            <span>16px-256px టెస్ట్ షీట్ ఓపెన్ చేయండి ↗</span>
          </a>
        </div>
      </div>

      <!-- SECTION 1: 3 OFFICIAL VECTOR CONCEPTS (TESTED AT 16px - 256px) -->
      <div>
        <div class="flex items-center justify-between mb-2">
          <span class="text-xs font-bold text-byzantine-900 uppercase tracking-wider bg-byzantine-100 px-2.5 py-0.5 rounded-md">★ అధికారిక వెక్టర్ లోగో కాన్సెప్ట్స్ (Pure Geometric SVGs)</span>
          <span class="text-[10px] text-jade-700 font-bold bg-jade-50 px-2 py-0.5 rounded border border-jade-200">Svg-Audit స్కోర్: పాస్</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-3.5">
          
          <!-- Concept A (Recommended) -->
          <div onclick="selectAppLogo('/logos/vector/concept-a-symbol.png', 'Concept A: ఇంపీరియల్ లోటస్ GV మోనోగ్రామ్')" class="cursor-pointer group p-3.5 rounded-2xl bg-white border-2 border-byzantine-500 shadow-glow-sm hover:shadow-glow-gold transition-all relative">
            <span class="absolute top-2 right-2 px-2 py-0.5 rounded-full bg-byzantine-500 text-vault-dark text-[9px] font-bold shadow-2xs">★ రికమండెడ్</span>
            <div class="aspect-video rounded-xl overflow-hidden bg-vault-dark mb-2.5 flex items-center justify-center p-2 border border-byzantine-500/20">
              <img src="/logos/vector/concept-a-lockup.png" alt="Concept A Lockup" class="w-full h-full object-contain group-hover:scale-105 transition-transform">
            </div>
            <div class="flex items-center justify-between">
              <div>
                <span class="font-bold text-vault-dark block text-xs font-telugu-title">Concept A: ఇంపీరియల్ లోటస్ GV మోనోగ్రామ్</span>
                <span class="text-[10px] text-stone-500 block mt-0.5">5-రేకుల రాజ కమల కిరీటం & కేంద్ర శగున్ నాణెం</span>
              </div>
              <button class="px-3 py-1 rounded-lg bg-vault-dark text-byzantine-400 font-bold text-[10px] btn-tactile">ఎంచుకోండి</button>
            </div>
          </div>

          <!-- Concept B -->
          <div onclick="selectAppLogo('/logos/vector/concept-b-symbol.png', 'Concept B: సావరిన్ ట్రెజరీ మెడల్లియన్')" class="cursor-pointer group p-3.5 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
            <div class="aspect-video rounded-xl overflow-hidden bg-vault-dark mb-2.5 flex items-center justify-center p-2 border border-vault-border">
              <img src="/logos/vector/concept-b-lockup.png" alt="Concept B Lockup" class="w-full h-full object-contain group-hover:scale-105 transition-transform">
            </div>
            <div class="flex items-center justify-between">
              <div>
                <span class="font-bold text-vault-dark block text-xs font-telugu-title">Concept B: సావరిన్ ట్రెజరీ మెడల్లియన్</span>
                <span class="text-[10px] text-stone-500 block mt-0.5">సంప్రదాయ కాసుల రౌండ్ సీల్ & కలశ జామెట్రీ</span>
              </div>
              <button class="px-3 py-1 rounded-lg bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[10px] border border-vault-border btn-tactile">ఎంచుకోండి</button>
            </div>
          </div>

          <!-- Concept C -->
          <div onclick="selectAppLogo('/logos/vector/concept-c-symbol.png', 'Concept C: ఆర్కిటెక్చరల్ బెవెల్డ్ GV')" class="cursor-pointer group p-3.5 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
            <div class="aspect-video rounded-xl overflow-hidden bg-vault-dark mb-2.5 flex items-center justify-center p-2 border border-vault-border">
              <img src="/logos/vector/concept-c-lockup.png" alt="Concept C Lockup" class="w-full h-full object-contain group-hover:scale-105 transition-transform">
            </div>
            <div class="flex items-center justify-between">
              <div>
                <span class="font-bold text-vault-dark block text-xs font-telugu-title">Concept C: ఆర్కిటెక్చరల్ బెవెల్డ్ GV</span>
                <span class="text-[10px] text-stone-500 block mt-0.5">కార్టియర్-రోలెక్స్ తరహా 3D ఫేసిటెడ్ మెటల్ లైన్లు</span>
              </div>
              <button class="px-3 py-1 rounded-lg bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[10px] border border-vault-border btn-tactile">ఎంచుకోండి</button>
            </div>
          </div>

        </div>
      </div>

      <!-- SECTION 2: 6 PHOTOREALISTIC 3D PHYSICAL FINISHES -->
      <div class="pt-2 border-t border-vault-border/70">
        <span class="text-[11px] font-bold text-stone-700 uppercase tracking-wider block mb-2">రియలిస్టిక్ 3D ఫిజికల్ మెటల్ & జ్యువెల్రీ ఫినిషెస్ (Photorealistic Variations)</span>
        
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2 text-xs">
          
          <div onclick="selectAppLogo('/logos/gv/gv_01_beveled_gold_ruby.jpg', '24K సాలిడ్ బెవెల్డ్ గోల్డ్ & రూబీ')" class="cursor-pointer group p-2 rounded-xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-lg overflow-hidden bg-vault-dark mb-1">
              <img src="/logos/gv/gv_01_beveled_gold_ruby.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
            </div>
            <span class="font-bold text-[10px] block truncate text-vault-dark">24K గోల్డ్ & రూబీ</span>
          </div>

          <div onclick="selectAppLogo('/logos/gv/gv_02_champagne_pave_diamonds.jpg', 'చాంపైన్ గోల్డ్ & మైక్రో డైమండ్స్')" class="cursor-pointer group p-2 rounded-xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-lg overflow-hidden bg-vault-dark mb-1">
              <img src="/logos/gv/gv_02_champagne_pave_diamonds.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
            </div>
            <span class="font-bold text-[10px] block truncate text-vault-dark">చాంపైన్ & వజ్రాలు</span>
          </div>

          <div onclick="selectAppLogo('/logos/gv/gv_03_burgundy_enamel_rosegold.jpg', 'కుంకుమ ఎనామెల్ & రోజ్ గోల్డ్')" class="cursor-pointer group p-2 rounded-xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-lg overflow-hidden bg-vault-dark mb-1">
              <img src="/logos/gv/gv_03_burgundy_enamel_rosegold.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
            </div>
            <span class="font-bold text-[10px] block truncate text-vault-dark">కుంకుమ & రోజ్ గోల్డ్</span>
          </div>

          <div onclick="selectAppLogo('/logos/gv/gv_04_minted_bullion_coin.jpg', 'మింటెడ్ బులియన్ గోల్డ్ కాయిన్')" class="cursor-pointer group p-2 rounded-xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-lg overflow-hidden bg-vault-dark mb-1">
              <img src="/logos/gv/gv_04_minted_bullion_coin.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
            </div>
            <span class="font-bold text-[10px] block truncate text-vault-dark">మింటెడ్ బులియన్ కాయిన్</span>
          </div>

          <div onclick="selectAppLogo('/logos/gv/gv_05_black_ceramic_liquid_gold.jpg', 'బ్లాక్ సిరామిక్ & లిక్విడ్ గోల్డ్')" class="cursor-pointer group p-2 rounded-xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-lg overflow-hidden bg-vault-dark mb-1">
              <img src="/logos/gv/gv_05_black_ceramic_liquid_gold.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
            </div>
            <span class="font-bold text-[10px] block truncate text-vault-dark">సిరామిక్ & లిక్విడ్ గోల్డ్</span>
          </div>

          <div onclick="selectAppLogo('/logos/gv/gv_06_watchmaker_horlogerie_gold.jpg', 'వాచ్‌మేకర్ హార్లోజరీ గోల్డ్')" class="cursor-pointer group p-2 rounded-xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-lg overflow-hidden bg-vault-dark mb-1">
              <img src="/logos/gv/gv_06_watchmaker_horlogerie_gold.jpg" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
            </div>
            <span class="font-bold text-[10px] block truncate text-vault-dark">వాచ్‌మేకర్ హార్లోజరీ</span>
          </div>

        </div>
      </div>

    </div>
  </section>'''

# Replace the showcase section in html
idx_start = html.find('<!-- 1.5 LOGO SELECTION SUITE')
if idx_start != -1:
    idx_end = html.find('</section>', idx_start) + len('</section>')
    html = html[:idx_start] + vector_banner_code + html[idx_end:]

# Write files
with open(r"c:\Project\Gift Valut\web_preview\index.html", "w", encoding="utf-8") as f:
    f.write(html)
with open(r"c:\Project\Gift Valut\web\index.html", "w", encoding="utf-8") as f:
    f.write(html)
with open(r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\giftvault_interactive_preview.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Logo-Design Skill Vector Suite injected across all files!")
