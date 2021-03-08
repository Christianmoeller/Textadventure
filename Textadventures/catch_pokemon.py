from Gamestate import player


def catch_pokemon():

    if player.pokemon_to_fight.Hp_Current < player.pokemon_to_fight.Hp_Max/2:
        if len(player.pokemon_list) == 6:
            print("Tur mir leid aber du kannst nicht mehr wie 6 Pokemon mit dir tragen.")
        else:
            player.pokemon_list.append(player.pokemon_to_fight)
            print("Du hast", player.pokemon_to_fight.Name, "gefangen!\nGlückwunsch")
            player.infight = False
            player.pokemon_to_fight = None
            return player.infight
    else:
        print("Du kannst das Pokemon noch nicht fagen solange es mehr als 50% HP hat")

