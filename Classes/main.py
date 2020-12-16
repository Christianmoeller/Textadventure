from Classes.def_classes import *
from Classes.monster import *
def begegnung (gs):
    antwortmöglichkeuten = {"kämpfen":fight, "laufen":laufen}
    print("Du kämpfst gegen:", gs.monster.Gattung)
    frage = "Greifst Du es an oder läufst Du weg\n"
    interaktion(antwortmöglichkeuten, gs, frage)

def ep(gs):
    print("Deine ep:", gs.player_ep)
    print("Benötigte Ep für Levelup:", gs.benötigte_ep)

def _help(gs):
    print("Willst Du deine Hp wissen? gebe \"hp\" ein\nWillst Du deinen Dmg wissen? Gebe \"dmg\" ein\nWillst Du eine Rüstung sehen? gebe \"rüstung\" ein\nWillst du deine Ep wissen? Gebe \"ep\" ein\n")
def rechts(gs):
    if wurf(0, 51) > 25:
        print("Ein rießiger Berg tut sich vor Dir auf. Du kannst eine Höle erkennen mit Monstern davor.\nSie scheinen Etwas zu bewachen. Eines der Monster nimmt dich wahr!")
        begegnung(gs)
    else :
        print("Der Weg ist steinig und schwer. Neue Kreuzung! \n")


def links (gs):
    if wurf(0, 51) > 25:
        print("Es geht steil Bergab! Du rutscht aus und landest mitten in einem Nests.\nEines der Ficher nimmt dich whar.")
        begegnung(gs)
    else :
        print("Der Weg ist steinig und schwer. Neue Kreuzung! \n")

def vor (gs):
    if wurf(0, 51) > 25:
        print("Du kommst an eine große Wiese voller Blumen und vielen Tieren. Wow was für ein schöner Ort.\nOh was ist das? Ein wildes Tier!")
        begegnung(gs)
    else :
        print("Der Weg ist steinig und schwer. Neue Kreuzung! \n")

def zurück(gs):
    if wurf(0, 51) > 25:
        print("Du gehst zurück wo du hergekommen bist.\nDummerweise ist Dir ein Monster gefolgt und stehst jetzt direkt vor Dir!")
        begegnung(gs)
    else :
        print("Der Weg ist steinig und schwer. Neue Kreuzung! \n")

def hp_abfrage(gs):
    print("Deine Hp betragen:", gs.playerhp,"\n")
def dmg_abfrage(gs):
    print("Dein Aktueller Schaden beträgt:",gs.playerdmg+gs.playerinventar["mainhand"]+gs.playerinventar["offhand"])
def rüstung_abfrage(gs):
    print("Helm",gs.playerrüstung["Helm"],"Brust",gs.playerrüstung["Brust"], "Beine", gs.playerrüstung["Beine"] )
    print("Dein Aktueller Rüstungswert ist:", gs.playerrüstung["Helm"]+gs.playerrüstung["Brust"]+gs.playerrüstung["Beine"], "(",gs.playerrüstung["Helm"], "+", gs.playerrüstung["Brust"], "+", gs.playerrüstung["Beine"], ")" )



def gameloop():
    gs = GameState("", 100, 20,{"mainhand":0,"offhand" :0},{"Helm":0, "Brust":0, "Beine":0}, 0, 100, monsterwahl())
    gs.playername    = input("Wie lautet dein Name?\n")
    print("Was für ein Sch**** Name...", gs.playername + "...Pff"+"\nNaja egal. Was wirst du tun?")
    Lebendig = True
    frage = "Welche Richtung gehst du?\n>>help<< für mehr Optionen\n"
    Antwortmöglichkeiten = {"rechts": rechts, "links": links, "vor": vor, "zurück": zurück, "hp": hp_abfrage, "dmg": dmg_abfrage, "rüstung": rüstung_abfrage, "help": _help, "ep":ep}
    while Lebendig == True:
        if gs.playerhp <= 0:
            Lebendig = False
            print("Game Over")
            exit()
        interaktion(Antwortmöglichkeiten, gs, frage)




print("Willkommen in der Welt von \"Bitte hier Name einfügen\".\nDu bist also der Held von dem noch nie jemand gehört hat?")

gameloop()
#Lrvrl system
