import asyncio
from playwright.async_api import async_playwright

async def check_errors():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}\nSTACK: {getattr(err, 'stack', '')}"))
        await page.goto("http://127.0.0.1:8080/")
        await page.wait_for_timeout(1000)
        await browser.close()

asyncio.run(check_errors())
