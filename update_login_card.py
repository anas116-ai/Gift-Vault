import os

files = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for fn in files:
    if not os.path.exists(fn):
        continue
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()

    # Update subtitle to Title Case
    c = c.replace('<div class="brand-subtitle">THE SACRED LEDGER</div>', '<div class="brand-subtitle">The Sacred Ledger</div>')

    # Update phone input placeholder
    c = c.replace('placeholder="Mobile Number" value="9876543210"', 'placeholder="Mobile Number" value=""')

    # Clean OTP boxes
    c = c.replace('<input type="text" id="otp-1" class="otp-box" value="1"', '<input type="text" id="otp-1" class="otp-box" value="" placeholder="|"')
    for num in range(2, 7):
        c = c.replace(f'<input type="text" id="otp-{num}" class="otp-box" value="{num}"', f'<input type="text" id="otp-{num}" class="otp-box" value=""')

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Updated: {fn}')

print('All index.html files updated successfully.')
