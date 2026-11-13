import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:qr_flutter/qr_flutter.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/glass_card.dart';
import '../../data/models/event_model.dart';

class QrPaymentScreen extends StatefulWidget {
  final EventModel event;

  const QrPaymentScreen({super.key, required this.event});

  @override
  State<QrPaymentScreen> createState() => _QrPaymentScreenState();
}

class _QrPaymentScreenState extends State<QrPaymentScreen> {
  final TextEditingController _amountController = TextEditingController(text: '2100');
  final TextEditingController _guestNameController = TextEditingController();
  bool _isPaid = false;

  String get _upiPayload {
    final amt = _amountController.text.trim();
    return 'upi://pay?pa=giftvault.family@okhdfcbank&pn=GiftVaultLedger&am=$amt&cu=INR&tn=${widget.event.name}';
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.canvasLight,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: Text(
          'UPI / QR పేమెంట్ కౌంటర్',
          style: GoogleFonts.playfairDisplay(fontWeight: FontWeight.w700, color: AppColors.textDark),
        ),
      ),
      body: ListView(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        children: [
          if (_isPaid) ...[
            // Success Card with celebratory animation
            GlassCard(
              padding: const EdgeInsets.all(28),
              margin: const EdgeInsets.symmetric(vertical: 20),
              child: Column(
                children: [
                  Container(
                    width: 70,
                    height: 70,
                    decoration: const BoxDecoration(
                      color: AppColors.success,
                      shape: BoxShape.circle,
                    ),
                    child: const Icon(Icons.check, color: Colors.white, size: 44),
                  ),
                  const SizedBox(height: 16),
                  Text(
                    'చెల్లింపు విజయవంతమైంది!',
                    style: GoogleFonts.playfairDisplay(fontSize: 22, fontWeight: FontWeight.w800, color: AppColors.success),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '₹${_amountController.text} నమోదైంది',
                    style: GoogleFonts.inter(fontSize: 26, fontWeight: FontWeight.w900, color: AppColors.textDark),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    _guestNameController.text.isNotEmpty ? 'బంధువు: ${_guestNameController.text}' : 'నగదు రహిత చదివింపులు',
                    style: GoogleFonts.inter(fontSize: 14, color: AppColors.textMuted),
                  ),
                  const SizedBox(height: 24),
                  ElevatedButton(
                    onPressed: () => Navigator.pop(context),
                    child: const Text('డ్యాష్‌బోర్డ్‌కు వెళ్ళు'),
                  ),
                ],
              ),
            ),
          ] else ...[
            // QR Display Card
            GlassCard(
              margin: EdgeInsets.zero,
              padding: const EdgeInsets.all(24),
              child: Column(
                children: [
                  Text(
                    widget.event.name,
                    style: GoogleFonts.playfairDisplay(fontSize: 18, fontWeight: FontWeight.w700, color: AppColors.textDark),
                  ),
                  Text(
                    'స్కాన్ చేసి నేరుగా చదివింపులు చెల్లించండి',
                    style: GoogleFonts.inter(fontSize: 13, color: AppColors.textMuted),
                  ),
                  const SizedBox(height: 20),

                  // QR Code
                  Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.06),
                          blurRadius: 16,
                          offset: const Offset(0, 4),
                        ),
                      ],
                    ),
                    child: QrImageView(
                      data: _upiPayload,
                      version: QrVersions.auto,
                      size: 210.0,
                      embeddedImage: null,
                    ),
                  ),

                  const SizedBox(height: 20),

                  // Quick Amount Chips
                  Text(
                    'అమౌంట్ (Amount ₹)',
                    style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.w600, color: AppColors.textMuted),
                  ),
                  const SizedBox(height: 6),
                  SizedBox(
                    width: 160,
                    child: TextField(
                      controller: _amountController,
                      textAlign: TextAlign.center,
                      keyboardType: TextInputType.number,
                      style: GoogleFonts.inter(fontSize: 26, fontWeight: FontWeight.w800, color: AppColors.textDark),
                      decoration: InputDecoration(
                        prefixText: '₹ ',
                        contentPadding: const EdgeInsets.symmetric(vertical: 8),
                        border: OutlineInputBorder(borderRadius: BorderRadius.circular(14)),
                      ),
                      onChanged: (_) => setState(() {}),
                    ),
                  ),

                  const SizedBox(height: 12),

                  Wrap(
                    spacing: 8,
                    children: [501, 1100, 2100, 5100].map((amt) {
                      return ActionChip(
                        label: Text('₹$amt'),
                        backgroundColor: Colors.white,
                        onPressed: () {
                          setState(() {
                            _amountController.text = amt.toString();
                          });
                        },
                      );
                    }).toList(),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 16),

            // Guest Name
            GlassCard(
              margin: EdgeInsets.zero,
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('చెల్లించే బంధువు పేరు (ఆప్షనల్)', style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.w600)),
                  const SizedBox(height: 6),
                  TextField(
                    controller: _guestNameController,
                    decoration: InputDecoration(
                      hintText: 'పేరు ఎంటర్ చేయండి',
                      filled: true,
                      fillColor: Colors.white.withOpacity(0.8),
                      border: OutlineInputBorder(borderRadius: BorderRadius.circular(14)),
                    ),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 20),

            // Mark as Received CTA
            ElevatedButton.icon(
              onPressed: () {
                setState(() => _isPaid = true);
              },
              icon: const Icon(Icons.check_circle_outline, color: AppColors.textDark),
              label: Text(
                'పేమెంట్ వచ్చింది (Mark as Received)',
                style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.w800),
              ),
            ),
          ],
        ],
      ),
    );
  }
}
