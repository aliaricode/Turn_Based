import requests
import json

def fetch_modern_data():
    print("--- STARTING MODERN DATA SCRAPE ---")

    # ==============================
    #         POKEMON DATA
    # ==============================
    poke_url = "https://play.pokemonshowdown.com/data/pokedex.json"
    print("Fetching Pokedex...")
    raw_poke_data = requests.get(poke_url).json()
    
    modern_pokedex = {}

    for key, info in raw_poke_data.items():
        # We can filter out weird stuff like "Pokestar Studios" if we want,
        # but for now, let's just grab valid pokemon with a number.
        if info.get('num', 0) < 1:
            continue

        # 1. Stats (Split SpA and SpD)
        stats = info.get('baseStats', {})
        stat_list = [
            stats.get('hp', 0),
            stats.get('atk', 0),
            stats.get('def', 0),
            stats.get('spa', 0),
            stats.get('spd', 0),
            stats.get('spe', 0)
        ]

        types = info.get('types', [])
        type_1 = types[0]
        type_2 = types[1] if len(types) > 1 else "None"

        abilities_raw = info.get('abilities', {})
        abil_1 = abilities_raw.get('0', "None")
        abil_2 = abilities_raw.get('1', "None")
        abil_h = abilities_raw.get('H', "None")

        modern_pokedex[info['name']] = stat_list + [type_1, type_2, abil_1, abil_2, abil_h]

    with open('modern_pokedex.json', 'w') as f:
        json.dump(modern_pokedex, f, indent=4)
    print(f"Saved {len(modern_pokedex)} Pokemon to 'modern_pokedex.json'")


    # ==============================
    #          MOVE DATA
    # ==============================
    move_url = "https://play.pokemonshowdown.com/data/moves.json"
    print("Fetching Moves...")
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
        
        modern_moves[info['name']] = [power, accuracy, pp, category, move_type, priority]

    with open('modern_moves.json', 'w') as f:
        json.dump(modern_moves, f, indent=4)
    print(f"Saved {len(modern_moves)} Moves to 'modern_moves.json'")
    print("--- DONE ---")

if __name__ == "__main__":
    fetch_modern_data()