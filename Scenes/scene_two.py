
from ascii_art import staircase
from ascii_art import running_upstairs

def scene_two(current_player, intruder):
    """The second scene of the game. Continues the game based off the players decisions
    from scene one. Each decision they make has a slightly different story line. Making it unique
    to the user and giving them more customization to how their journey goes.

    Multiple (while) loops have been used to make sure the scene does not move on until the user picks
     a correct input."""
    print("""\n---- Scene Two ----""")



    if current_player.last_action == "armed":
    #If the player choose to arm themselves. Based on the decision they made previously of specifically what weapon they chose,
    #a slightly different story line will play. Faced with multiple decisions as well.

        print("You now have a weapon.")
        if "Kitchen Knife" in current_player.inventory:
            print(f"""You stand firm behind the counter where the smell of steak is still in the air. Clutching the knife
white-knuckled. You hear another bang but this time it is followed by a  💥. A rain of glass falls to the floor
the intruder has broken in with a sledgehammer 🔨. You start to sweat. Should I attack him? Should I wait? These questions race in your mind.

Before you can overthink, he starts walking towards the kitchen. Do you decide to attack or run?""")  #What happens
        elif "Baseball Bat" in current_player.inventory:
            print(f"""You stand firm near the closet where you have sight of where the noise is coming from. Clutching the baseball bat
white-knuckled. You hear another bang but this time it is followed by a shatter 💥. A rain of glass falls to the floor
the intruder has broken in with a sledgehammer 🔨. You start to sweat. Should I attack him? Should I wait? These questions race in your mind.

Before you can overthink, he starts walking towards the kitchen. Do you decide to attack or run?""")  #What happens
        elif "Fire Poker" in current_player.inventory:
            print("""You stand firm near the fireplace, the smell of the old ashes getting stronger because of your heightened senses. Clutching 
the fire poker white-knuckled. You hear another bang but this time it is followed by a shatter 💥. A rain of glass falls to the floor
the intruder has broken in with a sledgehammer 🔨. You start to sweat. Should I attack him? Should I wait? These questions race in your mind.

Before you can overthink, he starts walking towards the kitchen. You can either attack or run.""")
        while True:
            decision = input("\nDo you want to attack? (y/n): ").strip().lower()
            if decision == "y":
                print("\nYou charge forward, weapon raised and adrenaline flowing through your veins.")
                print("The intruder stumbles back, caught off guard by your sudden courage.")
                intruder.take_damage(10)
                running_upstairs()
                print("\nYou've delivered the first blow! You run upstairs to hide.")
                current_player.last_action = "attack"
                scene_three.scene_three(current_player, intruder)
                break
            elif decision == "n":
                running_upstairs()
                print("\nYou decide to run upstairs you chose flight in your fight or flight response.")
                current_player.last_action = "run"
                scene_three.scene_three(current_player, intruder)
                break
            else:
                print("Please type 'y' or 'n'.")

    elif current_player.last_action == "hide":
    #If the player is currently hiding, goes through if,elif, and else statements based on the different locations the user could
    #be. Changes the story line based on that information.

        print("\nYou hear a crash — hidden away, peering through the darkness, you see a shadow.")
        if current_player.hiding_spot == "closet":
            print(
                "Through a sliver of light, you see the intruder pacing around outside. He peers through the window but does not see anything. So he makes "
                "his decision.")
        elif current_player.hiding_spot == "kitchen island":
            print(
                "Shadows cover your face as you peer out looking, waiting for any more movement. You can hear your own heart pounding against your chest. "
                "\nYou can see his shadow moving back and forth...")
        elif current_player.hiding_spot == "behind couch":
            print(
                "You crouch low behind the couch, trying not to breathe too loudly. Lightning flashes through the window, briefly illuminating his silhouette.")
        else:
            print("You stay hidden, unsure if the intruder has noticed you.")

        print(
            "You hear a loud bang  💥 — glass shatters onto the floor. The intruder is inside. He has a sledgehammer 🔨. You see the kitchen knife on the table but he will "
            "\nsee you if you decide to grab it. Stay hidden or go for the weapon?")
        while True:
            decision = input("\nDo you want to grab the knife? (y/n): ").strip().lower()
            if decision == "y":
                print("\nHeart pounding, you lunge for the knife!")
                print("\nYou come out of your hiding spot!")
                current_player.add_item("Kitchen Knife")
                print(
                    "The intruder is off guard. You take your chance. You slash wildly, landing a lucky hit! "
                    "\nThe intruder howls in pain as you sprint upstairs to safety.")
                running_upstairs()
                intruder.take_damage(20)
                current_player.last_action = "attack"
                input ("Press enter to continue...")
                scene_three.scene_three(current_player, intruder)
                break
            elif decision == "n":
                print("\nYou stay perfectly still, your breath shallow.")
                print("Then you spot something small — a foam ball from playing catch with friends earlier.")
                print("You grab it and gently toss it out into the living room.")
                print(
                    "The ball bounces softly... then rolls. The intruder turns toward the sound, momentarily distracted.")
                print("Taking your chance, you slip out, grab your phone from the kitchen counter, and bolt upstairs!")
                input ("\nPress enter to continue...")
                current_player.add_item("Phone")
                current_player.last_action = "escape"
                scene_three.scene_three(current_player, intruder)
                break
            else:
                print("Please type 'y' or 'n'.")


    elif current_player.last_action == "stealth":
    #If the player choose to change outfits. Each if,elif, and else statement is based on what the user decided to wear and plays
    #a different story based on that.
        print("\nMoving silently in your outfit, you try to stay unnoticed.")
        if "Soft Clothes" in current_player.inventory:
            print(
                "Your movements are silent. No one hears you. So you position yourself to escape or run to a new room for a weapon. "
                "\nHowever, you hear glass shatter  💥 to a million pieces and the intruder is in. He has a sledgehammer 🔨.")
            while True:
                staircase()
                choice = input("Do you sneak upstairs? (y/n): ").strip().lower()
                if choice == "y":
                    running_upstairs()
                    current_player.location = "upstairs"
                    scene_three.scene_three(current_player, intruder)
                    break
                elif choice == "n":
                    print("You stay put, hidden, but the intruder draws closer")
                    current_player.location = "downstairs"
                    current_player.last_action = "downstairs"
                    scene_three.scene_three(current_player, intruder)
                    break
                else:
                    print("Please type 'y' or 'n'.")

        elif "Workout Gear" in current_player.inventory:
        #If the user previously chose to change into workout gear. This branch will play as well as the story line. Used
        #if, elif, and else statements here.
            print(
                "You feel agile. Ready to run out of the house to save your life. But, all of your possessions will be gone. Either way, you are ready for it. "
                "\nYou hear the intruder break the lock on the door with a sledgehammer 🔨, he's in. But, he does not know where you are.")
            while True:
                choice = input("Do you run upstairs quickly to buy more time? (y/n): ").strip().lower()
                if choice == "y":
                    current_player.location = "upstairs"
                    running_upstairs()
                    print(
                        "You sprint upstairs out of the main floor to create distance. You remember you have your phone in your pocket.")
                    scene_three.scene_three(current_player, intruder)
                    break
                elif choice == "n":
                    print("\nYou stay put, hidden, but the intruder draws closer")
                    print("\nYou find yourself ducking behind the kitchen countertops looking out for him.")
                    print("You seem him stepping through the broken door.")
                    while True:
                        choice = input ("Charge at him or sneak upstairs while you still can? (charge/sneak): ").strip().lower()
                        if choice == "charge":
                            print(f"""\nYou did not have a weapon and he did. He overpowers you.""")
                            current_player.die()
                            break
                        elif choice == "sneak":
                            print(f"""You sneak away to the upstairs floor. He did not notice you. You are still alive.""")
                            scene_three.scene_three(current_player, intruder)
                            current_player.location = "downstairs"
                            break
                        else:
                            print ("Please type 'charge' or 'sneak'.")
                    break
                else:
                    print("Please type 'y' or 'n'.")

        elif "Keep current clothes" in current_player.inventory:
        #If the user chose to keep their current clothes, this branch will play.

            print("Saving time, you sit waiting for the next move. After watching every move of the man outside. He starts to barge through the door. "
                  "\nBANG! 💥 He breaks through with a sledgehammer 🔨.")
            while True:
                staircase()
                choice = input("Sneak upstairs? (y/n): ").strip().lower()
                if choice == "y":
                    running_upstairs()
                    current_player.location = "upstairs"
                    print("Your now upstairs and remember you have your phone!")
                    current_player.add_item("Phone")
                    scene_three.scene_three(current_player, intruder)
                    break
                elif choice == "n":
                    print("You stay put, hidden, but the intruder draws closer")
                    print("\nYou move to under the desk in the office.")
                    print("The intruder steps in through the broken window and you can hear the glass crunch.")
                    while True:
                        choice = input(
                            "\nYou now need to act. You find a piece of paper. Crumple it up and throw it to make"
                            "\nsound while you run for it? Or wait for him to pass and go hide somewhere else?"
                            "\n(wait/throw): ").strip().lower()
                        if choice == "wait":
                            print("\nNice! You made the right decision. The intruder passes and you make your way out.")
                            current_player.location = "downstairs"
                            current_player.last_action = "downstairs"
                            current_player.hiding_spot = "not upstairs"
                            scene_three.scene_three(current_player, intruder)
                        elif choice == "throw":
                            print(
                                "\nThe intruder hears you crumple up the paper. He rushes over and uses the sledgehammer.")
                            print("All you see is darkness...")
                            current_player.die()
                        else:
                            print("Please type 'wait' or 'throw'.")
                else:
                    print("Please type 'y' or 'n'.")

    elif current_player.last_action == "barricade":
    #If the player choose to protect their home. There is a different story based on what the user picked to protect their home. Along with
    #different decisions they have to make as well.
        print("\nYou have protected this entry point.")
        if "Full Barricade" in current_player.inventory:
        #If the user chose to barricade both the window and the main door, this branch of code will play.
            print(f"""Even with heavy pounding, the intruder can’t get in. However, just as you feel safe and secure, he smashes
through the garage door and you hear a long BANG!💥 He's in and it sounds like he has a sledgehammer... 🔨""")
            print("You spot him and have a chance to sneak up on him and strike!")
            choice = input(
                "\nDo you try to throw a punch or do you run upstairs to find a weapon and try to possibly call the police? (fight/run): ").strip().lower()
            if choice == "fight":
                print("""\nYou spot the intruder. Adrenaline coursing through your veins. You both lock eyes and you rush towards him.
But, in your rush of thought you did not realize he had the weapon and you did not. He strikes you down with 
the sledgehammer. You did not survive.""")
                current_player.alive = False
                current_player.health = 0
                print(current_player.die())
            elif choice == "run":
                running_upstairs()
                print(
                    "\nYou snap out of your trance and run upstairs. Escaping any danger that could have happened. Looking for a weapon.")
                print("You find a old BB gun, this will help you think to yourself.")
                input("Press enter to continue...")
                current_player.add_item("BB Gun")
                current_player.location = "upstairs"
                scene_three.scene_three(current_player, intruder)
            else:
                print("You hesitate, frozen in time, the intruder closes in on you. It is over.")
                current_player.alive = False
                current_player.health = 0
                print(current_player.die())
        elif "Barricaded Door" in current_player.inventory:
        #If the user chose to only barricade the door this branch of code will play
            print("You reinforced the main door. It's steady for now."
                  " But suddenly you hear shattering glass  💥 spread throughout the living room. \nHe found another way in."
                  " And he has a sledgehammer 🔨.")
            choice = input("Do you try to fight or run upstairs for more options? (fight/run): ").strip().lower()
            if choice == "fight":
                print("You rush toward the noise, fists ready. The intruder swings his weapon — a brutal blow lands.")
                print("You collapse. The world fades. You didn’t survive.")
                current_player.health = 0
                current_player.alive = False
                print(current_player.die())

            elif choice == "run":
                running_upstairs()
                print("You sprint upstairs to create distance. You remember you have your phone in your pocket.")
                print("You also stumble upon a heavy flashlight that could be used as a weapon")
                choice = input("Pick it up? (y/n): ").strip().lower()
                if choice == "y":
                    current_player.add_item("Heavy Flashlight")
                    scene_three.scene_three(current_player, intruder)
                    return
                elif choice == "n":
                    current_player.location = "upstairs"
                    scene_three.scene_three(current_player, intruder)
                    return
                else:
                    print("You are frozen like Elsa (you did not input correctly), your world turns black.")
                    current_player.health = 0
                    current_player.alive = False
                    print(current_player.die())
                    return
        elif "Barricaded Windows" in current_player.inventory:
        #If the user chose to barricade the window this branch of code will play
            print("""You block off the windows by moving a tall dresser in front of them. 
The front door is still weak. Moments later, you hear the clank of the knob dropped to the floor. The intruder has
a sledgehammer 🔨 and has broken in.""")
            while True:
                choice = input("Do you try to fight or run upstairs for more time? (fight/run): ").strip().lower()
                if choice == "fight":
                    print("You grab the toaster from the countertop and try to swing it."
                          "The intruder is stunned.")
                    intruder.health -= 10
                    print(f"\nIntruder is now at {intruder.health} health")
                    print("""\nIts no use. He overcomes the damage and overpowers you. It is over.""")
                    current_player.health = 0
                    current_player.alive = False
                    print(current_player.die())
                elif choice == "run":
                    running_upstairs()
                    print("""You run upstairs away from the danger. As the intruder looks through the kitchen
for valuables. However, you find a long metal rod from a bed. Thinking to yourself this could help.""")
                    while True:
                        choice = input("Pick it up? (y/n): ").strip().lower()
                        if choice == "y":
                            current_player.add_item("Long Metal Rod")
                            break
                        elif choice == "n":
                            print("\nYou did not pick up the weapon")
                            current_player.location = "upstairs"
                            break
                        else:
                            print("Please pick y or n.")
                            continue
                    scene_three.scene_three(current_player, intruder)
                    break

    else:

        print("You freeze for a moment, unsure of what to do next.")

from Scenes import scene_three
