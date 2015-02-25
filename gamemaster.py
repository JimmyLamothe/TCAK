import Dice
import tcakdice
import random

class Gamemaster(object):

    @staticmethod
    def fill_dice_bags():
        bloodlust_dicebag = Dice.Dice_Bag(tcakdice.bloodlust_die_1, tcakdice.bloodlust_die_2, tcakdice.bloodlust_die_3,
                             tcakdice.bloodlust_die_4, tcakdice.bloodlust_die_5, tcakdice.bloodlust_die_6)
        victims_dicebag = Dice.Dice_Bag(tcakdice.victims_die_1, tcakdice.victims_die_2, tcakdice.victims_die_3,
                                   tcakdice.victims_die_4, tcakdice.victims_die_5, tcakdice.victims_die_6)
        methods_dicebag = Dice.Dice_Bag(tcakdice.methods_die_1, tcakdice.methods_die_2, tcakdice.methods_die_3,
                                   tcakdice.methods_die_4, tcakdice.methods_die_5, tcakdice.methods_die_6)
        negligence_dicebag = Dice.Dice_Bag(tcakdice.negligence_die_1, tcakdice.negligence_die_2, tcakdice.negligence_die_3,
                                      tcakdice.negligence_die_4, tcakdice.negligence_die_5, tcakdice.negligence_die_6)
        dice_bag_dict = {"bloodlust_dicebag": bloodlust_dicebag ,"victims_dicebag": victims_dicebag,
                         "methods_dicebag": methods_dicebag, "negligence_dicebag":negligence_dicebag}
        return dice_bag_dict


class Killer(object):
    def __init__(self):
        self.dice_bag_dict = Gamemaster.fill_dice_bags()
        self.bloodlust_die = self.dice_bag_dict["bloodlust_dicebag"].draw_from_bag()
        self.victims_die = self.dice_bag_dict["victims_dicebag"].draw_from_bag()
        self.methods_die = self.dice_bag_dict["methods_dicebag"].draw_from_bag()
        self.negligence_die = self.dice_bag_dict["negligence_dicebag"].draw_from_bag()

    def roll_print(self):
        self.bloodlust_die.roll_print()
        self.victims_die.roll_print()
        self.methods_die.roll_print()
        self.negligence_die.roll_print()

    def roll_return(self):
        roll_list = []
        roll_list.append(self.bloodlust_die.roll_return())
        roll_list.append(self.victims_die.roll_return())
        roll_list.append(self.methods_die.roll_return())
        roll_list.append(self.negligence_die.roll_return())
        return roll_list

    def reveal(self):
        print (list(self.bloodlust_die.face_dict.values()))
        print (list(self.victims_die.face_dict.values()))
        print (list(self.methods_die.face_dict.values()))
        print (list(self.negligence_die.face_dict.values()))

    def empty_bags(self):
        for key in self.dice_bag_dict:
            while self.dice_bag_dict[key].contents_dict != {}:
                self.dice_bag_dict[key].draw_from_bag()



class Journalist(object):
    def __init__(self):
        self.tenaciousness = random.choice([2,2,3,3,4,4,5,6])
        self.connections = random.randint(1,6)

    def on_the_case(self):
        print('A new journalist is on the case. His tenaciousness score '
              'is {} and his connections score is {}.'.format(self.tenaciousness, self.connections))