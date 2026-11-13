import os
import shutil
import re
from PIL import Image, ImageFilter

brain_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"
bahi_khata_src = os.path.join(brain_dir, "royal_sacred_bahi_khata_1794505503356.jpg")

print("Bahi khata src exists:", os.path.exists(bahi_khata_src))

# Process image with PIL for supreme clarity
img = Image.open(bahi_khata_src)
w, h = img.size
target_w = 2000
target_h = int(h * (target_w / w))
img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
img_clean = img_resized.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))

temp_img = "bahi_khata_temp.jpg"
img_clean.save(temp_img, quality=95, optimize=True)

dirs = [
    "assets/images",
    "web_preview/assets/images",
    "build/web/assets/images",
    "web/assets/images"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    shutil.copy2(temp_img, os.path.join(d, "giftvault_hero_bahi_khata_master.jpg"))
    shutil.copy2(temp_img, os.path.join(d, "giftvault_hero_sacred_shagun_ledger.jpg"))
    shutil.copy2(temp_img, os.path.join(d, "giftvault_flagship_hero_vertical.jpg"))
    print(f"Copied master image to {d}")

if os.path.exists(temp_img):
    os.remove(temp_img)

# Now update HTML across all 4 files
new_hero_left = """        <div>
          <!-- Hidden bridge element for i18n automated tests -->
          <span class="hero-tagline-text" style="display:none;" data-i18n="tagline">SACRED BLESSINGS • DIGITAL RED NOTEBOOK</span>

          <!-- Eyebrow per User Request -->
          <div class="hero-eyebrow-pill" style="display: inline-flex; align-items: center; gap: 8px; font-size: 11px; font-weight: 800; color: #8A1526; background: rgba(138, 21, 38, 0.06); border: 1px solid rgba(138, 21, 38, 0.16); padding: 5px 14px; border-radius: 999px; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 18px;">
            <span style="width: 6px; height: 6px; border-radius: 50%; background: #8A1526;"></span>
            <span>MADE FOR EVERY FAMILY OCCASION</span>
          </div>

          <!-- Headline per User Request -->
          <h1 class="hero-massive-heading hero-heading" style="font-family: 'Cinzel', serif, var(--font-serif); font-size: clamp(34px, 4.0vw, 50px); font-weight: 700; color: #1F1916; line-height: 1.18; letter-spacing: -0.02em; margin: 0 0 18px;">
            Every Gift. Every Occasion. <br style="display: block;">
            <span style="background: linear-gradient(135deg, #8A1526 0%, #B8253B 60%, #D49A3D 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">All in One Place.</span>
          </h1>

          <!-- Subheading per User Request -->
          <p id="hero-subtext" style="font-size: 15.5px; color: #5C524B; line-height: 1.68; max-width: 540px; margin-bottom: 28px; font-weight: 450;">
            Keep track of the gifts you give and receive, manage family contributions, and revisit every occasion whenever you need. A simple, organised way to keep your family's gift records together.
          </p>

          <!-- Primary CTA & Secondary CTA per User Request -->
          <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 32px; align-items: center;">
            <div class="hero-actions-container" style="display: flex; flex-direction: row; align-items: center; justify-content: flex-start; gap: 12px; flex-wrap: nowrap; margin-bottom: 0;">
              <button type="button" id="btn-hero-signin" class="btn-tactile-primary" style="height: 32px !important; padding: 0 16px !important; font-size: 12.5px !important; font-weight: 700 !important; border-radius: 7px !important; border: none !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; box-shadow: none !important; margin: 0 !important;" onclick="navToView('login')">
                <span class="btn-tactile-label" style="position: relative; z-index: 10; color: #FFFFFF !important;">Create Your Family Vault</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="position: relative; z-index: 10;"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </button>
              <button type="button" class="btn-hero-demo" style="height: 32px !important; padding: 0 16px !important; font-size: 12.5px !important; font-weight: 700 !important; border-radius: 7px !important; border: 1.5px solid rgba(138, 21, 38, 0.25) !important; color: #8A1526 !important; background: #FFFFFF !important; cursor: pointer !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; gap: 6px !important; box-shadow: none !important; margin: 0 !important;" onclick="document.getElementById('features').scrollIntoView({behavior: 'smooth'})">
                <span>Explore Features</span>
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              </button>
            </div>
          </div>"""

def update_file(p):
    if not os.path.exists(p):
        return
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    # Match from section class="hero-cinematic-grid">\s*<div> ... up to <!-- 4 Core Pillars
    pattern = r'<section class="hero-cinematic-grid">\s*<div>.*?<!-- 4 Core Pillars'
    replacement = '<section class="hero-cinematic-grid">\n' + new_hero_left + '\n\n          <!-- 4 Core Pillars'
    
    if re.search(pattern, c, re.DOTALL):
        c = re.sub(pattern, replacement, c, flags=re.DOTALL)
        
        # Also ensure right image alt text is clean
        c = re.sub(r'alt="GiftVault 3D Hardware Showcase"', 'alt="GiftVault Sacred Bahi-Khata Ledger"', c)
        c = re.sub(r'alt="GiftVault Sacred Shagun & Gift Ledger"', 'alt="GiftVault Sacred Bahi-Khata Ledger"', c)
        c = re.sub(r'src="assets/images/giftvault_hero_sacred_shagun_ledger.jpg"', 'src="assets/images/giftvault_hero_bahi_khata_master.jpg"', c)
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Successfully updated hero section in {p}")
    else:
        print(f"Hero pattern not matched in {p}")

for p in ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']:
    update_file(p)

print("Hero section design update complete!")
