import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/glass_card.dart';

class SubscriptionScreen extends StatelessWidget {
  const SubscriptionScreen({super.key});

  void _checkoutPlan(BuildContext context, String planTitle, int price) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text('✓ ₹$price Razorpay / UPI గేట్‌వే కనెక్ట్ అవుతోంది... ($planTitle)'),
        backgroundColor: AppColors.champagneGold,
        behavior: SnackBarBehavior.floating,
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
          'రాయల్ ఫ్యామిలీ పాస్',
          style: GoogleFonts.suranna(
            fontWeight: FontWeight.bold,
            color: AppColors.textDark,
          ),
        ),
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            children: [
              Text(
                'మీ కుటుంబ శుభకార్యానికి అపరిమిత అధికారాలు',
                style: GoogleFonts.anekTelugu(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: AppColors.textDark,
                ),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 6),
              Text(
                'ఎలాంటి ఎంట్రీ లిమిట్స్ లేకుండా, ఎంతమంది కుటుంబ సభ్యులైనా కౌంటర్లలో పనిచేసే రాయల్ సౌలభ్యం.',
                style: GoogleFonts.anekTelugu(
                  fontSize: 12,
                  color: AppColors.textMuted,
                ),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 20),

              // Plan 1: Royal Event Pass (₹999)
              GlassCard(
                borderColor: AppColors.champagneGold,
                child: Padding(
                  padding: const EdgeInsets.all(18.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            'రాయల్ ఈవెంట్ పాస్',
                            style: GoogleFonts.suranna(
                              fontSize: 18,
                              fontWeight: FontWeight.bold,
                              color: AppColors.textDark,
                            ),
                          ),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                            decoration: BoxDecoration(
                              color: AppColors.lemonLime,
                              borderRadius: BorderRadius.circular(8),
                            ),
                            child: const Text(
                              'MOST POPULAR',
                              style: TextStyle(
                                fontSize: 9,
                                fontWeight: FontWeight.bold,
                                color: AppColors.textDark,
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 8),
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.baseline,
                        textBaseline: TextBaseline.alphabetic,
                        children: [
                          Text(
                            '₹999',
                            style: GoogleFonts.cinzel(
                              fontSize: 28,
                              fontWeight: FontWeight.w900,
                              color: AppColors.textDark,
                            ),
                          ),
                          const SizedBox(width: 4),
                          Text(
                            '/ ఒక శుభకార్యానికి (లైఫ్‌టైమ్ రికార్డ్)',
                            style: GoogleFonts.anekTelugu(
                              fontSize: 11,
                              color: AppColors.textMuted,
                            ),
                          ),
                        ],
                      ),
                      const Divider(height: 24),
                      _buildBullet('అపరిమిత చదివింపు ఎంట్రీలు (No Limit)'),
                      _buildBullet('అపరిమిత కౌంటర్ ఆపరేటర్ల ఆహ్వానం'),
                      _buildBullet('4K ఫోటో & షార్ట్ వీడియో ప్రూఫ్'),
                      _buildBullet('అతిథులకు ఆటోమేటిక్ WhatsApp ధన్యవాదాల SMS'),
                      _buildBullet('ఎరుపు బాహీఖాతా PDF & Excel షీట్'),
                      const SizedBox(height: 16),
                      SizedBox(
                        width: double.infinity,
                        height: 48,
                        child: ElevatedButton(
                          style: ElevatedButton.styleFrom(
                            backgroundColor: AppColors.lemonLime,
                            foregroundColor: AppColors.textDark,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(14),
                            ),
                          ),
                          onPressed: () => _checkoutPlan(context, 'రాయల్ ఈవెంట్ పాస్', 999),
                          child: const Text(
                            '₹999 తో ప్రారంభించండి →',
                            style: TextStyle(fontWeight: FontWeight.bold),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              const SizedBox(height: 16),

              // Plan 2: Shagun Pro Annual (₹2,499)
              GlassCard(
                child: Padding(
                  padding: const EdgeInsets.all(18.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'షగున్ ప్రో వార్షిక ప్లాన్',
                        style: GoogleFonts.suranna(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          color: AppColors.textDark,
                        ),
                      ),
                      const SizedBox(height: 8),
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.baseline,
                        textBaseline: TextBaseline.alphabetic,
                        children: [
                          Text(
                            '₹2,499',
                            style: GoogleFonts.cinzel(
                              fontSize: 28,
                              fontWeight: FontWeight.w900,
                              color: AppColors.textDark,
                            ),
                          ),
                          const SizedBox(width: 4),
                          Text(
                            '/ సంవత్సరానికి',
                            style: GoogleFonts.anekTelugu(
                              fontSize: 11,
                              color: AppColors.textMuted,
                            ),
                          ),
                        ],
                      ),
                      const Divider(height: 24),
                      _buildBullet('అపరిమిత శుభకార్యాలు (వివాహం, గృహప్రవేశం, బారసాల)'),
                      _buildBullet('జీవితాంతం "ఇచ్చినవి vs వచ్చినవి" లెడ్జర్'),
                      _buildBullet('గూగుల్ డ్రైవ్ ఆటోమేటెడ్ క్లౌడ్ బ్యాకప్'),
                      _buildBullet('VIP కస్టమర్ కేర్ సపోర్ట్'),
                      const SizedBox(height: 16),
                      SizedBox(
                        width: double.infinity,
                        height: 48,
                        child: OutlinedButton(
                          style: OutlinedButton.styleFrom(
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(14),
                            ),
                          ),
                          onPressed: () => _checkoutPlan(context, 'షగున్ ప్రో వార్షిక ప్లాన్', 2499),
                          child: const Text(
                            'వార్షిక ప్లాన్ ఎంచుకోండి',
                            style: TextStyle(
                              fontWeight: FontWeight.bold,
                              color: AppColors.textDark,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildBullet(String text) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 3.0),
      child: Row(
        children: [
          const Icon(Icons.check_circle, size: 16, color: AppColors.success),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              text,
              style: GoogleFonts.anekTelugu(
                fontSize: 12,
                color: AppColors.textDark,
              ),
            ),
          ),
        ],
      ),
    );
  }
}
