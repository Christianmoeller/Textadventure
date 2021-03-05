import all_commands
import PokemonClass
import Gamestate
import Conversations
import Story_lines
from Mainmenu import main_menu



def main():
    print(Conversations.Intro)
    #gs = Gamestate.Gamestate("", 0, [], "", [])
    Gamestate.player.name = input("\"Wie lautet dein Name?\"\n>")
    print("Prof. Acai: \"Ich heisse dich Willkommen", Gamestate.player.name,"\"","\n\"Mein Name ist Prof. Acai\"\n\"Um Deine Reise starten zu können, brauchst Du natürlich erstmal ein Start-Pokemon.\"\n\"Bitte wähle eines der folgenen aus:\"")
    firstpokemon = input("Schiggy-WASSER; Glumanda-FEUER, Bisasam-PFLANZE\n>")
    Gamestate.player.pokemon_list.append(PokemonClass.startpokemon(firstpokemon))
    Gamestate.player.current_pokemon = Gamestate.player.pokemon_list[0]
    #startPokemon = PokemonClass.startpokemon(firstpokemon)
    while True:
        print(">>>Hauptmenü<<<")
        new_user_input = input("Was willst du tun?\nKämpfen ---> Kämpfe gegen ein zufälliges Pokemon\nPokecenter ---> Heilt Dein Pokemon\nStats ---> Infos über Dein Pokemon\nGeld ---> Dein Kontostand\n>").lower().split(" ")
        if new_user_input[0].lower() in main_menu:
            main_menu[new_user_input[0]]()
main()