import PokemonClass
import random

def _help (gs):
    print(new_Commands.keys())

def travel(gs):
    #erlaubt es dir in andere städte zu reisen da es dort andere shops gibt und amit andere items zum kaufen
    pass

def fight(gs):
    gs.infight = True
    pokomon_to_fight = PokemonClass.choose_pokemon()

    print("Du kämpfst gegen:",pokomon_to_fight.Name)
    print("Was wirst du tun?")
    while gs.infight:
        answers = {"a": dmg_calculator, "b": pokemon_change, "c": current_hp}
        user_input = input("A:Kämpfen\nB:Pokemon wechseln\nC:Pokemonstats\nD:Laufen\n")
        if user_input in answers:
            answers[user_input[0]](gs, pokomon_to_fight)
        elif user_input == "d":
            print("Du bist entkommen!")
            gs.infight = False
        else :
            print("Irgendwas musst du ja machen also sag an!")


def current_hp(gs, Pokemon_to_fight):
    print("Dein Pokemon hat noch", gs.current_pokemon.Hp, "Hp.")


def dmg_calculator(gs, pokemon_to_fight):
    sucess = random.randrange(0,100)
    if sucess >= 10:
        pokemon_to_fight.Hp = pokemon_to_fight.Hp-gs.current_pokemon.Dmg
        print("Du hast dem Gegner Schaden gemacht. Es hat noch:", pokemon_to_fight.Hp, "HP")
        if pokemon_to_fight.Hp <=0:
            loot(gs, pokemon_to_fight)
            print("du hast das Pokemon besiegt.")
            gs.infight = False

    else:
        gs.current_pokemon.Hp = gs.current_pokemon.Hp-pokemon_to_fight.Dmg
        print("Der Gegener hat dir Schaden gemacht. Du hast noch:", gs.current_pokemon.Hp, "HP")
        if gs.current_pokemon.Hp <= 0:
            print("Dein Pokemon wurde besiegt. Spiel beendet!")
            quit()

def run(gs ,pokemon_to_fight):
    print("Du bist entkommen")
    gs.infight = False


def loot(gs, pokemon_to_fight):
    #abhängig von der stärke des pokemons das man besiegt hat soll man mehr geld bekommen
    gs.money += 1

def shop(gs):
    #eine Liste an items die einen wert haben für den man ihn kaufen kann   zb pokepälle  oder heiltränke für pokemon

    pass

def inventar(gs):
    #eine liste an allen items die der spieler mit sich trägt zb tränke oder pokebälle
    pass

def stats(gs):
    print("Name:",gs.name,"\nGeld:",gs.money,"\nInventar:",gs. inventar,"\nDein Pokemon:", gs.current_pokemon.Name)

def pokemon_change(gs, pokemon_to_fight):
    # man kann sein pokemon tauschen sowohl infight als auch ausserhalb des kampfes
    pass

def save(gs):
    #speichert das spiel bzw das gs die pokemon und so weiter    fragt mit welchem namen es gespeichert werden soll
    pass

def load(gs):
    #läd das spiel mit dem passenden  namen   listet alle spielstände auf
    pass

new_Commands = {
    'reisen':travel,
    'kämpfen':fight,
    'einkaufen':shop,
    'help':_help,
    'inventar':inventar,
    'stats':stats,
    'wechseln':pokemon_change,
    'save':save,
    'load':load
}