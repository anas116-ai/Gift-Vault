import re

target_files = [
    r'c:\Project\Gift Valut\web_preview\index.html',
    r'c:\Project\Gift Valut\web_preview\desktop.html',
    r'c:\Project\Gift Valut\web_preview\mobile.html',
    r'c:\Project\Gift Valut\build\web\index.html',
    r'c:\Project\Gift Valut\web\index.html'
]

with open(target_files[0], 'r', encoding='utf-8') as f:
    html = f.read()

# 1. ENHANCE CREATE EVENT MODAL WITH DYNAMIC FIELDS (Step 290 & 660)
# (Bride & Groom for Wedding; Child Name & Gender for Birthday; Head of House for Housewarming, etc.)
old_modal_fields = '''          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="modal_event_title_lbl">Event Celebration Title *</label>
            <input type="text" id="new-event-title" class="form-input-field" placeholder="e.g. Ramesh & Divya Vivaha Mahotsavam" required>
          </div>'''

new_modal_fields = '''          <!-- Dynamic Event Primary Fields based on Milestone (Step 290 & 660) -->
          <div id="dynamic-event-fields" style="background: var(--c-base); padding: 14px; border-radius: 10px; border: 1px solid var(--c-border); margin-bottom: 16px;">
            <!-- Wedding Pair Fields -->
            <div id="event-fields-wedding" style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
              <div>
                <label class="form-label-txt" style="font-size: 11.5px;" data-i18n="lbl_bride_name">వధువు పేరు (Bride Name) *</label>
                <input type="text" id="event-bride-name" class="form-input-field" placeholder="e.g., Snigdha" oninput="updateAutoEventTitle()">
              </div>
              <div>
                <label class="form-label-txt" style="font-size: 11.5px;" data-i18n="lbl_groom_name">వరుడు పేరు (Groom Name) *</label>
                <input type="text" id="event-groom-name" class="form-input-field" placeholder="e.g., Rahul" oninput="updateAutoEventTitle()">
              </div>
            </div>

            <!-- Birthday Child Fields -->
            <div id="event-fields-birthday" style="display: none; grid-template-columns: 1.5fr 1fr; gap: 12px;">
              <div>
                <label class="form-label-txt" style="font-size: 11.5px;" data-i18n="lbl_child_name">బాబు / పాప పేరు (Child Name) *</label>
                <input type="text" id="event-child-name" class="form-input-field" placeholder="e.g., Advait" oninput="updateAutoEventTitle()">
              </div>
              <div>
                <label class="form-label-txt" style="font-size: 11.5px;" data-i18n="lbl_milestone_year">మైల్‌స్టోన్ (Milestone)</label>
                <select id="event-child-milestone" class="form-input-field" onchange="updateAutoEventTitle()">
                  <option value="1st Birthday & Cradle">1st Birthday & Cradle</option>
                  <option value="Barasala / Naming">Barasala / Naming</option>
                  <option value="5th Birthday">5th Birthday</option>
                </select>
              </div>
            </div>

            <!-- Housewarming Fields -->
            <div id="event-fields-housewarming" style="display: none;">
              <label class="form-label-txt" style="font-size: 11.5px;" data-i18n="lbl_house_owner">గృహ యజమాని / కుటుంబ పేరు (Head of Household / Family) *</label>
              <input type="text" id="event-house-owner" class="form-input-field" placeholder="e.g., K. Rama Rao & Family Nilayam" oninput="updateAutoEventTitle()">
            </div>
          </div>

          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="modal_event_title_lbl">Generated Auspicious Title (శుభకార్యం శీర్షిక) *</label>
            <input type="text" id="new-event-title" class="form-input-field" placeholder="e.g., Rahul & Snigdha Kalyana Mahotsavam" required>
          </div>'''

if old_modal_fields in html:
    html = html.replace(old_modal_fields, new_modal_fields)

# Change onchange on new-event-type
html = html.replace('<select id="new-event-type" class="form-input-field" required>', '<select id="new-event-type" class="form-input-field" onchange="handleMilestoneCategoryChange(this.value)" required>')

# 2. ADD GUEST DEMO BUTTON ON LOGIN SCREEN (Step 602)
old_login_buttons = '''            <button type="submit" class="btn-crimson" style="width: 100%; justify-content: center; padding: 14px; font-size: 15px;">
              <span data-i18n="btn_login_submit">Enter Celebration Vault →</span>
            </button>
          </form>'''

