from Classes.def_classes import *
from Classes.monster import *
import json





def richtungsantworten_begegnung():
    a = "Ein rießiger Berg tut sich vor Dir auf. Du kannst eine Höle erkennen mit Monstern davor.\nSie scheinen Etwas zu bewachen. Eines der Monster nimmt dich wahr!\n"
    b = "Es geht steil Bergab! Du rutscht aus und landest in mitten eines Nests.\nEines der Vicher nimmt dich wahr.\n"
    c = "Du kommst an eine große Wiese voller Blumen und vielen Tieren. Wow was für ein schöner Ort.\nOh was ist das? Ein wildes Monster!\n"
    d = "Es fängt an zu regnen. Du wirst nass und deine Klamotten fangen an zu stinken.\nDer Gruch lockt ein Monster an.\n"
    e = "Du bist seit Tagen unterwegs. Du machst eine Pause und zündest ein Lagerfeuer an.\nDer Rauch lockt ein Monster an.\n"
    f = "Dir ist unfassbar langweilig. Du singst und tanzt vor dich hin.\nUnachtsam rensnt du in ein Nest von Monstern.\nSofort greiffet dich eins an.\n"
    liste = [a, b, c, d, e, f]
    antwort = random.choice(liste)
    return antwort

def richtungsantworten_ohne_begegnung():
    a = "Es ist ruhig, zu ruhig. Irgendwie verdächtig ruhig. Oh neue Kreuzung\n"
    b = "Alles sieht wie immer gleich aus. Genau wie davor. Na klar noch eine Kreuzung --wer hätte das gedacht---\n"
    c = "Fröhlich singst und tanzt du vor dich hin. Es ist so wunderbar friedlich.\nAus der Ferne siehst du eine neue Kreuzung\n"
    d = "Völlig fertig machst du eine Pause. Du machst nur kurz die Augen zu.\nDu schläfst ein. Nach ein paar Stunden wachst du total erschrocken wieder auf.\nEs ist zwar dunkel geworden aber es geht dir gut.\n"
    e = "Du holst dein Handy aus der Tasche. Kopfhörer rein und volle Lautstärke. Geiler Tag!!!!\n"
    f = "Du kommst was um vor Hunger. Nichts in Richweite. Nicht mal ein Scavenger den du abschlachten könntest und grillen. Nope--Nichts.\n"
    g = "Hmm\n"
    liste = [a, b, c, d, e, f, g]
    antwort = random.choice(liste)
    return antwort

def optionen(gs):
    print("Vergiss es gibt keine optionen für dich du KEK\n")
    fight(gs)

def begegnung (gs):
    antwortmöglichkeiten = {"kämpfen":fight, "laufen":laufen, "optionen":optionen}
    print("Du kämpfst gegen:", gs.monster.Gattung)
    frage = "Greifst Du es an oder läufst Du weg?\n>>kämpfen<<, >>laufen<<, >>optionen<<"
    interaktion(antwortmöglichkeiten, gs, frage)

def save_game(gs):
    file = open("save_game.txt", "w")
    x = json.dumps(gs, cls=GameStateEncoder)
    print(type(x))
    file.write(x)
def load_game(gs):
    file = open("save_game.txt", "r")
    x = json.loads(file)
    file.read(x)


def ep(gs):
    print("Deine ep:", gs.player_ep)
    print("Benötigte Ep für Levelup:", gs.benötigte_ep)

def _help(gs):
    print("Willst Du deine Hp wissen? gebe \"hp\" ein\nWillst Du deinen Dmg wissen? Gebe \"dmg\" ein\nWillst Du eine Rüstung sehen? gebe \"rüstung\" ein\nWillst du deine Ep wissen? Gebe \"ep\" ein\n")
def rechts(gs):
    if wurf(0, 51) > 25:
        print(richtungsantworten_begegnung())
        begegnung(gs)
    else :
        print(richtungsantworten_ohne_begegnung())


def links (gs):
    if wurf(0, 51) > 25:
        print(richtungsantworten_begegnung())
        begegnung(gs)
    else :
        print(richtungsantworten_ohne_begegnung())

def vor (gs):
    if wurf(0, 51) > 25:
        print(richtungsantworten_begegnung())
        begegnung(gs)
    else :
        print(richtungsantworten_ohne_begegnung())

def zurück(gs):
    if wurf(0, 51) > 25:
        print("Du gehst zurück wo du hergekommen bist.\nDummerweise ist Dir ein Monster gefolgt und stehst jetzt direkt vor Dir!")
        begegnung(gs)
    else :
        print(richtungsantworten_ohne_begegnung())

def hp_abfrage(gs):
    print("Deine Hp betragen:", gs.playerhp,"\n")
def dmg_abfrage(gs):
    print("Dein Aktueller Schaden beträgt:",gs.playerdmg+gs.playerinventar["mainhand"]+gs.playerinventar["offhand"])
def rüstung_abfrage(gs):
    print("Helm",gs.playerrüstung["Helm"],"Brust",gs.playerrüstung["Brust"], "Beine", gs.playerrüstung["Beine"] )
    print("Dein Aktueller Rüstungswert ist:", gs.playerrüstung["Helm"]+gs.playerrüstung["Brust"]+gs.playerrüstung["Beine"])



def gameloop():
    gs = GameState("", 100, 20,{"mainhand":0,"offhand" :0},{"Helm":0, "Brust":0, "Beine":0}, 0, 100, monsterwahl())
    gs.playername    = input("Wie lautet dein Name?\n")
    print("Was für ein Sch**** Name...", gs.playername + "...Pff"+"\nNaja egal.")
    Lebendig = True
    frage = "Welche Richtung gehst du?\n>>help<< für mehr Optionen\n"
    Antwortmöglichkeiten = {"rechts": rechts, "links": links, "vor": vor, "zurück": zurück, "hp": hp_abfrage, "dmg": dmg_abfrage, "rüstung": rüstung_abfrage, "help": _help, "ep":ep, "save":save_game, "laden":load_game}
    while Lebendig == True:
        if gs.playerhp <= 0:
            Lebendig = False
            print("Game Over")
            exit()
        interaktion(Antwortmöglichkeiten, gs, frage)




print("Willkommen in der Welt von \"F-T-A-P-I\".\nDu bist also der Held von dem noch nie jemand gehört hat?\nDeine Reise beginnt.")

gameloop()

#TODO
# save and load file .mehr info über das kampfsyste.
# neue riuchungen ohne begegnung
# inventar iwann zum auswählen   sprich menn man n pot findet wird der in eine tasche gepackt und man kann bei bedarf den pot nehmen
# kampfsystem überarbeiten  rudnenbasiert    kein autokampf mehr
# flucht erschweren  durch rätzel
# "wenn möglich" wärend des kampfes die mögichkeit pot zu nehmen bzw die help funktion zu benutzen
# lootverteilung
# Ziel einfügen
