import os
import shutil
from PIL import Image, ImageFilter

brain_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"
src_img = os.path.join(brain_dir, "giftvault_login_showcase_1794508010855.jpg")

print("Source exists:", os.path.exists(src_img))

# Optimize image for login showcase
img = Image.open(src_img)
w, h = img.size
# Crop or resize to portrait/aesthetic ratio (e.g., 1200x1500)
target_w = 1200
target_h = int(h * (target_w / w))
img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
img_clean = img_resized.filter(ImageFilter.UnsharpMask(radius=1.2, percent=110, threshold=3))

temp_out = "login_showcase_temp.jpg"
img_clean.save(temp_out, quality=95, optimize=True)

dirs = [
    "assets/images",
    "web_preview/assets/images",
    "build/web/assets/images",
    "web/assets/images"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    shutil.copy2(temp_out, os.path.join(d, "giftvault_login_showcase_reference.jpg"))
    shutil.copy2(temp_out, os.path.join(d, "giftvault_signin_luxury_gateway.jpg"))
    shutil.copy2(temp_out, os.path.join(d, "giftvault_login_showcase_final.jpg"))
    print(f"Copied to {d}")

if os.path.exists(temp_out):
    os.remove(temp_out)

print("Login reference image processed successfully!")
