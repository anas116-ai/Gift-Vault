# -*- coding: utf-8 -*-
"""
Inject interactive Logo Concept Showcase and Live Header Logo Swapper into web_preview/index.html
"""

import os

with open(r"c:\Project\Gift Valut\web_preview\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Header Logo to have an id so it can be swapped
old_logo_markup = '''<!-- Sacred Kalasam & Golden Treasury Vault Logo Mark -->
        <div class="relative w-10 h-10 rounded-xl bg-gradient-to-br from-byzantine-500 via-byzantine-600 to-amber-800 p-0.5 shadow-md shadow-byzantine-500/20 group-hover:scale-105 transition-transform">
          <div class="w-full h-full bg-vault-dark rounded-[10px] flex items-center justify-center relative overflow-hidden">
            <!-- Subtle Gold Radiance in Logo -->
            <div class="absolute inset-0 bg-radial from-byzantine-400/30 to-transparent"></div>
            
            <!-- Sacred Kalasam & Auspicious Coin Vector Mark -->
            <svg class="w-5 h-5 text-byzantine-400 relative z-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75">
              <!-- Kalasam Vessel -->
              <path d="M7 10h10c.8 0 1.5.6 1.7 1.4l1.1 5.6c.3 1.7-1 3-2.8 3H7c-1.8 0-3.1-1.3-2.8-3l1.1-5.6C5.5 10.6 6.2 10 7 10z" stroke="currentColor"/>
              <!-- Kalasam Neck & Lid -->
              <path d="M9 10V8a3 3 0 0 1 6 0v2" stroke="currentColor"/>
              <!-- Mango Leaves (Auspicious Foliage) -->
              <path d="M12 5C10 2 8 3 8 3s0 3 2 4" stroke="currentColor" stroke-linecap="round"/>
              <path d="M12 5C14 2 16 3 16 3s0 3-14 4" stroke="currentColor" stroke-linecap="round"/>
              <!-- Central Auspicious Shagun Coin Ring -->
              <circle cx="12" cy="15" r="2.2" stroke="#F9F4E3" fill="rgba(212, 175, 55, 0.35)"/>
            </svg>
          </div>
        </div>'''

new_logo_markup = '''<!-- Sacred Kalasam & Golden Treasury Vault Logo Mark (Live Swappable) -->
        <div id="app-header-logo-container" class="relative w-10 h-10 rounded-xl bg-gradient-to-br from-byzantine-500 via-byzantine-600 to-amber-800 p-0.5 shadow-md shadow-byzantine-500/20 group-hover:scale-105 transition-transform overflow-hidden">
          <img id="app-header-logo-img" src="/logos/concept_1_kalasam_crest.jpg" alt="GiftVault Crest" class="w-full h-full object-cover rounded-[10px]">
        </div>'''

if old_logo_markup in html:
    html = html.replace(old_logo_markup, new_logo_markup)
    print("Header logo markup updated to live swappable image!")

# 2. Add Logo Showcase Modal / Gallery Banner right above main viewport
showcase_banner = '''
  <!-- ============================================================== -->
  <!-- 1.5 LOGO SELECTION SUITE (4 BESPOKE ROYAL CONCEPTS) -->
  <!-- ============================================================== -->
  <section class="max-w-7xl mx-auto px-4 lg:px-8 pt-4 pb-2 w-full">
    <div class="spotlight-card p-4 border border-byzantine-500/35 bg-gradient-to-r from-vault-card via-byzantine-50/40 to-vault-card shadow-sm">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-3 mb-3 border-b border-vault-border/60 pb-2.5">
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-bold px-2 py-0.5 rounded-full bg-byzantine-100 text-byzantine-900 border border-byzantine-300">👑 లోగో సెలెక్షన్ సూట్</span>
            <h3 class="font-bold text-sm text-vault-dark font-telugu-title">మీ అప్లికేషన్ కోసం 4 రాయల్ లోగో డిజైన్లు</h3>
          </div>
          <p class="text-xs text-stone-500 mt-0.5">ఏదైనా లోగోపై క్లిక్ చేసి నేరుగా హెడర్‌లో మరియు యాప్‌లో ఎలా కనిపిస్తుందో లైవ్‌గా చూడండి</p>
        </div>
        <span class="text-[11px] font-bold text-jade-700 bg-jade-50 px-2.5 py-1 rounded-lg border border-jade-100 self-start md:self-auto">
          ✓ 4 కాన్సెప్ట్స్ రెడీ
        </span>
      </div>

      <!-- 4 Logo Concept Cards Grid -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
        
        <!-- Concept 1 -->
        <div onclick="selectAppLogo('/logos/concept_1_kalasam_crest.jpg', 'రాయల్ మంగళ కలశం క్రెస్ట్')" class="cursor-pointer group p-2.5 rounded-2xl bg-white border-2 border-byzantine-500 hover:shadow-glow-gold transition-all">
          <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-2 relative">
            <img src="/logos/concept_1_kalasam_crest.jpg" alt="Concept 1" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
            <span class="absolute top-1.5 left-1.5 px-1.5 py-0.5 rounded-md bg-vault-dark/80 text-byzantine-300 text-[9px] font-bold">కాన్సెప్ట్ 1</span>
          </div>
          <span class="font-bold text-vault-dark block text-[11px] font-telugu-title">రాయల్ మంగళ కలశం క్రెస్ట్</span>
          <span class="text-[10px] text-stone-500 block">24K గోల్డ్ కలశం, కొబ్బరికాయ & నెమలి పింఛాల సీల్</span>
          <button class="mt-2 w-full py-1 rounded-lg bg-vault-dark text-byzantine-400 font-bold text-[10px] btn-tactile">ఇది ఎంచుకోండి</button>
        </div>

        <!-- Concept 2 -->
        <div onclick="selectAppLogo('/logos/concept_2_red_ledger.jpg', 'ఎర్ర వెల్వెట్ చదివింపుల పుస్తకం & స్వర్ణ కమలం')" class="cursor-pointer group p-2.5 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
          <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-2 relative">
            <img src="/logos/concept_2_red_ledger.jpg" alt="Concept 2" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
            <span class="absolute top-1.5 left-1.5 px-1.5 py-0.5 rounded-md bg-vault-dark/80 text-byzantine-300 text-[9px] font-bold">కాన్సెప్ట్ 2</span>
          </div>
          <span class="font-bold text-vault-dark block text-[11px] font-telugu-title">ఎర్ర పుస్తకం & స్వర్ణ కమలం</span>
          <span class="text-[10px] text-stone-500 block">సాంప్రదాయ ఎర్ర లెడ్జర్ & బంగారు కమల కిరీటం</span>
          <button class="mt-2 w-full py-1 rounded-lg bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[10px] border border-vault-border btn-tactile">ఇది ఎంచుకోండి</button>
        </div>

        <!-- Concept 3 -->
        <div onclick="selectAppLogo('/logos/concept_3_gv_monogram.jpg', 'కార్టియర్-గ్రేడ్ మోడ్రన్ GV మోనోగ్రామ్')" class="cursor-pointer group p-2.5 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
          <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-2 relative">
            <img src="/logos/concept_3_gv_monogram.jpg" alt="Concept 3" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
            <span class="absolute top-1.5 left-1.5 px-1.5 py-0.5 rounded-md bg-vault-dark/80 text-byzantine-300 text-[9px] font-bold">కాన్సెప్ట్ 3</span>
          </div>
          <span class="font-bold text-vault-dark block text-[11px] font-telugu-title">మోడ్రన్ GV మోనోగ్రామ్</span>
          <span class="text-[10px] text-stone-500 block">కార్టియర్/రోలెక్స్ తరహా లగ్జరీ ఫిన్‌టెక్ చిహ్నం</span>
          <button class="mt-2 w-full py-1 rounded-lg bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[10px] border border-vault-border btn-tactile">ఇది ఎంచుకోండి</button>
        </div>

        <!-- Concept 4 -->
        <div onclick="selectAppLogo('/logos/concept_4_treasury_chest.jpg', 'రాయల్ ఖజానా పెట్టె')" class="cursor-pointer group p-2.5 rounded-2xl bg-white border border-vault-border hover:border-byzantine-500 hover:shadow-glow-gold transition-all">
          <div class="aspect-square rounded-xl overflow-hidden bg-vault-dark mb-2 relative">
            <img src="/logos/concept_4_treasury_chest.jpg" alt="Concept 4" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
            <span class="absolute top-1.5 left-1.5 px-1.5 py-0.5 rounded-md bg-vault-dark/80 text-byzantine-300 text-[9px] font-bold">కాన్సెప్ట్ 4</span>
          </div>
          <span class="font-bold text-vault-dark block text-[11px] font-telugu-title">రాయల్ ఖజానా పెట్టె</span>
          <span class="text-[10px] text-stone-500 block">దివ్యమైన కాంతులీనే బంగారు శగున్ ఖజానా పెట్టె</span>
          <button class="mt-2 w-full py-1 rounded-lg bg-vault-cream hover:bg-vault-dark hover:text-byzantine-400 text-stone-700 font-bold text-[10px] border border-vault-border btn-tactile">ఇది ఎంచుకోండి</button>
        </div>

      </div>
    </div>
  </section>
'''

if '<!-- ============================================================== -->' in html and '<!-- 2. MAIN VIEWPORT' in html:
    idx = html.find('<!-- 2. MAIN VIEWPORT')
    html = html[:idx] + showcase_banner + '\n  ' + html[idx:]
    print("Showcase banner inserted!")

# 3. Add JS function to switch header logo live
js_function = '''
    function selectAppLogo(imgSrc, title) {
      const img = document.getElementById('app-header-logo-img');
      if (img) {
        img.src = imgSrc;
        img.classList.add('scale-110');
        setTimeout(() => img.classList.remove('scale-110'), 250);
      }
      localStorage.setItem('giftvault_selected_logo', imgSrc);
      alert(`🎉 లోగో అప్‌డేట్ చేయబడింది: ${title}! హెడర్‌లో ప్రివ్యూ చూడండి.`);
    }
'''

idx_js = html.rfind('window.addEventListener')
if idx_js != -1:
    html = html[:idx_js] + js_function + '\n    ' + html[idx_js:]
    print("JS selectAppLogo function added!")

with open(r"c:\Project\Gift Valut\web_preview\index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open(r"c:\Project\Gift Valut\web\index.html", "w", encoding="utf-8") as f:
    f.write(html)

artifact_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"
with open(os.path.join(artifact_dir, "giftvault_interactive_preview.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Logo showcase injected and synced!")
