import Gamestate
import Items


def inventar_check():
    if Gamestate.player.inventar == {}:
        print("Du hast noch keine Items. Bitte geh in einen Shop und kaufe dort ein.")
        return False

    else:
        return True


def choose_item():
    notDone = True
    print("In deinem Inventar befinden sich folgende Items")
    i = 1
    for key, value in Gamestate.player.inventar.items():
        print(i,":", key.name, value)
        i = i+1

    while notDone:
        item_name_liste = list(Gamestate.player.inventar.keys())
        userinput = input("Welches Item möchtest du benutzen?")
        if userinput.isnumeric():
            userinput = int(userinput) - 1
            if userinput in range(len(item_name_liste)):
                return item_name_liste[userinput]
            else:
                print("Bitte richtige eingabe")


def use_item(itemname):
    if Gamestate.player.inventar[itemname] > 0:
        Gamestate.player.inventar[itemname] = Gamestate.player.inventar[itemname] - 1
        return True
    else:
        print("Du hast kein Item mehr davon")
        return False
