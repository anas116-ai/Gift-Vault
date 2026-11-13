import re
import json

target_files = [
    r'c:\Project\Gift Valut\web_preview\index.html',
    r'c:\Project\Gift Valut\web_preview\desktop.html',
    r'c:\Project\Gift Valut\web_preview\mobile.html',
    r'c:\Project\Gift Valut\build\web\index.html',
    r'c:\Project\Gift Valut\web\index.html'
]

with open(target_files[0], 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect where view-hub grid is
old_hub_grid = '''      <div class="events-selection-grid" id="events-hub-grid">
        <!-- Event Card 1: Wedding -->
        <div class="event-selection-card" onclick="enterWorkspaceEvent('event-wedding')">'''

# Let's check how the script section is organized and prepare the complete engine
print("Length of file:", len(html))
