def catch_pokemon(gs, pokemon_to_fight):
    if len(gs.pokemon_list) == 6:
        print("Tur mir leid aber du kannst nicht mehr wie 6 Pokemon mit dir tragen.")
    else:
        gs.pokemon_list.append(pokemon_to_fight)
        print("Du hast", pokemon_to_fight.Name, "gefangen!\nGlückwunsch")
        return
