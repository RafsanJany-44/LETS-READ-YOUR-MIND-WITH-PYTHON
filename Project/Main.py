from p47 import pet47
from p810 import pet810
from p111214 import pet111214
from circle_2 import circle_2
from instruction1 import instru
from demo import demo
import random

p47 = pet47()
p810 = pet810()
p111214 = pet111214()
circle2 = circle_2()
ins = instru()
dem = demo()

ins.starting()

demo = input("Want a demo?? (y/n)")
if demo == 'y' or demo == 'Y':
    dem.demon()
    print()

des = input("Lets begin.(y/n)")
print()
print()
while des == 'y' or des == 'Y':
    while 1:
        randomNum1 = (random.randint(2, 5))
        randomNum2 = (random.randint(8, 13))
        if randomNum1 != 5 or randomNum2 != 8:
            break

    i = randomNum1
    j = 0
    box = []
    baseNumber = 0
    while i <= randomNum2:
        box.append(i)
        i += 1
        j += 1
        baseNumber += 1
    print("code is nothing its just some numbers..do not consider it")
    print()
    print("Chosse a number from the circle below....")

    if baseNumber == 5:
        p47.pet5(box[0], box[1], box[2], box[3], box[4])
        print(" Ok, Here you go. Now rotate ""CLOCK-WISE"" as your number time.  (code " + str(
            random.randint(1001, 9999)) + ")")
        print()
        print(" EXMP : if your number is 'n' , go 'n' position ahead.  (code 6749)")
        print()
        des2 = input("Have you done?(y/n)")
        if des2 == 'y' or des2 == 'Y':
            print("You're doing well..Good job man..")
            print()
            print(" You have a new number. This is your number now. Trow the old number into the trash.  (code " + str(
                random.randint(1001, 9999)) + ")")

            print()
            print(
                " Look, we are just give you some instruction but the decision  is yours to chose the first number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()
            p47.pet5(box[0], box[1], box[2], box[3], box[4])
            print(
                " Ok, You have to do the previous step again.. But now just rotate ""ANTI CLOCK WISE"" as your present number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()

            des3 = input(" You are in another number..Stay here and press 'y': ")
            if des3 == 'y' or des3 == 'Y':
                print()
                circle2.box_4(randomNum1, randomNum2, baseNumber)





    elif baseNumber == 6:

        p47.pet6(box[0], box[1], box[2], box[3], box[4], box[5])
        print(" Ok, Here you go. Now rotate ""CLOCK-WISE"" as your number time.  (code " + str(
            random.randint(1001, 9999)) + ")")
        print()
        print(" EXMP : if your number is 'x' , go 'x' position ahead.  (code 6749)")
        print()

        print()

        des2 = input("Have you done?(y/n)")
        if des2 == 'y' or des2 == 'Y':
            print("You're doing well..Good job man..")
            print()
            print("Very nice..   (code 8849)")
            print(" You have a new number. This is your number now. Trow the old number into the trash.  (code " + str(
                random.randint(1001, 9999)) + ")")

            print()
            print(
                " Look, we are just give you some instruction but the decision  is yours to chose the first number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()
            p47.pet6(box[0], box[1], box[2], box[3], box[4], box[5])
            print(
                " Ok, You have to do the previous step again.. But now just rotate ""ANTI CLOCK WISE"" as your present number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()

        des3 = input("Have you done?(y/n)")
        if des3 == 'y':
            print()
            randomNum3 = (random.randint(1, 2))
            if randomNum3 == 1:
                circle2.box_4(randomNum1, randomNum2, baseNumber)
            else:
                circle2.box_5(randomNum1, randomNum2, baseNumber)









    elif baseNumber == 7:
        p47.pet7(box[0], box[1], box[2], box[3], box[4], box[5], box[6])
        print(" Ok, Here you go. Now rotate ""CLOCK-WISE"" as your number time.  (code " + str(
            random.randint(1001, 9999)) + ")")
        print()
        print(" EXMP : if your number is 'x' , go 'x' position ahead.  (code 6749)")
        print()

        print()

        des2 = input("Have you done?(y/n)")
        if des2 == 'y' or des2 == 'Y':
            print("You're doing well..Good job man..")
            print()
            print("Very nice..   (code 8849)")
            print(" You have a new number. This is your number now. Trow the old number into the trash.  (code " + str(
                random.randint(1001, 9999)) + ")")

            print()
            print(
                " Look, we are just give you some instruction but the decision  is yours to chose the first number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()
            p47.pet7(box[0], box[1], box[2], box[3], box[4], box[5], box[6])
            print(
                " Ok, You have to do the previous step again.. But now just rotate ""ANTI CLOCK WISE"" as your present number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()

        des3 = input("Have you done?(y/n)")
        if des3 == 'y':
            print()

            randomNum3 = (random.randint(1, 3))
            if randomNum3 == 1:
                circle2.box_4(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 2:
                circle2.box_5(randomNum1, randomNum2, baseNumber)
            else:
                circle2.box_6(randomNum1, randomNum2, baseNumber)




    elif baseNumber == 8:
        p810.pet8(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7])
        print(" Ok, Here you go. Now rotate ""CLOCK-WISE"" as your number time.  (code " + str(
            random.randint(1001, 9999)) + ")")
        print()
        print(" EXMP : if your number is 'x' , go 'x' position ahead.  (code 6749)")
        print()

        print()

        des2 = input("Have you done?(y/n)")
        if des2 == 'y' or des2 == 'Y':
            print("You're doing well..Good job man..")
            print()
            print("Very nice..   (code 8849)")
            print(" You have a new number. This is your number now. Trow the old number into the trash.  (code " + str(
                random.randint(1001, 9999)) + ")")

            print()
            print(
                " Look, we are just give you some instruction but the decision  is yours to chose the first number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()
            p810.pet8(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7])
            print(
                " Ok, You have to do the previous step again.. But now just rotate ""ANTI CLOCK WISE"" as your present number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()

        des3 = input("Have you done?(y/n)")
        if des3 == 'y':
            print()

            randomNum3 = (random.randint(1, 3))
            if randomNum3 == 1:
                circle2.box_4(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 2:
                circle2.box_5(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 3:
                circle2.box_6(randomNum1, randomNum2, baseNumber)






    elif baseNumber == 9:
        p810.pet9(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8])
        print(" Ok, Here you go. Now rotate ""CLOCK-WISE"" as your number time.  (code " + str(
            random.randint(1001, 9999)) + ")")
        print()
        print(" EXMP : if your number is 'x' , go 'x' position ahead.  (code 6749)")
        print()

        print()

        des2 = input("Have you done?(y/n)")
        if des2 == 'y' or des2 == 'Y':
            print("You're doing well..Good job man..")
            print()
            print("Very nice..   (code 8849)")
            print(" You have a new number. This is your number now. Trow the old number into the trash.  (code " + str(
                random.randint(1001, 9999)) + ")")

            print()
            print(
                " Look, we are just give you some instruction but the decision  is yours to chose the first number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()
            p810.pet9(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8])
            print(
                " Ok, You have to do the previous step again.. But now just rotate ""ANTI CLOCK WISE"" as your present number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()

        des3 = input("Have you done?(y/n)")
        if des3 == 'y':
            print()
            randomNum3 = 3  # (random.randint(1, 3))
            if randomNum3 == 1:
                circle2.box_5(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 2:
                circle2.box_6(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 3:
                circle2.box_7(randomNum1, randomNum2, baseNumber)




    elif baseNumber == 10:
        p810.pet10(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8], box[9])
        print(" Ok, Here you go. Now rotate ""CLOCK-WISE"" as your number time.  (code " + str(
            random.randint(1001, 9999)) + ")")
        print()
        print(" EXMP : if your number is 'x' , go 'x' position ahead.  (code 6749)")
        print()

        print()

        des2 = input("Have you done?(y/n)")
        if des2 == 'y' or des2 == 'Y':
            print("You're doing well..Good job man..")
            print()
            print("Very nice..   (code 8849)")
            print(" You have a new number. This is your number now. Trow the old number into the trash.  (code " + str(
                random.randint(1001, 9999)) + ")")

            print()
            print(
                " Look, we are just give you some instruction but the decision  is yours to chose the first number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()
            p810.pet10(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8], box[9])
            print(
                " Ok, You have to do the previous step again.. But now just rotate ""ANTI CLOCK WISE"" as your present number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()

        des3 = input("Have you done?(y/n)")
        if des3 == 'y':
            randomNum3 = (random.randint(1, 4))

            if randomNum3 == 1:
                circle2.box_5(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 2:
                circle2.box_6(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 3:
                circle2.box_7(randomNum1, randomNum2, baseNumber)
            else:
                circle2.box_8(randomNum1, randomNum2, baseNumber)




    elif baseNumber == 11:
        p111214.pet11(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8], box[9], box[10])

        print(" Ok, Here you go. Now rotate ""CLOCK-WISE"" as your number time.  (code " + str(
            random.randint(1001, 9999)) + ")")
        print()
        print(" EXMP : if your number is 'x' , go 'x' position ahead.  (code 6749)")
        print()

        print()

        des2 = input("Have you done?(y/n)")
        if des2 == 'y' or des2 == 'Y':
            print("You're doing well..Good job man..")
            print()
            print("Very nice..   (code 8849)")
            print(" You have a new number. This is your number now. Trow the old number into the trash.  (code " + str(
                random.randint(1001, 9999)) + ")")

            print()
            print(
                " Look, we are just give you some instruction but the decision  is yours to chose the first number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()
            p111214.pet11(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8], box[9], box[10])

            print(
                " Ok, You have to do the previous step again.. But now just rotate ""ANTI CLOCK WISE"" as your present number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()

        des3 = input("Have you done?(y/n)")
        if des3 == 'y':
            randomNum3 = (random.randint(1, 3))
            if randomNum3 == 1:
                circle2.box_6(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 2:
                circle2.box_7(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 3:
                circle2.box_8(randomNum1, randomNum2, baseNumber)



    elif baseNumber == 12:
        p111214.pet12(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8], box[9], box[10], box[11])
        print(" Ok, Here you go. Now rotate ""CLOCK-WISE"" as your number time.  (code " + str(
            random.randint(1001, 9999)) + ")")
        print()
        print(" EXMP : if your number is 'x' , go 'x' position ahead.  (code 6749)")
        print()

        print()

        des2 = input("Have you done?(y/n)")
        if des2 == 'y' or des2 == 'Y':
            print("You're doing well..Good job man..")
            print()
            print("Very nice..   (code 8849)")
            print(" You have a new number. This is your number now. Trow the old number into the trash.  (code " + str(
                random.randint(1001, 9999)) + ")")

            print()
            print(
                " Look, we are just give you some instruction but the decision  is yours to chose the first number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()
            p111214.pet12(box[0], box[1], box[2], box[3], box[4], box[5], box[6], box[7], box[8], box[9], box[10],
                          box[11])
            print(
                " Ok, You have to do the previous step again.. But now just rotate ""ANTI CLOCK WISE"" as your present number.  (code " + str(
                    random.randint(1001, 9999)) + ")")
            print()

        des3 = input("Have you done?(y/n)")
        if des3 == 'y':
            randomNum3 = (random.randint(1, 4))
            if randomNum3 == 1:
                circle2.box_6(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 2:
                circle2.box_7(randomNum1, randomNum2, baseNumber)
            elif randomNum3 == 3:
                circle2.box_8(randomNum1, randomNum2, baseNumber)
            else:
                circle2.box_9(randomNum1, randomNum2, baseNumber)

    des = input('do you want to start one more time?(y/n)')
print()
print("Thank You")
