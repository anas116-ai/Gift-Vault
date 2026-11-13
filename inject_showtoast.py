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
        c = f.read()

    if 'PRODUCTION ENGINE: TOASTS, EDIT/DELETE ENTRY' in c:
        print(f'{p}: already has production JS')
        continue

    # Inject right after <script>
    c = c.replace('<script>', '<script>\n' + js_production_code)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'{p}: successfully injected production JS after <script>')

print('Completed.')
