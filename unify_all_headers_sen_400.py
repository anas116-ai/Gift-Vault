import re
from bs4 import BeautifulSoup

def clean_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Ensure Google Font Sen is in head
    head = soup.find('head')
    if head and not soup.find('link', href=re.compile(r'family=Sen')):
        sen_link = soup.new_tag('link', rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Sen:wght@400;500;600;700;800&display=swap')
        head.append(sen_link)

    # Clean all h1, h2, h3, h4 tags
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        style = tag.get('style', '')
        # Remove any font-family and font-weight from inline style
        style = re.sub(r'font-family\s*:\s*[^;]+;?', '', style)
        style = re.sub(r'font-weight\s*:\s*[^;]+;?', '', style)
        style = style.strip()
        # Add Sen Regular 400
        new_style = f"font-family: 'Sen', sans-serif !important; font-weight: 400 !important; letter-spacing: -0.01em; {style}".strip()
        tag['style'] = new_style

    # Clean nav-brand-title
    for brand in soup.find_all(class_='nav-brand-title'):
        b_style = brand.get('style', '')
        b_style = re.sub(r'font-family\s*:\s*[^;]+;?', '', b_style)
        b_style = re.sub(r'font-weight\s*:\s*[^;]+;?', '', b_style)
        brand['style'] = f"font-family: 'Sen', sans-serif !important; font-weight: 400 !important; font-size: 22px; color: #37000A; letter-spacing: -0.01em; {b_style}".strip()

    # Clean login headlines
    for lh in soup.find_all(class_=['login-left-headline', 'login-right-heading']):
        lh_style = lh.get('style', '')
        lh_style = re.sub(r'font-family\s*:\s*[^;]+;?', '', lh_style)
        lh_style = re.sub(r'font-weight\s*:\s*[^;]+;?', '', lh_style)
        lh['style'] = f"font-family: 'Sen', sans-serif !important; font-weight: 400 !important; {lh_style}".strip()

    with open(path, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"Cleaned headers in {path} to Sen Regular 400")

for p in ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']:
    clean_file(p)
