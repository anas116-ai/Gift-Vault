from PIL import Image, ImageEnhance, ImageFilter
import os

# 1. Process Hero Image (NO COIN, NO DIYA)
hero_src = r'C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\giftvault_hero_mockup_1794499079993.jpg'
if os.path.exists(hero_src):
    im_hero = Image.open(hero_src)
    # Upscale to crisp 2000 x 2667 (3:4 aspect)
    w_hero = 2000
    h_hero = int(im_hero.height * (w_hero / im_hero.width))
    im_hero_scaled = im_hero.resize((w_hero, h_hero), Image.Resampling.LANCZOS)
    im_hero_sharp = im_hero_scaled.filter(ImageFilter.UnsharpMask(radius=1.6, percent=125, threshold=1))
    im_hero_final = ImageEnhance.Contrast(im_hero_sharp).enhance(1.03)

    for d in ['assets/images', 'web_preview/assets/images', 'build/web/assets/images', 'web/assets/images']:
        os.makedirs(d, exist_ok=True)
        im_hero_final.save(os.path.join(d, 'giftvault_flagship_hero_vertical.jpg'), 'JPEG', quality=95, subsampling=0)
    print('Hero product visual (Zero coins, Zero diyas) processed and saved!')

# 2. Process Login Palace Reception Masterpiece
login_src = r'C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\giftvault_luxury_wedding_login_1794499097615.jpg'
if os.path.exists(login_src):
    im_login = Image.open(login_src)
    # Upscale to 2752 x 1536
    w_login = 2752
    h_login = int(im_login.height * (w_login / im_login.width))
    im_login_scaled = im_login.resize((w_login, h_login), Image.Resampling.LANCZOS)
    im_login_sharp = im_login_scaled.filter(ImageFilter.UnsharpMask(radius=1.8, percent=130, threshold=1))
    im_login_final = ImageEnhance.Color(ImageEnhance.Contrast(im_login_sharp).enhance(1.04)).enhance(1.03)

    for d in ['assets/images', 'web_preview/assets/images', 'build/web/assets/images', 'web/assets/images']:
        os.makedirs(d, exist_ok=True)
        im_login_final.save(os.path.join(d, 'giftvault_login_showcase_final.jpg'), 'JPEG', quality=96, subsampling=0)
        im_login_final.save(os.path.join(d, 'giftvault_showcase_16k_master.jpg'), 'JPEG', quality=96, subsampling=0)
    print('Login palace reception masterpiece processed and saved!')