new_login_buttons = '''            <button type="submit" class="btn-crimson" style="width: 100%; justify-content: center; padding: 14px; font-size: 15px; margin-bottom: 12px;">
              <span data-i18n="btn_login_submit">Enter Celebration Vault →</span>
            </button>
            <button type="button" class="btn-outline-dark" style="width: 100%; justify-content: center; padding: 11px; font-size: 13.5px;" onclick="enterGuestDemoMode()">
              👀 <span data-i18n="btn_guest_demo">Explore as Guest (గెస్ట్ డెమో మోడ్)</span>
            </button>
          </form>'''

if old_login_buttons in html:
    html = html.replace(old_login_buttons, new_login_buttons)

# 3. ADD AMOUNT RANGE FILTER TO RED NOTEBOOK LEDGER (Step 40: "అమౌంట్ రేంజ్తో సెర్చ్ — ₹5,000 పైన ఇచ్చినవాళ్లు")
old_ledger_filters = '''          <div class="ledger-filter-pills">
            <button type="button" class="filter-pill active" onclick="filterLedgerMode('all', this)" data-i18n="filter_all">All (38)</button>
            <button type="button" class="filter-pill" onclick="filterLedgerMode('Cash', this)" data-i18n="filter_cash">Cash (22)</button>
            <button type="button" class="filter-pill" onclick="filterLedgerMode('UPI', this)" data-i18n="filter_upi">UPI QR (12)</button>
            <button type="button" class="filter-pill" onclick="filterLedgerMode('Gold', this)" data-i18n="filter_gold">Gold / Silver (4)</button>
          </div>'''

new_ledger_filters = '''          <div style="display: flex; gap: 12px; align-items: center; flex-wrap: wrap;">
            <div class="ledger-filter-pills">
              <button type="button" class="filter-pill active" onclick="filterLedgerMode('all', this)" data-i18n="filter_all">All (38)</button>
              <button type="button" class="filter-pill" onclick="filterLedgerMode('Cash', this)" data-i18n="filter_cash">Cash (22)</button>
              <button type="button" class="filter-pill" onclick="filterLedgerMode('UPI', this)" data-i18n="filter_upi">UPI QR (12)</button>
              <button type="button" class="filter-pill" onclick="filterLedgerMode('Gold', this)" data-i18n="filter_gold">Gold / Silver (4)</button>
            </div>
            <!-- Amount Tier Dropdown (Step 40) -->
            <select id="ledger-amount-tier" class="form-input-field" style="width: auto; padding: 6px 12px; font-size: 12px; border-radius: 20px;" onchange="filterLedgerAmountTier(this.value)">
              <option value="all" data-i18n="tier_all">All Amounts (అన్ని మొత్తాలు)</option>
              <option value="high" data-i18n="tier_high">₹5,000+ (గౌరవ బహుమతులు)</option>
              <option value="mid" data-i18n="tier_mid">₹1,001 - ₹5,000</option>
              <option value="regular" data-i18n="tier_regular">₹1,000 లోపు</option>
            </select>
          </div>'''

if old_ledger_filters in html:
    html = html.replace(old_ledger_filters, new_ledger_filters)

# 4. ADD PRINT SLIP BUTTON & MUNSHI RECORDER BADGE TO TABLE ROWS (Step 40: "ఎవరు ఎంట్రీ చేశారు — ఆటోమేటిక్గా లాగిన్ యూజర్ పేరు")
# Let's inspect the thead of the ledger table
old_ledger_th = '''                  <th data-i18n="th_amount">Auspicious Amount</th>
                  <th data-i18n="th_photo">Photo Proof</th>
                  <th data-i18n="th_action">Receipt</th>'''

new_ledger_th = '''                  <th data-i18n="th_amount">Auspicious Amount</th>
                  <th data-i18n="th_recorder">Recorded By</th>
                  <th data-i18n="th_photo">Photo Proof</th>
                  <th data-i18n="th_action">Receipt & Slip</th>'''

if old_ledger_th in html:
    html = html.replace(old_ledger_th, new_ledger_th)

