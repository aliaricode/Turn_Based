import subprocess
from utils import slow_print
from random import randint
from database import items

class Player:
    def __init__(self, name, team, items={}, ai=None):
        self.name = name
        self.team = team
        self.items = items
        self.ai = ai

    def team_checker(self):
        fainted = 0

        for poke in self.team:
            if poke.hp == 0:
                fainted += 1
        if fainted == len(self.team):
            return False
        return True

    def choose_pokemon(self, reason, used=None):
        if self.ai == "player":
            while True:
                subprocess.run('clear')
                for index, pokemon in enumerate(self.team, 1):
                    print(f"{index} -- {pokemon.name}")
                slow_print(f"Which pokemon do you want to {reason}?")

                try:
                    choice = int(input("-> "))
                    if 6 >= choice and choice >= 1:
                        if self.team[choice - 1].name == "None":
                            slow_print("Selected slot is empty!")
                        elif self.team[choice - 1].hp == 0:
                            slow_print("Selected pokemon is already fainted!")
                        elif self.team[choice -1] == used:
                            slow_print("The selected pokemon is already out!")
                        else:
                            pokemon.reset_soft_stats()
                            return self.team[choice - 1]
                    else:
                        slow_print("Please input a valid number!")
                except:
                    raise ValueError("please input a number!")
        else:
            possible = []
            for poke in self.team:
                if poke.hp > 0:
                    possible.append(poke)
            selected = possible[randint(0, len(possible)-1)]
            slow_print(f"{self.name} sent out {selected.name}")
            return selected
    
    def choose_item(self):
        if self.ai == "player":
            while True:
                subprocess.run("clear")
                for index, item in enumerate(self.items, 1):
                    print(f"{index} -- {item}")
                slow_print("Which item would you like to use?")

                try:
                    choice = int(input("-> "))
                    if 0 < choice <= len(self.items):
                        return self.items[choice-1]
                    elif choice == 0:
                        return 0
                    else:
                        slow_print("Please input a valid number!")
                except:
                    raise ValueError("Please input a number!")
            
    def use_item(self):
        item = self.choose_item()
        if item == 0:
            pass
        chosen_pokemon = self.choose_pokemon(f"use {item} on")
        slow_print(f"used {item} on {chosen_pokemon.name}!\nHealed {chosen_pokemon.name} by {items[item]}")
        chosen_pokemon.heal(items[item])