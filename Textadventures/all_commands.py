
import random

from Gamestate import player

def attackenmenu():
    print("Diese Attacken besitzt", player.current_pokemon.Name)
    zahl = 1
    for Attak in player.current_pokemon.Attacklist:
        print(zahl, Attak.Name, "Schaden:", Attak.Dmg, "Noch:", Attak.Attack_Counter_Current, "übrig.")
        zahl += 1
    int_answer = 0
    while not (int_answer > 0 and int_answer <= len(player.current_pokemon.Attacklist)):
        answer = input("Bitte wähle eine Attacke zwischen 1 und {}\n".format(len(player.current_pokemon.Attacklist)))
        if answer.isnumeric():
            int_answer = int(answer)
    if player.current_pokemon.Attacklist[int_answer - 1].Attack_Counter_Current == 0:
        print("Du hast leider keine attaken mehr frei davon")
        return
    print(player.current_pokemon.Name, "greift an mit:", player.current_pokemon.Attacklist[int(int_answer) - 1].Name)
    chossen_attack = player.current_pokemon.Attacklist[int(int_answer) - 1]
    chossen_attack.Attack_Counter_Current -= 1
    if chossen_attack.Attack_Counter_Current <= 0:
        chossen_attack.Attack_Counter_Current = 0
    return chossen_attack


def defeat_ep_calculation(pokemon_to_fight):
    return pokemon_to_fight.Ep_at_defeated_level1 + (pokemon_to_fight.Ep_at_defeated_level1 * 0.1)


def dmg_calculator(pokemon_to_fight, current_pokemon_attack):
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
            loot(pokemon_to_fight)
            self_level_calcultion(pokemon_to_fight)
            player.infight = False

    else:
        attack_choise = random.choice(pokemon_to_fight.Attacklist)
        player.current_pokemon.Hp_Current = player.current_pokemon.Hp_Current - attack_choise.Dmg
        print(pokemon_to_fight.Name, "setzt", attack_choise.Name, "ein.")
        print(pokemon_to_fight.Name, "hat dir", attack_choise.Dmg, "Schaden gemacht. Du hast noch:",
              player.current_pokemon.Hp_Current, "HP")
        if player.current_pokemon.Hp_Current <= 0:
            print("Dein Pokemon wurde besiegt. Spiel beendet!")
            quit()


def run():
    print("Du bist entkommen")
    player.infight = False


def loot(pokemon_to_fight):
    # abhängig von der stärke des pokemons das man besiegt hat soll man mehr geld bekommen
    player.money = player.money + pokemon_to_fight.Level + 10


def level_up_stats():
    player.current_pokemon.Hp_Max = player.current_pokemon.Hp_Max + 25
    player.current_pokemon.Hp_Current += 10
    player.current_pokemon.Dmg += 2
    print("Die Max Hp von:", player.current_pokemon.Name, "wurde um 20 erhöt.")
    print("Der Schaden von:", player.current_pokemon.Name, "wurde um 2 erhör.\n")


def self_level_calcultion(pokemon_to_fight):
    get_ep = player.current_pokemon.Current_ep + pokemon_to_fight.Ep_to_give
    print("Erhaltene Ep:", get_ep, "\n")
    player.current_pokemon.Current_ep = player.current_pokemon.Current_ep + get_ep
    if player.current_pokemon.Current_ep >= player.current_pokemon.Needed_ep:
        while player.current_pokemon.Current_ep >= player.current_pokemon.Needed_ep:
            player.current_pokemon.Level += 1
            print("Dein", player.current_pokemon.Name, "ist nun level:", player.current_pokemon.Level)
            level_up_stats()
            print("Seine Max Hp sind um 25 gestiegen.\nSeine Aktuellen Hp sind um 10 erhöt\n")
            player.current_pokemon.Current_ep = player.current_pokemon.Current_ep - player.current_pokemon.Needed_ep
            player.current_pokemon.Needed_ep = player.current_pokemon.Needed_ep + 150


def list_all_pokemon():
    print("Die Pokemon die du dabei hast sind:")
    for pokemon in player.pokemon_list:
        print(pokemon.Name, "\n")

