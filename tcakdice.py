import Dice



bloodlust_die_1 = Dice.Dice('Black','Black','Black','Grey','White','White')
bloodlust_die_2 = Dice.Dice('Black','Black','Black','Grey','Grey','White')
bloodlust_die_3 = Dice.Dice('Black','Black','Grey','Grey','Grey','White')
bloodlust_die_4 = Dice.Dice('Black','Black','Grey','White','White','White')
bloodlust_die_5 = Dice.Dice('Black','Grey','Grey','Grey','White','White')
bloodlust_die_6 = Dice.Dice('Black','Grey','Grey','White','White','White')

victims_die_1 = Dice.Dice('Canari','Canari','Orange','Orange','Yellow','Brown')
victims_die_2 = Dice.Dice('Canari','Canari','Orange','Yellow','Yellow','Brown')
victims_die_3 = Dice.Dice('Canari','Canari','Orange','Yellow','Brown','Brown')
victims_die_4 = Dice.Dice('Canari','Orange','Orange','Yellow','Yellow','Brown')
victims_die_5 = Dice.Dice('Canari','Orange','Orange','Yellow','Brown','Brown')
victims_die_6 = Dice.Dice('Canari','Orange','Yellow','Yellow','Brown','Brown')

methods_die_1 = Dice.Dice('Forest','Forest','Blue','Blue','Purple','Apple')
methods_die_2 = Dice.Dice('Forest','Forest','Blue','Purple','Purple','Apple')
methods_die_3 = Dice.Dice('Forest','Forest','Blue','Purple','Apple','Apple')
methods_die_4 = Dice.Dice('Forest','Blue','Blue','Purple','Purple','Apple')
methods_die_5 = Dice.Dice('Forest','Blue','Blue','Purple','Apple','Apple')
methods_die_6 = Dice.Dice('Forest','Blue','Purple','Purple','Apple','Apple')

negligence_die_1 = Dice.Dice(3,3,3,2,2,1)
negligence_die_2 = Dice.Dice(3,3,3,2,1,1)
negligence_die_3 = Dice.Dice(3,3,2,2,2,1)
negligence_die_4 = Dice.Dice(3,3,2,1,1,1)
negligence_die_5 = Dice.Dice(3,2,2,2,1,1)
negligence_die_6 = Dice.Dice(3,2,2,1,1,1)


bloodlust_dicebag = Dice.Dice_Bag(bloodlust_die_1,bloodlust_die_2,bloodlust_die_3,
                             bloodlust_die_4,bloodlust_die_5,bloodlust_die_6)

victims_dicebag = Dice.Dice_Bag(victims_die_1,victims_die_2,victims_die_3,
                           victims_die_4,victims_die_5,victims_die_6)

methods_dicebag = Dice.Dice_Bag(methods_die_1,methods_die_2,methods_die_3,
                           methods_die_4,methods_die_5,methods_die_6)

negligence_dicebag = Dice.Dice_Bag(negligence_die_1,negligence_die_2,negligence_die_3,
                              negligence_die_4,negligence_die_5,negligence_die_6)




bloodlust_die_1_list = list(bloodlust_die_1.face_dict.values())
bloodlust_die_2_list = list(bloodlust_die_2.face_dict.values())
bloodlust_die_3_list = list(bloodlust_die_3.face_dict.values())
bloodlust_die_4_list = list(bloodlust_die_4.face_dict.values())
bloodlust_die_5_list = list(bloodlust_die_5.face_dict.values())
bloodlust_die_6_list = list(bloodlust_die_6.face_dict.values())

victims_die_1_list = list(victims_die_1.face_dict.values())
victims_die_2_list = list(victims_die_2.face_dict.values())
victims_die_3_list = list(victims_die_3.face_dict.values())
victims_die_4_list = list(victims_die_4.face_dict.values())
victims_die_5_list = list(victims_die_5.face_dict.values())
victims_die_6_list = list(victims_die_6.face_dict.values())

methods_die_1_list = list(methods_die_1.face_dict.values())
methods_die_2_list = list(methods_die_2.face_dict.values())
methods_die_3_list = list(methods_die_3.face_dict.values())
methods_die_4_list = list(methods_die_4.face_dict.values())
methods_die_5_list = list(methods_die_5.face_dict.values())
methods_die_6_list = list(methods_die_6.face_dict.values())

negligence_die_1_list = list(negligence_die_1.face_dict.values())
negligence_die_2_list = list(negligence_die_2.face_dict.values())
negligence_die_3_list = list(negligence_die_3.face_dict.values())
negligence_die_4_list = list(negligence_die_4.face_dict.values())
negligence_die_5_list = list(negligence_die_5.face_dict.values())
negligence_die_6_list = list(negligence_die_6.face_dict.values())

bloodlust_dice_list = [bloodlust_die_1_list,bloodlust_die_2_list,bloodlust_die_3_list,
                       bloodlust_die_4_list,bloodlust_die_5_list,bloodlust_die_6_list]
victims_dice_list = [victims_die_1_list,victims_die_2_list,victims_die_3_list,
                     victims_die_4_list,victims_die_5_list,victims_die_6_list]
methods_dice_list = [methods_die_1_list,methods_die_2_list,methods_die_3_list,
                     methods_die_4_list,methods_die_5_list,methods_die_6_list]
negligence_dice_list = [negligence_die_1_list,negligence_die_2_list,negligence_die_3_list,
                        negligence_die_4_list,negligence_die_5_list,negligence_die_6_list]