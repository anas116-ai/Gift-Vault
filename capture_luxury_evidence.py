import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 960})
        page = await context.new_page()

        # 1. Landing Hero with 3D Coin and Etale plates
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.screenshot(path="test_evidence/masterpiece_3d_hero.png", full_page=False)

        # 2. Scroll to live shagun calculator
        calc = page.locator("#calc-guest-slider")
        if await calc.count() > 0:
            await calc.scroll_into_view_if_needed()
            await page.wait_for_timeout(600)
            await page.screenshot(path="test_evidence/masterpiece_number_plates.png", full_page=False)

        # 3. Hub with all 9 events
        await page.evaluate("navToView('hub')")
        await page.wait_for_timeout(600)
        await page.screenshot(path="test_evidence/masterpiece_event_hub.png", full_page=False)

        # 4. Workspace Red Notebook Ledger with entries
        chirala_card = page.locator(".event-selection-card:has-text('Tonsure'), .event-selection-card:has-text('Chirala')").first
        if await chirala_card.count() > 0:
            await chirala_card.click()
            await page.wait_for_timeout(400)
            ledger_tab = page.locator("button.ws-tab-btn[onclick*=\"'tab-ledger'\"]").first
            await ledger_tab.click()
            await page.wait_for_timeout(400)
            await page.screenshot(path="test_evidence/masterpiece_ledger_view.png", full_page=False)

        await browser.close()
        print("Captured all 4 visual evidence screenshots.")

if __name__ == "__main__":
    asyncio.run(capture())
