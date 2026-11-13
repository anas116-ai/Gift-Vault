import os, re

# Update landing-sections.css
for path in ['assets/css/landing-sections.css', 'web_preview/assets/css/landing-sections.css', 'build/web/assets/css/landing-sections.css', 'web/assets/css/landing-sections.css']:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(r'\.footer-master\s*\{[^}]*\}', '''.footer-master {
  background: #FAF7F2 !important;
  color: #475569 !important;
  padding: 54px 0 30px !important;
  margin-top: 60px;
  border-top: 1px solid rgba(226, 218, 205, 0.9) !important;
}''', content)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {path}")

print("Sync completed!")
