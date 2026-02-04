/**
 * Loading Skeleton Component
 *
 * Inspired by Magic UI (MIT License)
 * Adapted for platform-native UX intent and accessibility requirements.
 *
 * @see patterns/feedback/loading.md for UX intent
 */

import { useEffect, useState } from 'react';
import { cn } from '@/lib/utils';

// Hook to detect reduced motion preference
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
  rounded?: 'sm' | 'md' | 'lg' | 'full';
}

export function Skeleton({
  className,
  width,
  height = 16,
  rounded = 'md'
}: SkeletonProps) {
  const reducedMotion = useReducedMotion();

  const roundedClass = {
    sm: 'rounded-sm',
    md: 'rounded-md',
    lg: 'rounded-lg',
    full: 'rounded-full',
  }[rounded];

  return (
    <div
      className={cn(
        'bg-muted',
        roundedClass,
        !reducedMotion && 'animate-shimmer',
        className
      )}
      style={{ width, height }}
      aria-hidden="true"
    />
  );
}

interface LoadingSkeletonProps {
  /** Number of skeleton lines to show */
  lines?: number;
  /** Show avatar placeholder */
  showAvatar?: boolean;
  /** Custom className */
  className?: string;
}

export function LoadingSkeleton({
  lines = 3,
  showAvatar = false,
  className
}: LoadingSkeletonProps) {
  const reducedMotion = useReducedMotion();

  return (
    <div
      className={cn('space-y-3', className)}
      role="status"
      aria-busy="true"
      aria-label="Loading content"
    >
      {showAvatar && (
        <div className="flex items-center gap-3">
          <Skeleton
            width={40}
            height={40}
            rounded="full"
            className={!reducedMotion ? 'animate-shimmer' : ''}
          />
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
          className={!reducedMotion ? 'animate-shimmer' : ''}
        />
      ))}

      <span className="sr-only">Loading...</span>
    </div>
  );
}

/**
 * Add this to your tailwind.config.js:
 *
 * theme: {
 *   extend: {
 *     animation: {
 *       shimmer: 'shimmer 1.5s ease-in-out infinite',
 *     },
 *     keyframes: {
 *       shimmer: {
 *         '0%': { opacity: '1' },
 *         '50%': { opacity: '0.5' },
 *         '100%': { opacity: '1' },
 *       },
 *     },
 *   },
 * },
 */
