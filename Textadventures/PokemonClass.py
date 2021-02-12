import random
import Attack_list


def startpokemon(choosen):
    done = True
    while done:
        if choosen.lower() == "schiggy" or choosen.lower() == "wasser":
            print(
                "Prof. Acai: \"Beeindruckend! Du hast dich für Schiggy entschieden. Das WASSER-Pokemon.\"\n\"Was DAS zu bedeuten hat, musst du selber herausfinden.\"\n")
            done = False
            Schiggy = PokemonClass("Schiggy", "Wasser", 50, 50, 10, 1, 0, 100, 50,
                                   [Attack_list.Tackle, Attack_list.Water_Gun])
            return Schiggy

        elif choosen.lower() == "glumanda" or choosen.lower() == "feuer":
            print(
                "Prof. Acai: \"Sehr schön! Du hast dich für Glumanda entschieden. Das FEUER-Pokemon.\"\n\"Was DAS zu bedeuten hat, musst du selber herausfinden.\"\n")
            done = False
            Glumanda = PokemonClass("Glumanda", "Feuer", 50, 50, 10, 1, 0, 100, 50,
                                    [Attack_list.Tackle, Attack_list.Ember])
            return Glumanda

        elif choosen.lower() == "bisasam" or choosen.lower() == "pflanze":
            print(
                "Prof. Acai: \"Yeah! Du hast dich für Bisasam entschieden. Das PFLANZEN-Pokemon.\"\n\"Was DAS zu bedeuten hat, musst du selber herausfinden.\"\n")
            done = False
            Bisasam = PokemonClass("Bisasam", "Pflanze", 50, 50, 10, 1, 0, 100, 50,
                                   [Attack_list.Tackle, Attack_list.Scratch])
            return Bisasam
        elif choosen.lower() == "pikatchu" or choosen.lower() == "elecktro":
            print(
                "Prof. Acai: \"Ähm ja das Pokemon da drüben ist ein Pikatchu. Aber es ist nicht gut auf Menschen zu sprechen!\"\n...\n\"Was du bist kein Mensch und du willst es umbedingt haben?\"\n\"Nagut das Herz will was das Herz will.\"\n\"Es ist ein ELEKTO-Pokemon. Was DAS bedeutet musst du selber herausfinden.\"\n")
            done = False
            Pikatchu = PokemonClass("Pikatchu", "Elecktro", 60, 60, 15, 1, 0, 100, 50,
                                    [Attack_list.Tackle, Attack_list.Thunder_Bolt])
            return Pikatchu
        else:
            choosen = input("Du musst ein verfügbares Pokemon auswählen\n")


class PokemonClass:
    def __init__(self, Name, Type, Hp_Current, Hp_Max, Dmg, Level, Current_ep, Needed_ep, Ep_at_defeated_level1,
                 Attacklist):
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
        self.Attacklist = Attacklist


# ein wert den jedes pokemon bekommt das eina deres pokemon besieht hat der auf den current ep wert addiert wird
# ein level sysstem das ab einem bestimmten level sogar vill entwickeln lässt
# eine berechnung die jedes pokemon beim instanziiren durchlebt, die alle werte berechent abhängig von ihrem level


def fire_pokemon():
    Glumanda = PokemonClass("Glumanda", "Feuer", 50, 50, 10, 1, 0, 100, 10, [Attack_list.Scratch, Attack_list.Ember])
    Glutexo = PokemonClass("Glutexo", "Feuer", 75, 75, 20, 1, 0, 1500, 20,
                           [Attack_list.Scratch, Attack_list.Bite, Attack_list.Ember])
    Glurak = PokemonClass("Glurak", "Feuer", 100, 100, 40, 1, 0, 4000, 30,
                          [Attack_list.Scratch, Attack_list.Bite, Attack_list.Ember, Attack_list.Flame_Thrower])
    Fukano = PokemonClass("Fukano", "Feuer", 50, 50, 12, 1, 0, 100, 10,
                          [Attack_list.Tackle, Attack_list.Bite, Attack_list.Ember])
    Arkani = PokemonClass("Arkani", "Feuer", 75, 75, 30, 1, 0, 1500, 20,
                          [Attack_list.Tackle, Attack_list.Bite, Attack_list.Ember, Attack_list.Flame_Thrower])
    Vulpix = PokemonClass("Vulpix", "Feuer", 50, 50, 12, 1, 0, 100, 10,
                          [Attack_list.Tackle, Attack_list.Bite, Attack_list.Ember])
    Vulnona = PokemonClass("Vulnona", "Feuer", 75, 75, 30, 1, 0, 1500, 20,
                           [Attack_list.Tackle, Attack_list.Bite, Attack_list.Ember, Attack_list.Flame_Thrower])
    Lavados = PokemonClass("Lavados", "Feuer", 150, 150, 50, 1, 0, 1000, 500,
                           [Attack_list.Gust, Attack_list.Ember, Attack_list.Flame_Thrower])
    all_fire_pokemon = [Glumanda, Glutexo, Glurak, Fukano, Arkani, Vulpix, Vulnona, Lavados]
    return all_fire_pokemon


