/**
 * GiftVault Munshi Fast Entry Desk
 * Speed-optimized blessing logging with Smart Voice Command Auto-Fill, 
 * City Autocomplete Suggestions, and Physical Gift Photo Proof Capture
 */

window.GVMunshiDesk = {
  currentPhotoData: null,
  cameraStream: null,
  activeRecognition: null,

  // Curated list of Andhra Pradesh & Telangana and prominent Indian cities
  DEFAULT_CITIES: [
    'Chirala', 'Bapatla', 'Guntur', 'Vijayawada', 'Hyderabad', 
    'Visakhapatnam', 'Tirupati', 'Rajahmundry', 'Kakinada', 'Nellore', 
    'Ongole', 'Tenali', 'Kurnool', 'Anantapur', 'Kadapa', 'Eluru', 
    'Warangal', 'Nizamabad', 'Khammam', 'Karimnagar', 'Nandyal', 
    'Machilipatnam', 'Narsaraopet', 'Mangalagiri', 'Vetapalem', 'Ponnur',
    'Tadepalligudem', 'Tanuku', 'Bhimavaram', 'Palakollu', 'Gudivada',
    'Kavali', 'Kandukur', 'Markapur', 'Chittoor', 'Madanapalle',
    'Srikakulam', 'Vizianagaram', 'Proddatur', 'Hindupur', 'Dharmavaram',
    'Adoni', 'Yemmiganur', 'Miryalaguda', 'Suryapet', 'Nalgonda',
    'Siddipet', 'Mancherial', 'Ramagundam', 'Mahabubnagar',
    'Bengaluru', 'Chennai', 'Mumbai', 'Delhi', 'Pune', 'Kolkata'
  ],

  // -------------------------------------------------------------
  // 1. CITY AUTOCOMPLETE & QUICK SUGGESTIONS
  // -------------------------------------------------------------
  getAllCities() {
    const list = [...this.DEFAULT_CITIES];
    const event = window.GVStore ? window.GVStore.getActiveEvent() : null;
    if (event && event.entries) {
      event.entries.forEach(e => {
        if (e.place && !list.includes(e.place)) {
          list.unshift(e.place);
        }
      });
    }
    return list;
  },

  handleCityInput(val) {
    const query = (val || '').trim().toLowerCase();
    const box = document.getElementById('entry-city-suggestions');
    if (!box) return;

    const all = this.getAllCities();
    const matches = query ? all.filter(c => c.toLowerCase().includes(query)) : all.slice(0, 8);

    if (matches.length === 0) {
      box.style.display = 'none';
      return;
    }

    box.innerHTML = `
      <div style="padding: 6px 12px; font-size: 11px; font-weight: 800; color: #9E1B32; background: #FAF7F2; border-bottom: 1px solid rgba(212,175,55,0.3); text-transform: uppercase; font-family: 'Sen', sans-serif;">
        📍 Select City / Village (${matches.length})
      </div>
      ${matches.slice(0, 10).map(city => `
        <div onclick="window.GVMunshiDesk.selectCity('${city}')" style="padding: 8px 14px; font-size: 13px; font-family: 'Sen', sans-serif; font-weight: 600; color: #37000A; cursor: pointer; border-bottom: 1px solid #F6F2EC; display: flex; align-items: center; justify-content: space-between; transition: all 0.15s ease;" onmouseenter="this.style.background='#FDF2F4'; this.style.color='#9E1B32';" onmouseleave="this.style.background='#FFFFFF'; this.style.color='#37000A';">
          <span>${city}</span>
          <span style="font-size: 11px; color: #8A7E72;">Select ↵</span>
        </div>
      `).join('')}
    `;
    box.style.display = 'block';

    // Auto-close when clicking outside
    const outsideClickListener = (e) => {
      const cityContainer = document.getElementById('entry-city');
      if (box && !box.contains(e.target) && e.target !== cityContainer) {
        box.style.display = 'none';
        document.removeEventListener('click', outsideClickListener);
      }
    };
    setTimeout(() => document.addEventListener('click', outsideClickListener), 10);
  },

  selectCity(cityName) {
    const field = document.getElementById('entry-city');
    const box = document.getElementById('entry-city-suggestions');
    if (field) {
      field.value = cityName;
      field.dispatchEvent(new Event('input', { bubbles: true }));
      this.highlightField(field);
    }
    if (box) box.style.display = 'none';
  },

  // -------------------------------------------------------------
  // 2. SMART VOICE COMMAND AUTO-FILL ENGINE
  // -------------------------------------------------------------
  startSmartVoiceEntry() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const banner = document.getElementById('smart-voice-listening-banner');
    const transcriptEl = document.getElementById('smart-voice-live-transcript');

    if (!SpeechRecognition) {
      window.GVApp.showToast('🎙️ ఈ బ్రౌజర్‌లో వాయిస్ రికగ్నిషన్ సపోర్ట్ లేదు. దయచేసి టైప్ చేయండి.', 'gold');
      return;
    }

    try {
      if (this.activeRecognition) {
        this.activeRecognition.stop();
      }

      const recognition = new SpeechRecognition();
      this.activeRecognition = recognition;
      recognition.continuous = false;
      recognition.interimResults = true;
      recognition.lang = (window.GVStore && window.GVStore.state.language === 'te') ? 'te-IN' : 'en-IN';

      if (banner) banner.style.display = 'block';
      if (transcriptEl) transcriptEl.innerHTML = '<span style="color:#8A7E72;">[మాట్లాడండి: పేరు, ఊరు, మొత్తం, క్యాష్ లేదా యూపీఐ...]</span>';

      window.GVApp.showToast('🎙️ స్మార్ట్ వాయిస్ యాక్టివ్ అయింది. పూర్తి వివరాలు ఒకేసారి మాట్లాడండి!', 'gold');

      recognition.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
          transcript += event.results[i][0].transcript;
        }
        transcript = transcript.trim();
        if (transcriptEl && transcript) {
          transcriptEl.innerHTML = `🎙️ <em>"${transcript}"</em>`;
        }
      };

      recognition.onerror = () => {
        if (banner) banner.style.display = 'none';
        window.GVApp.showToast('🎙️ వాయిస్ వినపడలేదు, దయచేసి మళ్లీ ప్రయత్నించండి.', 'gold');
      };

      recognition.onend = () => {
        if (banner) banner.style.display = 'none';
        const finalSpoken = transcriptEl ? transcriptEl.innerText.replace(/^[🎙️\s*"']+|["'\s]+$/g, '') : '';
        if (finalSpoken && !finalSpoken.includes('[మాట్లాడండి')) {
          this.parseAndApplyVoiceCommand(finalSpoken);
        }
      };

      recognition.start();
    } catch (err) {
      if (banner) banner.style.display = 'none';
      window.GVApp.showToast('🎙️ మైక్ కనెక్ట్ కాలేదు. దయచేసి టైప్ చేయండి.', 'gold');
    }
  },

  stopVoiceRecognition() {
    if (this.activeRecognition) {
      this.activeRecognition.stop();
      this.activeRecognition = null;
    }
    const banner = document.getElementById('smart-voice-listening-banner');
    if (banner) banner.style.display = 'none';
  },

  parseSmartVoiceCommand(text) {
    let workingText = text;
    const result = {
      name: '',
      city: '',
      amount: null,
      mode: 'Cash',
      relation: '',
      phone: ''
    };

    // 1. Phone Extraction (10-digit number)
    const phoneMatch = workingText.match(/\b([6-9]\d{9})\b/);
    if (phoneMatch) {
      result.phone = phoneMatch[1];
      workingText = workingText.replace(phoneMatch[0], ' ');
    }

    // 2. Amount Extraction (Numbers, e.g. 5000, 5116, 15000, 10116)
    const amtMatch = workingText.match(/(?:₹|rs\.?|rupees|రూపాయలు)?\s*(\d{2,7})\s*(?:rupees|రూపాయలు|rs|\/-)?/i);
    if (amtMatch) {
      result.amount = parseInt(amtMatch[1], 10);
      workingText = workingText.replace(amtMatch[0], ' ');
    }

    // 3. Payment Mode Extraction
    if (/\b(upi|online|phonepe|gpay|యూపీఐ|ఆన్‌లైన్)\b/i.test(workingText)) {
      result.mode = 'UPI';
      workingText = workingText.replace(/\b(upi|online|phonepe|gpay|యూపీఐ|ఆన్‌లైన్)\b/ig, ' ');
    } else if (/\b(gold|బంగారం|గోల్డ్)\b/i.test(workingText)) {
      result.mode = 'Gold';
      workingText = workingText.replace(/\b(gold|బంగారం|గోల్డ్)\b/ig, ' ');
    } else if (/\b(silver|వెండి|సిల్వర్)\b/i.test(workingText)) {
      result.mode = 'Silver';
      workingText = workingText.replace(/\b(silver|వెండి|సిల్వర్)\b/ig, ' ');
    } else {
      workingText = workingText.replace(/\b(cash|నగదు|క్యాష్)\b/ig, ' ');
    }

    // 4. City Extraction
    const allCities = this.getAllCities();
    for (const c of allCities) {
      const reg = new RegExp(`\\b${c}\\b`, 'i');
      if (reg.test(workingText)) {
        result.city = c;
        workingText = workingText.replace(reg, ' ');
        break;
      }
    }

    // 5. Relationship Extraction
    if (/మేనమామ|మావయ్య|maternal uncle/i.test(workingText)) {
      result.relation = 'Maternal Uncle / Maternal Uncle';
      workingText = workingText.replace(/మేనమామ|మావయ్య|maternal uncle/ig, ' ');
    } else if (/బాబాయ్|పెదనాన్న|చిన్నాన్న|uncle/i.test(workingText)) {
      result.relation = 'Uncle / Uncle';
      workingText = workingText.replace(/బాబాయ్|పెదనాన్న|చిన్నాన్న|uncle/ig, ' ');
    } else if (/బావ|బావమరిది|brother-in-law/i.test(workingText)) {
      result.relation = 'Brother-in-law / Brother-in-law';
      workingText = workingText.replace(/బావ|బావమరిది|brother-in-law/ig, ' ');
    } else if (/మామగారు|father-in-law/i.test(workingText)) {
      result.relation = 'Father-in-law / Father-in-law';
      workingText = workingText.replace(/మామగారు|father-in-law/ig, ' ');
    } else if (/స్నేహితుడు|friend/i.test(workingText)) {
      result.relation = 'Friend / Friend';
      workingText = workingText.replace(/స్నేహితుడు|friend/ig, ' ');
    } else if (/బంధువు|relative/i.test(workingText)) {
      result.relation = 'Relative / Relative';
      workingText = workingText.replace(/బంధువు|relative/ig, ' ');
    }

    // 6. Guest Name Extraction (Clean up leftover filler words)
    workingText = workingText.replace(/\b(గారు|గారి|నుంచి|from|and|చదివింపు|రూపాయలు|rupees|rs)\b/ig, ' ');
    result.name = workingText.replace(/\s+/g, ' ').trim().replace(/^[,.-]+|[,.-]+$/g, '');

    return result;
  },

  parseAndApplyVoiceCommand(transcript) {
    const parsed = this.parseSmartVoiceCommand(transcript);
    let autoFilledCount = 0;

    // Apply Name
    const nameField = document.getElementById('entry-name');
    if (parsed.name && nameField) {
      nameField.value = parsed.name;
      nameField.dispatchEvent(new Event('input', { bubbles: true }));
      this.highlightField(nameField);
      autoFilledCount++;
    }

    // Apply City
    const cityField = document.getElementById('entry-city');
    if (parsed.city && cityField) {
      cityField.value = parsed.city;
      cityField.dispatchEvent(new Event('input', { bubbles: true }));
      this.highlightField(cityField);
      autoFilledCount++;
    }

    // Apply Amount
    const amtField = document.getElementById('entry-amount');
    if (parsed.amount && amtField) {
      amtField.value = parsed.amount;
      amtField.dispatchEvent(new Event('input', { bubbles: true }));
      this.highlightField(amtField);
      autoFilledCount++;
    }

    // Apply Mode
    if (parsed.mode) {
      this.selectMode(parsed.mode);
      const modeBtn = Array.from(document.querySelectorAll('.mode-select-btn')).find(b => b.innerText.trim() === parsed.mode);
      if (modeBtn) this.highlightField(modeBtn);
    }

    // Apply Relation
    const relField = document.getElementById('entry-relation');
    if (parsed.relation && relField) {
      relField.value = parsed.relation;
      this.highlightField(relField);
      autoFilledCount++;
    }

    // Apply Phone
    const phoneField = document.getElementById('entry-phone');
    if (parsed.phone && phoneField) {
      phoneField.value = parsed.phone;
      this.highlightField(phoneField);
      autoFilledCount++;
    }

    this.playTempleChime();
    window.GVApp.showToast(`✨ స్మార్ట్ వాయిస్: ${autoFilledCount} వివరాలు ఆటోమేటిక్‌గా నింపబడ్డాయి!`, 'emerald');
  },

  highlightField(el) {
    if (!el) return;
    el.style.transition = 'all 0.3s ease';
    el.style.borderColor = '#10B981';
    el.style.boxShadow = '0 0 14px rgba(16, 185, 129, 0.45)';
    setTimeout(() => {
      el.style.borderColor = '';
      el.style.boxShadow = '';
    }, 1200);
  },

  // -------------------------------------------------------------
  // 3. PHYSICAL GIFT / ENVELOPE PHOTO PROOF CAPTURE
  // -------------------------------------------------------------
  openCameraModal() {
    const modal = document.getElementById('modal-live-camera');
    const video = document.getElementById('camera-video-feed');
    const loading = document.getElementById('camera-loading-indicator');

    if (!modal || !video) return;
    modal.style.display = 'flex';

    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      if (loading) loading.style.display = 'flex';
      navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment', width: { ideal: 1280 }, height: { ideal: 720 } } })
        .then(stream => {
          this.cameraStream = stream;
          video.srcObject = stream;
          if (loading) loading.style.display = 'none';
        })
        .catch(err => {
          if (loading) loading.style.display = 'none';
          this.closeCameraModal();
          window.GVApp.showToast('📷 కెమెరా అందుబాటులో లేదు. ఫైల్ అప్‌లోడ్ ద్వారా ఫోటో ఎంచుకోండి.', 'gold');
          const fileInput = document.getElementById('entry-photo-file-input');
          if (fileInput) fileInput.click();
        });
    } else {
      this.closeCameraModal();
      window.GVApp.showToast('📷 బ్రౌజర్ కెమెరాను అనుమతించలేదు. ఫైల్ అప్‌లోడ్ చేయండి.', 'gold');
      const fileInput = document.getElementById('entry-photo-file-input');
      if (fileInput) fileInput.click();
    }
  },

  closeCameraModal() {
    const modal = document.getElementById('modal-live-camera');
    if (modal) modal.style.display = 'none';
    if (this.cameraStream) {
      this.cameraStream.getTracks().forEach(t => t.stop());
      this.cameraStream = null;
    }
  },

  snapCameraPhoto() {
    const video = document.getElementById('camera-video-feed');
    const canvas = document.getElementById('camera-snap-canvas');
    if (!video || !canvas) return;

    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const dataUrl = canvas.toDataURL('image/jpeg', 0.85);
    this.setPhotoData(dataUrl);
    this.closeCameraModal();
    window.GVApp.showToast('📸 గిఫ్ట్ ఫోటో ప్రూఫ్ జతచేయబడింది!', 'emerald');
  },

  handleFileUpload(event) {
    const file = event.target.files && event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      this.setPhotoData(e.target.result);
      window.GVApp.showToast('📸 గిఫ్ట్ ఫోటో ప్రూఫ్ అప్‌లోడ్ అయింది!', 'emerald');
    };
    reader.readAsDataURL(file);
  },

  setPhotoData(dataUrl) {
    this.currentPhotoData = dataUrl;
    const wrap = document.getElementById('entry-photo-preview-wrap');
    const img = document.getElementById('entry-photo-preview-img');
    const badge = document.getElementById('photo-attached-badge');

    if (img) img.src = dataUrl;
    if (wrap) wrap.style.display = 'flex';
    if (badge) badge.style.display = 'inline-block';
  },

  removePhoto() {
    this.currentPhotoData = null;
    const wrap = document.getElementById('entry-photo-preview-wrap');
    const img = document.getElementById('entry-photo-preview-img');
    const badge = document.getElementById('photo-attached-badge');
    const fileInput = document.getElementById('entry-photo-file-input');

    if (img) img.src = '';
    if (wrap) wrap.style.display = 'none';
    if (badge) badge.style.display = 'none';
    if (fileInput) fileInput.value = '';
  },

  // -------------------------------------------------------------
  // 4. LEGACY SINGLE-FIELD VOICE DICTATION
  // -------------------------------------------------------------
  startVoiceDictation() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const micBtn = document.getElementById('btn-entry-mic');
    const nameField = document.getElementById('entry-name');

    if (!SpeechRecognition) {
      window.GVApp.showToast('🎙️ మీ బ్రౌజర్‌లో వాయిస్ రికగ్నిషన్ సపోర్ట్ లేదు. దయచేసి టైప్ చేయండి.', 'gold');
      if (nameField) nameField.focus();
      return;
    }

    try {
      const recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = true;
      recognition.lang = (window.GVStore && window.GVStore.state.language === 'te') ? 'te-IN' : 'en-IN';

      if (micBtn) {
        micBtn.style.background = '#FF1F3D';
        micBtn.style.color = '#FFFFFF';
        micBtn.style.borderColor = '#FFFFFF';
        micBtn.innerHTML = '<span style="color:#FFF;">●</span> Listening...';
      }
      window.GVApp.showToast('🎙️ మైక్ ఆన్ అయింది. అతిథి పేరు మాట్లాడండి...', 'gold');

      recognition.onresult = (event) => {
        let transcript = '';
        for (let i = event.resultIndex; i < event.results.length; ++i) {
          transcript += event.results[i][0].transcript;
        }
        transcript = transcript.trim();
        if (transcript && nameField) {
          nameField.value = transcript;
          nameField.dispatchEvent(new Event('input', { bubbles: true }));
        }
      };

      recognition.onerror = () => {
        this.resetMicBtn(micBtn);
        window.GVApp.showToast('🎙️ మైక్ వినలేదు, మళ్లీ ప్రయత్నించండి లేదా నేరుగా టైప్ చేయండి.', 'gold');
      };

      recognition.onend = () => {
        this.resetMicBtn(micBtn);
        if (nameField && nameField.value) {
          this.highlightField(nameField);
          window.GVApp.showToast('✓ అతిథి పేరు నమోదు చేయబడింది!', 'emerald');
        }
      };

      recognition.start();
    } catch (err) {
      this.resetMicBtn(micBtn);
      window.GVApp.showToast('🎙️ మైక్ కనెక్ట్ కాలేదు. దయచేసి నేరుగా టైప్ చేయండి.', 'gold');
    }
  },

  resetMicBtn(micBtn) {
    if (!micBtn) return;
    micBtn.style.background = '#37000A';
    micBtn.style.color = '#D4AF37';
    micBtn.style.borderColor = '#D4AF37';
    micBtn.innerHTML = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2.2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg> <span>Mic</span>';
  },

  // -------------------------------------------------------------
  // 5. AUDIO & PRESET AMOUNT HELPERS
  // -------------------------------------------------------------
  selectMode(mode, btn) {
    window.GVStore.setState({ selectedMode: mode });
    document.querySelectorAll('.mode-select-btn').forEach(b => {
      b.classList.remove('active');
      b.style.borderColor = 'rgba(62,78,80,0.2)';
      b.style.color = '#37000A';
      b.style.background = '#FAF7F2';
    });
    const targetBtn = btn || Array.from(document.querySelectorAll('.mode-select-btn')).find(b => b.innerText.trim() === mode);
    if (targetBtn) {
      targetBtn.classList.add('active');
      targetBtn.style.borderColor = '#D4AF37';
      targetBtn.style.color = '#FFFFFF';
      targetBtn.style.background = '#37000A';
    }
  },

  addOneRupeeCoin() {
    const field = document.getElementById('entry-amount');
    if (!field) return;
    const current = parseInt(field.value, 10) || 0;
    field.value = current + 1;
    this.highlightField(field);
    window.GVApp.showToast('🪙 +₹1 Auspicious Coin Added', 'gold');
  },

  applyPresetAmount(val) {
    const field = document.getElementById('entry-amount');
    if (field) {
      field.value = val;
      this.highlightField(field);
    }
  },

  playTempleChime() {
    if (window.GVStore.state.isSoundboxMuted) return;
    try {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (!AudioCtx) return;
      const ctx = new AudioCtx();
      const now = ctx.currentTime;

      // Harmonic D5 + A5 Chime
      const osc1 = ctx.createOscillator();
      const gain1 = ctx.createGain();
      osc1.frequency.setValueAtTime(587.33, now); // D5
      gain1.gain.setValueAtTime(0.3, now);
      gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.8);
      osc1.connect(gain1);
      gain1.connect(ctx.destination);
      osc1.start(now);
      osc1.stop(now + 0.8);

      const osc2 = ctx.createOscillator();
      const gain2 = ctx.createGain();
      osc2.frequency.setValueAtTime(880.00, now + 0.08); // A5
      gain2.gain.setValueAtTime(0.2, now + 0.08);
      gain2.gain.exponentialRampToValueAtTime(0.001, now + 0.9);
      osc2.connect(gain2);
      gain2.connect(ctx.destination);
      osc2.start(now + 0.08);
      osc2.stop(now + 0.9);
    } catch (e) {
      // Audio blocked until user interaction
    }
  },

  // -------------------------------------------------------------
  // 6. FORM SUBMISSION WITH PHOTO PROOF STORAGE
  // -------------------------------------------------------------
  submit(e) {
    e.preventDefault();
    const event = window.GVStore.getActiveEvent();
    if (!event) return;

    const name = document.getElementById('entry-name').value.trim();
    const city = document.getElementById('entry-city').value.trim() || 'Chirala';
    const rel = document.getElementById('entry-relation').value;
    const amt = parseInt(document.getElementById('entry-amount').value, 10) || 0;
    const phone = document.getElementById('entry-phone').value.trim();
    const mode = window.GVStore.state.selectedMode || 'Cash';
    const photo = this.currentPhotoData || null;

    const nextNum = (event.entries ? event.entries.length : 0) + 1;
    const sno = `#GV-${100 + nextNum}`;

    const newEntry = {
      sno,
      name,
      place: city,
      relation: rel,
      mode,
      amount: amt,
      phone,
      photo,
      recorder: 'Suresh (Desk 1)'
    };

    if (!event.entries) event.entries = [];
    event.entries.push(newEntry);
    event.totalBlessings = (event.totalBlessings || 0) + amt;
    event.envelopesCount = event.entries.length;

    const allEvents = window.GVStore.state.events;
    allEvents[event.id] = event;

    window.GVRepository.save(allEvents);
    window.GVStore.setState({ events: allEvents }, 'ENTRY_ADDED');

    // Reset Form
    document.getElementById('entry-name').value = '';
    document.getElementById('entry-amount').value = '';
    this.removePhoto();
    document.getElementById('entry-name').focus();

    // Sound and Toast
    this.playTempleChime();
    window.GVApp.showToast(`✓ ${name} గారి చదివింపు (${sno} - ₹${amt.toLocaleString('en-IN')}${photo ? ' • 📸 ఫోటో ప్రూఫ్‌తో' : ''}) నమోదైంది!`, 'gold');
  }
};
