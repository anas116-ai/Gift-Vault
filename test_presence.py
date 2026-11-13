with open('web_preview/index.html', encoding='utf-8') as f:
    text = f.read()

print('modal-edit-entry:', 'modal-edit-entry' in text)
print('toast-container:', 'toast-container' in text)
print('showToast:', 'showToast' in text)
print('print-only:', 'print-only' in text)
