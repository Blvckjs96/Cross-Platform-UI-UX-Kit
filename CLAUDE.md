# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Cross-Platform UX Kit is an AI-powered design intelligence toolkit providing searchable databases of UI styles, color palettes, font pairings, chart types, UX guidelines, shadcn/ui components, animations, and cross-platform patterns. It works as a skill/workflow for AI coding assistants (Claude Code, Windsurf, Cursor, etc.).

## Search Command

```bash
python3 .claude/skills/cross-platform-ux-kit/scripts/search.py "<query>" --domain <domain> [-n <max_results>]
```

**Domain search:**
- `product` - Product type recommendations (SaaS, e-commerce, portfolio)
- `style` - UI styles (glassmorphism, minimalism, brutalism)
- `typography` - Font pairings with Google Fonts imports
- `color` - Color palettes by product type
- `landing` - Page structure and CTA strategies
- `chart` - Chart types and library recommendations
- `ux` - Best practices and anti-patterns
- `prompt` - AI prompts and CSS keywords
- `icons` - Icon recommendations from Lucide library
- `component` - shadcn/ui components (70+ with variants, props, accessibility)
- `animation` - Animation patterns (Tailwind Animate + Framer Motion)
- `effect` - UI effects (hover, focus, loading, transitions)

**Stack search:**
```bash
python3 .claude/skills/cross-platform-ux-kit/scripts/search.py "<query>" --stack <stack>
```
Available stacks: `html-tailwind`, `react`, `nextjs`, `vue`, `nuxtjs`, `nuxt-ui`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`, `electron`

**Cross-platform pattern search:**
```bash
python3 .claude/skills/cross-platform-ux-kit/scripts/search.py "<query>" --pattern
```
Searches navigation, feedback, and data-display patterns with implementations for Web, Electron, SwiftUI, React Native, and Flutter.

**Platform-specific search:**
```bash
python3 .claude/skills/cross-platform-ux-kit/scripts/search.py "<query>" --platform <platform>
```
Available platforms: `web`, `electron`, `swiftui`, `react-native`, `flutter`

**Design token search:**
```bash
python3 .claude/skills/cross-platform-ux-kit/scripts/search.py "<query>" --token <token_type>
```
Available tokens: `spacing`, `typography`, `color`, `motion`

## Architecture

```
.claude/skills/cross-platform-ux-kit/    # Claude Code skill
├── SKILL.md                      # Skill definition with workflow instructions
├── scripts/
│   ├── search.py                 # CLI entry point
│   └── core.py                   # BM25 + regex hybrid search engine
└── data/
    ├── styles.csv, colors.csv, typography.csv, etc.  # Domain databases
    ├── stacks/                   # Stack-specific guidelines (12 CSV files)
    ├── components/               # shadcn/ui databases
    │   ├── shadcn-components.csv # 70+ components
    │   ├── shadcn-animations.csv # 45+ animations
    │   └── shadcn-effects.csv    # 60+ effects
    └── cross-platform/           # Cross-platform system
        ├── tokens/               # Design tokens (JSON)
        │   ├── spacing.json
        │   ├── typography.json
        │   ├── color.json
        │   └── motion.json
        ├── patterns/             # UX patterns with platform implementations
        │   ├── navigation.csv
        │   ├── feedback.csv
        │   └── data-display.csv
        └── platforms/            # Platform-specific guidelines
            ├── web.csv
            ├── electron.csv
            ├── swiftui.csv
            ├── react-native.csv
            └── flutter.csv

.windsurf/workflows/              # Windsurf workflow copy
.agent/workflows/                 # Generic agent workflow copy
.github/prompts/                  # GitHub Copilot prompt
.kiro/steering/                   # Kiro steering file
.shared/cross-platform-ux-kit/   # Shared data copy
```

The search engine uses BM25 ranking combined with regex matching. Domain auto-detection is available when `--domain` is omitted.

## Sync Rules

When modifying files, keep all agent workflows in sync:

- **Data & Scripts** (`data/`, `scripts/`): Copy changes to `.shared/cross-platform-ux-kit/` and `cli/assets/.shared/cross-platform-ux-kit/`
- **SKILL.md**: Update corresponding files in `.agent/`, `.cursor/`, `.windsurf/`, `.github/prompts/`, `.kiro/steering/`
- **CLI assets**: Copy all skill folders to `cli/assets/` (`.claude/`, `.cursor/`, `.windsurf/`, `.agent/`, `.github/`, `.kiro/`, `.shared/`)

## Prerequisites

Python 3.x (no external dependencies required)

## Git Workflow

Never push directly to `main`. Always:

1. Create a new branch: `git checkout -b feat/... ` or `fix/...`
2. Commit changes
3. Push branch: `git push -u origin <branch>`
4. Create PR: `gh pr create`
