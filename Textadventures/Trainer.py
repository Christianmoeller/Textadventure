from PokemonClass import *
import random


class World_Trainer:
    def __init__(self,name, pokemon_list, money_value):
        self.name = name
        self.pokemon_list = pokemon_list
        self.money_value = money_value


def chosse_trainer():
    # wählt einen trainer aus
    trainer_list = []
    Theresa_Koellenberger = World_Trainer("Theresa_Koellenberger", [choose_pokemon(), choose_pokemon(), choose_pokemon()], 350)
    Christian_Wild = World_Trainer("Christian_Wild", [choose_pokemon(), choose_pokemon(), choose_pokemon()], 350)
    Jonathan_Dietrich = World_Trainer("Jonathan_Dietrich", [choose_pokemon(), choose_pokemon(), choose_pokemon()], 350)
    trainer_list.append(Theresa_Koellenberger)
    trainer_list.append(Christian_Wild)
    trainer_list.append(Jonathan_Dietrich)
    return random.choice(trainer_list)
