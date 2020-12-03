from Classes.def_classes import *

def wurf(unter=0, ober=100):
    zahl = random.randrange(unter, ober)
    #print("Dein Wurf war {}".format(zahl))
    return zahl

def begegnung(Hp, PlayerDmg):
    infight = True
    Warg = Monster(25, "Warg", 20)
    Wolf = Monster(20, "Wolf", 10)
    Oger = Monster(50, "Oger", 30)
    Mensch = Monster(100, "Mensch", 0) #Weil Menschen scheiße sind
    Orc = Monster(70, "Orc", 50)
    Monsterliste = [Warg, Wolf, Oger, Mensch, Orc]
    Choose = random.choice(Monsterliste)
    while infight:
        print(Choose.Gattung)
        begegnung = input("Was willst du tun? Laufen oder kämpfen?")
        if begegnung == "kämpfen":

            while Choose.HP > 0 and Hp > 0:
                if wurf() > 50:
                    Choose.HP = Choose.HP-PlayerDmg
                    print("Der", Choose.Gattung, "hat noch ", Choose.HP, "Hp")
                else:
                    Hp = Hp-Choose.Dmg
                if Choose.HP <= 0:
                    print("Der", Choose.Gattung, "ist Tot")
                if Hp <= 0:
                    print("Du Hast keine Hp mehr")
            infight = False
        elif begegnung == "laufen":
            zahl = wurf()
            if zahl > 25:
                print("Glück gehabt, du konntest fliegen ohne Schaden zu nehmen")
            else:
                Hp = Hp - Choose.Dmg
                print("Du konntest zwar fliehen aber der", Choose.Gattung, "hat dich erwischt")
                print("du hast noch", Hp, "Hp übrig")
            infight = False
        else:
            print("iwas musst du machen")
    return Hp

def gameloop():
    Hp = 100
    Spieler_dmg = 20
    Lebendig = True
    while Lebendig == True:
        if Hp <= 0:
            Lebendig = False
            print("Game Over")
            exit()

        print("Was wirst du tun?")
        userinput = input("rechts?, links?, vor?, zurück?, hp?\n")
        if userinput == "hp":
            print("HP: {}".format(Hp))
        elif userinput in ["rechts", "links", "vor", "zurück"]:
            ergebnis = roll_movement()
            if ergebnis < 25 and not ergebnis == -1:
                Hp = begegnung(Hp, Spieler_dmg)

        else:
            print("unbekannter Befehl!")

print("Willkommen in der Welt von \"Bitte hier Name einfügen\". Es liegt an dir.")
gameloop()