from Scenes import scenes
import player
from ascii_art import draw_ascii_house
from ascii_art import draw_smiley
from music import game_music

def start_game():
    """The introduction screen and welcome message of the game.
    """
    draw_smiley()
    game_music.music()
    name = (input ("WELCOME TO SAFEHOME SYSTEM, PLEASE ENTER YOUR NAME: " ))
    current_player = player.Player(name)
    welcome_message = (f" Welcome {current_player.name}, to the SafeHome defense system. This will be\n"
                       f"a true test of your skills and will power. Make the right choices and\n "
                       f"you will live to see another day, make a mistake, and that could be\n"
                       f"the end for you. I wish you the best! Be smart and make sure you\n"
                       f"think. Good luck {current_player.name}!")
    print(welcome_message)
    draw_ascii_house()

    input("\n Press Enter to continue...")
    scenes.scene_one(current_player)



