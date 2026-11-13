import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()
        
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        # 1. Hero section
        hero = await page.query_selector(".hero-cinematic-grid")
        if hero:
            await hero.scroll_into_view_if_needed()
            await hero.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/hero_new_showcase_verified.png")
            print("Captured new hero")

        # 2. Four Cards Strip
        cards_strip = await page.query_selector(".hero-four-cards-strip")
        if cards_strip:
            await cards_strip.scroll_into_view_if_needed()
            await cards_strip.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/hero_four_distinct_cards_verified.png")
            print("Captured 4 distinct cards strip")

        # 3. Full Hero + 4 Cards Together in one frame
        await page.evaluate("window.scrollTo(0, 0)")
        await page.wait_for_timeout(500)
        await page.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/hero_and_cards_full_view.png", clip={"x": 0, "y": 0, "width": 1440, "height": 920})
        print("Captured full hero and cards view")

        await browser.close()
        print("Verification capture complete!")

asyncio.run(capture())
