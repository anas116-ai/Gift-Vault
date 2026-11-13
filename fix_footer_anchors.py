for path in ['web_preview/index.html', 'web_preview/desktop.html', 'web_preview/mobile.html', 'build/web/index.html', 'web/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    code = code.replace('<a href="#" class="footer-link" onclick="navToView(\'app\'); openAppTab(\'desk\'); return false;">Desk Mode</a>', '<button type="button" class="footer-link" style="background:none;border:none;padding:0;cursor:pointer;font-family:inherit;" onclick="navToView(\'app\'); openAppTab(\'desk\');">Desk Mode</button>')
    code = code.replace('<a href="#" class="footer-link" onclick="navToView(\'app\'); openAppTab(\'ledger\'); return false;">Digital Red Book</a>', '<button type="button" class="footer-link" style="background:none;border:none;padding:0;cursor:pointer;font-family:inherit;" onclick="navToView(\'app\'); openAppTab(\'ledger\');">Digital Red Book</button>')
    code = code.replace('<a href="#" class="footer-link" onclick="navToView(\'app\'); openAppTab(\'expenses\'); return false;">Expense Audit</a>', '<button type="button" class="footer-link" style="background:none;border:none;padding:0;cursor:pointer;font-family:inherit;" onclick="navToView(\'app\'); openAppTab(\'expenses\');">Expense Audit</button>')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code)
print('Fixed dead anchors to semantic buttons.')
