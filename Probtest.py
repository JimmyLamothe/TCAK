from gamemaster import Killer

__author__ = 'Jimmy'

import Dice
import random
import tools
import collections
import tcakdice




def dice_dict_gen(dice):
# Input a list as parameter to get a counter dictionary.
# A counter dictionary adds up all instances of an item
# in a list and updates { item : instances } for each item.
    return dict(collections.Counter(dice))



def dice_compare(roll,dice):
# Compare two counter dictionaries with matching keys to get the
# absolute difference between their corresponding values.
# Parameters correspond to the actual roll proportions generated
# by the probability test and the real values on a given die.
# Lower values indicate better match chance. Values rounded
# to two decimal spaces.
    diff_dict = {}
    for key in roll:
        diff = abs((roll[key])-(dice[key]))
        diff_dict.update({key : float("{:.2f}".format(diff))})
    return diff_dict


def roll_list_gen(killer,rolls):
# Takes a specific killer (dice combination) and a number of rolls
# to make, and returns a list of all randomly rolled results.
    roll_list = []
    for roll in range(rolls):
        roll_list.append(killer.roll_return())
    return [item for roll in roll_list for item in roll]


def dice_dict_split(roll_dict,die_type):
# Takes a roll dictionary and returns a dictionary composed of faces of a
# specific die type.
    if die_type == "bloodlust":
        return {key : value for key, value in roll_dict.items() if key in ['Black', 'Grey', 'White']}
    elif die_type == "victims":
        return {key : value for key, value in roll_dict.items() if key in ['Canari', 'Brown', 'Yellow', 'Orange']}
    elif die_type == "methods":
        return {key : value for key, value in roll_dict.items() if key in ['Apple', 'Blue', 'Purple', 'Forest']}
    elif die_type == "negligence":
        return {key : value for key, value in roll_dict.items() if key in [1,2,3]}

def six_face_refactor(roll_dict):
# Takes a counter dictionary and returns the proportion of each
# item out of six, giving a fractional number of "dice faces"
# for each item, with the total faces adding up to exactly six.
    return {key : (float("{:.2f}".format(value/(sum(roll_dict.values()))*6))) for  key, value in roll_dict.items()}

def guess_die(face_dict,die_type,killer=False):
# Takes a dice roll dictionary refactored with six_face_refactor,
# a given die type, and returns the most likely die to have
# generated the results recorded in the roll dictionary. The
# guess_number variable tracks the lowest absolute difference,
# the guess variable tracks the current most probable die.
# The optional "killer" keyword parameter allows us to guess from
# the dice remaining in the dice bags corresponding to a particular
# game state.
    guess_number = 100
    guess = None
    if not killer:
        dice_list = tcakdice.bloodlust_dice_list
        if die_type == "victims":
            dice_list = tcakdice.victims_dice_list
        elif die_type == "methods":
            dice_list = tcakdice.methods_dice_list
        elif die_type == "negligence":
            dice_list = tcakdice.negligence_dice_list
    else:

        if die_type == "bloodlust":
            dice_list = [dice.face_list for dice in killer.dice_bag_dict["bloodlust_dicebag"].contents_dict.values()]
            dice_list.append(killer.bloodlust_die.face_list)
        elif die_type == "victims":
            dice_list = [dice.face_list for dice in killer.dice_bag_dict["victims_dicebag"].contents_dict.values()]
            dice_list.append(killer.victims_die.face_list)
        elif die_type == "methods":
            dice_list = [dice.face_list for dice in killer.dice_bag_dict["methods_dicebag"].contents_dict.values()]
            dice_list.append(killer.methods_die.face_list)
        elif die_type == "negligence":
            dice_list = [dice.face_list for dice in killer.dice_bag_dict["negligence_dicebag"].contents_dict.values()]
            dice_list.append(killer.negligence_die.face_list)

    for dice in dice_list:
        if sum(dice_compare(face_dict,dice_dict_gen(dice)).values()) < guess_number:
            guess_number = sum(dice_compare(face_dict,dice_dict_gen(dice)).values())
            guess = dice

    return guess

