import Classes.def_classes
import Classes.monster

def levelsystem(gs,monster):
    gs.player_ep = gs.player_ep + monster.monster_ep
    print("Du erhälst", monster.monster_ep, "EP")
    if gs.player_ep >= gs.benötigte_ep:
        print("Level UP")
        gs.player_ep = gs.player_ep - gs.benötigte_ep
        gs.playerhp = gs.playerhp + 10 # bei levelup werden die spieler Hp um 10 erhöt
        print("Deine Hp wurden um 10 erhör")
        gs.playerdmg = gs.playerdmg + 10 # bei levelup wird der spieler dmg um 10 erhöt
        print("Dein Schaden wurde um 10 erhöt")
        gs.benötigte_ep = gs.benötigte_ep + 100

    return gs
