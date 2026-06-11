import React, { useState } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  StatusBar,
  StyleSheet,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

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
  },
  dark: {
    background: '#1C1C1E',
    card:       '#2C2C2E',
    primary:    '#FFFFFF',
    secondary:  '#AEAEB2',
    accent:     '#0A84FF',
    decrement:  '#FF453A',
    reset:      '#8E8E93',
    border:     '#3A3A3C',
  },
};

export default function App() {
  const [count, setCount]           = useState(0);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const theme = isDarkMode ? THEMES.dark : THEMES.light;

  const handleIncrement = () => setCount(prev => prev + 1);

  const handleDecrement = () => {
    if (count > 0) {
      setCount(prev => prev - 1);
    }
  };

  const handleReset = () => setCount(0);

  const toggleTheme = () => setIsDarkMode(prev => !prev);

  const counterColor          = count === 0 ? theme.secondary : theme.accent;
  const isDecrementDisabled   = count === 0;

  return (
    <SafeAreaView style={[styles.safe, { backgroundColor: theme.background }]}>

      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        backgroundColor={theme.background}
      />

      <View style={[styles.container, { backgroundColor: theme.background }]}>

        {/* Header */}
        <View style={styles.header}>
          <Text style={[styles.appTitle, { color: theme.secondary }]}>
            COUNTER
          </Text>
          <TouchableOpacity
            style={[styles.themeBtn, { backgroundColor: theme.card, borderColor: theme.border }]}
            onPress={toggleTheme}
            activeOpacity={0.7}
          >
            <Text style={[styles.themeBtnText, { color: theme.primary }]}>
              {isDarkMode ? '☀️  Light Mode' : '🌙  Dark Mode'}
            </Text>
          </TouchableOpacity>
        </View>

        {/* Counter Card */}
        <View style={[styles.card, { backgroundColor: theme.card, borderColor: theme.border }]}>
          <Text style={[styles.countLabel, { color: theme.secondary }]}>
            Current Count
          </Text>
          <Text style={[styles.countDisplay, { color: counterColor }]}>
            {count}
          </Text>
          {isDecrementDisabled && (
            <Text style={[styles.minNotice, { color: theme.secondary }]}>
              minimum reached
            </Text>
          )}
        </View>

        {/* Decrement + Increment Row */}
        <View style={styles.primaryRow}>

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
            <Text style={[styles.primaryBtnSymbol, { color: isDecrementDisabled ? theme.secondary : '#FFFFFF' }]}>
              −
            </Text>
            <Text style={[styles.primaryBtnLabel, { color: isDecrementDisabled ? theme.secondary : '#FFFFFF' }]}>
              Decrement
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.primaryBtn, { backgroundColor: theme.accent, borderColor: theme.accent }]}
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

        {/* Reset Button */}
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

        {/* Footer */}
        <Text style={[styles.footer, { color: theme.secondary }]}>
          {isDarkMode ? 'Dark Mode Active' : 'Light Mode Active'}
        </Text>

      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: {
    flex: 1,
  },
  container: {
    flex:             1,
    alignItems:       'center',
    justifyContent:   'center',
    paddingHorizontal: 24,
  },
  header: {
    width:          '100%',
    flexDirection:  'row',
    justifyContent: 'space-between',
    alignItems:     'center',
    marginBottom:   32,
  },
  appTitle: {
    fontSize:      13,
    fontWeight:    '700',
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
  card: {
    width:           '100%',
    alignItems:      'center',
    justifyContent:  'center',
    paddingVertical: 40,
    borderRadius:    24,
    borderWidth:     1,
    marginBottom:    28,
    elevation:       4,
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
  },
  minNotice: {
    marginTop:     8,
    fontSize:      12,
    fontWeight:    '500',
    letterSpacing: 1,
  },
  primaryRow: {
    flexDirection:  'row',
    justifyContent: 'space-between',
    width:          '100%',
    gap:            12,
    marginBottom:   12,
  },
  primaryBtn: {
    flex:            1,
    alignItems:      'center',
    justifyContent:  'center',
    paddingVertical: 20,
    borderRadius:    18,
    borderWidth:     1,
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
  footer: {
    fontSize:      12,
    fontWeight:    '500',
    letterSpacing: 1,
  },
});
