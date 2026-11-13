import asyncio
from playwright.async_api import async_playwright

async def capture_sections():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # 1. Hero & Header
        await page.screenshot(path="hero_reference_inspired.png", clip={"x": 0, "y": 0, "width": 1440, "height": 720})
        print("Captured hero_reference_inspired.png")

        # 2. Services Section
        services = page.locator("#services")
        if await services.count() > 0:
            await services.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            await page.screenshot(path="circular_services_inspired.png")
            print("Captured circular_services_inspired.png")

        # 3. Moments Gallery (5 Portrait Cards)
        culture = page.locator("#culture")
        if await culture.count() > 0:
            await culture.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            await page.screenshot(path="moments_5cards_inspired.png")
            print("Captured moments_5cards_inspired.png")

        # 4. Testimonials & CTA Ribbon
        testim = page.locator("#testimonials")
        if await testim.count() > 0:
            await testim.scroll_into_view_if_needed()
            await page.wait_for_timeout(400)
            await page.screenshot(path="testimonials_and_cta_ribbon.png")
            print("Captured testimonials_and_cta_ribbon.png")

        # 5. Full page screenshot
        await page.screenshot(path="full_landing_page_editorial.png", full_page=True)
        print("Captured full_landing_page_editorial.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_sections())
