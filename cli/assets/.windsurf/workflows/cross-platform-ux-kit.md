---
description: Plan and implement UI
auto_execution_mode: 3
---

# UI/UX Pro Max - Design Intelligence

Searchable database of UI styles, color palettes, font pairings, chart types, product recommendations, UX guidelines, shadcn/ui components, animations, effects, cross-platform patterns, design tokens, and stack-specific best practices.

## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If Python is not installed, install it based on user's OS:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

---

## How to Use This Workflow

When user requests UI/UX work (design, build, create, implement, review, fix, improve), follow this workflow:

### Step 1: Analyze User Requirements

Extract key information from user request:
- **Product type**: SaaS, e-commerce, portfolio, dashboard, landing page, etc.
- **Style keywords**: minimal, playful, professional, elegant, dark mode, etc.
- **Industry**: healthcare, fintech, gaming, education, etc.
- **Stack**: React, Vue, Next.js, SwiftUI, Flutter, Electron, or default to `html-tailwind`
- **Platform**: Web, Electron, SwiftUI, React Native, Flutter (for cross-platform apps)

### Step 2: Search Relevant Domains

Use `search.py` multiple times to gather comprehensive information. Search until you have enough context.

```bash
python3 .shared/cross-platform-ux-kit/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Recommended search order:**

1. **Product** - Get style recommendations for product type
2. **Style** - Get detailed style guide (colors, effects, frameworks)
3. **Typography** - Get font pairings with Google Fonts imports
4. **Color** - Get color palette (Primary, Secondary, CTA, Background, Text, Border)
5. **Component** - Get shadcn/ui component specs (if using shadcn)
6. **Animation** - Get animation patterns (Tailwind Animate + Framer Motion)
7. **Effect** - Get UI effects (hover, focus, loading states)
8. **Landing** - Get page structure (if landing page)
9. **Chart** - Get chart recommendations (if dashboard/analytics)
10. **UX** - Get best practices and anti-patterns
11. **Stack** - Get stack-specific guidelines (default: html-tailwind)

### Step 3: Stack Guidelines (Default: html-tailwind)

If user doesn't specify a stack, **default to `html-tailwind`**.

```bash
python3 .shared/cross-platform-ux-kit/scripts/search.py "<keyword>" --stack html-tailwind
```

Available stacks: `html-tailwind`, `react`, `nextjs`, `vue`, `nuxtjs`, `nuxt-ui`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`, `electron`

### Step 4: Cross-Platform Patterns (Optional)

For apps targeting multiple platforms, search cross-platform UX patterns:

```bash
# Search patterns with implementations for all 5 platforms (Web, Electron, SwiftUI, React Native, Flutter)
python3 .shared/cross-platform-ux-kit/scripts/search.py "command palette" --pattern

# Search platform-specific guidelines
python3 .shared/cross-platform-ux-kit/scripts/search.py "navigation" --platform swiftui
python3 .shared/cross-platform-ux-kit/scripts/search.py "window" --platform electron
```

Available platforms: `web`, `electron`, `swiftui`, `react-native`, `flutter`

### Step 5: Design Tokens (Optional)

For precise design values, search design tokens:

```bash
python3 .shared/cross-platform-ux-kit/scripts/search.py "fast" --token motion
python3 .shared/cross-platform-ux-kit/scripts/search.py "lg" --token spacing
python3 .shared/cross-platform-ux-kit/scripts/search.py "primary" --token color
```

Available tokens: `spacing`, `typography`, `color`, `motion`

---

## Search Reference

### Available Domains

