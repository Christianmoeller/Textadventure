from Gamestate import player
class Citys:
    def __init__(self, name, pokemon_variation, trader):
        self.name = name
        self.pokemon_variation = pokemon_variation
        self.trader = trader

    def trade(self, gs):
        pass


class Items:
    def __init__(self, name, price):
        self.name = name
        self.price = price


pokeball = Items("Pokeball", 10)
superball = Items("Super Ball", 15)
hyperball = Items("Hyper Ball", 20)
hp_pot = Items("Heiltrank", 25)
super_hp_pot = Items("Super Heiltrank", 30)
hyper_hp_pot = Items("Hyper Heiltrank", 40)


class Trader:
    def __init__(self, name, Items):
        self.name = name
        self.items = Items

def print_all_trader_inventory(trader):
    liste = []
    for i in trader.items:
        liste.append(i.name)
    print(liste)



def pokeball_trader():
    print(pokeball_seller.name, "sagt: Willkommen in meinem Shop\nIch habe im Angebot:")
    print_all_trader_inventory(pokeball_seller)
    itemchoose = input("Was davon willst du kaufen?")
    if itemchoose == "pokeball":
        if player.money >=pokeball_seller.items[0].price:
            player.money = player.money - pokeball_seller.items[0].price
            print("Hier hast du einen Pokeball")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    elif itemchoose == "hyperball":
        if player.money >=pokeball_seller.items[2].price:
            player.money = player.money - pokeball_seller.items[2].price
            print("Hier hast du einen Hyperball")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    elif itemchoose == "superball":
        if player.money >= pokeball_seller.items[1].price:
            player.money = player.money - pokeball_seller.items[1].price
            print("Hier hast du ein Superball")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    else:
        print("Okay Ciao")

def potion_trader():
    print(pot_seller.name, "sagt: Willkommen in meinem Shop\nIch habe im Angebot:")
    print_all_trader_inventory(pot_seller)
    itemchoose = input("Was davon willst du kaufen?")
    if itemchoose == "trank":
        if player.money >=pot_seller.items[0].price:
            player.money = player.money - pot_seller.items[0].price
            print("Hier hast du einen Trank")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    elif itemchoose == "hypertrank":
        if player.money >=pot_seller.items[2].price:
            player.money = player.money - pot_seller.items[2].price
            print("Hier hast du einen Hypertank")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    elif itemchoose == "supertrank":
        if player.money >= pot_seller.items[1].price:
            player.money = player.money - pot_seller.items[1].price
            print("Hier hast du ein Supertrank")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    else:
        print("Okay Ciao")


pokeball_seller = Trader("Pokeball Verkäufer", [pokeball, superball, hyperball])
pot_seller = Trader("Tränke Verkäufer", [hp_pot, super_hp_pot, hyper_hp_pot])
