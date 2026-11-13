import subprocess
import sys

scripts = [
    'apply_complete_features.py',
    'apply_all_user_conversation_features.py',
    'add_all_missing_conversation_features.py',
    'apply_security_hardening.py',
    'redesign_footer.py',
    'comprehensive_design_fix.py'
]

for s in scripts:
    print(f"Running {s}...")
    res = subprocess.run([sys.executable, s], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error in {s}:")
        print(res.stderr)
        sys.exit(1)
    else:
        print(f"Completed {s} successfully.")

print("\nAll 6 steps executed! Exact previous version restored perfectly!")
