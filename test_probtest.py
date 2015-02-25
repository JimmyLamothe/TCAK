from gamemaster import Killer
import unittest
import Probtest
import tcakdice

class ProbTestCase(unittest.TestCase):
# Test functions used to validate the module Probtest.

    def test_dice_dict_gen(self):
        # Function correctly returns counter dictionary from list.
        test_list = ["w","w","c","c","c","d"]
        self.assertEqual(Probtest.dice_dict_gen(test_list),{"w":2,"c":3,"d":1})


    def test_dice_compare(self):
        # Function correctly returns difference between counter dictionary
        # values with matching keys.
        test_roll = {"w":1.55,"c":3.40,"d":1.05}
        test_dice = {"w":2,"c":3,"d":1}
        self.assertEqual(Probtest.dice_compare(test_roll,test_dice), {"w":0.45,"c":0.40,"d":0.05})


    def test_dice_dict_split(self):
        # Function correctly returns portion of dict corresponding to given die type.
        test_dict = {'Black':1, 'Grey':1, 'White':2,'Canari':1, 'Brown':1, 'Yellow':1, 'Orange':2,
                     'Apple':1, 'Blue':2, 'Purple':1, 'Forest':1,1:1,2:1,3:2}
        self.assertEqual(Probtest.dice_dict_split(test_dict,"bloodlust"), {'Black':1, 'Grey':1, 'White':2})
        self.assertEqual(Probtest.dice_dict_split(test_dict,"victims"), {'Canari':1, 'Brown':1, 'Yellow':1, 'Orange':2})
        self.assertEqual(Probtest.dice_dict_split(test_dict,"methods"), {'Apple':1, 'Blue':2, 'Purple':1, 'Forest':1})
        self.assertEqual(Probtest.dice_dict_split(test_dict,"negligence"), {1:1, 2:1, 3:2})


    def test_roll_list_gen(self):
        # Function correctly generates a killer and rolls its dice the correct number of times,
        # returning a roll list comprising all the roll results.
        killer = Killer()
        self.assertEqual(len(Probtest.roll_list_gen(killer,100)),400)


    def test_six_face_refactor(self):
        # Function correctly refactors a counter dictionary on a base of six.
        test_dict = {'Black':1, 'Grey':1, 'White':2}
        self.assertEqual(Probtest.six_face_refactor(test_dict),{'Black':1.50, 'Grey':1.50, 'White':3.00})


    def test_guess_die(self):
        # Function correctly guesses the most probable die from a given refactored counter dictionary.
        self.assertEqual(Probtest.guess_die({'Black':2.90, 'Grey':1.20, 'White':1.90},"bloodlust"),tcakdice.bloodlust_die_1_list)
        self.assertEqual(Probtest.guess_die({1:3.90, 2:1.20, 3:0.90},"negligence"),tcakdice.negligence_die_6_list)
        self.assertEqual(Probtest.guess_die({'Canari':2.20, 'Brown':2.20, 'Yellow':0.80, 'Orange':0.80},"victims"),tcakdice.victims_die_3_list)
        self.assertEqual(Probtest.guess_die({'Apple':1.75, 'Blue':2.35, 'Purple':0.85, 'Forest':1.05},"methods"),tcakdice.methods_die_5_list)
        # Function works correctly when assigned a killer.
        killer = Killer()
        self.assertEqual(Probtest.guess_die(Probtest.six_face_refactor(Probtest.dice_dict_gen(
            killer.bloodlust_die.face_list)),"bloodlust",killer=killer),killer.bloodlust_die.face_list)
        self.assertEqual(Probtest.guess_die(Probtest.six_face_refactor(Probtest.dice_dict_gen(
            killer.victims_die.face_list)),"victims",killer=killer),killer.victims_die.face_list)
        self.assertEqual(Probtest.guess_die(Probtest.six_face_refactor(Probtest.dice_dict_gen(
            killer.methods_die.face_list)),"methods",killer=killer),killer.methods_die.face_list)
        self.assertEqual(Probtest.guess_die(Probtest.six_face_refactor(Probtest.dice_dict_gen(
            killer.negligence_die.face_list)),"negligence",killer=killer),killer.negligence_die.face_list)



    def test_guess_test(self):
        # Function correctly returns True if guessed dice and killer dice match.
        killer = Killer()
        blood_guess = list(killer.bloodlust_die.face_dict.values())
        victims_guess = list(killer.victims_die.face_dict.values())
        methods_guess = list(killer.methods_die.face_dict.values())
        negligence_guess = list(killer.negligence_die.face_dict.values())
        self.assertTrue(Probtest.guess_test(blood_guess,"bloodlust",killer))
        self.assertTrue(Probtest.guess_test(victims_guess,"victims",killer))
        self.assertTrue(Probtest.guess_test(methods_guess,"methods",killer))
        self.assertTrue(Probtest.guess_test(negligence_guess,"negligence",killer))


    def test_roll_list_anal(self):
        # Function correctly returns the number of correct guesses and whether the killer was caught.
        killer = Killer()
        blood_list = list(killer.bloodlust_die.face_dict.values())
        victims_list = list(killer.victims_die.face_dict.values())
        methods_list = list(killer.methods_die.face_dict.values())
        negligence_list = list(killer.negligence_die.face_dict.values())
        temp_list = [blood_list,victims_list,methods_list,negligence_list]
        roll_list = [item for list in temp_list for item in list]
        guess_dict = {"correct_guess":4,"killer_caught":True}
        self.assertEqual(Probtest.roll_list_anal(roll_list,killer),guess_dict)
        blood_list = list(killer.dice_bag_dict["bloodlust_dicebag"].draw_from_bag().face_dict.values())
        victims_list = list(killer.victims_die.face_dict.values())
        methods_list = list(killer.methods_die.face_dict.values())
        negligence_list = list(killer.negligence_die.face_dict.values())
        temp_list = [blood_list,victims_list,methods_list,negligence_list]
        roll_list = [item for list in temp_list for item in list]
        guess_dict = {"correct_guess":3,"killer_caught":False}
        self.assertEqual(Probtest.roll_list_anal(roll_list,killer),guess_dict)


    def test_turn_test(self):
        # Function correctly generates the correct number of rolls and guesses.
        print ("turn_tests")
        guess_tracker = Probtest.turn_test(100,25)
        total_guesses = guess_tracker["correct_guesses"] + guess_tracker ["incorrect_guesses"]
        self.assertEqual(total_guesses,400)
        # Function correctly returns a higher percentage of correct guesses given more rolls to guess from.
        low_turns = Probtest.turn_test(100,25)
        medium_turns = Probtest.turn_test(100,75)
        high_turns = Probtest.turn_test(100,150)
        self.assertTrue(low_turns["success_rate"]<medium_turns["success_rate"]<high_turns["success_rate"])


    def test_pull_from_bag(self):
        # Function correctly returns a random dice from a random dice bag.
        killer = Killer()
        self.assertTrue(Probtest.pull_from_bag(killer))
        killer.empty_bags()
        self.assertFalse(Probtest.pull_from_bag(killer))


    def test_profile_test(self):
        # Function correctly generates the correct number of guesses.
        print ("profile_tests")
        guess_tracker = Probtest.profile_test(100,25,50)
        total_guesses = guess_tracker["correct_guesses"] + guess_tracker ["incorrect_guesses"]
        self.assertEqual(total_guesses,400)
        # Function always guesses correctly when all dice pulled from bag.
        guess_tracker = Probtest.profile_test(100,25,1)
        self.assertEqual(guess_tracker["success_rate"],1)
        # Function has a better success rate when more dice are pulled from bag.
        no_draws = Probtest.profile_test(200,80,0)
        low_draws = Probtest.profile_test(200,80,16)
        med_draws = Probtest.profile_test(200,80,8)
        high_draws = Probtest.profile_test(200,80,4)
        self.assertTrue(no_draws["success_rate"]<low_draws[
            "success_rate"]<med_draws["success_rate"]<high_draws["success_rate"])






