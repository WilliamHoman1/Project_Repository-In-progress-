from Scenes import scenes
import player

def start_game():
    """The start of the game, description and welcome message.
    """
    name = (input ("WELCOME TO SAFEHOME SYSTEM, PLEASE ENTER YOUR NAME: " ))
    current_player = player.Player(name)
    welcome_message = (f" Welcome {current_player.name}, to the SafeHome defense system. This will be\n"
                       f"a true test of your skills and will power. Make the right choices and\n "
                       f"you will live to see another day, make a mistake, and that could be\n"
                       f"the end for you. I wish you the best! Be smart and make sure you\n"
                       f"think. Good luck {current_player.name}!")
    print(welcome_message)

    input("\n Press Enter to continue...")
    scenes.scene_one(current_player)



