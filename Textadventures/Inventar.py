import Gamestate
import Items


def inventar_check(item):
    if item in Gamestate.player.inventar:
        if Gamestate.player.inventar.get(item) >= 0:
            return True
    return False
