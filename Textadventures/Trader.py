import Items
import Buy_Item
from Textadventures import Choose_menu


class Trader:
    def __init__(self, name, ItemList):
        self.name = name
        self.itemList = ItemList


obj_trader_VertaniaCity = Trader("Tim Hobbs",
                                 [Items.pokeball, Items.superball, Items.hyperball, Items.hp_pot, Items.super_hp_pot,
                                  Items.hyper_hp_pot])



def trader_VertaniaCity():
    print(obj_trader_VertaniaCity.name, "sagt: Willkommen in meinem Shop!")
    Choose_menu.menu("Für welches der folegenden Items interessierst du dich?",
                     {"Pokeball": Buy_Item.buyPokeball, "Superball": Buy_Item.buySuperball, "Hyperball": Buy_Item.buyHyperball})

