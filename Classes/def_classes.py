import random

def roll_movement():
    zahl = random.randrange(0, 100)
    return zahl


class Lebewesen:
    HP = 0
    Gattung = ""
    Dmg = 0


class Monster(Lebewesen):
    def __init__(self, HP, Gattung, Dmg):
        self.HP=HP
        self.Dmg=Dmg
        self.Gattung=Gattung


