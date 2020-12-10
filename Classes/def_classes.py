import random
import Classes.variablen
class Monster:
    def __init__(self, HP, Gattung, Dmg, Level):
        self.HP=HP
        self.Dmg=Dmg
        self.Gattung=Gattung
        self.Level = Level

class GameState:
    def __init__(self, playername, playerhp, playerdmg, playerinventar, playerrüstung):
        self.playername = playername
        self.playerhp = playerhp
        self.playerdmg = playerdmg
        self.playerinventar = playerinventar
        self.playerrüstung = playerrüstung


def schadenbrechenen (gamestate):
    return gamestate.playerdmg+gamestate.playerinventar["mainhand"]+gamestate.playerinventar["offhand"]

def random_waffe():
    waffenliste = Classes.variablen.Waffenliste
    w_choise = random.choice(waffenliste)
    return w_choise

# eine zahl zwischen 1-100
def wurf(unter=0, ober=100):
    return random.randrange(unter, ober)

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
def welches_item_findest_du():
    randomizeliste = [Classes.variablen.Waffenliste, Classes.variablen.Potionliste, Classes.variablen.Rüstungsliste]
    ausgewählteliste = random.choice(randomizeliste)
    object = random.choice(ausgewählteliste)
    return object# < ein object

def monsterwahl():
    Warg = Monster(25, "Warg", 20, 2)
    Wolf = Monster(20, "Wolf", 10, 2)
    Oger = Monster(50, "Oger", 30, 3)
    Mensch = Monster(100, "Mensch", 0, 4)
    Orc = Monster(70, "Orc", 50, 4)
    Junger_Scavenger = Monster(10, "junger Scavenger", 10, 1)
    Scavenger = Monster(20, "Scavenger", 15, 1)
    monsterliste = [Warg, Wolf, Oger, Orc, Junger_Scavenger, Scavenger, Mensch]
    monsterLevelListen = [[monster for monster in monsterliste if monster.Level == lvl] for lvl in range(1,5)]
    return random.choice(random.choices(monsterLevelListen, weights=(40,30,20,10), k=1)[0])
def monsterdmg(spielerrüstung, monsterdmg):
    komletterüstung = spielerrüstung.playerrüstung["Helm"]+spielerrüstung.playerrüstung["Brust"]+spielerrüstung.playerrüstung["Beine"]
    x = monsterdmg-komletterüstung
    if x <0:
        x= 0
    return x

def kampf (gamestate, infight):

#Monsterwahl, gegen welches Monster gekämpft werden soll
    playerschaden = schadenbrechenen(gamestate)
    monster = monsterwahl()
    while infight: #kampf gegen ein Mosnter aus monsterlsite
        print("Du musst gegen ein", monster.Gattung, "kämpfen und seine Hp betragen", monster.HP, "Er macht", monster.Dmg, "Schaden.", "Deine Hp betragen zu beginn", gamestate.playerhp)
        while monster.HP>0 and gamestate.playerhp>0 and infight==True: # wärend beide hp über 0 liegen wird gekämpft
            frage = input("Kämpfen oder Laufen?\n")
            if frage in ["kämpfen", "k"]:
                treffer = wurf(0,100)
                if treffer >= 30:
                    monster.HP = monster.HP-playerschaden
                    print("das Monster hat noch ", monster.HP, "Hp")
                else:
                    gamestate.playerhp = gamestate.playerhp-monsterdmg(gamestate, monster.Dmg)
                    print("Du hast noch", gamestate.playerhp, "Hp")
            elif frage == "laufen": #sollte er fliehen bestehtn eine chance von 50% das er entkommt und keinen dmg bekommt  oder einmal schaden bekommt
                if wurf(0,2) == 1:
                    print("Glück gehabt. Du entkommst ohne schaden zu bekommen")
                    infight = False
                else:
                    gamestate.playerhp = gamestate.playerhp-monster.Dmg
                    print("Du konntest fliegen aber", monster.Gattung, "macht dir Schaden in höhe von", monster.Dmg)
                    infight = False
            gamestate = w_oder_p(monster, gamestate)
        infight = False
    return gamestate



# inventar main hand  offhand   helm  rüstung...
#

