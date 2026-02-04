# cross-platform-ux-kit

CLI to install Cross-Platform UX Kit skill for AI coding assistants.

## Installation

```bash
npm install -g cross-platform-ux-kit
```

## Usage

```bash
# Install for specific AI assistant
uxkit init --ai claude      # Claude Code
uxkit init --ai cursor      # Cursor
uxkit init --ai windsurf    # Windsurf
uxkit init --ai codex       # Codex (Skills)
uxkit init --ai all         # All assistants

# Other commands
uxkit versions              # List available versions
uxkit update                # Update to latest version
uxkit init --version v1.0.0 # Install specific version
```

## Development

```bash
# Install dependencies
bun install

# Run locally
bun run src/index.ts --help

# Build
bun run build

# Link for local testing
bun link
```

## License

MIT
