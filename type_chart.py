type_chart = {
    "Normal": {
        "Rock": 0.5, 
        "Ghost": 0.0, 
        "Steel": 0.5
    },
    "Fire": {
        "Fire": 0.5, "Water": 0.5, "Grass": 2.0, "Ice": 2.0, 
        "Bug": 2.0, "Rock": 0.5, "Dragon": 0.5, "Steel": 2.0
    },
    "Water": {
        "Fire": 2.0, "Water": 0.5, "Grass": 0.5, 
        "Ground": 2.0, "Rock": 2.0, "Dragon": 0.5
    },
    "Electric": {
        "Water": 2.0, "Electric": 0.5, "Grass": 0.5, 
        "Ground": 0.0, "Flying": 2.0, "Dragon": 0.5
    },
    "Grass": {
        "Fire": 0.5, "Water": 2.0, "Grass": 0.5, "Poison": 0.5, 
        "Ground": 2.0, "Flying": 0.5, "Bug": 0.5, "Rock": 2.0, 
        "Dragon": 0.5, "Steel": 0.5
    },
    "Ice": {
        "Fire": 0.5, "Water": 0.5, "Grass": 2.0, "Ice": 0.5, 
        "Ground": 2.0, "Flying": 2.0, "Dragon": 2.0, "Steel": 0.5
    },
    "Fighting": {
        "Normal": 2.0, "Ice": 2.0, "Poison": 0.5, "Flying": 0.5, 
        "Psychic": 0.5, "Bug": 0.5, "Rock": 2.0, "Ghost": 0.0, 
        "Dark": 2.0, "Steel": 2.0, "Fairy": 0.5
    },
    "Poison": {
        "Grass": 2.0, "Poison": 0.5, "Ground": 0.5, "Rock": 0.5, 
        "Ghost": 0.5, "Steel": 0.0, "Fairy": 2.0
    },
    "Ground": {
        "Fire": 2.0, "Electric": 2.0, "Grass": 0.5, "Poison": 2.0, 
        "Flying": 0.0, "Bug": 0.5, "Rock": 2.0, "Steel": 2.0
    },
    "Flying": {
        "Electric": 0.5, "Grass": 2.0, "Fighting": 2.0, 
        "Bug": 2.0, "Rock": 0.5, "Steel": 0.5
    },
    "Psychic": {
        "Fighting": 2.0, "Poison": 2.0, "Psychic": 0.5, 
        "Dark": 0.0, "Steel": 0.5
    },
    "Bug": {
        "Fire": 0.5, "Grass": 2.0, "Fighting": 0.5, "Poison": 0.5, 
        "Flying": 0.5, "Psychic": 2.0, "Ghost": 0.5, "Dark": 2.0, 
        "Steel": 0.5, "Fairy": 0.5
    },
    "Rock": {
        "Fire": 2.0, "Ice": 2.0, "Fighting": 0.5, "Ground": 0.5, 
        "Flying": 2.0, "Bug": 2.0, "Steel": 0.5
    },
    "Ghost": {
        "Normal": 0.0, "Psychic": 2.0, "Ghost": 2.0, "Dark": 0.5
    },
    "Dragon": {
        "Dragon": 2.0, "Steel": 0.5, "Fairy": 0.0
    },
    "Steel": {
        "Fire": 0.5, "Water": 0.5, "Electric": 0.5, "Ice": 2.0, 
        "Rock": 2.0, "Steel": 0.5, "Fairy": 2.0
    },
    "Dark": {
        "Fighting": 0.5, "Psychic": 2.0, "Ghost": 2.0, 
        "Dark": 0.5, "Fairy": 0.5
    },
    "Fairy": {
        "Fire": 0.5, "Fighting": 2.0, "Poison": 0.5, 
        "Dragon": 2.0, "Steel": 0.5, "Dark": 2.0
    }
}

def effectivness(move_type, pokemon_type):
    if type(pokemon_type) == str:
        pokemon_type = [pokemon_type]

    multiplier = 1
    for poke_type in pokemon_type:    
        if poke_type in type_chart[move_type]:
            multiplier *= type_chart[move_type][poke_type]
    return multiplier