# Pokémon Battle Simulator — Prototype

A turn-based Pokémon-style battle simulator. This repository contains a working prototype focused on core battle mechanics; features and APIs will evolve frequently. Expect breaking changes.

## Status
- Prototype: functional local simulation
- Stability: experimental
- Goal: iterate quickly on mechanics, AI, and UI integrations

## Key features (current)
- Turn-based battle loop
- Simple move resolution (damage, accuracy, priority)
- basic stat changes
- Pokémon model with HP, stats, and moves

## Requirements
    - Python 3.8+

## Quick start
1. Clone the repo
     ```
     git clone <repo-url>
     cd <repo-directory>
     ```
2. Install dependencies if you don't have them (like python)

3. Run the simulator (example)
     ```
     python main.py
     ```

## Roadmap / Next items
- adding abilities
- Expand move/effect coverage (status, healing, weather)
- Improve AI decision-making
- Replay visualization and battle viewer
- Networked multiplayer / API
- Persistence for teams and snapshots

## Notes
- This is an actively developed prototype. Back up important work and expect breaking changes between releases.
- For questions or help, open an issue with logs and reproduction steps.
