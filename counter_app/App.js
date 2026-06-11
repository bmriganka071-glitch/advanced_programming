/**
 * CounterApp — Expo Go Compatible
 * Digital counter with Light / Dark theme toggle.
 *
 * ✅ Works with: Expo Go (no Android Studio needed)
 * Run: npx expo start  →  scan QR with Expo Go app
 *
 * File: App.js  (place in the root of your Expo project)
 */

import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StatusBar,
  StyleSheet,
  SafeAreaView,
  Platform,
} from 'react-native';

// ─── Theme Definitions ────────────────────────────────────────────────────────

const THEMES = {
  light: {
    background: '#F2F2F7',
    card:       '#FFFFFF',
    primary:    '#1C1C1E',
    secondary:  '#6C6C70',
    accent:     '#0A84FF',
    decrement:  '#FF453A',
    reset:      '#636366',
    border:     '#E5E5EA',
    statusBar:  'dark-content',
  },
  dark: {
    background: '#1C1C1E',
    card:       '#2C2C2E',
    primary:    '#FFFFFF',
    secondary:  '#AEAEB2',   // solid hex (no alpha) — Expo-safe
    accent:     '#0A84FF',
    decrement:  '#FF453A',
    reset:      '#8E8E93',
    border:     '#3A3A3C',
    statusBar:  'light-content',
  },
};

// ─── App Component ────────────────────────────────────────────────────────────

export default function App() {

  // ── State ──────────────────────────────────────────────────────────────────
  const [count, setCount]           = useState(0);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const theme = isDarkMode ? THEMES.dark : THEMES.light;

  // ── Counter handlers ───────────────────────────────────────────────────────

  const handleIncrement = () => setCount(prev => prev + 1);

  const handleDecrement = () => {
    // Constraint check: never allow count to go below 0
    if (count > 0) {
      setCount(prev => prev - 1);
    }
  };

  const handleReset = () => setCount(0);

  // ── Theme handler ──────────────────────────────────────────────────────────

  const toggleTheme = () => setIsDarkMode(prev => !prev);

  // ── Derived values ─────────────────────────────────────────────────────────

  // Counter number turns blue when > 0, muted when at 0
  const counterColor = count === 0 ? theme.secondary : theme.accent;

  // Decrement button is visually disabled at 0
  const isDecrementDisabled = count === 0;

  // ── Render ─────────────────────────────────────────────────────────────────

  return (
    <SafeAreaView style={[styles.safe, { backgroundColor: theme.background }]}>

      {/* StatusBar adapts to light/dark mode */}
      <StatusBar
        barStyle={theme.statusBar}
        backgroundColor={theme.background}   // Android only
      />

      <View style={[styles.container, { backgroundColor: theme.background }]}>

        {/* ── Header row ── */}
        <View style={styles.header}>
          <Text style={[styles.appTitle, { color: theme.secondary }]}>
            COUNTER
          </Text>

          <TouchableOpacity
            style={[
              styles.themeBtn,
              { backgroundColor: theme.card, borderColor: theme.border },
            ]}
            onPress={toggleTheme}
            activeOpacity={0.7}
          >
            <Text style={[styles.themeBtnText, { color: theme.primary }]}>
              {isDarkMode ? '☀️  Light Mode' : '🌙  Dark Mode'}
            </Text>
          </TouchableOpacity>
        </View>

        {/* ── Counter display card ── */}
        <View
          style={[
            styles.card,
            {
              backgroundColor: theme.card,
              borderColor: theme.border,
              // Shadow works on iOS; elevation works on Android
              shadowColor: isDarkMode ? '#000000' : '#AAAAAA',
            },
          ]}
        >
          <Text style={[styles.countLabel, { color: theme.secondary }]}>
            Current Count
          </Text>

          <Text style={[styles.countDisplay, { color: counterColor }]}>
            {count}
          </Text>

          {/* Shown only when count is at its minimum */}
          {isDecrementDisabled && (
            <Text style={[styles.minNotice, { color: theme.secondary }]}>
              minimum reached
            </Text>
          )}
        </View>

        {/* ── Decrement + Increment (side-by-side) ── */}
        <View style={styles.primaryRow}>

          {/* Decrement */}
          <TouchableOpacity
            style={[
              styles.primaryBtn,
              {
                backgroundColor: isDecrementDisabled ? theme.card : theme.decrement,
                borderColor:     isDecrementDisabled ? theme.border : theme.decrement,
                opacity:         isDecrementDisabled ? 0.45 : 1,
              },
            ]}
            onPress={handleDecrement}
            activeOpacity={isDecrementDisabled ? 1 : 0.75}
          >
            <Text style={[
              styles.primaryBtnSymbol,
              { color: isDecrementDisabled ? theme.secondary : '#FFFFFF' },
            ]}>
              −
            </Text>
            <Text style={[
              styles.primaryBtnLabel,
              { color: isDecrementDisabled ? theme.secondary : '#FFFFFF' },
            ]}>
              Decrement
            </Text>
          </TouchableOpacity>

          {/* Increment */}
          <TouchableOpacity
            style={[
              styles.primaryBtn,
              { backgroundColor: theme.accent, borderColor: theme.accent },
            ]}
            onPress={handleIncrement}
            activeOpacity={0.75}
          >
            <Text style={[styles.primaryBtnSymbol, { color: '#FFFFFF' }]}>
              +
            </Text>
            <Text style={[styles.primaryBtnLabel, { color: '#FFFFFF' }]}>
              Increment
            </Text>
          </TouchableOpacity>

        </View>

        {/* ── Reset button ── */}
        <TouchableOpacity
          style={[
            styles.resetBtn,
            {
              backgroundColor: theme.card,
              borderColor:     theme.border,
              opacity: count === 0 ? 0.4 : 1,
            },
          ]}
          onPress={handleReset}
          activeOpacity={count === 0 ? 1 : 0.7}
        >
          <Text style={[styles.resetBtnText, { color: theme.reset }]}>
            ↺  Reset to Zero
          </Text>
        </TouchableOpacity>

        {/* ── Footer status ── */}
        <Text style={[styles.footer, { color: theme.secondary }]}>
          {isDarkMode ? 'Dark Mode Active' : 'Light Mode Active'}
        </Text>

      </View>
    </SafeAreaView>
  );
}

