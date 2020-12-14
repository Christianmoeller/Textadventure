import random
import Classes.variablen
import Classes.monster

class GameState:
    def __init__(self, playername, playerhp, playerdmg, playerinventar, playerrüstung):
        self.playername = playername
        self.playerhp = playerhp
        self.playerdmg = playerdmg
        self.playerinventar = playerinventar
        self.playerrüstung = playerrüstung


def schadenbrechenen (gamestate):#< schaden meiens spielers wird berechent und zurückgegeben
    return gamestate.playerdmg+gamestate.playerinventar["mainhand"]+gamestate.playerinventar["offhand"]

def random_waffe():#eine random waffe wird rurückgegeben
    waffenliste = Classes.variablen.Waffenliste
    w_choise = random.choice(waffenliste)
    return w_choise

# eine zahl zwischen 1-100
def wurf(unter=0, ober=100):
    return random.randrange(unter, ober)

#TODO: Diese Methode ist sehr lang und kompliziert.
# Vielleicht kannst du zwei Methoden waffegefunden()
# und itemgefunden() erstellen, die den jeweiligen Fall
# behandeln.

#TODO: Sehr viel von deinem Code hier ist nach dem Schema "Eingabe einholen, Reaktion printen"
# Kannst du eine Methode schreiben, die für dich dieses Schema abarbeitet? Also eine Funktion, die
# einen Fragestring, und eine Liste an möglichen antworten nimmt, und den Index der vom Spieler gegebenen Antwort zurückgibt?


# Kampfsystem
def Hp_pot(gamestate, potion):
    gamestate.playerhp = gamestate.playerhp + potion.Wert
    return gamestate

def welches_item_findest_du():#entweder waffe, pot, oderrüstung wird erstellt und zurückgegeben
    randomizeliste = [Classes.variablen.Waffenliste, Classes.variablen.Potionliste, Classes.variablen.Rüstungsliste]
    ausgewählteliste = random.choice(randomizeliste)
    object = random.choice(ausgewählteliste)
    return object# < ein object

def fight(gamestate):
    monster = Classes.monster.monsterwahl()
    while monster.HP > 0 and gamestate.playerhp > 0:
        if wurf(0,100)>50: #< liegt die zahl zwischen 80-100 trifft der gegner mich
            gamestate.playerhp = gamestate.playerhp-Classes.monster.monsterdmg_berechnung(gamestate, monster.Dmg)
            print("player bekommt schaden")
        else:
            monster.HP = monster.HP-schadenbrechenen(gamestate)
            print("monster bekommt schaden")
    if monster.HP <= 0:
        print("Monster tot")
        loot(gamestate)
    return gamestate
def laufen(gs):
    print("Du rennst wie eine kleine Muschi davon. Angsthase")


def loot(gs):#<bekommt man loot?
    if wurf(0,100)>=0:
        print("du bekommt loot")
        gefundenes_item = welches_item_findest_du() # das ist ein objekt
        if type(gefundenes_item) == Classes.variablen.Wappon:
            print("waffe")
            loot_waffe(gs, gefundenes_item)
        elif type(gefundenes_item) == Classes.variablen.Armor:
            print("Rüstung")
            loot_rüstung(gs, gefundenes_item)
        elif type(gefundenes_item) == Classes.variablen.Potion:
            print("potion")
            loot_potion(gs, gefundenes_item)
    return gs

def loot_waffe(gs, object):
    if gs.playerinventar["mainhand"] == 0:
        gs.playerinventar["mainhand"] = object.Dmg
    elif gs.playerinventar["offhand"] == 0:
        gs.playerinventar["offhand"] = object.Dmg
    else:
        print("waffe weggeworfen")
    return gs


def loot_rüstung(gs, object):
    if object.Slot == "Helm":
        gs.playerrüstung["Helm"] = object.Wert
        print("Dein Helmrüstungswert hat sich erhöt")
    elif object.Slot == "Brust":
        gs.playerrüstung["Brust"] = object.Wert
        print("Dein Brustrüstungswert hat sich erhöt")
    elif object.Slot == "Beine":
        gs.playerrüstung["Beine"] = object.Wert
        print("Deine Beinrüstungswert hat sich erhöt")
    return gs
def loot_potion(gs, object):
    gs.playerhp = gs.playerhp+object.Wert
    Hp_pot(gs, object)
    return gs