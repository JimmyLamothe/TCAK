import random

class Dice(object):
    def __init__(self, *faces):
        self.face_list = [face for face in faces]
        self.face_dict = {}
        for (face, value) in list(enumerate(faces, start=1)):
            self.face_dict[face] = value

    def roll_print(self):
        roll = random.randint(1,len(self.face_dict))
        print (self.face_dict[roll])

    def roll_return(self):
        roll = random.randint(1,len(self.face_dict))
        return self.face_dict[roll]


class Dice_Bag(object):
    def __init__(self,*dice):
        self.contents_dict = {}
        for (die, identity) in list(enumerate(dice, start=1)):
            self.contents_dict[die] = identity

    def draw_from_bag(self):
        die = random.choice(list(self.contents_dict.keys()))
        return self.contents_dict.pop(die)

    def profile_draw(self):
        if self.contents_dict == {}:
            print ('That dicebag is empty!')
        else:
            die = random.choice(list(self.contents_dict.keys()))
            profile_draw = self.contents_dict.pop(die)
            print (list(profile_draw.face_dict.values()))









