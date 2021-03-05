import PokemonClass
import catch_pokemon
from all_commands import *
from Gamestate import player
import Citys
import pokemon_change
import Choose_menu


def _help():
    print(main_menu.keys())


def fight():
    player.infight = True
    pokomon_to_fight = PokemonClass.choose_pokemon()
    print("\nDu betritts die Arena und da steht schon ein Pokemon bereit für dich.")
    print("Es ist ein Wildes:", pokomon_to_fight.Name, "Lvl:", pokomon_to_fight.Level)
    print("Seine Hp", pokomon_to_fight.Hp_Current)
    print("Was wirst du tun?\n")
    while player.infight:
        print(">>>Kampfmenü<<<\n")
        user_input = input("A:Kämpfen\nB:Pokemon wechseln\nC:Pokemonstats\nD:Laufen\nE:Pokemon Fangen(noch Instand)\n>")
        if user_input.lower() == "a":
            dmg_calculator(pokomon_to_fight, attackenmenu())
        elif user_input.lower() == "b":
            pokemon_change.pokemon_change()
        elif user_input.lower() == "c":
            stats()
        elif user_input.lower() == "d":
            run()
        elif user_input.lower() == "e":
            catch_pokemon.catch_pokemon(pokomon_to_fight)
        else:
            print("Irgendwas musst du ja machen also sag an!")


def shop():
    Choose_menu.menu("Welchen Händler willst du sprechen?", {"pokeball": Citys.pokeball_trader, "tränke":Citys.potion_trader})



def inventar():
    # eine liste an allen items die der spieler mit sich trägt zb tränke oder pokebälle
    print("\nDiese Funktion ist noch nicht vorhanden!")


def stats():
    print("Was genau möchten sie Wissen?")
    answer = input("A: Aktuelle Pokemon Stats?\nB: Pokemon Wechseln?\nC: Sichern?\nD: Laden\n>")
    if answer.lower() == "a":
        print("Dein", player.current_pokemon.Name, ":", "\n", "Hp:", player.current_pokemon.Hp_Current, "/",
              player.current_pokemon.Hp_Max,
              "\n", "Erfahrung:", player.current_pokemon.Current_ep, "/", player.current_pokemon.Needed_ep, "\n",
              "Level:", player.current_pokemon.Level)

    elif answer.lower() == "b":
        pokemon_change.pokemon_change()
    elif answer.lower() == "c":
        print("Benötigte ep zum Levelup:", (player.current_pokemon.Needed_ep - player.current_pokemon.Current_ep))
    elif answer.lower() == "d":
        print("Dein Aktuelles Pokemon ist:", player.current_pokemon.Name)
        list_all_pokemon()
    else:
        print("Zurück")
        return


def money():
    print("Aktueller Kontostand:", player.money, "€\n")


def pokecenter():
    heal_notheal = input("Schwester Joy: \"Sollen wir uns um Ihr Pokemon kümmern?\"\n>")
    if heal_notheal == "ja":

        for pokemon in player.pokemon_list:
            pokemon.Hp_Current = pokemon.Hp_Max

        player.current_pokemon.Hp_Current = player.current_pokemon.Hp_Max
        for Attack in player.current_pokemon.Attacklist:
            Attack.Attack_Counter_Current = Attack.Attack_Counter_Max
        print("Musik...")
        print("Schwester Joy:\"Deinem Pokemon geht es wieder gut. Beehren sie uns bald wieder!\"")
    elif heal_notheal == "nein":
        print("Schester Joy:\"Okay. Beehren sie uns bald wieder!\"\n")
    else:
        return


def travel():
    pass


def save():
    pass


def load():
    pass


main_menu = {
    'reisen': travel,
    'kämpfen': fight,
    'einkaufen': shop,
    'help': _help,
    'inventar': inventar,
    'stats': stats,
    'wechseln': pokemon_change,
    'save': save,
    'load': load,
    'geld': money,
    'pokecenter': pokecenter
}
