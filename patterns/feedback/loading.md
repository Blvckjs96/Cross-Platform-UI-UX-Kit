# Loading Feedback Pattern

## UX Intent

Reduce user anxiety during wait times while maintaining the perception that the system is actively working.

## Behavior Rules

| Wait Duration | Feedback Type | Description |
|---------------|---------------|-------------|
| < 400ms | None | No visual feedback needed |
| 400ms – 2s | Skeleton | Show placeholder shapes matching content layout |
| > 2s | Skeleton + Status | Add text indicating progress/state |

## Platform-Agnostic Requirements

1. **Progressive disclosure** - Start with skeleton, escalate to status text if needed
2. **Content-aware shapes** - Skeleton should roughly match the expected content layout
3. **No jarring transitions** - Smooth fade between loading and loaded states

## Accessibility

- Respect `prefers-reduced-motion` - disable shimmer/animation effects
- Use `aria-busy="true"` on loading containers (Web)
- Avoid flashing or rapid animations that may trigger seizures
- Provide text alternatives for screen readers

## Anti-Patterns

❌ Spinner immediately on action
❌ Full-screen blocking loaders for partial content
❌ Shimmer animation that never stops
❌ Loading text without visual indication

## Platform Implementations

| Platform | Implementation | Notes |
|----------|----------------|-------|
| Web | `platforms/web/implementations/magic-ui/loading.tsx` | Shimmer skeleton, CSS animation |
| Electron | `platforms/electron/implementations/loading.tsx` | Reduced animation, keyboard-first |
| SwiftUI | `platforms/swiftui/examples/LoadingView.swift` | Native `.redacted()` placeholder |
| React Native | `platforms/react-native/implementations/Loading.tsx` | Native skeleton library |
| Flutter | `platforms/flutter/implementations/loading.dart` | Shimmer package or custom |

## Design Tokens

```json
{
  "skeleton": {
    "background": "var(--color-muted)",
    "shimmer": "var(--color-muted-foreground)",
    "borderRadius": "var(--radius-sm)",
    "animation": {
      "duration": "1.5s",
      "timing": "ease-in-out"
    }
  }
}
```

## References

- [Nielsen Norman Group: Response Times](https://www.nngroup.com/articles/response-times-3-important-limits/)
- [Material Design: Progress Indicators](https://m3.material.io/components/progress-indicators)
- [Apple HIG: Loading](https://developer.apple.com/design/human-interface-guidelines/loading)
