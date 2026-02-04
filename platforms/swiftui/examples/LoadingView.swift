/**
 * Loading View - SwiftUI Native Implementation
 *
 * Native implementation following Apple Human Interface Guidelines.
 * Does NOT use web-style shimmer animations.
 *
 * @see patterns/feedback/loading.md for UX intent
 */

import SwiftUI

/// A native loading skeleton view using SwiftUI's redacted modifier
struct LoadingView: View {
    var lines: Int = 3
    var showAvatar: Bool = false

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            if showAvatar {
                HStack(spacing: 12) {
                    Circle()
                        .fill(Color.gray.opacity(0.3))
                        .frame(width: 40, height: 40)

                    VStack(alignment: .leading, spacing: 6) {
                        RoundedRectangle(cornerRadius: 4)
                            .fill(Color.gray.opacity(0.3))
                            .frame(width: 120, height: 14)

                        RoundedRectangle(cornerRadius: 4)
                            .fill(Color.gray.opacity(0.3))
                            .frame(width: 80, height: 12)
                    }
                }
            }

            ForEach(0..<lines, id: \.self) { index in
                RoundedRectangle(cornerRadius: 4)
                    .fill(Color.gray.opacity(0.3))
                    .frame(height: 14)
                    .frame(maxWidth: index == lines - 1 ? 200 : .infinity)
            }
        }
        .redacted(reason: .placeholder)
        .accessibilityLabel("Loading content")
        .accessibilityHint("Please wait while content loads")
    }
}

/// A loading view with automatic timeout for status text
struct LoadingWithStatus: View {
    @State private var showStatus = false
    @State private var elapsedTime: TimeInterval = 0

    let statusThreshold: TimeInterval = 2.0
    let statusText: String

    init(statusText: String = "Loading, please wait...") {
        self.statusText = statusText
    }

    var body: some View {
        VStack(spacing: 16) {
            LoadingView()

            if showStatus {
                Text(statusText)
                    .font(.caption)
                    .foregroundColor(.secondary)
                    .transition(.opacity.combined(with: .move(edge: .top)))
            }
        }
        .animation(.easeInOut(duration: 0.3), value: showStatus)
        .onAppear {
            Timer.scheduledTimer(withTimeInterval: statusThreshold, repeats: false) { _ in
                withAnimation {
                    showStatus = true
                }
            }
        }
    }
}

/// Card-style loading skeleton
struct LoadingCard: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Image placeholder
            RoundedRectangle(cornerRadius: 8)
                .fill(Color.gray.opacity(0.3))
                .frame(height: 160)

            // Content
            LoadingView(lines: 2)
        }
        .padding()
        .background(Color(.systemBackground))
        .cornerRadius(12)
        .shadow(color: .black.opacity(0.1), radius: 4, x: 0, y: 2)
    }
}

// MARK: - Preview

#Preview {
    VStack(spacing: 24) {
        LoadingView()

        Divider()

        LoadingView(lines: 2, showAvatar: true)

        Divider()

        LoadingCard()
    }
    .padding()
}
