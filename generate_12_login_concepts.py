import os
from playwright.sync_api import sync_playwright

concepts = [
    {
        "id": "01",
        "title": "Option 01: Royal Mandapam Photographic Showcase",
        "desc": "Real authentic Indian wedding photography in high-contrast editorial frame, paired with crisp white auth panel.",
        "html": """
        <div class="split-card">
          <div class="left-pane" style="padding:0; position:relative; overflow:hidden;">
            <img src="assets/images/giftvault_flagship_hero_vertical.jpg" style="width:100%; height:100%; object-fit:cover; filter:contrast(1.05) saturate(1.1);">
            <div style="position:absolute; inset:0; background:linear-gradient(180deg, transparent 40%, rgba(15,23,42,0.9) 100%);"></div>
            <div style="position:absolute; bottom:28px; left:28px; right:28px; color:#FFF;">
              <span style="font-family:'Outfit',sans-serif; font-size:11px; font-weight:800; color:#F5D061; letter-spacing:0.12em; text-transform:uppercase;">HERITAGE VAULT #GV-101</span>
              <h2 style="font-family:'Outfit',sans-serif; font-size:24px; font-weight:800; margin:4px 0 8px;">Royal Vivaham & Celebrations</h2>
              <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#E2E8F0; line-height:1.5;">Every sacred shagun blessing and cash envelope preserved with 100% offline security.</p>
            </div>
          </div>
          <div class="right-pane">
            <div style="margin-bottom:28px;">
              <div style="width:44px; height:44px; border-radius:12px; background:linear-gradient(135deg,#9E1B32,#680E1C); display:flex; align-items:center; justify-content:center; margin-bottom:12px; box-shadow:0 8px 20px rgba(158,27,50,0.3);">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#FFE8A3" stroke-width="2"><path d="M4 10h16v11H4z"/><path d="M12 10v11M4 15h16"/></svg>
              </div>
              <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A;">Sign In to GiftVault</h1>
              <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B;">Enter your mobile number to manage celebration ledgers.</p>
            </div>
            <div class="form-group">
              <label class="lbl">Mobile Number</label>
              <div class="input-row">
                <span class="code">+91</span>
                <input class="inp" type="text" value="9876543210">
              </div>
            </div>
            <button class="btn-primary" style="background:#9E1B32; color:#FFF;">Send 6-Digit OTP &rarr;</button>
            <div class="divider"><span>or</span></div>
            <button class="btn-secondary">Sign in with Google</button>
            <button class="btn-guest">Continue as Guest (1-Click Demo)</button>
          </div>
        </div>
        """
    },
    {
        "id": "02",
        "title": "Option 02: Traditional Red Shagun Book (Erra Pustakam) to Digital",
        "desc": "Sacred crimson notebook motif with golden turmeric markings, honoring traditional Indian family customs.",
        "html": """
        <div class="split-card">
          <div class="left-pane" style="background:radial-gradient(circle at 30% 30%, #BA1E3B 0%, #7A0C1E 100%); color:#FFF; display:flex; flex-direction:column; justify-content:space-between; padding:44px;">
            <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(255,255,255,0.12); padding:6px 14px; border-radius:999px; width:fit-content; font-size:11px; font-weight:800; color:#FDE68A;">
              <span>DIGITAL ERRA PUSTAKAM</span>
            </div>
            <div style="text-align:center; padding:20px 0;">
              <div style="width:140px; height:180px; margin:0 auto; background:linear-gradient(135deg, #B91C1C, #7F1D1D); border:2px solid #F59E0B; border-radius:8px; box-shadow:0 20px 40px rgba(0,0,0,0.4); display:flex; flex-direction:column; align-items:center; justify-content:center; padding:16px;">
                <div style="font-family:'Cinzel',serif; font-size:16px; font-weight:800; color:#FDE68A; letter-spacing:0.1em;">శ్రీరస్తు</div>
                <div style="font-size:11px; font-weight:700; color:#FEE2E2; margin-top:6px;">శుభకార్యాల పుస్తకం</div>
                <div style="margin-top:14px; width:36px; height:36px; border-radius:50%; background:#F59E0B; color:#7F1D1D; font-weight:900; font-size:14px; display:flex; align-items:center; justify-content:center;">+₹1</div>
              </div>
            </div>
            <div>
              <h2 style="font-family:'Outfit',sans-serif; font-size:22px; font-weight:800; margin-bottom:6px;">Never Lose a Shagun Record</h2>
              <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:12.5px; color:#FECDD3; line-height:1.5;">Replacing messy red notebooks with an infallible digital ledger for the entire family.</p>
            </div>
          </div>
          <div class="right-pane">
            <div style="margin-bottom:24px;">
              <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A;">Access Family Ledger</h1>
              <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B;">Enter your 10-digit registered number.</p>
            </div>
            <div class="form-group">
              <label class="lbl">Mobile Number</label>
              <div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div>
            </div>
            <button class="btn-primary" style="background:#9E1B32; color:#FFF;">Get Sacred Passcode</button>
            <div class="divider"><span>or</span></div>
            <button class="btn-secondary">Google Fast-Sign</button>
            <button class="btn-guest">Guest Demo Access &rarr;</button>
          </div>
        </div>
        """
    },
    {
        "id": "03",
        "title": "Option 03: Minimalist Modern Silk & Auric Gold (Linear/Aura Architecture)",
        "desc": "Ultra-clean geometric aesthetics with 1px auric gold border, dark tactile button, and pure breathing space.",
        "html": """
        <div class="split-card" style="border:1.5px solid rgba(212,175,55,0.4); box-shadow:0 30px 80px rgba(0,0,0,0.5);">
          <div class="left-pane" style="background:#FAF7F2; border-right:1px solid #EBE5DB; display:flex; flex-direction:column; justify-content:space-between; padding:44px;">
            <div>
              <div style="font-family:'Outfit',sans-serif; font-size:20px; font-weight:900; color:#9E1B32; letter-spacing:-0.01em;">GIFTVAULT</div>
              <div style="font-size:10px; font-weight:800; color:#D97706; letter-spacing:0.15em; text-transform:uppercase; margin-top:2px;">ROYAL SHAGUN SANCTUARY</div>
            </div>
            <div style="padding:20px 0;">
              <div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:16px; padding:20px; box-shadow:0 10px 25px rgba(0,0,0,0.04);">
                <div style="display:flex; justify-content:space-between; font-size:12px; color:#64748B; margin-bottom:10px;">
                  <span>LIVE RECEPTION DESK</span>
                  <span style="color:#059669; font-weight:700;">● ONLINE SYNC</span>
                </div>
                <div style="font-family:'Outfit',sans-serif; font-size:28px; font-weight:800; color:#0F172A;">₹4,75,116</div>
                <div style="font-size:11.5px; color:#475569; margin-top:4px;">148 Envelopes Logged • 0 Errors</div>
              </div>
            </div>
            <div style="font-size:12px; color:#64748B; line-height:1.6;">
              Trusted by 1,200+ South Indian families across Hyderabad, Vijayawada, Vizag & Bangalore.
            </div>
          </div>
          <div class="right-pane">
            <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A; margin-bottom:6px;">Welcome Back</h1>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B; margin-bottom:24px;">Log in to access your wedding counter.</p>
            <div class="form-group">
              <label class="lbl">Mobile or Family ID</label>
              <div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div>
            </div>
            <button class="btn-primary" style="background:#0F172A; color:#FFF;">Sign In</button>
            <div class="divider"><span>or continue with</span></div>
            <button class="btn-secondary">Sign in with Google</button>
            <button class="btn-guest">Explore Guest Demo</button>
          </div>
        </div>
        """
    },
    {
        "id": "04",
        "title": "Option 04: Glassmorphic Floating Island (Frosted Luxury)",
        "desc": "Ultra-modern translucent glass card floating over an ambient dark wedding mandapam bokeh background.",
        "html": """
        <div class="split-card" style="background:rgba(255,255,255,0.85); backdrop-filter:blur(24px); border:1.5px solid rgba(255,255,255,0.6); box-shadow:0 35px 90px rgba(0,0,0,0.6);">
          <div class="left-pane" style="background:linear-gradient(135deg, rgba(158,27,50,0.88), rgba(104,14,28,0.95)); color:#FFF; display:flex; flex-direction:column; justify-content:space-between; padding:44px;">
            <div style="font-family:'Outfit',sans-serif; font-size:18px; font-weight:800; color:#FFE4A0;">GIFTVAULT GLASS</div>
            <div style="text-align:center;">
              <div style="width:72px; height:72px; border-radius:20px; background:rgba(255,255,255,0.15); border:1.5px solid rgba(255,255,255,0.3); display:flex; align-items:center; justify-content:center; margin:0 auto 16px;">
                <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#FFE4A0" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              </div>
              <div style="font-family:'Outfit',sans-serif; font-size:22px; font-weight:800;">256-Bit Vault Security</div>
              <div style="font-size:13px; color:#F1D5D8; margin-top:6px;">Local SQLite encryption with instant thermal slips.</div>
            </div>
            <div style="display:flex; justify-content:center; gap:6px;">
              <span style="width:24px; height:6px; background:#FFE4A0; border-radius:999px;"></span>
              <span style="width:6px; height:6px; background:rgba(255,255,255,0.4); border-radius:50%;"></span>
              <span style="width:6px; height:6px; background:rgba(255,255,255,0.4); border-radius:50%;"></span>
            </div>
          </div>
          <div class="right-pane" style="background:transparent;">
            <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A; margin-bottom:6px;">Private Vault Entrance</h1>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B; margin-bottom:24px;">Enter credentials to open your reception register.</p>
            <div class="form-group"><label class="lbl">Phone Number</label><div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div></div>
            <button class="btn-primary" style="background:#9E1B32; color:#FFF;">Verify OTP & Enter</button>
            <div class="divider"><span>or</span></div>
            <button class="btn-secondary">Continue with Google</button>
            <button class="btn-guest">Guest Fast-Pass</button>
          </div>
        </div>
        """
    },
    {
        "id": "05",
        "title": "Option 05: Organic Wave Surfer Flow (Adapted to Royal Crimson)",
        "desc": "Direct homage to Reference Image 2: Fluid organic wave connecting the visual celebration side to the white form.",
        "html": """
        <div class="split-card" style="position:relative;">
          <div class="left-pane" style="background:linear-gradient(135deg, #7A0C1E 0%, #9E1B32 100%); color:#FFF; display:flex; flex-direction:column; justify-content:space-between; padding:44px; position:relative;">
            <svg style="position:absolute; top:0; bottom:0; right:-1px; width:70px; height:100%; pointer-events:none;" viewBox="0 0 100 1000" preserveAspectRatio="none">
              <path d="M0,0 C60,250 10,500 70,750 C100,880 50,1000 50,1000 L100,1000 L100,0 Z" fill="#FFFFFF"/>
            </svg>
            <div style="font-family:'Outfit',sans-serif; font-size:18px; font-weight:800; color:#FFE4A0;">GIFTVAULT FLUID</div>
            <div>
              <div style="font-family:'Cinzel',serif; font-size:26px; font-weight:800; color:#FFE4A0; margin-bottom:8px;">శుభకార్య ప్రవేశం</div>
              <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13.5px; color:#F8D7DA; line-height:1.6; max-width:300px;">Every guest's blessing preserved seamlessly without paper ledger confusion.</p>
            </div>
            <div style="font-size:11px; color:rgba(255,255,255,0.7);">ROYAL WEDDING • GRIHA PRAVESHAM • SAMSKARAM</div>
          </div>
          <div class="right-pane" style="padding-left:60px;">
            <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A; margin-bottom:6px;">Sign In</h1>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B; margin-bottom:24px;">Manage your wedding reception counter.</p>
            <div class="form-group"><label class="lbl">Mobile Number</label><div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div></div>
            <button class="btn-primary" style="background:#9E1B32; color:#FFF;">Sign In to Desk</button>
            <div class="divider"><span>or</span></div>
            <button class="btn-secondary">Sign in with Google</button>
            <button class="btn-guest">Instant Guest Demo</button>
          </div>
        </div>
        """
    },
    {
        "id": "06",
        "title": "Option 06: Centered Royal Vault Floating Modal (Project Typography & Authentic Motifs)",
        "desc": "The Lovebirds-inspired centered format strictly styled with Outfit, Plus Jakarta Sans, and auspicious gold kalash motifs.",
        "html": """
        <div class="split-card">
          <div class="left-pane" style="background:linear-gradient(160deg, #A4BDAE 0%, #8FA597 100%); display:flex; flex-direction:column; justify-content:space-between; align-items:center; text-align:center; padding:40px;">
            <div style="flex:1; display:flex; align-items:center; justify-content:center;">
              <div style="width:120px; height:120px; border-radius:50%; background:rgba(255,255,255,0.18); display:flex; align-items:center; justify-content:center; box-shadow:0 12px 30px rgba(0,0,0,0.08);">
                <svg width="60" height="60" viewBox="0 0 24 24" fill="none"><path d="M12 2L4 7v10l8 5 8-5V7l-8-5z" fill="#E5B25D" stroke="#C6923C" stroke-width="1.5"/><circle cx="12" cy="12" r="4" fill="#9E1B32"/><text x="12" y="14" font-size="6" font-weight="900" fill="#FFF" text-anchor="middle">₹1</text></svg>
              </div>
            </div>
            <div style="display:flex; gap:6px; margin-bottom:14px;">
              <span style="width:24px; height:6px; background:#FFF; border-radius:999px;"></span>
              <span style="width:6px; height:6px; background:rgba(255,255,255,0.4); border-radius:50%;"></span>
              <span style="width:6px; height:6px; background:rgba(255,255,255,0.4); border-radius:50%;"></span>
            </div>
            <div>
              <h2 style="font-family:'Outfit',sans-serif; font-size:22px; font-weight:800; color:#FFF; margin-bottom:6px;">Every Sacred Blessing Preserved</h2>
              <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:12.5px; color:rgba(255,255,255,0.9); line-height:1.5;">The private digital sanctuary for Indian celebrations.</p>
            </div>
          </div>
          <div class="right-pane">
            <h1 style="font-family:'Outfit',sans-serif; font-size:28px; font-weight:800; color:#1E293B; margin-bottom:4px;">GiftVault</h1>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B; margin-bottom:24px;">Welcome to GiftVault</p>
            <div class="form-group"><label class="lbl">Username or Mobile Number</label><div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div></div>
            <button class="btn-primary" style="background:#1E293B; color:#FFF; border-radius:999px;">Sign In</button>
            <div class="divider"><span>or</span></div>
            <button class="btn-secondary" style="border-radius:999px;">Sign in with Google</button>
            <button class="btn-guest" style="border-radius:999px;">Continue as Guest (Instant Demo)</button>
          </div>
        </div>
        """
    },
    {
        "id": "07",
        "title": "Option 07: Live 2-Inch Thermal Slip & Reception Counter Preview",
        "desc": "Showcases the real 2-inch thermal printed slip with QR code alongside the instant sign-in form.",
        "html": """
        <div class="split-card">
          <div class="left-pane" style="background:#1E293B; color:#FFF; display:flex; flex-direction:column; justify-content:space-between; padding:36px;">
            <div style="font-size:11px; font-weight:800; color:#10B981; letter-spacing:0.1em;">THERMAL PRINTER READY</div>
            <div style="background:#FFF; color:#0F172A; border-radius:12px; padding:20px; font-family:'Courier New',monospace; font-size:12px; box-shadow:0 15px 35px rgba(0,0,0,0.3); border-top:4px dashed #9E1B32;">
              <div style="text-align:center; font-weight:800; font-size:14px; margin-bottom:4px;">GIFTVAULT SLIP</div>
              <div style="text-align:center; font-size:10px; color:#64748B; margin-bottom:12px;">ROYAL VIVAHAM #GV-101</div>
              <div style="border-bottom:1px dashed #CBD5E1; padding-bottom:8px; margin-bottom:8px;">
                <div>Guest: Mastan Rao Garu</div>
                <div>Amount: ₹15,117 (₹15,116 + ₹1)</div>
                <div>Mode: Cash Counter #1</div>
              </div>
              <div style="text-align:center; font-size:10px; color:#059669; font-weight:700;">VERIFIED SHAGUN RECEIPT</div>
            </div>
            <div style="font-size:12px; color:#94A3B8;">Compatible with all standard 58mm & 80mm Bluetooth printers.</div>
          </div>
          <div class="right-pane">
            <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A; margin-bottom:6px;">Reception Counter Login</h1>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B; margin-bottom:24px;">Sign in to start issuing guest thank-you slips.</p>
            <div class="form-group"><label class="lbl">Counter Operator Phone</label><div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div></div>
            <button class="btn-primary" style="background:#059669; color:#FFF;">Open Counter Workspace &rarr;</button>
            <div class="divider"><span>or</span></div>
            <button class="btn-secondary">Google Sign-In</button>
            <button class="btn-guest">Test Counter in Demo Mode</button>
          </div>
        </div>
        """
    },
    {
        "id": "08",
        "title": "Option 08: Dark Mode Imperial Noir & Gold",
        "desc": "Deep midnight slate (#0A0D12) with glowing crimson borders, brushed auric gold accents, and pure high-contrast elegance.",
        "html": """
        <div class="split-card" style="background:#0F172A; border:1.5px solid rgba(212,175,55,0.4); color:#FFF;">
          <div class="left-pane" style="background:linear-gradient(135deg, #1E1018 0%, #0A0205 100%); border-right:1px solid rgba(255,255,255,0.1); display:flex; flex-direction:column; justify-content:space-between; padding:44px;">
            <div style="font-family:'Outfit',sans-serif; font-size:20px; font-weight:800; color:#F5D061;">GIFTVAULT NOIR</div>
            <div style="text-align:center;">
              <div style="width:80px; height:80px; border-radius:50%; background:linear-gradient(135deg,#9E1B32,#4A0815); border:2px solid #F5D061; display:flex; align-items:center; justify-content:center; margin:0 auto 20px; box-shadow:0 0 35px rgba(212,175,55,0.3);">
                <span style="font-size:28px; font-weight:900; color:#F5D061;">👑</span>
              </div>
              <h2 style="font-family:'Outfit',sans-serif; font-size:24px; font-weight:800; color:#FFF; margin-bottom:8px;">Royal Family Heritage</h2>
              <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#CBD5E1; line-height:1.6;">Multi-event family ledger with generational memory.</p>
            </div>
            <div style="font-size:11px; color:#94A3B8;">100% PRIVATE • ZERO CLOUD DATA MINING</div>
          </div>
          <div class="right-pane" style="background:#0F172A; color:#FFF;">
            <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#FFF; margin-bottom:6px;">Imperial Vault Sign-In</h1>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#94A3B8; margin-bottom:24px;">Enter your phone number to access all family events.</p>
            <div class="form-group"><label class="lbl" style="color:#CBD5E1;">Mobile Number</label><div class="input-row" style="background:#1E293B; border-color:#334155;"><span class="code" style="color:#F5D061;">+91</span><input class="inp" style="color:#FFF;" type="text" value="9876543210"></div></div>
            <button class="btn-primary" style="background:linear-gradient(135deg,#F5D061,#D97706); color:#0F172A; font-weight:800;">Open Royal Vault &rarr;</button>
            <div class="divider" style="color:#64748B;"><span style="background:#0F172A;">or</span></div>
            <button class="btn-secondary" style="background:#1E293B; border-color:#334155; color:#FFF;">Google Fast-Sign</button>
            <button class="btn-guest" style="color:#F5D061; border-color:rgba(212,175,55,0.4);">Continue in Guest Demo</button>
          </div>
        </div>
        """
    },
    {
        "id": "09",
        "title": "Option 09: Palace Jharokha Architectural Frame",
        "desc": "Intricate royal Indian palace jaali archway framing the digital reception counter.",
        "html": """
        <div class="split-card">
          <div class="left-pane" style="background:radial-gradient(circle at 50% 40%, #881426 0%, #4D0914 100%); color:#FFF; display:flex; flex-direction:column; justify-content:space-between; padding:44px; position:relative;">
            <div style="font-family:'Outfit',sans-serif; font-size:16px; font-weight:800; color:#FDE68A;">ROYAL JHAROKHA</div>
            <div style="border:2px solid #F59E0B; border-radius:120px 120px 16px 16px; padding:36px 20px; text-align:center; background:rgba(0,0,0,0.2);">
              <div style="font-family:'Cinzel',serif; font-size:24px; font-weight:800; color:#FDE68A; margin-bottom:6px;">శ్రీ కళ్యాణ వేదిక</div>
              <p style="font-size:12.5px; color:#FEE2E2; line-height:1.5;">Historic auspicious ceremonies documented with royal prestige.</p>
            </div>
            <div style="font-size:11px; color:#FCA5A5;">AMARAVATI • HYDERABAD • BANGALORE</div>
          </div>
          <div class="right-pane">
            <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A; margin-bottom:6px;">Mandapam Portal Login</h1>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B; margin-bottom:24px;">Connect counter to the temple mandapam.</p>
            <div class="form-group"><label class="lbl">Mobile Number</label><div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div></div>
            <button class="btn-primary" style="background:#9E1B32; color:#FFF;">Enter Ceremony Vault</button>
            <div class="divider"><span>or</span></div>
            <button class="btn-secondary">Sign in with Google</button>
            <button class="btn-guest">Guest Demo Access</button>
          </div>
        </div>
        """
    },
    {
        "id": "10",
        "title": "Option 10: Compact Minimalist Card (Single Centered Column)",
        "desc": "Ultra-focused 460px centered luxury card with generous white space, perfect for quick mobile OTP.",
        "html": """
        <div style="max-width:460px; width:100%; margin:auto; background:#FFF; border-radius:24px; padding:40px 36px; box-shadow:0 30px 80px rgba(0,0,0,0.5); border:1.5px solid rgba(158,27,50,0.2); text-align:center;">
          <div style="width:52px; height:52px; border-radius:14px; background:linear-gradient(135deg,#9E1B32,#680E1C); display:flex; align-items:center; justify-content:center; margin:0 auto 16px; box-shadow:0 10px 24px rgba(158,27,50,0.3);">
            <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#FFE8A3" stroke-width="2"><path d="M4 10h16v11H4z"/><path d="M12 10v11M4 15h16"/></svg>
          </div>
          <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A; margin-bottom:4px;">Sign In to GiftVault</h1>
          <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B; margin-bottom:28px;">Enter mobile number to manage celebration ledgers.</p>
          <div class="form-group" style="text-align:left;"><label class="lbl">Mobile Number</label><div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div></div>
          <button class="btn-primary" style="background:#9E1B32; color:#FFF; margin-top:8px;">Send 6-Digit OTP &rarr;</button>
          <div class="divider"><span>or</span></div>
          <button class="btn-secondary">Sign in with Google</button>
          <button class="btn-guest">Continue as Guest (Instant Demo)</button>
        </div>
        """
    },
    {
        "id": "11",
        "title": "Option 11: Multi-Counter Reception Desk Showcase",
        "desc": "Highlights the 4-desk concurrent counter capability for large 1,000+ guest weddings.",
        "html": """
        <div class="split-card">
          <div class="left-pane" style="background:linear-gradient(135deg, #0F172A 0%, #1E293B 100%); color:#FFF; display:flex; flex-direction:column; justify-content:space-between; padding:40px;">
            <div style="font-size:11px; font-weight:800; color:#38BDF8; letter-spacing:0.12em;">MULTI-DESK ARCHITECTURE</div>
            <div>
              <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:12px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                <span style="font-weight:700; font-size:13px;">Counter A (Groom Side)</span>
                <span style="color:#10B981; font-weight:700; font-size:12px;">92 Logged</span>
              </div>
              <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:12px; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
                <span style="font-weight:700; font-size:13px;">Counter B (Bride Side)</span>
                <span style="color:#10B981; font-weight:700; font-size:12px;">114 Logged</span>
              </div>
              <div style="background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:12px; padding:12px; display:flex; justify-content:space-between; align-items:center;">
                <span style="font-weight:700; font-size:13px;">Counter C (VIP Desk)</span>
                <span style="color:#10B981; font-weight:700; font-size:12px;">48 Logged</span>
              </div>
            </div>
            <div style="font-size:12px; color:#94A3B8;">Zero line queues. Zero duplicate entries. Real-time auto sync.</div>
          </div>
          <div class="right-pane">
            <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A; margin-bottom:6px;">Multi-Desk Sign In</h1>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B; margin-bottom:24px;">Select your counter and begin entries.</p>
            <div class="form-group"><label class="lbl">Operator Mobile</label><div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div></div>
            <button class="btn-primary" style="background:#0F172A; color:#FFF;">Connect to Desk</button>
            <div class="divider"><span>or</span></div>
            <button class="btn-secondary">Google Fast-Sign</button>
            <button class="btn-guest">Guest Multi-Desk Demo</button>
          </div>
        </div>
        """
    },
    {
        "id": "12",
        "title": "Option 12: Auspicious Sindoor & Silk Editorial Showcase",
        "desc": "Warm auspicious sindoor crimson and pure ivory silk styling with ThreeUI tactile buttons.",
        "html": """
        <div class="split-card">
          <div class="left-pane" style="background:linear-gradient(135deg, #881426 0%, #C41E3A 100%); color:#FFF; display:flex; flex-direction:column; justify-content:space-between; padding:44px;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-family:'Outfit',sans-serif; font-size:18px; font-weight:900; color:#FFE4A0;">GIFTVAULT</span>
              <span style="background:rgba(255,255,255,0.2); font-size:10px; font-weight:800; padding:4px 10px; border-radius:999px;">OFFLINE 100%</span>
            </div>
            <div>
              <div style="font-size:11px; font-weight:800; color:#FDE68A; letter-spacing:0.15em; text-transform:uppercase; margin-bottom:6px;">THE SACRED VAULT</div>
              <h2 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; line-height:1.25; margin-bottom:10px;">Who Blessed The Family, Always Remembered</h2>
              <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#FEE2E2; line-height:1.55;">Complete reciprocity ledger: know who attended your event when you attend theirs.</p>
            </div>
            <div style="font-size:11px; color:#FECDD3;">256-BIT ENCRYPTED • ZERO LEAKAGE</div>
          </div>
          <div class="right-pane">
            <h1 style="font-family:'Outfit',sans-serif; font-size:26px; font-weight:800; color:#0F172A; margin-bottom:6px;">Sign In to GiftVault</h1>
            <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:13px; color:#64748B; margin-bottom:24px;">Enter your mobile number to manage ledgers.</p>
            <div class="form-group"><label class="lbl">Mobile Number</label><div class="input-row"><span class="code">+91</span><input class="inp" type="text" value="9876543210"></div></div>
            <button class="btn-primary" style="background:#9E1B32; color:#FFF; box-shadow:0 8px 24px rgba(158,27,50,0.35);">Send 6-Digit OTP &rarr;</button>
            <div class="divider"><span>or</span></div>
            <button class="btn-secondary">Sign in with Google</button>
            <button class="btn-guest">Explore as Guest (1-Click Demo)</button>
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
    <div class="concept-badge">CONCEPT #{id}</div>
  </div>
  {html}
</body>
</html>
"""

os.makedirs("login_concepts", exist_ok=True)
os.makedirs("test_evidence", exist_ok=True)
artifact_dir = "C:/Users/shaik/.gemini/antigravity/brain/47128eb9-b322-408f-8e56-a5a702b79ee3"

with sync_playwright() as p:
    browser = p.chromium.launch()
    for c in concepts:
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        html_file = f"login_concepts/concept_{c['id']}.html"
        full_html = template.format(
            title=c["title"],
            desc=c["desc"],
            id=c["id"],
            html=c["html"]
        )
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(full_html)
        
        file_url = "file:///" + os.path.abspath(html_file).replace("\\", "/")
        page.goto(file_url)
        page.wait_for_timeout(800)
        
        png_name = f"login_concept_{c['id']}.png"
        page.screenshot(path=f"login_concepts/{png_name}")
        page.screenshot(path=f"{artifact_dir}/{png_name}")
        page.close()
        print(f"Rendered {png_name} successfully.")
    browser.close()

print("All 12 login concepts rendered and saved to artifact directory!")
