import asyncio
from playwright.async_api import async_playwright

async def capture_new_designs():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1366, 'height': 850})
        
        # 1. Capture landing page & new navbar
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(400)
        await page.screenshot(path="test_evidence/live_nav_new.png")
        print("Captured live_nav_new.png")
        
        # 2. Capture full-screen edge-to-edge login
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(400)
        await page.screenshot(path="test_evidence/live_login_fullscreen.png")
        print("Captured live_login_fullscreen.png")
        
        await browser.close()

asyncio.run(capture_new_designs())