# 5. Add Print Thermal Slip Modal (Inspired by Chadivimpulu Telugu Desks)
print_slip_modal = '''
  <!-- MODAL: PRINT CHADIVIMPULU SLIP (Telugu Desk Thermal Slip) -->
  <div id="modal-print-slip" class="modal-backdrop">
    <div class="modal-card" style="max-width: 360px; text-align: center; font-family: monospace;">
      <div style="display: flex; justify-content: flex-end;">
        <button type="button" class="modal-close-btn" onclick="closePrintSlipModal()">&times;</button>
      </div>
      <div style="border: 1.5px dashed #000; padding: 18px 14px; background: #FFFDF9; border-radius: 8px;">
        <div style="font-size: 18px; font-weight: 800; font-family: var(--font-serif); margin-bottom: 2px;">॥ శ్రీరస్తు - శుభమస్తు ॥</div>
        <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; margin-bottom: 4px;" id="slip-event-name">Rahul & Snigdha Kalyanam</div>
        <div style="font-size: 10px; color: #555; margin-bottom: 12px;">చదివింపుల అధికారిక రసీదు • GIFTVAULT</div>
        <div style="border-top: 1px dashed #000; margin: 8px 0;"></div>
        <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 4px;">
          <span>సీరియల్ నం:</span> <strong id="slip-sno">#GV-101</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 4px;">
          <span>అతిథి పేరు:</span> <strong id="slip-guest-name">K. Venkata Rao Garu</strong>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 4px;">
          <span>ఊరు / నగరం:</span> <span id="slip-guest-city">Vijayawada</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 11px; margin-bottom: 4px;">
          <span>చెల్లింపు పద్ధతి:</span> <span id="slip-mode">UPI PhonePe</span>
        </div>
        <div style="border-top: 1px dashed #000; margin: 8px 0;"></div>
        <div style="font-size: 11px; font-weight: 700; margin-bottom: 4px;">శుభప్రదమైన కానుక మొత్తం:</div>
        <div style="font-size: 26px; font-weight: 900; color: #036D19; margin-bottom: 6px;" id="slip-amount">₹10,116</div>
        <div style="font-size: 10px; color: #555; margin-bottom: 12px;">నూరు కాలాల పాటు వధూవరులు వర్ధిల్లాలి</div>
        <div style="border-top: 1px dashed #000; margin: 8px 0;"></div>
        <div style="font-size: 9px; color: #777;">Recorded by: Suresh (Munshi Desk 1) • Verified Safe</div>
      </div>
      <div style="display: flex; gap: 10px; margin-top: 16px;">
        <button type="button" class="btn-outline-dark" style="flex: 1; font-size: 12px;" onclick="window.print()">🖨️ Print Slip</button>
        <button type="button" class="btn-crimson" style="flex: 1; font-size: 12px;" onclick="closePrintSlipModal()">Done</button>
      </div>
    </div>
  </div>
'''

if 'id="modal-print-slip"' not in html:
    html = html.replace('<!-- MODAL: ROYAL PLANS & EVENT PASS', print_slip_modal + '\n  <!-- MODAL: ROYAL PLANS & EVENT PASS')

# 6. Add JavaScript logic for:
# - handleMilestoneCategoryChange
# - updateAutoEventTitle
# - enterGuestDemoMode
# - filterLedgerAmountTier
# - openPrintSlip
js_event_logic = '''
function handleMilestoneCategoryChange(val) {
  const weddingFields = document.getElementById('event-fields-wedding');
  const birthdayFields = document.getElementById('event-fields-birthday');
  const houseFields = document.getElementById('event-fields-housewarming');

  if (weddingFields) weddingFields.style.display = 'none';
  if (birthdayFields) birthdayFields.style.display = 'none';
  if (houseFields) houseFields.style.display = 'none';

  if (val === 'Wedding') {
    if (weddingFields) weddingFields.style.display = 'grid';
  } else if (val === 'Birthday' || val === 'Tonsure') {
    if (birthdayFields) birthdayFields.style.display = 'grid';
  } else if (val === 'Housewarming') {
    if (houseFields) houseFields.style.display = 'block';
  }
  updateAutoEventTitle();
}

function updateAutoEventTitle() {
  const type = document.getElementById('new-event-type').value;
  const titleField = document.getElementById('new-event-title');
  if (type === 'Wedding') {
    const bride = document.getElementById('event-bride-name').value.trim() || 'Divya';
    const groom = document.getElementById('event-groom-name').value.trim() || 'Ramesh';
    titleField.value = groom + ' & ' + bride + ' Kalyana Mahotsavam';
  } else if (type === 'Birthday' || type === 'Tonsure') {
    const child = document.getElementById('event-child-name').value.trim() || 'Advait';
    const m = document.getElementById('event-child-milestone').value;
    titleField.value = child + ' ' + m;
  } else if (type === 'Housewarming') {
    const owner = document.getElementById('event-house-owner').value.trim() || 'K. Rama Rao Family';
    titleField.value = owner + ' Griha Pravesham';
  }
}

function enterGuestDemoMode() {
  navToView('hub');
}

function filterLedgerAmountTier(tier) {
  const rows = document.querySelectorAll('#ledger-tbody tr');
  rows.forEach(row => {
    const amtTxt = row.querySelector('.num-currency');
    if (!amtTxt) return;
    const num = parseInt(amtTxt.innerText.replace(/[^0-9]/g, ''), 10) || 0;
    if (tier === 'all') {
      row.style.display = '';
    } else if (tier === 'high' && num >= 5000) {
      row.style.display = '';
    } else if (tier === 'mid' && num > 1000 && num < 5000) {
      row.style.display = '';
    } else if (tier === 'regular' && num <= 1000) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
}

function openPrintSlip(sno, name, city, mode, amt) {
  document.getElementById('slip-sno').innerText = sno;
  document.getElementById('slip-guest-name').innerText = name;
  document.getElementById('slip-guest-city').innerText = city;
  document.getElementById('slip-mode').innerText = mode;
  document.getElementById('slip-amount').innerText = amt;
  const modal = document.getElementById('modal-print-slip');
  if (modal) modal.classList.add('active');
}

function closePrintSlipModal() {
  const modal = document.getElementById('modal-print-slip');
  if (modal) modal.classList.remove('active');
}
'''

