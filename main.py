from pokemon import Pokemon
from player import Player
from battler import battle
from utils import slow_print
import subprocess

def main():

    subprocess.run("clear")
    slow_print("\nStarting Pokemon battle Simulator!")
    
    pokemon1 = Pokemon("Charmander", 5, "Scratch", "Swords Dance", "Growl")
    pokemon2 = Pokemon("Charizard", 4, "Ember", "Explosion")
    pokemon3 = Pokemon("Bulbasaur", 6, "Pound")
    pokemon4 = Pokemon("Squirtle", 5, "Tackle")

    team1 = [pokemon1, pokemon2]
    team2 = [pokemon3, pokemon4]

    player1 = Player("imperium",team1, [], "player")
    player2 = Player("Ayda", team2)

    battle(player1, player2)

if __name__ == "__main__":
    main()