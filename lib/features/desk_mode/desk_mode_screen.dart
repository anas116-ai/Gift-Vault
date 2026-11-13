import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:uuid/uuid.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/glass_card.dart';
import '../../data/database/local_storage.dart';
import '../../data/models/event_model.dart';
import '../../data/models/gift_entry_model.dart';

class DeskModeScreen extends StatefulWidget {
  final EventModel event;

  const DeskModeScreen({super.key, required this.event});

  @override
  State<DeskModeScreen> createState() => _DeskModeScreenState();
}

class _DeskModeScreenState extends State<DeskModeScreen> {
  final _formKey = GlobalKey<FormState>();
  int _currentSerial = 1;

  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _phoneController = TextEditingController();
  final TextEditingController _villageController = TextEditingController();
  final TextEditingController _relationController = TextEditingController();
  final TextEditingController _amountController = TextEditingController();
  final TextEditingController _itemNameController = TextEditingController();
  final TextEditingController _quantityController = TextEditingController();
  final TextEditingController _estimatedValueController = TextEditingController();
  final TextEditingController _notesController = TextEditingController();

  String _selectedGiftType = 'CASH'; // CASH, GOLD, ITEM, GIFT, OTHER
  String _selectedPaymentMethod = 'CASH'; // CASH, UPI, QR, CHEQUE, OTHER
  bool _isVoiceRecording = false;
  bool _hasPhotoAttached = false;
  bool _hasReceiptAttached = false;

  @override
  void initState() {
    super.initState();
    _loadNextSerial();
  }

  Future<void> _loadNextSerial() async {
    final next = await LocalStorageService.instance.getNextSerialNumber(widget.event.id);
    setState(() {
      _currentSerial = next;
    });
  }

  void _quickAddAmount(int add) {
    final current = double.tryParse(_amountController.text) ?? 0.0;
    setState(() {
      _amountController.text = (current + add).toInt().toString();
    });
  }

