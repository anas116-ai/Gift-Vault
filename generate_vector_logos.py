# -*- coding: utf-8 -*-
"""
Generate precision geometric SVGs for GiftVault Logo Concepts using logo-design skill guidelines
"""

import os

identity_dir = r"c:\Project\Gift Valut\brand_identity"
os.makedirs(identity_dir, exist_ok=True)

# -------------------------------------------------------------
# CONCEPT A: Imperial Lotus GV Monogram
# -------------------------------------------------------------
symbol_a_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="title-a">
  <title id="title-a">GiftVault Imperial Lotus GV Monogram</title>
  <defs>
    <linearGradient id="gold-grad-a" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F9F4E3"/>
      <stop offset="45%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#947219"/>
    </linearGradient>
  </defs>

  <!-- Background Base (Optional for transparent/dark) -->
  <rect width="256" height="256" rx="48" fill="#0B0D13"/>

  <!-- Outer Auspicious Halo Ring -->
  <circle cx="128" cy="132" r="102" fill="none" stroke="url(#gold-grad-a)" stroke-width="2" stroke-dasharray="3 5" opacity="0.45"/>

  <!-- Sacred 5-Petal Lotus Crown at Top (y=38 to y=88) -->
  <g id="lotus-crown-a" fill="url(#gold-grad-a)">
    <!-- Central Lotus Petal -->
    <path d="M128 36 C134 48 138 64 128 78 C118 64 122 48 128 36 Z"/>
    <!-- Left Inner Petal -->
    <path d="M128 78 C121 66 108 55 98 62 C96 74 112 80 128 78 Z"/>
    <!-- Right Inner Petal -->
    <path d="M128 78 C135 66 148 55 158 62 C160 74 144 80 128 78 Z"/>
    <!-- Left Outer Flank -->
    <path d="M128 78 C115 72 92 68 84 80 C88 90 110 84 128 78 Z"/>
    <!-- Right Outer Flank -->
    <path d="M128 78 C141 72 164 68 172 80 C168 90 146 84 128 78 Z"/>
  </g>

  <!-- Interlocking 'G' and 'V' Monogram Geometry -->
  <g id="monogram-gv-a">
    <!-- Letter 'G': Sweeping Royal Outer Arch -->
    <path fill="url(#gold-grad-a)" d="M128 76 C78 76 42 110 42 154 C42 198 78 230 128 230 C168 230 198 204 204 166 L186 166 C180 192 158 212 128 212 C90 212 60 186 60 154 C60 120 90 94 128 94 C152 94 172 108 182 128 L200 120 C186 94 158 76 128 76 Z"/>
    <!-- Letter 'G' Inward Crossbar -->
    <path fill="url(#gold-grad-a)" d="M136 150 L204 150 L204 168 L154 168 L154 186 L136 186 Z"/>

    <!-- Letter 'V': Inverted Chevron Interlocking through Core -->
    <path fill="url(#gold-grad-a)" d="M96 102 L128 198 L160 102 L142 102 L128 152 L114 102 Z"/>
  </g>

  <!-- Auspicious Central Shagun Coin Core -->
  <g id="shagun-coin-core-a">
    <circle cx="128" cy="144" r="14" fill="#9B1B30" stroke="url(#gold-grad-a)" stroke-width="2"/>
    <circle cx="128" cy="144" r="8" fill="url(#gold-grad-a)"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# CONCEPT B: Sovereign Treasury Medallion (Circular Coin Seal)
