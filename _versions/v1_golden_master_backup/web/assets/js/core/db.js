/**
 * GiftVault Database Repository
 * Data persistence engine with schema versioning & integrity validation
 */

const STORAGE_KEY = 'GV_EVENTS_DATABASE_V1';

const SEED_EVENTS = {
  'event-wedding': {
    id: 'event-wedding',
    title: 'Rahul & Snigdha Kalyanam (రాయల్ వివాహం)',
    type: 'Wedding',
    date: '2026-11-20',
    venue: 'A1 Convention Centre, Vijayawada',
    guestsCount: 450,
    totalBlessings: 842116,
    totalExpenses: 415000,
    goldGrams: 42.5,
    silverGrams: 550,
    envelopesCount: 4,
    entries: [
      { sno: '#GV-101', name: 'K. Venkata Rao Garu', relation: 'బావ / Brother-in-law', place: 'Vijayawada', mode: 'UPI', amount: 10116, phone: '+919848011223', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-102', name: 'M. Subba Reddy Garu', relation: 'మామ / Father-in-law', place: 'Guntur', mode: 'Cash', amount: 25116, phone: '+919848022334', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-103', name: 'T. Suresh Sharma', relation: 'స్నేహితుడు / Friend', place: 'Hyderabad', mode: 'Cash', amount: 5116, phone: '+919848033445', recorder: 'Ramesh (Desk 2)' },
      { sno: '#GV-104', name: 'V. Krishna Murthy Garu', relation: 'బాబాయ్ / Uncle', place: 'Tenali', mode: 'Gold', amount: 45000, phone: '+919848044556', recorder: 'Suresh (Desk 1)' }
    ]
  },
  'event-housewarming': {
    id: 'event-housewarming',
    title: 'Sri Nilayam Griha Pravesham (గృహప్రవేశం)',
    type: 'Housewarming',
    date: '2026-12-10',
    venue: 'Sri Nilayam, Amaravati Township',
    guestsCount: 300,
    totalBlessings: 326000,
    totalExpenses: 180000,
    goldGrams: 15,
    silverGrams: 200,
    envelopesCount: 3,
    entries: [
      { sno: '#GV-101', name: 'Ch. Venugopal Garu', relation: 'బావ / Brother-in-law', place: 'Vijayawada', mode: 'UPI', amount: 11116, phone: '+919848055667', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-102', name: 'N. Surya Narayana', relation: 'పొరుగువారు / Neighbor', place: 'Mangalagiri', mode: 'Cash', amount: 5116, phone: '+919848066778', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-103', name: 'P. Satyanarayana', relation: 'బాబాయ్ / Uncle', place: 'Guntur', mode: 'Cash', amount: 10116, phone: '+919848077889', recorder: 'Suresh (Desk 1)' }
    ]
  },
  'event-halfsaree': {
    id: 'event-halfsaree',
    title: 'Sahithi Ritu Kala Samskara Kaaryam (లంగా వోణీల వేడుక)',
    type: 'HalfSaree',
    date: '2027-01-08',
    venue: 'Annapurna Kalyana Mandapam, Guntur',
    guestsCount: 250,
    totalBlessings: 215000,
    totalExpenses: 120000,
    goldGrams: 20,
    silverGrams: 300,
    envelopesCount: 3,
    entries: [
      { sno: '#GV-101', name: 'Y. Koteswara Rao Garu', relation: 'తాతయ్య / Grandfather', place: 'Tenali', mode: 'Cash', amount: 21116, phone: '+919848088990', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-102', name: 'V. Radhika Devi', relation: 'మేనత్త / Aunt', place: 'Vijayawada', mode: 'Gold', amount: 15116, phone: '+919848099001', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-103', name: 'K. Haritha', relation: 'స్నేహితుడు / Friend', place: 'Eluru', mode: 'UPI', amount: 5116, phone: '+919848012345', recorder: 'Suresh (Desk 1)' }
    ]
  },
  'event-khatna': {
    id: 'event-khatna',
    title: 'Zayan Khatna & Sunnat Celebration (సుల్తీ / ఖత్నా వేడుక)',
    type: 'Khatna',
    role: 'Boy',
    date: '2027-02-14',
    venue: 'Royal Palace Function Hall, Guntur',
    guestsCount: 400,
    totalBlessings: 312116,
    totalExpenses: 150000,
    goldGrams: 12.0,
    silverGrams: 250,
    envelopesCount: 3,
    entries: [
      { sno: '#GV-101', name: 'Mohammed Rafiq (Chirala)', relation: 'మేనమామ / Khala', place: 'Chirala', mode: 'Cash', amount: 25116, phone: '+919848077112', recorder: 'Ibrahim (Desk 1)' },
      { sno: '#GV-102', name: 'Abdul Kareem Garu', relation: 'బాబాయ్ / Chacha', place: 'Guntur', mode: 'UPI', amount: 11116, phone: '+919848077113', recorder: 'Ibrahim (Desk 1)' },
      { sno: '#GV-103', name: 'Syed Mansoor', relation: 'స్నేహితుడు / Dost', place: 'Vijayawada', mode: 'Cash', amount: 5116, phone: '+919848077114', recorder: 'Ibrahim (Desk 1)' }
    ]
  },
  'event-chirala-tonsure': {
    id: 'event-chirala-tonsure',
    title: 'Advait Tonsure & Haircut (కేశఖండన / పుట్టెంటకలు)',
    type: 'Tonsure',
    date: '2027-01-15',
    venue: 'Chirala Beach Shore Mandapam, Bapatla',
    guestsCount: 350,
    totalBlessings: 83831,
    totalExpenses: 28000,
    goldGrams: 10,
    silverGrams: 120,
    envelopesCount: 8,
    entries: [
      { sno: '#GV-101', name: 'Mastan Rao Garu (Chirala)', relation: 'Maternal Uncle / మేనమామ', place: 'Chirala', mode: 'Cash', amount: 15117, phone: '+919848099881', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-102', name: 'S. Ramana Murthy', relation: 'Uncle / బాబాయ్', place: 'Vetapalem', mode: 'UPI', amount: 11116, phone: '+919848099882', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-103', name: 'D. Srinivas Garu', relation: 'Friend / స్నేహితుడు', place: 'Bapatla', mode: 'Cash', amount: 10116, phone: '+919848099883', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-104', name: 'Kondaveeti Anji Reddy Garu', relation: 'Relative / బంధువు', place: 'Karamchedu', mode: 'Cash', amount: 5116, phone: '+919848099884', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-105', name: 'P. Venkata Lakshmi Devi', relation: 'Aunt / మేనత్త', place: 'Bapatla', mode: 'Cash', amount: 5116, phone: '+919848099885', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-106', name: 'Dr. K. Ramesh Babu', relation: 'Family Doctor / శ్రేయోభిలాషి', place: 'Guntur', mode: 'UPI', amount: 10116, phone: '+919848099886', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-107', name: 'Ch. Subba Rao Garu', relation: 'Grandfather / తాతయ్య', place: 'Chirala', mode: 'Cash', amount: 25116, phone: '+919848099887', recorder: 'Suresh (Desk 1)' },
      { sno: '#GV-108', name: 'G. Srinivasulu', relation: 'Neighbor / పొరుగువారు', place: 'Vetapalem', mode: 'Cash', amount: 2116, phone: '+919848099888', recorder: 'Suresh (Desk 1)' }
    ]
  }
};

window.GVRepository = {
  load() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) {
        const parsed = JSON.parse(raw);
        if (parsed && typeof parsed === 'object' && Object.keys(parsed).length > 0) {
          return parsed;
        }
      }
    } catch (e) {
      console.warn('Failed to parse storage, using seeds:', e);
    }
    return JSON.parse(JSON.stringify(SEED_EVENTS));
  },

  save(eventsMap) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(eventsMap));
    } catch (e) {
      console.error('Storage quota exceeded or unavailable:', e);
    }
  }
};
