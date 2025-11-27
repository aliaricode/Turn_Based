import pokemon
import battler

def main():

    print("\nStarting Pokemon battle Simulator!")
    
    pokemon1 = pokemon.Pokemon("Charmander", 5, "Scratch", "Swords Dance", "Growl")
    pokemon2 = pokemon.Pokemon("Bulbasaur", 6, "Pound")
    battler.battle(pokemon1, pokemon2)

if __name__ == "__main__":
    main()