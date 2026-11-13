# -*- coding: utf-8 -*-
"""
Inject 10-Logo Master Suite with 6 Hyper-Realistic GV Monogram Variations + 4 Heritage Master Concepts
"""

import os

with open(r"c:\Project\Gift Valut\web_preview\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the showcase banner with the comprehensive 10-Logo Suite
old_showcase_start = '<!-- ============================================================== -->\n  <!-- 1.5 LOGO SELECTION SUITE'
old_showcase_end = '</section>'

idx_start = html.find('<!-- 1.5 LOGO SELECTION SUITE')
if idx_start != -1:
    idx_end = html.find('</section>', idx_start) + len('</section>')
    
    new_10_logo_showcase = '''<!-- 1.5 LOGO SELECTION SUITE: 10 LUXURY CONCEPTS (6 HYPER-REALISTIC GV VARIATIONS + 4 HERITAGE CONCEPTS) -->
  <section class="max-w-7xl mx-auto px-4 lg:px-8 pt-4 pb-2 w-full">
    <div class="spotlight-card p-4 border border-byzantine-500/40 bg-gradient-to-r from-vault-card via-byzantine-50/50 to-vault-card shadow-sm space-y-3">
      
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-3 border-b border-vault-border/70 pb-3">
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-byzantine-500 text-vault-dark font-telugu-title shadow-2xs">👑 10 లగ్జరీ లోగోల కలెక్షన్</span>
            <h3 class="font-bold text-sm text-vault-dark font-telugu-title">మీ ఎంపిక కోసం 10 రియలిస్టిక్ లోగో డిజైన్లు</h3>
          </div>
          <p class="text-xs text-stone-600 mt-1">
            మీరు ఇష్టపడిన <strong class="text-byzantine-900 font-bold">Concept 3 ('GV' మోనోగ్రామ్)</strong> ఆధారంగా రూపొందించిన <strong>6 అల్ట్రా-రియలిస్టిక్ ఫిజికల్ మెటల్ వేరియేషన్లు</strong> + <strong>4 హెరిటేజ్ కాన్సెప్ట్స్</strong>. ఏదైనా లోగోపై క్లిక్ చేసి వెంటనే లైవ్‌గా హెడర్‌లో ఎలా ఉంటుందో చూడండి!
          </p>
        </div>
        <div class="flex items-center gap-2">
          <span class="text-xs font-bold text-jade-800 bg-jade-50 px-3 py-1 rounded-xl border border-jade-200">
            ✓ 10 డిజైన్లు సిద్ధంగా ఉన్నాయి
          </span>
        </div>
      </div>

      <!-- SECTION 1: 6 HYPER-REALISTIC 3D GV MONOGRAMS (USER'S PREFERRED CONCEPT) -->
      <div>
        <div class="flex items-center gap-1.5 mb-2">
          <span class="text-[11px] font-bold text-byzantine-900 uppercase tracking-wider bg-byzantine-100 px-2 py-0.5 rounded-md">★ ప్రాధాన్యత: రియలిస్టిక్ 'GV' మోనోగ్రామ్ వేరియేషన్స్ (6 Designs)</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5 text-xs">
          
          <!-- GV Var 1 -->
          <div onclick="selectAppLogo('/logos/gv/gv_01_beveled_gold_ruby.jpg', 'GV 01: సాలిడ్ 24K బెవెల్డ్ గోల్డ్ & రూబీ')" class="cursor-pointer group p-2 rounded-2xl bg-white border-2 border-byzantine-500 shadow-2xs hover:shadow-glow-gold transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/gv/gv_01_beveled_gold_ruby.jpg" alt="GV Var 1" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-byzantine-300 text-[8px] font-bold">GV-01</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">24K బెవెల్డ్ గోల్డ్ & రూబీ</span>
            <span class="text-[9px] text-stone-500 block">కార్టియర్-స్టైల్ సాలిడ్ గోల్డ్ & రూబీ రత్నం</span>
            <button class="mt-1.5 w-full py-0.5 rounded-md bg-vault-dark text-byzantine-400 font-bold text-[9px] btn-tactile">ఎంచుకోండి</button>
          </div>

          <!-- GV Var 2 -->
          <div onclick="selectAppLogo('/logos/gv/gv_02_champagne_pave_diamonds.jpg', 'GV 02: బ్రష్డ్ చాంపైన్ గోల్డ్ & పావే డైమండ్స్')" class="cursor-pointer group p-2 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/gv/gv_02_champagne_pave_diamonds.jpg" alt="GV Var 2" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-byzantine-300 text-[8px] font-bold">GV-02</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">చాంపైన్ గోల్డ్ & డైమండ్స్</span>
            <span class="text-[9px] text-stone-500 block">సాటిన్ బ్రష్డ్ మెటల్ & మైక్రో పావే వజ్రాలు</span>
            <button class="mt-1.5 w-full py-0.5 rounded-md bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[9px] border border-vault-border btn-tactile">ఎంచుకోండి</button>
          </div>

          <!-- GV Var 3 -->
          <div onclick="selectAppLogo('/logos/gv/gv_03_burgundy_enamel_rosegold.jpg', 'GV 03: రాయల్ బర్గండీ ఎనామెల్ & రోజ్ గోల్డ్')" class="cursor-pointer group p-2 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/gv/gv_03_burgundy_enamel_rosegold.jpg" alt="GV Var 3" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-byzantine-300 text-[8px] font-bold">GV-03</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">కుంకుమ ఎనామెల్ & రోజ్ గోల్డ్</span>
            <span class="text-[9px] text-stone-500 block">గిల్లోచే కుంకుమ డయల్ & 18K రోజ్ గోల్డ్</span>
            <button class="mt-1.5 w-full py-0.5 rounded-md bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[9px] border border-vault-border btn-tactile">ఎంచుకోండి</button>
          </div>

          <!-- GV Var 4 -->
          <div onclick="selectAppLogo('/logos/gv/gv_04_minted_bullion_coin.jpg', 'GV 04: మింటెడ్ 24K ప్యూర్ గోల్డ్ కాయిన్')" class="cursor-pointer group p-2 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/gv/gv_04_minted_bullion_coin.jpg" alt="GV Var 4" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-byzantine-300 text-[8px] font-bold">GV-04</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">మింటెడ్ శగున్ గోల్డ్ కాయిన్</span>
            <span class="text-[9px] text-stone-500 block">హై-రిలీఫ్ 1 ట్రాయ్ ఔన్స్ సాలిడ్ గోల్డ్ కాయిన్</span>
            <button class="mt-1.5 w-full py-0.5 rounded-md bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[9px] border border-vault-border btn-tactile">ఎంచుకోండి</button>
          </div>

          <!-- GV Var 5 -->
          <div onclick="selectAppLogo('/logos/gv/gv_05_black_ceramic_liquid_gold.jpg', 'GV 05: బ్లాక్ సిరామిక్ & లిక్విడ్ గోల్డ్')" class="cursor-pointer group p-2 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/gv/gv_05_black_ceramic_liquid_gold.jpg" alt="GV Var 5" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-byzantine-300 text-[8px] font-bold">GV-05</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">బ్లాక్ సిరామిక్ & లిక్విడ్ గోల్డ్</span>
            <span class="text-[9px] text-stone-500 block">కార్వ్డ్ మాట్ సిరామిక్ & కింత్సుగి గోల్డ్ ఇన్‌లే</span>
            <button class="mt-1.5 w-full py-0.5 rounded-md bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[9px] border border-vault-border btn-tactile">ఎంచుకోండి</button>
          </div>

          <!-- GV Var 6 -->
          <div onclick="selectAppLogo('/logos/gv/gv_06_watchmaker_horlogerie_gold.jpg', 'GV 06: వాచ్‌మేకర్ హార్లోజరీ గోల్డ్ బ్రిడ్జ్')" class="cursor-pointer group p-2 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/gv/gv_06_watchmaker_horlogerie_gold.jpg" alt="GV Var 6" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-byzantine-300 text-[8px] font-bold">GV-06</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">వాచ్‌మేకర్ హార్లోజరీ గోల్డ్</span>
            <span class="text-[9px] text-stone-500 block">పాటెక్ ఫిలిప్ స్టైల్ గోల్డ్ స్కెలిటన్ & క్రిస్టల్</span>
            <button class="mt-1.5 w-full py-0.5 rounded-md bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[9px] border border-vault-border btn-tactile">ఎంచుకోండి</button>
          </div>

        </div>
      </div>

      <!-- SECTION 2: 4 HERITAGE MASTER CONCEPTS (FOR FULL COMPARISON) -->
      <div class="pt-2 border-t border-vault-border/60">
        <div class="flex items-center gap-1.5 mb-2">
          <span class="text-[11px] font-bold text-stone-700 uppercase tracking-wider bg-vault-cream px-2 py-0.5 rounded-md">హెరిటేజ్ కాన్సెప్ట్స్ (4 Original Concepts)</span>
        </div>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-2.5 text-xs">
          
          <!-- Concept 1 -->
          <div onclick="selectAppLogo('/logos/concept_1_kalasam_crest.jpg', 'రాయల్ మంగళ కలశం క్రెస్ట్')" class="cursor-pointer group p-2 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/concept_1_kalasam_crest.jpg" alt="Concept 1" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-stone-300 text-[8px] font-bold">హెరిటేజ్ 1</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">మంగళ కలశం క్రెస్ట్</span>
            <span class="text-[9px] text-stone-500 block">24K గోల్డ్ కలశం, కొబ్బరికాయ & నెమలి తోరణం</span>
          </div>

          <!-- Concept 2 -->
          <div onclick="selectAppLogo('/logos/concept_2_red_ledger.jpg', 'ఎర్ర వెల్వెట్ చదివింపుల పుస్తకం & స్వర్ణ కమలం')" class="cursor-pointer group p-2 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/concept_2_red_ledger.jpg" alt="Concept 2" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-stone-300 text-[8px] font-bold">హెరిటేజ్ 2</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">ఎర్ర పుస్తకం & స్వర్ణ కమలం</span>
            <span class="text-[9px] text-stone-500 block">చదివింపుల డైరీ & బంగారు కమల కిరీటం</span>
          </div>

          <!-- Concept 3 Original -->
          <div onclick="selectAppLogo('/logos/concept_3_gv_monogram.jpg', 'మోడ్రన్ GV మోనోగ్రామ్ (Original)')" class="cursor-pointer group p-2 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/concept_3_gv_monogram.jpg" alt="Concept 3" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-stone-300 text-[8px] font-bold">హెరిటేజ్ 3</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">GV మోనోగ్రామ్ (Original)</span>
            <span class="text-[9px] text-stone-500 block">ఒరిజినల్ వెక్టోరియల్ మోనోగ్రామ్</span>
          </div>

          <!-- Concept 4 -->
          <div onclick="selectAppLogo('/logos/concept_4_treasury_chest.jpg', 'రాయల్ ఖజానా పెట్టె')" class="cursor-pointer group p-2 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 transition-all">
            <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-1.5 relative">
              <img src="/logos/concept_4_treasury_chest.jpg" alt="Concept 4" class="w-full h-full object-cover group-hover:scale-105 transition-transform">
              <span class="absolute top-1 left-1 px-1.5 py-0.2 rounded bg-vault-dark/85 text-stone-300 text-[8px] font-bold">హెరిటేజ్ 4</span>
            </div>
            <span class="font-bold text-vault-dark block text-[10px] truncate font-telugu-title">రాయల్ ఖజానా పెట్టె</span>
            <span class="text-[9px] text-stone-500 block">దివ్యమైన కాంతుల బంగారు ఖజానా పెట్టె</span>
          </div>

        </div>
      </div>

    </div>
  </section>'''

    html = html[:idx_start] + new_10_logo_showcase + html[idx_end:]
    print("Updated index.html with 10-Logo Suite!")

# Write updated files
with open(r"c:\Project\Gift Valut\web_preview\index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open(r"c:\Project\Gift Valut\web\index.html", "w", encoding="utf-8") as f:
    f.write(html)

artifact_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"
with open(os.path.join(artifact_dir, "giftvault_interactive_preview.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: 10-Logo Suite injected across all target files!")
