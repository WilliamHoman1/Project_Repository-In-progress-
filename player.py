"""This file holds the player class where all the users information is stored.
Carries on throughout multiple files. Holds different functions that can be called
at any point during the game."""

from game_engine import start_game
from ascii_art import death
from ascii_art import draw_smiley

def play_again(intruder = None):
    """Asks the player if they would like to play again."""
    choice = input("\nDo you want to play again (y/n): ").strip().lower()
    if choice == "y":
        print("\nRestarting game...\n")
        start_game()
    else:
        print("\nThank you for playing!")
        draw_smiley()
        exit()


class Player:
    """This is a player class where multiple functions can be called in various parts of the game.
    Once the player is created, it is carried over throughout the entire game."""

    def __init__(self, name):
        """The initializer method that creates the player object. Creates multiple
        empty/default variables to be modified as the game carries on."""
        self.alive = None
        self.name = name
        self.health = 100
        self.inventory = []
        self.defenses = []
        self.ready = False
        self.is_hiding = False
        self.hiding_spot = None
        self.is_alive = True
        self.last_action = None

    def add_item(self, item):
        """Function that adds an item to the inventory."""
        self.inventory.append(item)
        print(f"\n{item} added to inventory.")

    def show_inventory(self):
        """Function that shows the inventory."""
        if self.inventory:
            print("You have:")
            for item in self.inventory:
                print(f" - {item}")
        else:
            print("Your inventory is empty.")

    def hide(self):
        """Function that declares the user as hiding."""
        self.is_hiding = True
        print(f"\n{self.name} is now hiding.")

    def take_damage(self, damage):
        """Function that carries out the displaying of health after damage. Also
        takes care of the damage mechanism."""
        self.health -= damage
        print(f"\n{self.name} took {damage} damage! Health is now {self.health}.")
        if self.health <= 0:
            self.is_alive = False

    def die(self, intruder = None):
        """Function that displays when the user dies. Declares the user has failed, shows
        the users health, intruders health, and asks the player if they would like to play again."""
        self.alive = False
        self.health = 0
        death()
        print("\nYou have died.")
        print(f"Your health: {self.health}")
        if intruder:
            print(f"Intruder Health: {intruder.health}")
        choice = input("\n Do you want to play again (y/n): ").strip().lower()
        if choice == "y":
            print("\nRestarting game...\n")
            start_game()
        else:
            print("\nThank you for playing!")

