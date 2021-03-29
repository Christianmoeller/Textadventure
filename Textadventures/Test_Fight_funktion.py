import Gamestate
import random


def pokemon_fight():
    infight = True
    while infight:
        infight = choose_attack()

    return False


def choose_attack():
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
        print("Du hast leider keine attaken mehr frei davon.")
        return
    print(Gamestate.player.current_pokemon.Name, "greift an mit:",
          Gamestate.player.current_pokemon.Attacklist[int(int_answer) - 1].Name)
    chossen_attack = Gamestate.player.current_pokemon.Attacklist[int(int_answer) - 1]
    chossen_attack.Attack_Counter_Current -= 1
    if chossen_attack.Attack_Counter_Current <= 0:
        chossen_attack.Attack_Counter_Current = 0
    dmg_calc(Gamestate.player.current_pokemon.Attacklist[int(int_answer) - 1])
    if Gamestate.player.current_pokemon.Hp_Current <= 0:
        print("Du hast veroren")
        exit()
    if Gamestate.player.pokemon_to_fight.Hp_Current <= 0:
        print("Du hast gewonnen")
        return False


def dmg_calc(my_attack):
    Gamestate.player.pokemon_to_fight.Hp_Current = Gamestate.player.pokemon_to_fight.Hp_Current - my_attack.Dmg
    print(Gamestate.player.current_pokemon.Name, "setzt", my_attack.Name, "ein:", my_attack.Name, "hat", my_attack.Dmg,
          "schaden gemacht.")
    enemy_attack = random.choice(Gamestate.player.pokemon_to_fight.Attacklist)
    Gamestate.player.current_pokemon.Hp_Current = Gamestate.player.current_pokemon.Hp_Current - enemy_attack.Dmg
    print(Gamestate.player.pokemon_to_fight.Name, "setzt", enemy_attack.Name, "ein",
          Gamestate.player.pokemon_to_fight.Name, "hat dir", enemy_attack.Dmg, "Schaden gemacht.")
