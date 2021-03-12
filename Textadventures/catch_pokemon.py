import Gamestate
import Items
import Inventar
import random


def catch_pokemon():
    # forall bälle (hyper, super, poke)
    #         haben wir welche? ja -> füge einer neuen liste hinzu
    if Inventar.inventar_check():  # sollte ein item vorhanden sein = True ansonsten false und retun "du hast keine items"
        if Inventar.use_item(Inventar.choose_item()) and Gamestate.player.pokemon_to_fight.Hp_Current <= Gamestate.player.pokemon_to_fight.Hp_Max/2:  # verbraucht ein item ()
            catch = random.randrange(1, 100)
            if catch < 80:
                Gamestate.player.pokemon_list.append(Gamestate.player.pokemon_to_fight)
                print("Du hast", Gamestate.player.pokemon_to_fight.Name, "gefangen!\nGlückwunsch")
                Gamestate.player.infight = False
                Gamestate.player.pokemon_to_fight = None
        else:
            print("Das Pokemon hat noch zu viel Hp. Du musst es mehr schwächen")

