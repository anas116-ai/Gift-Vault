import json, os

for s in ['b1cf8230-85a5-4bd5-98c0-4b0c55c4622e', '1e1fd0ca-c194-4f92-987e-0cdf33d09423', 'da452cad-f0eb-4d28-b745-442d7b0214c3', 'b6548b4f-f553-4be3-bb26-348e97e6f706']:
    p = os.path.join(r'C:\Users\shaik\.gemini\antigravity\brain', s, '.system_generated', 'logs', 'transcript.jsonl')
    with open(p, 'r', encoding='utf-8') as f:
        for line in f:
            obj = json.loads(line)
            if obj.get('step_index') == 2:
                print(f"=== Subagent {s} step 2 ===")
                print(obj.get('content'))
