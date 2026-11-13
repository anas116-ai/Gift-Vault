import asyncio
from playwright.async_api import async_playwright

async def snap_nav():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1280, 'height': 800})
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        header = page.locator(".header-glass")
        await header.screenshot(path="test_evidence/nav_current.png")
        print("Captured nav_current.png")
        await browser.close()

asyncio.run(snap_nav())
