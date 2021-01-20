
class Attack():
    def __init__(self, Name, Dmg, Type, Anzahl):
        self.Name = Name
        self.Dmg = Dmg
        self.Type = Type
        self.Anzahl = Anzahl


Tackle = Attack("Tackle", 10, "Normal", 20)
Bite = Attack("Biss", 20, "Normal", 15)
Ember = Attack("Glut", 16, "Feuer", 18)
Scratch = Attack("Kratzer", 12, "Normal", 20)
Water_Gun = Attack("Aquaknarre", 16, "Wasser", 18)
Gust = Attack("Windstoß", "18", "Normal", 18)
Bubble_Beem = Attack("Blubbstrahl", 22, "Wasser", 10)
Thunder_Bolt = Attack("Donnerblitz", 16, "Elecktro", 18)
Headbutt = Attack("Kopfnuss", 14, "Normal", 22)
Flame_Thrower = Attack("Flammenwurf", 24, "Feuer", 10)
