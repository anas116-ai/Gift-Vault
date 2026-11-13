import json

with open(r'C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            content = data.get('content', '')
            idx = data.get('step_index')
            # Check length or interesting content
            if len(content) > 300 and idx not in [0, 40, 290, 309, 1371, 1387]:
                print(f"=== STEP {idx} (len {len(content)}) ===")
                print(content[:600])