| Domain | Use For | Example Keywords |
|--------|---------|------------------|
| `product` | Product type recommendations | SaaS, e-commerce, portfolio, healthcare, beauty, service |
| `style` | UI styles, colors, effects | glassmorphism, minimalism, dark mode, brutalism |
| `typography` | Font pairings, Google Fonts | elegant, playful, professional, modern |
| `color` | Color palettes by product type | saas, ecommerce, healthcare, beauty, fintech, service |
| `landing` | Page structure, CTA strategies | hero, hero-centric, testimonial, pricing, social-proof |
| `chart` | Chart types, library recommendations | trend, comparison, timeline, funnel, pie |
| `ux` | Best practices, anti-patterns | animation, accessibility, z-index, loading |
| `prompt` | AI prompts, CSS keywords | (style name) |
| `icons` | Icon recommendations | lucide, heroicons, navigation, action, status |
| `component` | shadcn/ui components (70+) | button, dialog, form, table, accordion, sheet |
| `animation` | Animation patterns (45+) | fade, slide, zoom, spin, pulse, bounce, spring |
| `effect` | UI effects (60+) | hover, focus, loading, skeleton, ripple, glow |

### Available Stacks

| Stack | Focus |
|-------|-------|
| `html-tailwind` | Tailwind utilities, responsive, a11y (DEFAULT) |
| `react` | State, hooks, performance, patterns |
| `nextjs` | SSR, routing, images, API routes |
| `vue` | Composition API, Pinia, Vue Router |
| `nuxtjs` | Nuxt 3, Composition API, modules |
| `nuxt-ui` | Nuxt UI components, theming |
| `svelte` | Runes, stores, SvelteKit |
| `swiftui` | Views, State, Navigation, Animation |
| `react-native` | Components, Navigation, Lists |
| `flutter` | Widgets, State, Layout, Theming |
| `shadcn` | shadcn/ui components, theming, forms, patterns |
| `electron` | Window, IPC, Security, Menu, Tray, Updates |

### Cross-Platform Search

| Command | Description |
|---------|-------------|
| `--pattern` | Search UX patterns with Web/Electron/SwiftUI/React Native/Flutter implementations |
| `--platform <name>` | Search platform-specific guidelines (web, electron, swiftui, react-native, flutter) |
| `--token <type>` | Search design tokens (spacing, typography, color, motion) |

---

## Example Workflow

**User request:** "Làm landing page cho dịch vụ chăm sóc da chuyên nghiệp"

**AI should:**

```bash
# 1. Search product type
python3 .shared/cross-platform-ux-kit/scripts/search.py "beauty spa wellness service" --domain product

# 2. Search style (based on industry: beauty, elegant)
python3 .shared/cross-platform-ux-kit/scripts/search.py "elegant minimal soft" --domain style

# 3. Search typography
python3 .shared/cross-platform-ux-kit/scripts/search.py "elegant luxury" --domain typography

# 4. Search color palette
python3 .shared/cross-platform-ux-kit/scripts/search.py "beauty spa wellness" --domain color

# 5. Search landing page structure
python3 .shared/cross-platform-ux-kit/scripts/search.py "hero-centric social-proof" --domain landing

# 6. Search UX guidelines
python3 .shared/cross-platform-ux-kit/scripts/search.py "animation" --domain ux
python3 .shared/cross-platform-ux-kit/scripts/search.py "accessibility" --domain ux

# 7. Search stack guidelines (default: html-tailwind)
python3 .shared/cross-platform-ux-kit/scripts/search.py "layout responsive" --stack html-tailwind
```

**Then:** Synthesize all search results and implement the design.

---

## Example: Cross-Platform Electron App

**User request:** "Build a command palette for an Electron app"

**AI should:**

```bash
# 1. Search component specs
python3 .shared/cross-platform-ux-kit/scripts/search.py "command dialog" --domain component

# 2. Search cross-platform pattern (get implementations for all platforms)
python3 .shared/cross-platform-ux-kit/scripts/search.py "command palette" --pattern

# 3. Search animation patterns
python3 .shared/cross-platform-ux-kit/scripts/search.py "fade zoom" --domain animation

# 4. Search Electron-specific guidelines
python3 .shared/cross-platform-ux-kit/scripts/search.py "window keyboard shortcut" --stack electron

# 5. Search motion tokens for timing
python3 .shared/cross-platform-ux-kit/scripts/search.py "normal ease" --token motion
```

---

## Tips for Better Results

