import Gamestate
import Trader
import Items


def buyPokeball():
    if Gamestate.player.money >= Trader.obj_trader_VertaniaCity.itemList[0].price:  # wenn geld ausreicht
        Gamestate.player.money = Gamestate.player.money - Trader.obj_trader_VertaniaCity.itemList[
            0].price  # Geld abgezogen
        if Gamestate.player.inventar == {}:
            Gamestate.player.inventar[Items.pokeball] = 1
        else:
            Gamestate.player.inventar[Items.pokeball] = Gamestate.player.inventar[Items.pokeball] + 1
    else:
        print(Trader.obj_trader_VertaniaCity.name, "Tut mir leid aber du hast nicht genug Geld bei dir!")


def buyHyperball():
    if Gamestate.player.money >= Trader.obj_trader_VertaniaCity.itemList[2].price:  # wenn geld ausreicht
        Gamestate.player.money = Gamestate.player.money - Trader.obj_trader_VertaniaCity.itemList[
            2].price  # Geld abgezogen
        if Items.hyperball not in Gamestate.player.inventar:
            Gamestate.player.inventar[Items.hyperball] = 1
        else:
            Gamestate.player.inventar[Items.hyperball] = Gamestate.player.inventar[Items.hyperball] + 1
    else:
        print(Trader.obj_trader_VertaniaCity.name, "Tut mir leid aber du hast nicht genug Geld bei dir!")


def buySuperball():
    if Gamestate.player.money >= Trader.obj_trader_VertaniaCity.itemList[1].price:  # wenn geld ausreicht
        Gamestate.player.money = Gamestate.player.money - Trader.obj_trader_VertaniaCity.itemList[
            1].price  # Geld abgezogen
        if Items.superball not in Gamestate.player.inventar:
            Gamestate.player.inventar[Items.superball] = 1
        else:
            Gamestate.player.inventar[Items.superball] = Gamestate.player.inventar[Items.superball] + 1
    else:
        print(Trader.obj_trader_VertaniaCity.name, "Tut mir leid aber du hast nicht genug Geld bei dir!")
