import Items
from Gamestate import player
from Textadventures import Choose_menu


class Trader:
    def __init__(self, name, ItemList):
        self.name = name
        self.itemList = ItemList


obj_dealer_for_everything = Trader("Tim Hobbs",
                               [Items.pokeball, Items.superball, Items.hyperball, Items.hp_pot, Items.super_hp_pot,
                                Items.hyper_hp_pot])


def dealer_for_everything():
    print(obj_dealer_for_everything.name, "sagt: Willkommen in meinem Shop! Such dir was aus.")
    itemlist = obj_dealer_for_everything.itemList
    for item in itemlist:
        print(item.name)
    itemchoose = input("Was davon willst du kaufen?")
    if itemchoose == "pokeball":
        if player.money >= dealer_for_everything.itemList[0].price:
            player.money = player.money - dealer_for_everything.itemList[0].price
            print("Hier hast du einen Pokeball")
        else:
            print("Tut mir leid aber du hast nicht genug Geld bei dir!")
    elif itemchoose == "hyperball":
        if player.money >= dealer_for_everything.itemList[2].price:
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

# wenn der händler aufgerufen wird  werden erst mal alle items angegeben die zur verfügung stehen
# der user soll aus diesen items mit der davor stehenden zahl ein item auswählen und dann wird erst der kauf abgewickelt
# jedes auflisten braucht eine funktion?

def testShop(sentence, itemlist):
    notDone = True
    print(sentence)

