import player
player = player.Player("Player1")


def scene_one():
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
    main_decision()


def weapon_choice():
    """If player chooses to arm themselves."""
    print("\nYou decide to arm yourself. What weapon do you grab?")
    print("1. Kitchen Knife – quick and light.")
    print("2. Baseball Bat – reliable reach and power.")
    print("3. Fire Poker – heavy, but solid.")
    choice = input("Choose your weapon (1–3): ")

    if choice == "1":
        player.add_item("Kitchen Knife")
        print("\nYou grab a kitchen knife from the drawer — better than nothing.")
    elif choice == "2":
        player.add_item("Baseball Bat")
        print("\nYou grab your baseball bat — solid and reliable.")
    elif choice == "3":
        player.add_item("Fire Poker")
        print("\nYou snatch a fire poker from the fireplace. It feels heavy in your hand.")
    else:
        print("Invalid choice. Try again.")
    weapon_choice(player)
    player.last_action = "armed"
    print("\n You grip onto your weapon, the thunder booms as you wait... ")


def hide_choice():
    """If player chooses to hide."""
    print("\nYou decide to hide. Where do you go?")
    print("1. Closet – small and dark.")
    print("2. Under the bed – cramped but hidden.")
    print("3. Behind the couch – not ideal, but quick.")
    choice = input("Choose your hiding spot (1–3): ")

    if choice == "1":
        player.hide()
        print("\nYou squeeze into the closet, holding your breath.")
    elif choice == "2":
        player.hide()
        print("\nYou slide under the bed, praying the intruder doesn’t look down.")
    elif choice == "3":
        player.hide()
        print("\nYou duck behind the couch. The rain masks your quiet breathing.")
    else:
        print("Invalid choice. Try again.")
        hide_choice()


def stealth_clothing_choice():
    """If player chooses to change clothes for stealth."""
    print("\nYou decide to change into quieter clothing.")
    print("1. Soft clothes – quieter footsteps.")
    print("2. Workout gear – flexible and silent.")
    print("3. Keep current clothes – too risky to waste time changing.")
    choice = input("Choose your outfit (1–3): ")

    if choice == "1":
        player.add_item("Soft Clothes")
        print("\nYou slip into soft, quiet clothes — every movement makes less noise.")
    elif choice == "2":
        player.add_item("Workout Gear")
        print("\nYou throw on workout clothes — light and easy to move in.")
    elif choice == "3":
        print("\nYou decide not to change. Every second counts.")
    else:
        print("Invalid choice. Try again.")
        stealth_clothing_choice()


def barricade_choice():
    """If player chooses to barricade the house."""
    print("\nYou decide to barricade the house. Where do you start?")
    print("1. Main door – push furniture against it.")
    print("2. Windows – close curtains and block with a dresser.")
    print("3. Both – it’ll take longer, but safer.")
    choice = input("Choose 1–3: ")

    if choice == "1":
        player.add_item("Barricaded Door")
        print("\nYou block the main door with furniture — it won’t be easy to break through.")

    elif choice == "2":
        player.add_item("Barricaded Windows")
        print("\nYou move a dresser against the windows — visibility reduced, safety increased.")
    elif choice == "3":
        player.add_item("Full Barricade")
        print("\nYou block doors and windows. The place feels secure... for now.")
    else:
        print("Invalid choice. Try again.")
        barricade_choice()



def main_decision():

    """The main action prompt that branches to specific follow-ups."""
    while True:
        print(f"\nPLAYER STATUS: {player.name} | HEALTH: {player.health}")# keep looping until a valid choice triggers scene_two
        print("\nIt’s decision time. What do you want to do?")
        print("1. Arm yourself.")
        print("2. Hide.")
        print("3. Change into a stealthy outfit.")
        print("4. Barricade the house.")
        print("5. Check inventory")
        choice = input("Choose 1–5: ")

        if choice == "1":
            weapon_choice()
            break
        elif choice == "2":
            hide_choice()
            break
        elif choice == "3":
            stealth_clothing_choice()
            break
        elif choice == "4":
            barricade_choice()
            break
        elif choice == "5":
            player.show_inventory()  # show inventory but does not advance scene
        else:
            print("Invalid choice. Try again.")

    # After a valid choice (1–5), move to the next scene
    from Scenes import scene_two
    scene_two.start(player)
