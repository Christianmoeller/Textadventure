class Wappon:
    def __init__(self,Dmg, Name, Seltenheit):
        self.Dmg = Dmg
        self.Name = Name
        self.Seltenheit = Seltenheit

class Items:
    def __init__(self, Wert, Name):
        self.Wert = Wert
        self.Name = Name

#Waffen
Altes_Schwert = Wappon(10, "Altes Schwert(10)", "Häufig")
Lang_Schwert = Wappon(15, "Langschwert(15)", "Häufig")
Neues_Schwert = Wappon(20, "Neues Schwert(20)", "Normal")
Links_Schwert = Wappon(50, "Schwert von Link(50)", "Sehr selten")
Waffenliste = [Altes_Schwert, Lang_Schwert, Neues_Schwert, Links_Schwert]

#Items wie Hp Pot
Kleiner_Hp_Pot = Items(20, "Hp Pot")
Großer_Hp_Pot = Items(40, "Großer Hp Pot")
