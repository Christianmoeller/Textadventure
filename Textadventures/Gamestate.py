import json
from PokemonClass import *
from Attack_list import *


class Gamestate:
    def __init__(self, name="", money=0, inventar=None, current_pokemon=None, pokemon_list=None):
        self.name = name
        self.money = money
        self.inventar = inventar
        self.current_pokemon = current_pokemon
        self.infight = False
        self.pokemon_list = pokemon_list
        self.pokemon_to_fight = None

    def save(self, path):
        f = open(path, "w")
        f.write(json.dumps(self, cls=GamestateJsonEncoder))
        f.close()



def load(path):
    f = open(path, "r")
    global player
    player = json.loads(f.read(), cls=GamestateJsonDecoder)
    f.close()


player = Gamestate("", 0, [], "", [])


class GamestateJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Gamestate):
            return vars(obj)
        elif isinstance(obj, PokemonClass):
            return vars(obj)
        elif isinstance(obj, Attack):
            return vars(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class GamestateJsonDecoder(json.JSONDecoder):
    def decode(self, s):
        d = json.JSONDecoder.decode(s)
        return Gamestate(d["name"], d["money"], d["inventar"], d["current_pokemon"], d["pokemon_list"])
