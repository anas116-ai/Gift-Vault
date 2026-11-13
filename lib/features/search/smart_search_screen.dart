import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/glass_card.dart';
import '../../data/models/gift_entry_model.dart';

class SmartSearchScreen extends StatefulWidget {
  final List<GiftEntryModel> entries;

  const SmartSearchScreen({super.key, required this.entries});

  @override
  State<SmartSearchScreen> createState() => _SmartSearchScreenState();
}

class _SmartSearchScreenState extends State<SmartSearchScreen> {
  final TextEditingController _searchController = TextEditingController();
  List<GiftEntryModel> _filtered = [];
  String _activeFilter = 'ALL'; // ALL, ABOVE_5000, GOLD, UPI

  @override
  void initState() {
    super.initState();
    _filtered = widget.entries;
  }

  void _filter(String query) {
    setState(() {
      _filtered = widget.entries.where((e) {
        final matchesQuery = e.guestName.toLowerCase().contains(query.toLowerCase()) ||
            e.villageCity.toLowerCase().contains(query.toLowerCase()) ||
            e.phoneNumber.contains(query) ||
            e.relation.toLowerCase().contains(query.toLowerCase()) ||
            e.itemName.toLowerCase().contains(query.toLowerCase());

        if (!matchesQuery) return false;

        if (_activeFilter == 'ABOVE_5000') return e.amount >= 5000;
        if (_activeFilter == 'GOLD') return e.giftType == 'GOLD';
        if (_activeFilter == 'UPI') return e.paymentMethod == 'UPI';

        return true;
      }).toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.canvasLight,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: Text(
          'స్మార్ట్ సెర్చ్ & ఫిల్టర్లు',
          style: GoogleFonts.playfairDisplay(fontWeight: FontWeight.w700, color: AppColors.textDark),
        ),
      ),
      body: Column(
        children: [
          // Search Input Bar
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
            child: TextField(
              controller: _searchController,
              decoration: InputDecoration(
                hintText: 'పేరు, ఊరు, ఫోన్ నంబర్, లేదా సంబంధం...',
                hintStyle: GoogleFonts.inter(fontSize: 14, color: AppColors.textMuted),
                prefixIcon: const Icon(Icons.search, color: AppColors.champagneGold),
                suffixIcon: IconButton(
                  icon: const Icon(Icons.mic, color: AppColors.lemonLime),
                  onPressed: () {
                    _searchController.text = 'మస్తాన్';
                    _filter('మస్తాన్');
                  },
                ),
                filled: true,
                fillColor: Colors.white,
                contentPadding: const EdgeInsets.symmetric(vertical: 14),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(20),
                  borderSide: const BorderSide(color: AppColors.borderLight),
                ),
                enabledBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(20),
                  borderSide: const BorderSide(color: AppColors.borderLight),
                ),
              ),
              onChanged: _filter,
            ),
          ),

          // Filter Chips
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
            child: Row(
              children: [
                _buildFilterChip('అన్నీ (All)', 'ALL'),
                const SizedBox(width: 8),
                _buildFilterChip('₹5,000 పైన ఇచ్చిన వారు', 'ABOVE_5000'),
                const SizedBox(width: 8),
                _buildFilterChip('బంగారం / వెండి', 'GOLD'),
                const SizedBox(width: 8),
                _buildFilterChip('UPI చెల్లింపులు', 'UPI'),
              ],
            ),
          ),

          const SizedBox(height: 10),

          // Search Results
          Expanded(
            child: _filtered.isEmpty
                ? Center(
                    child: Text(
                      'ఎటువంటి ఫలితాలు కనుగొనబడలేదు.',
                      style: GoogleFonts.inter(color: AppColors.textMuted),
                    ),
                  )
                : ListView.builder(
                    padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                    itemCount: _filtered.length,
                    itemBuilder: (context, index) {
                      final item = _filtered[index];
                      return GlassCard(
                        margin: const EdgeInsets.only(bottom: 10),
                        padding: const EdgeInsets.all(16),
                        child: Row(
                          children: [
                            CircleAvatar(
                              backgroundColor: AppColors.champagneGold.withOpacity(0.2),
                              child: Text(
                                item.guestName.isNotEmpty ? item.guestName.substring(0, 1) : '#',
                                style: GoogleFonts.inter(fontWeight: FontWeight.bold, color: AppColors.textDark),
                              ),
                            ),
                            const SizedBox(width: 14),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    item.guestName,
                                    style: GoogleFonts.inter(fontSize: 15, fontWeight: FontWeight.w700, color: AppColors.textDark),
                                  ),
                                  Text(
                                    '${item.villageCity} • ${item.relation} • Ph: ${item.phoneNumber}',
                                    style: GoogleFonts.inter(fontSize: 12, color: AppColors.textMuted),
                                  ),
                                ],
                              ),
                            ),
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.end,
                              children: [
                                if (item.giftType == 'CASH')
                                  Text(
                                    '₹${item.amount.toStringAsFixed(0)}',
                                    style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.w800, color: AppColors.success),
                                  )
                                else
                                  Text(
                                    item.itemName,
                                    style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.w700, color: AppColors.champagneGold),
                                  ),
                                Text(
                                  item.paymentMethod,
                                  style: GoogleFonts.inter(fontSize: 10, color: AppColors.textMuted),
                                ),
                              ],
                            ),
                          ],
                        ),
                      );
                    },
                  ),
          ),
        ],
      ),
    );
  }

  Widget _buildFilterChip(String label, String value) {
    final isSelected = _activeFilter == value;
    return ChoiceChip(
      label: Text(
        label,
        style: GoogleFonts.inter(
          fontSize: 12,
          fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
          color: isSelected ? AppColors.textDark : AppColors.textMuted,
        ),
      ),
      selected: isSelected,
      onSelected: (val) {
        if (val) {
          setState(() => _activeFilter = value);
          _filter(_searchController.text);
        }
      },
      selectedColor: AppColors.lemonLime,
      backgroundColor: Colors.white,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
    );
  }
}
