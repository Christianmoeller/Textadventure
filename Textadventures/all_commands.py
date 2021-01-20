import PokemonClass
import random

def _help (gs):
    print(new_Commands.keys())

def travel(gs):
    print("\nDiese Funktion ist noch nicht vorhanden!")
    #erlaubt es dir in andere städte zu reisen da es dort andere shops gibt und amit andere items zum kaufen

def fight(gs):
    gs.infight = True
    pokomon_to_fight = PokemonClass.choose_pokemon()
    print("\nDu betritts die Arena und da steht schon ein Pokemon bereit für dich.")
    print("Es ist ein Wildes:",pokomon_to_fight.Name, "Lvl:", pokomon_to_fight.Level)
    print("Seine Hp", pokomon_to_fight.Hp_Current)
    print("Was wirst du tun?\n")
    while gs.infight:
        print(">>>Kampfmenü<<<")
        answers = {"a": dmg_calculator, "b": pokemon_change, "c":pokemon_stats}
        user_input = input("A:Kämpfen\nB:Pokemon wechseln (nicht verfügbar)\nC:Pokemonstats\nD:Laufen\n>")
        if user_input in answers:
            answers[user_input[0]](gs, pokomon_to_fight)
        elif user_input == "d":
            print("Du bist entkommen!\n")
            gs.infight = False
        else :
            print("Irgendwas musst du ja machen also sag an!")


def current_hp(gs, Pokemon_to_fight):
    print("Dein Pokemon hat noch", gs.current_pokemon.Hp, "Hp.")

def defeat_ep_calculation(pokemon_to_fight):
    return pokemon_to_fight.Ep_at_defeated_level1+(pokemon_to_fight.Ep_at_defeated_level1*0.1)

def pokemon_stats(gs, pokemon_to_fight):
    print(">>>Statsmenü<<<")
    print("Was genau willst du den wissen?")
    answers = input("A: Pokemon Hp?\nB: Pokemon Level?\nC: Benötigte Ep zum Levelup?\nD: Zurück\n>")
    if answers == "a":
        print("Dein", gs.current_pokemon.Name, "Hat noch:", gs.current_pokemon.Hp_Current, "/",gs.current_pokemon.Hp_Max)
    elif answers == "b":
        print("Dein",gs.current_pokemon.Name ,"ist Level:", gs.current_pokemon.Level)
    elif answers == "c":
        print("Benötigte ep zum Levelup:", (gs.current_pokemon.Needed_ep-gs.current_pokemon.Current_ep))
    elif answers == "d":
        return
    else:
        print("Zurück")
        return

def dmg_calculator(gs, pokemon_to_fight):
    sucess = random.randrange(0,100)
    if sucess >= 10:
        pokemon_to_fight.Hp_Current = pokemon_to_fight.Hp_Current-gs.current_pokemon.Dmg
        print("Du hast", pokemon_to_fight.Name,gs.current_pokemon.Dmg,"Schaden gemacht.", pokemon_to_fight.Name,"hat noch:", pokemon_to_fight.Hp_Current, "HP")
        if pokemon_to_fight.Hp_Current <=0:
            print("du hast das Pokemon besiegt.")
            loot(gs, pokemon_to_fight)
            self_level_calcultion(gs, pokemon_to_fight)
            gs.infight = False

    else:
        gs.current_pokemon.Hp_Current = gs.current_pokemon.Hp_Current-pokemon_to_fight.Dmg
        print("Der Gegener hat dir Schaden gemacht. Du hast noch:", gs.current_pokemon.Hp_Current, "HP")
        if gs.current_pokemon.Hp_Current <= 0:
            print("Dein Pokemon wurde besiegt. Spiel beendet!")
            quit()

def run(gs ,pokemon_to_fight):
    print("Du bist entkommen")
    gs.infight = False


def loot(gs, pokemon_to_fight):
    #abhängig von der stärke des pokemons das man besiegt hat soll man mehr geld bekommen
    gs.money = gs.money+pokemon_to_fight.Level

