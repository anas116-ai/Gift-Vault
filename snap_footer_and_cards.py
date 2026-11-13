import asyncio
from playwright.async_api import async_playwright

async def snap_features_and_footer():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1366, 'height': 850})
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(500)
        
        # 1. Capture Smart Tools Cards
        features_sec = page.locator("#features")
        await features_sec.scroll_into_view_if_needed()
        await page.wait_for_timeout(300)
        await page.screenshot(path="test_evidence/live_aura_cards.png")
        print("Captured live_aura_cards.png")
        
        # 2. Capture Footer
        footer_el = page.locator(".footer-master")
        await footer_el.scroll_into_view_if_needed()
        await page.wait_for_timeout(300)
        await footer_el.screenshot(path="test_evidence/live_aura_footer.png")
        print("Captured live_aura_footer.png")
        
        await browser.close()

asyncio.run(snap_features_and_footer())
