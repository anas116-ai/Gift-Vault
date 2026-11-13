from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    
    # 1. Landing View
    page.goto('http://127.0.0.1:8080/')
    page.wait_for_timeout(800)
    
    # Screenshot Header & Hero
    page.screenshot(path='test_evidence/landing_hero_updated.png', clip={'x': 0, 'y': 0, 'width': 1920, 'height': 800})
    print('Snapped landing_hero_updated.png')
    
    # Scroll to Pricing
    pricing = page.locator('#pricing')
    pricing.scroll_into_view_if_needed()
    page.wait_for_timeout(500)
    page.screenshot(path='test_evidence/pricing_cards_updated.png', clip={'x': 0, 'y': 0, 'width': 1920, 'height': 1080})
    print('Snapped pricing_cards_updated.png')
    
    # 2. Login View
    page.click('#btn-header-signin')
    page.wait_for_timeout(1000)
    page.screenshot(path='test_evidence/login_view_cream_back_updated.png')
    print('Snapped login_view_cream_back_updated.png')
    
    browser.close()