def water_pokemon():
    Schiggy = PokemonClass("Schiggy", "Wasser", 50, 50, 10, 1, 0, 100, 10, [Attack_list.Tackle, Attack_list.Water_Gun])
    Schillok = PokemonClass("Schillok", "Wasser", 75, 75, 1, 15, 0, 1500, 20,
                            [Attack_list.Tackle, Attack_list.Water_Gun, Attack_list.Bubble_Beem])
    Turtok = PokemonClass("Turtok", "Wasser", 100, 100, 40, 1, 0, 4000, 30,
                          [Attack_list.Tackle, Attack_list.Water_Gun, Attack_list.Headbutt, Attack_list.Bubble_Beem])
    Quapsel = PokemonClass("Quapsel", "Wasser", 35, 35, 8, 1, 0, 100, 10, [Attack_list.Tackle, Attack_list.Water_Gun])
    Quaputzi = PokemonClass("Quaputzi", "Wasser", 65, 65, 1, 15, 0, 1500, 20,
                            [Attack_list.Tackle, Attack_list.Water_Gun, Attack_list.Bubble_Beem])
    Quappo = PokemonClass("Quappo", "Wasser", 80, 80, 35, 1, 0, 3600, 30,
                          [Attack_list.Tackle, Attack_list.Water_Gun, Attack_list.Headbutt, Attack_list.Bubble_Beem])
    all_water_pokemon = [Schiggy, Schillok, Turtok, Quapsel, Quaputzi, Quappo]
    return all_water_pokemon


def grass_pokemon():
    Bisasam = PokemonClass("Bisasam", "Pflanze", 50, 50, 10, 1, 0, 100, 10, [Attack_list.Tackle, Attack_list.Vine_Whip])
    Bisaknosp = PokemonClass("Bisaknosp", "Pflanze", 75, 75, 1, 1, 0, 1500, 20,
                             [Attack_list.Tackle, Attack_list.Vine_Whip, Attack_list.Mega_Drain])
    Bisaflor = PokemonClass("Bisaflor", "Pflanze", 100, 100, 40, 1, 0, 4000, 30,
                            [Attack_list.Tackle, Attack_list.Vine_Whip, Attack_list.Mega_Drain, Attack_list.Razor_Leaf])
    Knofensa = PokemonClass("Knofensa", "Pflanze", 40, 40, 10, 1, 0, 100, 10, [Attack_list.Tackle])
    Ultrigaria = PokemonClass("Ultrigaria", "Pflanze", 65, 65, 40, 1, 0, 1500, 20,
                              [Attack_list.Tackle, Attack_list.Vine_Whip])
    Sarzenia = PokemonClass("Sarzenia", "Pflanze", 90, 90, 35, 1, 0, 3600, 30,
                            [Attack_list.Tackle, Attack_list.Vine_Whip, Attack_list.Razor_Leaf])
    all_grass_pokemon = [Bisasam, Bisaknosp, Bisaflor, Knofensa, Ultrigaria, Sarzenia]
    return all_grass_pokemon


def choose_pokemon():
    all_Pokemon = [water_pokemon(), fire_pokemon(), grass_pokemon()]
    random_pokemon = random.choice(random.choice(all_Pokemon))
    level = random.randrange(1, 10)
    random_pokemon.Level = level
    random_pokemon.Hp_Current = random_pokemon.Hp_Current + (random_pokemon.Hp_Current * (level * 0.2))
    random_pokemon.Hp_Max = random_pokemon.Hp_Max + (random_pokemon.Hp_Max * (level * 0.2))
    random_pokemon.Ep_to_give = random_pokemon.Ep_to_give + (random_pokemon.Ep_to_give * (level))
    return random_pokemon
