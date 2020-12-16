import random
import Classes.variablen
import Classes.monster
import Classes.levelsystem

def interaktion (Antworten,gs, diefrage):
    inputnichtakzeptiert = True
    while inputnichtakzeptiert:
        userinput = input(diefrage)

        if userinput in Antworten:
            #if type(Antworten[userinput]) == str:
                #print(Antworten[userinput])
            #elif callable(Antworten[userinput]):
            Antworten[userinput](gs)
            inputnichtakzeptiert = False
            #else:
             #   print("ungiltiger type")
        else:
            print("Fehler")
class GameState:
    def __init__(self, playername, playerhp, playerdmg, playerinventar, playerrüstung, player_ep, benötigte_ep):
        self.playername = playername
        self.playerhp = playerhp
        self.playerdmg = playerdmg
        self.playerinventar = playerinventar
        self.playerrüstung = playerrüstung
        self.player_ep = player_ep
        self.benötigte_ep = benötigte_ep


def schadenbrechenen (gamestate):#< schaden meiens spielers wird berechent und zurückgegeben
    return gamestate.playerdmg+gamestate.playerinventar["mainhand"]+gamestate.playerinventar["offhand"]

def random_waffe():#eine random waffe wird rurückgegeben
    waffenliste = Classes.variablen.Waffenliste
    w_choise = random.choice(waffenliste)
    return w_choise

# eine zahl zwischen 1-100
def wurf(unter=0, ober=100):
    return random.randrange(unter, ober)

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
    print("Ein", monster.Gattung, "steht vor dir.")
    while monster.HP > 0 and gamestate.playerhp > 0:
        if wurf(0,100)>50: #< liegt die zahl zwischen 80-100 trifft der gegner mich
            gamestate.playerhp = gamestate.playerhp-Classes.monster.monsterdmg_berechnung(gamestate, monster.Dmg)
            print("player bekommt schaden")
            print(gamestate.playerhp)
        else:
            monster.HP = monster.HP-schadenbrechenen(gamestate)
            print("monster bekommt schaden")
    if monster.HP <= 0:
        print("Monster tot")
        Classes.levelsystem.levelsystem(gamestate, monster)
        loot(gamestate)
    return gamestate
def laufen(gs):
    print("Du rennst wie eine kleine Mu**** davon. Angsthase\nDu kommst wieder an eine neue Kreuzung\n")


def loot(gs):#<bekommt man loot?
    if wurf(0,100)>=0:
        gefundenes_item = welches_item_findest_du() # das ist ein objekt
        if type(gefundenes_item) == Classes.variablen.Wappon:
            print("Du hast ein", gefundenes_item.Name, "gefunden.\n")
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
        print("Du hast die Waffe in Deine Mainhand genommen")
        print("Dein Schaden wurde auf", gs.playerdmg+object.Dmg,"erhöt")
    elif gs.playerinventar["offhand"] == 0:
        gs.playerinventar["offhand"] = object.Dmg
        print("Du hast die Waffe in deine Offhand genommen")
        print("Dein Schaden wurde auf", gs.playerdmg+gs.playerinventar["mainhand"]+object.Dmg, "erhöt")
    elif gs.playerinventar["mainhand"] and gs.playerinventar["offhand"]>0:
        waffe_tauschen(gs, object)
    return gs

def waffe_tauschen(gs, object):
    antwort = input("Du hast bereits 2 Waffen. Willst du eine ersetzen?")
    if antwort == "ja":
        print("Mainhand:", gs.playerinventar["mainhand"], "Offhand:", gs.playerinventar["offhand"] )
        antwort = input("Welche Hand willst du ersetzen? Mainhand oder Offhand:")
        if antwort == "mainhand":
            gs.playerinventar["mainhand"] = object.Dmg
            print("Deine Mainhand wurde ersetzt durch:", object.Name)
        if antwort == "offhand":
            gs.playerinventar["offhand"] = object.Dmg
            print("Deine Offhand wurde ersetzt durch:", object.Name)
    else:
        print("Du wirfst die Waffe einfach weg. Du Herzloses Stück S***")


def waffe_tauschen_2():
    #interaktion(Antworten={"ja":})
    pass

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
    Hp_pot(gs, object)
    return gs

