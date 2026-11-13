import urllib.request

candidate_urls = {
    # Indian Wedding candidates:
    "wedding_1": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=1200&q=85", # Indian bride hands mehendi / wedding ceremony
    "wedding_2": "https://images.unsplash.com/photo-1583939003579-730e3918a45a?auto=format&fit=crop&w=1200&q=85", # Indian bride groom couple traditional attire
    "wedding_3": "https://images.unsplash.com/photo-1532712938310-34cb3982ef74?auto=format&fit=crop&w=1200&q=85", # Indian wedding rituals
    "wedding_4": "https://images.unsplash.com/photo-1604017011826-d3b4c23f8914?auto=format&fit=crop&w=1200&q=85", # Traditional wedding setup
    "wedding_5": "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=1200&q=85", # Celebration couple

    # Birthday & Barasala candidates:
    "birthday_1": "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=1200&q=85", # baby portrait joyful
    "birthday_2": "https://images.unsplash.com/photo-1519689680058-324335c77eba?auto=format&fit=crop&w=1200&q=85", # baby celebration cradle
    "birthday_3": "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?auto=format&fit=crop&w=1200&q=85", # cute baby smile
    "birthday_4": "https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?auto=format&fit=crop&w=1200&q=85", # family with baby
    "birthday_5": "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?auto=format&fit=crop&w=1200&q=85", # joyful child celebration

    # Griha Pravesh / Housewarming candidates:
    "house_1": "https://images.unsplash.com/photo-1590402494682-cd3fb53b1f70?auto=format&fit=crop&w=1200&q=85", # Indian entrance diya lamps
    "house_2": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=85", # warm luxury modern home entrance
    "house_3": "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=85", # illuminated beautiful home
    "house_4": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=85", # luxury home exterior
    "house_5": "https://images.unsplash.com/photo-1608755728617-aefab37d2edd?auto=format&fit=crop&w=1200&q=85"  # Diya lamps festival traditional
}

for name, url in candidate_urls.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, timeout=5)
        print(f"[{name}] HTTP {res.status} OK")
    except Exception as e:
        print(f"[{name}] FAILED: {e}")
