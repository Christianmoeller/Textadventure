import random

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
    def __init__(self, Wert, Name, Art, Slot, Rar):
        self.Wert = Wert
        self.Name = Name
        self.Art = Art
        self.Slot = Slot
        self.Rar = Rar

def Rüstungwahl():
    ArmorRarListen = [[armor for armor in allArmor() if armor.Rar == lvl] for lvl in range(1, 4)]
    return random.choice(random.choices(ArmorRarListen, weights=(40, 30, 20), k=1)[0])

def allArmor():
    Brustplatte = Armor(20, "Stoff Hemd", "Rüstung", "Brust", 1)
    Helm = Armor(5, "Stoff Müzte", "Rüstung", "Helm", 2)
    Hose = Armor(10, "Stoff Hose", "Rüstung", "Beine", 3)
    Leder_Brust = Armor(3, "Leder Brust", "Rüstung", "Brust", 1)
    Leder_Helm = Armor(3, "Leder Helm", "Rüstung", "Helm", 1)
    Leder_Hose = Armor(3, "Leder Hose", "Rüstung","Beine", 1)
    Eisen_Brustplatte = Armor(5, "Eisen Brustplatte", "Rüstung", "Brust", 2)
    Eisen_Helm = Armor(5, "Eisen Helm", "Rüstung", "Helm", 2)
    Eisen_Hose = Armor(5, "Eisen Hose", "Rüstung", "Beine", 2)
    Stahl_Brustplatte = Armor(9, "Stahl Brustplatte", "Rüstung", "Brust", 3)
    Stahl_Helm = Armor(9, "Stahl Helm", "Rüstung", "Helm", 3)
    Stahl_Hose = Armor(9, "Stahl Hose", "Rüstung", "Beine", 3)
    return [Brustplatte, Helm, Hose, Leder_Hose, Leder_Helm, Leder_Brust, Eisen_Brustplatte, Eisen_Hose, Eisen_Helm, Stahl_Brustplatte, Stahl_Helm, Stahl_Hose]
