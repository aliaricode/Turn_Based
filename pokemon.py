import json
import moves
from utils import slow_print

try:
    with open('modern_pokedex.json', 'r') as f:
        POKEMON_DB = json.load(f)
except FileNotFoundError:
    print("Error: JSON files not found! Run 'modern_scraper.py' first.")
    POKEMON_DB = {}

class Pokemon:
    def __init__(self, species, lvl, move1, move2=None, move3=None, move4=None, name=None):
        if species not in POKEMON_DB:
            raise ValueError("Species not found")
        if not (1 <= int(lvl) <= 100):
            raise ValueError("Level must be between 1 and 100")
        
        self.species = species
        if name == None:
            name = self.species
        self.name = name

        self.lvl = int(lvl)
        self.move1 = moves.Move(move1)
        self.move2 = moves.Move(move2)
        self.move3 = moves.Move(move3)
        self.move4 = moves.Move(move4)
        
        base = POKEMON_DB[species]
        self.type = [base[6]]
        if base[7] != "None":
            self.type.append(base[7])
        
        self.base_hp = base[0]
        self.base_atk = base[1]
        self.base_dfs = base[2]
        self.base_spa = base[3]
        self.base_spd = base[4]
        self.base_spe = base[5]

        self.max_hp = (base[0] * 2 * self.lvl // 100 + self.lvl + 10)
        self.hp = self.max_hp
        self.atk = (base[1] * 2 * self.lvl // 100 + 5)
        self.dfs = (base[2] * 2 * self.lvl // 100 + 5)
        self.spa = (base[3] * 2 * self.lvl // 100 + 5)
        self.spd = (base[4] * 2 * self.lvl // 100 + 5)
        self.spe = (base[5] * 2 * self.lvl // 100 + 5)
    
    def get_base_stat(self, stat):
        match stat:
            case("hp"):
                return self.base_hp
            case("atk"):
                return self.base_atk
            case("dfs"):
                return self.base_dfs
            case("spa"):
                return self.base_spa
            case("spd"):
                return self.base_spd
            case("spe"):
                return self.base_spe
        
    def get_stat(self, stat):
        match stat:
            case("hp"):
                return self.hp
            case("atk"):
                return self.atk
            case("dfs"):
                return self.dfs
            case("spa"):
                return self.spa
            case("spd"):
                return self.spd
            case("spe"):
                return self.spe

    def change_stat(self, stat, stage):
        if self.get_stat(stat) > (3 * self.get_base_stat(stat) * 2 * self.lvl // 100 + 5) and stage > 0:
            slow_print(f"{self.name}'s {stat} can't get raised anymore!")
        elif self.get_stat(stat) < (self.get_base_stat(stat) * 2 * self.lvl // 100 + 5) / 3 and stage < 0:
            slow_print(f"{self.name}'s {stat} can't get lowered anymore!")
        else:
          match stat:
            case("atk"):
                self.atk += self.atk * (stage * 0.5)
            case("dfs"):
                self.dfs += self.dfs * (stage * 0.5)
            case("spa"):
                self.spa += self.spa * (stage * 0.5)
            case("spd"):
                self.spd += self.spd * (stage * 0.5)
            case("spe"):
                self.spe += self.spe * (stage * 0.5)


    def heal(self, amount):
        self.hp += amount

    def take_damage(self, damage):
        self.hp -= damage