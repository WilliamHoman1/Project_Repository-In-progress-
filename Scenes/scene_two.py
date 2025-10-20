import player
import game_engine



def scene_two(current_player):
    print("""\n---- Scene Two ----""")

    if current_player.last_action == "armed":
        print("You now have a weapon.") #Add story
        if "Kitchen Knife" in current_player.inventory:
            print(f"""You stand firm behind the counter where the smell of steak is still in the air. Clutching the knife
white-knuckled. You hear another bang but this time it is followed by a shatter. A rain of glass falls to the floor
the intruder has broken in. You start to sweat. Should I attack him? Should I wait? These questions race in your mind.

Before you can overthink, he starts walking towards the kitchen. Do you decide to attack or run?""")#What happens
        elif "Baseball Bat" in current_player.inventory:
            print(f"""You stand firm near the closet where you have sight of where the noise is coming from. Clutching the baseball bat
white-knuckled. You hear another bang but this time it is followed by a shatter. A rain of glass falls to the floor
the intruder has broken in. You start to sweat. Should I attack him? Should I wait? These questions race in your mind.

Before you can overthink, he starts walking towards the kitchen. Do you decide to attack or run?""")#What happens
        elif "Fire Poker" in current_player.inventory:
            print("""You stand firm near the fireplace, the smell of the old ashes getting stronger because of your heighten senses. Clutching 
the fire poker white-knuckled. You hear another bang but this time it is followed by a shatter. A rain of glass falls to the floor
the intruder has broken in. You start to sweat. Should I attack him? Should I wait? These questions race in your mind.

Before you can overthink, he starts walking towards the kitchen. Do you decide to attack or run?""")

    elif current_player.last_action == "hide":
        print("You hear a crash — hidden away, peering through the darkness, you see a shadow.")
        if current_player.hiding_spot == "closet":
            print("Through a sliver of light, you see the intruder pacing around. You hold your breath as he steps closer to the closet door...")
        elif current_player.hiding_spot == "under bed":
            print("Dust clings to your face as footsteps echo closer. A boot stops inches from your head. You can see his shadow moving back and forth...")
        elif current_player.hiding_spot == "behind couch":
            print("You crouch low behind the couch, trying not to breathe too loudly. Lightning flashes through the window, briefly illuminating his silhouette.")
        else:
            print("You stay hidden, unsure if the intruder has noticed you.")

        print("You hear a loud bang — glass shatters onto the floor. The intruder is inside.")

    elif current_player.last_action == "stealth":
        print("Moving silently in your new outfit, you try to stay unnoticed.")
        # Add stealth story
        # You can check inventory for 'Soft Clothes' or 'Workout Gear'
        if "Soft Clothes" in current_player.inventory:
            print("Your movements are silent. No one hears you.")
        elif "Workout Gear" in current_player.inventory:
            print("")

    elif current_player.last_action == "barricade":
        print("You barricade doors and windows, making it hard for anyone to enter.")
        if "Full Barricade" in current_player.inventory:
            print("Even with heavy pounding, the intruder can’t get in.")
        # Continue story...
    else:
        # Default story if somehow last_action isn’t set
        print("You freeze for a moment, unsure of what to do next.")

