class Wappon:
    def __init__(self,Dmg, Name, Seltenheit):
        self.Dmg = Dmg
        self.Name = Name
        self.Seltenheit = Seltenheit

#Waffen
Altes_Schwert = Wappon(10, "Altes Schwert(10)", "Häufig")
Lang_Schwert = Wappon(15, "Langschwert(15)", "Häufig")
Neues_Schwert = Wappon(20, "Neues Schwert(20)", "Normal")
Links_Schwert = Wappon(50, "Schwert von Link(50)", "Sehr selten")
Waffenliste = [Altes_Schwert, Lang_Schwert, Neues_Schwert, Links_Schwert]

class Items:
    def __init__(self, Wert, Name, Art):
        self.Wert = Wert
        self.Name = Name
        self.Art = Art

#Items wie Hp Pot
class Potion(Items):
    def __init__(self, Wert, Namen, Art):
        self.Wert = Wert
        self.Name = Namen
        self.Art = Art
Kleiner_Hp_Pot = Potion(20, "Hp Pot", "Trank")
Großer_Hp_Pot = Potion(40, "Großer Hp Pot", "Trank")

Potionliste = [Kleiner_Hp_Pot, Großer_Hp_Pot]

class Armor(Items):
    def __init__(self, Wert, Name, Art, Slot):
        self.Wert = Wert
        self.Name = Name
        self.Art = Art
        self.Slot = Slot
#Items die den schaden der gegner verringern
Brustplatte = Armor(20,"Brustplatte", "Rüstung", "Brust")
Helm = Armor(5, "Helm", "Rüstung", "Helm")
Hose = Armor(10, "Hose", "Rüstung", "Beine")
Rüstungsliste = [Brustplatte, Helm, Hose]
