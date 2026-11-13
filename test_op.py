import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('http://127.0.0.1:8080/')
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(1000)
        op = await page.evaluate("() => window.getComputedStyle(document.getElementById('view-login')).opacity")
        print('Opacity after 1s:', op)
        await page.screenshot(path="test_evidence/test_after_1s.png")
        await browser.close()

asyncio.run(test())
