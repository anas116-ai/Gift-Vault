class GiftEntryModel {
  final String id;
  final String eventId;
  final int serialNumber;
  final String guestName;
  final String phoneNumber;
  final String villageCity;
  final String relation;
  final String giftType; // CASH, GOLD, ITEM, GIFT, OTHER
  final double amount;
  final String itemName;
  final String quantity;
  final double estimatedValue;
  final String paymentMethod; // CASH, UPI, QR, CHEQUE, OTHER
  final String? photoUrl;
  final String? videoUrl;
  final String? receiptUrl;
  final String? guestPhotoUrl;
  final String? voiceNoteUrl;
  final String notes;
  final String createdByName;
  final DateTime createdAt;
  final DateTime updatedAt;
  final bool isDeleted;
  final DateTime? deletedAt;

  GiftEntryModel({
    required this.id,
    required this.eventId,
    required this.serialNumber,
    required this.guestName,
    this.phoneNumber = '',
    this.villageCity = '',
    this.relation = '',
    this.giftType = 'CASH',
    this.amount = 0.0,
    this.itemName = '',
    this.quantity = '',
    this.estimatedValue = 0.0,
    this.paymentMethod = 'CASH',
    this.photoUrl,
    this.videoUrl,
    this.receiptUrl,
    this.guestPhotoUrl,
    this.voiceNoteUrl,
    this.notes = '',
    required this.createdByName,
    required this.createdAt,
    required this.updatedAt,
    this.isDeleted = false,
    this.deletedAt,
  });

  Map<String, dynamic> toJson() => {
    'id': id,
    'eventId': eventId,
    'serialNumber': serialNumber,
    'guestName': guestName,
    'phoneNumber': phoneNumber,
    'villageCity': villageCity,
    'relation': relation,
    'giftType': giftType,
    'amount': amount,
    'itemName': itemName,
    'quantity': quantity,
    'estimatedValue': estimatedValue,
    'paymentMethod': paymentMethod,
    'photoUrl': photoUrl,
    'videoUrl': videoUrl,
    'receiptUrl': receiptUrl,
    'guestPhotoUrl': guestPhotoUrl,
    'voiceNoteUrl': voiceNoteUrl,
    'notes': notes,
    'createdByName': createdByName,
    'createdAt': createdAt.toIso8601String(),
    'updatedAt': updatedAt.toIso8601String(),
    'isDeleted': isDeleted,
    'deletedAt': deletedAt?.toIso8601String(),
  };

  factory GiftEntryModel.fromJson(Map<String, dynamic> json) => GiftEntryModel(
    id: json['id'],
    eventId: json['eventId'],
    serialNumber: json['serialNumber'] ?? 1,
    guestName: json['guestName'],
    phoneNumber: json['phoneNumber'] ?? '',
    villageCity: json['villageCity'] ?? '',
    relation: json['relation'] ?? '',
    giftType: json['giftType'] ?? 'CASH',
    amount: (json['amount'] as num?)?.toDouble() ?? 0.0,
    itemName: json['itemName'] ?? '',
    quantity: json['quantity'] ?? '',
    estimatedValue: (json['estimatedValue'] as num?)?.toDouble() ?? 0.0,
    paymentMethod: json['paymentMethod'] ?? 'CASH',
    photoUrl: json['photoUrl'],
    videoUrl: json['videoUrl'],
    receiptUrl: json['receiptUrl'],
    guestPhotoUrl: json['guestPhotoUrl'],
    voiceNoteUrl: json['voiceNoteUrl'],
    notes: json['notes'] ?? '',
    createdByName: json['createdByName'] ?? 'User',
    createdAt: DateTime.parse(json['createdAt']),
    updatedAt: DateTime.parse(json['updatedAt']),
    isDeleted: json['isDeleted'] ?? false,
    deletedAt: json['deletedAt'] != null ? DateTime.parse(json['deletedAt']) : null,
  );
}