# -------------------------------------------------------------
symbol_b_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="title-b">
  <title id="title-b">GiftVault Sovereign Treasury Medallion</title>
  <defs>
    <linearGradient id="gold-grad-b" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBF8F0"/>
      <stop offset="35%" stop-color="#D4AF37"/>
      <stop offset="85%" stop-color="#A6823F"/>
      <stop offset="100%" stop-color="#644A20"/>
    </linearGradient>
  </defs>

  <rect width="256" height="256" rx="48" fill="#0B0D13"/>

  <!-- Beaded Kasu Rim (48 Decorative Dots around rim) -->
  <g fill="url(#gold-grad-b)" opacity="0.8">
    <circle cx="128" cy="128" r="110" fill="none" stroke="url(#gold-grad-b)" stroke-width="2.5"/>
    <circle cx="128" cy="128" r="98" fill="none" stroke="url(#gold-grad-b)" stroke-width="1" stroke-dasharray="2 6"/>
  </g>

  <!-- Central Crest: Geometric Kalasam & Intertwined GV -->
  <g id="crest-b">
    <!-- Sacred Kalasam Silhouette -->
    <path fill="#9B1B30" stroke="url(#gold-grad-b)" stroke-width="2" d="M104 128 L152 128 C158 128 164 134 162 142 L154 178 C152 186 142 192 128 192 C114 192 104 186 102 178 L94 142 C92 134 98 128 104 128 Z"/>
    
    <!-- Blooming Lotus on Kalasam Neck -->
    <path fill="url(#gold-grad-b)" d="M128 72 C134 84 140 102 128 116 C116 102 122 84 128 72 Z"/>
    <path fill="url(#gold-grad-b)" d="M128 116 C118 104 98 94 92 108 C96 118 116 118 128 116 Z"/>
    <path fill="url(#gold-grad-b)" d="M128 116 C138 104 158 94 164 108 C160 118 140 118 128 116 Z"/>

    <!-- Intertwined Geometric 'G' & 'V' -->
    <!-- The 'G' Arc -->
    <path fill="none" stroke="url(#gold-grad-b)" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"
          d="M172 104 C158 84 136 76 116 80 C84 86 64 114 64 146 C64 180 88 206 124 206 C158 206 182 184 184 152 L140 152"/>
    
    <!-- The 'V' Downward Chevron -->
    <path fill="none" stroke="url(#gold-grad-b)" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"
          d="M104 116 L128 168 L152 116"/>
    
    <!-- Central Shagun Sunburst Coin -->
    <circle cx="128" cy="144" r="9" fill="url(#gold-grad-b)"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# CONCEPT C: Architectural Luxury Beveled Monogram
# -------------------------------------------------------------
symbol_c_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="title-c">
  <title id="title-c">GiftVault Architectural Beveled GV Monogram</title>
  <defs>
    <!-- Facet Highlighting Gradients -->
    <linearGradient id="gold-light-c" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFDF9"/>
      <stop offset="50%" stop-color="#E5C158"/>
      <stop offset="100%" stop-color="#D4AF37"/>
    </linearGradient>
    <linearGradient id="gold-shadow-c" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#B89225"/>
      <stop offset="60%" stop-color="#84642C"/>
      <stop offset="100%" stop-color="#483415"/>
    </linearGradient>
  </defs>

  <rect width="256" height="256" rx="48" fill="#0B0D13"/>

  <!-- Elegant Octagonal Framing Chamfer -->
  <polygon points="128,18 226,58 226,198 128,238 30,198 30,58" fill="none" stroke="#D4AF37" stroke-width="1.5" opacity="0.35"/>

  <!-- Sculpted 3D Beveled Monogram Structure -->
  <g id="beveled-gv-c">
    <!-- Left Wing of 'G' (Light side) -->
    <path fill="url(#gold-light-c)" d="M128 52 C84 52 50 86 50 132 C50 178 84 212 128 212 C164 212 192 188 198 154 L180 154 C174 176 154 194 128 194 C94 194 68 168 68 132 C68 96 94 70 128 70 C146 70 162 78 172 92 L188 80 C174 62 152 52 128 52 Z"/>

    <!-- Inward Crossbar of 'G' (Shadow side) -->
    <path fill="url(#gold-shadow-c)" d="M142 142 L198 142 L198 158 L158 158 L158 174 L142 174 Z"/>

    <!-- Sharp Beveled 'V' - Left Blade (Light) -->
    <path fill="url(#gold-light-c)" d="M102 82 L128 174 L138 174 L118 82 Z"/>
    
    <!-- Sharp Beveled 'V' - Right Blade (Shadow) -->
    <path fill="url(#gold-shadow-c)" d="M154 82 L128 174 L138 174 L164 82 Z"/>

    <!-- Royal Lotus Coronet at Top Apex -->
    <g id="crown-c">
      <polygon points="128,42 135,62 128,70 121,62" fill="url(#gold-light-c)"/>
      <polygon points="128,70 148,60 145,72 132,74" fill="url(#gold-shadow-c)"/>
      <polygon points="128,70 108,60 111,72 124,74" fill="url(#gold-light-c)"/>
    </g>

    <!-- Center Minted Shagun Coin -->
    <circle cx="128" cy="132" r="12" fill="#9B1B30" stroke="url(#gold-light-c)" stroke-width="2"/>
    <circle cx="128" cy="132" r="6" fill="url(#gold-light-c)"/>
  </g>
