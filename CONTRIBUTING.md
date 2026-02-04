# Contributing to Cross-Platform UX Kit

This document defines the legal and technical rules for contributing to this cross-platform UX repository.

## Core Philosophy

> **One UX intent → Multiple native implementations**

- UX intent and patterns are defined by this repository
- External libraries (Magic UI, etc.) are only used at the implementation layer
- Each platform gets a native implementation that feels right for that platform

## Legal Rules

### Allowed

- Reference common UX patterns in the industry
- Copy small, selective code snippets from MIT-licensed libraries
- Adapt/rewrite code to fit UX intent
- Rename components, props, and comments
- Add clear attribution

### Forbidden

- ❌ Fork another UI/UX repository
- ❌ Copy README, docs, or marketing text
- ❌ Keep signature component names unchanged
- ❌ Copy entire folders/structure from another repo
- ❌ Put external libraries in `core/` or `patterns/`

**Violations will result in immediate PR rejection.**

## Attribution Standard

When referencing external code, add this attribution:

```javascript
/**
 * Inspired by Magic UI (MIT License)
 * Adapted to fit this repository's UX intent and platform rules.
 */
```

Do NOT write: "based on", "forked from", or "derived from".

## Technical Rules

### Workflow Order (Required)

1. Define UX Pattern in `patterns/`
2. Review intent & behavior
3. Write platform implementation in `platforms/`

❌ Never work in reverse order.

### Directory Structure

```
patterns/
  category/pattern-name.md      # UX intent (no code)

platforms/
  web/
    implementations/
      magic-ui/                  # Adapted from Magic UI
      custom/                    # Custom implementations
  electron/
    implementations/
  swiftui/
    examples/
  react-native/
    implementations/
  flutter/
    implementations/
```

- `patterns/` contains UX intent only (no UI code)
- UI code lives exclusively in `platforms/`

### Platform-Specific Rules

| Platform | Guidelines |
|----------|------------|
| **Web** | May use Magic UI (adapted), must support `prefers-reduced-motion` |
| **Electron** | Minimize heavy animations, prioritize keyboard-first UX |
| **SwiftUI** | No web animation styles, follow Apple HIG, use system spacing & animation |
| **React Native** | Use native components, respect accessibility settings |
| **Flutter** | Use Material/Cupertino patterns, respect `disableAnimations` |

## Pull Request Checklist

Before submitting a PR:

- [ ] UX pattern defined in `patterns/` first
- [ ] No copied README/docs/marketing text
- [ ] Attribution added for any referenced code
- [ ] Component names are original
- [ ] Platform implementation follows platform guidelines
- [ ] Accessibility requirements met (reduced motion, ARIA, etc.)
- [ ] No external libraries in `core/` or `patterns/`

## Message to Contributors

> You're not contributing UI. You're contributing UX logic that can live across multiple platforms.

This document is the official standard for all current and future contributions.
