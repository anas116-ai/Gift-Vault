/**
 * GiftVault Munshi Fast Entry Desk
 * Speed-optimized blessing logging with harmonic temple chime & auto-coin
 */

window.GVMunshiDesk = {
  selectMode(mode, btn) {
    window.GVStore.setState({ selectedMode: mode });
    document.querySelectorAll('.mode-select-btn').forEach(b => {
      b.classList.remove('active');
      b.style.borderColor = 'var(--border-subtle)';
      b.style.color = 'var(--text-secondary)';
    });
    if (btn) {
      btn.classList.add('active');
      btn.style.borderColor = 'var(--c-gold)';
      btn.style.color = 'var(--c-gold)';
    }
  },

  addOneRupeeCoin() {
    const field = document.getElementById('entry-amount');
    if (!field) return;
    const current = parseInt(field.value, 10) || 0;
    field.value = current + 1;
    window.GVApp.showToast('🪙 +₹1 Auspicious Coin Added', 'gold');
  },

  applyPresetAmount(val) {
    const field = document.getElementById('entry-amount');
    if (field) field.value = val;
  },

  playTempleChime() {
    if (window.GVStore.state.isSoundboxMuted) return;
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const now = ctx.currentTime;

      // Harmonic D5 + A5 Chime
      const osc1 = ctx.createOscillator();
      const gain1 = ctx.createGain();
      osc1.frequency.setValueAtTime(587.33, now); // D5
      gain1.gain.setValueAtTime(0.3, now);
      gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.8);
      osc1.connect(gain1);
      gain1.connect(ctx.destination);
      osc1.start(now);
      osc1.stop(now + 0.8);

      const osc2 = ctx.createOscillator();
      const gain2 = ctx.createGain();
      osc2.frequency.setValueAtTime(880.00, now + 0.08); // A5
      gain2.gain.setValueAtTime(0.2, now + 0.08);
      gain2.gain.exponentialRampToValueAtTime(0.001, now + 0.9);
      osc2.connect(gain2);
      gain2.connect(ctx.destination);
      osc2.start(now + 0.08);
      osc2.stop(now + 0.9);
    } catch (e) {
      // AudioContext blocked by browser policy until gesture
    }
  },

  submit(e) {
    e.preventDefault();
    const event = window.GVStore.getActiveEvent();
    if (!event) return;

    const name = document.getElementById('entry-name').value.trim();
    const city = document.getElementById('entry-city').value.trim() || 'Chirala';
    const rel = document.getElementById('entry-relation').value;
    const amt = parseInt(document.getElementById('entry-amount').value, 10) || 0;
    const phone = document.getElementById('entry-phone').value.trim();
    const mode = window.GVStore.state.selectedMode || 'Cash';

    const nextNum = (event.entries ? event.entries.length : 0) + 1;
    const sno = `#GV-${100 + nextNum}`;

    const newEntry = {
      sno,
      name,
      place: city,
      relation: rel,
      mode,
      amount: amt,
      phone,
      recorder: 'Suresh (Desk 1)'
    };

    if (!event.entries) event.entries = [];
    event.entries.push(newEntry);
    event.totalBlessings = (event.totalBlessings || 0) + amt;
    event.envelopesCount = event.entries.length;

    const allEvents = window.GVStore.state.events;
    allEvents[event.id] = event;

    window.GVRepository.save(allEvents);
    window.GVStore.setState({ events: allEvents }, 'ENTRY_ADDED');

    // Reset Form
    document.getElementById('entry-name').value = '';
    document.getElementById('entry-amount').value = '';
    document.getElementById('entry-name').focus();

    // Sound and Toast
    this.playTempleChime();
    window.GVApp.showToast(`✓ ${name} గారి చదివింపు (${sno} - ₹${amt.toLocaleString('en-IN')}) నమోదైంది!`, 'gold');
  }
};
