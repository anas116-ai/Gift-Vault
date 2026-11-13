# -*- coding: utf-8 -*-
"""
Clean demo data in desktop.html and mobile.html so web preview is also 100% fresh.
"""
import os
import re

PREVIEW_DIR = r"c:\Project\Gift Valut\web_preview"
WEB_DIR = r"c:\Project\Gift Valut\web"

for folder in [PREVIEW_DIR, WEB_DIR]:
    desk_file = os.path.join(folder, "desktop.html")
    if os.path.exists(desk_file):
        with open(desk_file, "r", encoding="utf-8") as f:
            c = f.read()
        
        # Replace DEFAULT_LEDGER with empty array
        c = re.sub(r"let DEFAULT_LEDGER = \[[\s\S]*?\];", "let DEFAULT_LEDGER = [];", c)
        # Clear storage on initial load if old sample data exists
        c = c.replace(
            "let DESK_LEDGER = JSON.parse(localStorage.getItem(STORAGE_KEY_LEDGER)) || DEFAULT_LEDGER;",
            "let DESK_LEDGER = JSON.parse(localStorage.getItem(STORAGE_KEY_LEDGER)) || [];"
        )
        # Update default KPI numbers to 0
        c = c.replace("₹8,42,101", "₹0")
        c = c.replace("₹4,15,000", "₹0")
        c = c.replace("+₹4,27,101", "₹0")
        c = c.replace("42.5", "0")
        c = c.replace("↑ 148 మంది బంధుమిత్రులు", "0 మంది బంధువులు")
        # Empty table placeholder
        c = c.replace(
            "if (fullTbody) {",
            """if (fullTbody) {
        if (DESK_LEDGER.length === 0) {
          fullTbody.innerHTML = '<tr><td colspan="9" style="text-align: center; padding: 40px; color: var(--text-muted);">ఇంకా ఎటువంటి కానుకలు నమోదు కాలేదు. పైనున్న "+ కొత్త కానుక ఎంట్రీ" బటన్ ద్వారా మీ మొదటి కానుకను నమోదు చేయండి.</td></tr>';
          return;
        }"""
        )
        c = c.replace(
            "if (recentTbody) {",
            """if (recentTbody) {
        if (DESK_LEDGER.length === 0) {
          recentTbody.innerHTML = '<tr><td colspan="7" style="text-align: center; padding: 30px; color: var(--text-muted);">ఇంకా ఎటువంటి కానుకలు నమోదు కాలేదు.</td></tr>';
        } else"""
        )
        with open(desk_file, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Cleaned {desk_file}")

    mob_file = os.path.join(folder, "mobile.html")
    if os.path.exists(mob_file):
        with open(mob_file, "r", encoding="utf-8") as f:
            m = f.read()
        m = re.sub(r"let DEFAULT_LEDGER = \[[\s\S]*?\];", "let DEFAULT_LEDGER = [];", m)
        m = m.replace(
            "let MOB_DATA = JSON.parse(localStorage.getItem(STORAGE_KEY_LEDGER)) || DEFAULT_LEDGER;",
            "let MOB_DATA = JSON.parse(localStorage.getItem(STORAGE_KEY_LEDGER)) || [];"
        )
        m = m.replace("₹8,42,101", "₹0")
        m = m.replace("₹4,15,000", "₹0")
        m = m.replace("+₹4,27,101", "₹0")
        m = m.replace("42.5g", "0g")
        m = m.replace(
            "if (recentBox) {",
            """if (recentBox) {
        if (MOB_DATA.length === 0) {
          recentBox.innerHTML = '<div style="text-align: center; padding: 24px; color: var(--text-muted); font-size: 13px;">ఇంకా ఏ కానుకలు నమోదు కాలేదు. క్రింద ఉన్న (+) బటన్ నొక్కి కొత్త కానుకను నమోదు చేయండి.</div>';
        } else"""
        )
        m = m.replace(
            "if (fullBox) {",
            """if (fullBox) {
        if (MOB_DATA.length === 0) {
          fullBox.innerHTML = '<div style="text-align: center; padding: 30px; color: var(--text-muted); font-size: 13px;">ఎర్ర పుస్తకంలో ఇంకా ఏ ఎంట్రీలు లేవు.</div>';
        } else"""
        )
        with open(mob_file, "w", encoding="utf-8") as f:
            f.write(m)
        print(f"Cleaned {mob_file}")

print("Cleaned demo data across all web files successfully.")
