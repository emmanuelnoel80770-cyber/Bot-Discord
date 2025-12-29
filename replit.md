# Discord Bot Project

## Overview

This is a Discord bot built with Python using the discord.py library. The bot follows a modular architecture using the Cogs extension system, allowing features to be organized into separate, loadable modules. Currently, the bot has basic connectivity functionality and a placeholder for thread-related features.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Bot Framework
- **Framework**: discord.py with commands extension
- **Pattern**: Cogs-based modular architecture
- **Rationale**: Cogs allow separating bot functionality into independent modules that can be loaded/unloaded dynamically, making the codebase more maintainable and organized

### Project Structure
```
├── main.py          # Bot entry point and initialization
└── cogs/            # Feature modules directory
    ├── system_message.py  # Bot connection/ready events
    └── threads.py         # Thread-related functionality (placeholder)
```

### Core Components

1. **Main Bot Class (BotDiscord)**
   - Extends `commands.Bot`
   - Uses `setup_hook` for async cog loading
   - Command prefix: `!`
   - Full intents enabled (`discord.Intents.all()`)

2. **Cog: system_message**
   - Handles bot lifecycle events
   - Currently implements `on_ready` listener for connection confirmation

3. **Cog: threads**
   - Placeholder module for thread-related features
   - Structure ready for implementation

### Authentication
- Bot token stored in environment variable `Token_Bot_Discord`
- Token accessed via `os.environ` for security

## External Dependencies

### Python Packages
- **discord.py**: Core Discord API wrapper and bot framework
- **Standard library**: `os` for environment variable access

### External Services
- **Discord API**: Bot connects to Discord's gateway for real-time events and interactions
- **Environment Variables**: 
  - `Token_Bot_Discord` - Discord bot authentication token (required)