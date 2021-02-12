def catch_pokemon(gs, pokemon_to_fight):

    if pokemon_to_fight.Hp_Current < pokemon_to_fight.Hp_Max/2:
        if len(gs.pokemon_list) == 6:
            print("Tur mir leid aber du kannst nicht mehr wie 6 Pokemon mit dir tragen.")
        else:
            gs.pokemon_list.append(pokemon_to_fight)
            print("Du hast", pokemon_to_fight.Name, "gefangen!\nGlückwunsch")
            gs.infight = False
            return gs.infight
    else:
        print("Du kannst das Pokemon noch nicht fagen solange es mehr als 50% HP hat")

