class EventSettings {
  final String photoRequirement; // REQUIRED, OPTIONAL, OFF
  final String videoRequirement; // REQUIRED, OPTIONAL, OFF
  final String receiptRequirement; // REQUIRED, OPTIONAL, OFF
  final String guestPhotoRequirement; // REQUIRED, OPTIONAL, OFF
  final bool voiceNotesEnabled;

  const EventSettings({
    this.photoRequirement = 'OPTIONAL',
    this.videoRequirement = 'OPTIONAL',
    this.receiptRequirement = 'OPTIONAL',
    this.guestPhotoRequirement = 'OPTIONAL',
    this.voiceNotesEnabled = true,
  });

  Map<String, dynamic> toJson() => {
    'photoRequirement': photoRequirement,
    'videoRequirement': videoRequirement,
    'receiptRequirement': receiptRequirement,
    'guestPhotoRequirement': guestPhotoRequirement,
    'voiceNotesEnabled': voiceNotesEnabled,
  };

  factory EventSettings.fromJson(Map<String, dynamic> json) => EventSettings(
    photoRequirement: json['photoRequirement'] ?? 'OPTIONAL',
    videoRequirement: json['videoRequirement'] ?? 'OPTIONAL',
    receiptRequirement: json['receiptRequirement'] ?? 'OPTIONAL',
    guestPhotoRequirement: json['guestPhotoRequirement'] ?? 'OPTIONAL',
    voiceNotesEnabled: json['voiceNotesEnabled'] ?? true,
  );
}

class EventModel {
  final String id;
  final String familyId;
  final String name; // e.g. "రమేష్ & సుజాత వివాహం"
  final String eventType; // Wedding, Reception, Haldi, Engagement, Housewarming, etc.
  final String? groomName; // వరుడు / మొదటి వ్యక్తి
  final String? brideName; // వధువు / రెండవ వ్యక్తి
  final DateTime eventDate;
  final String? muhurthamTime; // e.g. "ఉ. 09:45"
  final String venue;
  final String cityVillage;
  final String hostName;
  final String relationshipType;
  final String? eventTag; // e.g. "#కుమారుడిపెళ్లి"
  final String? coverImageUrl;
  final EventSettings settings;
  final String status; // ACTIVE, ARCHIVED, DELETED
  final DateTime? deletedAt;

  EventModel({
    required this.id,
    required this.familyId,
    required this.name,
    required this.eventType,
    this.groomName,
    this.brideName,
    required this.eventDate,
    this.muhurthamTime,
    required this.venue,
    required this.cityVillage,
    required this.hostName,
    required this.relationshipType,
    this.eventTag,
    this.coverImageUrl,
    this.settings = const EventSettings(),
    this.status = 'ACTIVE',
    this.deletedAt,
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'familyId': familyId,
    'name': name,
    'eventType': eventType,
    'groomName': groomName,
    'brideName': brideName,
    'eventDate': eventDate.toIso8601String(),
    'muhurthamTime': muhurthamTime,
    'venue': venue,
    'cityVillage': cityVillage,
    'hostName': hostName,
    'relationshipType': relationshipType,
    'eventTag': eventTag,
    'coverImageUrl': coverImageUrl,
    'settings': settings.toJson(),
    'status': status,
    'deletedAt': deletedAt?.toIso8601String(),
  };

  factory EventModel.fromJson(Map<String, dynamic> json) => EventModel(
    id: json['id'],
    familyId: json['familyId'],
    name: json['name'],
    eventType: json['eventType'] ?? 'Wedding',
    groomName: json['groomName'],
    brideName: json['brideName'],
    eventDate: DateTime.parse(json['eventDate']),
    muhurthamTime: json['muhurthamTime'],
    venue: json['venue'] ?? '',
    cityVillage: json['cityVillage'] ?? '',
    hostName: json['hostName'] ?? '',
    relationshipType: json['relationshipType'] ?? '',
    eventTag: json['eventTag'],
    coverImageUrl: json['coverImageUrl'],
    settings: json['settings'] != null ? EventSettings.fromJson(json['settings']) : const EventSettings(),
    status: json['status'] ?? 'ACTIVE',
    deletedAt: json['deletedAt'] != null ? DateTime.parse(json['deletedAt']) : null,
  );
}
