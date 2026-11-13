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

# 1. ENHANCE CSS WITH BULLETPROOF RESPONSIVE SYSTEM & ALIGNMENT UTILITIES
# Let's inspect where to insert the new responsive utility classes and overhaul existing CSS
design_enhancement_css = '''
    /* ==========================================
       BULLETPROOF RESPONSIVE & ALIGNMENT SYSTEM
       ========================================== */
    .container-wide {
      width: 100%;
      max-width: 1200px;
      margin-left: auto;
      margin-right: auto;
      padding-left: 24px;
      padding-right: 24px;
    }

    /* Unified Form Grids */
    .form-grid-3 {
      display: grid;
      grid-template-columns: 1.2fr 1fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }
    .form-grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 16px;
    }
    .responsive-split-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
    }

    /* Modal Cards General Styling */
    .modal-card {
      background: #FFFFFF;
      border: 2px solid var(--c-night);
      border-radius: 20px;
      width: 100%;
      max-height: 88vh;
      overflow-y: auto;
      box-shadow: 0 24px 48px -12px rgba(0, 4, 17, 0.35);
      padding: 28px;
    }

    /* Workspace Tabs Bar - Smooth Scrollable on Mobile */
    .ws-tabs-bar {
      background: #FFFFFF;
      border-bottom: 1.5px solid var(--c-border);
      padding: 0 24px;
      display: flex;
      gap: 8px;
      overflow-x: auto;
      white-space: nowrap;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: none;
    }
    .ws-tabs-bar::-webkit-scrollbar {
      display: none;
    }
    .ws-tab-btn {
      flex-shrink: 0;
      padding: 14px 18px;
      font-size: 13.5px;
      font-weight: 700;
      color: var(--c-muted);
      background: none;
      border: none;
      border-bottom: 3px solid transparent;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .ws-tab-btn:hover {
      color: var(--c-night);
    }
    .ws-tab-btn.active {
      color: var(--c-crimson);
      border-bottom-color: var(--c-crimson);
      background: rgba(248, 51, 60, 0.03);
    }

    /* Ledger Table - Bulletproof Alignment & Spacing */
    .ledger-table-wrap {
      background: #FFFFFF;
      border: 1.5px solid var(--c-night);
      border-radius: 14px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      box-shadow: var(--shadow-sm);
    }
    .ledger-table {
      width: 100%;
      min-width: 820px; /* guarantees columns never get squished into ladders */
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }
    .ledger-table th {
      background: #F8F9FA;
      color: var(--c-night);
      font-family: var(--font-sans);
      font-size: 11.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 14px 16px;
      border-bottom: 1.5px solid var(--c-night);
      white-space: nowrap;
    }
    .ledger-table th.th-right,
    .ledger-table td.td-right {
      text-align: right;
    }
    .ledger-table th.th-center,
    .ledger-table td.td-center {
      text-align: center;
    }
    .ledger-table td {
      padding: 13px 16px;
      border-bottom: 1px solid var(--c-border);
      vertical-align: middle;
      color: var(--c-night);
    }
    .ledger-table tbody tr:hover {
      background: rgba(248, 51, 60, 0.02);
    }

    /* Input Focus States for Impeccable Polish */
    .form-input-field:focus {
      border-color: var(--c-crimson) !important;
      outline: none;
      box-shadow: 0 0 0 3px rgba(248, 51, 60, 0.12) !important;
    }

    /* Quick Preset Buttons Grid */
    .quick-preset-btns {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(70px, 1fr));
      gap: 8px;
    }

    /* Mode Selector Grid */
    .payment-mode-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
      gap: 10px;
      margin-bottom: 20px;
    }

    /* Responsive Breakpoints */
    @media (max-width: 1080px) {
      .hero-grid {
        grid-template-columns: 1fr !important;
        gap: 40px !important;
      }
      .footer-grid {
        grid-template-columns: 1fr 1fr !important;
        gap: 32px !important;
      }
      .kpi-cards-grid {
        grid-template-columns: repeat(2, 1fr) !important;
      }
    }

    @media (max-width: 820px) {
      .form-grid-3 {
        grid-template-columns: 1fr !important;
        gap: 12px !important;
      }
      .form-grid-2,
      .responsive-split-2 {
        grid-template-columns: 1fr !important;
        gap: 16px !important;
      }
      .main-nav {
        padding: 10px 16px !important;
        flex-wrap: wrap;
        gap: 12px;
      }
      .nav-links-wrap {
        display: none !important; /* Hide desktop nav links on mobile to prevent squishing */
      }
      .nav-right-actions {
        margin-left: auto;
      }
      .hub-container-wrap {
        padding: 24px 16px 48px !important;
      }
      .events-selection-grid {
        grid-template-columns: 1fr !important;
      }
      .modal-card {
        padding: 20px 16px !important;
      }
      .footer-grid {
        grid-template-columns: 1fr !important;
        gap: 24px !important;
      }
      .footer-bottom-bar {
        flex-direction: column;
        align-items: flex-start;
        gap: 8px;
      }
    }

    @media (max-width: 600px) {
      .kpi-cards-grid {
        grid-template-columns: 1fr !important;
      }
      .hero-heading {
        font-size: 32px !important;
        line-height: 1.2 !important;
      }
      .hero-actions-row {
        flex-direction: column;
        align-items: stretch !important;
      }
      .hero-actions-row .btn-crimson,
      .hero-actions-row .btn-outline-dark {
        width: 100% !important;
        justify-content: center;
      }
      .page-back-nav-bar {
        padding: 10px 16px !important;
      }
      .page-breadcrumb {
        display: none !important;
      }
      .universal-side-back-btn {
        bottom: 16px;
        left: 12px;
        padding: 8px 14px;
        font-size: 11.5px;
      }
    }
'''

