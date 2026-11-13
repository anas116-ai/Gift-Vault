import re

# 1. Print CSS and Toast CSS to inject into <style>
production_css = '''
    /* ==========================================================================
       PRODUCTION-GRADE TOAST & PRINT STYLES
       ========================================================================== */
    .toast-container {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 9999999;
      display: flex;
      flex-direction: column;
      gap: 10px;
      pointer-events: none;
    }
    .toast-pill {
      pointer-events: auto;
      background: #000411;
      color: #FFFFFF;
      padding: 12px 18px;
      border-radius: 12px;
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 12px;
      box-shadow: 0 16px 36px rgba(0, 4, 17, 0.45);
      border: 1.5px solid rgba(229, 169, 60, 0.5);
      transform: translateY(20px);
      opacity: 0;
      transition: all 0.28s cubic-bezier(0.23, 1, 0.32, 1);
      max-width: 420px;
    }
    .toast-pill.show {
      transform: translateY(0);
      opacity: 1;
    }
    .toast-pill.success {
      border-color: #036D19;
      background: linear-gradient(135deg, #000411 0%, #03280B 100%);
    }
    .toast-pill.delete {
      border-color: #F8333C;
      background: linear-gradient(135deg, #000411 0%, #2D0507 100%);
    }

    /* Print Ledger Formal Stylesheet */
    .print-only {
      display: none;
    }
    @media print {
      #ambient-canvas,
      .main-header,
      .main-footer,
      .page-back-nav-bar,
      .ws-tabs-bar,
      .ledger-filter-bar,
      .btn-crimson,
      .btn-emerald,
      .btn-outline-dark,
      .btn-whatsapp-sm,
      .modal-backdrop,
      .toast-container,
      #tab-overview,
      #tab-entry,
      #tab-expenses,
      #tab-reciprocity {
        display: none !important;
      }

      body {
        background: #FFFFFF !important;
        color: #000000 !important;
        font-size: 11pt !important;
      }

      #view-app,
      #tab-ledger {
        display: block !important;
        opacity: 1 !important;
        padding: 0 !important;
        margin: 0 !important;
      }

      .print-only {
        display: block !important;
      }

      .ledger-table-wrap {
        overflow: visible !important;
        border: none !important;
      }

      .ledger-table {
        width: 100% !important;
        border-collapse: collapse !important;
        margin-top: 14px !important;
      }

      .ledger-table th,
      .ledger-table td {
        border: 1px solid #333333 !important;
        padding: 6px 8px !important;
        font-size: 9.5pt !important;
        color: #000000 !important;
      }
    }
'''

# 2. Toast container and Edit Modal HTML
toast_and_modal_html = '''
  <!-- TOAST NOTIFICATION CONTAINER -->
  <div id="toast-container" class="toast-container"></div>

  <!-- EDIT CHADIVIMPU ENTRY AUDIT MODAL -->
  <div id="modal-edit-entry" class="modal-backdrop">
    <div class="modal-dialog" style="max-width: 520px;">
      <div class="modal-header">
        <div>
          <div class="showcase-tag-sub">AUDIT CORRECTION</div>
          <h3 id="edit-modal-title" style="font-family: var(--font-serif); font-size: 22px; color: var(--c-night);">Edit Blessing Record</h3>
        </div>
        <button type="button" class="modal-close-btn" onclick="closeEditEntryModal()">✕</button>
      </div>
      <div class="modal-body">
        <form onsubmit="handleEditEntrySubmit(event)">
          <input type="hidden" id="edit-entry-sno">
          <div class="form-group-item">
            <label class="form-label-txt">Guest Full Name *</label>
            <input type="text" id="edit-entry-name" class="form-input-field" required>
          </div>
          <div class="form-grid-2">
            <div class="form-group-item">
              <label class="form-label-txt">Native City / Town</label>
              <input type="text" id="edit-entry-city" class="form-input-field">
            </div>
            <div class="form-group-item">
              <label class="form-label-txt">Relationship</label>
              <input type="text" id="edit-entry-relation" class="form-input-field">
            </div>
          </div>
          <div class="form-grid-2">
            <div class="form-group-item">
              <label class="form-label-txt">Blessing Amount (₹) *</label>
              <input type="number" id="edit-entry-amount" class="form-input-field num-currency" required>
            </div>
            <div class="form-group-item">
              <label class="form-label-txt">Payment Mode</label>
              <select id="edit-entry-mode" class="form-input-field">
                <option value="Cash">Cash</option>
                <option value="UPI">UPI PhonePe/GPay</option>
                <option value="Gold">Gold</option>
                <option value="Silver">Silver</option>
              </select>
            </div>
          </div>
          <div style="display: flex; gap: 10px; margin-top: 20px;">
            <button type="button" class="btn-outline-dark" onclick="closeEditEntryModal()">Cancel</button>
            <button type="submit" class="btn-crimson" style="flex: 1; justify-content: center;">Save Audit Corrections</button>
          </div>
        </form>
      </div>
    </div>
  </div>
'''

