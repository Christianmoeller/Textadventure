import random

class Monster:
    def __init__(self, HP, Gattung, Dmg, Level, monster_ep):
        self.HP=HP
        self.Dmg=Dmg
        self.Gattung=Gattung
        self.Level = Level
        self.monster_ep = monster_ep

def monsterdmg_berechnung(spielerrüstung, monsterdmg):
    komletterüstung = spielerrüstung.playerrüstung["Helm"]+spielerrüstung.playerrüstung["Brust"]+spielerrüstung.playerrüstung["Beine"]
    x = monsterdmg-komletterüstung
    if x <0:
        x= 0
    return x

def monsterwahl():
    monsterLevelListen = [[monster for monster in all_monster() if monster.Level == lvl] for lvl in range(1,5)]
    return random.choice(random.choices(monsterLevelListen, weights=(40,30,20,10), k=1)[0])

def all_monster():
    Warg = Monster(25, "Warg", 20, 2, 15)
    Wolf = Monster(20, "Wolf", 10, 2, 10)
    Oger = Monster(50, "Oger", 30, 3, 30)
    Mensch = Monster(100, "Mensch", 0, 4, 5)
    Orc = Monster(70, "Orc", 50, 4, 40)
    Junger_Scavenger = Monster(10, "junger Scavenger", 10, 1, 5)
    Scavenger = Monster(20, "Scavenger", 15, 1, 10)
    return [Warg, Wolf, Oger, Orc, Junger_Scavenger, Scavenger, Mensch]