def startpokemon(choosen):
    done = True
    while done:
        if choosen == "Schiggy".lower():
            print("Hey du hast dich für Schiggy entschieden.\nMit Sicherheit eine gute Wahl.")
            done = False
        elif choosen == "Glumanda".lower():
            print("Sehr schön. Du hast dich für Glumanda entschieden.\nMit Sicherheit eine gute Wahl.")
            done = False
        elif choosen == "Bisasam".lower():
            print("Du hast dich für Bisasam entschieden.\nMit Sicherheit eine gute Wahl.")
            done = False
        else:
            choosen =input("Du musst ein verfügbares Pokemon auswählen\n")

class Pokemon:
    def __init__(self, Name, Type, Hp, Dmg, Level, Current_ep, Needed_ep):
        self.Name = Name
        self.Type = Type
        self.Hp = Hp
        self.Dmg = Dmg
        self.Level = Level
        self.Current_ep = Current_ep
        self.Needed_ep = Needed_ep

def fire_pokemon():
    Glumanda =  Pokemon("Glumanda", "Feuer", 50, 10, 1, 0, 100)
    Glutexo = Pokemon("Glutexo", "Feuer", 75, 20, 15, 0, 15000)
    Glurak = Pokemon("Glurak", "Feuer", 100, 40, 36, 0, 40000)
    Fukano = Pokemon("Fukano", "Feuer", 50, 12, 1, 0, 100)
    Arkani = Pokemon("Arkani", "Feuer", 75, 30, 20, 0, 15000)
    Vulpix = Pokemon("Vulpix", "Feuer", 50, 12, 1, 0, 100)
    Vulnona = Pokemon("Vulnona", "Feuer", 75, 30, 20, 0, 15000)
    Lavados = Pokemon("Lavados","Feuer", 150, 50, 50, 0, 100000)
    all_fire_pokemon = [Glumanda, Glutexo, Glurak, Fukano, Arkani, Vulpix, Vulnona, Lavados]

def water_pokemon():
    Schiggy = Pokemon("Schiggy", "Wasser", 50, 10, 1, 0 ,100)
    Schillok = Pokemon("Schillok", "Wasser", 75, 20, 15, 0, 15000)
    Turtok = Pokemon("Turtok", "Wasser", 100, 40, 36, 0, 40000)
    Quapsel = Pokemon("Quapsel", "Wasser", 35, 8, 1, 0, 100)
    Quaputzi = Pokemon("Quaputzi", "Wasser", 65, 15, 15, 0 ,15000)
    Quappo = Pokemon("Quappo", "Wasser", 80, 35, 36, 0, 36000)
    all_water_pokemon = [Schiggy, Schillok, Turtok, Quapsel, Quaputzi, Quappo]

