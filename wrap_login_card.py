import os

def update_file(path):
    if not os.path.exists(path):
        return
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Search for login-edge-right and form
    # We want to insert the card wrapper around the form
    old_target = """        <div class="login-cream-topbar" style="width: 100%; max-width: 420px; margin-bottom: 14px; display: flex; justify-content: flex-start;">
          <button type="button" class="login-cream-back-btn" onclick="navToView('landing')" style="border-radius: 7px !important; padding: 6px 14px; font-size: 12.5px; font-weight: 600; background: #FFFFFF; border: 1px solid rgba(220, 212, 198, 0.95); color: #8A1526; display: inline-flex; align-items: center; gap: 6px; cursor: pointer; box-shadow: none;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            <span>Back to Celebrations</span>
          </button>
        </div>

          <form onsubmit="handleVerifyOTP(event); return false;">"""

    new_target = """        <div class="login-cream-topbar" style="width: 100%; max-width: 420px; margin-bottom: 16px; display: flex; justify-content: flex-start;">
          <button type="button" class="login-cream-back-btn" onclick="navToView('landing')" style="border-radius: 7px !important; padding: 7px 15px; font-size: 12.5px; font-weight: 600; background: #FFFFFF; border: 1.2px solid rgba(220, 212, 198, 0.95); color: #8A1526; display: inline-flex; align-items: center; gap: 7px; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            <span>Back to Celebrations</span>
          </button>
        </div>

        <!-- Sacred Luxury White Card Wrapper -->
        <div class="exact-auth-card-edge">
          <div class="auth-card-header" style="text-align: center; margin-bottom: 24px;">
            <div style="width: 46px; height: 46px; background: linear-gradient(135deg, #FAF4E8, #F3E7D3); border: 1.5px solid #E6D5B8; border-radius: 12px; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 12px; box-shadow: 0 4px 12px rgba(138,21,38,0.08);">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8A1526" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            </div>
            <h2 style="font-family: 'Cinzel', serif; font-size: 21px; font-weight: 700; color: #1F1916; margin: 0 0 6px 0; letter-spacing: 0.02em;">Sign In to Family Vault</h2>
            <p style="font-size: 12.5px; color: #7A6F68; margin: 0; line-height: 1.4;">Access your sacred shagun records and live reception desks</p>
          </div>

          <form onsubmit="handleVerifyOTP(event); return false;">"""

    if old_target in c:
        c = c.replace(old_target, new_target)
        # Also ensure closing </div> before </div> for login-edge-right
        # In current HTML:
        # </form>
        # </div>
        # </div>
        # </main>
        # We need </form> </div> </div> </div> </main> (one extra closing div for exact-auth-card-edge)
        end_old = """            <!-- Hidden bridge button for test suite -->
            <button type="button" class="btn-guest-pass" onclick="enterGuestDemoMode()" style="position: fixed; bottom: 0; left: 0; opacity: 0.01; width: 20px; height: 20px; z-index: 99999; cursor: pointer;" aria-hidden="true">Guest Demo</button>
          </form>

        </div>

      </div>"""

        end_new = """            <!-- Hidden bridge button for test suite -->
            <button type="button" class="btn-guest-pass" onclick="enterGuestDemoMode()" style="position: fixed; bottom: 0; left: 0; opacity: 0.01; width: 20px; height: 20px; z-index: 99999; cursor: pointer;" aria-hidden="true">Guest Demo</button>
          </form>
        </div>

      </div>"""

        if end_old in c:
            c = c.replace(end_old, end_new)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {path}")
    else:
        print(f"Pattern not found in {path}")

for p in ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']:
    update_file(p)
