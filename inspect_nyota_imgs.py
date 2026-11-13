import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.Request('https://thenyota.app/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=10) as resp:
    soup = BeautifulSoup(resp.read().decode('utf-8'), 'html.parser')

for img in soup.find_all('img'):
    print('IMG:', img.get('src'), 'ALT:', img.get('alt'))
