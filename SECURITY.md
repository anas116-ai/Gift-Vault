# Security Policy for GiftVault

GiftVault is dedicated to preserving Indian family celebration blessings with uncompromising privacy and security.

## 🛡️ Core Security Architecture

1. **100% Offline-First (Zero Cloud Leak Protocol)**
   - All celebration guest entries, shagun cash amounts, UPI transactions, and photo proofs are stored exclusively in the user's browser via **Local IndexedDB / Web Storage**.
   - No sensitive celebration records are ever uploaded to remote servers or third-party cloud brokers without explicit user initiation.

2. **XSS & Injection Hardening**
   - All guest inputs (guest names, native towns, familial relationships, and notes) pass through strict input sanitization and HTML escaping (`GVUtils.escapeHtml`) before DOM rendering.
   - External dependencies and CDN scripts are strictly vetted and pinned.

3. **Camera & Audio Stream Isolation**
   - MediaStreams used for the gift photo proof camera and voice dictation mic are acquired only upon explicit user interaction and are immediately stopped and cleared upon modal close.

## 🔒 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |

## 🚨 Reporting a Vulnerability

If you discover a security vulnerability or have concerns regarding data leakage in GiftVault:
1. Please **do not** open a public GitHub issue.
2. Submit your findings responsibly via email to: `security@giftvault.app` (or via private GitHub Vulnerability Reporting).
3. Include detailed steps to reproduce the issue and any proof-of-concept payloads.
4. We acknowledge all reports within 48 hours and work with you to patch any validated concerns before public disclosure.
