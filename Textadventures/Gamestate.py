class Gamestate:
    def __init__(self, name, money, inventar, current_pokemon):
        self.name = name
        self.money = money
        self.inventar = inventar
        self.start_pokeomn = current_pokemon
        self.infight = False