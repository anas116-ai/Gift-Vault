import re

target_files = [
    r'c:\Project\Gift Valut\web_preview\index.html',
    r'c:\Project\Gift Valut\web_preview\desktop.html',
    r'c:\Project\Gift Valut\web_preview\mobile.html',
    r'c:\Project\Gift Valut\build\web\index.html',
    r'c:\Project\Gift Valut\web\index.html'
]

with open(target_files[0], 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Relationship dropdown to Munshi Fast Entry (if not already detailed)
# Let's check entry form in html
old_entry_row = '''            <!-- Guest Name & City -->
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
              <div class="form-group-item" style="margin-bottom: 0;">
                <label class="form-label-txt" data-i18n="lbl_guest_name">Guest / Family Name *</label>
                <input type="text" id="entry-name" class="form-input-field" placeholder="e.g., K. Venkata Rao Garu" required>
              </div>
              <div class="form-group-item" style="margin-bottom: 0;">
                <label class="form-label-txt" data-i18n="lbl_city">Native Town / City</label>
                <input type="text" id="entry-city" class="form-input-field" placeholder="e.g., Vijayawada, Guntur">
              </div>
            </div>'''

new_entry_row = '''            <!-- Guest Name, Relationship & City -->
            <div style="display: grid; grid-template-columns: 1.2fr 1fr 1fr; gap: 16px; margin-bottom: 16px;">
              <div class="form-group-item" style="margin-bottom: 0;">
                <label class="form-label-txt" data-i18n="lbl_guest_name">Guest / Family Name *</label>
                <input type="text" id="entry-name" class="form-input-field" placeholder="e.g., K. Venkata Rao Garu" required>
              </div>
              <div class="form-group-item" style="margin-bottom: 0;">
                <label class="form-label-txt" data-i18n="lbl_relation">Relationship (సంబంధం)</label>
                <select id="entry-relation" class="form-input-field">
                  <option value="బావ / Brother-in-law" data-i18n="opt_rel_brother_in_law">బావ / Brother-in-law</option>
                  <option value="బాబాయ్ / Uncle" data-i18n="opt_rel_uncle">బాబాయ్ / Uncle</option>
                  <option value="మామ / Father-in-law" data-i18n="opt_rel_fil">మామ / Father-in-law</option>
                  <option value="మేనమామ / Maternal Uncle" data-i18n="opt_rel_mat_uncle">మేనమామ / Maternal Uncle</option>
                  <option value="స్నేహితుడు / Friend" data-i18n="opt_rel_friend">స్నేహితుడు / Friend</option>
                  <option value="బంధువు / Relative" selected data-i18n="opt_rel_relative">బంధువు / Relative</option>
                  <option value="పొరుగువారు / Neighbor" data-i18n="opt_rel_neighbor">పొరుగువారు / Neighbor</option>
                </select>
              </div>
              <div class="form-group-item" style="margin-bottom: 0;">
                <label class="form-label-txt" data-i18n="lbl_city">Native Town / City</label>
                <input type="text" id="entry-city" class="form-input-field" placeholder="e.g., Vijayawada, Guntur">
              </div>
            </div>'''

if old_entry_row in html:
    html = html.replace(old_entry_row, new_entry_row)

# 2. Add Family Sync & Roles + Media Verification Settings in Settings Tab
old_settings_section = '''      <!-- TAB 8: SETTINGS -->
      <section id="tab-settings" class="tab-pane">
        <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 28px; max-width: 680px; margin: 0 auto;">
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night); margin-bottom: 8px;" data-i18n="cfg_title">Event Configuration</h3>
          <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;" data-i18n="cfg_desc">Manage celebration parameters, PINs, and counter settings</p>

          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="cfg_name_lbl">Event Celebration Title</label>
            <input type="text" class="form-input-field" value="Rahul & Snigdha Kalyanam">
          </div>
          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="cfg_coin_lbl">Auspicious Coin Rounding</label>
            <select class="form-input-field">
              <option selected data-i18n="cfg_opt_coin">Always offer +₹1 lucky coin button</option>
              <option data-i18n="cfg_opt_round">Standard round numbers only</option>
            </select>
          </div>
          <div class="form-group-item">
            <label class="form-label-txt" data-i18n="cfg_pin_lbl">Desk Host Passcode</label>
            <input type="password" class="form-input-field" value="2026">
          </div>
          <button type="button" class="btn-crimson" onclick="alert('Settings saved successfully!')">
            <span data-i18n="btn_save_cfg">Save Configuration</span>
          </button>
        </div>
      </section>'''

new_settings_section = '''      <!-- TAB 8: SETTINGS, FAMILY SYNC & MEDIA POLICIES -->
      <section id="tab-settings" class="tab-pane">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; max-width: 1040px; margin: 0 auto;">
          
          <!-- Event Core & Media Verification Settings -->
          <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 24px;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
              <span style="font-size: 20px;">⚙️</span>
              <h3 style="font-family: var(--font-serif); font-size: 22px; font-weight: 800; color: var(--c-night);" data-i18n="cfg_title">Event Configuration</h3>
            </div>
            <p style="font-size: 13px; color: var(--c-muted); margin-bottom: 20px;" data-i18n="cfg_desc">Manage celebration parameters, PINs, and verification rules</p>

            <div class="form-group-item">
              <label class="form-label-txt" data-i18n="cfg_name_lbl">Event Celebration Title</label>
              <input type="text" class="form-input-field" value="Rahul & Snigdha Kalyanam">
            </div>

            <div class="form-group-item">
              <label class="form-label-txt" data-i18n="cfg_photo_policy">Gift Photo Proof Policy (ఫోటో సెట్టింగ్)</label>
              <select class="form-input-field">
                <option value="compulsory" data-i18n="opt_photo_compulsory">కంపల్సరీ (Compulsory for Gold & Articles)</option>
                <option value="optional" selected data-i18n="opt_photo_optional">ఐచ్ఛికం (Optional for all gifts)</option>
                <option value="off" data-i18n="opt_photo_off">ఆఫ్ (Disabled)</option>
              </select>
            </div>

            <div class="form-group-item">
              <label class="form-label-txt" data-i18n="cfg_video_policy">Short Video / Clip Policy (వీడియో సెట్టింగ్)</label>
              <select class="form-input-field">
                <option value="optional" selected data-i18n="opt_video_optional">ఐచ్ఛికం (Optional Short Video Clip / Drive Link)</option>
                <option value="compulsory" data-i18n="opt_video_compulsory">కంపల్సరీ (Mandatory)</option>
                <option value="off" data-i18n="opt_video_off">ఆఫ్ (Off)</option>
              </select>
            </div>

            <div class="form-group-item">
              <label class="form-label-txt" data-i18n="cfg_coin_lbl">Auspicious Coin Rounding</label>
              <select class="form-input-field">
                <option selected data-i18n="cfg_opt_coin">Always offer +₹1 lucky coin button</option>
                <option data-i18n="cfg_opt_round">Standard round numbers only</option>
              </select>
            </div>

            <div class="form-group-item">
              <label class="form-label-txt" data-i18n="cfg_pin_lbl">Desk Host Passcode (Security PIN)</label>
              <input type="password" class="form-input-field" value="2026">
            </div>

            <button type="button" class="btn-crimson" style="width: 100%;" onclick="alert(currentLang === 'te' ? 'సెట్టింగ్స్ సేవ్ చేయబడ్డాయి!' : 'Configuration saved successfully!')">
              <span data-i18n="btn_save_cfg">Save Configuration</span>
            </button>
          </div>

          <!-- Family Sync & Role Access (From Step 40 Requirements) -->
          <div style="background: #FFFFFF; border: 2px solid var(--c-night); border-radius: 16px; padding: 24px; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                  <span style="font-size: 20px;">👨‍👩‍👧‍👦</span>
                  <h3 style="font-family: var(--font-serif); font-size: 22px; font-weight: 800; color: var(--c-night);" data-i18n="family_sync_title">Family Sync & Munshi Roles</h3>
                </div>
                <span class="tag-badge" style="background: var(--c-emerald); color: #FFFFFF;" data-i18n="badge_cloud_live">3 ACTIVE DEVICES</span>
              </div>
              <p style="font-size: 13px; color: var(--c-muted); margin-bottom: 20px;" data-i18n="family_sync_desc">Multi-member simultaneous entry with role-based permissions (Owner, Munshi, Viewer)</p>

              <!-- Member List -->
              <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; background: var(--c-base); border-radius: 10px; border: 1px solid var(--c-border);">
                  <div>
                    <strong style="font-size: 13.5px; color: var(--c-night);">K. Rama Rao (You)</strong>
                    <div style="font-size: 11.5px; color: var(--c-muted);">ramarao@gmail.com • Primary Device</div>
                  </div>
                  <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF;" data-i18n="role_owner">OWNER</span>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; background: var(--c-base); border-radius: 10px; border: 1px solid var(--c-border);">
                  <div>
                    <strong style="font-size: 13.5px; color: var(--c-night);">Suresh (Brother / Reception Desk)</strong>
                    <div style="font-size: 11.5px; color: var(--c-muted);">+91 98480 12345 • Fast Voice Munshi</div>
                  </div>
                  <span class="tag-badge" style="background: var(--c-crimson); color: #FFFFFF;" data-i18n="role_munshi">MUNSHI / RECORDER</span>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 14px; background: var(--c-base); border-radius: 10px; border: 1px solid var(--c-border);">
                  <div>
                    <strong style="font-size: 13.5px; color: var(--c-night);">Lakshmi Garu (Mother)</strong>
                    <div style="font-size: 11.5px; color: var(--c-muted);">iPad Live View • Read Only</div>
                  </div>
                  <span class="tag-badge" style="background: var(--c-emerald); color: #FFFFFF;" data-i18n="role_viewer">FAMILY VIEWER</span>
                </div>
              </div>
            </div>

            <!-- Invite Button -->
            <div style="background: var(--c-base); border: 1.5px dashed var(--c-night); border-radius: 12px; padding: 16px; text-align: center;">
              <div style="font-size: 13px; font-weight: 700; color: var(--c-night); margin-bottom: 6px;" data-i18n="invite_family_btn_title">Invite Another Family Member / Munshi</div>
              <div style="font-size: 11.5px; color: var(--c-muted); margin-bottom: 12px;" data-i18n="invite_family_btn_desc">Generate a secure 6-digit sync link for instant joining on their phone</div>
              <button type="button" class="btn-outline-dark" style="font-size: 12.5px; padding: 8px 16px;" onclick="shareFamilySyncLink()">
                📲 <span data-i18n="btn_share_family_link">Share Family Sync Link (WhatsApp)</span>
              </button>
            </div>

          </div>

        </div>
      </section>'''

if old_settings_section in html:
    html = html.replace(old_settings_section, new_settings_section)

# 3. Add Pricing / Plans Modal (Inspired by Step 40: Rs. 49 / Rs. 99 per function pass & Sgunms/Thenyota)
pricing_modal_html = '''
  <!-- MODAL: ROYAL PLANS & EVENT PASS (Step 40 & Reference Apps Model) -->
  <div id="modal-pricing-plans" class="modal-backdrop">
    <div class="modal-card" style="max-width: 640px;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-size: 24px;">👑</span>
          <h3 style="font-family: var(--font-serif); font-size: 24px; font-weight: 800; color: var(--c-night);" data-i18n="plans_modal_title">Auspicious Celebration Plans</h3>
        </div>
        <button type="button" class="modal-close-btn" onclick="closePricingModal()">&times;</button>
      </div>
      <p style="font-size: 13.5px; color: var(--c-muted); margin-bottom: 24px;" data-i18n="plans_modal_sub">Affordable per-event pass or unlimited family lifetime access</p>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px;">
        <!-- Single Function Pass -->
        <div style="border: 2px solid var(--c-night); border-radius: 14px; padding: 20px; background: #FFFFFF; position: relative;">
          <span class="tag-badge" style="background: var(--c-night); color: #FFFFFF; font-size: 10.5px; position: absolute; top: -10px; right: 16px;" data-i18n="plan_badge_single">PER FUNCTION</span>
          <h4 style="font-family: var(--font-serif); font-size: 18px; font-weight: 700; color: var(--c-night); margin-bottom: 6px;" data-i18n="plan_single_title">Single Event Pass</h4>
          <div class="num-currency" style="font-size: 32px; font-weight: 800; color: var(--c-crimson); margin-bottom: 8px;">₹49 <span style="font-size: 13px; font-weight: 500; color: var(--c-muted);">/ event</span></div>
          <p style="font-size: 12px; color: var(--c-muted); margin-bottom: 16px;" data-i18n="plan_single_desc">Perfect for Haldi, Birthday or Small Function</p>
          <ul style="font-size: 12.5px; color: var(--c-night); line-height: 1.8; padding-left: 18px; margin-bottom: 20px;">
            <li data-i18n="plan_feat_1">Up to 500 Guest Entries</li>
            <li data-i18n="plan_feat_2">Fast Voice Dictation</li>
            <li data-i18n="plan_feat_3">WhatsApp Receipts</li>
            <li data-i18n="plan_feat_4">PDF & Excel Reports</li>
          </ul>
          <button type="button" class="btn-outline-dark" style="width: 100%;" onclick="alert(currentLang === 'te' ? 'ఈవెంట్ పాస్ యాక్టివేట్ అయ్యింది!' : 'Event Pass Activated!')" data-i18n="btn_choose_single">Choose Single Pass</button>
        </div>

        <!-- Royal Family Lifetime -->
        <div style="border: 2px solid var(--c-crimson); border-radius: 14px; padding: 20px; background: var(--c-base); position: relative; box-shadow: 0 8px 24px rgba(248,51,60,0.12);">
          <span class="tag-badge" style="background: var(--c-crimson); color: #FFFFFF; font-size: 10.5px; position: absolute; top: -10px; right: 16px;" data-i18n="plan_badge_family">MOST POPULAR</span>
          <h4 style="font-family: var(--font-serif); font-size: 18px; font-weight: 700; color: var(--c-crimson); margin-bottom: 6px;" data-i18n="plan_family_title">Royal Family Lifetime</h4>
          <div class="num-currency" style="font-size: 32px; font-weight: 800; color: var(--c-emerald); margin-bottom: 8px;">₹199 <span style="font-size: 13px; font-weight: 500; color: var(--c-muted);">/ lifetime</span></div>
          <p style="font-size: 12px; color: var(--c-muted); margin-bottom: 16px;" data-i18n="plan_family_desc">All family weddings, housewarmings & events forever</p>
          <ul style="font-size: 12.5px; color: var(--c-night); line-height: 1.8; padding-left: 18px; margin-bottom: 20px;">
            <li data-i18n="plan_f_feat_1">Unlimited Events & Entries</li>
            <li data-i18n="plan_f_feat_2">Multi-Device Family Sync (3+ Munshis)</li>
            <li data-i18n="plan_f_feat_3">Live Reception Audio Soundbox</li>
            <li data-i18n="plan_f_feat_4">Photo Proof Cloud Storage</li>
            <li data-i18n="plan_f_feat_5">Reciprocity Debt Matrix</li>
          </ul>
          <button type="button" class="btn-crimson" style="width: 100%;" onclick="alert(currentLang === 'te' ? 'రాయల్ లైఫ్‌టైమ్ ప్లాన్ యాక్టివేట్ అయ్యింది!' : 'Royal Lifetime Plan Activated!')" data-i18n="btn_choose_family">Unlock Lifetime Access</button>
        </div>
      </div>

      <div style="text-align: center; font-size: 11.5px; color: var(--c-muted);" data-i18n="plans_guarantee">
        🔒 100% Auspicious Guarantee • Safe Cloud Sync • Zero Advertisements
      </div>
    </div>
  </div>
'''

if 'id="modal-pricing-plans"' not in html:
    html = html.replace('<!-- MODAL: CREATE NEW AUSPICIOUS EVENT -->', pricing_modal_html + '\n  <!-- MODAL: CREATE NEW AUSPICIOUS EVENT -->')

# 4. Add "👑 Plans (₹49)" button in top navigation bar so user can access it anytime
old_nav_actions = '''      <div class="nav-right-actions">
        <!-- Live Language Dropdown Selector (Active Dynamic Translator) -->'''

new_nav_actions = '''      <div class="nav-right-actions">
        <!-- Royal Plans Button -->
        <button type="button" class="btn-outline-dark" style="padding: 6px 12px; font-size: 12px;" onclick="openPricingModal()">
          👑 <span data-i18n="nav_plans_btn">Plans (₹49)</span>
        </button>
        <!-- Live Language Dropdown Selector (Active Dynamic Translator) -->'''

if old_nav_actions in html and 'nav_plans_btn' not in html:
    html = html.replace(old_nav_actions, new_nav_actions)

# 5. Add JavaScript helper functions for pricing modal & family sync link
js_helpers = '''
function openPricingModal() {
  const m = document.getElementById('modal-pricing-plans');
  if (m) m.classList.add('active');
}
function closePricingModal() {
  const m = document.getElementById('modal-pricing-plans');
  if (m) m.classList.remove('active');
}
function shareFamilySyncLink() {
  const code = Math.floor(100000 + Math.random() * 900000);
  const text = encodeURIComponent("Namaskaram! Join Rahul & Snigdha Kalyanam Shagun Ledger on GiftVault with family sync code: " + code + ". Link: " + window.location.origin);
  window.open("https://wa.me/?text=" + text, "_blank");
}
'''

if 'function openPricingModal()' not in html:
    html = html.replace('function openCreateEventModal() {', js_helpers + '\nfunction openCreateEventModal() {')

# 6. Add i18n translations for new keys in English, Telugu, Hindi
te_translations_addition = '''    opt_rel_brother_in_law: "బావ / Brother-in-law",
    opt_rel_uncle: "బాబాయ్ / Uncle",
    opt_rel_fil: "మామ / Father-in-law",
    opt_rel_mat_uncle: "మేనమామ / Maternal Uncle",
    opt_rel_friend: "స్నేహితుడు / Friend",
    opt_rel_relative: "బంధువు / Relative",
    opt_rel_neighbor: "పొరుగువారు / Neighbor",
    cfg_photo_policy: "గిఫ్ట్ ఫోటో ప్రూఫ్ పాలసీ (ఫోటో సెట్టింగ్)",
    opt_photo_compulsory: "కంపల్సరీ (బంగారం & వస్తువులకు)",
    opt_photo_optional: "ఐచ్ఛికం (అన్ని గిఫ్ట్‌లకు)",
    opt_photo_off: "ఆఫ్ (అవసరం లేదు)",
    cfg_video_policy: "షార్ట్ వీడియో క్లిప్ పాలసీ (వీడియో సెట్టింగ్)",
    opt_video_optional: "ఐచ్ఛికం (షార్ట్ వీడియో / డ్రైవ్ లింక్)",
    opt_video_compulsory: "కంపల్సరీ (తప్పనిసరి)",
    opt_video_off: "ఆఫ్ (ఆపబడింది)",
    family_sync_title: "ఫ్యామిలీ సింక్ & మున్షీ రోల్స్",
    badge_cloud_live: "3 యాక్టివ్ డివైజ్‌లు",
    family_sync_desc: "రోల్ ఆధారిత అనుమతులతో (ఓనర్, మున్షీ, వ్యూయర్) ఒకేసారి బహుళ సభ్యుల నమోదు",
    role_owner: "ఓనర్",
    role_munshi: "మున్షీ / రికార్డర్",
    role_viewer: "ఫ్యామిలీ వ్యూయర్",
    invite_family_btn_title: "కుటుంబ సభ్యుడు లేదా మున్షీని ఆహ్వానించండి",
    invite_family_btn_desc: "వారి ఫోన్‌లో వెంటనే కనెక్ట్ అవ్వడానికి 6 అంకెల సింక్ లింక్ రూపొందించండి",
    btn_share_family_link: "ఫ్యామిలీ సింక్ లింక్ పంపండి (WhatsApp)",
    plans_modal_title: "రాయల్ శుభకార్య ప్లాన్‌లు",
    plans_modal_sub: "సరసమైన ఫంక్షన్ పాస్ లేదా అపరిమిత కుటుంబ లైఫ్‌టైమ్ యాక్సెస్",
    plan_badge_single: "సింగిల్ ఫంక్షన్",
    plan_single_title: "సింగిల్ ఈవెంట్ పాస్",
    plan_single_desc: "హల్దీ, బర్త్‌డే లేదా చిన్న శుభకార్యానికి సరిపోతుంది",
    plan_feat_1: "500 వరకు అతిథి ఎంట్రీలు",
    plan_feat_2: "ఫాస్ట్ వాయిస్ డిక్టేషన్",
    plan_feat_3: "వాట్సాప్ రసీదులు",
    plan_feat_4: "PDF & ఎక్సెల్ రిపోర్ట్‌లు",
    btn_choose_single: "సింగిల్ పాస్ ఎంచుకోండి",
    plan_badge_family: "అత్యంత ప్రజాదరణ",
    plan_family_title: "రాయల్ ఫ్యామిలీ లైఫ్‌టైమ్",
    plan_family_desc: "కుటుంబ వివాహాలు, గృహప్రవేశాలు & అన్ని ఫంక్షన్లు శాశ్వతంగా",
    plan_f_feat_1: "అపరిమిత ఈవెంట్‌లు & ఎంట్రీలు",
    plan_f_feat_2: "మల్టీ-డివైజ్ ఫ్యామిలీ సింక్ (3+ మున్షీలు)",
    plan_f_feat_3: "లైవ్ రిసెప్షన్ ఆడియో సౌండ్‌బాక్స్",
    plan_f_feat_4: "ఫోటో ప్రూఫ్ క్లౌడ్ స్టోరేజ్",
    plan_f_feat_5: "రుణ బాధ్యత (Reciprocity) మ్యాట్రిక్స్",
    btn_choose_family: "లైఫ్‌టైమ్ యాక్సెస్ అన్‌లాక్ చేయండి",
    plans_guarantee: "🔒 100% శుభప్రద హామీ • సురక్షిత క్లౌడ్ సింక్ • జీరో ప్రకటనలు",
    nav_plans_btn: "ప్లాన్‌లు (₹49)",
'''

en_translations_addition = '''    opt_rel_brother_in_law: "బావ / Brother-in-law",
    opt_rel_uncle: "బాబాయ్ / Uncle",
    opt_rel_fil: "మామ / Father-in-law",
    opt_rel_mat_uncle: "మేనమామ / Maternal Uncle",
    opt_rel_friend: "స్నేహితుడు / Friend",
    opt_rel_relative: "బంధువు / Relative",
    opt_rel_neighbor: "పొరుగువారు / Neighbor",
    cfg_photo_policy: "Gift Photo Proof Policy",
    opt_photo_compulsory: "Compulsory (Gold & Articles)",
    opt_photo_optional: "Optional (All Gifts)",
    opt_photo_off: "Off (Disabled)",
    cfg_video_policy: "Short Video / Clip Policy",
    opt_video_optional: "Optional (Short Video / Drive Link)",
    opt_video_compulsory: "Compulsory (Mandatory)",
    opt_video_off: "Off (Disabled)",
    family_sync_title: "Family Sync & Munshi Roles",
    badge_cloud_live: "3 ACTIVE DEVICES",
    family_sync_desc: "Simultaneous multi-member entry with role-based permissions (Owner, Munshi, Viewer)",
    role_owner: "OWNER",
    role_munshi: "MUNSHI / RECORDER",
    role_viewer: "FAMILY VIEWER",
    invite_family_btn_title: "Invite Family Member or Munshi",
    invite_family_btn_desc: "Generate a secure 6-digit sync link for instant joining on their smartphone",
    btn_share_family_link: "Share Family Sync Link (WhatsApp)",
    plans_modal_title: "Auspicious Celebration Plans",
    plans_modal_sub: "Affordable per-event pass or unlimited family lifetime access",
    plan_badge_single: "PER FUNCTION",
    plan_single_title: "Single Event Pass",
    plan_single_desc: "Perfect for Haldi, Birthday or Small Function",
    plan_feat_1: "Up to 500 Guest Entries",
    plan_feat_2: "Fast Voice Dictation",
    plan_feat_3: "WhatsApp Receipts",
    plan_feat_4: "PDF & Excel Reports",
    btn_choose_single: "Choose Single Pass",
    plan_badge_family: "MOST POPULAR",
    plan_family_title: "Royal Family Lifetime",
    plan_family_desc: "All family weddings, housewarmings & events forever",
    plan_f_feat_1: "Unlimited Events & Entries",
    plan_f_feat_2: "Multi-Device Family Sync (3+ Munshis)",
    plan_f_feat_3: "Live Reception Audio Soundbox",
    plan_f_feat_4: "Photo Proof Cloud Storage",
    plan_f_feat_5: "Reciprocity Debt Matrix",
    btn_choose_family: "Unlock Lifetime Access",
    plans_guarantee: "🔒 100% Auspicious Guarantee • Safe Cloud Sync • Zero Advertisements",
    nav_plans_btn: "Plans (₹49)",
'''

hi_translations_addition = '''    opt_rel_brother_in_law: "जीजाजी / साला (Brother-in-law)",
    opt_rel_uncle: "चाचाजी / ताऊजी (Uncle)",
    opt_rel_fil: "ससुरजी / फूफाजी (Father-in-law)",
    opt_rel_mat_uncle: "मामाजी (Maternal Uncle)",
    opt_rel_friend: "मित्र / दोस्त (Friend)",
    opt_rel_relative: "रिश्तेदार (Relative)",
    opt_rel_neighbor: "पड़ोसी (Neighbor)",
    cfg_photo_policy: "उपहार फोटो प्रमाण नीति (फोटो सेटिंग)",
    opt_photo_compulsory: "अनिवार्य (सोने और वस्तुओं के लिए)",
    opt_photo_optional: "वैकल्पिक (सभी उपहारों के लिए)",
    opt_photo_off: "बंद (जरूरत नहीं)",
    cfg_video_policy: "शॉर्ट वीडियो क्लिप नीति (वीडियो सेटिंग)",
    opt_video_optional: "वैकल्पिक (शॉर्ट वीडियो / ड्राइव लिंक)",
    opt_video_compulsory: "अनिवार्य (कंपलसरी)",
    opt_video_off: "बंद (ऑफ)",
    family_sync_title: "पारिवारिक सिंक और मुंशी भूमिकाएँ",
    badge_cloud_live: "3 सक्रिय डिवाइस",
    family_sync_desc: "भूमिका आधारित अनुमतियों (मालिक, मुंशी, दर्शक) के साथ एक साथ प्रविष्टि",
    role_owner: "मालिक (OWNER)",
    role_munshi: "मुंशी / रिकॉर्डर",
    role_viewer: "पारिवारिक दर्शक (VIEWER)",
    invite_family_btn_title: "परिवार के सदस्य या मुंशी को आमंत्रित करें",
    invite_family_btn_desc: "उनके फोन पर तुरंत जुड़ने के लिए 6-अंकीय सिंक लिंक बनाएं",
    btn_share_family_link: "पारिवारिक सिंक लिंक साझा करें (WhatsApp)",
    plans_modal_title: "शुभ उत्सव योजनाएं (Plans)",
    plans_modal_sub: "किफायती प्रति-समारोह पास या असीमित पारिवारिक लाइफटाइम एक्सेस",
    plan_badge_single: "प्रति समारोह",
    plan_single_title: "सिंगल इवेंट पास",
    plan_single_desc: "हल्दी, जन्मदिन या छोटे समारोह के लिए उत्तम",
    plan_feat_1: "500 मेहमानों तक प्रविष्टियां",
    plan_feat_2: "फास्ट वॉयस डिक्टेशन",
    plan_feat_3: "व्हाट्सएप रसीदें",
    plan_feat_4: "PDF और एक्सेल रिपोर्ट",
    btn_choose_single: "सिंगल पास चुनें",
    plan_badge_family: "सर्वाधिक लोकप्रिय",
    plan_family_title: "रॉयल फैमिली लाइफटाइम",
    plan_family_desc: "परिवार के सभी विवाह, गृह प्रवेश और समारोह हमेशा के लिए",
    plan_f_feat_1: "असीमित कार्यक्रम और प्रविष्टियां",
    plan_f_feat_2: "मल्टी-डिवाइस फैमिली सिंक (3+ मुंशी)",
    plan_f_feat_3: "लाइव रिसेप्शन ऑडियो साउंडबॉक्स",
    plan_f_feat_4: "फोटो प्रूफ क्लाउड स्टोरेज",
    plan_f_feat_5: "पारस्परिकता (Reciprocity) ऋण ट्रैकर",
    btn_choose_family: "लाइफटाइम एक्सेस अनलॉक करें",
    plans_guarantee: "🔒 100% शुभ गारंटी • सुरक्षित क्लाउड सिंक • शून्य विज्ञापन",
    nav_plans_btn: "योजनाएं (₹49)",
'''

if 'opt_rel_brother_in_law' not in html:
    html = html.replace('modal_event_create_desc: "Create an auspicious record', te_translations_addition + '    modal_event_create_desc: "Create an auspicious record')
    html = html.replace('modal_event_create_desc: "ఒక కొత్త వివాహం,', en_translations_addition + '    modal_event_create_desc: "ఒక కొత్త వివాహం,')
    html = html.replace('modal_event_create_desc: "एक नया विवाह,', hi_translations_addition + '    modal_event_create_desc: "एक नया विवाह,')

for path in target_files:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated: {path} ({len(html)} bytes)")

print("\nSuccessfully enriched and synchronized all targets with Family Sync, Media Policies, Relationship tags, and Pricing Pass!")
