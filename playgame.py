import Dice
import random
from gamemaster import Killer, Journalist

killer = Killer()

reveal = False
while not reveal:
    answer = input("Ready to roll? Type Y to roll the dice or R to reveal the killer's identity. "
                   "Type P to profile the killer. Type M to reveal a Media Card").lower()


    if answer == 'y':
        print()
        killer.roll_print()
        print()

    elif answer == 'p':
        dicebag = input('Which dice bag do you want to pick from? Type B for bloodlust bag, V for victim bag'
                        ', M for methods bag or N for negligence bag').lower()

        if dicebag == 'b':
            killer.dice_bag_dict["bloodlust_dicebag"].profile_draw()
        elif dicebag == 'v':
            killer.dice_bag_dict["victims_dicebag"].profile_draw()
        elif dicebag == 'm':
            killer.dice_bag_dict["methods_dicebag"].profile_draw()
        elif dicebag == 'n':
            killer.dice_bag_dict["negligence_dicebag"].profile_draw()
        else:
            print("You didn't enter a dice bag name")



    elif answer == 'm':
        roll = random.randint(1,16)
        if roll in (1,2,3,4):
            print()
            journalist = Journalist()
            journalist.on_the_case()
            print()
        elif roll == 5:
            print()
            print("Live Coverage! Move Public pressure counter leftwards one mark")
            print()
        else:
            print()
            print('No media events have occurred')
            print()



    elif answer == 'r':
        print()
        killer.reveal()
        reveal = True

    else:
        input('Please type Y to roll the dice or R to reveal the killer.')
        print()