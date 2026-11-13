import re

# Read current master app
with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    app_html = f.read()

# Let's inspect CSS variables in root
root_css = """
    :root {
      /* 60-30-10 Aesthetic Royal Indian Celebration Palette */
      /* 60% Dominant Background: Warm Pearl Alabaster / Ivory Silk */
      --bg-page: #FAF8F5;
      --bg-surface: #FFFFFF;
      --bg-surface-elevated: #F4EFEB;
      --bg-card: #FFFFFF;
      --bg-card-hover: #FDFBF7;
      
      /* 30% Structural / Secondary Neutral: Rich Deep Espresso Maroon / Slate Charcoal */
      --text-main: #1C1917;         /* Deepest Warm Charcoal */
      --text-muted: #57534E;        /* Warm Stone Grey */
      --text-dim: #78716C;          /* Muted Taupe */
      --border-subtle: #E7E2DA;     /* Soft Warm Parchment Border */
      --border-focus: #C5A059;      /* Focused Accent Border */
      
      /* 10% Accent Highlighting: Royal Champagne Gold & Auspicious Vermilion Kumkum */
      --accent-gold: #B8860B;       /* Noble Ochre / Champagne Gold */
      --accent-gold-light: #C5A059; /* Soft Polished Gold */
      --accent-gold-bg: #F9F4EB;    /* Light Golden Wash */
      --accent-vermilion: #C2410C;  /* Traditional Auspicious Sindhoor/Kumkum */
      --accent-green: #15803D;      /* Auspicious Betel/Emerald Green */
      --accent-blue: #0284C7;       /* Royal Cerulean */
      
      /* Typography */
      --font-display: 'Clash Display', 'Playfair Display', serif;
      --font-body: 'Plus Jakarta Sans', 'Noto Sans Telugu', sans-serif;
      --font-numbers: 'Cabinet Grotesk', 'Satoshi', sans-serif;

      /* Elevation Shadows */
      --shadow-sm: 0 1px 2px rgba(28, 25, 23, 0.04);
      --shadow-md: 0 4px 12px -2px rgba(28, 25, 23, 0.06), 0 2px 6px -1px rgba(28, 25, 23, 0.03);
      --shadow-lg: 0 12px 32px -4px rgba(28, 25, 23, 0.08), 0 4px 12px -2px rgba(28, 25, 23, 0.04);
      --shadow-hover: 0 16px 40px -6px rgba(184, 134, 11, 0.12), 0 4px 16px -2px rgba(28, 25, 23, 0.05);
    }
"""

print('Palettes prepared.')
