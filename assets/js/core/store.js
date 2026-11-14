/**
 * GiftVault State Management Store
 * Reactive Pub/Sub Architecture with Immutable Update Cycles
 */

class GiftVaultStore {
  constructor() {
    this.listeners = [];
    this.state = {
      events: {},
      activeEventId: 'event-wedding',
      currentLang: 'te',
      selectedMode: 'Cash',
      isSoundboxMuted: false,
      searchQuery: '',
      activeView: 'landing'
    };
  }

  subscribe(listener) {
    this.listeners.push(listener);
    return () => {
      this.listeners = this.listeners.filter(l => l !== listener);
    };
  }

  notify(event, payload) {
    this.listeners.forEach(listener => {
      try {
        listener(this.state, event, payload);
      } catch (err) {
        console.error('Store listener error:', err);
      }
    });
  }

  setState(partialState, actionName = 'UPDATE') {
    this.state = { ...this.state, ...partialState };
    this.notify(actionName, partialState);
  }

  getActiveEvent() {
    return this.state.events[this.state.activeEventId] || null;
  }
}

window.GVStore = new GiftVaultStore();

// Global Security & Craft Utilities
window.GVUtils = {
  escapeHtml(str) {
    if (str === null || str === undefined) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }
};
