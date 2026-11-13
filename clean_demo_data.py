# -*- coding: utf-8 -*-
"""
Remove all demo/sample data from GiftVault Flutter & Web codebase.
Ensure fresh, empty state ready for real users.
"""
import os
import re

LOCAL_STORAGE_PATH = r"c:\Project\Gift Valut\lib\data\database\local_storage.dart"
DASHBOARD_PATH = r"c:\Project\Gift Valut\lib\features\dashboard\dashboard_screen.dart"

# 1. Update local_storage.dart
with open(LOCAL_STORAGE_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Replace _getSampleEvents() with empty list
content = re.sub(
    r"if \(jsonString == null\) return _getSampleEvents\(\);",
    "if (jsonString == null) return [];",
    content
)
content = re.sub(
    r"return _getSampleEvents\(\);",
    "return [];",
    content
)

# Replace _getSampleEntries() with empty list
content = re.sub(
    r"if \(jsonString == null\) return _getSampleEntries\(eventId\);",
    "if (jsonString == null) return [];",
    content
)
content = re.sub(
    r"return _getSampleEntries\(eventId\);",
    "return [];",
    content
)

# Replace the implementations of _getSampleEvents and _getSampleEntries
sample_events_pattern = r"List<EventModel> _getSampleEvents\(\) \{[\s\S]*?List<GiftEntryModel> _getSampleEntries\(String eventId\) \{[\s\S]*?\n  \}"
replacement = """  List<EventModel> _getSampleEvents() => [];
  List<GiftEntryModel> _getSampleEntries(String eventId) => [];

  // Clear all data for fresh reset
  Future<void> clearAllData() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_eventsKey);
    await prefs.remove(_entriesKey);
    await prefs.remove(_activeEventKey);
  }"""

content = re.sub(sample_events_pattern, replacement, content)

with open(LOCAL_STORAGE_PATH, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated local_storage.dart to return 100% fresh/empty data.")

# 2. Update dashboard_screen.dart to handle empty state gracefully and dynamically
with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    dash_content = f.read()

# Replace hardcoded 'రామారావు కుటుంబం' with dynamic event/family name
dash_content = dash_content.replace(
    "'రామారావు కుటుంబం'",
    "_selectedEvent != null ? (_selectedEvent!.hostName.isNotEmpty ? _selectedEvent!.hostName : _selectedEvent!.name) : 'నా కుటుంబ ఖాతా'"
)

# In the desk mode button, if no event exists, prompt to create event
dash_content = dash_content.replace(
"""                      onPressed: () async {
                        if (_selectedEvent != null) {
                          final refreshed = await Navigator.push(
                            context,
                            MaterialPageRoute(builder: (_) => DeskModeScreen(event: _selectedEvent!)),
                          );
                          if (refreshed == true) _loadDashboardData();
                        }
                      },""",
"""                      onPressed: () async {
                        if (_selectedEvent != null) {
                          final refreshed = await Navigator.push(
                            context,
                            MaterialPageRoute(builder: (_) => DeskModeScreen(event: _selectedEvent!)),
                          );
                          if (refreshed == true) _loadDashboardData();
                        } else {
                          final created = await Navigator.push(
                            context,
                            MaterialPageRoute(builder: (_) => const CreateEventScreen()),
                          );
                          if (created == true) _loadDashboardData();
                        }
                      },"""
)

with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
    f.write(dash_content)
print("Updated dashboard_screen.dart to handle fresh empty state gracefully.")
