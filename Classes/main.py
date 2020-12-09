from Classes.def_classes import *




def gameloop():
    gs = GameState("", 100, 20,{"mainhand":0,"offhand" :0})
    gs.playername    = input("Wie heißt du?\n")
    gs.playerdmg = gs.playerdmg
    print("Hallo", gs.playername + ".")

    Lebendig = True
    while Lebendig == True:
        if Hp <= 0:
            Lebendig = False
            print("Game Over")
            exit()

        print("Was wirst du tun?")
        userinput = input("Gehst du nach rechts, links nach vorne oder zurück?\n")
        if userinput == "hp":
            print("HP: {}".format(gs.playerhp))
        elif userinput == "dmg":
            print("Dmg: {}".format(gs.playerdmg))
        elif userinput in ["rechts", "links", "vor", "zurück"]:
            ergebnis = wurf(0,100)
            if ergebnis >= 50:
                gs = kampf(gs, True)
            elif ergebnis >=0 and ergebnis <=20:
                userinput = input("Du kommst an eine Weggabelung. Gehst du links oder rechts")
                if userinput == "rechts":
                    print("eine große Wand versperrt dir den weg. Du gehst zurück")
                elif userinput == "links":
                    print("soweit so gut")
                else:
                    print("Unbekannter Befeh!")

            elif ergebnis == 1:
                print("Du hast Gewonnen")
                exit()
        else:
            print("unbekannter Befehl!")

print("Willkommen in der Welt von \"Bitte hier Name einfügen\". Es liegt an dir.")
gameloop()


