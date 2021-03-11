import Items
import Gamestate
from Textadventures import Choose_menu


class Trader:
    def __init__(self, name, ItemList):
        self.name = name
        self.itemList = ItemList


obj_trader_VertaniaCity = Trader("Tim Hobbs",
                                 [Items.pokeball, Items.superball, Items.hyperball, Items.hp_pot, Items.super_hp_pot,
                                  Items.hyper_hp_pot])


# def trader_interaction(trader):
# printe begrüßung, rufe buy_dialogue() auf

# def: buy_dialogue(itemlist):
# print itemliste, rufe nach auswahl buy() auf

# def: buy(item)
# kauflogik (item in gamestate übernehmen, geld abziehen

def trader_VertaniaCity():
    print(obj_trader_VertaniaCity.name, "sagt: Willkommen in meinem Shop!")
    Choose_menu.menu("Für welches der folegenden Items interessierst du dich?",
                     {"Pokeball": buyPokemall, "Superball": buySuperball, "Hyperball": buyHyperball})


# inventar py datei   neu schreiben
#

def buyPokemall():
    if Gamestate.player.money >= obj_trader_VertaniaCity.itemList[0].price:
        Gamestate.player.money = Gamestate.player.money - obj_trader_VertaniaCity.itemList[0].price
        if Gamestate.player.inventar.get("Pokeball") == None:
            Gamestate.player.inventar["Pokeball"] = 1
        else:
            Gamestate.player.inventar["Pokeball"] = Gamestate.player.inventar["Pokeball"]+1
        print(obj_trader_VertaniaCity.name, ": Hier hast du einen Pokeball")
    else:
        print(obj_trader_VertaniaCity.name, ": Tut mir leid aber du hast nicht genug Geld bei dir!")


def buyHyperball():
    if Gamestate.player.money >= obj_trader_VertaniaCity.itemList[2].price:
        Gamestate.player.money = Gamestate.player.money - obj_trader_VertaniaCity.itemList[2].price
        Gamestate.player.inventar.append(obj_trader_VertaniaCity.itemList[2])
        print(obj_trader_VertaniaCity.name, ": Hier hast du einen Hyperball")
    else:
        print(obj_trader_VertaniaCity.name, ": Tut mir leid aber du hast nicht genug Geld bei dir!")


def buySuperball():
    if Gamestate.player.money >= obj_trader_VertaniaCity.itemList[1].price:
        Gamestate.player.money = Gamestate.player.money - obj_trader_VertaniaCity.itemList[1].price
        Gamestate.player.inventar.append(obj_trader_VertaniaCity.itemList[1])
        print(obj_trader_VertaniaCity.name, ": Hier hast du ein Superball")
    else:
        print(obj_trader_VertaniaCity.name, ": Tut mir leid aber du hast nicht genug Geld bei dir!")
