with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="view-login"')
end_idx = c.find('</main>', idx)
print(c[idx:end_idx+7])
