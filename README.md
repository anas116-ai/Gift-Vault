# GiftVault (గిఫ్ట్‌వాల్ట్) 🎁

> **Sacred Indian Family Shagun Vault & Digital Red Notebook**  
> *100% Offline Privacy • Multi-Lingual Voice Dictation • 2-Inch Thermal Slips • Live Photo Proofs • Zero Cloud Leak*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Slopdar Score](https://img.shields.io/badge/Slopdar-0%2F100%20(Hand--Crafted)-brightgreen)](#)
[![Offline First](https://img.shields.io/badge/Architecture-100%25%20Offline%20First-success)](#)
[![Security](https://img.shields.io/badge/Security-Sanitized%20%26%20Hardened-blue)](#)

---

## 📖 Overview

In Indian celebrations (Weddings, Griha Pravesham, Silver Jubilees, Cradle Ceremonies), families traditionally record cash gifts (*Moyyulu*, *Chadhivimpu*, *Tamboolam*, *Shagun*) in a red physical diary (*Munshi Book*). These paper notebooks frequently suffer from handwriting illegibility, misplaced slips, calculation errors, or physical loss.

**GiftVault** modernizes this sacred generational tradition with an ultra-fast, offline-ready web application engineered for chaotic reception counters.

---

## ✨ Key Capabilities

* 🎙️ **Hands-Free Telugu & English Voice Dictation**:
  Speak naturally (*"Mastan Rao Garu, Chirala, 15000 cash"*), and GiftVault parses and populates the Name, Native City, Amount, and Mode automatically.
* 📸 **Live Webcam & File Gift Photo Proofs**:
  Capture instant snapshot proof of high-value gifts, gold ornaments, or shagun envelopes right at the reception counter.
* 🧾 **2-Inch ESC/POS Thermal Receipt Printing**:
  Instantly print professional official blessing slips on portable Bluetooth thermal printers for return gift hampers.
* 🛡️ **100% Offline-First Security (Zero Cloud Leak Protocol)**:
  Runs completely local using IndexedDB. No celebration financial data ever leaves your device without manual export.
* 📊 **Smart Reciprocity Ledger**:
  Instantly check how much a family gave at your previous functions when attending their future celebrations.
* ⚡ **High-Speed Munshi Counter with City Autocomplete**:
  Pre-loaded smart autocomplete suggestions for major Andhra Pradesh and Telangana towns and cities.
* 🔔 **Chime Audio Feedback**:
  Plays an authentic auspicious soundbox confirmation chime upon logging every blessing.
* 📁 **Instant CSV & PDF Export**:
  Export complete tally sheets formatted for wedding accounts and family elders.

---

## 🏛️ Architecture & Tech Stack

```
GiftVault/
├── index.html                 # Self-contained offline application shell
├── serve_nocache.py           # Local development server with no-cache headers
├── assets/
│   ├── css/                   # Design tokens, typography, layout, thermal styles
│   ├── js/
│   │   ├── core/              # State store (Pub/Sub), IndexedDB, keyboard engine, icons
│   │   ├── components/        # Munshi desk, ledger table, receipt modal, estimator
│   │   ├── i18n/              # Telugu & English translations dictionary
│   │   └── app.js             # Runtime orchestrator & event bus
│   ├── images/                # Vector logos, celebration photography, UI assets
│   └── audio/                 # Sacred soundbox chime feedback
├── tests/                     # Automated Playwright E2E verification test suite
├── LICENSE                    # MIT License
├── README.md                  # Project documentation
├── SECURITY.md                # Responsible disclosure & privacy architecture
├── robots.txt                 # Search engine directives
└── sitemap.xml                # Sitemap definition
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/giftvault.git
cd giftvault
```

### 2. Start the Local Server
```bash
python serve_nocache.py
```
Open your browser at **`http://localhost:8080/`**.

---

## 🧪 Automated Testing

GiftVault includes an end-to-end verification suite testing voice dictation, modal handling, city suggestions, slip printing, and offline persistence:

```bash
python tests/test_giftvault_e2e.py
```

---

## 🛡️ Security & Privacy

GiftVault is built with senior-level security practices:
* **Input Sanitization**: All guest names, relations, and notes are sanitized via `GVUtils.escapeHtml` before DOM rendering to eliminate XSS risks.
* **Zero Telemetry**: No third-party analytics trackers, cookies, or tracking pixels.
* **Isolated MediaStreams**: Camera and mic streams are acquired only on demand and terminated immediately upon modal dismissal.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - feel free to use, modify, and distribute for family celebrations and commercial deployments.