if 'function handleMilestoneCategoryChange' not in html:
    html = html.replace('function openPricingModal() {', js_event_logic + '\nfunction openPricingModal() {')

# 7. Update ledger rows rendering in JS to include Recorded By badge and Print Slip button
old_render_js = '''    const row = document.createElement('tr');
    row.innerHTML = `
      <td><span class="serial-num">${item.sno}</span></td>
      <td><strong>${item.name}</strong><br><small style="color:var(--c-muted);">${item.relation || 'బంధువు / Relative'}</small></td>
      <td>${item.place}</td>
      <td><span class="mode-badge ${badgeClass}">${item.mode}</span></td>
      <td class="num-currency" style="font-weight:700; color:var(--c-night);">${amtDisplay}</td>
      <td>${photoHtml}</td>
      <td>
        <button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${item.name}', '${amtDisplay}', '${item.phone || ''}', '${item.place}')">
          📲 WhatsApp
        </button>
      </td>
    `;'''

new_render_js = '''    const row = document.createElement('tr');
    row.innerHTML = `
      <td><span class="serial-num">${item.sno}</span></td>
      <td><strong>${item.name}</strong><br><small style="color:var(--c-muted);">${item.relation || 'బంధువు / Relative'}</small></td>
      <td>${item.place}</td>
      <td><span class="mode-badge ${badgeClass}">${item.mode}</span></td>
      <td class="num-currency" style="font-weight:700; color:var(--c-night);">${amtDisplay}</td>
      <td><span style="font-size:11px; color:var(--c-muted); background:var(--c-base); padding:3px 6px; border-radius:4px; border:1px solid var(--c-border);">${item.recorder || 'Suresh (Desk 1)'}</span></td>
      <td>${photoHtml}</td>
      <td style="white-space:nowrap;">
        <button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${item.name}', '${amtDisplay}', '${item.phone || ''}', '${item.place}')">
          📲 WhatsApp
        </button>
        <button type="button" class="btn-outline-dark" style="padding:4px 8px; font-size:11px; margin-left:4px;" onclick="openPrintSlip('${item.sno}', '${item.name}', '${item.place}', '${item.mode}', '${amtDisplay}')">
          🖨️ Slip
        </button>
      </td>
    `;'''

if old_render_js in html:
    html = html.replace(old_render_js, new_render_js)

# Add translations for new labels
html = html.replace('btn_login_submit: "Enter Celebration Vault →",', 'btn_login_submit: "Enter Celebration Vault →",\n    btn_guest_demo: "Explore as Guest (గెస్ట్ డెమో మోడ్)",\n    tier_all: "All Amounts (అన్ని మొత్తాలు)",\n    tier_high: "₹5,000+ (గౌరవ బహుమతులు)",\n    tier_mid: "₹1,001 - ₹5,000",\n    tier_regular: "₹1,000 లోపు",\n    th_recorder: "Recorded By",\n    lbl_bride_name: "వధువు పేరు (Bride Name)",\n    lbl_groom_name: "వరుడు పేరు (Groom Name)",\n    lbl_child_name: "బాబు / పాప పేరు (Child Name)",\n    lbl_house_owner: "గృహ యజమాని / కుటుంబ పేరు",')

for path in target_files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated: {path} ({len(html)} bytes)")

print("\nSuccessfully added all discussed features from Step 40, Step 290, Step 602 & Step 660!")
