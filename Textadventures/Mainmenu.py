import PokemonClass
import catch_pokemon
from all_commands import attackenmenu, list_all_pokemon, run, current_pokemon_stats
import pokemon_change
import Choose_menu
import Gamestate
import Trader
from Trainer import chosse_trainer


def trainer_fight():
    trainer_to_fight = chosse_trainer()
    trainer_list_len = len(trainer_to_fight.pokemon_list)
    player_list_len = len(Gamestate.player.pokemon_list)
    Gamestate.player.pokemon_to_fight = trainer_to_fight.pokemon_list[0]
    print(trainer_to_fight.name, "möchte Kämpfen.\n", trainer_to_fight.name, "'s erstes Pokemon ist:", Gamestate.player.pokemon_to_fight.Name,
          "Level:", Gamestate.player.pokemon_to_fight.Level)
    Gamestate.player.infight = True
    while Gamestate.player.infight and trainer_list_len > 0 and player_list_len > 0:
        print(">>>Kampfmenü<<<\n")
        Choose_menu.menu("Was willst du tun",
                         {"Angriff": attackenmenu, "Pokemon wechseln": pokemon_change.pokemon_change,
                          "Status deiner Pokemon": pokemon_stats})


def fight():
    Gamestate.player.infight = True
    Gamestate.player.pokemon_to_fight = PokemonClass.choose_pokemon()
    print("\nDu betritts die Arena und da steht schon ein Pokemon bereit für dich.")
    print("Es ist ein Wildes:", Gamestate.player.pokemon_to_fight.Name, "Lvl:", Gamestate.player.pokemon_to_fight.Level)
    print("Seine Hp", Gamestate.player.pokemon_to_fight.Hp_Current)
    print("Was wirst du tun?\n")
    while Gamestate.player.infight:
        print(">>>Kampfmenü<<<\n")
        Choose_menu.menu("Was willst du tun",
                         {"Angriff": attackenmenu, "Pokemon wechseln": pokemon_change.pokemon_change,
                          "Status deiner Pokemon": pokemon_stats, "Weg laufen": run,
                          "Pokemon fangen": catch_pokemon.catch_pokemon})


def shop():
    Choose_menu.menu("Welchen Händler willst du sprechen?", {"Händer aus Vertania City": Trader.trader_VertaniaCity})


def inventar():
    if Gamestate.player.inventar == {}:
        print("Dein Inventar ist leer. Geh in den Shop um dir Items zu kaufen.")
    else:
        print("In deinem Inventar befinden sich folgende Items")
        for key, value in Gamestate.player.inventar.items():
            print(key.name, value)


def pokemon_stats():
    Choose_menu.menu("Was genau willst du Wissen", {"Alle Pokemon": list_all_pokemon,
                                                    "Aktuelles Pokemon Stats": current_pokemon_stats})


def money():
    print("Aktueller Kontostand:", Gamestate.player.money, "€\n")


def pokecenter():
    heal_notheal = input("Schwester Joy: \"Sollen wir uns um Ihr Pokemon kümmern?\"\n>")
    if heal_notheal == "ja":

        for pokemon in Gamestate.player.pokemon_list:
            pokemon.Hp_Current = pokemon.Hp_Max

        Gamestate.player.current_pokemon.Hp_Current = Gamestate.player.current_pokemon.Hp_Max
        for Attack in Gamestate.player.current_pokemon.Attacklist:
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
    Gamestate.player.save("gamestate.json")
    print("Spielstand Gespeichert")


def load_game():
    player = Gamestate.load("gamestate.json")