</svg>'''

# -------------------------------------------------------------
# HORIZONTAL LOCKUPS (0 0 960 256)
# -------------------------------------------------------------
def make_lockup(symbol_inner, title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 256" width="960" height="256" role="img" aria-labelledby="title-lockup">
  <title id="title-lockup">{title} Horizontal Lockup</title>
  <defs>
    <linearGradient id="gold-text-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FBF8F0"/>
      <stop offset="40%" stop-color="#D4AF37"/>
      <stop offset="100%" stop-color="#947219"/>
    </linearGradient>
  </defs>

  <rect width="960" height="256" rx="40" fill="#0B0D13"/>

  <!-- Left Symbol (216x216) -->
  <g transform="translate(24, 20) scale(0.84)">
    {symbol_inner}
  </g>

  <!-- Divider Line -->
  <line x1="250" y1="48" x2="250" y2="208" stroke="#D4AF37" stroke-width="1.5" opacity="0.3"/>

  <!-- Right Typography: GIFTVAULT + Telugu Tagline -->
  <g transform="translate(290, 0)">
    <!-- English Luxury Brand Name (Cinzel Style Pathing) -->
    <text x="0" y="128" fill="url(#gold-text-grad)" font-family="'Cinzel Decorative', 'Cinzel', serif" font-size="64" font-weight="800" letter-spacing="8">GIFTVAULT</text>
    
    <!-- Telugu Tagline: చదివింపుల డిజిటల్ ఖజానా -->
    <text x="4" y="176" fill="#F4EFEA" font-family="'Anek Telugu', 'Ramabhadra', sans-serif" font-size="24" font-weight="600" letter-spacing="1">రాయల్ చదివింపుల డిజిటల్ ఖజానా</text>
    
    <!-- Auspicious Seal Dots -->
    <circle cx="368" cy="170" r="3" fill="#9B1B30"/>
    <text x="382" y="175" fill="#D4AF37" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700" letter-spacing="2">SHAGUN LEDGER</text>
  </g>
</svg>'''

# Save Symbols
with open(os.path.join(identity_dir, "concept-a-symbol.svg"), "w", encoding="utf-8") as f:
    f.write(symbol_a_svg)
with open(os.path.join(identity_dir, "concept-b-symbol.svg"), "w", encoding="utf-8") as f:
    f.write(symbol_b_svg)
with open(os.path.join(identity_dir, "concept-c-symbol.svg"), "w", encoding="utf-8") as f:
    f.write(symbol_c_svg)

# Save Lockups
with open(os.path.join(identity_dir, "concept-a-lockup.svg"), "w", encoding="utf-8") as f:
    f.write(make_lockup(symbol_a_svg, "Imperial Lotus GV"))
with open(os.path.join(identity_dir, "concept-b-lockup.svg"), "w", encoding="utf-8") as f:
    f.write(make_lockup(symbol_b_svg, "Sovereign Treasury Medallion"))
with open(os.path.join(identity_dir, "concept-c-lockup.svg"), "w", encoding="utf-8") as f:
    f.write(make_lockup(symbol_c_svg, "Architectural Beveled GV"))

print("SUCCESS: 3 Vector Logo Symbols & Lockups generated in brand_identity/!")
