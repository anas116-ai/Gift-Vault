import os
import shutil
from PIL import Image, ImageEnhance, ImageFilter

brain_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"

hero_src = os.path.join(brain_dir, "giftvault_hero_sacred_shagun_ledger_1794502964334.jpg")
login_src = os.path.join(brain_dir, "giftvault_signin_luxury_gateway_1794502972419.jpg")

print("Hero src exists:", os.path.exists(hero_src))
print("Login src exists:", os.path.exists(login_src))

# 1. Process Hero Image
img_hero = Image.open(hero_src)
print("Original hero size:", img_hero.size)
# Resize to high-density 2560x1440 or keep aspect ratio
w, h = img_hero.size
target_w = 2000
target_h = int(h * (target_w / w))
img_hero_resized = img_hero.resize((target_w, target_h), Image.Resampling.LANCZOS)
# Subtle unsharp mask for crystal clarity
img_hero_clean = img_hero_resized.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))

hero_out_name = "giftvault_hero_sacred_shagun_ledger.jpg"
hero_temp_path = "hero_temp.jpg"
img_hero_clean.save(hero_temp_path, quality=95, optimize=True)

# 2. Process Login Image
img_login = Image.open(login_src)
print("Original login size:", img_login.size)
lw, lh = img_login.size
login_target_w = 2000
login_target_h = int(lh * (login_target_w / lw))
img_login_resized = img_login.resize((login_target_w, login_target_h), Image.Resampling.LANCZOS)
img_login_clean = img_login_resized.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))

login_out_name = "giftvault_signin_luxury_gateway.jpg"
login_temp_path = "login_temp.jpg"
img_login_clean.save(login_temp_path, quality=95, optimize=True)

# Copy to all 4 project directories
dirs = [
    "assets/images",
    "web_preview/assets/images",
    "build/web/assets/images",
    "web/assets/images"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    # Copy hero
    shutil.copy2(hero_temp_path, os.path.join(d, hero_out_name))
    # Also overwrite the old names so any cached/referenced paths automatically pick up the new masterpiece
    shutil.copy2(hero_temp_path, os.path.join(d, "giftvault_flagship_hero_vertical.jpg"))
    shutil.copy2(hero_temp_path, os.path.join(d, "giftvault_hero_showcase.png"))
    
    # Copy login
    shutil.copy2(login_temp_path, os.path.join(d, login_out_name))
    shutil.copy2(login_temp_path, os.path.join(d, "giftvault_login_showcase_final.jpg"))
    shutil.copy2(login_temp_path, os.path.join(d, "giftvault_showcase_16k_master.jpg"))
    print(f"Copied images to {d}")

if os.path.exists(hero_temp_path):
    os.remove(hero_temp_path)
if os.path.exists(login_temp_path):
    os.remove(login_temp_path)

print("All images processed and synchronized across all directories!")
