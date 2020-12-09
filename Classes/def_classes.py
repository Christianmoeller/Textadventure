import random
import Classes.variablen
class Monster:
    def __init__(self, HP, Gattung, Dmg, Level):
        self.HP=HP
        self.Dmg=Dmg
        self.Gattung=Gattung
        self.Level = Level

class GameState:
    def __init__(self, playername, playerhp, playerdmg, playerinventar):
        self.playername = playername
        self.playerhp = playerhp
        self.playerdmg = playerdmg
        self.playerinventar = playerinventar


def schadenbrechenen (gamestate):
    schadenfürdenkampf = gamestate.playerdmg+gamestate.playerinventar["mainhand"]+gamestate.playerinventar["offhand"]
    return schadenfürdenkampf


def random_waffe():
    waffenliste = Classes.variablen.Waffenliste
    w_choise = random.choice(waffenliste)
    return w_choise

# eine zahl zwischen 1-100
def wurf(unter=0, ober=100):
    zahl = random.randrange(unter, ober)
    return zahl

# wenn die hp meines monsters bei 0 oder kleiner ist besteht die chance eine waffe zu finden die mein dmg erhöt oder ein potion zu finden der meine hp erhöt
def w_oder_p(monster, gamestate):
    if monster.HP <= 0:
        if type(welches_item_findest_du())== type(Classes.variablen.Wappon):
            gamestate.playerinventar["mainhand"] == 0

        if type(welches_item_findest_du())== type(Classes.variablen.Items):
            pass

        else:
            waffe = random_waffe()
            print("Du Findest ein", waffe.Name)
            if gamestate.playerinventar["mainhand"] ==0:
                gamestate.playerinventar["mainhand"] = waffe.Dmg
            elif gamestate.playerinventar["offhand"] ==0:
                gamestate.playerinventar["offhand"] = waffe.Dmg
            else:
                #if gamestate.playerinventar["offhand"] >= 0 and gamestate.playerinventar["mainhand"]>0
                abfrage= input("du hast bereits 2 waffen. Willst du die neue waffe ersetzen oder nicht")
                if abfrage == "ja":
                    abfrage = input("welche waffe willst du ersetzen? mainhand oder offhand")
                    if abfrage == "mainhand":
                        gamestate.playerinventar["mainhand"] = waffe.Dmg
                        print("deine Mainhand wurde ersetzt")
                    else:
                            gamestate.playerinventar["offhand"] = waffe.Dmg
                            print("deine offhand wurde ersetzt")
                else:
                    print("gut du hast die neue waffe weggeworfen")
                    return gamestate
            print(gamestate.playerinventar["mainhand"])

            print("Dein Schaden erhöt sich um", waffe.Dmg,)


    return gamestate
# Kampfsystem

def welches_item_findest_du():
    randomizeliste = [Classes.variablen.Waffenliste, Classes.variablen.Itemliste]
    object = random.choice(randomizeliste)
    return random.choice(object)# < ein object

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


def kampf (gamestate, infight):

#Monsterwahl, gegen welches Monster gekämpft werden soll
    playerschaden = schadenbrechenen(gamestate)
    monster = monsterwahl()
    while infight: #kampf gegen ein Mosnter aus monsterlsite
        print("Du kämpfst gegen einen", monster.Gattung, "und seine Hp betragen", monster.HP, "Er macht", monster.Dmg, "Schaden.", "Deine Hp betragen zu beginn", gamestate.playerhp)
        while monster.HP>0 and gamestate.playerhp>0 and infight==True: # wärend beide hp über 0 liegen wird gekämpft
            frage = input("Kämpfen oder Laufen?\n")
            if frage in ["kämpfen", "k"]: #sollte die antwort kämpfen sein soll der kampf bis zum tot geämpft werden
                treffer = wurf(0,100)
                if treffer >= 30:
                    monster.HP = monster.HP-playerschaden
                    print("das Monster hat noch ", monster.HP, "Hp")
                else:
                    gamestate.playerhp = gamestate.playerhp-monster.Dmg
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

