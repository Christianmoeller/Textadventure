import Gamestate
import Items


def catch_pokemon():
    # forall bälle (hyper, super, poke)
    #         haben wir welche? ja -> füge einer neuen liste hinzu
    for key, value in Gamestate.player.inventar.items():
        print(key, value)
    if Gamestate.player.pokemon_to_fight.Hp_Current < Gamestate.player.pokemon_to_fight.Hp_Max / 2 and \
            Gamestate.player.inventar.get(Items.pokeball) > 0:
        if len(Gamestate.player.pokemon_list) == 6:
            print("Tur mir leid aber du kannst nicht mehr wie 6 Pokemon mit dir tragen.")
        else:
            Gamestate.player.pokemon_list.append(Gamestate.player.pokemon_to_fight)
            print("Du hast", Gamestate.player.pokemon_to_fight.Name, "gefangen!\nGlückwunsch")
            Gamestate.player.infight = False
            Gamestate.player.inventar["Pokeball"] = Gamestate.player.inventar["Pokeball"]-1
            Gamestate.player.pokemon_to_fight = None
            return Gamestate.player.infight
    else:
        if Gamestate.player.inventar.get(Items.pokeball) <= 0:
            print("Du hast keinen pokeball übrig")
        elif Gamestate.player.pokemon_to_fight.Hp_Current < Gamestate.player.pokemon_to_fight.Hp_Max / 2:
            print("Du kannst das Pokemon noch nicht fagen solange es mehr als 50% HP hat")