# 3. Print Header & Footer inside tab-ledger
print_ledger_header_html = '''
        <!-- Official Sacred Print Header (Visible during Print only) -->
        <div class="print-only" style="text-align: center; border-bottom: 2px solid #000; padding-bottom: 12px; margin-bottom: 16px;">
          <div style="font-size: 16pt; font-weight: 800; letter-spacing: 0.05em;">॥ శ్రీరస్తు • శుభమస్తు • అవిఘ్నమస్తు ॥</div>
          <div style="font-size: 14pt; font-weight: 800; margin-top: 4px;">GIFTVAULT (గిఫ్ట్ వాలెట్) • రాయల్ శుభకార్య ఖజానా రిజిస్టర్</div>
          <div id="print-event-meta" style="font-size: 10pt; color: #333; margin-top: 4px;">Official Celebration Audit Ledger</div>
        </div>
'''

print_ledger_footer_html = '''
        <!-- Official Print Footer Signature Block -->
        <div class="print-only" style="margin-top: 36px; padding-top: 18px; border-top: 1px dashed #000; display: flex; justify-content: space-between; font-size: 10pt;">
          <div>
            <strong>తయారు చేసిన మున్షీ (Recorded by):</strong><br>
            ...................................................
          </div>
          <div style="text-align: center;">
            <strong>మొత్తం చదివింపులు (Total Blessings):</strong><br>
            <span id="print-total-blessings" style="font-size: 12pt; font-weight: 800;">₹0</span>
          </div>
          <div style="text-align: right;">
            <strong>కుటుంబ పెద్దల సంతకం (Audited & Approved):</strong><br>
            ...................................................
          </div>
        </div>
'''

