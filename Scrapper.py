import requests
import json

def fetch_modern_data():
    print("--- STARTING MODERN DATA SCRAPE (Standard) ---")

    # ==============================
    # PART 1: POKEMON DATA (Gen 9)
    # ==============================
    poke_url = "https://play.pokemonshowdown.com/data/pokedex.json"
    print("Fetching Pokedex...")
    
    # Reverted to standard request (No verify=False)
    raw_poke_data = requests.get(poke_url).json()
    
    modern_pokedex = {}

    for key, info in raw_poke_data.items():
        if info.get('num', 0) < 1:
            continue

        # Stats
        stats = info.get('baseStats', {})
        stat_list = [
            stats.get('hp', 0),
            stats.get('atk', 0),
            stats.get('def', 0),
            stats.get('spa', 0),
            stats.get('spd', 0),
            stats.get('spe', 0)
        ]

        # Types
        types = info.get('types', [])
        type_1 = types[0]
        type_2 = types[1] if len(types) > 1 else "None"

        # Abilities
        abilities_raw = info.get('abilities', {})
        abil_1 = abilities_raw.get('0', "None")
        abil_2 = abilities_raw.get('1', "None")
        abil_h = abilities_raw.get('H', "None")

        # Format: [HP, Atk, Def, SpA, SpD, Spe, Type1, Type2, Abil1, Abil2, Hidden]
        modern_pokedex[info['name']] = stat_list + [type_1, type_2, abil_1, abil_2, abil_h]

    with open('modern_pokedex.json', 'w') as f:
        json.dump(modern_pokedex, f, indent=4)
    print(f"Saved {len(modern_pokedex)} Pokemon.")


    # ==============================
    # PART 2: MOVE DATA (Safe Defaults)
    # ==============================
    move_url = "https://play.pokemonshowdown.com/data/moves.json"
    print("Fetching Moves...")
    
    # Reverted to standard request
    raw_move_data = requests.get(move_url).json()

    modern_moves = {}

    for key, info in raw_move_data.items():
        category = info.get('category', 'Status')
        power = info.get('basePower', 0)
        
        accuracy = info.get('accuracy', 100)
        if accuracy is True: accuracy = 100 
        
        pp = info.get('pp', 0)
        move_type = info.get('type', 'Normal')
        priority = info.get('priority', 0)

        # Boosts: Default to empty dict {} instead of None
        # Logic: info.get('boosts') might return None if the key exists but is null
        # using 'or {}' ensures it is always a dictionary.
        boosts = info.get('boosts') or {}

        # Status: Default to string "None" instead of None
        status = info.get('status') or "None"
        
        target = info.get('target', 'normal')
        
        flags = info.get('flags', {})

        # Format: [Power, Accuracy, PP, Category, Type, Priority, Boosts, Status, Target, Flags]
        modern_moves[info['name']] = [
            power, 
            accuracy, 
            pp, 
            category, 
            move_type, 
            priority, 
            boosts, 
            status, 
            target,
            flags 
        ]

    with open('modern_moves.json', 'w') as f:
        json.dump(modern_moves, f, indent=4)
    print(f"Saved {len(modern_moves)} Moves.")
    print("--- DONE ---")

if __name__ == "__main__":
    fetch_modern_data()