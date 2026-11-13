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
            await hero.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/hero_master_verified.png")
            print("Captured hero")

        # 2. Four Cards Strip
        cards_strip = await page.query_selector(".hero-four-cards-strip")
        if cards_strip:
            await cards_strip.scroll_into_view_if_needed()
            await cards_strip.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/hero_four_cards_verified.png")
            print("Captured 4 cards strip")
        
        # 3. Built for Families section
        family_elem = await page.query_selector(".hero-ref1-family-section")
        if family_elem:
            await family_elem.scroll_into_view_if_needed()
            await family_elem.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/family_bespoke_graphic_verified.png")
            print("Captured family section")
        
        # 4. Calculator section
        calc_elem = await page.query_selector("#calculator")
        if calc_elem:
            await calc_elem.scroll_into_view_if_needed()
            await calc_elem.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/calculator_redesign_verified.png")
            print("Captured calculator")
                
        # 5. Features (6 cards)
        feat_elem = await page.query_selector("#features")
        if feat_elem:
            await feat_elem.scroll_into_view_if_needed()
            await feat_elem.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/features_six_cards_verified.png")
            print("Captured features")
                
        # 6. Culture (3 real photos)
        cult_elem = await page.query_selector("#culture")
        if cult_elem:
            await cult_elem.scroll_into_view_if_needed()
            await cult_elem.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/culture_three_real_images_verified.png")
            print("Captured culture")
                
        # 7. Pricing (52px gap, compact height)
        price_elem = await page.query_selector("#pricing")
        if price_elem:
            await price_elem.scroll_into_view_if_needed()
            await price_elem.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/pricing_spaced_cards_verified.png")
            print("Captured pricing")
                
        # 8. Login Page
        await page.evaluate("navToView('login')")
        await page.wait_for_timeout(800)
        await page.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/login_fullpage_verified.png", full_page=False)
        print("Captured login fullpage")

        await browser.close()
        print("All verification screenshots captured successfully!")

asyncio.run(capture())
