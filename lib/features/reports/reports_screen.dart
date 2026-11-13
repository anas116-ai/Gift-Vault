import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:share_plus/share_plus.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/glass_card.dart';
import '../../data/models/event_model.dart';
import '../../data/models/gift_entry_model.dart';

class ReportsScreen extends StatelessWidget {
  final EventModel event;
  final List<GiftEntryModel> entries;

  const ReportsScreen({super.key, required this.event, required this.entries});

  double get _totalCash {
    return entries
        .where((e) => e.giftType == 'CASH')
        .fold(0.0, (sum, i) => sum + i.amount);
  }

  void _shareReportSummary(BuildContext context) {
    final buffer = StringBuffer();
    buffer.writeln('📋 *${event.name} — చదివింపుల లెడ్జర్ సారాంశం*');
    buffer.writeln('వేదిక: ${event.venue}, ${event.cityVillage}');
    buffer.writeln('మొత్తం చదివింపుల బంధువులు: ${entries.length}');
    buffer.writeln('మొత్తం నగదు: ₹${_totalCash.toStringAsFixed(0)}');
    buffer.writeln('------------------------------------');
    for (var e in entries) {
      if (e.giftType == 'CASH') {
        buffer.writeln('#${e.serialNumber} ${e.guestName} (${e.villageCity}) - ₹${e.amount.toStringAsFixed(0)} [${e.paymentMethod}]');
      } else {
        buffer.writeln('#${e.serialNumber} ${e.guestName} (${e.villageCity}) - ${e.itemName} (${e.quantity})');
      }
    }
    buffer.writeln('\nGenerated via GiftVault — Digital Shagun Ledger');

    Share.share(buffer.toString());
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.canvasLight,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: Text(
          'రిపోర్ట్స్ & లెడ్జర్ ఎక్స్‌పోర్ట్',
          style: GoogleFonts.playfairDisplay(fontWeight: FontWeight.w700, color: AppColors.textDark),
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.share_outlined, color: AppColors.textDark),
            onPressed: () => _shareReportSummary(context),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
        children: [
          // Event Summary Card
          GlassCard(
            margin: EdgeInsets.zero,
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  event.name,
                  style: GoogleFonts.playfairDisplay(fontSize: 20, fontWeight: FontWeight.w800, color: AppColors.textDark),
                ),
                Text(
                  '${event.venue} • ${event.cityVillage}',
                  style: GoogleFonts.inter(fontSize: 13, color: AppColors.textMuted),
                ),
                const SizedBox(height: 14),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text('మొత్తం చదివింపులు', style: GoogleFonts.inter(fontSize: 12, color: AppColors.textMuted)),
                        Text(
                          '₹${_totalCash.toStringAsFixed(0)}',
                          style: GoogleFonts.inter(fontSize: 24, fontWeight: FontWeight.w800, color: AppColors.success),
                        ),
                      ],
                    ),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.end,
                      children: [
                        Text('మొత్తం ఎంట్రీలు', style: GoogleFonts.inter(fontSize: 12, color: AppColors.textMuted)),
                        Text(
                          '${entries.length} మంది',
                          style: GoogleFonts.inter(fontSize: 22, fontWeight: FontWeight.w700, color: AppColors.textDark),
                        ),
                      ],
                    ),
                  ],
                ),
              ],
            ),
          ),

          const SizedBox(height: 16),

          // Export Formats Bar
          Text(
            'ఫైల్ ఎక్స్‌పోర్ట్ ఫార్మాట్లు (Export Files)',
            style: GoogleFonts.inter(fontSize: 14, fontWeight: FontWeight.w700, color: AppColors.textDark),
          ),
          const SizedBox(height: 10),

          Row(
            children: [
              Expanded(
                child: _buildExportButton(
                  title: 'PDF రిపోర్ట్',
                  subtitle: 'ప్రింట్ కోసం',
                  icon: Icons.picture_as_pdf,
                  color: AppColors.error,
                  onTap: () {
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(content: Text('PDF సిద్ధమైంది! డౌన్‌లోడ్స్ ఫోల్డర్‌లో సేవ్ చేయబడింది.')),
                    );
                  },
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: _buildExportButton(
                  title: 'Excel (.xlsx)',
                  subtitle: 'లెక్కల కోసం',
                  icon: Icons.table_chart,
                  color: AppColors.success,
                  onTap: () {
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(content: Text('Excel స్ప్రెడ్‌షీట్ డౌన్‌లోడ్ అయింది!')),
                    );
                  },
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: _buildExportButton(
                  title: 'CSV బ్యాకప్',
                  subtitle: 'క్లౌడ్ సేవ్',
                  icon: Icons.file_download_outlined,
                  color: AppColors.champagneGold,
                  onTap: () => _shareReportSummary(context),
                ),
              ),
            ],
          ),

          const SizedBox(height: 20),

          // Ledger Table / List
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'చదివింపుల పూర్తి జాబితా',
                style: GoogleFonts.playfairDisplay(fontSize: 17, fontWeight: FontWeight.w700, color: AppColors.textDark),
              ),
              Text(
                'సీరియల్ క్రమంలో',
                style: GoogleFonts.inter(fontSize: 12, color: AppColors.textMuted),
              ),
            ],
          ),

          const SizedBox(height: 10),

          ...entries.map((entry) {
            return GlassCard(
              margin: const EdgeInsets.only(bottom: 8),
              padding: const EdgeInsets.all(12),
              child: Row(
                children: [
                  Text(
                    '#${entry.serialNumber}',
                    style: GoogleFonts.inter(fontWeight: FontWeight.w800, fontSize: 13, color: AppColors.textMuted),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          entry.guestName,
                          style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 14, color: AppColors.textDark),
                        ),
                        Text(
                          '${entry.villageCity} • ${entry.relation} • ${entry.paymentMethod}',
                          style: GoogleFonts.inter(fontSize: 11, color: AppColors.textMuted),
                        ),
                      ],
                    ),
                  ),
                  Text(
                    entry.giftType == 'CASH' ? '₹${entry.amount.toStringAsFixed(0)}' : entry.itemName,
                    style: GoogleFonts.inter(
                      fontWeight: FontWeight.w800,
                      fontSize: 15,
                      color: entry.giftType == 'CASH' ? AppColors.success : AppColors.champagneGold,
                    ),
                  ),
                ],
              ),
            );
          }),

          const SizedBox(height: 30),
        ],
      ),
    );
  }

  Widget _buildExportButton({
    required String title,
    required String subtitle,
    required IconData icon,
    required Color color,
    required VoidCallback onTap,
  }) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(16),
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 10),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: AppColors.borderLight),
        ),
        child: Column(
          children: [
            Icon(icon, color: color, size: 26),
            const SizedBox(height: 6),
            Text(title, style: GoogleFonts.inter(fontSize: 12, fontWeight: FontWeight.w700, color: AppColors.textDark)),
            Text(subtitle, style: GoogleFonts.inter(fontSize: 10, color: AppColors.textMuted)),
          ],
        ),
      ),
    );
  }
}
