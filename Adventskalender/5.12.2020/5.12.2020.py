with open("5.12.2020 input") as f:
    liste = f.readlines()


new_list= []

for i in liste:
    i = i.replace("\n", "")
    rows = int(i[:7].replace("B", "1").replace("F", "0"),2)
    columns = int(i[-3:].replace("R", "1").replace("L", "0"),2)
    seat_id = rows * 8 + columns
    print("rows:",rows)
    print("columns:", columns)
    print("seat_id:", seat_id)
    new_list.append(seat_id)
seats = sorted(new_list)


#ich erstell eine komplette liste indem ich aus der reichweite vom ersten zum letzen element eine lste erstelle  ziehe von eben dieser liste meinevorhandenen lsite ab und erhalte eine zahl die fehlt
x = set(range(seats[0], seats[-1])) - set(seats)
print(x)

print(seats)