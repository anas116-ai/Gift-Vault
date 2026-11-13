import asyncio
from playwright.async_api import async_playwright

async def snap_luxury():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 950})
        page = await context.new_page()

        await page.goto("http://127.0.0.1:8080/")
        await page.wait_for_timeout(400)

        # Update slider via evaluate
        await page.evaluate("""() => {
            const slider = document.getElementById('calc-guest-slider');
            if (slider) {
                slider.value = 650;
                updateLiveCalculator();
            }
        }""")
        await page.wait_for_timeout(300)

        # Scroll to calculator section and capture
        calc = page.locator("#calculator-section")
        if await calc.count() > 0:
            await calc.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            await page.screenshot(path="test_evidence/luxury_calculator_plates.png")
            print("Captured: test_evidence/luxury_calculator_plates.png")

        # Scroll to top and capture hero with canvas
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(300)
        await page.screenshot(path="test_evidence/luxury_hero_canvas.png")
        print("Captured: test_evidence/luxury_hero_canvas.png")

        await browser.close()

asyncio.run(snap_luxury())
