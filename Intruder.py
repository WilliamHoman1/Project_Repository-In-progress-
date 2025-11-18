
class Intruder:
    """This class sets up the default intruder that the player will be defending against.
    The intruder is carried throughout the game and its attributes (health) are updated throughout the game."""
    def __init__(self, name= "Intruder", health = 100, damage = 10):
        self.name = name
        self.health = 100
        self.inventory = []

    def take_damage(self, amount):
        """This function contains the mechanics for the intruder taking
        damage."""
        self.health -= amount
        print(f"\n{self.name} takes {amount} damage! Intruder Health: {self.health}")
        if self.health <= 0:
            print("You creep closer to get a better look, hes non responsive but still alive. The cops finally arrive and take him away."
                  "You've done it. Your home is safe.")

