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



def random_waffe():
    waffenliste = Classes.variablen.Waffenliste
    w_choise = random.choice(waffenliste)
    return w_choise

# eine zahl zwischen 1-100
def wurf(unter=0, ober=100):
    zahl = random.randrange(unter, ober)
    return zahl

# wenn die hp meines monsters bei 0 oder kleiner ist besteht die chance eine waffe zu finden die mein dmg erhöt oder ein potion zu finden der meine hp erhöt
def w_oder_p(monster, gamestate, Hp_pot):
    w_oderp = wurf(0,100)
    if monster.HP <= 0:
        if w_oderp >=50:
            gamestate.playerhp = gamestate.playerhp + Hp_pot
            print("Dein Leben erhöht sich um", Hp_pot)
        else:
            waffe = random_waffe()
            gamestate.playerinventar["mainhand"] = gamestate.playerinventar["mainhand"] + waffe.Dmg
            gamestate.playerdmg = gamestate.playerdmg+gamestate.playerinventar["mainhand"]
            print(gamestate.playerinventar["mainhand"])
            print("Du Findest ein", waffe.Name)
            print("Dein Schaden erhöt sich um", waffe.Dmg, "dein Dmg beträgt jetzt", gamestate.playerdmg)


    return gamestate
# Kampfsystem

def monsterwahl():
    Warg = Monster(25, "Warg", 20, 2)
    Wolf = Monster(20, "Wolf", 10, 2)
    Oger = Monster(50, "Oger", 30, 3)
    Mensch = Monster(100, "Mensch", 100, 4)
    Orc = Monster(70, "Orc", 50, 4)
    Junger_Scavenger = Monster(10, "junger Scavenger", 10, 1)
    Scavenger = Monster(20, "Scavenger", 15, 1)
    monsterliste = [Warg, Wolf, Oger, Orc, Junger_Scavenger, Scavenger, Mensch]
    monsterLevelListen = [[monster for monster in monsterliste if monster.Level == lvl] for lvl in range(1,5)]
    return random.choice(random.choices(monsterLevelListen, weights=(40,30,20,20), k=1)[0])


def kampf (gamestate, infight):

#Monsterwahl, gegen welches Monster gekämpft werden soll
    monster = monsterwahl()
    while infight: #kampf gegen ein Mosnter aus monsterlsite
        print("Du kämpfst gegen einen", monster.Gattung, "und seine Hp betragen", monster.HP, "Er macht", monster.Dmg, "Schaden.", "Deine Hp betragen zu beginn", gamestate.playerhp)
        while monster.HP>0 and gamestate.playerhp>0 and infight==True: # wärend beide hp über 0 liegen wird gekämpft
            frage = input("Kämpfen oder Laufen?\n")
            if frage == "kämpfen": #sollte die antwort kämpfen sein soll der kampf bis zum tot geämpft werden
                treffer = wurf(0,100)
                if treffer >= 50:
                    monster.HP = monster.HP-gamestate.playerdmg
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
            gamestate = w_oder_p(monster, gamestate, Classes.variablen.Kleiner_Hp_Pot.Wert)
        infight = False
    return gamestate



# inventar main hand  offhand   helm  rüstung...
#wenn man sich für eine richtug entscheidet gibt es mehr wahrscheinlichkeiten als nur ein monser zu treffen
#zum beispiel noch ein item zu finden oder einfach eine story
# schaden auf default   wenn eine waffe aufgehoben wird, wird der default  wert nixht erhöt     das heißt ein dic mit key = waffen namen und value = der waffenschaden
# mit dichname[key]< für den value von diesem key