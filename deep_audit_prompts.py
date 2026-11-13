import json

user_prompts = []
with open(r'C:\Users\shaik\.gemini\antigravity\brain\47128eb9-b322-408f-8e56-a5a702b79ee3\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            content = data.get('content', '')
            idx = data.get('step_index')
            if content and not content.startswith('<CONTEXT_SUMMARY>') and not content.startswith('Comments on artifact'):
                user_prompts.append((idx, content))

print(f"Total user prompts found: {len(user_prompts)}")
for idx, p in user_prompts:
    print(f"\n--- STEP {idx} (length {len(p)}) ---")
    lines = [line.strip() for line in p.split('\n') if line.strip() and not line.startswith('<ADDITIONAL_METADATA>') and not line.startswith('<USER_SETTINGS_CHANGE>')]
    for l in lines[:10]:
        print("  ", l[:120])
