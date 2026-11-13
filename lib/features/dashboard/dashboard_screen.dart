import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/glass_card.dart';
import '../../data/database/local_storage.dart';
import '../../data/models/event_model.dart';
import '../../data/models/gift_entry_model.dart';
import '../desk_mode/desk_mode_screen.dart';
import '../events/create_event_screen.dart';
import '../reports/reports_screen.dart';
import '../search/smart_search_screen.dart';
import '../qr_payment/qr_payment_screen.dart';

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  EventModel? _selectedEvent;
  List<GiftEntryModel> _recentEntries = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadDashboardData();
  }

  Future<void> _loadDashboardData() async {
    setState(() => _isLoading = true);
    final events = await LocalStorageService.instance.getEvents();
    if (events.isNotEmpty) {
      _selectedEvent = events.first;
      final entries = await LocalStorageService.instance.getEntries(_selectedEvent!.id);
      _recentEntries = entries;
    }
    setState(() => _isLoading = false);
  }

  double get _totalReceived {
    return _recentEntries
        .where((e) => e.giftType == 'CASH')
        .fold(0.0, (sum, item) => sum + item.amount);
  }

  int get _goldItemsCount {
    return _recentEntries.where((e) => e.giftType == 'GOLD').length;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.canvasLight,
      body: _isLoading
          ? const Center(child: CircularProgressIndicator(color: AppColors.lemonLime))
          : SafeArea(
              child: RefreshIndicator(
                onRefresh: _loadDashboardData,
                color: AppColors.lemonLime,
                child: ListView(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  children: [
                    // Header: Family Name & Cloud Sync Status
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              children: [
                                Text(
                                  _selectedEvent != null ? (_selectedEvent!.hostName.isNotEmpty ? _selectedEvent!.hostName : _selectedEvent!.name) : 'నా కుటుంబ ఖాతా',
                                  style: GoogleFonts.playfairDisplay(
                                    fontSize: 22,
                                    fontWeight: FontWeight.w800,
                                    color: AppColors.textDark,
                                  ),
                                ),
                                const SizedBox(width: 6),
                                Container(
                                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                                  decoration: BoxDecoration(
                                    color: AppColors.champagneGold.withOpacity(0.2),
                                    borderRadius: BorderRadius.circular(10),
                                  ),
                                  child: Text(
                                    'ఓనర్',
                                    style: GoogleFonts.inter(fontSize: 10, fontWeight: FontWeight.bold, color: AppColors.champagneGold),
                                  ),
                                ),
                              ],
                            ),
                            Text(
                              'GiftVault డిజిటల్ లెడ్జర్',
                              style: GoogleFonts.inter(fontSize: 13, color: AppColors.textMuted),
                            ),
                          ],
                        ),
                        // Cloud Sync Indicator
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                          decoration: BoxDecoration(
                            color: Colors.white,
                            borderRadius: BorderRadius.circular(20),
                            border: Border.all(color: AppColors.borderLight),
                          ),
                          child: Row(
                            children: [
                              Container(
                                width: 8,
                                height: 8,
                                decoration: const BoxDecoration(
                                  color: AppColors.success,
                                  shape: BoxShape.circle,
                                ),
                              ),
                              const SizedBox(width: 6),
                              Text(
                                'సింక్ అయింది',
                                style: GoogleFonts.inter(fontSize: 11, fontWeight: FontWeight.w600, color: AppColors.textDark),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),

                    const SizedBox(height: 16),

                    // Hero Glassmorphism Bento Grid Summary
                    GlassCard(
                      margin: EdgeInsets.zero,
                      padding: const EdgeInsets.all(20),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                _selectedEvent?.name ?? 'యాక్టివ్ ఫంక్షన్',
                                style: GoogleFonts.inter(fontSize: 14, fontWeight: FontWeight.w600, color: AppColors.textMuted),
                              ),
                              Container(
                                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                                decoration: BoxDecoration(
                                  color: AppColors.lemonLime.withOpacity(0.4),
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                child: Text(
                                  'లైవ్ కౌంటర్',
                                  style: GoogleFonts.inter(fontSize: 11, fontWeight: FontWeight.bold, color: AppColors.textDark),
                                ),
                              ),
                            ],
                          ),
                          const SizedBox(height: 10),
                          Text(
                            '₹${_totalReceived.toStringAsFixed(0)}',
                            style: GoogleFonts.inter(
                              fontSize: 34,
                              fontWeight: FontWeight.w900,
                              color: AppColors.textDark,
                              letterSpacing: -1,
                            ),
                          ),
                          const SizedBox(height: 4),
                          Text(
                            'మొత్తం చదివింపులు (${_recentEntries.length} మంది బంధువులు ఇచ్చారు)',
                            style: GoogleFonts.inter(fontSize: 13, color: AppColors.textMuted),
                          ),
                          const SizedBox(height: 16),
                          const Divider(color: AppColors.borderLight, height: 1),
                          const SizedBox(height: 14),
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceAround,
                            children: [
                              _buildMetricItem('ఎంట్రీల సంఖ్య', '${_recentEntries.length}', Icons.format_list_numbered),
                              Container(width: 1, height: 30, color: AppColors.borderLight),
                              _buildMetricItem('బంగారం/వెండి', '$_goldItemsCount కానుకలు', Icons.diamond_outlined),
                              Container(width: 1, height: 30, color: AppColors.borderLight),
                              _buildMetricItem('వేదిక', _selectedEvent?.cityVillage ?? 'విజయవాడ', Icons.location_on_outlined),
                            ],
                          ),
                        ],
                      ),
                    ),

                    const SizedBox(height: 18),

                    // High Priority Action: Enter Desk Mode (Big CTA)
                    ElevatedButton.icon(
                      onPressed: () async {
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
                      },
                      icon: const Icon(Icons.flash_on, color: AppColors.textDark, size: 24),
                      label: Text(
                        'డెస్క్ మోడ్ ఓపెన్ చేయి (హై-స్పీడ్ ఎంట్రీ)',
                        style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.w800),
                      ),
                    ),

                    const SizedBox(height: 16),

                    // Quick Action Tools Grid
                    Row(
                      children: [
                        Expanded(
                          child: _buildActionTile(
                            title: 'కొత్త ఫంక్షన్',
                            icon: Icons.add_circle_outline,
                            color: AppColors.champagneGold,
                            onTap: () async {
                              final created = await Navigator.push(
                                context,
                                MaterialPageRoute(builder: (_) => const CreateEventScreen()),
                              );
                              if (created == true) _loadDashboardData();
                            },
                          ),
                        ),
                        const SizedBox(width: 10),
                        Expanded(
                          child: _buildActionTile(
                            title: 'QR పేమెంట్',
                            icon: Icons.qr_code_2_outlined,
                            color: AppColors.deepRose,
                            onTap: () {
                              if (_selectedEvent != null) {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(builder: (_) => QrPaymentScreen(event: _selectedEvent!)),
                                );
                              }
                            },
                          ),
                        ),
                        const SizedBox(width: 10),
                        Expanded(
                          child: _buildActionTile(
                            title: 'స్మార్ట్ సెర్చ్',
                            icon: Icons.search_outlined,
                            color: const Color(0xFF7FD8D0),
                            onTap: () {
                              Navigator.push(
                                context,
                                MaterialPageRoute(builder: (_) => SmartSearchScreen(entries: _recentEntries)),
                              );
                            },
                          ),
                        ),
                        const SizedBox(width: 10),
                        Expanded(
                          child: _buildActionTile(
                            title: 'రిపోర్ట్స్',
                            icon: Icons.picture_as_pdf_outlined,
                            color: AppColors.lemonLime,
                            onTap: () {
                              if (_selectedEvent != null) {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(
                                    builder: (_) => ReportsScreen(
                                      event: _selectedEvent!,
                                      entries: _recentEntries,
                                    ),
                                  ),
                                );
                              }
                            },
                          ),
                        ),
                      ],
                    ),

                    const SizedBox(height: 20),

                    // Recent Entries Section Header
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text(
                          'ఇటీవలి చదివింపులు (Recent Entries)',
                          style: GoogleFonts.playfairDisplay(fontSize: 18, fontWeight: FontWeight.w700, color: AppColors.textDark),
                        ),
                        Text(
                          'మొత్తం: ${_recentEntries.length}',
                          style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.w600, color: AppColors.champagneGold),
                        ),
                      ],
                    ),

                    const SizedBox(height: 10),

                    // Recent Entries List
                    if (_recentEntries.isEmpty)
                      Container(
                        padding: const EdgeInsets.all(30),
                        child: Center(
                          child: Text(
                            'ఇంకా ఎటువంటి ఎంట్రీలు లేవు. డెస్క్ మోడ్ ద్వారా జోడించండి!',
                            style: GoogleFonts.inter(color: AppColors.textMuted),
                          ),
                        ),
                      )
                    else
                      ..._recentEntries.map((entry) => _buildEntryCard(entry)),

                    const SizedBox(height: 40),
                  ],
                ),
              ),
            ),
    );
  }

  Widget _buildMetricItem(String label, String value, IconData icon) {
    return Column(
      children: [
        Icon(icon, size: 18, color: AppColors.textMuted),
        const SizedBox(height: 4),
        Text(value, style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 13, color: AppColors.textDark)),
        Text(label, style: GoogleFonts.inter(fontSize: 11, color: AppColors.textMuted)),
      ],
    );
  }

  Widget _buildActionTile({
    required String title,
    required IconData icon,
    required Color color,
    required VoidCallback onTap,
  }) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(16),
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 14),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: AppColors.borderLight),
        ),
        child: Column(
          children: [
            Icon(icon, color: color, size: 24),
            const SizedBox(height: 6),
            Text(
              title,
              style: GoogleFonts.inter(fontSize: 11, fontWeight: FontWeight.w600, color: AppColors.textDark),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildEntryCard(GiftEntryModel entry) {
    return GlassCard(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.all(14),
      child: Row(
        children: [
          // Serial number badge
          Container(
            width: 36,
            height: 36,
            alignment: Alignment.center,
            decoration: BoxDecoration(
              color: AppColors.lemonLime.withOpacity(0.5),
              shape: BoxShape.circle,
            ),
            child: Text(
              '#${entry.serialNumber}',
              style: GoogleFonts.inter(fontWeight: FontWeight.w800, fontSize: 12, color: AppColors.textDark),
            ),
          ),
          const SizedBox(width: 12),
          // Name and Details
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  entry.guestName,
                  style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 15, color: AppColors.textDark),
                ),
                Text(
                  '${entry.villageCity.isNotEmpty ? entry.villageCity : "ఊరు"} • ${entry.relation.isNotEmpty ? entry.relation : "బంధువు"}',
                  style: GoogleFonts.inter(fontSize: 12, color: AppColors.textMuted),
                ),
              ],
            ),
          ),
          // Amount or Item
          Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              if (entry.giftType == 'CASH')
                Text(
                  '₹${entry.amount.toStringAsFixed(0)}',
                  style: GoogleFonts.inter(
                    fontWeight: FontWeight.w800,
                    fontSize: 16,
                    color: AppColors.success,
                  ),
                )
              else
                Text(
                  entry.itemName.isNotEmpty ? entry.itemName : entry.giftType,
                  style: GoogleFonts.inter(
                    fontWeight: FontWeight.w700,
                    fontSize: 13,
                    color: AppColors.champagneGold,
                  ),
                ),
              Text(
                entry.paymentMethod,
                style: GoogleFonts.inter(fontSize: 10, color: AppColors.textMuted, fontWeight: FontWeight.w500),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
