import PokemonClass
import random
import catch_pokemon
import pokemon_change


def _help(gs):
    print(new_Commands.keys())


def travel(gs):
    print("\nDiese Funktion ist noch nicht vorhanden!")
    # erlaubt es dir in andere städte zu reisen da es dort andere shops gibt und amit andere items zum kaufen


def fight(gs):
    clear_screen()
    gs.infight = True
    pokomon_to_fight = PokemonClass.choose_pokemon()
    print("\nDu betritts die Arena und da steht schon ein Pokemon bereit für dich.")
    print("Es ist ein Wildes:", pokomon_to_fight.Name, "Lvl:", pokomon_to_fight.Level)
    print("Seine Hp", pokomon_to_fight.Hp_Current)
    print("Was wirst du tun?\n")
    while gs.infight:
        print(">>>Kampfmenü<<<\n")
        user_input = input("A:Kämpfen\nB:Pokemon wechseln\nC:Pokemonstats\nD:Laufen\nE:Pokemon Fangen(noch Instand)\n>")
        if user_input.lower() == "a":
            dmg_calculator(gs, pokomon_to_fight, attackenmenu(gs))
        elif user_input.lower() == "b":
            pokemon_change.pokemon_change(gs)
        elif user_input.lower() == "c":
            stats(gs)
        elif user_input.lower() == "d":
            run(gs)
        elif user_input.lower() == "e":
            catch_pokemon.catch_pokemon(gs, pokomon_to_fight)
        else:
            print("Irgendwas musst du ja machen also sag an!")


def current_hp(gs, Pokemon_to_fight):
    print("Dein Pokemon hat noch", gs.current_pokemon.Hp, "Hp.")


def attackenmenu(gs):
    print("Diese Attacken besitzt", gs.current_pokemon.Name)
    zahl = 1
    for Attak in gs.current_pokemon.Attacklist:
        print(zahl, Attak.Name, "Schaden:", Attak.Dmg, "Noch:", Attak.Attack_Counter_Current, "übrig.")
        zahl += 1
    int_answer = 0
    while not (int_answer > 0 and int_answer <= len(gs.current_pokemon.Attacklist)):
        answer = input("Bitte wähle eine Attacke zwischen 1 und {}\n".format(len(gs.current_pokemon.Attacklist)))
        if answer.isnumeric():
            int_answer = int(answer)
    if gs.current_pokemon.Attacklist[int_answer - 1].Attack_Counter_Current == 0:
        print("Du hast leider keine attaken mehr frei davon")
        return
    print(gs.current_pokemon.Name, "greift an mit:", gs.current_pokemon.Attacklist[int(int_answer) - 1].Name)
    chossen_attack = gs.current_pokemon.Attacklist[int(int_answer) - 1]
    chossen_attack.Attack_Counter_Current -= 1
    if chossen_attack.Attack_Counter_Current <= 0:
        chossen_attack.Attack_Counter_Current = 0
    return chossen_attack


def defeat_ep_calculation(pokemon_to_fight):
    return pokemon_to_fight.Ep_at_defeated_level1 + (pokemon_to_fight.Ep_at_defeated_level1 * 0.1)


def dmg_calculator(gs, pokemon_to_fight, current_pokemon_attack):
    if current_pokemon_attack == None:
        return
    sucess = random.randrange(0, 100)
    if sucess >= 10:
        print("Du setzt:", current_pokemon_attack.Name, "ein")
        pokemon_to_fight.Hp_Current = pokemon_to_fight.Hp_Current - current_pokemon_attack.Dmg
        print("Du hast", pokemon_to_fight.Name, current_pokemon_attack.Dmg, "Schaden gemacht.", pokemon_to_fight.Name,
              "hat noch:", pokemon_to_fight.Hp_Current, "HP")
        if pokemon_to_fight.Hp_Current <= 0:
            print("du hast das Pokemon besiegt.")
            loot(gs, pokemon_to_fight)
            self_level_calcultion(gs, pokemon_to_fight)
            gs.infight = False

    else:
        attack_choise = random.choice(pokemon_to_fight.Attacklist)
        gs.current_pokemon.Hp_Current = gs.current_pokemon.Hp_Current - attack_choise.Dmg
        print(pokemon_to_fight.Name, "setzt", attack_choise.Name, "ein.")
        print(pokemon_to_fight.Name, "hat dir", attack_choise.Dmg, "Schaden gemacht. Du hast noch:",
              gs.current_pokemon.Hp_Current, "HP")
        if gs.current_pokemon.Hp_Current <= 0:
            print("Dein Pokemon wurde besiegt. Spiel beendet!")
            quit()


