target_files = [
    r'c:\Project\Gift Valut\web_preview\index.html',
    r'c:\Project\Gift Valut\web_preview\desktop.html',
    r'c:\Project\Gift Valut\web_preview\mobile.html',
    r'c:\Project\Gift Valut\build\web\index.html',
    r'c:\Project\Gift Valut\web\index.html'
]

engine_code = '''// ==========================================
    // 7. MULTI-EVENT REAL DATABASE & PERSISTENCE ENGINE
    // ==========================================
    let currentActiveEventId = 'event-wedding';

    // Seed Data with Wedding, Birthday, and Chirala Beach Haircut / Tonsure
    const DEFAULT_EVENTS_DB = {
      'event-wedding': {
        id: 'event-wedding',
        title: 'Rahul & Snigdha Kalyanam',
        type: 'Wedding',
        date: '2026-11-24',
        venue: 'Grand Kalyana Mandapam, Guntur',
        totalBlessings: 842116,
        totalExpenses: 415000,
        goldGrams: 42.5,
        silverGrams: 550,
        envelopesCount: 4,
        entries: [
          { sno: '#GV-101', name: 'K. Venkata Rao Garu', relation: 'బావ / Brother-in-law', place: 'Vijayawada', mode: 'UPI', amount: 10116, phone: '+919848011223', recorder: 'Suresh (Desk 1)', photoUrl: '' },
          { sno: '#GV-102', name: 'M. Subba Reddy Garu', relation: 'మామ / Father-in-law', place: 'Guntur', mode: 'Cash', amount: 25116, phone: '+919848022334', recorder: 'Suresh (Desk 1)', photoUrl: '' },
          { sno: '#GV-103', name: 'T. Suresh Sharma', relation: 'స్నేహితుడు / Friend', place: 'Hyderabad', mode: 'Cash', amount: 5116, phone: '+919848033445', recorder: 'Ramesh (Desk 2)', photoUrl: '' },
          { sno: '#GV-104', name: 'V. Krishna Murthy Garu', relation: 'బాబాయ్ / Uncle', place: 'Tenali', mode: 'Gold', amount: 45000, phone: '+919848044556', recorder: 'Suresh (Desk 1)', photoUrl: '' }
        ]
      },
      'event-birthday': {
        id: 'event-birthday',
        title: 'Advait 1st Birthday & Cradle',
        type: 'Birthday',
        date: '2026-12-12',
        venue: 'Minerva Grand Banquet, Hyderabad',
        totalBlessings: 155000,
        totalExpenses: 80000,
        goldGrams: 15.0,
        silverGrams: 200,
        envelopesCount: 2,
        entries: [
          { sno: '#GV-101', name: 'P. Anjaneyulu Garu', relation: 'తాతయ్య / Grandfather', place: 'Rajahmundry', mode: 'Cash', amount: 11116, phone: '+919848055667', recorder: 'Suresh (Desk 1)', photoUrl: '' },
          { sno: '#GV-102', name: 'Ch. Madhav', relation: 'మేనమామ / Maternal Uncle', place: 'Hyderabad', mode: 'Gold', amount: 25000, phone: '+919848066778', recorder: 'Suresh (Desk 1)', photoUrl: '' }
        ]
      },
      'event-chirala-tonsure': {
        id: 'event-chirala-tonsure',
        title: 'Advait Tonsure / Hair Cut (పుట్టెంటకలు / కేశఖండన)',
        type: 'Tonsure',
        date: '2027-01-15',
        venue: 'Chirala Beach Shore Mandapam, Bapatla',
        totalBlessings: 36348,
        totalExpenses: 18000,
        goldGrams: 5.0,
        silverGrams: 150,
        envelopesCount: 3,
        entries: [
          { sno: '#GV-101', name: 'Mastan Rao Garu (Chirala)', relation: 'మేనమామ / Maternal Uncle', place: 'Chirala', mode: 'Cash', amount: 15116, phone: '+919848077889', recorder: 'Suresh (Desk 1)', photoUrl: '' },
          { sno: '#GV-102', name: 'S. Ramana Murthy', relation: 'బాబాయ్ / Uncle', place: 'Vetapalem', mode: 'UPI', amount: 11116, phone: '+919848088990', recorder: 'Suresh (Desk 1)', photoUrl: '' },
          { sno: '#GV-103', name: 'D. Srinivas Garu', relation: 'స్నేహితుడు / Friend', place: 'Bapatla', mode: 'Cash', amount: 10116, phone: '+919848099001', recorder: 'Suresh (Desk 1)', photoUrl: '' }
        ]
      }
    };

    function getEventsDatabase() {
      try {
        const saved = localStorage.getItem('GV_EVENTS_DATABASE_V1');
        if (saved) return JSON.parse(saved);
      } catch (e) {
        console.warn('LocalStorage read error:', e);
      }
      return DEFAULT_EVENTS_DB;
    }

    function saveEventsDatabase(db) {
      try {
        localStorage.setItem('GV_EVENTS_DATABASE_V1', JSON.stringify(db));
      } catch (e) {
        console.warn('LocalStorage save error:', e);
      }
    }

    let EVENTS_DATABASE = getEventsDatabase();

    function renderEventsHub() {
      const grid = document.getElementById('events-hub-grid');
      if (!grid) return;
      grid.innerHTML = '';

      Object.values(EVENTS_DATABASE).forEach(event => {
        const card = document.createElement('div');
        card.className = 'event-selection-card';
        card.onclick = () => enterWorkspaceEvent(event.id);

        let typeBadgeBg = 'var(--c-night)';
        if (event.type === 'Wedding') typeBadgeBg = 'var(--c-crimson)';
        if (event.type === 'Tonsure') typeBadgeBg = '#7C3AED';
        if (event.type === 'Birthday') typeBadgeBg = '#0284C7';
        if (event.type === 'Housewarming') typeBadgeBg = '#036D19';

        card.innerHTML = `
          <div>
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
              <span class="tag-badge" style="background: ${typeBadgeBg}; color: #FFFFFF;">${event.type.toUpperCase()}</span>
              <span style="font-family: var(--font-sans); font-feature-settings: 'tnum'; font-size: 12px; font-weight: 700; color: var(--c-emerald);">ACTIVE VAULT</span>
            </div>
            <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 800; color: var(--c-night); margin-bottom: 6px;">
              ${escapeHtml(event.title)}
            </h3>
            <p style="font-size: 12.5px; color: var(--c-muted); margin-bottom: 14px;">
              📅 ${escapeHtml(event.date)} • 📍 ${escapeHtml(event.venue)}
            </p>
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 18px;">
              <span class="tag-badge" style="background: var(--c-base); color: var(--c-night); border: 1px solid var(--c-border);">
                ${event.entries ? event.entries.length : 0} Envelopes
              </span>
              <span class="tag-badge" style="background: #ECFDF5; color: var(--c-emerald); border: 1px solid #A7F3D0; font-weight: 800;">
                ₹${event.totalBlessings.toLocaleString('en-IN')} Total
              </span>
            </div>
          </div>
          <button type="button" class="btn-crimson" style="width: 100%; justify-content: center; padding: 10px;">
            <span>Enter Auspicious Desk →</span>
          </button>
        `;
        grid.appendChild(card);
      });
    }

    function enterWorkspaceEvent(eventId) {
      if (!EVENTS_DATABASE[eventId]) {
        eventId = 'event-wedding';
      }
      currentActiveEventId = eventId;
      const event = EVENTS_DATABASE[eventId];

      document.getElementById('ws-event-header-name').innerText = event.title;
      const subMeta = document.getElementById('ws-event-sub-meta');
      if (subMeta) {
        subMeta.innerText = `📅 ${event.date} • 📍 ${event.venue} • 🏷️ ${event.type}`;
      }

      updateWorkspaceKPIs(event);
      renderActiveEventTables();
      navToView('app');
    }

    function updateWorkspaceKPIs(event) {
      const totalAmtEl = document.getElementById('overview-total-amt');
      if (totalAmtEl) totalAmtEl.innerText = '₹' + event.totalBlessings.toLocaleString('en-IN');

      const countEl = document.getElementById('overview-envelopes-count');
      if (countEl) countEl.innerText = `${event.entries.length} envelopes logged`;

      const scInflow = document.getElementById('showcase-inflow-val');
      if (scInflow) scInflow.innerText = '₹' + event.totalBlessings.toLocaleString('en-IN');

      const scSurplus = document.getElementById('showcase-surplus-val');
      if (scSurplus) {
        const surplus = event.totalBlessings - (event.totalExpenses || 0);
        scSurplus.innerText = (surplus >= 0 ? '+' : '') + '₹' + surplus.toLocaleString('en-IN');
      }
    }

    function renderActiveEventTables() {
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event) return;

      const fullTbody = document.getElementById('ws-full-ledger-body');
      const recentTbody = document.getElementById('ws-recent-table-body');

      if (fullTbody) fullTbody.innerHTML = '';
      if (recentTbody) recentTbody.innerHTML = '';

      if (!event.entries || event.entries.length === 0) {
        if (fullTbody) {
          fullTbody.innerHTML = `<tr><td colspan="8" style="text-align: center; padding: 36px 16px; color: var(--c-muted);">
            🏮 ఈ శుభకార్యానికి ఇంకా చదివింపులు నమోదు కాలేదు. మున్షీ డెస్క్ నుండి మొదటి చదివింపును నమోదు చేయండి!
          </td></tr>`;
        }
        if (recentTbody) {
          recentTbody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 20px; color: var(--c-muted);">No entries yet</td></tr>`;
        }
        return;
      }

      event.entries.forEach(item => {
        const safeName = escapeHtml(item.name);
        const safeRelation = escapeHtml(item.relation || 'బంధువు / Relative');
        const safePlace = escapeHtml(item.place);
        const safeSno = escapeHtml(item.sno);
        const safeRecorder = escapeHtml(item.recorder || 'Suresh (Desk 1)');
        const safeAmt = '₹' + item.amount.toLocaleString('en-IN');
        const safePhone = escapeHtml(item.phone || '');

        let badgeClass = 'mode-cash';
        if (item.mode === 'UPI') badgeClass = 'mode-upi';
        if (item.mode === 'Gold') badgeClass = 'mode-gold';
        if (item.mode === 'Silver') badgeClass = 'mode-silver';

        const photoHtml = item.photoUrl ? `<span style="color:var(--c-emerald); font-weight:700;">📷 Photo</span>` : `<span style="color:var(--c-muted); font-size:11px;">None</span>`;

        if (fullTbody) {
          const row = document.createElement('tr');
          row.innerHTML = `
            <td class="td-center"><span class="serial-num">${safeSno}</span></td>
            <td><strong>${safeName}</strong><br><small style="color:var(--c-muted); font-size:11.5px;">${safeRelation}</small></td>
            <td>${safePlace}</td>
            <td class="td-center"><span class="mode-badge ${badgeClass}">${escapeHtml(item.mode)}</span></td>
            <td class="td-right num-currency" style="font-weight:800; color:var(--c-night); font-size:14.5px;">${safeAmt}</td>
            <td><span style="font-size:11px; color:var(--c-muted); background:var(--c-base); padding:3px 6px; border-radius:4px; border:1px solid var(--c-border); white-space:nowrap;">${safeRecorder}</span></td>
            <td class="td-center">${photoHtml}</td>
            <td class="td-center" style="white-space:nowrap;">
              <button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${safeName.replace(/'/g, "\\\\'")}', '${safeAmt}', '${safePhone}', '${safePlace.replace(/'/g, "\\\\'")}')">
                📲 WhatsApp
              </button>
              <button type="button" class="btn-outline-dark" style="padding:4px 8px; font-size:11px; margin-left:4px;" onclick="openPrintSlip('${safeSno}', '${safeName.replace(/'/g, "\\\\'")}', '${safePlace.replace(/'/g, "\\\\'")}', '${escapeHtml(item.mode)}', '${safeAmt}')">
                🖨️ Slip
              </button>
            </td>
          `;
          fullTbody.appendChild(row);
        }

        if (recentTbody) {
          const recRow = document.createElement('tr');
          recRow.innerHTML = `
            <td>Just now</td>
            <td><strong>${safeName}</strong></td>
            <td>${safePlace}</td>
            <td>${safeRelation}</td>
            <td class="num-currency" style="color: var(--c-emerald); font-weight: 700;">${safeAmt}</td>
            <td><span class="mode-badge ${badgeClass}">${escapeHtml(item.mode)}</span></td>
            <td><button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${safeName.replace(/'/g, "\\\\'")}', '${safeAmt}', '${safePhone}', '${safePlace.replace(/'/g, "\\\\'")}')">📲 WhatsApp</button></td>
          `;
          recentTbody.prepend(recRow);
        }
      });
    }

    function handleMunshiSubmit(e) {
      e.preventDefault();
      const event = EVENTS_DATABASE[currentActiveEventId];
      if (!event) return;

      const name = document.getElementById('entry-name').value.trim();
      const city = document.getElementById('entry-city').value.trim() || 'Chirala';
      const rel = document.getElementById('entry-relation') ? document.getElementById('entry-relation').value : 'బంధువు / Relative';
      const amt = parseInt(document.getElementById('entry-amount').value, 10) || 0;
      const phone = document.getElementById('entry-phone') ? document.getElementById('entry-phone').value.trim() : '';

      const activeModeBtn = document.querySelector('.mode-btn.active') || document.querySelector('.mode-select-btn.active');
      const mode = activeModeBtn ? activeModeBtn.innerText.trim() : 'Cash';

      const nextNum = (event.entries ? event.entries.length : 0) + 1;
      const sno = `#GV-${100 + nextNum}`;

      const newEntry = {
        sno: sno,
        name: name,
        place: city,
        relation: rel,
        mode: mode,
        amount: amt,
        phone: phone,
        photoUrl: currentPhotoBase64 || '',
        recorder: 'Suresh (Desk 1)',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };

      if (!event.entries) event.entries = [];
      event.entries.push(newEntry);
      event.totalBlessings += amt;
      event.envelopesCount = event.entries.length;

      saveEventsDatabase(EVENTS_DATABASE);
      testSoundboxAnnouncement(name, amt);

      updateWorkspaceKPIs(event);
      renderActiveEventTables();
      renderEventsHub();

      document.getElementById('entry-name').value = '';
      document.getElementById('entry-amount').value = '';
      const photoPreview = document.getElementById('gift-photo-preview');
      if (photoPreview) {
        photoPreview.style.display = 'none';
        currentPhotoBase64 = null;
      }

      alert(currentLang === 'te' ? `${name} గారి చదివింపు (${sno} - ₹${amt}) "${event.title}" లో విజయవంతంగా నమోదైంది!` : `Successfully recorded shagun for ${name} (${sno} - ₹${amt}) in "${event.title}"!`);
    }

    function handleCreateEventSubmit(e) {
      e.preventDefault();
      const title = document.getElementById('new-event-title').value.trim();
      const type = document.getElementById('new-event-type').value;
      const date = document.getElementById('new-event-date').value || new Date().toISOString().split('T')[0];
      const venue = document.getElementById('new-event-venue').value.trim() || 'Chirala Beach Shore Mandapam';
      const guests = parseInt(document.getElementById('new-event-guests').value, 10) || 200;

      const newId = 'event-' + Date.now();
      EVENTS_DATABASE[newId] = {
        id: newId,
        title: title,
        type: type,
        date: date,
        venue: venue,
        guestsCount: guests,
        totalBlessings: 0,
        totalExpenses: 0,
        goldGrams: 0,
        silverGrams: 0,
        envelopesCount: 0,
        entries: []
      };

      saveEventsDatabase(EVENTS_DATABASE);
      renderEventsHub();
      closeCreateEventModal();
      enterWorkspaceEvent(newId);

      alert(currentLang === 'te' ? `నూతన శుభకార్యం "${title}" ఖజానా విజయవంతంగా సృష్టించబడింది! మొదటి చదివింపును (#GV-101) నమోదు చేయండి.` : `New celebration "${title}" created successfully! Record entry #GV-101 at the desk.`);
    }

    function updateLiveCalculator() {
      const type = document.getElementById('calc-event-type').value;
      const guests = parseInt(document.getElementById('calc-guest-slider').value, 10);
      document.getElementById('calc-guest-lbl').innerText = guests;

      let avg = 2200;
      if (type === 'tonsure') avg = 1800;
      if (type === 'housewarming') avg = 2500;
      if (type === 'birthday') avg = 1500;
      if (type === 'wedding') avg = 3000;

      document.getElementById('calc-avg-txt').innerText = `Avg ₹${avg.toLocaleString('en-IN')}/guest`;
      const total = guests * avg;
      document.getElementById('calc-total-shagun').innerText = '₹' + total.toLocaleString('en-IN');
    }

    '''

for p in target_files:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    idx1 = c.find('function handleMunshiSubmit(e) {')
    idx2 = c.find('function testSoundboxAnnouncement(', idx1)
    if idx1 != -1 and idx2 != -1:
        c = c[:idx1] + engine_code + c[idx2:]
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Injected Real Database Engine into {p}")
    else:
        print(f"⚠️ Bounds not found in {p}")

print("\nEngine injection complete!")