def guess_test(guess,die_type,killer):
# Takes a dice guess, a dice type and a killer (dice combination).
# Returns True if the guess corresponds to the killer, False otherwise.
    killer_die = list(killer.bloodlust_die.face_dict.values())
    if die_type == "victims":
        killer_die = list(killer.victims_die.face_dict.values())
    elif die_type == "methods":
        killer_die = list(killer.methods_die.face_dict.values())
    elif die_type == "negligence":
        killer_die = list(killer.negligence_die.face_dict.values())
    return guess == killer_die


def roll_list_anal(roll_list,killer):
# Analyzes a list of rolls and tries to guess what which possible dice
# are most likely to have generated such a list. Updates global variables
# tracking prediction successes and failures, both for individual dice
# guesses and for "catching the killer" (guessing all four dice correctly).

    # Generate a counter dictionary from the given roll list.
    roll_dict = collections.Counter(roll_list)

    # Split the counter dictionary into individual counter dictionaries
    # corresponding to the four dice types.
    bloodlust_dict = dice_dict_split(roll_dict,"bloodlust")
    victims_dict = dice_dict_split(roll_dict,"victims")
    methods_dict = dice_dict_split(roll_dict,"methods")
    negligence_dict = dice_dict_split(roll_dict,"negligence")

    # Refactor the values for each face to give likely number of faces on
    # a hypothetical dice, limited to two decimal numbers.
    bloodlust_faces = six_face_refactor(bloodlust_dict)
    victims_faces = six_face_refactor(victims_dict)
    methods_faces = six_face_refactor(methods_dict)
    negligence_faces = six_face_refactor(negligence_dict)

    # Generate a guess for each of the four dice types by comparing the rolls
    # to the actual possible dice values.
    blood_guess = guess_die(bloodlust_faces,"bloodlust",killer=killer)
    vict_guess = guess_die(victims_faces,"victims",killer=killer)
    meth_guess = guess_die(methods_faces,"methods",killer=killer)
    neg_guess = guess_die(negligence_faces,"negligence",killer=killer)

    # Having generated guesses for all four dice, we now test these guesses against
    # the actual dice that generated the random roll list. We return a dictionary
    # containing the number of dice guessed correctly and whether or not the
    # killer was caught.
    guess_dict = {"correct_guess":0, "killer_caught":True, "bloodlust_guess":0, "victims_guess":0,
                  "methods_guess":0,"negligence_guess":0}
    if guess_test(blood_guess,"bloodlust",killer):
        guess_dict["correct_guess"] +=1
        guess_dict["bloodlust_guess"] = 1
    else:
        guess_dict["killer_caught"] = False
    if guess_test(vict_guess,"victims",killer):
        guess_dict["correct_guess"] +=1
        guess_dict["victims_guess"] = 1
    else:
        guess_dict["killer_caught"] = False
    if guess_test(meth_guess,"methods",killer):
        guess_dict["correct_guess"] +=1
        guess_dict["methods_guess"] = 1
    else:
        guess_dict["killer_caught"] = False
    if guess_test(neg_guess,"negligence",killer):
        guess_dict["correct_guess"] +=1
        guess_dict["negligence_guess"] = 1
    else:
        guess_dict["killer_caught"] = False
    return guess_dict




# DEPRECATED FOR profile_test.
# This function tests how likely a perfect player would be to catch the killer.
# The turns parameter determines how many rolls the program will get to try to
# guess the killer for each trial. The trials parameter determines how many trials
# to run. The more turns, the better chance the program will catch the killer for
# each trial. The more trials, the longer the test, but the more accurate the
# values generated will be.
def turn_test(trials,turns):
    guess_tracker = {"correct_guesses":0, "incorrect_guesses":0, "killers_caught":0}
    for i in range(trials):
        # Generate a killer to test
        killer = Killer()
        # Try to catch the killer and add results to guess_tracker
        guess_dict = roll_list_anal(roll_list_gen(killer,turns),killer)
        guess_tracker["correct_guesses"] += guess_dict["correct_guess"]
        guess_tracker["incorrect_guesses"] += (4 - guess_dict["correct_guess"])
        if guess_dict["killer_caught"]:
            guess_tracker["killers_caught"] +=1
    print ("Killer caught {}% of the time".format(guess_tracker["killers_caught"]/trials*100))
    success_rate = guess_tracker["correct_guesses"] /\
                   (guess_tracker["correct_guesses"] + guess_tracker["incorrect_guesses"])
    print ("Dice correctly guessed {}% of the time.".format(success_rate*100))
    guess_tracker["success_rate"] = success_rate
    return guess_tracker

