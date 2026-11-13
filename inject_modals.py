modals_html = '''
  <!-- ==========================================================================
       2-INCH THERMAL RECEIPT SLIP MODAL (58MM PRINTER SIMULATION)
       ========================================================================== -->
  <div id="modal-print-slip" class="modal-backdrop">
    <div class="modal-dialog" style="max-width: 400px;">
      <div class="modal-header">
        <div>
          <div class="showcase-tag-sub">58MM THERMAL RECEIPT PREVIEW</div>
          <h3 style="font-family: var(--font-serif); font-size: 20px; color: var(--c-night);">2-inch Reception Slip</h3>
        </div>
        <button type="button" class="modal-close-btn" onclick="closePrintSlipModal()">✕</button>
      </div>
      <div class="modal-body">
        <div style="background: #FFFFFF; border: 2px dashed #CBD5E1; padding: 20px; font-family: monospace; color: #000411; border-radius: 8px;">
          <div style="text-align: center; border-bottom: 1px dashed #64748B; padding-bottom: 10px; margin-bottom: 12px;">
            <div style="font-weight: 800; font-size: 16px; letter-spacing: 0.05em;">GIFTVAULT • గిఫ్ట్ వాలెట్</div>
            <div style="font-size: 11px; color: #475569;">ROYAL RECEPTION DESK • DIGITAL RECEIPT</div>
            <div style="font-size: 12px; font-weight: 700; margin-top: 4px; color: var(--c-crimson);">॥ శ్రీరస్తు • శుభమస్తు • అవిఘ్నమస్తు ॥</div>
          </div>
          <div style="font-size: 12.5px; line-height: 1.8;">
            <div style="display: flex; justify-content: space-between;"><span>Slip Serial No:</span> <strong id="slip-sno">#GV-101</strong></div>
            <div style="display: flex; justify-content: space-between;"><span>Guest Name:</span> <strong id="slip-guest-name">K. Venkata Rao Garu</strong></div>
            <div style="display: flex; justify-content: space-between;"><span>Native Place:</span> <strong id="slip-guest-city">Vijayawada</strong></div>
            <div style="display: flex; justify-content: space-between;"><span>Mode:</span> <strong id="slip-mode">UPI PhonePe</strong></div>
            <div style="display: flex; justify-content: space-between; font-size: 16px; margin: 10px 0; padding: 8px 0; border-top: 1px dashed #64748B; border-bottom: 1px dashed #64748B;">
              <span style="font-weight: 800;">CHADIVIMPU AMOUNT:</span> <strong id="slip-amount" style="color: #036D19;">₹10,116</strong>
            </div>
            <div style="text-align: center; font-size: 11px; color: #475569; margin-top: 10px;">
              🙏 Gratefully received with warm blessings.<br>
              Real-time logged in GiftVault Family Treasury.<br>
              Instant WhatsApp copy dispatched to mobile.
            </div>
          </div>
        </div>
        <div style="margin-top: 18px; display: flex; gap: 10px;">
          <button type="button" class="btn-emerald" style="flex: 1; justify-content: center; padding: 12px;" onclick="window.print()">
            <span>🖨️</span> <span>Print Thermal Slip</span>
          </button>
          <button type="button" class="btn-outline-dark" style="padding: 12px 20px;" onclick="closePrintSlipModal()">
            Done
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       ANTI-CREDENTIAL SHARING AUSPICIOUS PRICING MODAL (PER-EVENT PASS)
       ========================================================================== -->
  <div id="modal-pricing-plans" class="modal-backdrop">
    <div class="modal-dialog" style="max-width: 680px;">
      <div class="modal-header">
        <div>
          <div class="showcase-tag-sub">PREVENT ABUSE • FAIR SHARING MODEL</div>
          <h3 style="font-family: var(--font-serif); font-size: 24px; color: var(--c-night);">Celebration Access Plans</h3>
        </div>
        <button type="button" class="modal-close-btn" onclick="closePricingModal()">✕</button>
      </div>
      <div class="modal-body">
        <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 20px; line-height: 1.6;">
          <strong>Why Per-Event Licensing?</strong> To protect family privacy and avoid subscription sharing between unrelated parties, GiftVault licenses access per sacred event (Bride/Groom or Child's Milestone) rather than a shared loose login. Each celebration gets its own dedicated, cryptographically sealed ledger.
        </p>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 20px;">
          <!-- Plan 1: Single Auspicious Event Pass -->
          <div style="border: 2px solid var(--c-crimson); border-radius: 12px; padding: 20px; background: #FFFFFF; position: relative;">
            <div style="position: absolute; top: -11px; right: 14px; background: var(--c-crimson); color: #FFFFFF; font-size: 10px; font-weight: 800; padding: 3px 8px; border-radius: 9999px;">
              MOST POPULAR
            </div>
            <div style="font-size: 12px; font-weight: 800; color: var(--c-crimson); text-transform: uppercase;">ఏక శుభకార్య పాస్ (Single Event)</div>
            <div style="font-family: var(--font-serif); font-size: 32px; font-weight: 800; color: var(--c-night); margin: 6px 0;">₹49 <span style="font-size: 13px; font-family: var(--font-sans); color: var(--c-muted); font-weight: normal;">/ celebration</span></div>
            <p style="font-size: 12.5px; color: #475569; margin-bottom: 14px;">Perfect for weddings, tonsures, or housewarmings. Unlocks 1 dedicated celebration forever.</p>
            <ul style="font-size: 12px; line-height: 1.8; color: var(--c-night); padding-left: 18px; margin-bottom: 16px;">
              <li>🔒 Bound to 1 Milestone Event & Venue</li>
              <li>⚡ Up to 4 Munshi Desks in Sync</li>
              <li>📲 Unlimited WhatsApp Receipts</li>
              <li>🖨️ 2-inch Thermal Print & CSV Export</li>
              <li>🛡️ Device-Token Protected (No password leakage)</li>
            </ul>
            <button type="button" class="btn-crimson" style="width: 100%; justify-content: center;" onclick="alert('Auspicious ₹49 Event Pass activated for active celebration!'); closePricingModal();">
              Activate ₹49 Pass
            </button>
          </div>

          <!-- Plan 2: Royal Family Annual Milestone Pass -->
          <div style="border: 1.5px solid var(--c-border); border-radius: 12px; padding: 20px; background: #FAF9F6;">
            <div style="font-size: 12px; font-weight: 800; color: var(--c-emerald); text-transform: uppercase;">రాజ కుటుంబ పాస్ (Family Trio)</div>
            <div style="font-family: var(--font-serif); font-size: 32px; font-weight: 800; color: var(--c-night); margin: 6px 0;">₹99 <span style="font-size: 13px; font-family: var(--font-sans); color: var(--c-muted); font-weight: normal;">/ 3 celebrations</span></div>
            <p style="font-size: 12.5px; color: #475569; margin-bottom: 14px;">Ideal for families celebrating multiple events (e.g. Engagement + Kalyanam + Housewarming).</p>
            <ul style="font-size: 12px; line-height: 1.8; color: var(--c-night); padding-left: 18px; margin-bottom: 16px;">
              <li>🎪 Up to 3 Auspicious Milestones</li>
              <li>🔄 Reciprocity Comparison across all 3 events</li>
              <li>🎙️ Voice AI Munshi Dictation</li>
              <li>☁️ Automated Drive / Cloud Backup</li>
              <li>👥 Family Hub Synchronization</li>
            </ul>
            <button type="button" class="btn-emerald" style="width: 100%; justify-content: center;" onclick="alert('Royal Family ₹99 Pass activated! 3 Event slots available.'); closePricingModal();">
              Get Family Pass (₹99)
            </button>
          </div>
        </div>

        <div style="background: var(--c-base); padding: 12px 16px; border-radius: 8px; border: 1px solid var(--c-border); font-size: 12px; color: #475569; display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 18px;">💡</span>
          <span><strong>Family Sync Security:</strong> Extended relatives join using a temporary 6-digit session OTP (e.g. <code>842911</code>), keeping your master account credential secure.</span>
        </div>
      </div>
    </div>
  </div>
'''

files = ['web_preview/index.html', 'web_preview/desktop.html', 'web_preview/mobile.html', 'build/web/index.html', 'web/index.html']

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()

    # If modal-print-slip already in file, skip
    if 'id="modal-print-slip"' in content:
        print(f'{p}: already has modal-print-slip')
        continue

    # Insert before <footer class="main-footer">
    target = '  <!-- Main Footer -->'
    if target in content:
        content = content.replace(target, modals_html + '\n' + target)
        print(f'{p}: inserted modals before Main Footer')
    else:
        # Fallback target
        target = '<footer class="main-footer">'
        content = content.replace(target, modals_html + '\n' + target)
        print(f'{p}: inserted modals before footer tag')

    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)

print('Modals injected into all target files.')