def run(gs):
    print("Du bist entkommen")
    gs.infight = False


def loot(gs, pokemon_to_fight):
    # abhängig von der stärke des pokemons das man besiegt hat soll man mehr geld bekommen
    gs.money = gs.money + pokemon_to_fight.Level + 10


def level_up_stats(gs):
    gs.current_pokemon.Hp_Max = gs.current_pokemon.Hp_Max + 25
    gs.current_pokemon.Hp_Current += 10
    gs.current_pokemon.Dmg += 2
    print("Die Max Hp von:", gs.current_pokemon.Name, "wurde um 20 erhöt.")
    print("Der Schaden von:", gs.current_pokemon.Name, "wurde um 2 erhör.\n")


def self_level_calcultion(gs, pokemon_to_fight):
    get_ep = gs.current_pokemon.Current_ep + pokemon_to_fight.Ep_to_give
    print("Erhaltene Ep:", get_ep, "\n")
    gs.current_pokemon.Current_ep = gs.current_pokemon.Current_ep + get_ep
    if gs.current_pokemon.Current_ep >= gs.current_pokemon.Needed_ep:
        while gs.current_pokemon.Current_ep >= gs.current_pokemon.Needed_ep:
            gs.current_pokemon.Level += 1
            print("Dein", gs.current_pokemon.Name, "ist nun level:", gs.current_pokemon.Level)
            level_up_stats(gs)
            print("Seine Max Hp sind um 25 gestiegen.\nSeine Aktuellen Hp sind um 10 erhöt\n")
            gs.current_pokemon.Current_ep = gs.current_pokemon.Current_ep - gs.current_pokemon.Needed_ep
            gs.current_pokemon.Needed_ep = gs.current_pokemon.Needed_ep + 150


def shop(gs):
    # eine Liste an items die einen wert haben für den man ihn kaufen kann   zb pokepälle  oder heiltränke für pokemon
    print("\nDiese Funktion ist noch nicht vorhanden!")


def inventar(gs):
    # eine liste an allen items die der spieler mit sich trägt zb tränke oder pokebälle
    print("\nDiese Funktion ist noch nicht vorhanden!")


def list_all_pokemon(gs):
    print("Die Pokemon die du dabei hast sind:")
    for pokemon in gs.pokemon_list:
        print(pokemon.Name, "\n")


def stats(gs):
    print("Was genau möchten sie Wissen?")
    answer = input("A: Pokemon HP?\nB: Pokemon Level?\nC: Benötigte Ep zum Levelup?\nD: Zurück\n>")
    if answer.lower() == "a":
        print("Dein", gs.current_pokemon.Name, "Hat noch:", gs.current_pokemon.Hp_Current, "/",
              gs.current_pokemon.Hp_Max)
    elif answer.lower() == "b":
        print("Dein", gs.current_pokemon.Name, "ist Level:", gs.current_pokemon.Level)
    elif answer.lower() == "c":
        print("Benötigte ep zum Levelup:", (gs.current_pokemon.Needed_ep - gs.current_pokemon.Current_ep))
    elif answer.lower() == "d":
        print("Dein Aktuelles Pokemon ist:", gs.current_pokemon.Name)
        list_all_pokemon(gs)
    else:
        print("Zurück")
        return


def save(gs):
    # speichert das spiel bzw das gs die pokemon und so weiter    fragt mit welchem namen es gespeichert werden soll
    print("\nDiese Funktion ist noch nicht vorhanden!")


def load(gs):
    # läd das spiel mit dem passenden  namen   listet alle spielstände auf
    print("\nDiese Funktion ist noch nicht vorhanden!")


def money(gs):
    print("Aktueller Kontostand:", gs.money, "€\n")


def pokecenter(gs):
    heal_notheal = input("Schwester Joy: \"Sollen wir uns um Ihr Pokemon kümmern?\"\n>")
    if heal_notheal == "ja":
        gs.current_pokemon.Hp_Current = gs.current_pokemon.Hp_Max
        for Attack in gs.current_pokemon.Attacklist:
            Attack.Attack_Counter_Current = Attack.Attack_Counter_Max
        print("Musik...")
        print("Schwester Joy:\"Deinem Pokemon geht es wieder gut. Beehren sie uns bald wieder!\"")
    elif heal_notheal == "nein":
        print("Schester Joy:\"Okay. Beehren sie uns bald wieder!\"\n")
    else:
        return


def clear_screen():
    condition = 0
    while condition < 20:
        print()
        condition += 1


new_Commands = {
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
