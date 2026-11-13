import json

with open(r'C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        idx = data.get('step_index')
        if data.get('type') == 'USER_INPUT' and 622 < idx < 1365:
            content = data.get('content', '')
            if len(content) > 100:
                print(f"=== STEP {idx} ===")
                print(content[:350].strip())
