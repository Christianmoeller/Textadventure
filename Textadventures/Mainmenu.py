import PokemonClass
import catch_pokemon
from all_commands import *
from Gamestate import *
import Citys
import pokemon_change
import Choose_menu
import json


def _help():
    pass


def fight():
    player.infight = True
    player.pokemon_to_fight = PokemonClass.choose_pokemon()
    print("\nDu betritts die Arena und da steht schon ein Pokemon bereit für dich.")
    print("Es ist ein Wildes:", player.pokemon_to_fight.Name, "Lvl:", player.pokemon_to_fight.Level)
    print("Seine Hp", player.pokemon_to_fight.Hp_Current)
    print("Was wirst du tun?\n")
    while player.infight:
        print(">>>Kampfmenü<<<\n")
        Choose_menu.menu("Was willst du tun", {"angriff":attackenmenu,"pokemon wechseln":pokemon_change.pokemon_change,
                                               "stats":pokemon_change.pokemon_change, "laufen":run,"fangen":catch_pokemon.catch_pokemon})





def shop():
    Choose_menu.menu("Welchen Händler willst du sprechen?", {"pokeball": Citys.pokeball_trader, "tränke":Citys.potion_trader})



def inventar():
    # eine liste an allen items die der spieler mit sich trägt zb tränke oder pokebälle
    print("\nDiese Funktion ist noch nicht vorhanden!")


def pokemon_stats():
    Choose_menu.menu("Was genau willst du Wissen", {"Alle Pokemon":list_all_pokemon,
    "Aktuelles Pokemon Stats":current_pokemon_stats})


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
    player.save("gamestate.json")
    print("Spielstand Gespeichert")


def load_game():
    player = load("gamestate.json")



