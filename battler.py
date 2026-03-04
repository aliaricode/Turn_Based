import random
from brain import Brain
from brain import player
from utils import slow_print
from type_chart import effectivness
import subprocess

def damage_calc(pokemon1, pokemon2, used_attack):
    match used_attack.category:
        case("Physical"):
            atk = pokemon1.atk
            dfs = pokemon2.dfs
        case("Special"):
            atk = pokemon1.spa
            dfs = pokemon2.spd
        case(__):
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
        subprocess.run('clear')
        pokemon.use_move()
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
                slow_print(f"{pokemon.name} missed!")
        else:
                if move.stat != {}:
                    for stat in move.stat:
                        match move.target:
                            case("self"):
                                slow_print(f"{pokemon.name} raised it's {stat} by {move.stat[stat]} stages!")
                                pokemon.change_stat(stat, move.stat[stat])
                            case("allAdjacentFoes"):
                                slow_print(f"{pokemon.name} lowered {target.name}'s {stat} by {-1 * (move.stat[stat])} stages!")
                                target.change_stat(stat, move.stat[stat])
                            case(__):
                                slow_print("not yet implemented")

def sequence_set(pokemon1, pokemon2):        
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
    return first, second


def battle(player1, player2):
    team1 = player1.team
    team2 = player2.team
    pokemon1 = team1[0]
    pokemon2 = team2[0]

    if pokemon1.hp == 0:
        for poke in team1:
            if poke.hp != 0:
                pokemon1 = poke
                break

    pokemon2.name = f"Enemy {pokemon2.name}"
    while player1.team_checker() and player2.team_checker():

        pokemon1.move = player(pokemon1)
        pokemon2.move = Brain(pokemon2)

        if type(pokemon1.move) == str:
            match(pokemon1.move):
                case "pokemon":
                    pokemon1 = player1.switch_pokemon(pokemon1)
                    first = pokemon1
                    second = pokemon2
                case "item":
                    print("not yet implemented!")
                case "run":
                    break
        else:
            first, second = sequence_set(pokemon1, pokemon2)
            turn(first, second, first.move)

        if second.hp != 0:            
            turn(second, first, second.move)
        if pokemon1.hp <= 0:
            slow_print(f"{pokemon1.name} fainted!")
            if not player1.team_checker():
                slow_print("You are out of usable pokemon!\nYou have lost")
            else:
                pokemon1 = player1.switch_pokemon()
        elif pokemon2.hp <= 0:
            slow_print(f"{pokemon2.name} fainted!")
            if not player2.team_checker():
                slow_print("Your opponent is out of usable pokemon\nYou have won!")