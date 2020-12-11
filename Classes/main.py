from Classes.def_classes import *

def rechts(gs):
    if wurf() >=50:
        kampf(gs,True)
def links (gs):
    if wurf() >=50:
        kampf(gs,True)
def vor (gs):
    if wurf() >=50:
        kampf(gs,True)
def zurück(gs):
    if wurf() >=50:
        kampf(gs,True)
def hp_abfrage(gs):
    print("Deine Hp betragen:", gs.playerhp,"\n")
def dmg_abfrage(gs):
    print("Dein Aktueller Schaden beträgt:",gs.playerdmg+gs.playerinventar["mainhand"]+gs.playerinventar["offhand"])
def rüstung_abfrage(gs):
    print("Dein Aktueller Rüstungswert ist:", gs.playerrüstung["Helm"]+gs.playerrüstung["Brust"]+gs.playerrüstung["Beine"])


def interaktion (Antworten,gs,):
    userinput = input("Gehst du nach \"rechts\", \"links\" nach \"vorne\" oder \"zurück\"?\nWillst Du deine Hp wissen? gebe \"hp\" ein\nWillst Du deinen Dmg wissen? Gebe \"dmg\" ein\nWilslt Du eine Rüstung sehen? gebe \"rüstung\" ein\n")
    Antworten[userinput](gs,)

def gameloop():
    gs = GameState("", 100, 20,{"mainhand":0,"offhand" :0},{"Helm":0, "Brust":0, "Beine":0})
    gs.playername    = input("Erst einmal. Wie heißt du?\n")
    print("Hallo", gs.playername + "."+"\nWas wirst du tun?\n")
    Lebendig = True
    while Lebendig == True:
        if gs.playerhp <= 0:
            Lebendig = False
            print("Game Over")
            exit()


        Antwortmöglichkeiten = {"rechts": rechts, "links":links, "vor":vor, "zurück":zurück,"hp":hp_abfrage, "dmg":dmg_abfrage,"rüstung":rüstung_abfrage}
        interaktion(Antwortmöglichkeiten, gs)
    else:
        print("unbekannter Befehl!")

print("Willkommen in der Welt von \"Bitte hier Name einfügen\". Es liegt an dir.")

gameloop()


