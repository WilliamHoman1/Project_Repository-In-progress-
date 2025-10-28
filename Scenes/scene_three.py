import player
import game_engine
from Intruder import Intruder
import threading


def input_with_timeout(prompt, timeout=5):
    """Gives user a time limit to make a decision"""
    result = [None]

    def ask():
        result[0] = input(prompt).strip().lower()

    thread = threading.Thread(target=ask)  #Runs the ask() function.
    thread.daemon = True  #Will automatically close when main program exits.
    thread.start()
    thread.join(timeout)  #Wait for the program to finish and then closes after
    return result[0]  #Stores the user input within the time limit.


def scene_three(current_player, intruder):
    """Scene Three."""
    print("\n---- Scene Three ----")

    print("""
You slam the door from behind you. Your heart is racing. But most importantly, you are alive. 
What am I going to do? What am I going to do? questions rapidly fly in your mind. The rain pours harder 
and you hear the creak of the stairs. Footsteps.""")
    choice = input("\nWant to check inventory (y/n):").strip().lower()
    if choice == "y":
        current_player.show_inventory()
        input("\nPress enter to continue...")
    else:
        input("\nAre you ready? Press Enter to continue... ")

    match current_player.last_action:
        case "attack":
            original_weapon = current_player.inventory[-1]
            print("\n As you panic looking for anything to help you, you spot three different items. ")
            item_choice = input(
                "Pick up fork from bowl, mini flag, or pen? (Bowl, Mini Flag, or Pen): ").strip().lower()
            if item_choice in ("bowl", "mini flag", "pen"):
                current_player.add_item(item_choice.title())
                print(f"\nYou picked up the {item_choice}. Suddenly the intruder bursts in!")
                print("There is no running, you two lock eyes.")
                attack_choice = input(f"\nUse {item_choice.title()} or {original_weapon}: ").strip().lower()
                if attack_choice.strip().lower() in (item_choice.lower(), original_weapon.lower()):
                    print("You land a hit!")
                    intruder.take_damage(10)
                    print("\nThe intruder lunges back at you and swings his sledgehammer, grazing your shoulder!")
                    current_player.take_damage(10)
                else:
                    print("You missed!")

                go_again = input_with_timeout(
                    "\nQuick!! You have 10 seconds! Go for another hit while you have him injured? (y/n):", timeout=10)
                if go_again == "y":
                    print("You strike again!")
                    intruder.take_damage(10)
                elif go_again == "n":
                    print("\nYou step back to catch your breath.")
                else:
                    print("\n You froze too long... its over.")
                    current_player.die()
            else:
                print(f"You froze but you still have your {original_weapon}.")

        case "y":
            print("\ny")
        case "n":
            print("\nn")
        case "escape":
            print("\nescape")
        case "run":
            print("\nrun")
        case "stealth":
            print("\nstealth")
        case _:
            print("N/a")
