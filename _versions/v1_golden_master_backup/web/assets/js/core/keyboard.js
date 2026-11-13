/**
 * GiftVault Mandapam Rapid-Fire Keyboard Shortcuts
 * Senior Staff Engineer Standard: Zero mouse dependency for Munshi desks
 */

window.GVKeyboard = {
  init() {
    window.addEventListener('keydown', (e) => {
      // Ignore if user is currently typing inside an input/textarea/select
      const activeTag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      const isInput = activeTag === 'input' || activeTag === 'textarea' || activeTag === 'select';

      // 1. ESC: Close all active modals
      if (e.key === 'Escape') {
        document.querySelectorAll('.modal-backdrop, .modal-backdrop-lux').forEach(m => m.classList.remove('active'));
        return;
      }

      // 2. Hotkey 'N' (New Entry Desk)
      if (!isInput && (e.key === 'n' || e.key === 'N')) {
        e.preventDefault();
        const tabBtn = document.querySelector("button.ws-tab-btn[onclick*=\"'tab-entry'\"]");
        if (tabBtn) {
          tabBtn.click();
          const nameInput = document.getElementById('entry-name');
          if (nameInput) nameInput.focus();
        }
        return;
      }

      // 3. Hotkey '/' (Ledger Search)
      if (!isInput && e.key === '/') {
        e.preventDefault();
        const tabBtn = document.querySelector("button.ws-tab-btn[onclick*=\"'tab-ledger'\"]");
        if (tabBtn) {
          tabBtn.click();
          const searchInput = document.getElementById('ledger-search-input');
          if (searchInput) {
            setTimeout(() => searchInput.focus(), 50);
          }
        }
        return;
      }
    });

    // Special listener inside Amount Input for instant +1 Lucky Coin
    const amtInput = document.getElementById('entry-amount');
    if (amtInput) {
      amtInput.addEventListener('keydown', (e) => {
        if (e.key === '+' || e.key === '=') {
          e.preventDefault();
          if (typeof window.addOneRupeeCoin === 'function') {
            window.addOneRupeeCoin();
          }
        }
      });
    }
  }
};