1. **Be specific with keywords** - "healthcare SaaS dashboard" > "app"
2. **Search multiple times** - Different keywords reveal different insights
3. **Combine domains** - Style + Typography + Color = Complete design system
4. **Always check UX** - Search "animation", "z-index", "accessibility" for common issues
5. **Use stack flag** - Get implementation-specific best practices
6. **Iterate** - If first search doesn't match, try different keywords
7. **Use component search** - Get shadcn/ui specs with variants, props, accessibility
8. **Use pattern search** - Get cross-platform implementations for common UX patterns
9. **Use token search** - Get precise values for spacing, colors, motion
10. **Split Into Multiple Files** - For better maintainability:
    - Separate components into individual files (e.g., `Header.tsx`, `Footer.tsx`)
    - Extract reusable styles into dedicated files
    - Keep each file focused and under 200-300 lines

---

## Common Rules for Professional UI

These are frequently overlooked issues that make UI look unprofessional:

### Icons & Visual Elements

| Rule | Do | Don't |
|------|----|------ |
| **No emoji icons** | Use SVG icons (Heroicons, Lucide, Simple Icons) | Use emojis like 🎨 🚀 ⚙️ as UI icons |
| **Stable hover states** | Use color/opacity transitions on hover | Use scale transforms that shift layout |
| **Correct brand logos** | Research official SVG from Simple Icons | Guess or use incorrect logo paths |
| **Consistent icon sizing** | Use fixed viewBox (24x24) with w-6 h-6 | Mix different icon sizes randomly |

### Interaction & Cursor

| Rule | Do | Don't |
|------|----|------ |
| **Cursor pointer** | Add `cursor-pointer` to all clickable/hoverable cards | Leave default cursor on interactive elements |
| **Hover feedback** | Provide visual feedback (color, shadow, border) | No indication element is interactive |
| **Smooth transitions** | Use `transition-colors duration-200` | Instant state changes or too slow (>500ms) |

### Light/Dark Mode Contrast

| Rule | Do | Don't |
|------|----|------ |
| **Glass card light mode** | Use `bg-white/80` or higher opacity | Use `bg-white/10` (too transparent) |
| **Text contrast light** | Use `#0F172A` (slate-900) for text | Use `#94A3B8` (slate-400) for body text |
| **Muted text light** | Use `#475569` (slate-600) minimum | Use gray-400 or lighter |
| **Border visibility** | Use `border-gray-200` in light mode | Use `border-white/10` (invisible) |

### Layout & Spacing

| Rule | Do | Don't |
|------|----|------ |
| **Floating navbar** | Add `top-4 left-4 right-4` spacing | Stick navbar to `top-0 left-0 right-0` |
| **Content padding** | Account for fixed navbar height | Let content hide behind fixed elements |
| **Consistent max-width** | Use same `max-w-6xl` or `max-w-7xl` | Mix different container widths |

---

## Pre-Delivery Checklist

Before delivering UI code, verify these items:

### Visual Quality
- [ ] No emojis used as icons (use SVG instead)
- [ ] All icons from consistent icon set (Heroicons/Lucide)
- [ ] Brand logos are correct (verified from Simple Icons)
- [ ] Hover states don't cause layout shift
- [ ] Use theme colors directly (bg-primary) not var() wrapper

### Interaction
- [ ] All clickable elements have `cursor-pointer`
- [ ] Hover states provide clear visual feedback
- [ ] Transitions are smooth (150-300ms)
- [ ] Focus states visible for keyboard navigation

### Light/Dark Mode
- [ ] Light mode text has sufficient contrast (4.5:1 minimum)
- [ ] Glass/transparent elements visible in light mode
- [ ] Borders visible in both modes
- [ ] Test both modes before delivery

### Layout
- [ ] Floating elements have proper spacing from edges
- [ ] No content hidden behind fixed navbars
- [ ] Responsive at 320px, 768px, 1024px, 1440px
- [ ] No horizontal scroll on mobile

### Accessibility
- [ ] All images have alt text
- [ ] Form inputs have labels
- [ ] Color is not the only indicator
- [ ] `prefers-reduced-motion` respected
