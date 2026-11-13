/**
 * GiftVault Cultural Localization Engine
 * Default: 100% Pure English Everywhere
 */

window.GVI18n = {
  activeLang: 'en',

  en: {
    tagline: 'SACRED CELEBRATIONS • DIGITAL SHAGUN VAULT',
    heading: 'Every Sacred Celebration Deserves a <em>Royal Gift Vault</em>',
    subheading: 'The modern digital ledger for Indian celebrations. Seamlessly track gifts, shagun, and guest blessings with complete family privacy and instant reports.',
    navFeatures: 'Features',
    navDashboard: 'Dashboard',
    navGiftCounter: 'Gift Counter',
    navPricing: 'Pricing',
    navFaq: 'FAQ',
    btnSignIn: 'Sign In',
    btnGetStarted: 'Sign In to Family Vault',
    btnExploreDemo: 'Explore Live Demo',
    pillar1: 'Record Gifts & Shagun',
    pillar2: 'Family Collaboration',
    pillar3: '100% Secure & Private',
    pillar4: 'Reports & Backup',
    receptionDesk: 'Gift Entry Counter',
    guestDemo: 'Explore Live Demo',
    estimatorTitle: 'Live Celebration Shagun Estimator',
    guestsLabel: 'Expected Family Guests',
    avgBlessing: 'Average Shagun Envelope',
    estBlessings: 'Estimated Total Blessings'
  },

  te: {
    tagline: 'శుభారంభం • మంగళ కార్యం',
    heading: 'ప్రతి శుభకార్యానికి <em>డిజిటల్ చదివింపుల</em> ఖజానా',
    subheading: 'వివాహాలు, గృహప్రవేశాలు, సుల్తీ మరియు శుభకార్యాల చదివింపులను అత్యంత పవిత్రంగా, పారదర్శకంగా భద్రపరిచే ఆధునిక డిజిటల్ ఎర్ర పుస్తకం.',
    navFeatures: 'ఫీచర్లు',
    navDashboard: 'డ్యాష్‌బోర్డ్',
    navGiftCounter: 'చదివింపుల కౌంటర్',
    navPricing: 'ప్లాన్లు',
    navFaq: 'సందేహాలు',
    btnSignIn: 'సైన్ ఇన్',
    btnGetStarted: 'ప్రారంభించండి • సైన్ ఇన్',
    btnExploreDemo: 'లైవ్ డెమో పరిశీలించండి',
    pillar1: 'చదివింపులు & బహుమతుల నమోదు',
    pillar2: 'కుటుంబ సభ్యుల సమన్వయం',
    pillar3: '100% ప్రైవేట్ & సురక్షితం',
    pillar4: 'రిపోర్టులు & డౌన్‌లోడ్',
    receptionDesk: 'చదివింపుల కౌంటర్',
    guestDemo: 'గెస్ట్ డెమో మోడ్',
    estimatorTitle: 'లైవ్ శుభకార్య చదివింపుల అంచనా',
    guestsLabel: 'ఆహ్వానితుల సంఖ్య',
    avgBlessing: 'సగటు చదివింపు',
    estBlessings: 'అంచనా చదివింపుల మొత్తం'
  },

  hi: {
    tagline: 'शुभ आरंभ • मंगल कार्य',
    heading: 'हर मांगलिक कार्य के लिए <em>डिजिटल न्योता-शगुन</em> सिंहासन',
    subheading: 'विवाह, गृहप्रवेश, मुंडन एवं सभी पावन उत्सवों के शगुन को पूर्ण पारदर्शिता और पवित्रता से सहेजने का आधुनिक राजकोष।',
    navFeatures: 'विशेषताएं',
    navDashboard: 'डैशबोर्ड',
    navGiftCounter: 'शगुन काउंटर',
    navPricing: 'योजनाएं',
    navFaq: 'प्रश्नोत्तरी',
    btnSignIn: 'साइन इन',
    btnGetStarted: 'शुरुआत करें • साइन इन',
    btnExploreDemo: 'लाइव डेमो देखें',
    pillar1: 'शगुन व उपहार प्रविष्टि',
    pillar2: 'पारिवारिक सहयोग',
    pillar3: '100% सुरक्षित व निजी',
    pillar4: 'रिपोर्ट व बैकअप',
    receptionDesk: 'शगुन पटल प्रवेश',
    guestDemo: 'अतिथि डेमो मोड',
    estimatorTitle: 'लाइव उत्सव शगुन संगणक',
    guestsLabel: 'अतिथियों की संख्या',
    avgBlessing: 'औसत शगुन',
    estBlessings: 'अनुमानित कुल शगुन'
  },

  apply(lang) {
    this.activeLang = lang || 'en';
    const t = this[this.activeLang] || this.en;

    const tag = document.querySelector('.hero-tagline-text');
    if (tag) tag.innerText = t.tagline;

    const h1 = document.querySelector('.hero-heading, .hero-massive-heading');
    if (h1) h1.innerHTML = t.heading;

    const p = document.getElementById('hero-subtext');
    if (p) p.innerText = t.subheading;

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (t[key]) {
        el.innerText = t[key];
      }
    });
  }
};
