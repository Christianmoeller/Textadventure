import random
def startpokemon(choosen):
    done = True
    while done:
        if choosen.lower() == "schiggy" or choosen.lower() == "wasser":
            print("Hey du hast dich für Schiggy entschieden.\nMit Sicherheit eine gute Wahl.\n")
            done = False
            Schiggy = PokemonClass("Schiggy", "Wasser", 50, 50, 10, 1, 0, 100, 50)
            return Schiggy

        elif choosen.lower() == "glumanda" or choosen.lower() == "feuer":
            print("Sehr schön. Du hast dich für Glumanda entschieden.\nMit Sicherheit eine gute Wahl.\n")
            done = False
            Glumanda = PokemonClass("Glumanda", "Feuer", 50, 50, 10, 1, 0, 100, 50)
            return Glumanda

        elif choosen.lower() == "bisasam" or choosen.lower() == "pflanze":
            print("Du hast dich für Bisasam entschieden.\nMit Sicherheit eine gute Wahl. Du hast wohl keine Ahnung von Pokomen!\n")
            done = False
            Bisasam = PokemonClass("Bisasam", "Pflanze", 50, 50, 10, 1, 0, 100, 50)
            return Bisasam

        else:
            choosen =input("Du musst ein verfügbares Pokemon auswählen\n")

class PokemonClass:
    def __init__(self, Name, Type, Hp_Current, Hp_Max, Dmg, Level, Current_ep, Needed_ep, Ep_at_defeated_level1):
        self.Name = Name
        self.Type = Type
        self.Hp_Current = Hp_Current
        self.Hp_Max = Hp_Max
        self.Dmg = Dmg
        self.Level = Level
        self.Current_ep = Current_ep
        self.Needed_ep = Needed_ep
        self.Ep_at_defeated_level1 = Ep_at_defeated_level1
        self.Ep_to_give = Ep_at_defeated_level1


#ein wert den jedes pokemon bekommt das eina deres pokemon besieht hat der auf den current ep wert addiert wird
#ein level sysstem das ab einem bestimmten level sogar vill entwickeln lässt
#eine berechnung die jedes pokemon beim instanziiren durchlebt, die alle werte berechent abhängig von ihrem level



def fire_pokemon():
    Glumanda =  PokemonClass("Glumanda", "Feuer", 50, 50, 10, 1, 0, 100, 50)
    Glutexo = PokemonClass("Glutexo", "Feuer", 75, 75, 20, 15, 0, 15000, 100)
    Glurak = PokemonClass("Glurak", "Feuer", 100, 100, 40, 36, 0, 40000, 1000)
    Fukano = PokemonClass("Fukano", "Feuer", 50, 50, 12, 1, 0, 100, 70)
    Arkani = PokemonClass("Arkani", "Feuer", 75, 75,  30, 20, 0, 15000, 150)
    Vulpix = PokemonClass("Vulpix", "Feuer", 50, 50, 12, 1, 0, 100, 70)
    Vulnona = PokemonClass("Vulnona", "Feuer", 75, 75, 30, 20, 0, 15000, 150)
    Lavados = PokemonClass("Lavados", "Feuer", 150, 150, 50, 50, 0, 100000, 5000)
    all_fire_pokemon = [Glumanda, Glutexo, Glurak, Fukano, Arkani, Vulpix, Vulnona, Lavados]
    return all_fire_pokemon

def water_pokemon():
    Schiggy = PokemonClass("Schiggy", "Wasser", 50, 50, 10, 1, 0, 100, 50)
    Schillok = PokemonClass("Schillok", "Wasser", 75, 75,  20, 15, 0, 15000, 100)
    Turtok = PokemonClass("Turtok", "Wasser", 100, 100, 40, 36, 0, 40000, 1000)
    Quapsel = PokemonClass("Quapsel", "Wasser", 35, 35,  8, 1, 0, 100,50)
    Quaputzi = PokemonClass("Quaputzi", "Wasser", 65, 65,  15, 15, 0, 15000, 100)
    Quappo = PokemonClass("Quappo", "Wasser", 80, 80, 35, 36, 0, 36000, 1000)
    all_water_pokemon = [Schiggy, Schillok, Turtok, Quapsel, Quaputzi, Quappo]
    return all_water_pokemon



def choose_pokemon():
    all_Pokemon = [water_pokemon(), fire_pokemon()]
    random_pokemon = random.choice(random.choice(all_Pokemon))
    level =random.randrange(1,10)
    random_pokemon.Level = level
    random_pokemon.Hp_Current = random_pokemon.Hp_Current + (random_pokemon.Hp_Current * (level*0.2))
    random_pokemon.Hp_Max = random_pokemon.Hp_Max + (random_pokemon.Hp_Max * (level * 0.2))
    random_pokemon.Ep_to_give = random_pokemon.Ep_to_give + (random_pokemon.Ep_to_give*(level/2))
    return random_pokemon