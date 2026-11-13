import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/glass_card.dart';

class RecycleBinItem {
  final String id;
  final int serialNo;
  final String guestName;
  final String village;
  final int amount;
  final String giftType;
  final DateTime deletedAt;
  final String deletedBy;

  RecycleBinItem({
    required this.id,
    required this.serialNo,
    required this.guestName,
    required this.village,
    required this.amount,
    required this.giftType,
    required this.deletedAt,
    required this.deletedBy,
  });
}

class RecycleBinScreen extends StatefulWidget {
  const RecycleBinScreen({super.key});

  @override
  State<RecycleBinScreen> createState() => _RecycleBinScreenState();
}

class _RecycleBinScreenState extends State<RecycleBinScreen> {
  final List<RecycleBinItem> _binItems = [
    RecycleBinItem(
      id: 'bin_1',
      serialNo: 113,
      guestName: 'ఆవుల కోటేశ్వరరావు',
      village: 'నరసరావుపేట',
      amount: 1116,
      giftType: 'Cash',
      deletedAt: DateTime.now().subtract(const Duration(hours: 14)),
      deletedBy: 'సురేష్ (కౌంటర్ B)',
    ),
    RecycleBinItem(
      id: 'bin_2',
      serialNo: 112,
      guestName: 'బాపట్ల వీరయ్య గారు',
      village: 'బాపట్ల',
      amount: 501,
      giftType: 'Cash',
      deletedAt: DateTime.now().subtract(const Duration(days: 1)),
      deletedBy: 'రమేష్ (అడ్మిన్)',
    ),
  ];

  void _restoreItem(RecycleBinItem item) {
    setState(() {
      _binItems.removeWhere((i) => i.id == item.id);
    });
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('✓ #${item.serialNo} (${item.guestName}) తిరిగి లెడ్జర్‌లోకి పునరుద్ధరించబడింది!'),
        backgroundColor: AppColors.success,
        behavior: SnackBarBehavior.floating,
      ),
    );
  }

  void _purgeItem(RecycleBinItem item) {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('శాశ్వతంగా తొలగించాలా?'),
        content: Text('#${item.serialNo} (${item.guestName}) రికార్డును శాశ్వతంగా తొలగిస్తే తిరిగి పొందలేరు.'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('రద్దు'),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(backgroundColor: Colors.red),
            onPressed: () {
              Navigator.pop(ctx);
              setState(() {
                _binItems.removeWhere((i) => i.id == item.id);
              });
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(
                  content: Text('ఎంట్రీ శాశ్వతంగా తొలగించబడింది.'),
                  behavior: SnackBarBehavior.floating,
                ),
              );
            },
            child: const Text('తొలగించు', style: TextStyle(color: Colors.white)),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.canvasLight,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: Text(
          '30-రోజుల రీసైకిల్ బిన్',
          style: GoogleFonts.suranna(
            fontWeight: FontWeight.bold,
            color: AppColors.textDark,
          ),
        ),
      ),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              GlassCard(
                child: Padding(
                  padding: const EdgeInsets.all(14.0),
                  child: Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(10),
                        decoration: BoxDecoration(
                          color: Colors.purple.shade50,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: const Icon(Icons.shield_outlined, color: Colors.purple, size: 26),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Text(
                          'కళ్యాణ మండపం రష్ లో పొరపాటున తొలగించిన ఏ చదివింపు ఎంట్రీ అయినా ఇక్కడ 30 రోజుల వరకు సురక్షితంగా ఉంటుంది.',
                          style: GoogleFonts.anekTelugu(
                            fontSize: 12,
                            color: AppColors.textMuted,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 16),
              Text(
                'తొలగించబడిన రికార్డులు (${_binItems.length})',
                style: GoogleFonts.anekTelugu(
                  fontWeight: FontWeight.bold,
                  fontSize: 14,
                  color: AppColors.textDark,
                ),
              ),
              const SizedBox(height: 8),
              Expanded(
                child: _binItems.isEmpty
                    ? Center(
                        child: Text(
                          'రీసైకిల్ బిన్ ఖాళీగా ఉంది.',
                          style: GoogleFonts.anekTelugu(color: AppColors.textMuted),
                        ),
                      )
                    : ListView.separated(
                        itemCount: _binItems.length,
                        separatorBuilder: (_, __) => const SizedBox(height: 10),
                        itemBuilder: (context, index) {
                          final item = _binItems[index];
                          return GlassCard(
                            child: Padding(
                              padding: const EdgeInsets.all(12.0),
                              child: Row(
                                children: [
                                  CircleAvatar(
                                    backgroundColor: Colors.purple.shade100,
                                    child: Text(
                                      '#${item.serialNo}',
                                      style: const TextStyle(
                                        fontSize: 11,
                                        fontWeight: FontWeight.bold,
                                        color: Colors.purple,
                                      ),
                                    ),
                                  ),
                                  const SizedBox(width: 12),
                                  Expanded(
                                    child: Column(
                                      crossAxisAlignment: CrossAxisAlignment.start,
                                      children: [
                                        Text(
                                          '${item.guestName} (${item.village})',
                                          style: GoogleFonts.anekTelugu(
                                            fontWeight: FontWeight.bold,
                                            fontSize: 13,
                                            color: AppColors.textDark,
                                          ),
                                        ),
                                        Text(
                                          '₹${item.amount} • తొలగించిన వారు: ${item.deletedBy}',
                                          style: GoogleFonts.anekTelugu(
                                            fontSize: 11,
                                            color: AppColors.textMuted,
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                  IconButton(
                                    icon: const Icon(Icons.restore, color: AppColors.success),
                                    tooltip: 'పునరుద్ధరించు (Restore)',
                                    onPressed: () => _restoreItem(item),
                                  ),
                                  IconButton(
                                    icon: const Icon(Icons.delete_forever, color: Colors.red),
                                    tooltip: 'శాశ్వతంగా తొలగించు',
                                    onPressed: () => _purgeItem(item),
                                  ),
                                ],
                              ),
                            ),
                          );
                        },
                      ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
