from playwright.sync_api import sync_playwright
import os
import shutil
from PIL import Image

os.makedirs('test_evidence', exist_ok=True)
brain_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    
    # 1. Landing View
    page.goto('http://127.0.0.1:8080/')
    page.wait_for_timeout(800)
    
    # Screenshot Header & Hero
    page.screenshot(path='test_evidence/landing_hero_master.png', clip={'x': 0, 'y': 0, 'width': 1920, 'height': 850})
    print('Snapped landing_hero_master.png')
    
    # Features Section
    features = page.locator('#features')
    features.scroll_into_view_if_needed()
    page.wait_for_timeout(600)
    page.screenshot(path='test_evidence/features_section_master.png', clip={'x': 0, 'y': 700, 'width': 1920, 'height': 900})
    print('Snapped features_section_master.png')
    
    # 2. Login View
    page.click('#btn-header-signin')
    page.wait_for_timeout(1000)
    page.screenshot(path='test_evidence/login_view_master.png')
    print('Snapped login_view_master.png')
    
    browser.close()

# Copy to brain and generate crops
for fn in ['landing_hero_master.png', 'features_section_master.png', 'login_view_master.png']:
    s = os.path.join('test_evidence', fn)
    d = os.path.join(brain_dir, fn)
    if os.path.exists(s):
        shutil.copy2(s, d)

# Generate high-resolution crops
hero_img = Image.open('test_evidence/landing_hero_master.png')
hw, hh = hero_img.size

# Navbar crop (shows Gift Counter without green dot and 32px sign in)
crop_navbar = hero_img.crop((0, 0, hw, 90))
crop_navbar.save(os.path.join(brain_dir, 'navbar_no_green_dot_crop.png'))

# Hero buttons crop (shows Sign In and Explore Demo side-by-side, 32px, exact baseline)
crop_hero_btns = hero_img.crop((200, 480, 750, 600))
crop_hero_btns.save(os.path.join(brain_dir, 'hero_buttons_32px_aligned_crop.png'))

# Hero Master Image crop
crop_hero_mockup = hero_img.crop((900, 80, 1850, 800))
crop_hero_mockup.save(os.path.join(brain_dir, 'hero_creative_master_crop.png'))

# Features button crop
feat_img = Image.open('test_evidence/features_section_master.png')
fw, fh = feat_img.size
crop_feat = feat_img.crop((int(fw * 0.15), 0, int(fw * 0.85), fh))
crop_feat.save(os.path.join(brain_dir, 'features_and_hub_button_crop.png'))

# Login Image & Card crops
login_img = Image.open('test_evidence/login_view_master.png')
lw, lh = login_img.size
crop_login_left = login_img.crop((0, 0, int(lw * 0.52), lh))
crop_login_left.save(os.path.join(brain_dir, 'login_palace_floral_crop.png'))

crop_login_card = login_img.crop((int(lw * 0.50), 0, lw, lh))
crop_login_card.save(os.path.join(brain_dir, 'login_card_32px_crop.png'))

print('All evidence screenshots and crops generated!')
