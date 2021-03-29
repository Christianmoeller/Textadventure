import Conversations
import Gamestate
from PokemonClass import startpokemon
from Choose_menu import menu
from Mainmenu import fight, pokecenter, pokemon_stats, money, save, load_game, shop, inventar, trainer_fight
from pokemon_change import pokemon_change
from Trainer import chosse_trainer
import all_commands


def main():
    print(Conversations.Intro)
    Gamestate.player.name = input("\"Wie lautet dein Name?\"\n>")
    print("Prof. Acai: \"Ich heisse dich Willkommen", Gamestate.player.name, "\"",
          "\n\"Mein Name ist Prof. Acai\"\n\"Um Deine Reise starten zu können, brauchst Du natürlich erstmal ein Start-Pokemon.\"\n\"Bitte wähle eines der folgenen aus:\"")
    firstpokemon = input("Schiggy-WASSER; Glumanda-FEUER, Bisasam-PFLANZE\n>")
    Gamestate.player.pokemon_list.append(startpokemon(firstpokemon))
    Gamestate.player.current_pokemon = Gamestate.player.pokemon_list[0]
    while True:
        print(">>>Hauptmenü<<<")
        menu("Was willst du tun?\n",
             {"Kämpfen": fight, "Pokecenter": pokecenter, "Pokemon": pokemon_stats, "Pokemon wechseln": pokemon_change,
              "Inventar": inventar,
              "Geldbeutel": money, "Einkaufen": shop,"Trainer Kampf":trainer_fight, "save": save, "load": load_game})


main()