# 4. JS Production Engine additions
js_production_code = '''
    // ==========================================================================
    // PRODUCTION ENGINE: TOASTS, EDIT/DELETE ENTRY, EVENT AUDIT & CSV
    // ==========================================================================
    let isSoundboxMuted = false;

    function toggleSoundboxMute() {
      isSoundboxMuted = !isSoundboxMuted;
      const btnText = document.getElementById('soundbox-toggle-text');
      if (btnText) {
        btnText.innerText = isSoundboxMuted ? '🔇 Soundbox Muted' : '🔊 Soundbox ON';
      }
      showToast(isSoundboxMuted ? '🔇 Soundbox audio muted' : '🔊 Soundbox audio activated', 'gold');
    }

    function showToast(message, type = 'gold') {
      const container = document.getElementById('toast-container');
      if (!container) return;
      const toast = document.createElement('div');
      toast.className = `toast-pill ${type}`;
      let icon = '✨';
      if (type === 'success') icon = '✓';
      if (type === 'delete') icon = '🗑️';
      if (type === 'slip') icon = '🖨️';
      toast.innerHTML = `<span style="font-size: 18px;">${icon}</span><span>${message}</span>`;
      container.appendChild(toast);
      requestAnimationFrame(() => toast.classList.add('show'));
      setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
      }, 3500);
    }

    // Replace native alert with Toast
    window.alert = function(msg) {
      showToast(msg, 'gold');
    };

    function openEditEntryModal(sno) {
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event || !event.entries) return;
      const entry = event.entries.find(e => e.sno === sno);
      if (!entry) return;

      document.getElementById('edit-entry-sno').value = entry.sno;
      document.getElementById('edit-entry-name').value = entry.name;
      document.getElementById('edit-entry-city').value = entry.place;
      document.getElementById('edit-entry-relation').value = entry.relation || '';
      document.getElementById('edit-entry-amount').value = entry.amount;
      document.getElementById('edit-entry-mode').value = entry.mode;
      document.getElementById('edit-modal-title').innerText = `Edit Blessing (${entry.sno})`;

      const modal = document.getElementById('modal-edit-entry');
      if (modal) modal.classList.add('active');
    }

    function closeEditEntryModal() {
      const modal = document.getElementById('modal-edit-entry');
      if (modal) modal.classList.remove('active');
    }

    function handleEditEntrySubmit(e) {
      e.preventDefault();
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event || !event.entries) return;

      const sno = document.getElementById('edit-entry-sno').value;
      const entry = event.entries.find(e => e.sno === sno);
      if (!entry) return;

      entry.name = document.getElementById('edit-entry-name').value.trim();
      entry.place = document.getElementById('edit-entry-city').value.trim();
      entry.relation = document.getElementById('edit-entry-relation').value.trim();
      entry.amount = parseInt(document.getElementById('edit-entry-amount').value, 10) || 0;
      entry.mode = document.getElementById('edit-entry-mode').value;

      event.totalBlessings = event.entries.reduce((sum, item) => sum + (parseInt(item.amount, 10) || 0), 0);
      saveEventsDatabase(EVENTS_DATABASE);
      updateWorkspaceKPIs(event);
      renderActiveEventTables();
      closeEditEntryModal();
      showToast(`✓ Entry ${sno} updated! Total recalculated to ₹${event.totalBlessings.toLocaleString('en-IN')}`, 'success');
    }

    function deleteEntry(sno) {
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event || !event.entries) return;
      const idx = event.entries.findIndex(e => e.sno === sno);
      if (idx === -1) return;

      const item = event.entries[idx];
      event.entries.splice(idx, 1);
      event.totalBlessings = event.entries.reduce((sum, it) => sum + (parseInt(it.amount, 10) || 0), 0);
      event.envelopesCount = event.entries.length;

      saveEventsDatabase(EVENTS_DATABASE);
      updateWorkspaceKPIs(event);
      renderActiveEventTables();
      renderEventsHub();
      showToast(`🗑️ Entry ${sno} (${item.name}) removed. Total updated.`, 'delete');
    }

    function deleteCelebrationEvent(eventId, evObj) {
      if (evObj) evObj.stopPropagation();
      const ev = EVENTS_DATABASE[eventId];
      if (!ev) return;

      delete EVENTS_DATABASE[eventId];
      saveEventsDatabase(EVENTS_DATABASE);
      renderEventsHub();
      showToast(`🗑️ Celebration "${ev.title}" deleted from Treasury.`, 'delete');
    }

    function exportLedgerCSV() {
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event || !event.entries || event.entries.length === 0) {
        showToast('⚠️ No entries in this celebration to export!', 'gold');
        return;
      }

      let csv = "Serial No,Guest Name,Native Place,Relationship,Payment Mode,Amount (INR),Recorded By,Phone\\n";
      event.entries.forEach(item => {
        const row = [
          item.sno || '',
          item.name || '',
          item.place || '',
          item.relation || '',
          item.mode || '',
          item.amount || 0,
          item.recorder || 'Desk 1',
          item.phone || ''
        ].map(val => '"' + String(val).replace(/"/g, '""') + '"');
        csv += row.join(',') + '\\n';
      });

      const blob = new Blob(["\\uFEFF" + csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const cleanTitle = (event.title || 'Celebration').replace(/[^a-zA-Z0-9_]/g, '_');
      const link = document.createElement("a");
      link.setAttribute("href", url);
      link.setAttribute("download", `GiftVault_${cleanTitle}_Ledger.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
      showToast(`📥 Exported ${event.entries.length} entries to CSV!`, 'success');
    }

    function printLedgerSheet() {
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (event) {
        const pMeta = document.getElementById('print-event-meta');
        if (pMeta) pMeta.innerText = `${event.title} • 📅 ${event.date} • 📍 ${event.venue}`;
        const pTotal = document.getElementById('print-total-blessings');
        if (pTotal) pTotal.innerText = '₹' + event.totalBlessings.toLocaleString('en-IN') + ` (${event.entries ? event.entries.length : 0} Envelopes)`;
      }
      window.print();
    }
'''

