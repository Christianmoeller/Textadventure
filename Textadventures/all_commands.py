import random
import Gamestate
import Choose_menu
import Mainmenu




def attackenmenu():
    print("Diese Attacken besitzt", Gamestate.player.current_pokemon.Name)
    zahl = 1
    for Attack in Gamestate.player.current_pokemon.Attacklist:
        print(zahl, Attack.Name, "Schaden:", Attack.Dmg, "Noch:", Attack.Attack_Counter_Current, "übrig.")
        zahl += 1
    int_answer = 0
    while not (int_answer > 0 and int_answer <= len(Gamestate.player.current_pokemon.Attacklist)):
        answer = input(
            "Bitte wähle eine Attacke zwischen 1 und {}\n".format(len(Gamestate.player.current_pokemon.Attacklist)))
        if answer.isnumeric():
            int_answer = int(answer)
    if Gamestate.player.current_pokemon.Attacklist[int_answer - 1].Attack_Counter_Current == 0:
        print("Du hast leider keine attaken mehr frei davon")
        return
    print(Gamestate.player.current_pokemon.Name, "greift an mit:",
          Gamestate.player.current_pokemon.Attacklist[int(int_answer) - 1].Name)
    chossen_attack = Gamestate.player.current_pokemon.Attacklist[int(int_answer) - 1]
    chossen_attack.Attack_Counter_Current -= 1
    if chossen_attack.Attack_Counter_Current <= 0:
        chossen_attack.Attack_Counter_Current = 0
    dmg_calculator(chossen_attack)


def defeat_ep_calculation(pokemon_to_fight):
    return pokemon_to_fight.Ep_at_defeated_level1 + (pokemon_to_fight.Ep_at_defeated_level1 * 0.1)


def dmg_calculator(current_pokemon_attack):
    if current_pokemon_attack == None:
        return
    sucess = random.randrange(0, 100)
    if sucess >= 10:
        print("Du setzt:", current_pokemon_attack.Name, "ein")
        Gamestate.player.pokemon_to_fight.Hp_Current = Gamestate.player.pokemon_to_fight.Hp_Current - current_pokemon_attack.Dmg
        print("Du hast", Gamestate.player.pokemon_to_fight.Name, current_pokemon_attack.Dmg, "Schaden gemacht.",
              Gamestate.player.pokemon_to_fight.Name,
              "hat noch:", Gamestate.player.pokemon_to_fight.Hp_Current, "HP")
        if Gamestate.player.pokemon_to_fight.Hp_Current <= 0:
            print("du hast das Pokemon besiegt.")
            loot(Gamestate.player.pokemon_to_fight)
            self_level_calcultion(Gamestate.player.pokemon_to_fight)
            Gamestate.player.infight = False
            Gamestate.player.pokemon_to_fight = None

    else:
        attack_choise = random.choice(Gamestate.player.pokemon_to_fight.Attacklist)
        Gamestate.player.current_pokemon.Hp_Current = Gamestate.player.current_pokemon.Hp_Current - attack_choise.Dmg
        print(Gamestate.player.pokemon_to_fight.Name, "setzt", attack_choise.Name, "ein.")
        print(Gamestate.player.pokemon_to_fight.Name, "hat dir", attack_choise.Dmg, "Schaden gemacht. Du hast noch:",
              Gamestate.player.current_pokemon.Hp_Current, "HP")
        if Gamestate.player.current_pokemon.Hp_Current <= 0:
            print("Dein Pokemon wurde besiegt. Spiel beendet!")
            quit()


def run():
    print("Du bist entkommen")
    Gamestate.player.infight = False


def loot(pokemon_to_fight):
    # abhängig von der stärke des pokemons das man besiegt hat soll man mehr geld bekommen
    Gamestate.player.money = Gamestate.player.money + pokemon_to_fight.Level + 10


def level_up_stats():
    Gamestate.player.current_pokemon.Hp_Max = Gamestate.player.current_pokemon.Hp_Max + 25
    Gamestate.player.current_pokemon.Hp_Current += 10
    Gamestate.player.current_pokemon.Dmg += 2
    print("Die Max Hp von:", Gamestate.player.current_pokemon.Name, "wurde um 20 erhöt.")
    print("Der Schaden von:", Gamestate.player.current_pokemon.Name, "wurde um 2 erhör.\n")


def self_level_calcultion(pokemon_to_fight):
    get_ep = Gamestate.player.current_pokemon.Current_ep + pokemon_to_fight.Ep_to_give
    print("Erhaltene Ep:", get_ep, "\n")
    Gamestate.player.current_pokemon.Current_ep = Gamestate.player.current_pokemon.Current_ep + get_ep
    if Gamestate.player.current_pokemon.Current_ep >= Gamestate.player.current_pokemon.Needed_ep:
        while Gamestate.player.current_pokemon.Current_ep >= Gamestate.player.current_pokemon.Needed_ep:
            Gamestate.player.current_pokemon.Level += 1
            print("Dein", Gamestate.player.current_pokemon.Name, "ist nun level:",
                  Gamestate.player.current_pokemon.Level)
            level_up_stats()
            print("Seine Max Hp sind um 25 gestiegen.\nSeine Aktuellen Hp sind um 10 erhöt\n")
            Gamestate.player.current_pokemon.Current_ep = Gamestate.player.current_pokemon.Current_ep - Gamestate.player.current_pokemon.Needed_ep
            Gamestate.player.current_pokemon.Needed_ep = Gamestate.player.current_pokemon.Needed_ep + 150


def list_all_pokemon():
    print("Die Pokemon die du dabei hast sind:")
    for pokemon in Gamestate.player.pokemon_list:
        print(pokemon.Name, "Level:", pokemon.Level, "Hp:", pokemon.Hp_Current, "/", pokemon.Hp_Max)
    print("\n")


def current_pokemon_stats():
    print(Gamestate.player.current_pokemon.Name, ": Meine Hp liegen bei", Gamestate.player.current_pokemon.Hp_Current,
          "von",
          Gamestate.player.current_pokemon.Hp_Max
          , "\nIch habe", Gamestate.player.current_pokemon.Current_ep, "EP und brauche noch",
          Gamestate.player.current_pokemon.Needed_ep, "EP für level", Gamestate.player.current_pokemon.Level + 1)


def start_load():
    userinput = input("Wills du Starten oder Spielstand landen?")
    if userinput == "start":
        return
    elif userinput == "laden":
        Mainmenu.load_game()
        Choose_menu.menu("Was willst du tun?\n",
             {"Kämpfen": Mainmenu.fight, "Pokecenter": Mainmenu.pokecenter, "Pokemon": Mainmenu.pokemon_stats, "Pokemon wechseln": Mainmenu.pokemon_change,
              "Inventar": Mainmenu.inventar,
              "Geldbeutel": Mainmenu.money, "Einkaufen": Mainmenu.shop, "save": Mainmenu.save, "load": Mainmenu.load_game})
