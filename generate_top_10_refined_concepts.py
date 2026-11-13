import os
from playwright.sync_api import sync_playwright

artifact_dir = "C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3"
os.makedirs("login_refined_concepts", exist_ok=True)

abs_hero_img = "file:///" + os.path.abspath("assets/images/giftvault_flagship_hero_vertical.jpg").replace("\\", "/")
abs_ipad_img = "file:///" + os.path.abspath(f"{artifact_dir}/giftvault_login_ui_mockup_1794488875172.jpg").replace("\\", "/")
abs_palace_img = "file:///" + os.path.abspath(f"{artifact_dir}/giftvault_luxury_login_mockup_1794488893754.jpg").replace("\\", "/")

refined_concepts = [
    {
        "id": "R01",
        "title": "Refined Concept 01: Grand Wedding Table & iPad Ledger",
        "desc": "Real wedding reception table with marigold garlands, brass diyas, and an iPad showing live GiftVault ledger.",
        "left_html": f"""
        <div style="width:100%; height:100%; position:relative; overflow:hidden;">
          <img src="{abs_hero_img}" style="width:100%; height:100%; object-fit:cover; display:block; filter:contrast(1.05) saturate(1.1);">
          <div style="position:absolute; inset:0; background:linear-gradient(180deg, transparent 40%, rgba(15,23,42,0.92) 100%);"></div>
          <div style="position:absolute; bottom:32px; left:32px; right:32px; color:#FFF;">
            <div style="font-family:'Outfit',sans-serif; font-size:11px; font-weight:800; color:#F5D061; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:4px;">OFFICIAL WEDDING RECEPTION DESK</div>
            <h2 style="font-family:'Outfit',sans-serif; font-size:24px; font-weight:800; line-height:1.25; margin-bottom:6px;">Royal Vivaham & Celebrations</h2>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#E2E8F0; line-height:1.5;">Every guest blessing and shagun envelope safely recorded with zero paper leakage.</p>
          </div>
        </div>
        """
    },
    {
        "id": "R02",
        "title": "Refined Concept 02: English Luxury Heritage Ledger & Mobile App",
        "desc": "Concept 2 reimagined: 100% English branding 'GiftVault - The Sacred Ledger', zero Hindi, and zero +1 coins.",
        "left_html": """
        <div style="background:radial-gradient(circle at 35% 30%, #BA1E3B 0%, #680E1C 100%); width:100%; height:100%; padding:44px; display:flex; flex-direction:column; justify-content:space-between; color:#FFF;">
          <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(255,255,255,0.12); padding:6px 14px; border-radius:999px; width:fit-content; font-size:11px; font-weight:800; color:#FDE68A; letter-spacing:0.08em;">
            <span>HERITAGE VAULT SANCTUARY</span>
          </div>
          <div style="text-align:center; padding:20px 0;">
            <div style="width:160px; height:200px; margin:0 auto; background:linear-gradient(145deg, #B91C1C 0%, #7F1D1D 100%); border:2px solid #F59E0B; border-radius:12px; box-shadow:0 25px 50px rgba(0,0,0,0.5); display:flex; flex-direction:column; align-items:center; justify-content:center; padding:18px; position:relative;">
              <div style="font-family:'Cinzel',serif; font-size:14px; font-weight:800; color:#FDE68A; letter-spacing:0.12em;">GIFTVAULT</div>
              <div style="width:36px; height:1.5px; background:#F59E0B; margin:8px 0;"></div>
              <div style="font-family:'Outfit',sans-serif; font-size:11.5px; font-weight:700; color:#FEE2E2; text-align:center; line-height:1.4;">The Sacred Celebration Ledger</div>
              <div style="position:absolute; bottom:14px; font-size:10px; font-weight:800; color:#FDE68A; letter-spacing:0.1em;">ESTD. HERITAGE</div>
            </div>
          </div>
          <div>
            <h2 style="font-family:'Outfit',sans-serif; font-size:22px; font-weight:800; margin-bottom:6px;">Who Blessed The Family, Always Remembered</h2>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:12.5px; color:#FECDD3; line-height:1.55;">Replace fragile paper notebooks with an infallible, offline-ready private family ledger.</p>
          </div>
        </div>
        """
    },
    {
        "id": "R03",
        "title": "Refined Concept 03: Live Reception Desk Counter Statistics",
        "desc": "Displays live wedding counter analytics (Total Logged, Guests Count, 100% Offline Badge).",
        "left_html": """
        <div style="background:linear-gradient(140deg, #160408 0%, #300813 50%, #4D0C1E 100%); width:100%; height:100%; padding:44px; display:flex; flex-direction:column; justify-content:space-between; color:#FFF;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div style="font-family:'Outfit',sans-serif; font-size:18px; font-weight:800; color:#F5D061;">GIFTVAULT</div>
            <div style="background:rgba(16,185,129,0.18); border:1px solid #10B981; padding:4px 10px; border-radius:999px; font-size:11px; font-weight:800; color:#10B981;">OFFLINE READY 100%</div>
          </div>
          <div style="background:rgba(255,255,255,0.06); border:1.5px solid rgba(255,255,255,0.12); border-radius:18px; padding:24px; box-shadow:0 20px 40px rgba(0,0,0,0.3);">
            <div style="font-size:11.5px; font-weight:800; color:#FDE68A; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:8px;">ACTIVE RECEPTION COUNTER #1</div>
            <div style="font-family:'Outfit',sans-serif; font-size:36px; font-weight:900; color:#FFFFFF; margin-bottom:4px;">₹4,75,000</div>
            <div style="font-size:13px; color:#CBD5E1; margin-bottom:18px;">148 Envelopes & Cash Gifts Logged</div>
            <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:14px; display:flex; justify-content:space-between; font-size:12px; color:#E2E8F0;">
              <span>Thermal Slips: 148 Printed</span>
              <span style="color:#F5D061; font-weight:700;">Zero Discrepancies</span>
            </div>
          </div>
          <div>
            <h2 style="font-family:'Outfit',sans-serif; font-size:20px; font-weight:800; margin-bottom:6px;">Private & Confidential Ledger</h2>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:12.5px; color:#F1D5D8; line-height:1.5;">Data stored securely on your local device. No unauthorized cloud exposure.</p>
          </div>
        </div>
        """
    },
    {
        "id": "R04",
        "title": "Refined Concept 04: Royal Palatial Wedding Mandapam Scene",
        "desc": "An illuminated heritage wedding pavilion in golden ambient light paired with pure white auth container.",
        "left_html": f"""
        <div style="width:100%; height:100%; position:relative; overflow:hidden;">
          <img src="{abs_palace_img}" style="width:100%; height:100%; object-fit:cover; display:block;">
          <div style="position:absolute; inset:0; background:linear-gradient(180deg, transparent 40%, rgba(15,23,42,0.92) 100%);"></div>
          <div style="position:absolute; bottom:32px; left:32px; right:32px; color:#FFF;">
            <div style="font-family:'Outfit',sans-serif; font-size:11px; font-weight:800; color:#F5D061; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:4px;">ROYAL PALACE MANDAPAM</div>
            <h2 style="font-family:'Outfit',sans-serif; font-size:24px; font-weight:800; margin-bottom:6px;">Auspicious Celebration Vault</h2>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#E2E8F0; line-height:1.5;">Preserve every sacred shagun blessing with dignity and royal precision.</p>
          </div>
        </div>
        """
    },
    {
        "id": "R05",
        "title": "Refined Concept 05: Organic Crimson Wave Flow (Reference Image 2)",
        "desc": "Dynamic fluid wave dividing royal crimson celebration panel and pure white sign-in card.",
        "left_html": """
        <div style="background:linear-gradient(135deg, #7A0C1E 0%, #9E1B32 100%); width:100%; height:100%; padding:44px; display:flex; flex-direction:column; justify-content:space-between; color:#FFF; position:relative;">
          <svg style="position:absolute; top:0; bottom:0; right:-1px; width:70px; height:100%; pointer-events:none;" viewBox="0 0 100 1000" preserveAspectRatio="none">
            <path d="M0,0 C65,230 15,490 75,730 C105,860 55,1000 55,1000 L100,1000 L100,0 Z" fill="#FFFFFF"/>
          </svg>
          <div style="font-family:'Outfit',sans-serif; font-size:18px; font-weight:800; color:#FFE4A0;">GIFTVAULT</div>
          <div>
            <div style="font-size:11px; font-weight:800; color:#FDE68A; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:6px;">SACRED FAMILY SANCTUARY</div>
            <h2 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; line-height:1.25; margin-bottom:10px;">Preserve Every Blessing in Real Time</h2>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#FEE2E2; line-height:1.55; max-width:320px;">Dedicated reception counter for weddings, housewarmings, and auspicious family milestones.</p>
          </div>
          <div style="font-size:11px; color:rgba(255,255,255,0.7);">HYDERABAD • VIJAYAWADA • BENGALURU • VIZAG</div>
        </div>
        """
    },
    {
        "id": "R06",
        "title": "Refined Concept 06: Live 2-Inch Thermal Slip & Bluetooth Sync",
        "desc": "Highlights the 2-inch printed thank-you receipt slip generated live at reception desk.",
        "left_html": """
        <div style="background:#0F172A; width:100%; height:100%; padding:36px; display:flex; flex-direction:column; justify-content:space-between; color:#FFF;">
          <div style="font-size:11px; font-weight:800; color:#10B981; letter-spacing:0.1em;">THERMAL RECEIPT PRINTER READY</div>
          <div style="background:#FFF; color:#0F172A; border-radius:12px; padding:22px; font-family:'JetBrains Mono',monospace; font-size:12px; box-shadow:0 15px 35px rgba(0,0,0,0.35); border-top:4px solid #9E1B32;">
            <div style="text-align:center; font-weight:800; font-size:14px; font-family:'Outfit',sans-serif; margin-bottom:2px;">GIFTVAULT RECEIPT</div>
            <div style="text-align:center; font-size:10px; color:#64748B; margin-bottom:12px;">OFFICIAL SHAGUN SLIP #GV-101</div>
            <div style="border-bottom:1px dashed #CBD5E1; padding-bottom:10px; margin-bottom:10px; line-height:1.6;">
              <div>Guest: Mastan Rao Garu</div>
              <div>City: Chirala, AP</div>
              <div>Amount: ₹15,000</div>
              <div>Mode: Cash Counter #1</div>
            </div>
            <div style="text-align:center; font-size:10.5px; color:#059669; font-weight:800;">✓ RECORDED IN FAMILY VAULT</div>
          </div>
          <div style="font-size:12px; color:#94A3B8;">Compatible with all standard 2-inch Bluetooth & USB thermal printers.</div>
        </div>
        """
    },
    {
        "id": "R07",
        "title": "Refined Concept 07: Minimalist Warm Ivory & Auric Gold Frame",
        "desc": "Clean architectural luxury with gold auric borders and pure geometric typography.",
        "left_html": """
        <div style="background:#FAF7F2; border-right:1px solid #EBE5DB; width:100%; height:100%; padding:44px; display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div style="font-family:'Outfit',sans-serif; font-size:22px; font-weight:900; color:#9E1B32;">GIFTVAULT</div>
            <div style="font-size:10px; font-weight:800; color:#D97706; letter-spacing:0.15em; text-transform:uppercase; margin-top:2px;">ROYAL SHAGUN SANCTUARY</div>
          </div>
          <div style="background:#FFF; border:1.5px solid rgba(158,27,50,0.18); border-radius:16px; padding:22px; box-shadow:0 10px 30px rgba(15,23,42,0.05);">
            <div style="font-size:11px; font-weight:800; color:#9E1B32; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:6px;">ALL-IN-ONE CELEBRATION APP</div>
            <ul style="font-size:13px; color:#334155; line-height:2; padding-left:18px;">
              <li>Instant 2-Inch Thermal Slips</li>
              <li>WhatsApp Digital Receipts</li>
              <li>Official Excel & PDF Ledgers</li>
              <li>Up to 4 Concurrent Counters</li>
            </ul>
          </div>
          <div style="font-size:12px; color:#64748B;">
            Zero subscription traps. Lifetime private family archives.
          </div>
        </div>
        """
    },
    {
        "id": "R08",
        "title": "Refined Concept 08: Dark Mode Midnight Noir & Imperial Gold",
        "desc": "High-contrast dark mode with glowing imperial gold buttons and velvet crimson accents.",
        "left_html": """
        <div style="background:linear-gradient(145deg, #180308 0%, #0A0204 100%); border-right:1px solid rgba(255,255,255,0.1); width:100%; height:100%; padding:44px; display:flex; flex-direction:column; justify-content:space-between; color:#FFF;">
          <div style="font-family:'Outfit',sans-serif; font-size:20px; font-weight:800; color:#F5D061;">GIFTVAULT NOIR</div>
          <div style="text-align:center;">
            <div style="width:76px; height:76px; border-radius:20px; background:linear-gradient(135deg, #9E1B32, #680E1C); border:1.5px solid #F5D061; display:flex; align-items:center; justify-content:center; margin:0 auto 18px; box-shadow:0 12px 30px rgba(212,175,55,0.3);">
              <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#F5D061" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <h2 style="font-family:'Outfit',sans-serif; font-size:24px; font-weight:800; margin-bottom:8px;">256-Bit Encrypted Vault</h2>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#CBD5E1; line-height:1.6;">Highest standard of local encryption for family gift records.</p>
          </div>
          <div style="font-size:11px; color:#94A3B8;">ZERO CLOUD LEAKAGE • 100% OFFLINE READY</div>
        </div>
        """
    },
    {
        "id": "R09",
        "title": "Refined Concept 09: Multi-Desk Reception Architecture",
        "desc": "Visually showcases Groom Desk, Bride Desk, and VIP Counter working simultaneously.",
        "left_html": """
        <div style="background:linear-gradient(135deg, #0F172A 0%, #1E293B 100%); width:100%; height:100%; padding:40px; display:flex; flex-direction:column; justify-content:space-between; color:#FFF;">
          <div style="font-size:11px; font-weight:800; color:#38BDF8; letter-spacing:0.12em;">MULTI-DESK COUNTER ARCHITECTURE</div>
          <div>
            <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:12px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:700; font-size:13px;">Desk A (Groom Side)</span>
              <span style="color:#10B981; font-weight:700; font-size:12px;">₹2,45,000 (84 Gifts)</span>
            </div>
            <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:12px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:700; font-size:13px;">Desk B (Bride Side)</span>
              <span style="color:#10B981; font-weight:700; font-size:12px;">₹2,10,000 (72 Gifts)</span>
            </div>
            <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
              <span style="font-weight:700; font-size:13px;">Desk C (VIP Counter)</span>
              <span style="color:#10B981; font-weight:700; font-size:12px;">₹1,20,000 (18 Gifts)</span>
            </div>
          </div>
          <div style="font-size:12px; color:#94A3B8;">Automatic real-time sync across all reception desks.</div>
        </div>
        """
    },
    {
        "id": "R10",
        "title": "Refined Concept 10: ThreeUI Tactile Glassmorphism Studio",
        "desc": "Dual-tone tactile buttons, specular reflections, and pristine white auth card.",
        "left_html": """
        <div style="background:linear-gradient(135deg, #2D050E 0%, #4D0917 50%, #7A0C22 100%); width:100%; height:100%; padding:44px; display:flex; flex-direction:column; justify-content:space-between; color:#FFF;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div style="font-family:'Outfit',sans-serif; font-size:18px; font-weight:800; color:#FFE4A0;">GIFTVAULT</div>
            <div style="font-size:11px; font-weight:700; color:#FDE68A;">THREEUI TACTILE</div>
          </div>
          <div style="background:rgba(255,255,255,0.08); backdrop-filter:blur(16px); border:1.5px solid rgba(255,228,160,0.3); border-radius:20px; padding:24px; text-align:center;">
            <div style="width:54px; height:54px; border-radius:14px; background:linear-gradient(135deg, #FFE4A0, #D4AF37); display:flex; align-items:center; justify-content:center; margin:0 auto 14px; box-shadow:0 8px 20px rgba(212,175,55,0.4);">
              <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#9E1B32" stroke-width="2.2"><path d="M4 10h16v11H4z"/><path d="M12 10v11M4 15h16"/></svg>
            </div>
            <div style="font-family:'Outfit',sans-serif; font-size:22px; font-weight:800; color:#FFF; margin-bottom:6px;">Auspicious Shagun Sanctuary</div>
            <div style="font-size:12.5px; color:#F1D5D8; line-height:1.5;">Designed specifically for Indian families and auspicious celebrations.</div>
          </div>
          <div style="display:flex; justify-content:space-between; font-size:11.5px; color:#FCA5A5;">
            <span>Zero Paper Mess</span>
            <span>Instant PDF & Excel Export</span>
          </div>
        </div>
        """
    }
]

template = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin:0; padding:0; }}
body {{
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: radial-gradient(circle at 50% 25%, #252D37 0%, #161A20 55%, #0B0E12 100%);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 30px;
  color: #0F172A;
}}
.concept-header {{
  max-width: 1040px;
  width: 100%;
  margin-bottom: 20px;
  color: #FFFFFF;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}
.concept-badge {{
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.25);
  padding: 6px 14px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 700;
  color: #F5D061;
}}
.split-card {{
  max-width: 1020px;
  width: 100%;
  min-height: 580px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  border-radius: 26px;
  overflow: hidden;
  box-shadow: 0 40px 100px -20px rgba(0,0,0,0.75), 0 0 0 1px rgba(255,255,255,0.1);
  background: #FFFFFF;
}}
.left-pane {{
  min-height: 580px;
}}
.right-pane {{
  background: #FFFFFF;
  padding: 44px 48px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}
.form-group {{ margin-bottom: 18px; }}
.lbl {{ display:block; font-size:11.5px; font-weight:700; color:#64748B; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:6px; }}
.input-row {{ display:flex; align-items:center; border:1.5px solid #E2E8F0; border-radius:12px; background:#F8FAFC; overflow:hidden; transition:border-color 0.2s; }}
.input-row:focus-within {{ border-color:#9E1B32; background:#FFF; }}
.code {{ padding:12px 14px; font-size:14px; font-weight:800; color:#0F172A; background:#F1F5F9; border-right:1px solid #E2E8F0; }}
.inp {{ border:none; outline:none; background:transparent; padding:12px 14px; font-size:14.5px; font-family:inherit; color:#0F172A; width:100%; }}
.btn-primary {{ width:100%; padding:13px 24px; font-size:14px; font-weight:700; border:none; border-radius:12px; cursor:pointer; font-family:inherit; transition:transform 0.15s; }}
.btn-primary:hover {{ transform:translateY(-1px); }}
.divider {{ display:flex; align-items:center; gap:12px; margin:18px 0; color:#94A3B8; font-size:11.5px; }}
.divider::before, .divider::after {{ content:''; flex:1; height:1px; background:#E2E8F0; }}
.btn-secondary {{ width:100%; padding:11px 20px; font-size:13.5px; font-weight:700; border:1.5px solid #E2E8F0; border-radius:12px; background:#FFF; color:#334155; cursor:pointer; font-family:inherit; margin-bottom:10px; }}
.btn-guest {{ width:100%; padding:10px 18px; font-size:12.5px; font-weight:700; border:1px dashed rgba(158,27,50,0.4); border-radius:12px; background:#FFF5F6; color:#9E1B32; cursor:pointer; font-family:inherit; }}
</style>
</head>
<body>
  <div class="concept-header">
    <div>
      <div style="font-family:'Outfit',sans-serif; font-size:22px; font-weight:800;">{title}</div>
      <div style="font-size:12.5px; color:#94A3B8; margin-top:2px;">{desc}</div>
    </div>
    <div class="concept-badge">REFINED #{id}</div>
  </div>
  <div class="split-card">
    <div class="left-pane">
      {left_html}
    </div>
    <div class="right-pane">
      <div style="margin-bottom:24px;">
        <div style="width:44px; height:44px; border-radius:12px; background:linear-gradient(135deg,#9E1B32,#680E1C); display:flex; align-items:center; justify-content:center; margin-bottom:12px; box-shadow:0 8px 20px rgba(158,27,50,0.3);">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFE8A3" stroke-width="2"><path d="M4 10h16v11H4z"/><path d="M12 10v11M4 15h16"/></svg>
        </div>
        <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A; margin-bottom:4px;">Sign In to GiftVault</h1>
        <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B;">Enter mobile number to manage celebration ledgers.</p>
      </div>

      <div class="form-group">
        <label class="lbl">Mobile Number</label>
        <div class="input-row">
          <span class="code">+91</span>
          <input class="inp" type="tel" value="9876543210" maxlength="10">
        </div>
      </div>

      <button class="btn-primary" style="background:#9E1B32; color:#FFF; box-shadow:0 8px 20px rgba(158,27,50,0.3);">
        Send 6-Digit OTP &rarr;
      </button>

      <div class="divider"><span>or continue with</span></div>

      <button class="btn-secondary" style="display:flex; align-items:center; justify-content:center; gap:8px;">
        <svg width="16" height="16" viewBox="0 0 24 24"><path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/><path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/><path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/><path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/></svg>
        <span>Sign in with Google</span>
      </button>

      <button class="btn-guest">
        Continue as Guest (Sri Krishna Family Demo)
      </button>

      <div style="margin-top:16px; text-align:center; font-size:11.5px; color:#64748B;">
        256-Bit SSL Encrypted • Works 100% Offline
      </div>
    </div>
  </div>
</body>
</html>
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    for c in refined_concepts:
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        html_file = f"login_refined_concepts/concept_{c['id']}.html"
        full_html = template.format(
            title=c["title"],
            desc=c["desc"],
            id=c["id"],
            left_html=c["left_html"]
        )
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        
        file_url = "file:///" + os.path.abspath(html_file).replace("\\", "/")
        page.goto(file_url)
        page.wait_for_timeout(800)
        
        png_name = f"refined_login_{c['id']}.png"
        page.screenshot(path=f"login_refined_concepts/{png_name}")
        page.screenshot(path=f"{artifact_dir}/{png_name}")
        page.close()
        print(f"Rendered {png_name} successfully.")
    browser.close()

print("All 10 refined concepts rendered and saved to artifact directory!")
