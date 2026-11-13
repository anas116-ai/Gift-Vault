import asyncio
from playwright.async_api import async_playwright

async def debug_entry():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        page.on("dialog", lambda d: asyncio.create_task(d.accept()))
        page.on("console", lambda m: print("PAGE CONSOLE:", m.text))
        page.on("pageerror", lambda e: print("PAGE ERROR:", e))

        await page.goto("http://localhost:8080/")
        await page.evaluate("enterGuestDemoMode()")
        await page.wait_for_timeout(300)
        
        # Check active event
        active_id = await page.evaluate("currentActiveEventId")
        print("Active event ID initially:", active_id)

        # Enter first workspace event
        await page.evaluate("enterWorkspaceEvent('event-wedding')")
        print("After enterWorkspaceEvent, active event ID:", await page.evaluate("currentActiveEventId"))

        # Switch to tab-entry
        await page.evaluate("switchWorkspaceTab('tab-entry')")
        
        # Fill inputs
        await page.fill("#entry-name", "Test Guest Garu")
        await page.fill("#entry-city", "Chirala")
        await page.fill("#entry-amount", "5116")
        
        print("Values filled. Now clicking submit button...")
        btn = page.locator("#tab-entry button[type='submit']").first
        print("Button exists:", await btn.count(), "visible:", await btn.is_visible())
        
        await btn.click()
        await page.wait_for_timeout(500)
        
        # Check entries count in EVENTS_DATABASE
        entries = await page.evaluate("EVENTS_DATABASE[currentActiveEventId].entries")
        print("Entries in EVENTS_DATABASE:", entries)
        
        total = await page.evaluate("EVENTS_DATABASE[currentActiveEventId].totalBlessings")
        print("Total blessings:", total)
        
        await browser.close()

asyncio.run(debug_entry())
