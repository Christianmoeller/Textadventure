import all_commands
import PokemonClass
import Gamestate
import Conversations
import Story_lines



def main():
    print(Conversations.Intro)
    gs = Gamestate.Gamestate("", 0, [], "")
    gs.name = input("\"Wie lautet dein Name?\"\n>")
    print("Prof. Acai: \"Ich heisse dich Willkommen", gs.name,"\"","\n\"Mein Name ist Prof. Acai\"\n\"Um Deine Reise starten zu können, brauchst Du natürlich erstmal ein Start-Pokemon.\"\n\"Bitte wähle eines der folgenen aus:\"")
    firstpokemon = input("Schiggy-WASSER; Glumanda-FEUER, Bisasam-PFLANZE\n>")
    gs.current_pokemon = PokemonClass.startpokemon(firstpokemon)
    #startPokemon = PokemonClass.startpokemon(firstpokemon)
    while True:
        print(">>>Hauptmenü<<<")
        new_user_input = input("Was willst du tun?\nKämpfen ---> Kämpfe gegen ein zufälliges Pokemon\nPokecenter ---> Heilt Dein Pokemon\nStats ---> Infos über Dein Pokemon\nGeld ---> Dein Kontostand\n>").lower().split(" ")
        if new_user_input[0].lower() in all_commands.new_Commands:
            all_commands.new_Commands[new_user_input[0]](gs)
main()