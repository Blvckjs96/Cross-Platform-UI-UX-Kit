/**
 * Loading Skeleton Component - Electron Optimized
 *
 * Adapted for desktop environment with reduced animation
 * to minimize CPU/battery usage.
 *
 * @see patterns/feedback/loading.md for UX intent
 */

import { useEffect, useState } from 'react';
import { cn } from '@/lib/utils';

// Detect if window is in background (Electron specific)
function useWindowFocus(): boolean {
  const [focused, setFocused] = useState(true);

  useEffect(() => {
    const handleFocus = () => setFocused(true);
    const handleBlur = () => setFocused(false);

    window.addEventListener('focus', handleFocus);
    window.addEventListener('blur', handleBlur);

    return () => {
      window.removeEventListener('focus', handleFocus);
      window.removeEventListener('blur', handleBlur);
    };
  }, []);

  return focused;
}

function useReducedMotion(): boolean {
  const [reduced, setReduced] = useState(false);

  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setReduced(mediaQuery.matches);

    const handler = (e: MediaQueryListEvent) => setReduced(e.matches);
    mediaQuery.addEventListener('change', handler);
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);

  return reduced;
}

interface SkeletonProps {
  className?: string;
  width?: string | number;
  height?: string | number;
}

export function Skeleton({ className, width, height = 16 }: SkeletonProps) {
  const reducedMotion = useReducedMotion();
  const windowFocused = useWindowFocus();

  // Disable animation when window is not focused (saves CPU)
  const shouldAnimate = !reducedMotion && windowFocused;

  return (
    <div
      className={cn(
        'bg-muted rounded-md',
        shouldAnimate && 'animate-pulse-subtle',
        className
      )}
      style={{ width, height }}
      aria-hidden="true"
    />
  );
}

interface LoadingSkeletonProps {
  lines?: number;
  showAvatar?: boolean;
  className?: string;
}

export function LoadingSkeleton({
  lines = 3,
  showAvatar = false,
  className
}: LoadingSkeletonProps) {
  return (
    <div
      className={cn('space-y-3', className)}
      role="status"
      aria-busy="true"
      aria-label="Loading content"
    >
      {showAvatar && (
        <div className="flex items-center gap-3">
          <Skeleton width={40} height={40} className="rounded-full" />
          <div className="space-y-2 flex-1">
            <Skeleton height={14} width="60%" />
            <Skeleton height={12} width="40%" />
          </div>
        </div>
      )}

      {Array.from({ length: lines }).map((_, i) => (
        <Skeleton
          key={i}
          height={14}
          width={i === lines - 1 ? '70%' : '100%'}
        />
      ))}

      <span className="sr-only">Loading...</span>
    </div>
  );
}

/**
 * Electron-optimized Tailwind config:
 *
 * theme: {
 *   extend: {
 *     animation: {
 *       // Subtle animation - lower CPU usage than full shimmer
 *       'pulse-subtle': 'pulse-subtle 2s ease-in-out infinite',
 *     },
 *     keyframes: {
 *       'pulse-subtle': {
 *         '0%, 100%': { opacity: '1' },
 *         '50%': { opacity: '0.7' },
 *       },
 *     },
 *   },
 * },
 */
