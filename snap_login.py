from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('http://127.0.0.1:8080/')
    page.wait_for_timeout(500)
    page.click('#btn-header-signin')
    page.wait_for_timeout(1000)
    page.screenshot(path='current_login_view.png', full_page=False)
    browser.close()
print('Screenshot taken: current_login_view.png')
