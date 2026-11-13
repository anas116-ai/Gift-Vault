import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:intl/intl.dart';
import 'package:uuid/uuid.dart';
import '../../core/theme/app_colors.dart';
import '../../core/theme/glass_card.dart';
import '../../data/database/local_storage.dart';
import '../../data/models/event_model.dart';

class CreateEventScreen extends StatefulWidget {
  const CreateEventScreen({super.key});

  @override
  State<CreateEventScreen> createState() => _CreateEventScreenState();
}

class _CreateEventScreenState extends State<CreateEventScreen> {
  final _formKey = GlobalKey<FormState>();

  final TextEditingController _titleController = TextEditingController();
  final TextEditingController _personOneController = TextEditingController();
  final TextEditingController _personTwoController = TextEditingController();
  final TextEditingController _customCategoryController = TextEditingController();
  final TextEditingController _venueController = TextEditingController();
  final TextEditingController _cityController = TextEditingController();
  final TextEditingController _timeController = TextEditingController(text: '09:45 AM');
  final TextEditingController _tagController = TextEditingController(text: '#కుటుంబవేడుక');

  DateTime _selectedDate = DateTime.now();
  String _selectedCategory = 'Wedding'; // Wedding, Birthday, Housewarming, Naming, Custom

  // Event Rules
  String _photoRule = 'REQUIRED'; // REQUIRED, OPTIONAL, OFF
  String _videoRule = 'OPTIONAL';
  String _receiptRule = 'OPTIONAL';
  String _guestPhotoRule = 'OPTIONAL';
  bool _voiceNotesEnabled = true;

  Future<void> _pickDate() async {
    final picked = await showDatePicker(
      context: context,
      initialDate: _selectedDate,
      firstDate: DateTime(2020),
      lastDate: DateTime(2035),
      builder: (context, child) {
        return Theme(
          data: ThemeData.light().copyWith(
            colorScheme: const ColorScheme.light(
              primary: AppColors.champagneGold,
              onPrimary: Colors.white,
              onSurface: AppColors.textDark,
            ),
          ),
          child: child!,
        );
      },
    );
    if (picked != null) {
      setState(() => _selectedDate = picked);
    }
  }

  String get _personOneLabel {
    switch (_selectedCategory) {
      case 'Wedding':
      case 'Reception':
      case 'Engagement':
        return 'వరుడు పేరు (Groom Name)';
      case 'Birthday':
        return 'పుట్టినరోజు బాబు/పాప పేరు (Birthday Child)';
      case 'Housewarming':
        return 'యజమాని పేరు (Primary Owner)';
      case 'Naming':
        return 'చిన్నారి పేరు (Baby Name)';
      default:
        return 'ప్రధాన వ్యక్తి పేరు (Main Person)';
    }
  }

  String get _personTwoLabel {
    switch (_selectedCategory) {
      case 'Wedding':
      case 'Reception':
      case 'Engagement':
        return 'వధువు పేరు (Bride Name)';
      case 'Birthday':
        return 'వయస్సు (Age in Years)';
      case 'Housewarming':
        return 'యజమానురాలి పేరు (Spouse)';
      case 'Naming':
        return 'తల్లిదండ్రుల పేర్లు (Parents)';
      default:
        return 'రెండవ వ్యక్తి / కుటుంబం (Secondary / Family)';
    }
  }

