from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('http://127.0.0.1:8080/')
    page.wait_for_timeout(500)
    page.click('#btn-header-signin')
    page.wait_for_timeout(300)
    btn = page.locator("button[onclick*='enterGuestDemoMode()']").first
    btn.click(timeout=3000)
    page.wait_for_timeout(500)
    hub_active = page.locator('#view-hub').is_visible()
    print('Hub visible after guest click:', hub_active)
    browser.close()
