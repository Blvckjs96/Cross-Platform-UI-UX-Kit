#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI/UX Pro Max Core - BM25 search engine for UI/UX style guides
"""

import csv
import re
import json
from pathlib import Path
from math import log
from collections import defaultdict

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent / "data"
MAX_RESULTS = 3

CSV_CONFIG = {
    "style": {
        "file": "styles.csv",
        "search_cols": ["Style Category", "Keywords", "Best For", "Type"],
        "output_cols": ["Style Category", "Type", "Keywords", "Primary Colors", "Effects & Animation", "Best For", "Performance", "Accessibility", "Framework Compatibility", "Complexity"]
    },
    "prompt": {
        "file": "prompts.csv",
        "search_cols": ["Style Category", "AI Prompt Keywords (Copy-Paste Ready)", "CSS/Technical Keywords"],
        "output_cols": ["Style Category", "AI Prompt Keywords (Copy-Paste Ready)", "CSS/Technical Keywords", "Implementation Checklist"]
    },
    "color": {
        "file": "colors.csv",
        "search_cols": ["Product Type", "Keywords", "Notes"],
        "output_cols": ["Product Type", "Keywords", "Primary (Hex)", "Secondary (Hex)", "CTA (Hex)", "Background (Hex)", "Text (Hex)", "Border (Hex)", "Notes"]
    },
    "chart": {
        "file": "charts.csv",
        "search_cols": ["Data Type", "Keywords", "Best Chart Type", "Accessibility Notes"],
        "output_cols": ["Data Type", "Keywords", "Best Chart Type", "Secondary Options", "Color Guidance", "Accessibility Notes", "Library Recommendation", "Interactive Level"]
    },
    "landing": {
        "file": "landing.csv",
        "search_cols": ["Pattern Name", "Keywords", "Conversion Optimization", "Section Order"],
        "output_cols": ["Pattern Name", "Keywords", "Section Order", "Primary CTA Placement", "Color Strategy", "Conversion Optimization"]
    },
    "product": {
        "file": "products.csv",
        "search_cols": ["Product Type", "Keywords", "Primary Style Recommendation", "Key Considerations"],
        "output_cols": ["Product Type", "Keywords", "Primary Style Recommendation", "Secondary Styles", "Landing Page Pattern", "Dashboard Style (if applicable)", "Color Palette Focus"]
    },
    "ux": {
        "file": "ux-guidelines.csv",
        "search_cols": ["Category", "Issue", "Description", "Platform"],
        "output_cols": ["Category", "Issue", "Platform", "Description", "Do", "Don't", "Code Example Good", "Code Example Bad", "Severity"]
    },
    "typography": {
        "file": "typography.csv",
        "search_cols": ["Font Pairing Name", "Category", "Mood/Style Keywords", "Best For", "Heading Font", "Body Font"],
        "output_cols": ["Font Pairing Name", "Category", "Heading Font", "Body Font", "Mood/Style Keywords", "Best For", "Google Fonts URL", "CSS Import", "Tailwind Config", "Notes"]
    },
    "icons": {
        "file": "icons.csv",
        "search_cols": ["Category", "Icon Name", "Keywords", "Best For"],
        "output_cols": ["Category", "Icon Name", "Keywords", "Library", "Import Code", "Usage", "Best For", "Style"]
    },
    "component": {
        "file": "components/shadcn-components.csv",
        "search_cols": ["Component", "Category", "Variants", "Key Props", "Accessibility"],
        "output_cols": ["Component", "Category", "Variants", "Key Props", "Accessibility", "Animation", "Composition", "Common Mistakes", "Code Example", "Docs URL"]
    },
    "animation": {
        "file": "components/shadcn-animations.csv",
        "search_cols": ["Animation", "Type", "Use Cases", "Tailwind Class"],
        "output_cols": ["Animation", "Type", "Tailwind Class", "Framer Motion", "Duration", "Easing", "Use Cases", "Performance", "Reduced Motion"]
    },
    "effect": {
        "file": "components/shadcn-effects.csv",
        "search_cols": ["Effect", "Category", "Trigger", "Implementation"],
        "output_cols": ["Effect", "Category", "Implementation", "Trigger", "Duration", "Props", "Example", "Notes"]
    },
    "pattern": {
        "file": "cross-platform/patterns/navigation.csv",
        "search_cols": ["Pattern", "Intent", "Trigger"],
        "output_cols": ["Pattern", "Intent", "Trigger", "Web", "Electron", "SwiftUI", "React Native", "Flutter", "Accessibility"]
    },
    "platform": {
        "file": "cross-platform/platforms/web.csv",
        "search_cols": ["Category", "Guideline", "Description"],
        "output_cols": ["Category", "Guideline", "Description", "Do", "Don't", "Platform Notes"]
    }
}

STACK_CONFIG = {
    "html-tailwind": {"file": "stacks/html-tailwind.csv"},
    "react": {"file": "stacks/react.csv"},
    "nextjs": {"file": "stacks/nextjs.csv"},
    "vue": {"file": "stacks/vue.csv"},
    "nuxtjs": {"file": "stacks/nuxtjs.csv"},
    "nuxt-ui": {"file": "stacks/nuxt-ui.csv"},
    "svelte": {"file": "stacks/svelte.csv"},
    "swiftui": {"file": "stacks/swiftui.csv"},
    "react-native": {"file": "stacks/react-native.csv"},
    "flutter": {"file": "stacks/flutter.csv"},
    "shadcn": {"file": "stacks/shadcn.csv"},
    "electron": {"file": "stacks/electron.csv"}
}

# Pattern files for multi-file pattern search
PATTERN_FILES = {
    "navigation": "cross-platform/patterns/navigation.csv",
    "feedback": "cross-platform/patterns/feedback.csv",
    "data-display": "cross-platform/patterns/data-display.csv"
}

# Platform files for platform-specific guidelines
PLATFORM_FILES = {
    "web": "cross-platform/platforms/web.csv",
    "electron": "cross-platform/platforms/electron.csv",
    "swiftui": "cross-platform/platforms/swiftui.csv",
    "react-native": "cross-platform/platforms/react-native.csv",
    "flutter": "cross-platform/platforms/flutter.csv"
}

# Token files for design tokens
TOKEN_FILES = {
    "spacing": "cross-platform/tokens/spacing.json",
    "typography": "cross-platform/tokens/typography.json",
    "color": "cross-platform/tokens/color.json",
    "motion": "cross-platform/tokens/motion.json"
}

# Common columns for all stacks
_STACK_COLS = {
    "search_cols": ["Category", "Guideline", "Description", "Do", "Don't"],
    "output_cols": ["Category", "Guideline", "Description", "Do", "Don't", "Code Good", "Code Bad", "Severity", "Docs URL"]
}

AVAILABLE_STACKS = list(STACK_CONFIG.keys())


# ============ BM25 IMPLEMENTATION ============
class BM25:
    """BM25 ranking algorithm for text search"""

    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.corpus = []
        self.doc_lengths = []
        self.avgdl = 0
        self.idf = {}
        self.doc_freqs = defaultdict(int)
        self.N = 0

    def tokenize(self, text):
        """Lowercase, split, remove punctuation, filter short words"""
        text = re.sub(r'[^\w\s]', ' ', str(text).lower())
        return [w for w in text.split() if len(w) > 2]

    def fit(self, documents):
        """Build BM25 index from documents"""
        self.corpus = [self.tokenize(doc) for doc in documents]
        self.N = len(self.corpus)
        if self.N == 0:
            return
        self.doc_lengths = [len(doc) for doc in self.corpus]
        self.avgdl = sum(self.doc_lengths) / self.N

        for doc in self.corpus:
            seen = set()
            for word in doc:
                if word not in seen:
                    self.doc_freqs[word] += 1
                    seen.add(word)

        for word, freq in self.doc_freqs.items():
            self.idf[word] = log((self.N - freq + 0.5) / (freq + 0.5) + 1)

    def score(self, query):
        """Score all documents against query"""
        query_tokens = self.tokenize(query)
        scores = []

        for idx, doc in enumerate(self.corpus):
            score = 0
            doc_len = self.doc_lengths[idx]
            term_freqs = defaultdict(int)
            for word in doc:
                term_freqs[word] += 1

            for token in query_tokens:
                if token in self.idf:
                    tf = term_freqs[token]
                    idf = self.idf[token]
                    numerator = tf * (self.k1 + 1)
                    denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                    score += idf * numerator / denominator

            scores.append((idx, score))

        return sorted(scores, key=lambda x: x[1], reverse=True)


# ============ SEARCH FUNCTIONS ============
def _load_csv(filepath):
    """Load CSV and return list of dicts"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Core search function using BM25"""
    if not filepath.exists():
        return []

    data = _load_csv(filepath)

    # Build documents from search columns
    documents = [" ".join(str(row.get(col, "")) for col in search_cols) for row in data]

    # BM25 search
    bm25 = BM25()
    bm25.fit(documents)
    ranked = bm25.score(query)

    # Get top results with score > 0
    results = []
    for idx, score in ranked[:max_results]:
        if score > 0:
            row = data[idx]
            results.append({col: row.get(col, "") for col in output_cols if col in row})

    return results


