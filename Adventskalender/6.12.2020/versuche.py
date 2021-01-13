with open("6.12.2020 input") as f:
    f = f.read().split("\n\n")




#print(f)
#print(f[0])
#print(f[0][0])
liste = []

for gruppe in f:
    liste.append(gruppe.split("\n"))
print(liste)
ergebnis = 0

for gruppe in liste:
    schnittmenge = set(gruppe[0])
    for person in gruppe:
        personen_set = set(person)
        schnittmenge = schnittmenge & personen_set
    ergebnis = ergebnis +len(schnittmenge)
    print(ergebnis)

#alle gleichen antworten aus einem element der lsite f

#schnittmendge
