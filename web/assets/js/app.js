/**
 * GiftVault Application Controller & Bootstrap
 * Modern Senior Staff Engineer Architecture: Modular orchestration, backward compatibility bridges
 */

window.GVApp = {
  checkAuthSession() {
    try {
      const raw = localStorage.getItem('GV_AUTH_SESSION');
      const badge = document.getElementById('nav-user-badge');
      const avatar = document.getElementById('nav-user-avatar');
      const nameEl = document.getElementById('nav-user-name');
      const signinBtn = document.getElementById('btn-header-signin');

      if (raw) {
        const sess = JSON.parse(raw);
        if (badge) badge.style.display = 'inline-flex';
        if (avatar) avatar.innerText = sess.initials || 'SK';
        if (nameEl) nameEl.innerText = sess.name || 'Sri Krishna Family';
        // Keep Sign In button always visible on landing navbar per user direction
        if (signinBtn) signinBtn.style.display = 'inline-flex';
        if (badge) badge.style.display = 'none';
      }
    } catch (e) {}
  },

  init() {
    this.checkAuthSession();
    // 1. Initialize State with Database seeds or persistence
    const storedEvents = window.GVRepository.load();
    window.GVStore.setState({ events: storedEvents, activeEventId: 'event-wedding' });

    // 2. Subscribe renderers to state changes
    window.GVStore.subscribe((state, action) => {
      this.renderHub();
      this.updateWorkspaceHeader();
      window.GVLedgerTable.render();
    });

    // 3. Initialize Component Runtimes
    if (window.GVHero3D && typeof window.GVHero3D.init === 'function') {
      window.GVHero3D.init();
    }
    if (window.GVEstimator && typeof window.GVEstimator.update === 'function') {
      window.GVEstimator.update();
    }
    if (window.GVKeyboard && typeof window.GVKeyboard.init === 'function') {
      window.GVKeyboard.init();
    }
    this.renderHub();
    this.updateWorkspaceHeader();
    if (window.GVLedgerTable && typeof window.GVLedgerTable.render === 'function') {
      window.GVLedgerTable.render();
    }
  },

  showToast(message, type = 'gold') {
    const container = document.getElementById('toast-container');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = 'toast-pill-lux';
    toast.innerHTML = `<span>${message}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.25s ease';
      setTimeout(() => toast.remove(), 250);
    }, 3200);
  },

  navTo(viewId) {
    document.querySelectorAll('.view-screen-pane').forEach(el => el.classList.remove('active'));
    const target = document.getElementById('view-' + viewId);
    if (target) {
      target.classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
    window.GVStore.setState({ activeView: viewId });
    if (viewId === 'hub') this.renderHub();

    // Isolate views: Landing footer only shows on the Landing page
    const footer = document.querySelector('.footer-master');
    if (footer) {
      footer.style.display = (viewId === 'landing') ? 'block' : 'none';
    }

    // Full-screen view isolation: Global header is hidden on login for 100% immersive canvas
    const header = document.querySelector('.header-glass');
    if (header) {
      header.style.display = (viewId === 'login') ? 'none' : 'block';
    }
  },

  renderHub() {
    const grid = document.getElementById('events-hub-grid');
    if (!grid) return;
    grid.innerHTML = '';

    const events = Object.values(window.GVStore.state.events);
    events.forEach(event => {
      const card = document.createElement('div');
      card.className = 'card-luxury event-card-luxury event-selection-card';
      card.style.cursor = 'pointer';
      card.onclick = (e) => {
        if (!e.target.closest('button')) this.enterEvent(event.id);
      };

      card.innerHTML = `
        <div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
            <div style="display:flex; align-items:center; gap:6px;">
              <span style="background:var(--c-primary); color:#FFF; font-size:10.5px; font-weight:800; padding:4px 10px; border-radius:var(--radius-full); letter-spacing:0.06em;">
                ${event.type.toUpperCase()}
              </span>
              ${event.role ? `<span style="background:#FEF3C7; color:#92400E; font-size:10px; font-weight:800; padding:3px 8px; border-radius:var(--radius-full); border:1px solid #FDE68A;">${event.role.toUpperCase()}</span>` : ''}
            </div>
            <span style="font-size:11.5px; color:var(--c-emerald); font-weight:700;">● Active Vault</span>
          </div>
          <h3 style="font-family:var(--font-sans); font-size:18px; font-weight:800; color:#0F172A; margin-bottom:6px;">
            ${event.title}
          </h3>
          <p style="font-size:12.5px; color:var(--text-secondary); margin-bottom:16px;">
            📅 ${event.date} • 📍 ${event.venue}
          </p>
          <div style="display:flex; gap:8px; margin-bottom:20px;">
            <span style="background:#F5EFEB; border:1px solid var(--border-subtle); padding:4px 10px; border-radius:var(--radius-sm); font-size:12px; color:#475569; font-weight:600;">
              ${event.entries ? event.entries.length : 0} Envelopes
            </span>
            <span style="background:var(--c-primary-light); border:1px solid var(--c-primary-border); padding:4px 10px; border-radius:var(--radius-sm); font-size:12px; color:var(--c-primary); font-weight:800;">
              ₹${(event.totalBlessings || 0).toLocaleString('en-IN')} Total
            </span>
          </div>
        </div>
        <div style="display:flex; gap:8px;">
          <button type="button" class="btn-primary" style="flex:1;" onclick="window.GVApp.enterEvent('${event.id}')">
            <span>Enter Gift Desk</span> ${window.GVIcons.arrowRight}
          </button>
          <button type="button" class="btn-secondary" style="padding:10px 14px; color:#EF4444;" title="Delete Celebration" onclick="window.GVApp.deleteEvent('${event.id}', event)">
            ${window.GVIcons.trash}
          </button>
        </div>
      `;
      grid.appendChild(card);
    });
  },

  enterEvent(eventId) {
    const events = window.GVStore.state.events;
    if (!events[eventId]) eventId = 'event-wedding';
    window.GVStore.setState({ activeEventId: eventId });
    this.updateWorkspaceHeader();
    window.GVLedgerTable.render();
    this.navTo('app');
  },

  updateWorkspaceHeader() {
    const event = window.GVStore.getActiveEvent();
    if (!event) return;

    const nameEl = document.getElementById('ws-event-header-name');
    if (nameEl) nameEl.innerText = event.title;

    const subEl = document.getElementById('ws-event-sub-meta');
    if (subEl) subEl.innerText = `📅 ${event.date} • 📍 ${event.venue} • 🏷️ ${event.type}`;

    const totalEl = document.getElementById('overview-total-amt');
    if (totalEl) totalEl.innerText = '₹' + (event.totalBlessings || 0).toLocaleString('en-IN');

    const envEl = document.getElementById('overview-envelopes-count');
    if (envEl) envEl.innerText = `${event.entries ? event.entries.length : 0} envelopes logged`;
  },

  createEvent(e) {
    e.preventDefault();
    const typeSelect = document.getElementById('new-event-type');
    let type = typeSelect ? typeSelect.value : 'Wedding';
    const title = document.getElementById('new-event-title').value.trim();
    const date = document.getElementById('new-event-date').value;
    const venue = document.getElementById('new-event-venue').value.trim();
    const guests = parseInt(document.getElementById('new-event-guests').value, 10) || 200;

    let role = 'Family';
    if (type === 'Wedding' || type === 'Reception') role = 'Bride & Groom';
    else if (type === 'Khatna') role = 'Boy';
    else if (type === 'HalfSaree') role = 'Girl';
    else if (type === 'Tonsure' || type === 'Birthday' || type === 'Naming') role = 'Boy / Girl';
    else if (type === 'Seemantham') role = 'Mother-to-be';
    else if (type === 'Jubilee') role = 'Elders';

    const customRoleEl = document.getElementById('new-event-role');
    const customTagEl = document.getElementById('new-event-custom-tag');
    if (type === 'Custom') {
      if (customRoleEl) role = customRoleEl.value;
      if (customTagEl && customTagEl.value.trim()) type = customTagEl.value.trim();
    }

    const newId = 'event-' + Date.now();
    const newEvent = {
      id: newId,
      title,
      type,
      role,
      date,
      venue,
      guestsCount: guests,
      totalBlessings: 0,
      totalExpenses: 0,
      goldGrams: 0,
      silverGrams: 0,
      envelopesCount: 0,
      entries: []
    };

    const allEvents = window.GVStore.state.events;
    allEvents[newId] = newEvent;

    window.GVRepository.save(allEvents);
    window.GVStore.setState({ events: allEvents, activeEventId: newId });

    document.getElementById('modal-create-event').classList.remove('active');
    this.enterEvent(newId);
    this.showToast(`✓ నూతన శుభకార్యం "${title}" విజయవంతంగా సృష్టించబడింది!`, 'gold');
  },

  deleteEvent(eventId, ev) {
    if (ev) ev.stopPropagation();
    const allEvents = window.GVStore.state.events;
    delete allEvents[eventId];
    window.GVRepository.save(allEvents);
    window.GVStore.setState({ events: allEvents });
    this.showToast('Celebration deleted from Vault', 'gold');
  },

  switchTab(tabId, btn) {
    document.querySelectorAll('.ws-tab-pane').forEach(el => el.style.display = 'none');
    const target = document.getElementById(tabId);
    if (target) target.style.display = 'block';

    document.querySelectorAll('.ws-tab-btn, .ws-tab-btn-lux').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
  }
};

// ============================================================================
// BACKWARD-COMPATIBLE RUNTIME BRIDGES (Ensures 100% Test & HTML Compatibility)
// ============================================================================
window.navToView = (v) => window.GVApp.navTo(v);
window.enterGuestDemoMode = () => {
  window.GVApp.navTo('hub');
  window.GVApp.showToast('✓ గెస్ట్ డెమో మోడ్ సక్రియం అయింది! (Guest Demo Active)', 'gold');
};
window.openHeroDemo = () => window.enterGuestDemoMode();
window.openEventWorkspace = (id) => window.GVApp.enterEvent(id);
window.enterWorkspaceEvent = (id) => window.GVApp.enterEvent(id);
window.switchWorkspaceTab = (tabId, btn) => window.GVApp.switchTab(tabId, btn);
window.openCreateEventModal = () => document.getElementById('modal-create-event').classList.add('active');
window.closeCreateEventModal = () => document.getElementById('modal-create-event').classList.remove('active');
window.handleCreateEventSubmit = (e) => window.GVApp.createEvent(e);
window.handleMunshiSubmit = (e) => window.GVMunshiDesk.submit(e);
window.selectEntryMode = (mode, btn) => window.GVMunshiDesk.selectMode(mode, btn);
window.addOneRupeeCoin = () => window.GVMunshiDesk.addOneRupeeCoin();
window.applyAuspiciousAmount = (val) => window.GVMunshiDesk.applyPresetAmount(val);
window.filterLedgerTable = () => window.GVLedgerTable.filter();
window.exportLedgerCSV = () => window.GVLedgerTable.exportCSV();
window.printLedgerSheet = () => window.print();
window.openEditEntryModal = (sno) => window.GVLedgerTable.openEdit(sno);
window.closeEditEntryModal = () => document.getElementById('modal-edit-entry').classList.remove('active');
window.handleEditEntrySubmit = (e) => window.GVLedgerTable.saveEdit(e);
window.deleteEntry = (sno) => window.GVLedgerTable.deleteEntry(sno);
window.openPrintSlip = (sno, name, city, mode, amt) => window.GVReceiptModal.open(sno, name, city, mode, amt);
window.closePrintSlipModal = () => window.GVReceiptModal.close();
window.openPricingModal = () => document.getElementById('modal-pricing-plans').classList.add('active');
window.closePricingModal = () => document.getElementById('modal-pricing-plans').classList.remove('active');
window.switchLoginTab = (tabId) => {
  document.querySelectorAll('.login-tab-content').forEach(el => el.style.display = 'none');
  document.querySelectorAll('.login-tab-nav-btn').forEach(btn => btn.classList.remove('active'));
  const target = document.getElementById('login-pane-' + tabId);
  const btn = document.getElementById('tab-btn-' + tabId);
  if (target) target.style.display = 'block';
  if (btn) btn.classList.add('active');
};

window.handleSendMobileOTP = (e) => {
  if (e) e.preventDefault();
  const phone = document.getElementById('login-mobile-input').value;
  if (!phone || phone.length < 10) {
    window.GVApp.showToast('⚠️ దయచేసి సరైన 10-అంకెల మొబైల్ నెంబర్ నమోదు చేయండి', 'ruby');
    return;
  }
  document.getElementById('mobile-step-phone').style.display = 'none';
  document.getElementById('mobile-step-otp').style.display = 'block'; startOtpCountdown();
  window.GVApp.showToast(`📩 OTP కోడ్ ${phone} కి పంపబడింది (OTP: 123456)`, 'emerald');
};

window.handleVerifyOTP = (e) => {
  if (e) e.preventDefault();
  const phone = document.getElementById('login-mobile-input').value || '9876543210';
  localStorage.setItem('GV_AUTH_SESSION', JSON.stringify({ name: 'Sri Krishna Family', phone: '+91 ' + phone, initials: 'SK', provider: 'Mobile OTP' }));
  window.GVApp.checkAuthSession();
  window.GVApp.showToast('✓ OTP ధృవీకరించబడింది! వాలెట్ ఓపెన్ అవుతోంది...', 'emerald');
  setTimeout(() => {
    window.GVApp.navTo('hub');
  }, 400);
};

window.handleGoogleSignIn = () => {
  window.GVApp.showToast('🌐 Google ద్వారా ధృవీకరించబడింది (srikrishna.family@gmail.com)', 'emerald');
  setTimeout(() => {
    window.GVApp.navTo('hub');
  }, 400);
};

window.updateLiveCalculator = () => window.GVEstimator.update();
window.showToast = (msg, type) => window.GVApp.showToast(msg, type);

window.setAppViewport = (mode) => {
  const body = document.body;
  const btnDesktop = document.getElementById('btn-view-desktop');
  const btnMobile = document.getElementById('btn-view-mobile');

  if (mode === 'mobile') {
    body.classList.add('mobile-viewport-active');
    if (btnDesktop) btnDesktop.classList.remove('active');
    if (btnMobile) btnMobile.classList.add('active');
    window.GVApp.showToast('📱 Mobile Responsive View Enabled (390px Mandapam Flow)', 'gold');
  } else {
    body.classList.remove('mobile-viewport-active');
    if (btnDesktop) btnDesktop.classList.add('active');
    if (btnMobile) btnMobile.classList.remove('active');
    window.GVApp.showToast('🖥️ Desktop Full-Width View Active', 'gold');
  }
};

window.handleLanguageChange = (lang) => {
  window.GVI18n.apply(lang);
  window.GVApp.showToast(`🌐 Language set to ${lang.toUpperCase()}`, 'gold');
};

window.startVoiceDictation = () => {
  if (window.GVMunshiDesk && window.GVMunshiDesk.startVoiceDictation) {
    window.GVMunshiDesk.startVoiceDictation();
  } else {
    window.GVApp.showToast('🎙️ మైక్ ఆక్టివేట్ అయింది. అతిథి పేరు మాట్లాడండి...', 'gold');
  }
};

window.handleLoginSubmit = () => {
  const phone = document.getElementById('login-phone') ? document.getElementById('login-phone').value : '9876543210';
  localStorage.setItem('GV_AUTH_SESSION', JSON.stringify({ name: 'Sri Krishna Family', phone: '+91 ' + phone, initials: 'SK', provider: 'Mobile OTP' }));
  if (window.GVApp) {
    window.GVApp.checkAuthSession();
    window.GVApp.showToast('✓ Welcome to Family Vault! Accessing ledgers...', 'emerald');
    window.GVApp.navTo('hub');
  }
};

window.switchAuthTab = (tab) => {
  const signinForm = document.getElementById('auth-pane-signin');
  const signupForm = document.getElementById('auth-pane-signup');
  const btnIn = document.getElementById('tab-btn-signin');
  const btnUp = document.getElementById('tab-btn-signup');
  if (tab === 'signin') {
    if (signinForm) signinForm.style.display = 'block';
    if (signupForm) signupForm.style.display = 'none';
    if (btnIn) { btnIn.classList.add('active'); btnIn.style.background = '#37000A'; btnIn.style.color = '#FFFFFF'; }
    if (btnUp) { btnUp.classList.remove('active'); btnUp.style.background = 'transparent'; btnUp.style.color = '#37000A'; }
  } else {
    if (signinForm) signinForm.style.display = 'none';
    if (signupForm) signupForm.style.display = 'block';
    if (btnIn) { btnIn.classList.remove('active'); btnIn.style.background = 'transparent'; btnIn.style.color = '#37000A'; }
    if (btnUp) { btnUp.classList.add('active'); btnUp.style.background = '#37000A'; btnUp.style.color = '#FFFFFF'; }
  }
};

window.handleSignUpSubmit = () => {
  const name = document.getElementById('signup-name') ? document.getElementById('signup-name').value : 'New Family';
  const phone = document.getElementById('signup-phone') ? document.getElementById('signup-phone').value : '9876543210';
  localStorage.setItem('GV_AUTH_SESSION', JSON.stringify({ name: name, phone: '+91 ' + phone, initials: name.substring(0, 2).toUpperCase(), provider: 'Family Registration' }));
  if (window.GVApp) {
    window.GVApp.checkAuthSession();
    window.GVApp.showToast(`✓ Family Vault created for ${name}!`, 'emerald');
    window.GVApp.navTo('hub');
  }
};

// Global Events Database accessor (Backward-compatibility)
Object.defineProperty(window, 'EVENTS_DATABASE', {
  get() { return window.GVStore.state.events; },
  set(val) { window.GVStore.setState({ events: val }); }
});

// Bootstrap on DOM Ready
window.addEventListener('DOMContentLoaded', () => {
  window.GVApp.init();
});


window.toggleGoogleAccountChooser = () => {
  const chooser = document.getElementById('google-account-chooser');
  if (chooser) {
    chooser.style.display = chooser.style.display === 'none' ? 'block' : 'none';
  }
};

window.selectGoogleAccount = (name, email, initials) => {
  localStorage.setItem('GV_AUTH_SESSION', JSON.stringify({ name, email, initials, provider: 'Google' }));
  window.GVApp.checkAuthSession();
  window.GVApp.showToast(`🌐 Google Verified: ${name} (${email})`, 'emerald');
  setTimeout(() => {
    window.GVApp.navTo('hub');
  }, 450);
};

window.handleOtpInput = (el, idx) => {
  if (el.value.length === 1 && idx < 6) {
    const next = document.getElementById('otp-' + (idx + 1));
    if (next) next.focus();
  }
};

window.handleOtpKeyDown = (e, idx) => {
  if (e.key === 'Backspace' && !e.target.value && idx > 1) {
    const prev = document.getElementById('otp-' + (idx - 1));
    if (prev) prev.focus();
  }
};

window.handleEventTypeChange = (val) => {
  const customBox = document.getElementById('custom-event-extra-fields');
  if (customBox) {
    customBox.style.display = val === 'Custom' ? 'block' : 'none';
  }
};

let otpTimerInterval = null;
function startOtpCountdown() {
  let count = 28;
  const countEl = document.getElementById('otp-countdown-val');
  if (otpTimerInterval) clearInterval(otpTimerInterval);
  otpTimerInterval = setInterval(() => {
    count--;
    if (countEl) countEl.innerText = count;
    if (count <= 0) clearInterval(otpTimerInterval);
  }, 1000);
}
