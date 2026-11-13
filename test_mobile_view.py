import asyncio
from playwright.async_api import async_playwright

async def snap_mobile():
    async with async_playwright() as p:
        # iPhone 14 Pro mobile viewport (393 x 852)
        device = p.devices['iPhone 14 Pro']
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(**device)
        page = await context.new_page()

        await page.goto("http://localhost:8080/")
        await page.screenshot(path="test_evidence/mobile_landing.png")
        print("Mobile Landing captured: test_evidence/mobile_landing.png")

        # Go to Login
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(300)
        await page.screenshot(path="test_evidence/mobile_login.png")
        print("Mobile Login captured: test_evidence/mobile_login.png")

        # Enter Guest demo (Event Hub)
        await page.evaluate("enterGuestDemoMode()")
        await page.wait_for_timeout(300)
        await page.screenshot(path="test_evidence/mobile_hub.png")
        print("Mobile Hub captured: test_evidence/mobile_hub.png")

        # Enter Workspace Event
        await page.evaluate("enterWorkspaceEvent('event-wedding')")
        await page.wait_for_timeout(300)
        await page.screenshot(path="test_evidence/mobile_workspace_overview.png")
        print("Mobile Workspace Overview captured: test_evidence/mobile_workspace_overview.png")

        # Switch to Munshi Fast Entry
        await page.evaluate("switchWorkspaceTab('tab-entry')")
        await page.wait_for_timeout(300)
        await page.screenshot(path="test_evidence/mobile_munshi_entry.png")
        print("Mobile Munshi Entry captured: test_evidence/mobile_munshi_entry.png")

        await browser.close()

asyncio.run(snap_mobile())
