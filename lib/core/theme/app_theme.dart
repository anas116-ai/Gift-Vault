import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'app_colors.dart';

class AppTheme {
  static ThemeData get lightTheme {
    return ThemeData(
      useMaterial3: true,
      scaffoldBackgroundColor: AppColors.canvasLight,
      colorScheme: const ColorScheme.light(
        primary: AppColors.lemonLime,
        secondary: AppColors.deepRose,
        surface: AppColors.surfaceCard,
        error: AppColors.error,
        onPrimary: AppColors.textDark,
        onSecondary: Colors.white,
        onSurface: AppColors.textDark,
      ),
      textTheme: TextTheme(
        displayLarge: GoogleFonts.cinzel(
          fontSize: 32,
          fontWeight: FontWeight.w800,
          color: AppColors.textDark,
          letterSpacing: -0.5,
        ),
        displayMedium: GoogleFonts.cinzel(
          fontSize: 26,
          fontWeight: FontWeight.w700,
          color: AppColors.textDark,
        ),
        headlineLarge: GoogleFonts.anekTelugu(
          fontSize: 22,
          fontWeight: FontWeight.w700,
          color: AppColors.textDark,
        ),
        headlineMedium: GoogleFonts.anekTelugu(
          fontSize: 18,
          fontWeight: FontWeight.w600,
          color: AppColors.textDark,
        ),
        bodyLarge: GoogleFonts.anekTelugu(
          fontSize: 16,
          fontWeight: FontWeight.w400,
          color: AppColors.textDark,
          height: 1.5,
        ),
        bodyMedium: GoogleFonts.anekTelugu(
          fontSize: 14,
          fontWeight: FontWeight.w400,
          color: AppColors.textMuted,
          height: 1.4,
        ),
        labelLarge: GoogleFonts.inter(
          fontSize: 16,
          fontWeight: FontWeight.w700,
          color: AppColors.textDark,
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: AppColors.lemonLime,
          foregroundColor: AppColors.textDark,
          minimumSize: const Size(double.infinity, 56), // Elder-friendly 56dp height
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20),
          ),
          elevation: 0,
          textStyle: GoogleFonts.inter(
            fontSize: 16,
            fontWeight: FontWeight.w800,
          ),
        ),
      ),
    );
  }
}