# Insert the design enhancement CSS before </style>
if '.container-wide' not in html:
    html = html.replace('</style>', design_enhancement_css + '\n  </style>')

# 2. Update Munshi Fast Entry Grid from inline styles to .form-grid-3
old_munshi_grid = '<div style="display: grid; grid-template-columns: 1.2fr 1fr 1fr; gap: 16px; margin-bottom: 16px;">'
new_munshi_grid = '<div class="form-grid-3">'
if old_munshi_grid in html:
    html = html.replace(old_munshi_grid, new_munshi_grid)

# 3. Update Settings 2-column grid from inline styles to .responsive-split-2
old_settings_grid = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; max-width: 1040px; margin: 0 auto;">'
new_settings_grid = '<div class="responsive-split-2" style="max-width: 1040px; margin: 0 auto;">'
if old_settings_grid in html:
    html = html.replace(old_settings_grid, new_settings_grid)

# 4. Update Expenses 2-column grid from inline styles to .form-grid-2
old_exp_grid = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px;">'
new_exp_grid = '<div class="form-grid-2" style="margin-bottom: 24px;">'
if old_exp_grid in html:
    html = html.replace(old_exp_grid, new_exp_grid)

# 5. Update Pricing Modal 2-column grid from inline styles to .responsive-split-2
old_pricing_grid = '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px;">'
new_pricing_grid = '<div class="responsive-split-2" style="margin-bottom: 24px;">'
if old_pricing_grid in html:
    html = html.replace(old_pricing_grid, new_pricing_grid)

# 6. Update Hero CTA Row to class .hero-actions-row
old_hero_row = '<div style="display: flex; gap: 14px; margin-bottom: 28px; flex-wrap: wrap;">'
new_hero_row = '<div class="hero-actions-row" style="display: flex; gap: 14px; margin-bottom: 28px; flex-wrap: wrap;">'
if old_hero_row in html:
    html = html.replace(old_hero_row, new_hero_row)

# 7. Update Ledger table headers with proper alignment classes
old_table_headers = '''                <tr>
                  <th data-i18n="th_sno">#</th>
                  <th data-i18n="th_guest">Guest Name</th>
                  <th data-i18n="th_place">Native Place</th>
                  <th data-i18n="th_mode">Mode</th>
                  <th data-i18n="th_amount">Auspicious Amount</th>
                  <th data-i18n="th_recorder">Recorded By</th>
                  <th data-i18n="th_photo">Photo Proof</th>
                  <th data-i18n="th_action">Receipt & Slip</th>
                </tr>'''

new_table_headers = '''                <tr>
                  <th class="th-center" style="width: 48px;" data-i18n="th_sno">#</th>
                  <th data-i18n="th_guest">Guest Name & Family</th>
                  <th data-i18n="th_place">Native Place</th>
                  <th class="th-center" style="width: 90px;" data-i18n="th_mode">Mode</th>
                  <th class="th-right" style="width: 130px;" data-i18n="th_amount">Auspicious Amount</th>
                  <th style="width: 130px;" data-i18n="th_recorder">Recorded By</th>
                  <th class="th-center" style="width: 100px;" data-i18n="th_photo">Photo Proof</th>
                  <th class="th-center" style="width: 160px;" data-i18n="th_action">Receipt & Slip</th>
                </tr>'''

if old_table_headers in html:
    html = html.replace(old_table_headers, new_table_headers)

# 8. Update table row rendering in JS to match alignment classes
old_js_row = '''    const row = document.createElement('tr');
    row.innerHTML = `
      <td><span class="serial-num">${safeSno}</span></td>
      <td><strong>${safeName}</strong><br><small style="color:var(--c-muted);">${safeRelation}</small></td>
      <td>${safePlace}</td>
      <td><span class="mode-badge ${badgeClass}">${escapeHtml(item.mode)}</span></td>
      <td class="num-currency" style="font-weight:700; color:var(--c-night);">${safeAmt}</td>
      <td><span style="font-size:11px; color:var(--c-muted); background:var(--c-base); padding:3px 6px; border-radius:4px; border:1px solid var(--c-border);">${safeRecorder}</span></td>
      <td>${photoHtml}</td>
      <td style="white-space:nowrap;">'''

new_js_row = '''    const row = document.createElement('tr');
    row.innerHTML = `
      <td class="td-center"><span class="serial-num">${safeSno}</span></td>
      <td><strong>${safeName}</strong><br><small style="color:var(--c-muted); font-size:11.5px;">${safeRelation}</small></td>
      <td>${safePlace}</td>
      <td class="td-center"><span class="mode-badge ${badgeClass}">${escapeHtml(item.mode)}</span></td>
      <td class="td-right num-currency" style="font-weight:800; color:var(--c-night); font-size:14.5px;">${safeAmt}</td>
      <td><span style="font-size:11px; color:var(--c-muted); background:var(--c-base); padding:3px 6px; border-radius:4px; border:1px solid var(--c-border); white-space:nowrap;">${safeRecorder}</span></td>
      <td class="td-center">${photoHtml}</td>
      <td class="td-center" style="white-space:nowrap;">'''

if old_js_row in html:
    html = html.replace(old_js_row, new_js_row)

for path in target_files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Polished & Synchronized: {path} ({len(html)} bytes)")

print("\nComprehensive design, alignment, and responsive overhaul complete!")
