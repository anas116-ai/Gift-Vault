import asyncio
from playwright.async_api import async_playwright

async def verify_proto():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))

        await page.goto("file:///c:/Project/Gift%20Valut/test_luxury_motion_prototype.html")
        await page.wait_for_timeout(500)

        # Check canvas
        canvas = page.locator("#ambient-canvas")
        assert await canvas.is_visible(), "Canvas should be visible"

        # Check number plates
        slots = page.locator(".plate-digit-slot")
        slots_count = await slots.count()
        print(f"Number plate slots rendered: {slots_count}")
        assert slots_count == 6, f"Expected 6 slots for 842,116, got {slots_count}"

        # Click randomize button
        btn = page.locator("button.btn-lux")
        await btn.click()
        await page.wait_for_timeout(500)

        # Screenshot prototype
        await page.screenshot(path="test_evidence/luxury_motion_prototype.png")
        print("Prototype verified & screenshot captured: test_evidence/luxury_motion_prototype.png")

        print("Errors encountered:", len(errors))
        if errors:
            print("Errors:", errors)

        await browser.close()

asyncio.run(verify_proto())
