import os
from playwright.sync_api import sync_playwright

def capture():
    artifact_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1400, "height": 1050})
        page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        page.wait_for_timeout(500)

        # 1. Full hero viewport screenshot
        full_hero_path = os.path.join(artifact_dir, "hero_code_crafted_full.png")
        page.screenshot(path=full_hero_path, animations="disabled")
        print("Captured full hero page:", full_hero_path)

        # 2. Hero Grid element screenshot
        hero_el = page.locator(".hero-cinematic-grid")
        if hero_el.count() > 0:
            hero_grid_path = os.path.join(artifact_dir, "hero_code_crafted_grid_crop.png")
            hero_el.screenshot(path=hero_grid_path, animations="disabled")
            print("Captured hero grid crop:", hero_grid_path)

        # 3. Navbar screenshot showing button alignment
        nav_el = page.locator(".header-glass")
        if nav_el.count() > 0:
            nav_path = os.path.join(artifact_dir, "navbar_verified_crop.png")
            nav_el.screenshot(path=nav_path, animations="disabled")
            print("Captured navbar crop:", nav_path)

        browser.close()

if __name__ == "__main__":
    capture()