def detect_domain(query):
    """Auto-detect the most relevant domain from query"""
    query_lower = query.lower()

    domain_keywords = {
        "color": ["color", "palette", "hex", "#", "rgb"],
        "chart": ["chart", "graph", "visualization", "trend", "bar", "pie", "scatter", "heatmap", "funnel"],
        "landing": ["landing", "page", "cta", "conversion", "hero", "testimonial", "pricing", "section"],
        "product": ["saas", "ecommerce", "e-commerce", "fintech", "healthcare", "gaming", "portfolio", "crypto", "dashboard"],
        "prompt": ["prompt", "css", "implementation", "variable", "checklist", "tailwind"],
        "style": ["style", "design", "ui", "minimalism", "glassmorphism", "neumorphism", "brutalism", "dark mode", "flat", "aurora"],
        "ux": ["ux", "usability", "accessibility", "wcag", "touch", "scroll", "keyboard", "mobile"],
        "typography": ["font", "typography", "heading", "serif", "sans"],
        "icons": ["icon", "icons", "lucide", "heroicons", "symbol", "glyph", "pictogram", "svg icon"],
        "component": ["component", "button", "dialog", "modal", "input", "select", "accordion", "tabs", "card", "form", "table", "dropdown", "popover", "tooltip", "sheet", "drawer", "avatar", "badge"],
        "animation": ["animation", "animate", "transition", "fade", "slide", "zoom", "spin", "pulse", "bounce", "framer", "motion"],
        "effect": ["effect", "hover", "focus", "active", "loading", "skeleton", "shimmer", "ripple", "glow"],
        "pattern": ["pattern", "sidebar", "command palette", "navigation", "feedback", "empty state", "loading state", "master detail", "kanban", "timeline"]
    }

    scores = {domain: sum(1 for kw in keywords if kw in query_lower) for domain, keywords in domain_keywords.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "style"


def search(query, domain=None, max_results=MAX_RESULTS):
    """Main search function with auto-domain detection"""
    if domain is None:
        domain = detect_domain(query)

    config = CSV_CONFIG.get(domain, CSV_CONFIG["style"])
    filepath = DATA_DIR / config["file"]

    if not filepath.exists():
        return {"error": f"File not found: {filepath}", "domain": domain}

    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)

    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results
    }


