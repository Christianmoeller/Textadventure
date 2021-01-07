f = open("2.12.2020 input.txt", "r")
liste = f.readlines()
def versuch():
    #progress = 0
    count = 0
    #elementliste = liste[progress]

    for elementliste in liste:


        line = elementliste.split(":")
        leftside = line[0]
        leftsidesplit = leftside.split()
        rightside = line[1]
        conditionletter = leftsidesplit[1]
        conditionnumber = leftsidesplit[0]
        minmaxsplit = conditionnumber.split("-")
        minimum = int(minmaxsplit[0])
        maximum = int(minmaxsplit[1])

        conditionlettercount = rightside.count(conditionletter)
        if conditionlettercount >= minimum and conditionlettercount <= maximum:
            count = count + 1
            print("yes")
        else:
            print("nope")
    return count

print(versuch())







