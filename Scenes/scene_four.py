import player
import random
from player import play_again

ACTIONS = {
    "fight": {
        "player_damage": (8,14),
        "self_damage": (6,12),
        "text": "You attack with your weapon!",
        "dodge_chance": None
    },
    "dodge": {
        "player_damage": 0,
        "self_damage": "chance",
        "text":  "You try to dodge the attack!",
        "dodge_chance": 0.7
    },
    "run": {
        "player_damage": 0,
        "self_damage": (12,18),
        "text": "You try to run, but the intruder grabs you!",
        "dodge_chance": None
    }
}

def scene_four(current_player, intruder):
    print ("""\n---- Scene Four ----""")
    print("""
You have now barricaded yourself in the last possible spot. The intruder has checked every 
other room upstairs. You hear the quiet steps of the black boots the intruder is wearing.
He is nearing the door. Silence. BANG!! The intruder smashes through the door to get to you.
This is it. This is the final confrontation. SURVIVE UNTIL THE POLICE ARRIVE!!""")

    while True:
        if current_player.health <=0:
            print("\nYou fall to the floor and the last thing you see is the metal of the hammer...")
            current_player.die()
            break
        if intruder.health <= 20:
            print("\nThe intruder falls unconscious. You've done it. You hear the sirens and the screeching "
                  "halt of the cop cars.")
            print("Officers burst in frantically. The intruder is arrested. Your home is safe. You are alive."
                  "YOU SURVIVE!!")
            play_again()
            # have a restart game option here
            break
        print (f"\nYour health: {current_player.health}")
        print(f"Intruder health: {intruder.health}")

        action = input("Fight, dodge(risky), or run?").strip().lower()

        if action in ACTIONS:
            info = ACTIONS[action]
            print ("\n" + info["text"])
            #Deal damage
            if isinstance(info["player_damage"], tuple):
                low, high = info["player_damage"]
                dmg = random.randint(low, high)
                print (f"You strike the intruder for {dmg} damage!")
                intruder.take_damage(dmg)
            elif info["player_damage"] > 0:
                intruder.take_damage(info["player_damage"])

            #Dodge mechanic
            if info["self_damage"] == "chance":
                if random.random() < info["dodge_chance"]:
                    print("You successfully dodged!")
                else:
                    dmg = random.randint(6,12)
                    print(f"You failed to dodge and he gets to you for {dmg} damage!")
                    current_player.take_damage(dmg)

                #Normal damage for run and fight
            elif isinstance(info["self_damage"], tuple):
                low, high = info["self_damage"]
                dmg = random.randint(low, high)
                print(f"The intruder hits you for {dmg} damage!")
                current_player.take_damage(dmg)
                #Fixed damage
            elif isinstance(info["self_damage"], int) and info["self_damage"] > 0:
                print(f"The intruder hits you for {info['self_damage']} damage!")
                current_player.take_damage(info["self_damage"])

            else:
                print("The intruder hesitates, you take no damage.")





