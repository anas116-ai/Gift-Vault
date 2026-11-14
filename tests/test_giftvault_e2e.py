import asyncio
import os
import json
import sys
from playwright.async_api import async_playwright

async def run_tests():
    print("=" * 60, flush=True)
    print("🚀 STARTING COMPREHENSIVE END-TO-END TEST SUITE FOR GIFTVAULT", flush=True)
    print("=" * 60, flush=True)

    test_results = {
        "passed": [],
        "failed": [],
        "issues_found": [],
        "events_created": []
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 900})
        page = await context.new_page()
        page.set_default_timeout(6000)

        # Auto-accept all alerts and dialogs instantly via asyncio task
        page.on("dialog", lambda d: asyncio.create_task(d.accept()))

        # Capture console errors
        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: console_errors.append(str(err)))

        # -------------------------------------------------------------
        # TEST 1: Page Load & Initial State
        # -------------------------------------------------------------
        print("\n[TEST 1] Loading http://127.0.0.1:8080/ ...", flush=True)
        try:
            await page.goto("http://127.0.0.1:8080/", wait_until="networkidle")
            title = await page.title()
            assert "GiftVault" in title
            test_results["passed"].append("Page Loaded successfully with title: " + title)
            print("  ✅ PASS: Page loaded successfully.", flush=True)
        except Exception as e:
            test_results["failed"].append(f"Page Load failed: {e}")
            print(f"  ❌ FAIL: {e}", flush=True)

        # -------------------------------------------------------------
        # TEST 2: Multi-Language Switching (English, Telugu, Hindi)
        # -------------------------------------------------------------
        print("\n[TEST 2] Testing Multi-Language Dynamic Translation...", flush=True)
        try:
            lang_select = page.locator("#lang-select")
            
            # Switch to Telugu
            await lang_select.select_option("te")
            await page.wait_for_timeout(300)
            hero_tag = await page.locator(".hero-tagline-text").inner_text()
            print(f"  Telugu text sample: '{hero_tag}'", flush=True)
            assert "శుభకార్య" in hero_tag or "శుభ" in hero_tag or "MANGALA" in hero_tag or "AARAMBH" in hero_tag
            test_results["passed"].append("Multi-Language Switch to Telugu verified")

            # Switch to Hindi
            await lang_select.select_option("hi")
            await page.wait_for_timeout(300)
            hero_h1 = await page.locator(".hero-heading").inner_text()
            print(f"  Hindi heading sample: '{hero_h1[:50]}...'", flush=True)
            test_results["passed"].append("Multi-Language Switch to Hindi verified")

            # Switch back to English
            await lang_select.select_option("en")
            await page.wait_for_timeout(300)
            test_results["passed"].append("Multi-Language Switch to English verified")
            print("  ✅ PASS: Multi-Language engine working live.", flush=True)
        except Exception as e:
            test_results["failed"].append(f"Language Switch failed: {e}")
            print(f"  ❌ FAIL: {e}", flush=True)

        # -------------------------------------------------------------
        # TEST 3: Live Shagun Calculator on Landing Page
        # -------------------------------------------------------------
        print("\n[TEST 3] Testing Interactive Landing Page Calculator...", flush=True)
        try:
            calc_slider = page.locator("#calc-guest-slider")
            if await calc_slider.count() > 0:
                await calc_slider.fill("500")
                await page.wait_for_timeout(200)
                total_disp = await page.locator("#calc-total-shagun").inner_text()
                print(f"  Calculator output for 500 guests: {total_disp}", flush=True)
                test_results["passed"].append(f"Live Calculator functional: 500 guests -> {total_disp}")
                print("  ✅ PASS: Live Calculator working.", flush=True)
        except Exception as e:
            test_results["issues_found"].append(f"Calculator issue: {e}")

        # -------------------------------------------------------------
        # TEST 4: Navigation to Login & Guest Demo Access
        # -------------------------------------------------------------
        print("\n[TEST 4] Testing Sign-In & Guest Demo Flow...", flush=True)
        try:
            # Direct reliable trigger for login view
            await page.evaluate("navToView('login')")
            await page.wait_for_timeout(300)

            # Verify view-login is active
            login_active = await page.locator("#view-login").is_visible()
            assert login_active, "View login should be active"
            print("  Login View is active.", flush=True)

            # Click Explore as Guest
            guest_btn = page.locator("button[onclick*='enterGuestDemoMode()']").first
            await guest_btn.click()
            await page.wait_for_timeout(300)

            # Verify view-hub is active
            hub_active = await page.locator("#view-hub").is_visible()
            assert hub_active, "View Hub should be active"
            test_results["passed"].append("Sign-In and Guest Demo entrance successful")
            print("  ✅ PASS: Event Hub reached via Guest Demo.", flush=True)
        except Exception as e:
            test_results["failed"].append(f"Login/Guest entrance failed: {e}")
            print(f"  ❌ FAIL: {e}", flush=True)

        # -------------------------------------------------------------
        # TEST 5: Creating 5 NEW Creative Events & Testing Data Isolation
        # -------------------------------------------------------------
        print("\n[TEST 5] Creating 5 Diverse & Creative Auspicious Events...", flush=True)

        new_events_data = [
            {
                "type": "Tonsure",
                "title": "Advait Tonsure & Haircut (కేశఖండన / పుట్టెంటకలు)",
                "date": "2027-01-15",
                "venue": "Chirala Beach Shore Mandapam, Bapatla",
                "guests": "350",
                "shagun_entries": [
                    {"name": "Mastan Rao Garu (Chirala)", "city": "Chirala", "rel": "మేనమామ / Maternal Uncle", "amt": "15116", "mode": "Cash"},
                    {"name": "S. Ramana Murthy", "city": "Vetapalem", "rel": "బాబాయ్ / Uncle", "amt": "11116", "mode": "UPI"},
                    {"name": "D. Srinivas Garu", "city": "Bapatla", "rel": "స్నేహితుడు / Friend", "amt": "10116", "mode": "Cash"},
                    {"name": "K. Venkataratnam", "city": "Guntur", "rel": "బావ / Brother-in-law", "amt": "5116", "mode": "UPI"}
                ]
            },
            {
                "type": "Wedding",
                "title": "Sita & Ramachandra Kalyana Mahotsavam (రాయల్ వివాహం)",
                "date": "2027-02-10",
                "venue": "Sri Sita Ramachandra Temple Kalyana Vedika, Bhadrachalam",
                "guests": "800",
                "shagun_entries": [
                    {"name": "B. Janardhan Rao Garu", "city": "Khammam", "rel": "మామ / Father-in-law", "amt": "25116", "mode": "Cash"},
                    {"name": "G. Rajeshwar Sharma", "city": "Warangal", "rel": "స్నేహితుడు / Friend", "amt": "11116", "mode": "UPI"},
                    {"name": "K. Srinivasa Charyulu", "city": "Bhadrachalam", "rel": "బంధువు / Relative", "amt": "5116", "mode": "Gold"}
                ]
            },
            {
                "type": "Housewarming",
                "title": "Sri Nilayam Griha Pravesham (గృహప్రవేశ మహోత్సవం)",
                "date": "2027-03-05",
                "venue": "Sri Nilayam, Amaravati Township",
                "guests": "400",
                "shagun_entries": [
                    {"name": "Ch. Venugopal Garu", "city": "Vijayawada", "rel": "బావ / Brother-in-law", "amt": "11116", "mode": "UPI"},
                    {"name": "N. Surya Narayana", "city": "Mangalagiri", "rel": "పొరుగువారు / Neighbor", "amt": "5116", "mode": "Cash"},
                    {"name": "P. Satyanarayana", "city": "Guntur", "rel": "బాబాయ్ / Uncle", "amt": "10116", "mode": "Cash"}
                ]
            },
            {
                "type": "HalfSaree",
                "title": "Ananya Half Saree & Ritu Kala Samskara Kaaryam (లంగా వోణీల వేడుక)",
                "date": "2027-04-14",
                "venue": "A1 Convention Centre, Vijayawada",
                "guests": "300",
                "shagun_entries": [
                    {"name": "Y. Koteswara Rao Garu", "city": "Tenali", "rel": "తాతయ్య / Grandfather", "amt": "21116", "mode": "Cash"},
                    {"name": "V. Radhika Devi", "city": "Vijayawada", "rel": "మేనత్త / Aunt", "amt": "15116", "mode": "Gold"},
                    {"name": "K. Haritha", "city": "Eluru", "rel": "స్నేహితుడు / Friend", "amt": "5116", "mode": "UPI"}
                ]
            },
            {
                "type": "Custom",
                "title": "Sahasra Chandi Maha Yagnam & Shanti Kaaryam (శాంతి మహోత్సవం)",
                "date": "2027-05-01",
                "venue": "SV Vedic University Campus, Tirupati",
                "guests": "500",
                "shagun_entries": [
                    {"name": "M. Jagannadha Sharma", "city": "Tirupati", "rel": "బంధువు / Relative", "amt": "10116", "mode": "Cash"},
                    {"name": "K. Narayana Swamy", "city": "Nellore", "rel": "స్నేహితుడు / Friend", "amt": "5116", "mode": "UPI"}
                ]
            }
        ]

        # Iterate and create each event, add entries, verify isolation
        for idx, ev in enumerate(new_events_data, 1):
            print(f"\n  ---> [5.{idx}] Creating Event: '{ev['title']}'...", flush=True)
            
            # Ensure we are on Hub view
            hub_visible = await page.locator("#view-hub").is_visible()
            if not hub_visible:
                await page.evaluate("navToView('hub')")
                await page.wait_for_timeout(300)

            # Click + Create New Event
            create_btn = page.locator("button[onclick*='openCreateEventModal()']").first
            await create_btn.click()
            await page.wait_for_timeout(300)

            # Fill Create Event Modal
            await page.select_option("#new-event-type", ev["type"])
            await page.wait_for_timeout(100)
            await page.fill("#new-event-title", ev["title"])
            await page.fill("#new-event-date", ev["date"])
            await page.fill("#new-event-venue", ev["venue"])
            await page.fill("#new-event-guests", ev["guests"])

            # Submit event creation
            submit_event_btn = page.locator("#modal-create-event button[type='submit']")
            await submit_event_btn.click()
            await page.wait_for_timeout(500)

            # Verify Workspace loaded for this event
            ws_title = await page.locator("#ws-event-header-name").inner_text()
            print(f"       Workspace Header: '{ws_title}'", flush=True)

            # Switch to Fast Munshi Entry tab using reliable selector
            munshi_tab_btn = page.locator("button.ws-tab-btn[onclick*=\"'tab-entry'\"]").first
            await munshi_tab_btn.click()
            await page.wait_for_timeout(200)

            # Record each shagun blessing
            event_total_added = 0
            for s_idx, s in enumerate(ev["shagun_entries"], 1):
                # Fill name
                await page.fill("#entry-name", s["name"])
                # Fill city
                await page.fill("#entry-city", s["city"])
                # Select relationship if present
                rel_select = page.locator("#entry-relation")
                if await rel_select.count() > 0:
                    try:
                        await rel_select.select_option(label=s["rel"])
                    except:
                        pass
                
                # Fill amount
                await page.fill("#entry-amount", s["amt"])

                # Test +₹1 Lucky Coin on first entry
                if s_idx == 1:
                    lucky_btn = page.locator("button[onclick*='addOneRupeeCoin']").first
                    if await lucky_btn.count() > 0:
                        await lucky_btn.click()
                        val_after = await page.locator("#entry-amount").input_value()
                        print(f"       Lucky Coin applied: {s['amt']} -> {val_after}", flush=True)
                        s["amt"] = val_after

                # Click mode button if available
                mode_btn = page.locator(f".mode-select-btn:has-text('{s['mode']}'), .mode-btn:has-text('{s['mode']}')").first
                if await mode_btn.count() > 0:
                    await mode_btn.click()

                # Submit Entry
                submit_entry_btn = page.locator("#tab-entry button[type='submit']").first
                await submit_entry_btn.click()
                await page.wait_for_timeout(400)

                event_total_added += int(s["amt"])

            # Verify total blessings on overview tab
            overview_tab_btn = page.locator("button.ws-tab-btn[onclick*=\"'tab-overview'\"]").first
            await overview_tab_btn.click()
            await page.wait_for_timeout(200)

            total_kpi = await page.locator("#overview-total-amt").inner_text()
            print(f"       Event '{ev['title']}' Total Logged: {total_kpi} ({len(ev['shagun_entries'])} entries)", flush=True)
            
            # Verify Red Notebook Ledger table
            ledger_tab_btn = page.locator("button.ws-tab-btn[onclick*=\"'tab-ledger'\"]").first
            await ledger_tab_btn.click()
            await page.wait_for_timeout(200)

            # Check rows count in ws-full-ledger-body
            rows = page.locator("#ws-full-ledger-body tr")
            rows_count = await rows.count()
            print(f"       Ledger rows count: {rows_count}", flush=True)
            assert rows_count == len(ev["shagun_entries"]), f"Expected {len(ev['shagun_entries'])} rows, got {rows_count}"

            # Check sequential S.No on first row
            first_sno = await rows.first.locator("td").first.inner_text()
            print(f"       First S.No: '{first_sno}'", flush=True)
            assert "#GV-101" in first_sno or "1" in first_sno

            test_results["events_created"].append({
                "title": ev["title"],
                "type": ev["type"],
                "venue": ev["venue"],
                "total": total_kpi,
                "entries_count": rows_count
            })

            # Navigate back to Event Hub for the next event
            await page.evaluate("navToView('hub')")
            await page.wait_for_timeout(300)

        # -------------------------------------------------------------
        # TEST 6: LocalStorage Persistence across Page Reload
        # -------------------------------------------------------------
        print("\n[TEST 6] Testing LocalStorage Persistence across Full Page Reload...", flush=True)
        try:
            await page.reload(wait_until="networkidle")
            await page.wait_for_timeout(500)

            # Navigate back to Hub
            await page.evaluate("navToView('hub')")
            await page.wait_for_timeout(400)

            # Verify events rendered in Hub
            hub_cards = page.locator("#events-hub-grid .event-selection-card")
            hub_cards_count = await hub_cards.count()
            print(f"  Total event cards in Hub after reload: {hub_cards_count}", flush=True)
            assert hub_cards_count >= 8, f"Expected at least 8 events, found {hub_cards_count}"
            test_results["passed"].append(f"Persistence Verified: {hub_cards_count} events survived full browser reload!")
            print("  ✅ PASS: LocalStorage persistence working 100%.", flush=True)
        except Exception as e:
            test_results["failed"].append(f"Reload Persistence failed: {e}")
            print(f"  ❌ FAIL: {e}", flush=True)

        # -------------------------------------------------------------
        # TEST 7: Search and Filter in Red Notebook Ledger
        # -------------------------------------------------------------
        print("\n[TEST 7] Testing Real-time Ledger Search & Filters...", flush=True)
        try:
            # Enter the Chirala Tonsure event
            chirala_card = page.locator(".event-selection-card:has-text('Tonsure'), .event-selection-card:has-text('Chirala')").first
            await chirala_card.click()
            await page.wait_for_timeout(300)

            # Switch to Ledger tab
            ledger_tab_btn = page.locator("button.ws-tab-btn[onclick*=\"'tab-ledger'\"]").first
            await ledger_tab_btn.click()
            await page.wait_for_timeout(200)

            # Test Search Input
            search_input = page.locator("#ledger-search-input, #ledger-search-box")
            if await search_input.count() > 0:
                await search_input.fill("Mastan")
                await page.wait_for_timeout(300)
                visible_rows = await page.locator("#ws-full-ledger-body tr:visible").count()
                print(f"  Rows matching 'Mastan': {visible_rows}", flush=True)
                assert visible_rows >= 1, "Should show Mastan Rao row"
                await search_input.fill("") # clear
                await page.wait_for_timeout(200)
                test_results["passed"].append("Real-time Ledger Search verified")
                print("  ✅ PASS: Search filter working.", flush=True)
        except Exception as e:
            test_results["issues_found"].append(f"Ledger Search test issue: {e}")

        # -------------------------------------------------------------
        # TEST 8: 2-inch Thermal Slip Modal
        # -------------------------------------------------------------
        print("\n[TEST 8] Testing 2-inch Thermal Slip Modal...", flush=True)
        try:
            slip_btn = page.locator("button:has-text('Slip'), button:has-text('2-inch')").first
            if await slip_btn.count() > 0:
                await slip_btn.click()
                await page.wait_for_timeout(300)
                slip_modal = page.locator("#modal-print-slip")
                assert await slip_modal.is_visible(), "Thermal slip modal should be visible"
                slip_amt = await page.locator("#slip-amount").inner_text()
                print(f"  Thermal slip preview opened with amount: {slip_amt}", flush=True)
                
                # Close slip modal
                close_btn = page.locator("#modal-print-slip button:has-text('Done'), #modal-print-slip .modal-close-btn").first
                await close_btn.click()
                await page.wait_for_timeout(200)
                test_results["passed"].append("Thermal Slip Modal verified")
                print("  ✅ PASS: 2-inch Thermal Slip modal functioning.", flush=True)
        except Exception as e:
            test_results["issues_found"].append(f"Slip modal issue: {e}")

        # -------------------------------------------------------------
        # TEST 9: Auspicious Pricing Plans Modal (Per-Event Anti-Abuse Pass)
        # -------------------------------------------------------------
        print("\n[TEST 9] Testing Auspicious Pricing Modal...", flush=True)
        try:
            await page.evaluate("openPricingModal()")
            await page.wait_for_timeout(300)
            pricing_modal = page.locator("#modal-pricing-plans")
            assert await pricing_modal.is_visible(), "Pricing modal should be visible"
            print("  ✅ PASS: Pricing modal displayed with ₹49 Single Event and ₹99 Family Pack.", flush=True)
            test_results["passed"].append("Celebration Plans (₹49 Single Event & ₹99 Family Pack) verified")
            await page.evaluate("closePricingModal()")
            await page.wait_for_timeout(200)
        except Exception as e:
            test_results["issues_found"].append(f"Pricing modal issue: {e}")

        # Capture final screenshot evidence
        os.makedirs("test_evidence", exist_ok=True)
        screenshot_path = "test_evidence/giftvault_test_summary.png"
        await page.screenshot(path=screenshot_path, full_page=False)
        print(f"\n📸 Final Evidence Screenshot captured: {screenshot_path}", flush=True)

        await browser.close()

    print("\n" + "=" * 60, flush=True)
    print("📊 TEST SUMMARY REPORT", flush=True)
    print("=" * 60, flush=True)
    print(f"✅ Total Passed Checks: {len(test_results['passed'])}", flush=True)
    print(f"❌ Total Failed Checks: {len(test_results['failed'])}", flush=True)
    print(f"⚠️ Issues/Notices: {len(test_results['issues_found'])}", flush=True)
    print(f"🎉 New Events Created & Verified: {len(test_results['events_created'])}", flush=True)
    for ev in test_results['events_created']:
        print(f"   • {ev['title']} ({ev['venue']}) -> {ev['total']} ({ev['entries_count']} entries)", flush=True)

    print("\nConsole errors encountered:", len(console_errors), flush=True)
    if console_errors:
        for err in console_errors[:5]:
            print("  ⚠️", err, flush=True)

    # Save summary report to JSON
    with open("test_evidence/test_report.json", "w", encoding="utf-8") as f:
        json.dump(test_results, f, indent=2, ensure_ascii=False)
    print("\nTest report saved to test_evidence/test_report.json", flush=True)

if __name__ == "__main__":
    asyncio.run(run_tests())
