import re

target_files = [
    r'c:\Project\Gift Valut\web_preview\index.html',
    r'c:\Project\Gift Valut\web_preview\desktop.html',
    r'c:\Project\Gift Valut\web_preview\mobile.html',
    r'c:\Project\Gift Valut\build\web\index.html',
    r'c:\Project\Gift Valut\web\index.html'
]

with open(target_files[0], 'r', encoding='utf-8') as f:
    html = f.read()

# Add escapeHtml right after <script>
escape_code = '''<script>
    // ==========================================
    // 0. CYBERSECURITY & XSS SANITIZATION SUITE
    // ==========================================
    function escapeHtml(str) {
      if (str === null || str === undefined) return '';
      return String(str).replace(/[&<>"']/g, function(char) {
        switch (char) {
          case '&': return '&amp;';
          case '<': return '&lt;';
          case '>': return '&gt;';
          case '"': return '&quot;';
          case "'": return '&#39;';
          default: return char;
        }
      });
    }

    function sanitizeAlphanumeric(str) {
      return escapeHtml(str).trim();
    }
'''

if 'function escapeHtml' not in html:
    html = html.replace('<script>', escape_code, 1)

# Now check row rendering sanitization
old_tr_full = '''    const row = document.createElement('tr');
    row.innerHTML = `
      <td><span class="serial-num">${item.sno}</span></td>
      <td><strong>${item.name}</strong><br><small style="color:var(--c-muted);">${item.relation || 'బంధువు / Relative'}</small></td>
      <td>${item.place}</td>
      <td><span class="mode-badge ${badgeClass}">${item.mode}</span></td>
      <td class="num-currency" style="font-weight:700; color:var(--c-night);">${amtDisplay}</td>
      <td><span style="font-size:11px; color:var(--c-muted); background:var(--c-base); padding:3px 6px; border-radius:4px; border:1px solid var(--c-border);">${item.recorder || 'Suresh (Desk 1)'}</span></td>
      <td>${photoHtml}</td>
      <td style="white-space:nowrap;">
        <button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${item.name}', '${amtDisplay}', '${item.phone || ''}', '${item.place}')">
          📲 WhatsApp
        </button>
        <button type="button" class="btn-outline-dark" style="padding:4px 8px; font-size:11px; margin-left:4px;" onclick="openPrintSlip('${item.sno}', '${item.name}', '${item.place}', '${item.mode}', '${amtDisplay}')">
          🖨️ Slip
        </button>
      </td>
    `;'''

new_tr_full = '''    const safeName = escapeHtml(item.name);
    const safeRelation = escapeHtml(item.relation || 'బంధువు / Relative');
    const safePlace = escapeHtml(item.place);
    const safeSno = escapeHtml(item.sno);
    const safeRecorder = escapeHtml(item.recorder || 'Suresh (Desk 1)');
    const safeAmt = escapeHtml(amtDisplay);
    const safePhone = escapeHtml(item.phone || '');

    const row = document.createElement('tr');
    row.innerHTML = `
      <td><span class="serial-num">${safeSno}</span></td>
      <td><strong>${safeName}</strong><br><small style="color:var(--c-muted);">${safeRelation}</small></td>
      <td>${safePlace}</td>
      <td><span class="mode-badge ${badgeClass}">${escapeHtml(item.mode)}</span></td>
      <td class="num-currency" style="font-weight:700; color:var(--c-night);">${safeAmt}</td>
      <td><span style="font-size:11px; color:var(--c-muted); background:var(--c-base); padding:3px 6px; border-radius:4px; border:1px solid var(--c-border);">${safeRecorder}</span></td>
      <td>${photoHtml}</td>
      <td style="white-space:nowrap;">
        <button type="button" class="btn-whatsapp-sm" onclick="sendWhatsAppReceipt('${safeName.replace(/'/g, "\\\\'")}', '${safeAmt}', '${safePhone}', '${safePlace.replace(/'/g, "\\\\'")}')">
          📲 WhatsApp
        </button>
        <button type="button" class="btn-outline-dark" style="padding:4px 8px; font-size:11px; margin-left:4px;" onclick="openPrintSlip('${safeSno}', '${safeName.replace(/'/g, "\\\\'")}', '${safePlace.replace(/'/g, "\\\\'")}', '${escapeHtml(item.mode)}', '${safeAmt}')">
          🖨️ Slip
        </button>
      </td>
    `;'''

if old_tr_full in html:
    html = html.replace(old_tr_full, new_tr_full)

for path in target_files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated: {path} ({len(html)} bytes)")

print("\nSuccessfully integrated escapeHtml across all files!")
