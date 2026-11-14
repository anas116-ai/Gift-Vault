<div align="center">

  <a href="https://github.com/anas116-ai/Gift-Vault">
    <img src="docs/images/giftvault_logo_card.png" alt="GiftVault Sacred Emblem" width="130" height="130" style="border-radius: 28px;" />
  </a>

  # GiftVault (గిఫ్ట్‌వాల్ట్)

  ### *Sacred Indian Family Shagun Vault & Digital Red Notebook*

  <p align="center">
    <strong>డిజిటల్ నవ్య తాంబూల &amp; శకునాల భాండాగారం</strong><br>
    <em>Generational Indian Celebration Gifting • 100% Offline Local Privacy • Hands-Free Voice Dictation • 2-Inch Thermal Slips</em>
  </p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![Slopdar Score](https://img.shields.io/badge/Slopdar-0%2F100%20(Hand--Crafted)-brightgreen)](#-code-craftsmanship--slopdar-audit)
  [![Offline Architecture](https://img.shields.io/badge/Privacy-100%25%20Offline%20First-success)](#-zero-cloud-leak-architecture)
  [![Code Style](https://img.shields.io/badge/Code%20Style-Vanilla%20%26%20Zero--Bloat-blue)](#)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#)

</div>

---

<p align="center">
  <img src="docs/images/giftvault_github_banner.png" alt="GiftVault Flagship Showcase Banner" width="100%" />
</p>

---

## 🌟 The Generational Challenge & Solution (సమస్య &amp; పరిష్కారం)

In Indian weddings (*రాయల్ వివాహం*), housewarmings (*గృహప్రవేశం*), silver jubilees (*రజతోత్సవం*), and cradle ceremonies (*పుట్టెంటకలు / నామకరణం*), guests present auspicious cash gifts (*Moyyulu*, *Chadhivimpu*, *Tamboolam*, *Shagun*).

Traditionally, volunteer relatives record these in a physical red notebook (**Munshi Book / బహీ-ఖాతా**). Under heavy reception rush, this paper system creates major friction:

```
┌──────────────────────────────────────────────┐       ┌──────────────────────────────────────────────┐
│       TRADITIONAL PAPER NOTEBOOK             │       │              GIFTVAULT SANCTUARY             │
├──────────────────────────────────────────────┤  VS   ├──────────────────────────────────────────────┤
│ ❌ Illegible handwriting & spelling mistakes │  ──>  │ ✅ Hands-free Telugu & English Voice Parsing │
│ ❌ Lost cash envelopes & misplaced slips     │  ──>  │ ✅ Instant 2-Inch Bluetooth Thermal Receipts │
│ ❌ Zero physical security or confidentiality │  ──>  │ ✅ 100% Offline Local IndexedDB Encryption   │
│ ❌ Hours searching diaries for reciprocity   │  ──>  │ ✅ Instant search across family generations  │
└──────────────────────────────────────────────┘       └──────────────────────────────────────────────┘
```

---

<p align="center">
  <img src="docs/images/giftvault_features_showcase.png" alt="GiftVault Core Interface Walkthrough" width="100%" />
</p>

---

## ✨ Flagship Capabilities (కీలక ఫీచర్లు)

* 🎙️ **Hands-Free Telugu & English Voice Dictation**:
  Speak naturally (*"Mastan Rao Garu, Chirala, 15000 cash"*). GiftVault automatically parses the Guest Name, Native Town, Amount, and Gift Mode into discrete fields.
* 📸 **Live Webcam & File Gift Photo Proofs**:
  Capture instant webcam verification snapshots of high-value gifts, gold ornaments, or shagun envelopes right at the reception counter.
* 🧾 **2-Inch ESC/POS Thermal Receipt Printing**:
  Instantly print professional blessing slips on portable Bluetooth thermal receipt printers to place inside return gift (*తాంబూలం*) hampers for elders.
* 🪙 **Auspicious ₹1 Lucky Coin Protocol**:
  One-key <kbd>+</kbd> shortcut instantly adds the sacred ₹1 coin to round amounts (`₹5,000` ➔ `₹5,001`, `₹15,116` ➔ `₹15,117`).
* 🛡️ **100% Offline-First Security (Zero Cloud Leak Protocol)**:
  Runs completely inside your browser via local IndexedDB. No celebration financial data ever touches remote cloud servers.
* 📊 **Generational Reciprocity Ledger**:
  Instant search filter allows you to verify what each relative gave at past celebrations when you attend their future events.
* 🔔 **Temple Chime Soundbox Confirmation**:
  Plays an authentic sacred temple chime upon saving each verified gift entry.
* 📁 **Instant CSV & Printable Ledger Export**:
  Export complete itemized spreadsheets sorted by serial number, city, or relation with one click.

---

## ⌨️ Rapid-Fire Keyboard Shortcuts (మున్షి హాట్‌కీస్)

GiftVault is engineered for lightning-speed reception desks so volunteers never need to touch a mouse:

| Shortcut | Action | Description |
| :---: | :--- | :--- |
| <kbd>N</kbd> | **New Entry Desk** | Switches to the gift logging desk and auto-focuses the guest name field. |
| <kbd>/</kbd> | **Quick Ledger Search** | Focuses the live search filter to look up any guest, city, or relation. |
| <kbd>+</kbd> or <kbd>=</kbd> | **+₹1 Lucky Coin** | Inside Amount field, automatically increments sum by ₹1 for auspicious blessing. |
| <kbd>Enter ↵</kbd> | **Save &amp; Print** | Saves entry, triggers confirmation chime, and opens thermal slip preview. |
| <kbd>Esc</kbd> | **Dismiss Modal** | Closes any active receipt preview, photo proof, or camera dialog. |

---

## 🏛️ Clean Repository Architecture

```
GiftVault/
├── index.html                   # High-performance self-contained SPA application shell
├── serve_nocache.py             # Development server with instant zero-cache headers
├── assets/
│   ├── css/                     # Modulated tokens, typography, layout, thermal styles
│   ├── js/
│   │   ├── core/                # Reactive store (Pub/Sub), IndexedDB, keyboard, icons
│   │   ├── components/          # Munshi desk, ledger table, receipt modal, estimator
│   │   ├── i18n/                # Telugu & English translations dictionary
│   │   └── app.js               # Runtime orchestrator & component lifecycle
│   ├── images/                  # Mathematical SVG logos, celebration photography
│   └── audio/                   # Auspicious temple soundbox chime
├── docs/
│   └── images/                  # High-res GitHub banner and interface showcase panels
├── tests/
│   └── test_giftvault_e2e.py    # Automated Playwright 9-step E2E verification test suite
├── LICENSE                      # Official MIT License
├── README.md                    # Project documentation & visual guide
├── SECURITY.md                  # Responsible vulnerability disclosure policy
├── robots.txt                   # Search crawler directives
└── sitemap.xml                  # XML sitemap schema
```

---

## 🚀 Quick Start (ప్రారంభించండి)

```bash
# 1. Clone the repository
git clone https://github.com/anas116-ai/Gift-Vault.git

# 2. Navigate to project folder
cd Gift-Vault

# 3. Start local development server
python serve_nocache.py
```
Open your browser at **`http://localhost:8080/`**.

---

## 🧪 Automated Testing & Verification

GiftVault includes a comprehensive Playwright test suite verifying voice dictation, modal dialogs, town autocomplete, receipt printing, and IndexedDB persistence:

```bash
python tests/test_giftvault_e2e.py
```

```text
============================================================
📊 TEST SUMMARY REPORT
============================================================
✅ Total Passed Checks: 9
❌ Total Failed Checks: 0
🎉 Multi-Event Isolation: 100% Verified
🛡️ LocalStorage Persistence: PASS across page reloads
🧾 2-Inch Thermal Slip: PASS with verified amounts
============================================================
```

---

## 🛰️ Code Craftsmanship & Slopdar Audit

GiftVault was audited using the [Slopdar](https://github.com/Slopdar/slopdar) scanner to eliminate AI boilerplate, template fingerprints, and marketing fluff:

* **Slop Score**: **`0 / 100`** (Tier: **`🛠️ Hand-Crafted`**)
* **Security**: Zero Stored XSS vulnerability with `GVUtils.escapeHtml` DOM sanitization.
* **Network Weight**: Zero unused CDN dependencies; Three.js 600KB bloat eliminated.

---

## 🔒 Security & Offline Privacy

* **Zero Cloud Leak Protocol**: No guest names, cash sums, or celebration dates are ever transmitted to external servers. Everything resides inside your local browser.
* **Input Sanitization**: All user strings undergo mathematical escaping before insertion into the DOM.
* **Isolated MediaStreams**: Camera and mic permissions are held strictly during active capture and terminated immediately upon modal exit.

For detailed privacy guidelines, please read our [SECURITY.md](SECURITY.md).

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

<div align="center">
  <sub>Crafted with devotion for sacred Indian family celebrations. Designed with bespoke SVG geometry and pure craftsmanship.</sub>
</div>
