import os
from playwright.sync_api import sync_playwright

def capture():
    artifact_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 1050})
        page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        page.wait_for_timeout(1000)

        # 1. Full hero viewport screenshot
        full_hero_path = os.path.join(artifact_dir, "hero_reference1_redesign_full.png")
        page.screenshot(path=full_hero_path)
        print("Captured full hero page:", full_hero_path)

        # 2. Hero Grid element screenshot
        hero_el = page.locator(".hero-cinematic-grid")
        if hero_el.count() > 0:
            hero_grid_path = os.path.join(artifact_dir, "hero_reference1_grid_crop.png")
            hero_el.screenshot(path=hero_grid_path)
            print("Captured hero grid crop:", hero_grid_path)

        # 3. Features strip crop
        feat_el = page.locator(".hero-ref1-features-strip")
        if feat_el.count() > 0:
            feat_path = os.path.join(artifact_dir, "hero_reference1_features_strip_crop.png")
            feat_el.screenshot(path=feat_path)
            print("Captured features strip crop:", feat_path)

        # 4. Family section crop
        fam_el = page.locator(".hero-ref1-family-section")
        if fam_el.count() > 0:
            fam_path = os.path.join(artifact_dir, "hero_reference1_family_section_crop.png")
            fam_el.screenshot(path=fam_path)
            print("Captured family section crop:", fam_path)

        browser.close()

if __name__ == "__main__":
    capture()