# The following functions allow us to better simulate an
# actual game by integrating profiling (removal of dice
# from the dice bags in the process of the game, in addition
# to those drawn at the start to generate the killer).

def pull_from_bag(killer):
    # Remove a random dice from a random bag and return it.
    dicebag_list = [bag for bag in list(killer.dice_bag_dict.keys()) if killer.dice_bag_dict[bag].contents_dict != {}]
    choice = False
    if dicebag_list:
        choice = killer.dice_bag_dict[random.choice(dicebag_list)].draw_from_bag()
    if choice:
        return choice

# This function tests how likely a perfect player would be to catch the killer.
# The turn_max parameter tells us how many turns to roll. The profile_max parameter
# tells us how often to draw a dice from a dice bag (every "x" turns). Enter 0 for
# profile_max to have no profile draws take place.

def profile_test(trials,turn_max,profile_rate):
    # THe
    guess_tracker = {"correct_guesses":0, "incorrect_guesses":0, "killers_caught":0,"dice_left":20,
                     "correct_bloodlust":0, "correct_victims":0, "correct_methods":0, "correct_negligence":0}
    if profile_rate > turn_max:
        profile_rate = 0
    if profile_rate == 0:
        turns = turn_max
    else:
        turns = min(turn_max, profile_rate * 20)
        guess_tracker["dice_left"] -= int(turns/profile_rate)
    for i in range(trials):
        # Generate a killer to test
        killer = Killer()
        roll_list = []
        # Try to catch the killer and add results to guess_tracker
        # If profile_rate_max == 0 : don't draw from bag and roll all turns.
        if profile_rate == 0:
            roll_list += roll_list_gen(killer,turns)
        # Else draw from bag every "profile_rate" turns and add rolls to list.
        else:
            for i in range(int(turns/profile_rate)):
                roll_list += roll_list_gen(killer,profile_rate)
                pull_from_bag(killer)
        guess_dict = roll_list_anal(roll_list,killer)
        guess_tracker["correct_guesses"] += guess_dict["correct_guess"]
        guess_tracker["incorrect_guesses"] += (4 - guess_dict["correct_guess"])
        guess_tracker["correct_bloodlust"] += guess_dict["bloodlust_guess"]
        guess_tracker["correct_victims"] += guess_dict["victims_guess"]
        guess_tracker["correct_methods"] += guess_dict["methods_guess"]
        guess_tracker["correct_negligence"] += guess_dict["negligence_guess"]
        if guess_dict["killer_caught"]:
            guess_tracker["killers_caught"] +=1
    print ("Killer caught {}% of the time".format(guess_tracker["killers_caught"]/trials*100))
    success_rate = guess_tracker["correct_guesses"] /\
                   (guess_tracker["correct_guesses"] + guess_tracker["incorrect_guesses"])
    print ("Dice correctly guessed {}% of the time.".format(success_rate*100))
    print ("Bloodlust die correctly guessed {}% of the time.".format(guess_tracker["correct_bloodlust"]/trials*100))
    print ("Victims die correctly guessed {}% of the time.".format(guess_tracker["correct_victims"]/trials*100))
    print ("Methods die correctly guessed {}% of the time.".format(guess_tracker["correct_methods"]/trials*100))
    print ("Negligence die correctly guessed {}% of the time.".format(guess_tracker["correct_negligence"]/trials*100))
    guess_tracker["success_rate"] = success_rate
    print ("{} dice left in bag".format(guess_tracker["dice_left"]))
    return guess_tracker



profile_test(1000,30,2)