def search_stack(query, stack, max_results=MAX_RESULTS):
    """Search stack-specific guidelines"""
    if stack not in STACK_CONFIG:
        return {"error": f"Unknown stack: {stack}. Available: {', '.join(AVAILABLE_STACKS)}"}

    filepath = DATA_DIR / STACK_CONFIG[stack]["file"]

    if not filepath.exists():
        return {"error": f"Stack file not found: {filepath}", "stack": stack}

    results = _search_csv(filepath, _STACK_COLS["search_cols"], _STACK_COLS["output_cols"], query, max_results)

    return {
        "domain": "stack",
        "stack": stack,
        "query": query,
        "file": STACK_CONFIG[stack]["file"],
        "count": len(results),
        "results": results
    }


def search_pattern(query, max_results=MAX_RESULTS):
    """Search cross-platform UX patterns across all pattern files"""
    all_results = []
    pattern_cols = {
        "search_cols": ["Pattern", "Intent", "Trigger"],
        "output_cols": ["Pattern", "Intent", "Trigger", "Web", "Electron", "SwiftUI", "React Native", "Flutter", "Accessibility"]
    }

    for name, file in PATTERN_FILES.items():
        filepath = DATA_DIR / file
        if filepath.exists():
            results = _search_csv(filepath, pattern_cols["search_cols"], pattern_cols["output_cols"], query, max_results)
            for r in results:
                r["_pattern_type"] = name
            all_results.extend(results)

    # Sort by relevance (re-rank if needed) and limit
    return {
        "domain": "pattern",
        "query": query,
        "count": len(all_results[:max_results]),
        "results": all_results[:max_results]
    }


