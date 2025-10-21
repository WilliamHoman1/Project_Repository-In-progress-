import player
import game_engine
from Intruder import Intruder



def scene_two(current_player):
    print("""\n---- Scene Two ----""")
    intruder = Intruder()

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
        while True:
                decision = input("\nDo you want to attack? (y/n): ").strip().lower()
                if decision == "y":
                    print("\nYou charge forward, weapon raised and adrenaline flowing through your veins.")
                    print("The intruder stumbles back, caught off guard by your sudden courage.")
                    intruder.take_damage(10)
                    print("You've delivered the first blow! You run upstairs to hide.")
                    current_player.last_action = "attack"
                    break
                elif decision == "n":
                    print("\nYou decide to run upstairs you chose flight in your fight or flight response.")
                    current_player.last_action = "run"
                    #can later branch to a running/escape scene
                    break
                else:
                    print("Please type 'y' or 'n'.")

    elif current_player.last_action == "hide":
        print("You hear a crash — hidden away, peering through the darkness, you see a shadow.")
        if current_player.hiding_spot == "closet":
            print("Through a sliver of light, you see the intruder pacing around outside. He peers through the window but does not see anything. So he makes "
                  "his decision.")
        elif current_player.hiding_spot == "under bed":
            print("Dust clings to your face as you peer out looking, waiting for any more movement. You can hear your own heart pounding against your chest and onto the floor."
                  "You can see his shadow moving back and forth...")
        elif current_player.hiding_spot == "behind couch":
            print("You crouch low behind the couch, trying not to breathe too loudly. Lightning flashes through the window, briefly illuminating his silhouette.")
        else:
            print("You stay hidden, unsure if the intruder has noticed you.")

        print("You hear a loud bang — glass shatters onto the floor. The intruder is inside. Your see the kitchen knife on the table but he will see you if you "
              "decide to grab it. Stay hidden or go for the weapon?")
        while True:
            decision = input("\nDo you want to grab the knife? (y/n): ").strip().lower()
            if decision == "y":
                print("\nHeart pounding, you lunge for the knife!")
                current_player.add_item("Kitchen Knife")
                intruder.take_damage(10)
                print("You slash wildly, landing a lucky hit! The intruder howls in pain as you sprint upstairs to safety.")
                current_player.last_action = "attack"
                break
            elif decision == "n":
                print("\nYou stay perfectly still, your breath shallow.")
                print("Then you spot something small — a **foam ball** tucked beside you in the closet.")
                print("You grab it and gently toss it out into the living room.")
                print("The ball bounces softly... then rolls. The intruder turns toward the sound, momentarily distracted.")
                print("Taking your chance, you slip out, grab your phone from the kitchen counter, and bolt upstairs!")

                current_player.add_item("Phone")
                current_player.last_action = "escape"
                break
            else:
                print("Please type 'y' or 'n'.")


    elif current_player.last_action == "stealth":
        print("Moving silently in your new outfit, you try to stay unnoticed.")
        # Add stealth story
        # You can check inventory for 'Soft Clothes' or 'Workout Gear'
        if "Soft Clothes" in current_player.inventory:
            print("Your movements are silent. No one hears you. So you position yourself to escape or run to a new room for a weapon.")
        elif "Workout Gear" in current_player.inventory:
            print("You feel agile. Ready to run out of the house to save your life. But, all of your possessions will be gone. Either way, you are ready for it.")

    elif current_player.last_action == "barricade":
        print("You barricade doors and windows, making it hard for anyone to enter.")
        if "Full Barricade" in current_player.inventory:
            print("Even with heavy pounding, the intruder can’t get in. However, you remember and unlocked door from being outside earlier. Suddenly you hear it creek open."
                  "The intruder is in.")
        # Continue story...
    else:
        # Default story if somehow last_action isn’t set
        print("You freeze for a moment, unsure of what to do next.")

