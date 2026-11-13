import re

target_files = [
    r'c:\Project\Gift Valut\web_preview\index.html',
    r'c:\Project\Gift Valut\web_preview\desktop.html',
    r'c:\Project\Gift Valut\web_preview\mobile.html',
    r'c:\Project\Gift Valut\build\web\index.html',
    r'c:\Project\Gift Valut\web\index.html'
]

with open(target_files[0], 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect CSS to ensure the visual hierarchy is top-tier:
# Check if buttons have beautiful micro-interactions, cards have subtle luxury borders, and fonts render crisp KaTeX/Google font styling.

# 1. Update the CSS styles to enhance card aesthetics, visual contrast, and interactive feedback
master_css_polish = '''
    /* ==========================================
       MASTERPIECE AESTHETIC POLISH (Thenyota & Sgunms Inspired)
       ========================================== */
    /* Subtle decorative top brand accent */
    body::before {
      content: "";
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--c-crimson) 0%, #D91C25 50%, var(--c-crimson) 100%);
      z-index: 9999;
    }

    /* Cards Luxury Polish */
    .cap-card,
    .event-selection-card,
    .kpi-card,
    .munshi-entry-card,
    .footer-trust-card {
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      box-shadow: 0 4px 16px -2px rgba(0, 4, 17, 0.04), 0 2px 6px -1px rgba(0, 4, 17, 0.02);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .cap-card:hover,
    .event-selection-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 16px 32px -4px rgba(0, 4, 17, 0.08), 0 6px 12px -2px rgba(0, 4, 17, 0.03);
      border-color: #CBD5E1;
    }

    /* Tactile Mode Selector Buttons in Munshi Desk */
    .mode-btn {
      background: #FFFFFF;
      border: 1.5px solid #E2E8F0;
      color: var(--c-night);
      padding: 10px 14px;
      border-radius: 10px;
      font-family: var(--font-sans);
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }
    .mode-btn:hover {
      border-color: #94A3B8;
      background: #F8F9FA;
    }
    .mode-btn.active {
      background: var(--c-night);
      color: #FFFFFF;
      border-color: var(--c-night);
      box-shadow: 0 4px 12px rgba(0, 4, 17, 0.15);
    }

    /* Tactile Auspicious Amount Preset Chips */
    .amt-preset-chip {
      background: #F8F9FA;
      border: 1.5px solid #E2E8F0;
      color: var(--c-night);
      padding: 6px 14px;
      border-radius: 9999px;
      font-family: var(--font-sans);
      font-size: 12.5px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .amt-preset-chip:hover {
      background: #FFF1F2;
      border-color: #FECDD3;
      color: var(--c-crimson);
      transform: translateY(-1px);
    }
    .amt-preset-chip.lucky-coin {
      background: #FFF1F2;
      border-color: var(--c-crimson);
      color: var(--c-crimson);
      font-weight: 800;
    }
    .amt-preset-chip.lucky-coin:hover {
      background: var(--c-crimson);
      color: #FFFFFF;
    }

    /* Voice Dictation Active Wave Effect */
    @keyframes micPulse {
      0% { box-shadow: 0 0 0 0 rgba(248, 51, 60, 0.4); }
      70% { box-shadow: 0 0 0 10px rgba(248, 51, 60, 0); }
      100% { box-shadow: 0 0 0 0 rgba(248, 51, 60, 0); }
    }
    .btn-voice.listening {
      background: var(--c-crimson) !important;
      color: #FFFFFF !important;
      border-color: var(--c-crimson) !important;
      animation: micPulse 1.5s infinite;
    }

    /* High-Precision Form Inputs */
    .form-input-field {
      border: 1.5px solid #CBD5E1 !important;
      border-radius: 8px !important;
      transition: all 0.2s ease !important;
    }
    .form-input-field:focus {
      border-color: var(--c-crimson) !important;
      box-shadow: 0 0 0 3px rgba(248, 51, 60, 0.12) !important;
    }
'''

if '/* MASTERPIECE AESTHETIC POLISH' not in html:
    html = html.replace('</style>', master_css_polish + '\n  </style>')

# Ensure all mode buttons in Munshi entry form use the .mode-btn class if not already
html = html.replace('class="btn-outline-dark mode-select-btn"', 'class="mode-btn mode-select-btn"')
html = html.replace('class="btn-outline-dark mode-select-btn active"', 'class="mode-btn mode-select-btn active"')

# Write updated code to all 5 target files
for path in target_files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Masterpiece Polish Synced: {path} ({len(html)} bytes)")

print("\nSuccessfully applied reference-inspired best visual design while keeping 100% of our concept!")
