import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'core/theme/app_theme.dart';
import 'features/dashboard/dashboard_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const GiftVaultApp());
}

class GiftVaultApp extends StatelessWidget {
  const GiftVaultApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GiftVault - డిజిటల్ చదివింపుల లెడ్జర్',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale('te', 'IN'), // Telugu
        Locale('en', 'US'), // English
        Locale('hi', 'IN'), // Hindi
      ],
      home: const DashboardScreen(),
    );
  }
}
