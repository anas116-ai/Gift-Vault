with open('index.html', encoding='utf-8') as f:
    c = f.read()

# 1. Check nav user badge and sign in button
s1 = c.find('nav-user-badge')
print('=== Nav user badge & Sign in ===')
print(c[s1-100:s1+400])

# 2. Check hero buttons
s2 = c.find('hero-cta-btn')
print('=== Hero buttons ===')
print(c[s2-100:s2+600])

# 3. Check pricing card buttons
s3 = c.find('pricing-card')
print('=== Pricing card ===')
print(c[s3:s3+800])

# 4. Check login button & back button in view-login
s4 = c.find('id="view-login"')
print('=== View login top & buttons ===')
print(c[s4:s4+1200])
