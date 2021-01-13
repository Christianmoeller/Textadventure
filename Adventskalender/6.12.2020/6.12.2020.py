
with open("6.12.2020 input") as f:
    f = f.readlines()
#print("orginale liste:",f)

gruppe = []

for i in f:
    i = i.replace("\n", "")
    gruppe.append(i)
f = ",".join(gruppe)

f = f.split(",,")

gruppe2 = []

for i in f:
    i = i.split(",")
    gruppe2.append(i)
#print(gruppe2)

var = 0

for m in f:
    eins = m.split(",")
    print(eins)
    eins = set(m)
    print(m)
    print(eins)
    var += 1





x = set(gruppe2[0][0])
y = set(gruppe2[0][1])






#for i in f:
    #l = i.replace(",","")
    #x = x+len(set(l))
    #lineofchar.append(set(l))


#print(lineofchar)


# indersection
#pro gruppe