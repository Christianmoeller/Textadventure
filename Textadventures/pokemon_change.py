import Gamestate


def pokemon_change():
    zahl = 1
    print("Das sind Deine Pokemon")
    for pokemon in Gamestate.player.pokemon_list:
        print(zahl, pokemon.Name, "lvl:", pokemon.Level, "Hp", pokemon.Hp_Current, pokemon.Hp_Max)
        zahl += 1
    int_answer = 0
    while not (int_answer > 0 and int_answer <= len(Gamestate.player.pokemon_list)):
        answer = input("Bitte wähle einses der Pokemon zwischen 1 und {}\n".format(len(Gamestate.player.pokemon_list)))
        if answer.isnumeric():
            int_answer = int(answer)
    Gamestate.player.current_pokemon = Gamestate.player.pokemon_list[int(answer) - 1]
    print(Gamestate.player.current_pokemon.Name, "ist jetzt dein neues Frontpokemon")
