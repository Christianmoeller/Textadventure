class Attack():
    def __init__(self, Name, Dmg, Type, Attack_Counter_Current, Attack_Counter_Max):
        self.Name = Name
        self.Dmg = Dmg
        self.Type = Type
        self.Attack_Counter_Current = Attack_Counter_Current
        self.Attack_Counter_Max = Attack_Counter_Max



Tackle = Attack("Tackle", 10, "Normal", 20, 20)
Bite = Attack("Biss", 20, "Normal", 15, 15)
Ember = Attack("Glut", 16, "Feuer", 18, 18)
Scratch = Attack("Kratzer", 12, "Normal", 20, 20)
Water_Gun = Attack("Aquaknarre", 16, "Wasser", 18, 18)
Gust = Attack("Windstoß", "18", "Normal", 18, 18)
Bubble_Beem = Attack("Blubbstrahl", 22, "Wasser", 10, 10)
Thunder_Bolt = Attack("Donnerblitz", 16, "Elecktro", 18, 18)
Headbutt = Attack("Kopfnuss", 14, "Normal", 22, 22)
Flame_Thrower = Attack("Flammenwurf", 24, "Feuer", 10, 10)
Vine_Whip = Attack("Rankenhieb", 16, "Pflanze", 18, 18)
Mega_Drain = Attack("Mega Sauger", 15, "Pflanze", 16, 16)
Razor_Leaf = Attack("Rasierblatt", 22, "Pflanze", 10, 10)
