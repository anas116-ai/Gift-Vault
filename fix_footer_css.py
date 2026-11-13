import os

# Update landing-sections.css across all directories
target_files = [
    'assets/css/landing-sections.css',
    'web_preview/assets/css/landing-sections.css',
    'build/web/assets/css/landing-sections.css',
    'web/assets/css/landing-sections.css'
]

for fpath in target_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the conflicting .footer-master rule
        content = content.replace(
            '''.footer-master {
  border-top: 1px solid var(--border-moderate);
  background: #FAF7F2;
  padding: 50px 0 30px;
  margin-top: 60px;
  color: #475569;
}''',
            '''.footer-master {
  background: #0E1217 !important;
  color: #CBD5E1 !important;
  padding: 64px 0 32px !important;
  margin-top: 60px;
  border-top: 1px solid rgba(198, 146, 60, 0.3) !important;
}'''
        )
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fpath}")

print("Sync completed!")
