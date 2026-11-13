import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1440, 'height': 900})
        page = await context.new_page()
        
        await page.goto('http://127.0.0.1:8080/', wait_until='networkidle')
        await page.wait_for_timeout(1000)
        
        # 1. Navbar Crop
        navbar = page.locator('nav.navbar')
        if await navbar.count() > 0:
            await navbar.screenshot(path='C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/navbar_final_verified.png')
            print("Captured navbar_final_verified.png")
            
        # 2. Hero Section
        hero = page.locator('header.hero-section')
        if await hero.count() > 0:
            await hero.screenshot(path='C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/hero_final_verified.png', animations='disabled')
            print("Captured hero_final_verified.png")
            
        # 3. Features Section
        features = page.locator('#features')
        if await features.count() > 0:
            await features.screenshot(path='C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/features_final_verified.png')
            print("Captured features_final_verified.png")

        # 4. Culture Section (3 cards)
        culture = page.locator('#culture')
        if await culture.count() > 0:
            await culture.screenshot(path='C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/culture_final_verified.png')
            print("Captured culture_final_verified.png")

        # 5. Full Landing Page bottom check (verify no login bleed)
        await page.screenshot(path='C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/landing_full_verified.png', full_page=True)
        print("Captured landing_full_verified.png")

        # 6. Click Sign In and inspect Login Page
        sign_in_btn = page.locator("button:has-text('Sign In')").first
        if await sign_in_btn.count() > 0:
            await sign_in_btn.click()
            await page.wait_for_timeout(1000)
            await page.screenshot(path='C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/login_page_final_verified.png')
            print("Captured login_page_final_verified.png")
            
        await browser.close()

if __name__ == '__main__':
    asyncio.run(capture())
