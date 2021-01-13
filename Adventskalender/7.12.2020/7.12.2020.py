def parts_to_colors(color_part):
    color_strings = color_part.split(", ")
    listofcolor = []
    for colorstring in color_strings:
        colorstringparts = colorstring.split()
        color = colorstringparts[1] + " "+ colorstringparts[2]
        listofcolor.append(color)
    return listofcolor

def tuple_rule(maincolor, secondcolors):
    listoftuple = []
    for color in secondcolors:
        tuple = (maincolor, color)
        listoftuple.append(tuple)
    return listoftuple

def get_cointaining (rule_liste, find_color):
    colorliste  = []
    for color in rule_liste:
        if color[1] == find_color:
            colorliste.append(color[0])
    return colorliste


def main():

    with open("7.12.2020 input") as f:
        f = f.readlines()
    rules = []
    for line in f:
        parts = line.split(" bags contain ")
        maincolor = parts[0]

        colors = parts_to_colors(parts[1])
        rules = rules + (tuple_rule(maincolor, colors))
    print(rules)
    get_cointaining(rules, "shiny gold")


main()