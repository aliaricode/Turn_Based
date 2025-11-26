import random

def player(pokemon):
    moves = [pokemon.move1, pokemon.move2, pokemon.move3, pokemon.move4]
    while True:
        print("-"*20)
        for index, move in enumerate(moves, 1):
            if move.name != "None":
                    print(f"{index}. {move.name}")
            else:
                print(f"{index}. --")
        print("Choose your attack: ")

        try:
            choice = int(input("> "))
                
            if 1 <= choice <= 4:
                selected_move = moves[choice - 1]
                if selected_move.name == "None":
                        print("That move slot is empty!")
                else:
                    return selected_move
            else:
                print("Please choose a number between 1 and 4.")
        except ValueError:
                print("Invalid input! Please enter a number.")

def Brain(pokemon):
    all_moves = [pokemon.move1, pokemon.move2, pokemon.move3, pokemon.move4]
    valid_moves = []
    for move in all_moves:
        if move.name != "None":
            valid_moves.append(move)
    return random.choice(valid_moves)