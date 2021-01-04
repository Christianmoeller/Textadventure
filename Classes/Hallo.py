def manipulieren(obj, kljdfg):
    obj["hallo3"] = 3
    kljdfg.append("keinezahl")
    ergebnis = kljdfg + ["lol"]
    return ergebnis


def main():
    mydict = {"hallo1": 1, "hallo2": 2}
    einezahl = ["zahl"]
    print(mydict)
    ergebnis = manipulieren(mydict, einezahl)
    print(mydict)
    print(einezahl)
    print(ergebnis)

main()