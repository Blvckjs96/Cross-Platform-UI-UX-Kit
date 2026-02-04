Cross-platform UX/UI Pro Max

One UX intent. Multiple native implementations.

Tài liệu này mô tả toàn bộ tư duy, kiến trúc repo, và chiến lược xây dựng một design system / UX skillset dùng chung cho đa nền tảng (Web, Electron, SwiftUI), tập trung vào AI-first & desktop-first UX.

1. Mục tiêu

Xây dựng 1 repo duy nhất dùng cho nhiều nền tảng

Giữ UX intent nhất quán, nhưng UI implementation native theo từng platform

Dùng được cho:

AI tools

Developer tools

Desktop apps (Electron / macOS)

Web apps

Không cố gắng "write once, run everywhere" cho UI — mà là:

Design once, implement natively everywhere

2. Triết lý cốt lõi
Platform-aware, không phải platform-agnostic

UX principle: dùng chung

UX pattern: dùng chung về ý nghĩa (intent)

UI layout & interaction: khác nhau theo platform

Ví dụ:

Command Palette

Web: modal overlay

Electron: floating spotlight window

SwiftUI: sheet + focus binding

3. Cấu trúc repo đề xuất
ux-ui-pro-max/
├─ README.md
│
├─ core/
│  ├─ philosophy.md            # Triết lý UX tổng thể
│  ├─ ux-principles.md         # Hierarchy, spacing, clarity
│  ├─ accessibility.md         # A11y, focus, keyboard
│  ├─ interaction-model.md     # Mouse, keyboard, touch, trackpad
│  ├─ design-tokens.md         # Quy ước token
│
├─ tokens/
│  ├─ spacing.json
│  ├─ typography.json
│  ├─ color.json
│  └─ motion.json
│
├─ patterns/
│  ├─ navigation/
│  │  ├─ sidebar.md
│  │  ├─ tabbar.md
│  │  └─ command-palette.md
│  ├─ feedback/
│  │  ├─ loading.md
│  │  ├─ error.md
│  │  └─ empty-state.md
│  ├─ data/
│  │  ├─ table.md
│  │  ├─ inspector.md
│  │  └─ filters.md
│
├─ platforms/
│  ├─ web/
│  │  ├─ guidelines.md
│  │  ├─ do-dont.md
│  │  └─ examples/
│  ├─ electron/
│  │  ├─ windowing.md
│  │  ├─ keyboard-shortcuts.md
│  │  ├─ titlebar.md
│  │  └─ examples/
│  ├─ swiftui/
│  │  ├─ apple-hig.md
│  │  ├─ navigation.md
│  │  ├─ focus.md
│  │  └─ examples/
│
├─ prompts/
│  ├─ generate-ui.prompt.md
│  ├─ adapt-ui-to-platform.prompt.md
│  ├─ review-ux.prompt.md
│  └─ refactor-cross-platform.prompt.md
4. Design Tokens – xương sống của hệ thống

Design token giúp:

Giữ consistency UX

Cho phép UI khác nhau theo platform

Ví dụ: spacing.json
{
  "xs": 4,
  "sm": 8,
  "md": 12,
  "lg": 16,
  "xl": 24
}
Mapping theo platform
Token	Web (px)	Electron (px)	SwiftUI
xs	4	4	4
md	12	12	12
xl	24	24	24

SwiftUI sử dụng thông qua extension hoặc modifier chuẩn hoá.

5. UX Pattern = Intent, không phải layout
Ví dụ: Command Palette

Intent:

Trigger action nhanh

Keyboard-first

Fuzzy search

Behavior:

Mở bằng ⌘K / Ctrl+K

Không phụ thuộc vào navigation

Triển khai theo platform:

Web: Modal overlay

Electron: Spotlight-style window

SwiftUI: .sheet + focus state

Pattern chỉ định mục tiêu UX, không ép layout.

6. Platform-specific guidelines
Web

Responsive

Scroll-based navigation

Browser constraints

Electron

Fixed / resizable window

Keyboard shortcut là first-class

Context menu, multi-window

SwiftUI

Tuân thủ Apple Human Interface Guidelines

Focus & accessibility native

System spacing & animation

7. Prompt system (AI-first)

Repo này được thiết kế để AI có thể đọc và sinh UI đúng platform.

Prompt sinh UI
You are a senior UX engineer.


Input:
- Feature description
- Target platform: Web | Electron | SwiftUI
- Design tokens
- UX patterns


Task:
- Generate platform-native UI
- Respect platform conventions
- Keep UX intent identical
Prompt review
Review this UI implementation.
Compare it with UX intent in /patterns.
Flag any platform violations or UX regressions.
8. Anti-pattern cần tránh

❌ Copy UI web sang desktop

❌ Dùng chung component React cho SwiftUI

❌ Bỏ qua keyboard & focus

❌ Token có nhưng không enforce

9. Lộ trình phát triển repo
Phase 1 – Core

core/

tokens/

5–7 UX patterns chính

Phase 2 – Platform depth

Electron UX chuyên sâu

SwiftUI navigation & focus

Phase 3 – AI-first

Prompt generate

Prompt review

Prompt refactor cross-platform

10. Định vị open-source

Repo hướng tới:

Developer

AI app builder

Desktop app maker

Thông điệp chính:

One UX intent. Multiple native implementations.

Document này là nền tảng để tiếp tục mở rộng README, patterns chi tiết, và prompt system.