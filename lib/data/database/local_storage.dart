import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/event_model.dart';
import '../models/gift_entry_model.dart';

class LocalStorageService {
  static const String _eventsKey = 'giftvault_events';
  static const String _entriesKey = 'giftvault_entries';
  static const String _activeEventKey = 'giftvault_active_event_id';

  // Singleton instance
  static final LocalStorageService instance = LocalStorageService._internal();
  LocalStorageService._internal();

  // Load all active events
  Future<List<EventModel>> getEvents() async {
    final prefs = await SharedPreferences.getInstance();
    final jsonString = prefs.getString(_eventsKey);
    if (jsonString == null) return [];

    try {
      final List<dynamic> list = jsonDecode(jsonString);
      return list
          .map((item) => EventModel.fromJson(item))
          .where((e) => e.status != 'DELETED')
          .toList();
    } catch (e) {
      return [];
    }
  }

  // Save Event
  Future<void> saveEvent(EventModel event) async {
    final prefs = await SharedPreferences.getInstance();
    final events = await getEvents();
    final index = events.indexWhere((e) => e.id == event.id);
    if (index >= 0) {
      events[index] = event;
    } else {
      events.insert(0, event);
    }
    await prefs.setString(_eventsKey, jsonEncode(events.map((e) => e.toJson()).toList()));
  }

  // Active Event
  Future<String?> getActiveEventId() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString(_activeEventKey);
  }

  Future<void> setActiveEventId(String eventId) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_activeEventKey, eventId);
  }

  // Load all entries for an event
  Future<List<GiftEntryModel>> getEntries(String eventId) async {
    final prefs = await SharedPreferences.getInstance();
    final jsonString = prefs.getString(_entriesKey);
    if (jsonString == null) return [];

    try {
      final List<dynamic> list = jsonDecode(jsonString);
      return list
          .map((item) => GiftEntryModel.fromJson(item))
          .where((e) => e.eventId == eventId && !e.isDeleted)
          .toList()
        ..sort((a, b) => b.serialNumber.compareTo(a.serialNumber));
    } catch (e) {
      return [];
    }
  }

  // Get next serial number for an event
  Future<int> getNextSerialNumber(String eventId) async {
    final entries = await getEntries(eventId);
    if (entries.isEmpty) return 1;
    final maxSerial = entries.map((e) => e.serialNumber).reduce((a, b) => a > b ? a : b);
    return maxSerial + 1;
  }

  // Save new or updated entry
  Future<void> saveEntry(GiftEntryModel entry) async {
    final prefs = await SharedPreferences.getInstance();
    final jsonString = prefs.getString(_entriesKey);
    List<GiftEntryModel> allEntries = [];

    if (jsonString != null) {
      try {
        final List<dynamic> list = jsonDecode(jsonString);
        allEntries = list.map((item) => GiftEntryModel.fromJson(item)).toList();
      } catch (_) {}
    }

    final index = allEntries.indexWhere((e) => e.id == entry.id);
    if (index >= 0) {
      allEntries[index] = entry;
    } else {
      allEntries.add(entry);
    }

    await prefs.setString(_entriesKey, jsonEncode(allEntries.map((e) => e.toJson()).toList()));
  }

  // Soft delete with 30-day recovery
  Future<void> softDeleteEntry(String entryId) async {
    final prefs = await SharedPreferences.getInstance();
    final jsonString = prefs.getString(_entriesKey);
    if (jsonString == null) return;

    final List<dynamic> list = jsonDecode(jsonString);
    final allEntries = list.map((item) => GiftEntryModel.fromJson(item)).toList();
    final index = allEntries.indexWhere((e) => e.id == entryId);
    if (index >= 0) {
      final existing = allEntries[index];
      allEntries[index] = GiftEntryModel(
        id: existing.id,
        eventId: existing.eventId,
        serialNumber: existing.serialNumber,
        guestName: existing.guestName,
        phoneNumber: existing.phoneNumber,
        villageCity: existing.villageCity,
        relation: existing.relation,
        giftType: existing.giftType,
        amount: existing.amount,
        itemName: existing.itemName,
        quantity: existing.quantity,
        estimatedValue: existing.estimatedValue,
        paymentMethod: existing.paymentMethod,
        photoUrl: existing.photoUrl,
        videoUrl: existing.videoUrl,
        receiptUrl: existing.receiptUrl,
        guestPhotoUrl: existing.guestPhotoUrl,
        voiceNoteUrl: existing.voiceNoteUrl,
        notes: existing.notes,
        createdByName: existing.createdByName,
        createdAt: existing.createdAt,
        updatedAt: DateTime.now(),
        isDeleted: true,
        deletedAt: DateTime.now(),
      );
      await prefs.setString(_entriesKey, jsonEncode(allEntries.map((e) => e.toJson()).toList()));
    }
  }

  // Fallback Sample Events for instant UX demo
    List<EventModel> _getSampleEvents() => [];
  List<GiftEntryModel> _getSampleEntries(String eventId) => [];

  // Clear all data for fresh reset
  Future<void> clearAllData() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_eventsKey);
    await prefs.remove(_entriesKey);
    await prefs.remove(_activeEventKey);
  }
}
