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
#

# wenn die hp meines monsters bei 0 oder kleiner ist besteht die chance eine waffe zu finden die mein dmg erhöt oder ein potion zu finden der meine hp erhöt
def w_oder_p(monster, gamestate):
    if monster.HP <= 0:
        gefundenes_item = welches_item_findest_du()
        print(gefundenes_item.Name)
        if type(gefundenes_item)== Classes.variablen.Wappon:
            if gamestate.playerinventar["mainhand"] == 0:
                gamestate.playerinventar["mainhand"] = gefundenes_item.Dmg
                print("Du hast ein", gefundenes_item.Name, "gefunden.")
                print("Dein Schaden erhöt sich um", gefundenes_item.Dmg)
            elif gamestate.playerinventar["offhand"] == 0:
                gamestate.playerinventar["offhand"] = gefundenes_item.Dmg
                print("Du hast eine Waffe gefunden und sie in die offhand genommen")
                print("dein schaden erhöt sich um", gefundenes_item.Dmg)
            else:
                print("Du findest ein", gefundenes_item.Name)
                abfrage = input("Du hast bereits 2 waffen. Willst du die neue waffe ersetzen oder nicht?\n")
                if abfrage == "ja":
                    abfrage = input("welche waffe willst du ersetzen? mainhand oder offhand?\n")
                    if abfrage == "mainhand":
                        gamestate.playerinventar["mainhand"] = gefundenes_item.Dmg
                        print("Deine Mainhand wurde ersetzt")
                    else:
                        gamestate.playerinventar["offhand"] = gefundenes_item.Dmg
                        print("Deine offhand wurde ersetzt")
                #TODO: Wenn ich "Ja" eintippe, wird die Waffe weggeworfen :( Frage explizit möglichkeiten ab ("ja,"nein") und gib "unbekannter Befehl" aus, wenn etwas anderes eingegeben wird
                else:
                    print("Okay, du hast die neue Waffe weggeworfen. Du wirst diese nie! wieder! sehen. Es ist vorbei! Aus!")
                    return gamestate
        elif type(gefundenes_item) == Classes.variablen.Potion:
            Hp_pot(gamestate, gefundenes_item)
            print("Deine hp erhöt sich um", gefundenes_item.Wert)
        elif type(gefundenes_item) == Classes.variablen.Armor:
            if gefundenes_item.Slot == "Helm":
                gamestate.playerrüstung["Helm"] = gefundenes_item.Wert
                print("Dein Helmrüstungswert hat sich erhöt")
            elif gefundenes_item.Slot == "Brust":
                gamestate.playerrüstung["Brust"] = gefundenes_item.Wert
                print("Dein Brustrüstungswert hat sich erhöt")
            elif gefundenes_item.Slot == "Beine":
                gamestate.playerrüstung["Beine"] = gefundenes_item.Wert
                print("Deine Beinrüstungswert hat sich erhöt")
    return gamestate
# Kampfsystem
def Hp_pot(gamestate, potion):
    gamestate.playerhp = gamestate.playerhp + potion.Wert
    return gamestate
def welches_item_findest_du():#entweder waffe, pot, oderrüstung wird erstellt und zurückgegeben
    randomizeliste = [Classes.variablen.Waffenliste, Classes.variablen.Potionliste, Classes.variablen.Rüstungsliste]
    ausgewählteliste = random.choice(randomizeliste)
    object = random.choice(ausgewählteliste)
    return object# < ein object

#TODO: hier drin hast du auch 2 zentrale Ereignisse: spieler wählt kämpfen, oder spieler wählt laufen.
# Die können auch in eine eigene Methode rein
#def kampf (gamestate, infight):
#    while infight: #kampf gegen ein Mosnter aus monsterlsite
#        print("Du musst gegen ein", monster.Gattung, "kämpfen. Seine Hp betragen", monster.HP, "und er macht", monster.Dmg, "Schaden.", "Deine Hp betragen zu beginn", gamestate.playerhp)
#        while monster.HP>0 and gamestate.playerhp>0 and infight==True: # wärend beide hp über 0 liegen wird gekämpft
#            frage = input("Kämpfen oder Laufen?\n")
#            if frage in ["kämpfen", "k"]:
#                treffer = wurf(0,100)
#                if treffer >= 30:
#                    monster.HP = monster.HP-playerschaden
#                    print(monster.Gattung, "hat noch ", monster.HP, "Hp")
#                else:
#                    gamestate.playerhp = gamestate.playerhp-Classes.monster.monsterdmg(gamestate, monster.Dmg)
#                    print("Du hast noch", gamestate.playerhp, "Hp")
#            elif frage == "laufen": #sollte er fliehen bestehtn eine chance von 50% das er entkommt und keinen dmg bekommt  oder einmal schaden bekommt
#                if wurf(0,2) == 1:
#                    print("Glück gehabt. Du entkommst ohne schaden zu bekommen\n")
#                    infight = False
#                else:
#                    gamestate.playerhp = gamestate.playerhp-monster.Dmg
#                    print("Du konntest fliegen aber", monster.Gattung, "macht dir Schaden in höhe von", monster.Dmg)
#                    infight = False
#            gamestate = w_oder_p(monster, gamestate)
#        infight = False
#    return gamestate

def fight(gamestate,monster, infight):
    playerschaden = schadenbrechenen(gamestate)
    while monster.HP > 0 and gamestate.playerhp > 0 and infight == True:
        if wurf(0,100)>80: #< liegt die zahl zwischen 80-100 trifft der gegner mich
            gamestate.playerhp = gamestate.playerhp-Classes.monster.monsterdmg_berechnung(gamestate, monster.Dmg)
        if monster.HP <=0:
            loot()
            print("Monster tot")
            infight = False
        else:
            monster.HP = monster.HP-schadenbrechenen(gamestate)

    return gamestate


def laufen():
    print("Du bist davon gelaufen! Wie eine kleine...")

def kampf_laufen():
    return input("Willst du \"kämpfen\" oder \"laufen\"")
def loot():#<bekommt man loot?
    if wurf(0,100)>0:
        gefundenes_item = welches_item_findest_du()
        if gefundenes_item == Classes.variablen.Wappon:
            print("Waffe gefunden")
        elif gefundenes_item == Classes.variablen.Armor:
            print("rüstung gefunen")
        elif gefundenes_item == Classes.variablen.Potion:
            print("potion gefunden")

