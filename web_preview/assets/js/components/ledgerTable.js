/**
 * GiftVault Digital Ledger Component
 * Fast searching with Instant Autocomplete Suggestions, Row Mutations, UTF-8 CSV & Official PDF Export
 */

window.GVLedgerTable = {
  render() {
    const event = window.GVStore.getActiveEvent();
    const tbody = document.getElementById('ws-full-ledger-body');
    const recentTbody = document.getElementById('ws-recent-entries-tbody');
    if (!tbody || !event) return;

    tbody.innerHTML = '';
    if (recentTbody) recentTbody.innerHTML = '';

    const entries = event.entries || [];

    entries.forEach(item => {
      const row = document.createElement('tr');
      row.id = `row-${item.sno.replace(/[^a-zA-Z0-9]/g, '')}`;
      row.innerHTML = `
        <td><strong class="tabular-nums" style="color:var(--c-primary); font-weight:800;">${item.sno}</strong></td>
        <td><strong style="color:#0F172A; font-size:13.5px;">${item.name}</strong></td>
        <td style="color:#475569;">${item.place}</td>
        <td><span style="font-size:12px; color:#64748B; background:#F8F5F0; padding:2px 8px; border-radius:4px; border:1px solid #EBE5DB;">${item.relation}</span></td>
        <td><span style="background:var(--c-primary-light); color:var(--c-primary); padding:2px 8px; border-radius:4px; font-size:11px; font-weight:700; border:1px solid var(--c-primary-border);">${item.mode}</span></td>
        <td class="tabular-nums" style="font-weight:800; color:var(--c-primary); font-size:14.5px;">₹${item.amount.toLocaleString('en-IN')}</td>
        <td><span style="font-size:11.5px; color:#94A3B8;">${item.recorder || 'Desk 1'}</span></td>
        <td style="white-space:nowrap;">
          <button type="button" class="btn-secondary" style="padding:4px 9px; font-size:11.5px;" onclick="window.GVReceiptModal.open('${item.sno}', '${item.name}', '${item.place}', '${item.mode}', '₹${item.amount.toLocaleString('en-IN')}')">
            ${window.GVIcons.printer} <span>Slip</span>
          </button>
          <button type="button" class="btn-secondary" style="padding:4px 8px; font-size:11.5px; margin-left:4px;" onclick="window.GVLedgerTable.openEdit('${item.sno}')">
            ${window.GVIcons.edit}
          </button>
          <button type="button" class="btn-secondary" style="padding:4px 8px; font-size:11.5px; margin-left:4px; color:#EF4444;" onclick="window.GVLedgerTable.deleteEntry('${item.sno}')">
            ${window.GVIcons.trash}
          </button>
        </td>
      `;
      tbody.appendChild(row);

      if (recentTbody && recentTbody.children.length < 5) {
        recentTbody.appendChild(row.cloneNode(true));
      }
    });

    this.filter();
  },

  filter() {
    const qInput = document.getElementById('ledger-search-input');
    const mSelect = document.getElementById('ledger-filter-mode');
    const q = (qInput ? qInput.value : '').toLowerCase().trim();
    const m = (mSelect ? mSelect.value : 'ALL');

    const event = window.GVStore.getActiveEvent();
    const suggestionsBox = document.getElementById('ledger-search-suggestions');
    const rows = document.querySelectorAll('#ws-full-ledger-body tr');

    rows.forEach(r => {
      const text = r.innerText.toLowerCase();
      const matchesQ = text.includes(q);
      const matchesM = m === 'ALL' || text.includes(m.toLowerCase());
      r.style.display = (matchesQ && matchesM) ? '' : 'none';
    });

    // Update Live Search Suggestions Dropdown
    if (suggestionsBox && event && event.entries) {
      if (q.length > 0) {
        const matches = event.entries.filter(e => 
          e.name.toLowerCase().includes(q) || 
          e.place.toLowerCase().includes(q) ||
          e.relation.toLowerCase().includes(q)
        );

        if (matches.length > 0) {
          suggestionsBox.style.display = 'block';
          suggestionsBox.innerHTML = `
            <div style="padding:6px 12px; font-size:11px; font-weight:700; color:#64748B; background:#F8F5F0; border-bottom:1px solid #EBE5DB; text-transform:uppercase;">
              Matching Guests (${matches.length})
            </div>
            ${matches.slice(0, 6).map(m => `
              <div onclick="window.GVLedgerTable.selectSuggestion('${m.name}')" style="display:flex; justify-content:space-between; align-items:center; padding:8px 12px; cursor:pointer; border-bottom:1px solid #F1ECE4; transition:background 0.15s;" onmouseover="this.style.background='#FDF2F4'" onmouseout="this.style.background='#FFF'">
                <div>
                  <div style="font-weight:700; font-size:13px; color:#0F172A;">${m.name}</div>
                  <div style="font-size:11px; color:#64748B;">${m.place} • ${m.relation}</div>
                </div>
                <div style="text-align:right;">
                  <span style="font-weight:800; color:var(--c-primary); font-size:13px;">₹${m.amount.toLocaleString('en-IN')}</span>
                  <div style="font-size:10px; color:#94A3B8;">${m.sno}</div>
                </div>
              </div>
            `).join('')}
          `;
        } else {
          suggestionsBox.style.display = 'block';
          suggestionsBox.innerHTML = `
            <div style="padding:10px 14px; font-size:12px; color:#64748B; text-align:center;">
              No matching guest entries found for "${q}"
            </div>
          `;
        }
      } else {
        suggestionsBox.style.display = 'none';
      }
    }
  },

  selectSuggestion(name) {
    const qInput = document.getElementById('ledger-search-input');
    const suggestionsBox = document.getElementById('ledger-search-suggestions');
    if (qInput) qInput.value = name;
    if (suggestionsBox) suggestionsBox.style.display = 'none';
    this.filter();

    // Highlight row
    const rows = document.querySelectorAll('#ws-full-ledger-body tr');
    rows.forEach(r => {
      if (r.innerText.toLowerCase().includes(name.toLowerCase())) {
        r.style.background = '#FEF2F2';
        setTimeout(() => r.style.background = '', 2000);
      }
    });
  },

  openEdit(sno) {
    const event = window.GVStore.getActiveEvent();
    if (!event || !event.entries) return;
    const entry = event.entries.find(e => e.sno === sno);
    if (!entry) return;

    document.getElementById('edit-entry-sno').value = entry.sno;
    document.getElementById('edit-entry-name').value = entry.name;
    document.getElementById('edit-entry-city').value = entry.place;
    document.getElementById('edit-entry-relation').value = entry.relation;
    document.getElementById('edit-entry-amount').value = entry.amount;

    document.getElementById('modal-edit-entry').classList.add('active');
  },

  saveEdit(e) {
    e.preventDefault();
    const event = window.GVStore.getActiveEvent();
    if (!event || !event.entries) return;

    const sno = document.getElementById('edit-entry-sno').value;
    const entry = event.entries.find(e => e.sno === sno);
    if (!entry) return;

    entry.name = document.getElementById('edit-entry-name').value.trim();
    entry.place = document.getElementById('edit-entry-city').value.trim();
    entry.relation = document.getElementById('edit-entry-relation').value;
    entry.amount = parseInt(document.getElementById('edit-entry-amount').value, 10) || 0;

    event.totalBlessings = event.entries.reduce((sum, it) => sum + (parseInt(it.amount, 10) || 0), 0);
    const allEvents = window.GVStore.state.events;
    allEvents[event.id] = event;

    window.GVRepository.save(allEvents);
    window.GVStore.setState({ events: allEvents }, 'ENTRY_UPDATED');

    document.getElementById('modal-edit-entry').classList.remove('active');
    window.GVApp.showToast(`✓ Entry ${sno} updated successfully!`, 'gold');
  },

  deleteEntry(sno) {
    const event = window.GVStore.getActiveEvent();
    if (!event || !event.entries) return;
    const idx = event.entries.findIndex(e => e.sno === sno);
    if (idx === -1) return;

    event.entries.splice(idx, 1);
    event.totalBlessings = event.entries.reduce((sum, it) => sum + (parseInt(it.amount, 10) || 0), 0);
    event.envelopesCount = event.entries.length;

    const allEvents = window.GVStore.state.events;
    allEvents[event.id] = event;

    window.GVRepository.save(allEvents);
    window.GVStore.setState({ events: allEvents }, 'ENTRY_DELETED');

    window.GVApp.showToast(`Entry ${sno} deleted`, 'gold');
  },

  exportCSV() {
    const event = window.GVStore.getActiveEvent();
    if (!event || !event.entries) return;

    let csv = "Serial No,Guest Name,Native Place,Relationship,Payment Mode,Amount (INR)\n";
    event.entries.forEach(i => {
      csv += `"${i.sno}","${i.name}","${i.place}","${i.relation}","${i.mode}","${i.amount}"\n`;
    });

    const blob = new Blob(["\uFEFF" + csv], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `GiftVault_${event.title.replace(/[^a-zA-Z0-9]/g, '_')}_Ledger.csv`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    window.GVApp.showToast(`📥 Exported ${event.entries.length} entries to CSV!`, 'gold');
  },

  exportPDF() {
    const event = window.GVStore.getActiveEvent();
    if (!event || !event.entries) return;

    const printWin = window.open('', '_blank', 'width=900,height=750');
    if (!printWin) {
      window.print();
      return;
    }

    const rowsHtml = event.entries.map((item, idx) => `
      <tr style="border-bottom:1px solid #E2E8F0; ${idx % 2 === 0 ? 'background:#FAF8F5;' : 'background:#FFF;'}">
        <td style="padding:10px 12px; font-weight:800; color:#9E1B32;">${item.sno}</td>
        <td style="padding:10px 12px; font-weight:700; color:#0F172A;">${item.name}</td>
        <td style="padding:10px 12px; color:#475569;">${item.place}</td>
        <td style="padding:10px 12px; color:#475569;">${item.relation}</td>
        <td style="padding:10px 12px; color:#0F172A; font-weight:600;">${item.mode}</td>
        <td style="padding:10px 12px; text-align:right; font-weight:800; color:#9E1B32;">₹${item.amount.toLocaleString('en-IN')}</td>
      </tr>
    `).join('');

    const htmlContent = `
      <!DOCTYPE html>
      <html>
      <head>
        <title>GiftVault Official Celebration Ledger - ${event.title}</title>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
          body { font-family: 'Plus Jakarta Sans', sans-serif; margin: 40px; color: #0F172A; }
          .header { display: flex; justify-content: space-between; border-bottom: 2px solid #9E1B32; padding-bottom: 20px; margin-bottom: 24px; }
          .logo { font-family: 'Outfit', sans-serif; font-size: 26px; font-weight: 800; color: #9E1B32; }
          .title { font-family: 'Outfit', sans-serif; font-size: 22px; font-weight: 800; margin: 4px 0; color: #0F172A; }
          .meta { font-size: 13px; color: #475569; }
          .stat-box { background: #FAF7F2; border: 1px solid #E2E8F0; border-radius: 8px; padding: 12px 20px; text-align: right; }
          .stat-val { font-size: 22px; font-weight: 800; color: #9E1B32; }
          table { width: 100%; border-collapse: collapse; margin-top: 16px; font-size: 13px; }
          th { background: #9E1B32; color: #FFFFFF; padding: 10px 12px; text-align: left; font-weight: 700; font-size: 12px; }
          th:last-child { text-align: right; }
          .footer { margin-top: 40px; border-top: 1px dashed #CBD5E1; padding-top: 20px; display: flex; justify-content: space-between; font-size: 12px; color: #64748B; }
          @media print { body { margin: 20px; } button { display: none; } }
        </style>
      </head>
      <body>
        <div style="margin-bottom: 16px;">
          <button onclick="window.print()" style="padding: 10px 20px; background: #9E1B32; color: #FFF; border: none; border-radius: 6px; font-weight: 700; cursor: pointer;">
            🖨️ Print / Save as PDF
          </button>
        </div>

        <div class="header">
          <div>
            <div class="logo">🎁 GiftVault</div>
            <div class="title">${event.title}</div>
            <div class="meta">📅 Date: ${event.date} • 📍 Venue: ${event.venue} • 🏷️ Celebration: ${event.type}</div>
          </div>
          <div class="stat-box">
            <div style="font-size: 11px; text-transform: uppercase; color: #64748B; font-weight: 700;">Total Gifts & Shagun</div>
            <div class="stat-val">₹${(event.totalBlessings || 0).toLocaleString('en-IN')}</div>
            <div style="font-size: 11px; color: #059669; font-weight: 700;">${event.entries.length} Guest Envelopes</div>
          </div>
        </div>

        <table>
          <thead>
            <tr>
              <th>S.No</th>
              <th>Guest Name</th>
              <th>Native Place / City</th>
              <th>Relationship</th>
              <th>Payment Mode</th>
              <th>Amount (INR)</th>
            </tr>
          </thead>
          <tbody>
            ${rowsHtml}
          </tbody>
        </table>

        <div class="footer">
          <div>Official Family Record • Generated via GiftVault Digital Red Notebook</div>
          <div>Authorized Signature: _______________________</div>
        </div>
      </body>
      </html>
    `;

    printWin.document.write(htmlContent);
    printWin.document.close();
    window.GVApp.showToast(`📄 PDF report generated for ${event.title}!`, 'emerald');
  }
};
