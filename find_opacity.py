import asyncio
from playwright.async_api import async_playwright

async def find_opacity_source():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.evaluate("navToView('login')")
        
        info = await page.evaluate("""() => {
            const el = document.getElementById('view-login');
            const rules = [];
            for (const sheet of document.styleSheets) {
                try {
                    for (const rule of sheet.cssRules) {
                        if (rule.selectorText && el.matches(rule.selectorText)) {
                            rules.push({ selector: rule.selectorText, css: rule.cssText });
                        }
                    }
                } catch(e) {}
            }
            return {
                styleAttr: el.getAttribute('style'),
                className: el.className,
                matchingRules: rules
            };
        }""")
        print(info)
        await browser.close()

asyncio.run(find_opacity_source())
