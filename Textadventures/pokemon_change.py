def pokemon_change(gs):
    zahl = 1
    print("Das sind Deine Pokemon")
    for pokemon in gs.pokemon_list:
        print(zahl, pokemon.Name, "lvl:",pokemon.Level, "Hp", pokemon.Hp_Current, pokemon.Hp_Max)
        zahl += 1
    int_answer = 0
    while not (int_answer >0 and int_answer <= len(gs.pokemon_list)):
        answer = input("Bitte wähle einses der Pokemon zwischen 1 und {}\n".format(len(gs.pokemon_list)))
        if answer.isnumeric():
            int_answer = int(answer)
    gs.current_pokemon = gs.pokemon_list[int(answer)-1]
    print(gs.current_pokemon.Name, "ist jetzt dein neues Frontpokemon")