files = ['web_preview/index.html', 'web_preview/desktop.html', 'web_preview/mobile.html', 'build/web/index.html', 'web/index.html']

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject production CSS
    if 'PRODUCTION-GRADE TOAST & PRINT STYLES' not in content:
        content = content.replace('  </style>', production_css + '\n  </style>')
        print(f'{p}: injected production CSS')

    # 2. Inject Toast & Edit Modal before </body>
    if 'id="modal-edit-entry"' not in content:
        content = content.replace('</body>', toast_and_modal_html + '\n</body>')
        print(f'{p}: injected Toast & Edit Modal')

    # 3. Inject Print header & footer into tab-ledger
    if 'class="print-only"' not in content:
        target_tb = '<div class="ledger-table-wrap">'
        if target_tb in content:
            content = content.replace(target_tb, print_ledger_header_html + '\n' + target_tb)
            print(f'{p}: injected print header into tab-ledger')
        target_tb_end = '</table>\n        </div>'
        if target_tb_end in content:
            content = content.replace(target_tb_end, target_tb_end + '\n' + print_ledger_footer_html)
            print(f'{p}: injected print footer into tab-ledger')

    # 4. Inject Production JS Engine
    if 'PRODUCTION ENGINE: TOASTS, EDIT/DELETE ENTRY' not in content:
        target_js = '    // ==========================================\n    // 1. NAVIGATION & ROUTING'
        if target_js in content:
            content = content.replace(target_js, js_production_code + '\n' + target_js)
            print(f'{p}: injected production JS')

    # 5. Update renderActiveEventTables action buttons to include Edit & Delete
    old_actions = """            <td class="td-center" style="white-space:nowrap;">
              <button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${safeName.replace(/'/g, "\\\\'")}', '${safeAmt}', '${safePhone}', '${safePlace.replace(/'/g, "\\\\'")}')">
                📲 WhatsApp
              </button>
              <button type="button" class="btn-outline-dark" style="padding:4px 8px; font-size:11px; margin-left:4px;" onclick="openPrintSlip('${safeSno}', '${safeName.replace(/'/g, "\\\\'")}', '${safePlace.replace(/'/g, "\\\\'")}', '${escapeHtml(item.mode)}', '${safeAmt}')">
                🖨️ Slip
              </button>
            </td>"""

    new_actions = """            <td class="td-center" style="white-space:nowrap;">
              <button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${safeName.replace(/'/g, "\\\\'")}', '${safeAmt}', '${safePhone}', '${safePlace.replace(/'/g, "\\\\'")}')">
                📲 WhatsApp
              </button>
              <button type="button" class="btn-outline-dark" style="padding:4px 8px; font-size:11px; margin-left:4px;" onclick="openPrintSlip('${safeSno}', '${safeName.replace(/'/g, "\\\\'")}', '${safePlace.replace(/'/g, "\\\\'")}', '${escapeHtml(item.mode)}', '${safeAmt}')">
                🖨️ Slip
              </button>
              <button type="button" class="btn-outline-dark" style="padding:4px 8px; font-size:11px; margin-left:4px;" onclick="openEditEntryModal('${safeSno}')">
                ✏️
              </button>
              <button type="button" class="btn-outline-dark" style="padding:4px 8px; font-size:11px; margin-left:4px; color:#DC2626; border-color:#FECDD3;" onclick="deleteEntry('${safeSno}')">
                🗑️
              </button>
            </td>"""

    if old_actions in content:
        content = content.replace(old_actions, new_actions)
        print(f'{p}: updated row action buttons with Edit & Delete')

    # 6. Update print button in tab-ledger to call printLedgerSheet()
    content = content.replace('onclick="window.print()"', 'onclick="printLedgerSheet()"')

    # 7. Update Event Cards in renderEventsHub to include Delete button
    old_card_btn = """          <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 10px;">
            <span>Enter Auspicious Desk →</span>
          </button>"""

    new_card_btn = """          <div style="display: flex; gap: 8px; margin-top: 10px;">
            <button type="button" class="btn-crimson" style="flex: 1; justify-content: center; padding: 10px;" onclick="enterWorkspaceEvent('${event.id}')">
              <span>Enter Auspicious Desk →</span>
            </button>
            <button type="button" class="btn-outline-dark" style="padding: 10px 14px; color: #DC2626; border-color: #FECDD3;" title="Delete Celebration" onclick="deleteCelebrationEvent('${event.id}', event)">
              🗑️
            </button>
          </div>"""

    if old_card_btn in content:
        content = content.replace(old_card_btn, new_card_btn)
        print(f'{p}: updated Event cards with Delete action')

    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)

print('All 5 files updated to 100% Production Grade.')
