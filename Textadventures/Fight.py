from random import random

import all_commands as ac
import Textadventures as Ts

def fight(gs):
    ac.clear_screen()
    gs.infight = True
    pokomon_to_fight = Ts.PokemonClass.choose_pokemon()
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
            Ts.pokemon_change.pokemon_change(gs)
        elif user_input.lower() == "c":
            Ts.stats(gs)
        elif user_input.lower() == "d":
            run(gs)
        elif user_input.lower() == "e":
            Ts.catch_pokemon.catch_pokemon(gs, pokomon_to_fight)
        else:
            print("Irgendwas musst du ja machen also sag an!")

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
