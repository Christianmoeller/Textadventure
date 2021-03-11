import all_commands
import PokemonClass
import Gamestate
import Conversations
import Story_lines
from Mainmenu import *
import Choose_menu
from pokemon_change import *



def main():
    print(Conversations.Intro)
    player.name = input("\"Wie lautet dein Name?\"\n>")
    print("Prof. Acai: \"Ich heisse dich Willkommen", player.name,"\"","\n\"Mein Name ist Prof. Acai\"\n\"Um Deine Reise starten zu können, brauchst Du natürlich erstmal ein Start-Pokemon.\"\n\"Bitte wähle eines der folgenen aus:\"")
    firstpokemon = input("Schiggy-WASSER; Glumanda-FEUER, Bisasam-PFLANZE\n>")
    player.pokemon_list.append(startpokemon(firstpokemon))
    player.current_pokemon = player.pokemon_list[0]
    while True:
        print(">>>Hauptmenü<<<")
        Choose_menu.menu("Was willst du tun?\n",{"Kämpfen":fight, "Pokecenter":pokecenter, "Pokemon":pokemon_stats, "Pokemon wechseln":pokemon_change, "Geldbeutel":money, "save":save, "load":load_game})
main()
