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

# Let's inspect the JavaScript section of web_preview/index.html
# We need to build a comprehensive Event & Ledger State Manager:
# 1. EVENTS_STORE in localStorage:
#    - 'event-wedding': Rahul & Snigdha Kalyanam (with its entries)
#    - 'event-birthday': Advait 1st Birthday & Cradle (with its entries)
#    - dynamic new events created by user (e.g. Chirala Beach Hair Cut)
# 2. currentActiveEventId tracks which event is open!
# 3. renderEventWorkspace(eventId) renders THAT event's header, KPI totals, recent ledger table, and entries starting from #1!
# 4. handleMunshiSubmit saves to the active event's entries, increments S.No, updates active event's KPIs, and saves to localStorage!
# 5. renderEventsHub() dynamically renders all events from EVENTS_STORE into the Event Hub grid!

print("Read HTML length:", len(html))
