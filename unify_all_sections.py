import os
import re

old_family_pattern = re.compile(
    r'<section class="hero-ref1-family-section".*?</section>',
    re.DOTALL
)

new_family_section = """<section class="hero-ref1-family-section" style="display: grid; grid-template-columns: 1fr 1.05fr; gap: 40px; align-items: center; background: #FFFFFF; border: 1.5px solid rgba(220, 200, 180, 0.4); border-radius: 20px; padding: 32px 38px; box-shadow: 0 16px 45px rgba(0,0,0,0.04); margin-bottom: 45px;">
        <!-- Left: Family Image -->
        <div style="border-radius: 16px; overflow: hidden; box-shadow: 0 12px 30px rgba(0,0,0,0.08); border: 1px solid rgba(220, 200, 180, 0.35);">
          <img src="assets/images/giftvault_family_reference_showcase.png" alt="Indian Family Reviewing GiftVault" style="width: 100%; height: auto; display: block; object-fit: cover;">
        </div>
        <!-- Right: Text Content -->
        <div>
          <div style="display: inline-flex; align-items: center; gap: 6px; font-size: 11px; font-weight: 800; color: #8A1526; background: rgba(138, 21, 38, 0.06); border: 1px solid rgba(138, 21, 38, 0.16); padding: 4px 14px; border-radius: 7px; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 16px; font-family: 'Plus Jakarta Sans', sans-serif;">
            <span style="color: #D4AF37;">◆</span>
            <span>BUILT FOR FAMILIES</span>
            <span style="color: #8A1526;">•</span>
          </div>
          <h2 style="font-family: 'Outfit', 'Plus Jakarta Sans', sans-serif; font-size: clamp(24px, 2.6vw, 34px); font-weight: 750; color: #1F1916; line-height: 1.25; margin: 0 0 14px; text-transform: none; letter-spacing: -0.02em;">
            A Smarter Way to Remember Together
          </h2>
          <p style="font-size: 15px; color: #5C524B; line-height: 1.65; margin-bottom: 22px; font-weight: 450; font-family: 'Plus Jakarta Sans', sans-serif;">
            From weddings to family gatherings, GiftVault helps you stay organised and connected with your loved ones.
          </p>
          <button type="button" class="btn-tactile-primary" onclick="navToView('login')">
            <span>Learn More</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </section>"""

targets = ['index.html', 'web_preview/index.html', 'build/web/index.html', 'web/index.html']

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    content = old_family_pattern.sub(new_family_section, content)
    with open(t, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated family section in {t}")