// ─── StyleSheet ───────────────────────────────────────────────────────────────

const styles = StyleSheet.create({

  safe: {
    flex: 1,
  },

  container: {
    flex: 1,
    alignItems:      'center',
    justifyContent:  'center',
    paddingHorizontal: 24,
  },

  // ── Header ──
  header: {
    width:           '100%',
    flexDirection:   'row',
    justifyContent:  'space-between',
    alignItems:      'center',
    marginBottom:    32,
  },
  appTitle: {
    fontSize:    13,
    fontWeight:  '700',
    letterSpacing: 3,
  },
  themeBtn: {
    paddingVertical:   8,
    paddingHorizontal: 14,
    borderRadius:      20,
    borderWidth:       1,
  },
  themeBtnText: {
    fontSize:   13,
    fontWeight: '600',
  },

  // ── Counter card ──
  card: {
    width:           '100%',
    alignItems:      'center',
    justifyContent:  'center',
    paddingVertical: 40,
    borderRadius:    24,
    borderWidth:     1,
    marginBottom:    28,
    // iOS shadow
    shadowOffset:  { width: 0, height: 4 },
    shadowOpacity: 0.10,
    shadowRadius:  12,
    // Android shadow
    elevation: 4,
  },
  countLabel: {
    fontSize:      12,
    fontWeight:    '600',
    letterSpacing: 2,
    textTransform: 'uppercase',
    marginBottom:  12,
  },
  countDisplay: {
    fontSize:      88,
    fontWeight:    '800',
    lineHeight:    96,
    letterSpacing: -2,
  },
  minNotice: {
    marginTop:     8,
    fontSize:      12,
    fontWeight:    '500',
    letterSpacing: 1,
  },

  // ── Primary row ──
  primaryRow: {
    flexDirection:   'row',
    justifyContent:  'space-between',
    width:           '100%',
    gap:             12,
    marginBottom:    12,
  },
  primaryBtn: {
    flex:           1,
    alignItems:     'center',
    justifyContent: 'center',
    paddingVertical: 20,
    borderRadius:   18,
    borderWidth:    1,
  },
  primaryBtnSymbol: {
    fontSize:   28,
    fontWeight: '300',
    lineHeight: 34,
  },
  primaryBtnLabel: {
    fontSize:      12,
    fontWeight:    '600',
    letterSpacing: 0.5,
    marginTop:     2,
  },

  // ── Reset button ──
  resetBtn: {
    width:           '100%',
    alignItems:      'center',
    justifyContent:  'center',
    paddingVertical: 16,
    borderRadius:    18,
    borderWidth:     1,
    marginBottom:    32,
  },
  resetBtnText: {
    fontSize:      15,
    fontWeight:    '600',
    letterSpacing: 0.3,
  },

  // ── Footer ──
  footer: {
    fontSize:      12,
    fontWeight:    '500',
    letterSpacing: 1,
  },
});
