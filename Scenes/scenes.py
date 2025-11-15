from ascii_art import shirt
from ascii_art import weapon
from ascii_art import hiding

def scene_one(current_player):
    """First scene the player will go through, backstory and set up of the
    story line."""
    print("""\nOn a cloudy Thursday night, you are home alone, preparing to make dinner 
while throwing your favorite show on the T.V. You bring out the ingredients, seasonings,
utensils and everything you need to make yourself a steak dinner. A treat to nourish your
body from working all the day long. You go into the pantry to grab some paper towels to
pat down the steak. 
\nSuddenly, BANG! BANG! BANG!, you are freighted, but it is only the sound of thunder. A 
downpour has started. Relieved you begin cooking the steak as the thunder and lightning
roll on. Time passes. The food is done and you sit down to eat. Suddenly. \n
BANG! BANG! BANG! again. You look towards the window only to find a silhouette of a man
prying at your door. You think to yourself, what do i do? Am I getting robed? Am I going
to die???""")
    main_decision(current_player)


def weapon_choice(current_player):
    """If player chooses to arm themselves. Faced with another option screen."""
    weapon()
    print("\nYou decide to arm yourself. What weapon do you grab?")
    print("1. Kitchen Knife – quick and light.")
    print("2. Baseball Bat – reliable reach and power.")
    print("3. Fire Poker – heavy, but solid.")
    choice = input("Choose your weapon (1–3): ")

    if choice == "1":
        current_player.add_item("Kitchen Knife")
        print("\nYou grab a kitchen knife from the drawer — better than nothing.")
    elif choice == "2":
        current_player.add_item("Baseball Bat")
        print("\nYou grab your baseball bat — solid and reliable.")
    elif choice == "3":
        current_player.add_item("Fire Poker")
        print("\nYou snatch a fire poker from the fireplace. It feels heavy in your hand.")
    else:
        print("Invalid choice. Try again.")
        return False
    current_player.last_action = "armed"
    print("\n You grip onto your weapon, the thunder booms as you wait... ")
    return True

def hide_choice(current_player):
    """If player chooses to hide. Faced with another option screen."""
    hiding()
    print("\nYou decide to hide. Where do you go?")
    print("1. Closet – small and dark.")
    print("2. Under the kitchen island – cramped but hidden.")
    print("3. Behind the couch – not ideal, but quick.")
    choice = input("Choose your hiding spot (1–3): ")

    if choice == "1":
        current_player.hide()
        current_player.hiding_spot = "closet"
        current_player.last_action = "hide"
        print("\nYou squeeze into the closet, holding your breath.")
        return True
    elif choice == "2":
        current_player.hide()
        current_player.hiding_spot = "kitchen island"
        current_player.last_action = "hide"
        print("\nYou slide under the island, praying the intruder doesn’t look under the countertops.")
        return True
    elif choice == "3":
        current_player.hide()
        current_player.hiding_spot = "behind couch"
        current_player.last_action = "hide"
        print("\nYou duck behind the couch. The rain masks your quiet breathing.")
        return True
    else:
        print("Invalid choice. Try again.")
        return False


def stealth_clothing_choice(current_player):
    """If player chooses to change clothes for stealth. Faced with another option screen."""
    shirt()
    print("\nYou decide to change into quieter clothing.")
    print("1. Soft clothes – quieter footsteps.")
    print("2. Workout gear – flexible and silent.")
    print("3. Keep current clothes – too risky to waste time changing.")
    choice = input("Choose your outfit (1–3): ")

    if choice == "1":
        current_player.add_item("Soft Clothes")
        current_player.last_action = "stealth"
        print("\nYou slip into soft, quiet clothes — every movement makes less noise.")
        return True
    elif choice == "2":
        current_player.add_item("Workout Gear")
        current_player.last_action = "stealth"
        print("\nYou throw on workout clothes — light and easy to move in.")
        return True
    elif choice == "3":
        current_player.add_item("Keep current clothes")
        current_player.last_action = "stealth"
        print("\nYou decide not to change. Every second counts.")
        return True
    else:
        print("Invalid choice. Try again.")
        return False


def barricade_choice(current_player):
    """If player chooses to barricade the house. Faced with another option screen."""
    print("\nYou decide to barricade the house. Where do you start?")
    print("1. Main door – push furniture against it.")
    print("2. Windows – close curtains and block with a dresser.")
    print("3. Both – it’ll take longer, but safer.")
    choice = input("Choose 1–3: ")

    if choice == "1":
        current_player.add_item("Barricaded Door")
        print("\nYou block the main door with furniture — it won’t be easy to break through.")
    elif choice == "2":
        current_player.add_item("Barricaded Windows")
        print("\nYou move a dresser against the windows — visibility reduced, safety increased.")
    elif choice == "3":
        current_player.add_item("Full Barricade")
        print("\nYou block doors and windows. The place feels secure... for now.")
    else:
        print("Invalid choice. Try again.")
        barricade_choice(current_player)

    current_player.last_action = "barricade"
    print("\nYou brace yourself, heart pounding louder.")
    return True



def main_decision(current_player):
    """The main action prompt that branches to specific follow-ups."""
    while True:
        print(f"\nPLAYER STATUS: {current_player.name} | HEALTH: {current_player.health}")# keep looping until a valid choice triggers scene_two
        print("\nIt’s decision time. What do you want to do?")
        print("1. Arm yourself.")
        print("2. Hide.")
        print("3. Change into a stealthy outfit.")
        print("4. Barricade the house.")
        print("5. Check inventory")
        choice = input("Choose 1–5: ")

        valid_choice = True

        if choice == "1":
            valid_choice = weapon_choice(current_player)
        elif choice == "2":
            valid_choice = hide_choice(current_player)
        elif choice == "3":
            valid_choice = stealth_clothing_choice(current_player)
        elif choice == "4":
            valid_choice = barricade_choice(current_player)
        elif choice == "5":
            current_player.show_inventory() #Show inventory but does not advance scene
            valid_choice = False
        else:
            print("Invalid choice. Try again.")
            valid_choice = False
        if valid_choice:
            break

    # After a valid choice (1–5), move to the next  scene
    from Scenes import scene_two
    from Intruder import Intruder

    intruder = Intruder()
    scene_two.scene_two(current_player, intruder)