  Future<void> _saveEntry({bool addAnother = true}) async {
    if (!_formKey.currentState!.validate()) return;

    final entry = GiftEntryModel(
      id: const Uuid().v4(),
      eventId: widget.event.id,
      serialNumber: _currentSerial,
      guestName: _nameController.text.trim(),
      phoneNumber: _phoneController.text.trim(),
      villageCity: _villageController.text.trim(),
      relation: _relationController.text.trim(),
      giftType: _selectedGiftType,
      amount: double.tryParse(_amountController.text) ?? 0.0,
      itemName: _itemNameController.text.trim(),
      quantity: _quantityController.text.trim(),
      estimatedValue: double.tryParse(_estimatedValueController.text) ?? 0.0,
      paymentMethod: _selectedPaymentMethod,
      photoUrl: _hasPhotoAttached ? 'local_camera_capture.jpg' : null,
      receiptUrl: _hasReceiptAttached ? 'local_receipt_proof.jpg' : null,
      notes: _notesController.text.trim(),
      createdByName: 'మున్షీ / అకౌంట్ ఓనర్',
      createdAt: DateTime.now(),
      updatedAt: DateTime.now(),
    );

    await LocalStorageService.instance.saveEntry(entry);

    if (!mounted) return;

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        backgroundColor: AppColors.success,
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        content: Row(
          children: [
            const Icon(Icons.check_circle, color: Colors.white),
            const SizedBox(width: 12),
            Text(
              'ఎంట్రీ #$_currentSerial విజయవంతంగా నమోదైంది!',
              style: GoogleFonts.inter(fontWeight: FontWeight.w600, color: Colors.white),
            ),
          ],
        ),
      ),
    );

    if (addAnother) {
      _resetForm();
    } else {
      Navigator.pop(context, true);
    }
  }

  void _resetForm() {
    _nameController.clear();
    _phoneController.clear();
    _villageController.clear();
    _relationController.clear();
    _amountController.clear();
    _itemNameController.clear();
    _quantityController.clear();
    _estimatedValueController.clear();
    _notesController.clear();
    setState(() {
      _currentSerial++;
      _hasPhotoAttached = false;
      _hasReceiptAttached = false;
    });
  }

  // Voice recognition simulation (Sarvam AI style)
  void _toggleVoiceInput() {
    setState(() {
      _isVoiceRecording = !_isVoiceRecording;
    });

    if (_isVoiceRecording) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          backgroundColor: AppColors.canvasDark,
          content: Text(
            'మాట్లాడండి... (ఉదా: "మస్తాన్ రావు, తెనాలి, ఐదు వేల రూపాయలు క్యాష్")',
            style: GoogleFonts.inter(color: AppColors.lemonLime),
          ),
          duration: const Duration(seconds: 3),
        ),
      );

      // Simulate parsing spoken Telugu
      Future.delayed(const Duration(seconds: 2), () {
        if (mounted && _isVoiceRecording) {
          setState(() {
            _nameController.text = 'కె. రమేష్ బాబు';
            _villageController.text = 'గుంటూరు';
            _relationController.text = 'స్నేహితుడు';
            _amountController.text = '5000';
            _selectedGiftType = 'CASH';
            _isVoiceRecording = false;
          });
        }
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.canvasLight,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              widget.event.name,
              style: GoogleFonts.playfairDisplay(
                fontSize: 18,
                fontWeight: FontWeight.w700,
                color: AppColors.textDark,
              ),
            ),
            Text(
              'హై-స్పీడ్ డెస్క్ మోడ్ (కౌంటర్ ఎంట్రీ)',
              style: GoogleFonts.inter(fontSize: 12, color: AppColors.textMuted),
            ),
          ],
        ),
        actions: [
          Container(
            margin: const EdgeInsets.only(right: 16),
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
            decoration: BoxDecoration(
              color: AppColors.lemonLime,
              borderRadius: BorderRadius.circular(20),
            ),
            child: Row(
              children: [
                const Icon(Icons.confirmation_number_outlined, size: 16, color: AppColors.textDark),
                const SizedBox(width: 6),
                Text(
                  'నంబర్: $_currentSerial',
                  style: GoogleFonts.inter(fontWeight: FontWeight.w800, color: AppColors.textDark),
                ),
              ],
            ),
          ),
        ],
      ),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          children: [
            // Voice Input Quick Action Bar
            GlassCard(
              margin: const EdgeInsets.only(bottom: 12),
              padding: const EdgeInsets.all(14),
              child: Row(
                children: [
                  GestureDetector(
                    onTap: _toggleVoiceInput,
                    child: Container(
                      width: 50,
                      height: 50,
                      decoration: BoxDecoration(
                        color: _isVoiceRecording ? AppColors.deepRose : AppColors.lemonLime,
                        shape: BoxShape.circle,
                        boxShadow: [
                          BoxShadow(
                            color: (_isVoiceRecording ? AppColors.deepRose : AppColors.lemonLime).withOpacity(0.35),
                            blurRadius: 12,
                            spreadRadius: 2,
                          ),
                        ],
                      ),
                      child: Icon(
                        _isVoiceRecording ? Icons.mic : Icons.mic_none,
                        color: _isVoiceRecording ? Colors.white : AppColors.textDark,
                        size: 26,
                      ),
                    ),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          _isVoiceRecording ? 'వింటున్నాము... మాట్లాడండి' : 'స్పీచ్-టు-టెక్స్ట్ (వాయిస్ ఎంట్రీ)',
                          style: GoogleFonts.inter(
                            fontWeight: FontWeight.w700,
                            fontSize: 14,
                            color: _isVoiceRecording ? AppColors.deepRose : AppColors.textDark,
                          ),
                        ),
                        Text(
                          'తెలుగు లేదా ఇంగ్లీష్‌లో పేరు, ఊరు, అమౌంట్ చెప్పండి',
                          style: GoogleFonts.inter(fontSize: 12, color: AppColors.textMuted),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),

            // Gift Type Selector Chips
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 6),
              child: SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  children: [
                    _buildTypeChip('డబ్బు (Cash)', 'CASH', Icons.account_balance_wallet_outlined),
                    const SizedBox(width: 8),
                    _buildTypeChip('బంగారం / వెండి (Gold)', 'GOLD', Icons.diamond_outlined),
                    const SizedBox(width: 8),
                    _buildTypeChip('చీరలు / బట్టలు (Clothes)', 'ITEM', Icons.checkroom_outlined),
                    const SizedBox(width: 8),
                    _buildTypeChip('గిఫ్ట్ వస్తువులు', 'GIFT', Icons.card_giftcard_outlined),
                    const SizedBox(width: 8),
                    _buildTypeChip('ఇతరములు', 'OTHER', Icons.more_horiz),
                  ],
                ),
              ),
            ),

            const SizedBox(height: 10),

            // Main Details Glass Container
            GlassCard(
              padding: const EdgeInsets.all(20),
              margin: EdgeInsets.zero,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Amount Field (Large display for Cash)
                  if (_selectedGiftType == 'CASH') ...[
                    Text(
                      'చదివింపుల అమౌంట్ (₹ Amount)*',
                      style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 14),
                    ),
                    const SizedBox(height: 6),
                    TextFormField(
                      controller: _amountController,
                      keyboardType: TextInputType.number,
                      style: GoogleFonts.inter(
                        fontSize: 28,
                        fontWeight: FontWeight.w800,
                        color: AppColors.textDark,
                      ),
                      decoration: InputDecoration(
                        prefixIcon: const Padding(
                          padding: EdgeInsets.symmetric(horizontal: 12),
                          child: Text('₹', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: AppColors.champagneGold)),
                        ),
                        prefixIconConstraints: const BoxConstraints(minWidth: 0, minHeight: 0),
                        hintText: '500',
                        filled: true,
                        fillColor: Colors.white.withOpacity(0.7),
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(16),
                          borderSide: const BorderSide(color: AppColors.borderLight),
                        ),
                      ),
                      validator: (val) {
                        if (_selectedGiftType == 'CASH' && (val == null || val.trim().isEmpty)) {
                          return 'దయచేసి అమౌంట్ ఎంటర్ చేయండి';
                        }
                        return null;
                      },
                    ),

                    const SizedBox(height: 8),

                    // Quick Chips for Indian Traditional Shagun Amounts (+501, +1100, +2100, +5100)
                    Wrap(
                      spacing: 8,
                      children: [
                        _buildQuickAmountChip(501),
                        _buildQuickAmountChip(1100),
                        _buildQuickAmountChip(2100),
                        _buildQuickAmountChip(5100),
                        _buildQuickAmountChip(10000),
                      ],
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Non-Cash Fields (Gold, Sarees, Items)
                  if (_selectedGiftType != 'CASH') ...[
                    Text(
                      'వస్తువు / గిఫ్ట్ వివరాలు (Item Name)*',
                      style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 14),
                    ),
                    const SizedBox(height: 6),
                    TextFormField(
                      controller: _itemNameController,
                      decoration: _buildInputDecoration('ఉదా: పట్టుచీర, బంగారు గొలుసు, వెండి పాత్ర...'),
                      validator: (val) {
                        if (_selectedGiftType != 'CASH' && (val == null || val.trim().isEmpty)) {
                          return 'వస్తువు పేరు రాయండి';
                        }
                        return null;
                      },
                    ),
                    const SizedBox(height: 12),
                    Row(
                      children: [
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text('పరిమాణం (Quantity)', style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 13)),
                              const SizedBox(height: 4),
                              TextFormField(
                                controller: _quantityController,
                                decoration: _buildInputDecoration('ఉదా: 2 గ్రాములు / 1 జత'),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text('అంచనా విలువ (₹ Est.)', style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 13)),
                              const SizedBox(height: 4),
                              TextFormField(
                                controller: _estimatedValueController,
                                keyboardType: TextInputType.number,
                                decoration: _buildInputDecoration('₹ విలువ'),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Guest Name (Required)
                  Text(
                    'ఇచ్చిన వారి పేరు (Guest Name)*',
                    style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 14),
                  ),
                  const SizedBox(height: 6),
                  TextFormField(
                    controller: _nameController,
                    style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.w600),
                    decoration: _buildInputDecoration('పూర్తి పేరు (ఉదా: కాకర్ల రామకృష్ణ)'),
                    validator: (val) => (val == null || val.trim().isEmpty) ? 'పేరు తప్పనిసరి' : null,
                  ),

                  const SizedBox(height: 12),

                  // Village / Town & Phone Number
                  Row(
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('ఊరు / నగరం (Village)', style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 13)),
                            const SizedBox(height: 4),
                            TextFormField(
                              controller: _villageController,
                              decoration: _buildInputDecoration('ఊరి పేరు'),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('ఫోన్ నంబర్ (Phone)', style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 13)),
                            const SizedBox(height: 4),
                            TextFormField(
                              controller: _phoneController,
                              keyboardType: TextInputType.phone,
                              decoration: _buildInputDecoration('10 అంకెల నంబర్'),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),

                  const SizedBox(height: 12),

                  // Relationship
                  Text('సంబంధం (Relationship)', style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 13)),
                  const SizedBox(height: 4),
                  TextFormField(
                    controller: _relationController,
                    decoration: _buildInputDecoration('ఉదా: మేనమామ, బాబాయ్, స్నేహితుడు, సహోద్యోగి'),
                  ),

                  const SizedBox(height: 16),

                  // Payment Method Options
                  Text('చెల్లింపు మార్గం (Payment Mode)', style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 13)),
                  const SizedBox(height: 6),
                  SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(
                      children: [
                        _buildPaymentChip('క్యాష్ (Cash)', 'CASH'),
                        const SizedBox(width: 6),
                        _buildPaymentChip('Google Pay / PhonePe (UPI)', 'UPI'),
                        const SizedBox(width: 6),
                        _buildPaymentChip('QR స్కాన్', 'QR'),
                        const SizedBox(width: 6),
                        _buildPaymentChip('చెక్ (Cheque)', 'CHEQUE'),
                      ],
                    ),
                  ),

                  const SizedBox(height: 16),

                  // Proof Attachments (Photo, Receipt)
                  Row(
                    children: [
                      Expanded(
                        child: OutlinedButton.icon(
                          onPressed: () {
                            setState(() {
                              _hasPhotoAttached = !_hasPhotoAttached;
                            });
                          },
                          icon: Icon(
                            _hasPhotoAttached ? Icons.check_circle : Icons.camera_alt_outlined,
                            color: _hasPhotoAttached ? AppColors.success : AppColors.textDark,
                          ),
                          label: Text(
                            _hasPhotoAttached ? 'ఫోటో రెడీ' : 'గిఫ్ట్ ఫోటో',
                            style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.w600),
                          ),
                          style: OutlinedButton.styleFrom(
                            side: BorderSide(
                              color: _hasPhotoAttached ? AppColors.success : AppColors.borderLight,
                              width: 1.5,
                            ),
                            padding: const EdgeInsets.symmetric(vertical: 14),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                          ),
                        ),
                      ),
                      const SizedBox(width: 10),
                      Expanded(
                        child: OutlinedButton.icon(
                          onPressed: () {
                            setState(() {
                              _hasReceiptAttached = !_hasReceiptAttached;
                            });
                          },
                          icon: Icon(
                            _hasReceiptAttached ? Icons.check_circle : Icons.receipt_long_outlined,
                            color: _hasReceiptAttached ? AppColors.success : AppColors.textDark,
                          ),
                          label: Text(
                            _hasReceiptAttached ? 'రశీదు రెడీ' : 'UPI రశీదు',
                            style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.w600),
                          ),
                          style: OutlinedButton.styleFrom(
                            side: BorderSide(
                              color: _hasReceiptAttached ? AppColors.success : AppColors.borderLight,
                              width: 1.5,
                            ),
                            padding: const EdgeInsets.symmetric(vertical: 14),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),

            const SizedBox(height: 20),

            // Continuous Save & Next Button
            ElevatedButton(
              onPressed: () => _saveEntry(addAnother: true),
              style: ElevatedButton.styleFrom(
                backgroundColor: AppColors.lemonLime,
                foregroundColor: AppColors.textDark,
                minimumSize: const Size(double.infinity, 60), // Extra large elder-friendly CTA
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(Icons.save_outlined, color: AppColors.textDark, size: 24),
                  const SizedBox(width: 10),
                  Text(
                    'సేవ్ చేసి తర్వాతి ఎంట్రీ (Save & Next)',
                    style: GoogleFonts.inter(fontSize: 17, fontWeight: FontWeight.w800),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 10),

            // Just Save & Close
            TextButton(
              onPressed: () => _saveEntry(addAnother: false),
              child: Text(
                'సేవ్ చేసి ముగించు (Save & Finish)',
                style: GoogleFonts.inter(
                  color: AppColors.textMuted,
                  fontSize: 14,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),

            const SizedBox(height: 30),
          ],
        ),
      ),
    );
  }

  Widget _buildTypeChip(String label, String value, IconData icon) {
    final isSelected = _selectedGiftType == value;
    return ChoiceChip(
      label: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 16, color: isSelected ? AppColors.textDark : AppColors.textMuted),
          const SizedBox(width: 6),
          Text(
            label,
            style: GoogleFonts.inter(
              fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
              color: isSelected ? AppColors.textDark : AppColors.textMuted,
            ),
          ),
        ],
      ),
      selected: isSelected,
      onSelected: (val) {
        if (val) setState(() => _selectedGiftType = value);
      },
      selectedColor: AppColors.lemonLime,
      backgroundColor: Colors.white.withOpacity(0.8),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: BorderSide(color: isSelected ? AppColors.lemonLime : AppColors.borderLight),
      ),
    );
  }

  Widget _buildPaymentChip(String label, String value) {
    final isSelected = _selectedPaymentMethod == value;
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
        if (val) setState(() => _selectedPaymentMethod = value);
      },
      selectedColor: AppColors.champagneGold.withOpacity(0.3),
      backgroundColor: Colors.white.withOpacity(0.7),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: BorderSide(color: isSelected ? AppColors.champagneGold : AppColors.borderLight),
      ),
    );
  }

  Widget _buildQuickAmountChip(int amount) {
    return ActionChip(
      label: Text(
        '+₹$amount',
        style: GoogleFonts.inter(fontSize: 12, fontWeight: FontWeight.w700, color: AppColors.textDark),
      ),
      backgroundColor: Colors.white,
      side: const BorderSide(color: AppColors.borderLight),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      onPressed: () => _quickAddAmount(amount),
    );
  }

  InputDecoration _buildInputDecoration(String hint) {
    return InputDecoration(
      hintText: hint,
      hintStyle: GoogleFonts.inter(fontSize: 14, color: AppColors.textMuted.withOpacity(0.6)),
      filled: true,
      fillColor: Colors.white.withOpacity(0.7),
      contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(16),
        borderSide: const BorderSide(color: AppColors.borderLight),
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(16),
        borderSide: const BorderSide(color: AppColors.borderLight),
      ),
      focusedBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(16),
        borderSide: const BorderSide(color: AppColors.champagneGold, width: 1.5),
      ),
    );
  }
}
