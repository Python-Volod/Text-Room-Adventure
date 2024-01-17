#=======================================================================================================================================================================
# A separate file for battle interaction for Room adventure game by python-voldemort # stored separatly for better readability of the main game file
#================================================================================Modules================================================================================

import random
import time

#=====================================================
#==================in-game functions==================
#=====================================================

# This function is copied from the main file, because it is imposible to import them as it raises circular import error
def draw_picture(location, alighnment = "left", speed = 0.09):
    with open(location, "r") as image:
        # Read all instanteniously
        if speed == -1:
            print(image.read())
            return 0
        image = image.readlines()
        # Read line by line // for dramatic effect
        if alighnment == "left":
            for line in image:
                print(line, end="")
                time.sleep(speed)
        elif alighnment == "center":
            for line in image:
                print("\t\t\t" + line)
                time.sleep(speed)

# Main function
def battle(player, opponent, current_loc):
    player_info = list(player.get_info())
    player_info.pop(3) # Player's mental health, irrelavant to battle
    opponent_info = opponent.get_info()

    def players_turn():
        action = input("Do you (a)ttack or (d)efend? ").lower()
        damage = 0
        defence = False
        if player.classType == "DoomSlayer":
            if action == "a":
                player.choose_weapon()
                damage = player.calculateAttack()
                print("{} the {} attacks the {} with {}!".format(player_info[0], player_info[1], opponent_info[0], player.weapon))
            else:
                print("{} the {} is on guard".format(player_info[0], player_info[1]))
                defence = True
            return damage, defence
        else:
            if action == "a":
                damage = player.calculateAttack()
                print("{} the {} attacks the {}!".format(player_info[0], player_info[1], opponent_info[0]))
            else:
                print("{} the {} is on guard".format(player_info[0], player_info[1]))
                defence = True
            return damage, defence

    def opponents_turn():
        action = random.randint(1, 2)
        damage = 0
        defence = False
        if action == 1:
            print("the {} attacks {} the {}!".format(opponent_info[0], player_info[0], player_info[1]))
            damage = opponent.calculateAttack()
        else:
            print("the {} is on guard".format(opponent_info[0]))
            defence = True
        return damage, defence

    print("{} the {} Against the {}".format(player_info[0], player_info[1], opponent_info[0]))
    print(opponent)
    round_count = 1
    while True:
        if  player.isStillAlive() == False and  opponent.isStillAlive() == False:
            print("\n" * 5)
            print("The fight ends with both opponents killing each other\n\n")
            time.sleep(1.5)
            draw_picture("in_game_text/end_game_through_death.txt")
            break
        elif  player.isStillAlive() == False:
            print("\n" * 5)
            print("{} kills you\n\n".format(opponent_info[0]))
            draw_picture("in_game_text/end_game_through_death.txt")
            time.sleep(1.5)
            break
        elif opponent.isStillAlive() == False:
            print("\n" * 5)
            print("// You were able to defeat the {}!\n".format(opponent_info[0]))
            print("---------End of Fight---------\n\n")
            opponent.revive()
            current_loc.opponents.remove(opponent)
            if player.classType == "DoomSlayer":
                player.finish_him()
            break
        print("\n---- Round {} ----\n".format(round_count))
        player_damage, p_def = players_turn()
        opponent_damage, o_def = opponents_turn()
        if p_def:
            opponent_damage = opponent_damage - opponent_damage * player.defence
        if o_def:
            player_damage = player_damage - player_damage * opponent.defence
        player.calculateDefence(opponent_damage)
        opponent.calculateDefence(player_damage)
        print("{} now has only {:.2f} HP left!".format(player_info[0], player.HP))
        print("{} now has only {:.2f} HP left!".format(opponent_info[0], opponent.HP))
        round_count += 1
