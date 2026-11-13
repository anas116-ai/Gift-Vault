import asyncio
from playwright.async_api import async_playwright

async def capture():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        page = await b.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(800)

        # 1. 5 Highlighted Celebration Cards
        culture = page.locator("#culture")
        await culture.scroll_into_view_if_needed()
        await page.wait_for_timeout(300)
        await page.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/moments_highlighted_cards_verified.png")
        print("Captured moments_highlighted_cards_verified.png")

        # 2. Redesigned Pricing Section
        pricing = page.locator("#pricing")
        await pricing.scroll_into_view_if_needed()
        await page.wait_for_timeout(300)
        await page.screenshot(path="C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3/redesigned_pricing_passes_verified.png")
        print("Captured redesigned_pricing_passes_verified.png")

        # 3. Check if CTA banner exists
        cta_count = await page.locator(".royal-cta-banner").count()
        print(f"Royal CTA Banner count on page: {cta_count} (Expected: 0)")

        await b.close()

if __name__ == "__main__":
    asyncio.run(capture())
