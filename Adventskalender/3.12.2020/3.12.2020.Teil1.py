f = open("3.12.2020source.txt", "r")
liste = f.readlines()



movementtoright = 1
movementdown = 3
line = liste[movementdown]
charactercounter = len(line)-1

def walkL (down, right, linelength):
    newdown = down + 3
    newright = (right + 1) % (linelength + 1)
    return (newdown, newright)

posx = 0
posy = 0
def treecheck():
    if pos[]





while posy <= len(liste)-1:
    # def neues feld
    # def checktz ob baum 1
    # posy erhöt 2
    #checken ob baum ja oder nein
    #dann weiter
    #walkL ist ein tupel
















def funk():
    linecounter = 0
    treecounter = 0
    truecounter = 0
    a = 0

    rightpos = 0
    downpos = 0
"""    while downpos <= len(liste)-1 :
        #checkfield(downpos, rightpos)
        walk = walkL(downpos, rightpos, charactercounter)
        rightpos = walk[0]
        downpos = walk[1]
"""
    for i in liste:

        if linecounter % 3 == 0:
            truecounter = truecounter+1
            linecharacter = i[a]
            a = a + movementtoright
            linecounter = linecounter + 1
            print(linecharacter)
            if linecharacter == "#":
                treecounter = treecounter+1
        else:
            # print("weiter")
            linecounter = linecounter + 1
        if a == charactercounter:
            print("character anzahl:", a)
            a = 0
        print("-y:",linecounter, "x:", a)
    print(treecounter)
    #print(linecounter)
    #print(truecounter)
funk()

