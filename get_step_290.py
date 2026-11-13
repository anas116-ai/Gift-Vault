import json

transcript_path = r'C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\.system_generated\logs\transcript.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT' and obj.get('step_index') == 290:
            print("STEP 290:")
            print(obj.get('content', ''))
