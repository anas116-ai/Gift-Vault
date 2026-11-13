/**
 * GiftVault Authentic 2-Inch Thermal Slip Modal
 * Traditional "శ్రీరస్తు - శుభమస్తు" layout with thermal printer formatting
 */

window.GVReceiptModal = {
  open(sno, name, city, mode, amt) {
    document.getElementById('slip-sno').innerText = sno;
    document.getElementById('slip-guest-name').innerText = name;
    document.getElementById('slip-guest-city').innerText = city;
    document.getElementById('slip-mode').innerText = mode;
    document.getElementById('slip-amount').innerText = amt;

    const timeEl = document.getElementById('slip-timestamp');
    if (timeEl) {
      const now = new Date();
      timeEl.innerText = now.toLocaleDateString('en-IN') + ' ' + now.toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' });
    }

    document.getElementById('modal-print-slip').classList.add('active');
  },

  close() {
    document.getElementById('modal-print-slip').classList.remove('active');
  },

  print() {
    window.print();
  }
};
