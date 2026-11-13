import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()
        
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        # 1. Hero + 3 Creative Cards in one view
        await page.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/hero_and_3creative_cards_verified.png", clip={"x": 0, "y": 0, "width": 1440, "height": 950})
        print("Captured hero and 3 creative cards")

        # 2. Zoomed in 3 Creative Cards Strip
        cards_elem = await page.query_selector(".card-animate")
        if cards_elem:
            parent = await cards_elem.evaluate_handle("el => el.closest('section')")
            if parent:
                await parent.scroll_into_view_if_needed()
                await parent.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/creative_three_cards_verified.png")
                print("Captured 3 creative cards section")

        # 3. Built for Families Compact Card
        family_elem = await page.query_selector(".hero-ref1-family-section")
        if family_elem:
            await family_elem.scroll_into_view_if_needed()
            await family_elem.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/built_for_families_compact_verified.png")
            print("Captured compact family section")

        # 4. Culture section (Reference Image 2 luxury cards)
        cult_elem = await page.query_selector("#culture")
        if cult_elem:
            await cult_elem.scroll_into_view_if_needed()
            await cult_elem.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/culture_reference2_luxury_cards_verified.png")
            print("Captured culture section")

        # 5. Login View (Split luxury frame, Reference Image 1)
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(800)
        await page.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/login_luxury_frame_verified.png", full_page=False)
        print("Captured login luxury frame")

        await browser.close()
        print("All verification screenshots captured successfully!")

asyncio.run(capture())
