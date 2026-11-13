import json

transcript_path = r'C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\.system_generated\logs\transcript.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT':
            content = obj.get('content', '')
            idx = obj.get('step_index', 0)
            # Filter steps around 40 to 1370
            if 30 <= idx <= 1380:
                print(f"\n=== STEP {idx} ===")
                # Print first 600 chars of each
                print(content[:800])
