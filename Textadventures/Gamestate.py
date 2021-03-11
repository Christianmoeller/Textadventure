import json
from PokemonClass import PokemonClass, fromJSON
from Attack_list import Attack
from Items import Items, fromJSONItem


class Gamestate:
    def __init__(self, name="", money=0, inventar = {}, current_pokemon=None, pokemon_list=None):
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


player = Gamestate("", 0, {}, "", [])


def load(path):
    f = open(path, "r")
    global player
    player = json.loads(f.read(), cls=GamestateJsonDecoder)
    f.close()


class GamestateJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Gamestate) or isinstance(obj, PokemonClass) or isinstance(obj, Attack) or isinstance(obj, Items):
            return vars(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class GamestateJsonDecoder(json.JSONDecoder):
    def decode(self, s, w=None):
        d = json.JSONDecoder.decode(self, s)
        currentPokemon = fromJSON(d["current_pokemon"])
        pokemonListJSON = d["pokemon_list"]
        pokemonList = []
        for pokemonJSON in pokemonListJSON:
            pokemonList.append(fromJSON(pokemonJSON))
        inventory = {}
        for itemJSON in d["inventar"].keys():
            inventory[fromJSONItem(itemJSON)] = d["inventar"][itemJSON]
        return Gamestate(d["name"], d["money"], inventory, currentPokemon, pokemonList)