  Future<void> _submitEvent() async {
    if (!_formKey.currentState!.validate()) return;

    final title = _titleController.text.trim();
    final p1 = _personOneController.text.trim();
    final p2 = _personTwoController.text.trim();

    final newEvent = EventModel(
      id: const Uuid().v4(),
      familyId: 'fam_001',
      name: title.isNotEmpty ? title : '$p1 & $p2 $_selectedCategory',
      eventType: _selectedCategory == 'Custom' ? _customCategoryController.text.trim() : _selectedCategory,
      groomName: p1,
      brideName: p2,
      eventDate: _selectedDate,
      muhurthamTime: _timeController.text.trim(),
      venue: _venueController.text.trim(),
      cityVillage: _cityController.text.trim(),
      hostName: '$p1 కుటుంబం',
      relationshipType: _selectedCategory,
      eventTag: _tagController.text.trim(),
      settings: EventSettings(
        photoRequirement: _photoRule,
        videoRequirement: _videoRule,
        receiptRequirement: _receiptRule,
        guestPhotoRequirement: _guestPhotoRule,
        voiceNotesEnabled: _voiceNotesEnabled,
      ),
    );

    await LocalStorageService.instance.saveEvent(newEvent);
    await LocalStorageService.instance.setActiveEventId(newEvent.id);

    if (!mounted) return;

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        backgroundColor: AppColors.success,
        content: Text(
          'ఫంక్షన్ "${newEvent.name}" సృష్టించబడింది!',
          style: GoogleFonts.inter(fontWeight: FontWeight.w600, color: Colors.white),
        ),
      ),
    );

    Navigator.pop(context, true);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.canvasLight,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        title: Text(
          'కొత్త ఫంక్షన్ సృష్టించండి',
          style: GoogleFonts.cinzel(fontWeight: FontWeight.w800, color: AppColors.textDark, fontSize: 18),
        ),
      ),
      body: Form(
        key: _formKey,
        child: ListView(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
          children: [
            GlassCard(
              margin: EdgeInsets.zero,
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Event Category Selector
                  Text('శుభకార్యం రకం (Event Category)*', style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 13)),
                  const SizedBox(height: 6),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 14),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(color: AppColors.borderLight),
                    ),
                    child: DropdownButtonHideUnderline(
                      child: DropdownButton<String>(
                        isExpanded: true,
                        value: _selectedCategory,
                        items: const [
                          DropdownMenuItem(value: 'Wedding', child: Text('💍 వివాహం (Wedding)')),
                          DropdownMenuItem(value: 'Reception', child: Text('🥂 రిసెప్షన్ (Reception)')),
                          DropdownMenuItem(value: 'Engagement', child: Text('💎 నిశ్చితార్థం (Engagement)')),
                          DropdownMenuItem(value: 'Birthday', child: Text('🎂 పుట్టినరోజు (Birthday)')),
                          DropdownMenuItem(value: 'Housewarming', child: Text('🏡 గృహప్రవేశం (Housewarming)')),
                          DropdownMenuItem(value: 'Naming', child: Text('👶 బారసాల / నామకరణం (Naming Ceremony)')),
                          DropdownMenuItem(value: 'Custom', child: Text('✨ ఇతర కొత్త ఫంక్షన్ (Custom / Other)')),
                        ],
                        onChanged: (val) {
                          if (val != null) setState(() => _selectedCategory = val);
                        },
                      ),
                    ),
                  ),

                  if (_selectedCategory == 'Custom') ...[
                    const SizedBox(height: 12),
                    Text('కొత్త ఫంక్షన్ పేరు రాయండి*', style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 13, color: AppColors.champagneGold)),
                    const SizedBox(height: 4),
                    TextFormField(
                      controller: _customCategoryController,
                      decoration: _buildInputDecoration('ఉదా: ప్రమోషన్ పార్టీ / వ్రతం'),
                      validator: (v) => _selectedCategory == 'Custom' && (v == null || v.trim().isEmpty) ? 'ఫంక్షన్ పేరు రాయండి' : null,
                    ),
                  ],

                  const SizedBox(height: 14),

                  // Event Title
                  Text('ఫంక్షన్ హెడ్‌లైన్ (Event Title)*', style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 13)),
                  const SizedBox(height: 6),
                  TextFormField(
                    controller: _titleController,
                    decoration: _buildInputDecoration('ఉదా: రమేష్ & సుజాత వివాహం'),
                    validator: (v) => (v == null || v.trim().isEmpty) ? 'ఫంక్షన్ పేరు అవసరం' : null,
                  ),

                  const SizedBox(height: 14),

                  // Dynamic Person Roles Container
                  Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.85),
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(color: AppColors.champagneGold.withOpacity(0.4)),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          children: [
                            const Icon(Icons.people_alt_outlined, color: AppColors.champagneGold, size: 18),
                            const SizedBox(width: 8),
                            Text(
                              'ప్రధాన వ్యక్తుల వివరాలు',
                              style: GoogleFonts.inter(fontWeight: FontWeight.w800, fontSize: 13, color: AppColors.textDark),
                            ),
                          ],
                        ),
                        const SizedBox(height: 10),
                        Row(
                          children: [
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(_personOneLabel, style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 11, color: AppColors.textMuted)),
                                  const SizedBox(height: 4),
                                  TextFormField(
                                    controller: _personOneController,
                                    decoration: _buildInputDecoration('పేరు'),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(width: 10),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(_personTwoLabel, style: GoogleFonts.inter(fontWeight: FontWeight.w600, fontSize: 11, color: AppColors.textMuted)),
                                  const SizedBox(height: 4),
                                  TextFormField(
                                    controller: _personTwoController,
                                    decoration: _buildInputDecoration('వివరాలు'),
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),

                  const SizedBox(height: 14),

                  // Date & Muhurtham Time
                  Row(
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('ఫంక్షన్ తేదీ*', style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 13)),
                            const SizedBox(height: 6),
                            InkWell(
                              onTap: _pickDate,
                              child: Container(
                                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 14),
                                decoration: BoxDecoration(
                                  color: Colors.white,
                                  borderRadius: BorderRadius.circular(16),
                                  border: Border.all(color: AppColors.borderLight),
                                ),
                                child: Text(
                                  DateFormat('dd MMM yyyy').format(_selectedDate),
                                  style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.bold, color: AppColors.textDark),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(width: 10),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('ముహూర్తం సమయం*', style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 13)),
                            const SizedBox(height: 6),
                            TextFormField(
                              controller: _timeController,
                              decoration: _buildInputDecoration('ఉదా: 09:45 AM'),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),

                  const SizedBox(height: 14),

                  // Venue & City
                  Row(
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('వేదిక / మండపం పేరు', style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 13)),
                            const SizedBox(height: 4),
                            TextFormField(
                              controller: _venueController,
                              decoration: _buildInputDecoration('కళ్యాణ వేదిక'),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(width: 10),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('ఊరు / నగరం*', style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 13)),
                            const SizedBox(height: 4),
                            TextFormField(
                              controller: _cityController,
                              decoration: _buildInputDecoration('విజయవాడ'),
                              validator: (v) => (v == null || v.trim().isEmpty) ? 'ఊరు అవసరం' : null,
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),

                  const SizedBox(height: 14),

                  // Event Tag
                  Text('ఫంక్షన్ ట్యాగ్ (Tag)', style: GoogleFonts.inter(fontWeight: FontWeight.w700, fontSize: 13)),
                  const SizedBox(height: 4),
                  TextFormField(
                    controller: _tagController,
                    decoration: _buildInputDecoration('#కుమారుడిపెళ్లి, #హల్దీవేడుక'),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 16),

            // Rules Card
            GlassCard(
              margin: EdgeInsets.zero,
              padding: const EdgeInsets.all(18),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'ఈ ఫంక్షన్ నియమాలు (Function Rules)',
                    style: GoogleFonts.cinzel(fontSize: 15, fontWeight: FontWeight.w700, color: AppColors.textDark),
                  ),
                  const SizedBox(height: 12),
                  _buildRuleDropdown(
                    label: 'గిఫ్ట్ ఫోటో (Gift Photo)',
                    value: _photoRule,
                    onChanged: (val) => setState(() => _photoRule = val!),
                  ),
                  const SizedBox(height: 10),
                  _buildRuleDropdown(
                    label: 'షార్ట్ వీడియో (Short Video)',
                    value: _videoRule,
                    onChanged: (val) => setState(() => _videoRule = val!),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 20),

            ElevatedButton(
              onPressed: _submitEvent,
              child: Text(
                'ఫంక్షన్ క్రియేట్ చేయి (Create Event)',
                style: GoogleFonts.inter(fontSize: 16, fontWeight: FontWeight.w800),
              ),
            ),

            const SizedBox(height: 30),
          ],
        ),
      ),
    );
  }

  Widget _buildRuleDropdown({
    required String label,
    required String value,
    required ValueChanged<String?> onChanged,
  }) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Expanded(
          child: Text(
            label,
            style: GoogleFonts.inter(fontSize: 13, fontWeight: FontWeight.w600, color: AppColors.textDark),
          ),
        ),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 10),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: AppColors.borderLight),
          ),
          child: DropdownButtonHideUnderline(
            child: DropdownButton<String>(
              value: value,
              items: const [
                DropdownMenuItem(value: 'REQUIRED', child: Text('కంపల్సరీ', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold))),
                DropdownMenuItem(value: 'OPTIONAL', child: Text('ఆప్షనల్', style: TextStyle(fontSize: 12))),
                DropdownMenuItem(value: 'OFF', child: Text('ఆఫ్', style: TextStyle(fontSize: 12))),
              ],
              onChanged: onChanged,
            ),
          ),
        ),
      ],
    );
  }

  InputDecoration _buildInputDecoration(String hint) {
    return InputDecoration(
      hintText: hint,
      hintStyle: GoogleFonts.inter(fontSize: 13, color: AppColors.textMuted.withOpacity(0.6)),
      filled: true,
      fillColor: Colors.white.withOpacity(0.8),
      contentPadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(14),
        borderSide: const BorderSide(color: AppColors.borderLight),
      ),
      enabledBorder: OutlineInputBorder(
        borderRadius: BorderRadius.circular(14),
        borderSide: const BorderSide(color: AppColors.borderLight),
      ),
    );
  }
}
