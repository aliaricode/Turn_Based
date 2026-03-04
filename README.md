# Python Pokémon Battle Engine

A fully functional, terminal-based turn-based fighting game engine. Built with a modular architecture, this simulator decouples the core battle logic from the data layer by dynamically scraping the latest Generation 9 stats directly from Pokémon Showdown.

## Features

* **Dynamic Data Scraper:** Pulls the most up-to-date Pokémon base stats, typings, and move data using a custom API scraper.
* **Accurate Damage Mechanics:** Implements the official damage formula, including STAB (Same Type Attack Bonus), critical hits, random damage variance, and a full type effectiveness matrix.
* **Stat Modifiers:** Fully functional buff/debuff system (up to +/- 6 stages) for in-battle stat changes.
* **Turn Resolution:** Priority brackets and speed stats dynamically calculate the sequence of turns.
* **Retro UI:** Text-based interface utilizing a custom `slow_print` utility to mimic the classic Gameboy-era RPG feel.

## Tech Stack & Architecture

* **Language:** Python 3.10+
* **Design Pattern:** Object-Oriented Programming (OOP) with distinct state management for `Pokemon`, `Move`, `Player`, and `Brain` (AI).
* **Data Handling:** JSON-based persistent storage populated via REST API scraping.

## Quick Start

### 1. Clone the repository
```bash
git clone [https://github.com/Imperium34/Turn_Based.git](https://github.com/Imperium34/Turn_Based.git)
cd Turn_Based
```

### 2. Install dependencies
The scraper requires the `requests` library to fetch game data.
```bash
pip install requests
```

### 3. Generate Game Data (Required)
To ensure you have the latest stats and to keep the repository lightweight, you must fetch the data locally before playing:
```bash
python Scrapper.py
```

### 4. Run the Simulator
```bash
python main.py
```

## Roadmap / Future Implementations
* [ ] **Inventory System:** Implement held items and bag functionality during battles.
* [ ] **Abilities:** Integrate ability effects into the `damage_calc` loop.
* [ ] **Status Conditions:** Add Burn, Paralysis, Poison, Sleep, and Freeze logic.
* [ ] **Advanced AI:** Upgrade `brain.py` from random valid-move selection to heuristic decision-making.