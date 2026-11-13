import asyncio
from playwright.async_api import async_playwright

async def capture_perfect_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1280, 'height': 880})
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(300)
        await page.screenshot(path="test_evidence/live_combined_login_final.png")
        print("Captured test_evidence/live_combined_login_final.png")
        await browser.close()

asyncio.run(capture_perfect_login())
