from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    
    errors = []
    page.on('console', lambda msg: errors.append(msg.text) if msg.type == 'error' else None)
    page.on('pageerror', lambda exc: errors.append(str(exc)))
    
    page.goto('http://127.0.0.1:8080/')
    page.wait_for_timeout(800)
    
    # Check navbar sign-in button
    btn_header = page.locator('#btn-header-signin')
    canvas_count = btn_header.locator('canvas.btn-tactile-gl').count()
    print('Header button canvas count:', canvas_count)
    
    # Hover over header button to test physics
    btn_header.hover()
    page.wait_for_timeout(300)
    
    # Move across header button
    box = btn_header.bounding_box()
    if box:
        page.mouse.move(box['x'] + 5, box['y'] + box['height'] / 2)
        page.wait_for_timeout(100)
        page.mouse.move(box['x'] + box['width'] - 5, box['y'] + box['height'] / 2)
        page.wait_for_timeout(200)
    
    # Click header sign-in to go to login view
    btn_header.click()
    page.wait_for_timeout(800)
    
    # Check login button (.btn-enter-vault)
    btn_login = page.locator('.btn-enter-vault')
    canvas_count_login = btn_login.locator('canvas.btn-tactile-gl').count()
    print('Login button canvas count:', canvas_count_login)
    
    # Hover and sweep mouse over login button
    box_login = btn_login.bounding_box()
    if box_login:
        page.mouse.move(box_login['x'] + 10, box_login['y'] + box_login['height'] / 2)
        page.wait_for_timeout(100)
        page.mouse.move(box_login['x'] + box_login['width'] / 2, box_login['y'] + box_login['height'] / 2)
        page.wait_for_timeout(100)
        page.mouse.move(box_login['x'] + box_login['width'] - 10, box_login['y'] + box_login['height'] / 2)
        page.wait_for_timeout(200)
    
    # Take screenshot of login view with tactile shader button
    page.screenshot(path='test_evidence/tactile_shader_login.png')
    print('Screenshot saved: test_evidence/tactile_shader_login.png')
    
    print('Page errors encountered:', len(errors))
    if errors:
        print('Errors:', errors)
        
    browser.close()
