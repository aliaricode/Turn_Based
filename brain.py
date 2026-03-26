import random
import subprocess
from utils import slow_print

def player(pokemon):
     moves = ["Fight", "Bag", "Pokemon", "Run"]
     while True:
        subprocess.run("clear")
        print("-"*20)
        for index, move in enumerate(moves, 1):
            print(f"{index}. {move}")
        print("Choose your attack: ")

        try:
            choice = int(input("-> "))

            if 1 <= choice <= 4:

                match choice:
                    case 1:
                        subprocess.run("clear")
                        return player_move(pokemon)
                    case 2:
                        return "item"
                    case 3:
                        return "pokemon"
                    case 4:
                        return "run"
                    case _:
                        slow_print("please input a valid number")

        except ValueError:
            slow_print("Please choose a number!")

def player_move(pokemon):
    moves = [pokemon.move1, pokemon.move2, pokemon.move3, pokemon.move4]
    while True:
        subprocess.run('clear')
        print("-"*20)
        for index, move in enumerate(moves, 1):
            if move.name != "None":
                    print(f"{index}. {move.name} ({move.pp})")
            else:
                print(f"{index}. --")
        print("Choose your attack: ")

        try:
            choice = int(input("-> "))
                
            if 1 <= choice <= 4:
                selected_move = moves[choice - 1]
                if selected_move.name == "None":
                        slow_print("That move slot is empty!")
                else:
                    if selected_move.pp == 0:
                        slow_print(f"{selected_move.name} has no pp left!")
                    else:
                        return selected_move
            else:
                slow_print("Please choose a number between 1 and 4.")
        except ValueError:
                slow_print("Invalid input! Please enter a number.")

def Brain(pokemon):
    all_moves = [pokemon.move1, pokemon.move2, pokemon.move3, pokemon.move4]
    valid_moves = []
    for move in all_moves:
        if move.name != "None":
            valid_moves.append(move)
    return random.choice(valid_moves)