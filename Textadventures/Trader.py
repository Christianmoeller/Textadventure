import Items
from Gamestate import player

class Trader:
    def __init__(self, name, ItemList):
        self.name = name
        self.itemList = ItemList


dealer_for_everything = Trader("Verkäufer für Allgemeines", [Items.pokeball, Items.superball, Items.hyperball, Items.hp_pot, Items.super_hp_pot, Items.hyper_hp_pot])


def pokeball_trader():
    print(dealer_for_everything.name, "sagt: Willkommen in meinem Shop\nIch habe im Angebot:")
    itemchoose = input("Was davon willst du kaufen?")
    if itemchoose == "pokeball":
        if player.money >=dealer_for_everything.itemList[0].price:
            player.money = player.money - dealer_for_everything.itemList[0].price
            print("Hier hast du einen Pokeball")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    elif itemchoose == "hyperball":
        if player.money >=dealer_for_everything.itemList[2].price:
            player.money = player.money - dealer_for_everything.itemList[2].price
            print("Hier hast du einen Hyperball")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    elif itemchoose == "superball":
        if player.money >= dealer_for_everything.itemList[1].price:
            player.money = player.money - dealer_for_everything.itemList[1].price
            print("Hier hast du ein Superball")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    else:
        print("Okay Ciao")