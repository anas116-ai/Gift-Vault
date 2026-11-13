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

        # 1. Hero and 4 Cards
        await page.screenshot(path=os.path.join(artifacts_dir, "hero_restored_with_4cards.png"), clip={"x": 0, "y": 0, "width": 1440, "height": 1100})
        print("Captured hero_restored_with_4cards.png")

        # 2. Culture 3 Cards (Half Image, Half Clean Text, No People)
        await page.locator("#culture").scroll_into_view_if_needed()
        await page.wait_for_timeout(400)
        await page.locator("#culture").screenshot(path=os.path.join(artifacts_dir, "culture_no_people_half_cards.png"))
        print("Captured culture_no_people_half_cards.png")

        # 3. Clean English Pricing Cards (No Telugu)
        await page.locator("#pricing").scroll_into_view_if_needed()
        await page.wait_for_timeout(400)
        await page.locator("#pricing").screenshot(path=os.path.join(artifacts_dir, "pricing_clean_english_cards.png"))
        print("Captured pricing_clean_english_cards.png")

        # 4. Login Page (Before-Previous Master Frame)
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(600)
        await page.screenshot(path=os.path.join(artifacts_dir, "login_before_previous_restored.png"), full_page=False)
        print("Captured login_before_previous_restored.png")

        await browser.close()

asyncio.run(capture())