def level_up_stats(gs):
    gs.current_pokemon.Hp_Max = gs.current_pokemon.Hp_Max +25
    gs.current_pokemon.Hp_Current += 10

def self_level_calcultion(gs, pokemon_to_fight):
    get_ep = gs.current_pokemon.Current_ep+pokemon_to_fight.Ep_to_give
    print("Erhaltene Ep:", get_ep)
    gs.current_pokemon.Current_ep = gs.current_pokemon.Current_ep+get_ep
    if gs.current_pokemon.Current_ep >= gs.current_pokemon.Needed_ep:
        while gs.current_pokemon.Current_ep >= gs.current_pokemon.Needed_ep:
            gs.current_pokemon.Level += 1
            print("Dein",gs.current_pokemon.Name,"ist nun level:", gs.current_pokemon.Level)
            level_up_stats(gs)
            print("Seine Max Hp sind um 25 gestiegen.\nSeine Aktuellen Hp sind um 10 erhöt\n")
            gs.current_pokemon.Current_ep = gs.current_pokemon.Current_ep-gs.current_pokemon.Needed_ep
            gs.current_pokemon.Needed_ep = gs.current_pokemon.Needed_ep + 150


def shop(gs):
    #eine Liste an items die einen wert haben für den man ihn kaufen kann   zb pokepälle  oder heiltränke für pokemon
    print("\nDiese Funktion ist noch nicht vorhanden!")

def inventar(gs):
    #eine liste an allen items die der spieler mit sich trägt zb tränke oder pokebälle
    print("\nDiese Funktion ist noch nicht vorhanden!")

def stats(gs):
    print("Was genau möchten sie Wissen?")
    answer = input("A: Pokemon HP?\nB: Pokemon Level?\nC: Benötigte Ep zum Levelup?\nD: Zurück\n>")
    if answer == "a":
        print("Dein", gs.current_pokemon.Name, "Hat noch:", gs.current_pokemon.Hp_Current, "/",gs.current_pokemon.Hp_Max)
    elif answer == "b":
        print("Dein",gs.current_pokemon.Name ,"ist Level:", gs.current_pokemon.Level)
    elif answer == "c":
        print("Benötigte ep zum Levelup:", (gs.current_pokemon.Needed_ep-gs.current_pokemon.Current_ep))
    elif answer == "d":
        return
    else:
        print("Zurück")
        return



def pokemon_change(gs, pokemon_to_fight):
    # man kann sein pokemon tauschen sowohl infight als auch ausserhalb des kampfes
    print("\nDiese Funktion ist noch nicht vorhanden!")

def save(gs):
    #speichert das spiel bzw das gs die pokemon und so weiter    fragt mit welchem namen es gespeichert werden soll
    print("\nDiese Funktion ist noch nicht vorhanden!")

def load(gs):
    #läd das spiel mit dem passenden  namen   listet alle spielstände auf
    print("\nDiese Funktion ist noch nicht vorhanden!")

def money(gs):
    print("Aktueller Kontostand:", gs.money, "€\n")

def pokecenter(gs):
    heal_notheal = input("Schwester Joy: \"Sollen wir uns um Ihr Pokemon kümmern?\"\n>")
    if heal_notheal == "ja":
        gs.current_pokemon.Hp_Current = gs.current_pokemon.Hp_Max
        print("Musik...")
        print("Schwester Joy:\"Deinem Pokemon geht es wieder gut. Beehren sie uns bald wieder!\"")
    elif heal_notheal == "nein":
        print("Schester Joy:\"Okay. Beehren sie uns bald wieder!\"")
    else:
        return


new_Commands = {
    'reisen':travel,
    'kämpfen':fight,
    'einkaufen':shop,
    'help':_help,
    'inventar':inventar,
    'stats':stats,
    'wechseln':pokemon_change,
    'save':save,
    'load':load,
    'geld':money,
    'pokecenter':pokecenter
}