def search_platform(query, platform=None, max_results=MAX_RESULTS):
    """Search platform-specific guidelines"""
    platform_cols = {
        "search_cols": ["Category", "Guideline", "Description"],
        "output_cols": ["Category", "Guideline", "Description", "Do", "Don't", "Platform Notes"]
    }

    if platform and platform in PLATFORM_FILES:
        # Search specific platform
        filepath = DATA_DIR / PLATFORM_FILES[platform]
        if not filepath.exists():
            return {"error": f"Platform file not found: {filepath}"}

        results = _search_csv(filepath, platform_cols["search_cols"], platform_cols["output_cols"], query, max_results)
        return {
            "domain": "platform",
            "platform": platform,
            "query": query,
            "count": len(results),
            "results": results
        }
    else:
        # Search all platforms
        all_results = []
        for name, file in PLATFORM_FILES.items():
            filepath = DATA_DIR / file
            if filepath.exists():
                results = _search_csv(filepath, platform_cols["search_cols"], platform_cols["output_cols"], query, max_results)
                for r in results:
                    r["_platform"] = name
                all_results.extend(results)

        return {
            "domain": "platform",
            "query": query,
            "count": len(all_results[:max_results]),
            "results": all_results[:max_results]
        }


def search_tokens(query, token_type=None):
    """Search design tokens (spacing, typography, color, motion)"""
    def flatten_json(obj, prefix=""):
        """Flatten nested JSON to searchable strings"""
        items = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                new_key = f"{prefix}.{k}" if prefix else k
                if isinstance(v, dict):
                    items.extend(flatten_json(v, new_key))
                else:
                    items.append({"key": new_key, "value": str(v)})
        return items

    def search_in_json(data, query):
        """Search flattened JSON for query matches"""
        flat = flatten_json(data)
        query_lower = query.lower()
        matches = []
        for item in flat:
            if query_lower in item["key"].lower() or query_lower in item["value"].lower():
                matches.append(item)
        return matches

    results = []
    files = [token_type] if token_type and token_type in TOKEN_FILES else TOKEN_FILES.keys()

    for name in files:
        filepath = DATA_DIR / TOKEN_FILES[name]
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            matches = search_in_json(data, query)
            for m in matches:
                m["_token_type"] = name
            results.extend(matches)

    return {
        "domain": "token",
        "query": query,
        "token_type": token_type,
        "count": len(results),
        "results": results[:20]  # Limit token results
    }


AVAILABLE_PLATFORMS = list(PLATFORM_FILES.keys())
AVAILABLE_TOKENS = list(TOKEN_FILES.keys())
