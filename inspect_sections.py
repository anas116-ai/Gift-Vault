import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Hero grid:", bool(re.search(r'<div class="hero-showcase-container', text)))
print("Cards under hero:", bool(re.search(r'hero-four-cards-strip|features-collection-grid', text)))
print("Built for families:", bool(re.search(r'hero-ref1-family-section', text)))
print("Culture section:", bool(re.search(r'id="culture"', text)))
print("Pricing section:", bool(re.search(r'id="pricing"', text)))
print("Login view:", bool(re.search(r'id="view-login"', text)))
