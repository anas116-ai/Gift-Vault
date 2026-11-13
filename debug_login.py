import asyncio
from playwright.async_api import async_playwright

async def debug_login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1280, 'height': 860})
        
        errors = []
        page.on("console", lambda msg: print(f"CONSOLE [{msg.type}]: {msg.text}"))
        page.on("pageerror", lambda err: print(f"PAGEERROR: {err}"))
        
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        print("Page title:", await page.title())
        
        # Check active view before
        active_before = await page.evaluate("() => document.querySelector('.view-screen-pane.active')?.id")
        print("Active before:", active_before)
        
        # Call navToView('login')
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(500)
        
        active_after = await page.evaluate("() => document.querySelector('.view-screen-pane.active')?.id")
        print("Active after:", active_after)
        
        is_login_visible = await page.locator("#view-login").is_visible()
        print("Is #view-login visible:", is_login_visible)
        
        login_display = await page.evaluate("() => window.getComputedStyle(document.getElementById('view-login')).display")
        print("Computed display of #view-login:", login_display)

        login_opacity = await page.evaluate("() => window.getComputedStyle(document.getElementById('view-login')).opacity")
        print("Computed opacity of #view-login:", login_opacity)

        login_html = await page.evaluate("() => document.getElementById('view-login').innerHTML.substring(0, 200)")
        print("Inner HTML prefix:", login_html)

        await page.screenshot(path="test_evidence/debug_login.png")
        await browser.close()

asyncio.run(debug_login())
