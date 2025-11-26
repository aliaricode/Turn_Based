import random
import brain
from utils import slow_print
from type_chart import effectivness

def damage_calc(pokemon1, pokemon2, used_attack):
    if used_attack.category == "Physical":
         atk = pokemon1.atk
         dfs = pokemon2.dfs
    elif used_attack.category == "Special":
         atk = pokemon1.spa
         dfs = pokemon2.spd
    else:
         raise ValueError("this is not a damage move!")
    lvl = pokemon1.lvl
    if random.randint(0, 100) >= 95:
         lvl = lvl * 2
    damage = round(((2 * lvl + 5) * used_attack.pwr * atk) / (dfs * 50))
    if used_attack.type in pokemon1.type:
        damage = round(damage * 1.5)
    damage = damage * effectivness(used_attack.type, pokemon2.type)
    damage = round(damage * (random.randint(85, 100) / 100))
    if damage > pokemon2.hp:
         damage = pokemon2.hp
    return damage

def turn(pokemon, target, move):
        slow_print(f"{pokemon.name} used {move.name}!")
        if move.category != "Status":
            if move.acc * 255/100 > random.randint(0, 255):
                damage = damage_calc(pokemon, target, move)
                if effectivness(move.type, target.type) > 1:
                    slow_print("It's super effective!")
                if effectivness(move.type, target.type) < 1:
                    slow_print("it's not very effective...")
                target.take_damage(damage)
                slow_print(f"{target.name} took {damage} damage!")
            else:
                slow_print(f"{pokemon.name} missed like an idiot lmao what a loser")
        else:
                slow_print("not yet implemented")

def battle(pokemon1, pokemon2):

    pokemon2.name = f"Enemy {pokemon2.name}"
    while pokemon1.hp > 0 and pokemon2.hp > 0:

        pokemon1.move = brain.player(pokemon1)
        pokemon2.move = brain.Brain(pokemon2)

        if pokemon1.move.prio > pokemon2.move.prio:
            first = pokemon1
            second = pokemon2
        elif pokemon2.move.prio > pokemon1.move.prio:
            first = pokemon2
            second = pokemon1

        else:
            if pokemon1.spe > pokemon2.spe:
                first = pokemon1
                second = pokemon2
            elif pokemon2.spe > pokemon1.spe:
                first = pokemon2
                second = pokemon1
            else:
                if random.random() > 0.5:
                    first = pokemon1
                    second = pokemon2
                else:
                    first = pokemon2
                    second = pokemon1

        turn(first, second, first.move)

        if second.hp <= 0:
                break
            
        turn(second, first, second.move)
        
    if pokemon1.hp <= 0:
        slow_print(f"{pokemon1.name} fainted!")
        slow_print("you lost!")
    elif pokemon2.hp <= 0:
        slow_print(f"{pokemon2.name} fainted!")
        slow_print("You won!")