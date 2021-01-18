import random
def startpokemon(choosen):
    done = True
    while done:
        if choosen.lower() == "schiggy" or choosen.lower() == "wasser":
            print("Hey du hast dich für Schiggy entschieden.\nMit Sicherheit eine gute Wahl.\n")
            done = False
            Schiggy = PokemonClass("Schiggy", "Wasser", 50, 10, 1, 0, 100)
            return Schiggy

        elif choosen.lower() == "glumanda" or choosen.lower() == "feuer":
            print("Sehr schön. Du hast dich für Glumanda entschieden.\nMit Sicherheit eine gute Wahl.\n")
            done = False
            Glumanda = PokemonClass("Glumanda", "Feuer", 50, 10, 1, 0, 100)
            return Glumanda

        elif choosen.lower() == "bisasam" or choosen.lower() == "pflanze":
            print("Du hast dich für Bisasam entschieden.\nMit Sicherheit eine gute Wahl. Du hast wohl keine Ahnung von Pokomen!\n")
            done = False
            Bisasam = PokemonClass("Bisasam", "Pflanze", 50, 10, 1, 0, 100)
            return Bisasam

        else:
            choosen =input("Du musst ein verfügbares Pokemon auswählen\n")

class PokemonClass:
    def __init__(self, Name, Type, Hp, Dmg, Level, Current_ep, Needed_ep):
        self.Name = Name
        self.Type = Type
        self.Hp = Hp
        self.Dmg = Dmg
        self.Level = Level
        self.Current_ep = Current_ep
        self.Needed_ep = Needed_ep

def fire_pokemon():
    Glumanda =  PokemonClass("Glumanda", "Feuer", 50, 10, 1, 0, 100)
    Glutexo = PokemonClass("Glutexo", "Feuer", 75, 20, 15, 0, 15000)
    Glurak = PokemonClass("Glurak", "Feuer", 100, 40, 36, 0, 40000)
    Fukano = PokemonClass("Fukano", "Feuer", 50, 12, 1, 0, 100)
    Arkani = PokemonClass("Arkani", "Feuer", 75, 30, 20, 0, 15000)
    Vulpix = PokemonClass("Vulpix", "Feuer", 50, 12, 1, 0, 100)
    Vulnona = PokemonClass("Vulnona", "Feuer", 75, 30, 20, 0, 15000)
    Lavados = PokemonClass("Lavados", "Feuer", 150, 50, 50, 0, 100000)
    all_fire_pokemon = [Glumanda, Glutexo, Glurak, Fukano, Arkani, Vulpix, Vulnona, Lavados]
    return all_fire_pokemon

def water_pokemon():
    Schiggy = PokemonClass("Schiggy", "Wasser", 50, 10, 1, 0, 100)
    Schillok = PokemonClass("Schillok", "Wasser", 75, 20, 15, 0, 15000)
    Turtok = PokemonClass("Turtok", "Wasser", 100, 40, 36, 0, 40000)
    Quapsel = PokemonClass("Quapsel", "Wasser", 35, 8, 1, 0, 100)
    Quaputzi = PokemonClass("Quaputzi", "Wasser", 65, 15, 15, 0, 15000)
    Quappo = PokemonClass("Quappo", "Wasser", 80, 35, 36, 0, 36000)
    all_water_pokemon = [Schiggy, Schillok, Turtok, Quapsel, Quaputzi, Quappo]
    return all_water_pokemon



def choose_pokemon():
    all_Pokemon = [water_pokemon(), fire_pokemon()]
    return random.choice(random.choice(all_Pokemon))