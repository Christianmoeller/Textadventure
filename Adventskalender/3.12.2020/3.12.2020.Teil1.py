def tree_counter(down, right, map):
    tree = 0
    position_x = 0
    for line in range(0, len(map), down):
        if map[line][position_x] == "#":
            tree += 1
        position_x = (position_x + right) % len(map[0])
    return tree
f = open("3.12.2020source.txt")

biome = [line.replace("\n", "") for line in f]

firstright = 1
firstdown = 1

secondright = 3 # bereits erledigt
seconddown = 1  #bereits erledigt

thirdright = 5
thirddown = 1

fouthright = 7
fourthdown = 1

fifthright = 1
fifthdown = 2




w =(tree_counter(seconddown, secondright, biome ))
v = (tree_counter(firstdown, firstright, biome ))
x = (tree_counter(thirddown, thirdright, biome ))
y = (tree_counter(fourthdown, fouthright, biome ))
z = (tree_counter(fifthdown, fifthright, biome ))

print(v*w*x*z*y)