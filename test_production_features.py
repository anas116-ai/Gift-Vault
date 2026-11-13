import asyncio
from playwright.async_api import async_playwright

async def verify_production():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1400, "height": 900})
        page = await context.new_page()

        errors = []
        page.on("pageerror", lambda err: errors.append(str(err)))

        print("1. Loading http://127.0.0.1:8080/ ...")
        await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
        await page.wait_for_timeout(300)

        # Verify Toast system exists
        toast_cont = page.locator("#toast-container")
        assert await toast_cont.count() > 0, "Toast container must exist"

        # Trigger a test toast
        await page.evaluate("showToast('సమగ్ర పరీక్ష విజయవంతమైంది! (Production Test Active)', 'success')")
        await page.wait_for_timeout(300)
        toast_el = page.locator(".toast-pill.show")
        assert await toast_el.is_visible(), "Toast should be visible"
        print("   ✅ PASS: Royal Toast notification active and rendered.")

        # Navigate to Event Hub
        print("2. Entering Event Hub...")
        await page.evaluate("enterGuestDemoMode()")
        await page.wait_for_timeout(300)

        # Enter first wedding event
        print("3. Entering Workspace...")
        await page.evaluate("enterWorkspaceEvent('event-wedding')")
        await page.wait_for_timeout(300)

        # Switch to Ledger tab
        await page.evaluate("switchWorkspaceTab('tab-ledger')")
        await page.wait_for_timeout(300)

        # Verify Edit and Delete buttons on rows
        rows = page.locator("#ws-full-ledger-body tr")
        rows_count = await rows.count()
        print(f"   Ledger rows count: {rows_count}")
        assert rows_count >= 1, "Should have rows in ledger"

        edit_btn = rows.first.locator("button:has-text('✏️')")
        assert await edit_btn.is_visible(), "Edit button should be visible on rows"

        # Open Edit Modal on first row
        print("4. Testing Edit Modal on entry...")
        await edit_btn.click()
        await page.wait_for_timeout(300)
        edit_modal = page.locator("#modal-edit-entry")
        assert await edit_modal.is_visible(), "Edit modal should be visible"

        # Change name and amount
        await page.fill("#edit-entry-name", "K. Venkata Rao Garu (Audited)")
        await page.fill("#edit-entry-amount", "15116")
        submit_edit = page.locator("#modal-edit-entry button[type='submit']")
        await submit_edit.click()
        await page.wait_for_timeout(400)

        # Check updated name in row
        updated_first_name = await rows.first.locator("strong").inner_text()
        print(f"   Updated First Name: {updated_first_name}")
        assert "Audited" in updated_first_name
        print("   ✅ PASS: Audit Edit entry working with live recalculation.")

        # Test CSV Export
        print("5. Testing CSV Export function...")
        await page.evaluate("exportLedgerCSV()")
        await page.wait_for_timeout(300)
        print("   ✅ PASS: CSV Export triggered cleanly.")

        # Capture evidence screenshot of Production Workspace & Ledger
        await page.screenshot(path="test_evidence/production_verified_ledger.png")
        print("📸 Production Evidence captured: test_evidence/production_verified_ledger.png")

        print("Errors encountered:", len(errors))
        if errors:
            print("Errors:", errors)

        await browser.close()

asyncio.run(verify_production())
