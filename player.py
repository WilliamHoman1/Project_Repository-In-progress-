class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.defenses = []
        self.ready = False
        self.is_hiding = False
        self.is_alive = True

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")
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

    def status(self):
        return f"{self.name} | Health: {self.health} | Inventory: {self.inventory}"
