import asyncio
import os
from playwright.async_api import async_playwright

async def capture():
    artifacts_dir = r"C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3"
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://127.0.0.1:8080/")
        await page.wait_for_timeout(1000)

        # 1. Hero and Reference 4 Showcase
        await page.locator(".hero-cinematic-grid").screenshot(path=os.path.join(artifacts_dir, "hero_reference4_showcase_verified.png"))
        print("Captured hero_reference4_showcase_verified.png")

        # 2. Hero + 3 Creative Cards
        await page.screenshot(path=os.path.join(artifacts_dir, "hero_and_3cards_verified.png"), clip={"x": 0, "y": 0, "width": 1440, "height": 1150})
        print("Captured hero_and_3cards_verified.png")

        # 3. Pricing Section with Telugu Mentions
        await page.locator("#pricing").scroll_into_view_if_needed()
        await page.wait_for_timeout(400)
        await page.locator("#pricing").screenshot(path=os.path.join(artifacts_dir, "pricing_telugu_cards_verified.png"))
        print("Captured pricing_telugu_cards_verified.png")

        # 4. Culture 3 Aspect Cards
        await page.locator("#culture").scroll_into_view_if_needed()
        await page.wait_for_timeout(400)
        await page.locator("#culture").screenshot(path=os.path.join(artifacts_dir, "culture_reference3_cards_verified.png"))
        print("Captured culture_reference3_cards_verified.png")

        # 5. Full Landing Page Flow
        await page.screenshot(path=os.path.join(artifacts_dir, "giftvault_landing_flow_master.png"), full_page=True)
        print("Captured giftvault_landing_flow_master.png")

        await browser.close()

asyncio.run(capture())
