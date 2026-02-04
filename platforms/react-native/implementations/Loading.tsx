/**
 * Loading Skeleton Component - React Native
 *
 * Native implementation using React Native's Animated API.
 * Respects accessibility settings.
 *
 * @see patterns/feedback/loading.md for UX intent
 */

import React, { useEffect, useRef } from 'react';
import {
  View,
  Animated,
  StyleSheet,
  AccessibilityInfo,
  ViewStyle,
} from 'react-native';

// Hook to detect reduced motion preference
function useReducedMotion(): boolean {
  const [reduced, setReduced] = React.useState(false);

  useEffect(() => {
    AccessibilityInfo.isReduceMotionEnabled().then(setReduced);

    const subscription = AccessibilityInfo.addEventListener(
      'reduceMotionChanged',
      setReduced
    );

    return () => subscription.remove();
  }, []);

  return reduced;
}

interface SkeletonProps {
  width?: number | string;
  height?: number;
  borderRadius?: number;
  style?: ViewStyle;
}

export function Skeleton({
  width = '100%',
  height = 16,
  borderRadius = 4,
  style,
}: SkeletonProps) {
  const reducedMotion = useReducedMotion();
  const opacity = useRef(new Animated.Value(1)).current;

  useEffect(() => {
    if (reducedMotion) return;

    const animation = Animated.loop(
      Animated.sequence([
        Animated.timing(opacity, {
          toValue: 0.5,
          duration: 750,
          useNativeDriver: true,
        }),
        Animated.timing(opacity, {
          toValue: 1,
          duration: 750,
          useNativeDriver: true,
        }),
      ])
    );

    animation.start();
    return () => animation.stop();
  }, [reducedMotion, opacity]);

  return (
    <Animated.View
      style={[
        styles.skeleton,
        { width, height, borderRadius, opacity: reducedMotion ? 1 : opacity },
        style,
      ]}
    />
  );
}

interface LoadingSkeletonProps {
  lines?: number;
  showAvatar?: boolean;
  style?: ViewStyle;
}

export function LoadingSkeleton({
  lines = 3,
  showAvatar = false,
  style,
}: LoadingSkeletonProps) {
  return (
    <View
      style={[styles.container, style]}
      accessible
      accessibilityRole="progressbar"
      accessibilityLabel="Loading content"
      accessibilityState={{ busy: true }}
    >
      {showAvatar && (
        <View style={styles.avatarRow}>
          <Skeleton width={40} height={40} borderRadius={20} />
          <View style={styles.avatarContent}>
            <Skeleton width="60%" height={14} />
            <Skeleton width="40%" height={12} />
          </View>
        </View>
      )}

      {Array.from({ length: lines }).map((_, i) => (
        <Skeleton
          key={i}
          width={i === lines - 1 ? '70%' : '100%'}
          height={14}
        />
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    gap: 12,
  },
  skeleton: {
    backgroundColor: '#E5E7EB', // gray-200
  },
  avatarRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  avatarContent: {
    flex: 1,
    gap: 6,
  },
});

export default LoadingSkeleton;
