import asyncio
from playwright.async_api import async_playwright

async def snap_clean_nav_and_footer():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1366, 'height': 850})
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(400)
        
        # 1. Navbar and Hero
        header_el = page.locator(".header-glass")
        await header_el.screenshot(path="test_evidence/clean_nav_final.png")
        print("Captured clean_nav_final.png")
        
        # 2. Restored Footer
        footer_el = page.locator(".footer-master")
        await footer_el.scroll_into_view_if_needed()
        await page.wait_for_timeout(300)
        await footer_el.screenshot(path="test_evidence/restored_footer_final.png")
        print("Captured restored_footer_final.png")
        
        await browser.close()

asyncio.run(snap_clean_nav_and_footer())
