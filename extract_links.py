import json
import re

user_links = []
app_names = set()

with open(r'C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            txt = data.get('content', '')
            idx = data.get('step_index')
            urls = re.findall(r'https?://[^\s<>"\')]+', txt)
            if urls:
                user_links.append((idx, urls))
            
            # Check for mentions of apps
            words = ['sgunms', 'nyota', 'shagun', 'chadivimpulu', 'dmoi', 'family function', 'gift note', 'budget']
            for w in words:
                if w in txt.lower():
                    app_names.add(w)

print("=== ALL LINKS GIVEN BY USER ===")
for idx, urls in user_links:
    print(f"Step {idx}:")
    for u in urls:
        print(f"  - {u}")

print("\n=== KEYWORDS/APPS DISCUSSED ===")
for a in app_names:
    print(f"  - {a}")
