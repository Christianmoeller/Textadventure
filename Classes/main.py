from Classes.def_classes import *
from Classes.monster import *
def begegnung (gs):
    if wurf() >=50:
        if kampf_laufen() == "kämpfen":
            fight(gs, monsterwahl(), True)
        else:
            laufen()

def _help(gs):
    print("Willst Du deine Hp wissen? gebe \"hp\" ein\nWillst Du deinen Dmg wissen? Gebe \"dmg\" ein\nWillst Du eine Rüstung sehen? gebe \"rüstung\" ein\n")
def rechts(gs):
    begegnung(gs)

def links (gs):
    begegnung(gs)

def vor (gs):
    begegnung(gs)
def zurück(gs):
    begegnung(gs)

def hp_abfrage(gs):
    print("Deine Hp betragen:", gs.playerhp,"\n")
def dmg_abfrage(gs):
    print("Dein Aktueller Schaden beträgt:",gs.playerdmg+gs.playerinventar["mainhand"]+gs.playerinventar["offhand"])
def rüstung_abfrage(gs):
    print("Dein Aktueller Rüstungswert ist:", gs.playerrüstung["Helm"]+gs.playerrüstung["Brust"]+gs.playerrüstung["Beine"])


def interaktion (Antworten,gs):
    userinput = input("Gehst du nach \"rechts\", \"links\" nach \"vorne\" oder \"zurück\"? Für mehr Optionen \"help\"\n")
    if userinput in Antworten:
        Antworten[userinput](gs)
    else:
        print("Fehler")

def gameloop():
    gs = GameState("", 100, 20,{"mainhand":0,"offhand" :0},{"Helm":0, "Brust":0, "Beine":0})
    gs.playername    = input("Erst einmal. Wie heißt du?\n")
    print("Hallo", gs.playername + "."+"\nWas wirst du tun?")
    Lebendig = True
    while Lebendig == True:
        if gs.playerhp <= 0:
            Lebendig = False
            print("Game Over")
            exit()


        Antwortmöglichkeiten = {"rechts": rechts, "links":links, "vor":vor, "zurück":zurück,"hp":hp_abfrage, "dmg":dmg_abfrage,"rüstung":rüstung_abfrage, "help":_help}
        interaktion(Antwortmöglichkeiten, gs)

print("Willkommen in der Welt von \"Bitte hier Name einfügen\". Es liegt an dir.")

gameloop()


