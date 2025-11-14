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

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.defenses = []
        self.ready = False
        self.is_hiding = False
        self.hiding_spot = None
        self.is_alive = True
        self.house_status= "intact"
        self.last_action = None

    def add_item(self, item):
        self.inventory.append(item)
        print(f"\n{item} added to inventory.")
    def show_inventory(self):
        if self.inventory:
            print("You have:")
            for item in self.inventory:
                print(f" - {item}")
        else:
            print("Your inventory is empty.")
    def hide(self):
        self.is_hiding = True
        print(f"{self.name} is now hiding.")

    def add_defense(self, defense):
        self.defenses.append(defense)

    def take_damage(self, damage):
        self.health -= damage
        print(f"\n{self.name} took {damage} damage! Health is now {self.health}.")
        if self.health <= 0:
            self.is_alive = False


    def status(self):
        return f"{self.name} | Health: {self.health} | Inventory: {self.inventory}"

    def die(self, intruder = None):
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

