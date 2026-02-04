/// Loading Skeleton Component - Flutter
///
/// Native implementation using Flutter's animation system.
/// Respects accessibility settings (reduce motion).
///
/// @see patterns/feedback/loading.md for UX intent

import 'package:flutter/material.dart';
import 'package:flutter/semantics.dart';

/// A skeleton loading placeholder
class Skeleton extends StatefulWidget {
  final double? width;
  final double height;
  final double borderRadius;

  const Skeleton({
    super.key,
    this.width,
    this.height = 16,
    this.borderRadius = 4,
  });

  @override
  State<Skeleton> createState() => _SkeletonState();
}

class _SkeletonState extends State<Skeleton>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 1500),
      vsync: this,
    );

    _animation = Tween<double>(begin: 1.0, end: 0.5).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeInOut),
    );

    _controller.repeat(reverse: true);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final reduceMotion = MediaQuery.of(context).disableAnimations;

    return AnimatedBuilder(
      animation: _animation,
      builder: (context, child) {
        return Container(
          width: widget.width,
          height: widget.height,
          decoration: BoxDecoration(
            color: Colors.grey[300]!.withOpacity(
              reduceMotion ? 1.0 : _animation.value,
            ),
            borderRadius: BorderRadius.circular(widget.borderRadius),
          ),
        );
      },
    );
  }
}

/// A loading skeleton with multiple lines
class LoadingSkeleton extends StatelessWidget {
  final int lines;
  final bool showAvatar;

  const LoadingSkeleton({
    super.key,
    this.lines = 3,
    this.showAvatar = false,
  });

  @override
  Widget build(BuildContext context) {
    return Semantics(
      label: 'Loading content',
      excludeSemantics: true,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (showAvatar) ...[
            Row(
              children: [
                const Skeleton(
                  width: 40,
                  height: 40,
                  borderRadius: 20,
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: const [
                      Skeleton(width: 120, height: 14),
                      SizedBox(height: 6),
                      Skeleton(width: 80, height: 12),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
          ],
          ...List.generate(
            lines,
            (index) => Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: Skeleton(
                width: index == lines - 1 ? 200 : double.infinity,
                height: 14,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

/// A loading card skeleton
class LoadingCard extends StatelessWidget {
  const LoadingCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: const [
            // Image placeholder
            Skeleton(height: 160, borderRadius: 8),
            SizedBox(height: 12),
            // Content
            LoadingSkeleton(lines: 2),
          ],
        ),
      ),
    );
  }
}
