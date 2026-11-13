import asyncio
from playwright.async_api import async_playwright

async def snap_final_evidence():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1366, 'height': 850})
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(400)
        
        # 1. Capture fixed footer
        footer_el = page.locator(".footer-master")
        await footer_el.scroll_into_view_if_needed()
        await page.wait_for_timeout(300)
        await footer_el.screenshot(path="test_evidence/live_aura_footer_fixed.png")
        print("Captured live_aura_footer_fixed.png")
        
        # 2. Capture login page with creative background
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(400)
        await page.screenshot(path="test_evidence/live_login_creative_bg.png")
        print("Captured live_login_creative_bg.png")
        
        await browser.close()

asyncio.run(snap_final_evidence())
