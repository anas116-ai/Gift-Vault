/**
 * ThreeUI Etale 52 Mechanical Rolling Number Plates
 * Precision spring physics digit roll controller
 */

window.GVEstimator = {
  update() {
    const slider = document.getElementById('calc-guest-slider');
    const select = document.getElementById('calc-tier-select');
    if (!slider || !select) return;

    const guests = parseInt(slider.value, 10);
    const avg = parseInt(select.value, 10);
    const total = guests * avg;

    const guestDisp = document.getElementById('calc-guests-disp');
    if (guestDisp) guestDisp.innerText = guests.toLocaleString('en-IN');

    const totalEl = document.getElementById('calc-total-shagun');
    if (totalEl) totalEl.innerText = '₹' + total.toLocaleString('en-IN');

    const totalStr = total.toString().padStart(8, '0');
    for (let i = 0; i < 8; i++) {
      const ribbon = document.getElementById(`ribbon-${i}`);
      if (ribbon) {
        const digit = parseInt(totalStr[i], 10);
        ribbon.style.transform = `translateY(-${digit * 38}px)`;
      }
    }
  }
};
