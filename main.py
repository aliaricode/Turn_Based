import builder
import battler

def main():

    print("\nStarting Pokemon battle Simulator!")
    
    pokemon1 = builder.Pokemon("Charmander", 5, "Scratch")
    pokemon2 = builder.Pokemon("Bulbasaur", 6, "Pound")
    battler.battle(pokemon1, pokemon2)

if __name__ == "__main__":
    main()