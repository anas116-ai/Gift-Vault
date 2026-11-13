import asyncio
from playwright.async_api import async_playwright

async def capture_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={'width': 1280, 'height': 860})
        page = await context.new_page()
        
        # Navigate to server
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        
        # Trigger login view
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(600)
        
        # Capture screenshot
        await page.screenshot(path="test_evidence/live_combined_login_final.png", full_page=False)
        print("Captured test_evidence/live_combined_login_final.png")
        await browser.close()

asyncio.run(capture_login())
