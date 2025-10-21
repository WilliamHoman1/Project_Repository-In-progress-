
class Intruder:
    def __init__(self, name= "Intruder", health = 100, damage = 10):
        self.name = name
        self.health = 100
        self.inventory = []
        self.last_action = None
        self.hiding_spot = None

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! Intruder Health: {self.health}")
        if self.health <= 0:
            print("You creep closer to get a better look, hes non responsive but still alive. The cops finally arrive and take him away."
                  "You've done it. Your home is safe.")

