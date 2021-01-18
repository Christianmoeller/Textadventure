import all_commands
import PokemonClass
import Gamestate



def main():
    print("Wilkommen in der unglaubelichen Welt von Pokemon 2.0!\nSicher fragst du dich was wie das sein kann.\nDoch das lernst du im laufe deses Spiels.")
    gs = Gamestate.Gamestate("", 0, [], "")
    gs.name = input("Wie lautet dein Name?\n")
    print("Hallo",gs.name, ".Zu Beginn brauchst du natürlich erstmal ein Start-Pokemon.\nBitte wähle eines der folgenen aus:")
    firstpokemon = input("Schiggy-WASSER; Glumanda-FEUER, Bisasam-PFLANZE\n")
    gs.current_pokemon = PokemonClass.startpokemon(firstpokemon)
    #startPokemon = PokemonClass.startpokemon(firstpokemon)
    while True:
        new_user_input = input("Was willst du tun?\n>>help<< für mehr Infos\n").lower().split(" ")
        if new_user_input[0] in all_commands.new_Commands:
            all_commands.new_Commands[new_user_input[0]](gs)
main()