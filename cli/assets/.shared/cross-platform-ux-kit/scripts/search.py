#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI/UX Pro Max Search - BM25 search engine for UI/UX style guides
Usage: python search.py "<query>" [--domain <domain>] [--stack <stack>] [--max-results 3]

Domains: style, prompt, color, chart, landing, product, ux, typography, icons, component, animation, effect, pattern, platform
Stacks: html-tailwind, react, nextjs, vue, svelte, swiftui, react-native, flutter, shadcn, electron
Tokens: spacing, typography, color, motion
Platforms: web, electron, swiftui, react-native, flutter
"""

import argparse
from core import (
    CSV_CONFIG, AVAILABLE_STACKS, MAX_RESULTS,
    search, search_stack, search_pattern, search_platform, search_tokens,
    AVAILABLE_PLATFORMS, AVAILABLE_TOKENS
)


def format_output(result):
    """Format results for Claude consumption (token-optimized)"""
    if "error" in result:
        return f"Error: {result['error']}"

    output = []
    domain = result.get("domain", "unknown")

    if result.get("stack"):
        output.append(f"## UI Pro Max Stack Guidelines")
        output.append(f"**Stack:** {result['stack']} | **Query:** {result['query']}")
        output.append(f"**Source:** {result['file']} | **Found:** {result['count']} results\n")
    elif domain == "token":
        output.append(f"## UI Pro Max Design Tokens")
        output.append(f"**Token Type:** {result.get('token_type', 'all')} | **Query:** {result['query']}")
        output.append(f"**Found:** {result['count']} results\n")
    elif domain == "pattern":
        output.append(f"## UI Pro Max Cross-Platform Patterns")
        output.append(f"**Query:** {result['query']} | **Found:** {result['count']} results\n")
    elif domain == "platform":
        output.append(f"## UI Pro Max Platform Guidelines")
        platform = result.get('platform', 'all')
        output.append(f"**Platform:** {platform} | **Query:** {result['query']}")
        output.append(f"**Found:** {result['count']} results\n")
    else:
        output.append(f"## UI Pro Max Search Results")
        output.append(f"**Domain:** {domain} | **Query:** {result['query']}")
        output.append(f"**Source:** {result.get('file', 'N/A')} | **Found:** {result['count']} results\n")

    for i, row in enumerate(result['results'], 1):
        output.append(f"### Result {i}")
        for key, value in row.items():
            if key.startswith("_"):
                continue  # Skip internal keys
            value_str = str(value)
            if len(value_str) > 500:
                value_str = value_str[:500] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UI Pro Max Search")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="Search domain")
    parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="Stack-specific search")
    parser.add_argument("--pattern", "-p", action="store_true", help="Search cross-platform patterns")
    parser.add_argument("--platform", choices=AVAILABLE_PLATFORMS, help="Platform-specific search")
    parser.add_argument("--token", "-t", choices=AVAILABLE_TOKENS, help="Design token search")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="Max results (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Priority: token > pattern > platform > stack > domain
    if args.token:
        result = search_tokens(args.query, args.token)
    elif args.pattern:
        result = search_pattern(args.query, args.max_results)
    elif args.platform:
        result = search_platform(args.query, args.platform, args.max_results)
    elif args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
    else:
        result = search(args.query, args.domain, args.max_results)

    if args.json:
        import json
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_output(result))
