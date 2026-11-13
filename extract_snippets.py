with open('web_preview/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's locate view-landing content
start_landing = text.find('id="view-landing"')
start_login = text.find('id="view-login"')
start_app = text.find('id="view-app"')

print('Landing section starts at:', start_landing, 'Login at:', start_login, 'App at:', start_app)

with open('landing_snippet.html', 'w', encoding='utf-8') as out:
    out.write(text[start_landing:start_login])

with open('login_snippet.html', 'w', encoding='utf-8') as out:
    out.write(text[start_login:start_app])

print('Saved snippets.')
