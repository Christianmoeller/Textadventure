f = open("2.12.2020 input.txt", "r")
liste = f.readlines()


def firsttry():
    count = 0
    for elementlist in liste:
        line = elementlist.split(":")
        leftside = line[0]
        leftsidesplit = leftside.split()
        rightside = line[1]
        conditionletter = leftsidesplit[1]
        conditionnumber = leftsidesplit[0]
        minmaxsplit = conditionnumber.split("-")
        minimum = int(minmaxsplit[0])
        maximum = int(minmaxsplit[1])

        if (conditionletter == rightside[minimum]) ^ (conditionletter == rightside[maximum]):
            count = count + 1
    return count


print(firsttry())
