import threading   # Allows multiple functions to work at the same time.
from Scenes import scene_four
from ascii_art import phone


def input_with_timeout(prompt, timeout=10):
    """Gives user a time limit to make a decision.
    Runs for the given amount of seconds and then quits the program and runs
    the consequence. Forcing the user to make a decision."""
    result = [None]

    def ask():
        result[0] = input(prompt).strip().lower()

    thread = threading.Thread(target=ask)  #Runs the ask() function.
    thread.daemon = True  #Will automatically close when main program exits.
    thread.start()
    thread.join(timeout)  #Wait for the program to finish and then closes after
    return result[0]  #Stores the user input within the time limit.


def scene_three(current_player, intruder):
    """The third scene of the game. Based off decisions from scene one and two.
    Progresses through their individual story."""
    print("\n---- Scene Three ----")
    print("""
Your heart is racing. But most importantly, you are alive.
You currently are hidden in an extra bedroom.
 
What am I going to do? What am I going to do? questions rapidly fly in your mind. The rain pours harder 
and you hear the creak of the floor boards. Footsteps.""")
#Player regains breathe after scene two, goes to another form of option choosing with embedded user
#input. In the form of match cases. First, allows the user to check inventory and gather their mind
#before continuing.

    valid_weapons = ["fork", "mini flag", "pen"]
    stealth_weapons = ["pencil","metal ruler", "broken glass bottle"]

    while True:
        choice = input("\nWant to check inventory (y/n):").strip().lower()
        if choice == "y":
            current_player.show_inventory()
            input("\nPress enter to continue...")
            break
        elif choice == "n":
            input("\nAre you ready? Press Enter to continue... ")
            break
        else:
            print("\nInvalid input. Please try again.")

    match current_player.last_action:
    #Matches the players last action to the case and then plays through it.
        case "attack":
        #Player previously chose to attack. They now choose a new item and have immediate
        #confrontation. Includes a timed component that puts the user under increased pressure
        #to make a decision.
            original_weapon = current_player.inventory[-1]
            print("\nAs you panic looking for anything more to help you, you spot three different items. ")
            while True:
                item_choice = input(
                    "Pick up fork, mini flag, or pen? (Fork, Mini Flag, or Pen): ").strip().lower()
                if item_choice in valid_weapons:
                    current_player.add_item(item_choice.title())
                    print(f"\nYou picked up the {item_choice}. Suddenly the intruder bursts in "
                          f"to the room you're hiding in!")
                    print("There is no running, you two lock eyes.")
                    break
                else:
                    print("\nInvalid input. Please try again.")
            while True:
                attack_choice = input(f"\nUse {item_choice.title()} or {original_weapon}: ").strip().lower()
                if attack_choice.strip().lower() in (item_choice.lower(), original_weapon.lower()):
                    print("You land a hit!")
                    intruder.take_damage(10)
                    print("\nThe intruder lunges back at you and swings his sledgehammer, grazing your shoulder!")
                    current_player.take_damage(10)

                    go_again = input_with_timeout(
                        "\nQuick!! You have 10 seconds! Go for another hit while you have him injured? (y/n):",
                        timeout=10)
                    if go_again == "y":
                        print("You strike again!")
                        intruder.take_damage(10)
                        print ("\nYou run to another bedroom upstairs. Remembering your phone in your pocket. You start to dial 911...")
                        print("The police say they will be there in 5 minutes.")
                        current_player.add_item("Phone")
                        current_player.location = "another room"
                        scene_four.scene_four(current_player, intruder)
                        break
                    elif go_again == "n":
                        print("\nYou missed an opportunity. As he is stunned, you run to another room.")
                        print("You remember your phone. You begin to dial 911...")
                        print("The police say they will be there in 5 minutes.")
                        current_player.location = "another room"
                        scene_four.scene_four(current_player, intruder)
                        break
                    else:
                        print("\n You froze too long... its over.")
                        current_player.die()
                        break

        case "downstairs":
        #Player choose to stay downstairs. They now are faced with getting out of a situation
        #they put themselves in.
            print("\nYou hear the intruder drawing near. You must think quick. You hide in the pantry." )
            print("\nHowever, hes now in front of the door!!")

            while True:
                choice3 = input("\nSlam open the door on the intruder and run upstairs? (y/n):").strip().lower()
                if choice3 == "y":
                    intruder.take_damage(10)
                    print("\nIt worked! You run upstairs. Remembering your phone is in your pocket. You start to dial 911...")
                    current_player.add_item("Phone")
                    current_player.location = "another room"
                    scene_four.scene_four(current_player, intruder)
                    return
                elif choice3 == "n":
                    print("\nHe checked the pantry.")
                    current_player.die()
                    return
                else:
                    print("\nPlease pick a valid choice.")

        case "escape":
        #Player tried to escape the scene and hid upstairs. They are faced with a choice
        #of calling 9/11 to progress the story.
            print("\nAfraid of any confrontation. You hide in the very back of the room under a nightstand. You pull out your phone.")
            while True:
                phone()
                choice5 = input("\nDial 911? (y/n):").strip().lower()
                if choice5 == "y":
                    print("\nYou start to dial 911. Explaining your life is in danger. The police say they will be there in 5 minutes.")
                    print("You think to yourself. Survive 5 more minutes. I can do that.")
                    print("\nIn a moment of courage you look around for something to defend yourself.")
                    while True:
                        choice6 = input("Go get the metal ruler from the desk drawer in the room? (y/n):").strip().lower()
                        if choice6 == "y":
                            current_player.add_item("Metal ruler")
                            current_player.location = "another room"
                            scene_four.scene_four(current_player, intruder)
                            break
                        elif choice6 == "n":
                            print ("\nYou decided not to.")
                            print ("\nThe intruder finds you but you never picked up a weapon. Your path ends here...")
                            current_player.die()
                            break
                        else:
                            print("\n Please choose either 'y' or 'n'.")
                    break
                elif choice5 == "n":
                    print("\nYou think the intruder will hear you and you did not pick a weapon to defend yourself.")
                    print("You wait, terrified.")
                    print("The intruder bursts in, its too late.")
                    current_player.die()
                else:
                    print ("\n Please choose either 'y' or 'n'.")
        case "run":
        #Players last action was to run. They hide near the stairs. Faced with more decision's
        #to make.
            original_weapon = current_player.inventory[-1]
            print("\nYou are hiding in the corner right before the stairwell. Looking to see if you can spot the intruder.")
            print(f"You spot him and hide behind the wall. {original_weapon} in hand.")
            while True:
                choice4 = input(f"\nHe walks up the stairs looking for valuables. You have time to strike. Do it? (y/n):").strip().lower()
                if choice4 == "y":
                    intruder.take_damage(20)
                    print("\nSuccessful! He's wounded! You move to another room upstairs. Phone in your pocket. You start to dial 911...")
                    print("The police say they will be there in 5 minutes. Survive 5 more minutes.")
                    current_player.location = "another room"
                    scene_four.scene_four(current_player, intruder)
                    return
                elif choice4 == "n":
                    print("\nYou hid in the corner. Too scared to act. He got to you first.")
                    current_player.die()
                    return
                else:
                    print("\n Please choose either 'y' or 'n'.")


        case "stealth":
        #Players last action was to be stealthy. This mini scene plays out because they picked that.
        #The user is once again faced with different decisions.
            print(f"\nLooking around the room for something to defend yourself you find a pencil, metal ruler, and broken glass bottle.")
            while True:
                weapon_choice = input("\nWhich one do you want?").strip().lower()
                if weapon_choice in stealth_weapons:
                    current_player.add_item(weapon_choice.title())
                    print("\nThe intruder creaks up the stairs and runs towards you.")
                    break
                else:
                    print("Please pick a valid weapon.")
            while True:
                choice = input("\nDodge or fight?").strip().lower()
                if choice == "fight":
                    print(f"You stab with the {current_player.inventory[-1]}! ")
                    intruder.take_damage(20)
                    print("\nThe intruder lunges back at you with his sledgehammer! You have 5 seconds!")
                    choice2 = input_with_timeout("Dodge? (y/n):", timeout = 5)
                    if choice2 == "y":
                        print("You dodge! Running to another room!")
                        while True:
                            phone()
                            dial_choice= input("As your running you feel your phone in your pocket. Dial 911? (y/n):").strip().lower()
                            if dial_choice == "y":
                                print("The police say they will be there in 5 minutes!")
                                current_player.add_item("Phone")
                                current_player.location = "another room"
                                scene_four.scene_four(current_player, intruder)
                                break
                            elif dial_choice == "n":
                                print("\nAs your debating to make a decision the intruder sneaks up on you...")
                                print("It is over.")
                                current_player.die()
                                break
                            else:
                                print("Please choose either 'y' or 'n'.")
                        return
                    elif choice2 == "n":
                        print("He stabs you fatally.")
                        current_player.die()
                        return
                    else:
                        print("\nYou froze too long... its over.")
                        current_player.die()
                        return
                elif choice == "dodge":
                    print(f"\nYou dodge and slice with {current_player.inventory[-1]}! ")
                    intruder.take_damage(15)
                    print("As he is wounded. You run to another room to gather yourself.")
                    while True:
                        phone()
                        choice3 = input("\nRemembering your phone in your pocket. Do you call 911? (y/n):").strip().lower()
                        if choice3 == "y":
                            print("Great choice. The police say they are on their way!")
                            current_player.add_item("Phone")
                            current_player.location = "another room"
                            scene_four.scene_four(current_player, intruder)
                            break
                        elif choice3 == "n":
                            print("As you freeze in making a decision. He sneaks up on you and closes in.")
                            print("Its over....")
                            current_player.die()
                            break
                        else:
                            print("\n Please choose either 'y' or 'n'.")

                else:
                    print("\nPlease type 'dodge' or 'fight'.")

        case _:
        #This is the last case out of the actions. This is for the user that decided to barricade their home.
            print("\nAs you hide out of site terrified, the intruder"
                  "begins heading your direction. ")
            choice = input(f"\nYou must act fast, use the {current_player.inventory[-1]} or run for safety (run/attack): ").strip().lower()
            if choice == "run":
                while True:
                    phone()
                    choice = input("\nYou make it to the bathroom and remember you have your phone on you. Start to dial 911? (y/n):").strip().lower()
                    if choice == "y":
                        print ("\nGreat! The cops said they will be there in 5 minutes.")
                        print ("'I need to survive 5 more minutes' you tell yourself")
                        current_player.location = "another room"
                        scene_four.scene_four(current_player, intruder)
                        break
                    elif choice == "n":
                        print("\nYou did not dial 911 and the intruder heard you. No one is coming to save you now.")
                        current_player.die()
                        break
                    else:
                        print("\nPlease type 'y' or 'n'.")
            if choice == "attack":
                print(f"In a moment of fearlessness you come out from the shadows and smack the intruder with the {current_player.inventory[-1]}.")
                intruder.take_damage(20)
                print("\nYou stun him and move on to the next room that you can find shelter in.")
                current_player.location = "next room"
                print ("You remember your phone on you and start to dial 911.")
                current_player.add_item("Phone")
                print("You have to survive for 5 more minutes until the police get there.")



