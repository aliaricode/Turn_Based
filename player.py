import subprocess
from utils import slow_print

class Player:
    def __init__(self, name, team, items=[], ai=None):
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

    def switch_pokemon(self, used=None):
        while True:
            subprocess.run('clear')
            for index, pokemon in enumerate(self.team, 1):
                print(f"{index} -- {pokemon.name}")
            slow_print("Which pokemon do you want to switch to?")

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