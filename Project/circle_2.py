from p47 import pet47
from p810 import pet810
from p111214 import pet111214
from track import track
import random

p47 = pet47()
p810 = pet810()
p111214 = pet111214()
t = track()


class circle_2:

    def box_4(self, start, end, base_number):

        print()

        b = []
        while True:
            while 1:
                r = random.randint(start, end)
                if r != base_number:
                    break
            if r not in b:
                b.append(r)
            if len(b) == 4:
                break


        randomnum1 = random.randint(0, 3)

        b[randomnum1] = base_number
        p47.pet4(b[0], b[1], b[2], b[3])

        i = b.index(base_number)
        c = t.clock(4, base_number, i)
        ac = t.anti_clock(4, base_number, i)
        print()


        des4 = input(" Does this circle contains your latest number? (y/n)")
        if des4 == "y" or des4 == "Y":
            print()
            print("for last time ...")
            randomnum2 = random.randint(1, 2)
            if randomnum2 == 1:

                print("Now plz rotate as CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                print()
                if des == 'y':
                    print(
                        "There is " + str(random.randint(92, 96)) + "% Possibility  that you are in number " + str(b[c]))
                    print("You are a good counter if it matches with your last number.")
            else:
                print("Now plz rotate as ANTI CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                if des == 'y':
                    print("There is " + str(random.randint(93, 95)) + "% Possibility  that your are in number " + str(
                        b[ac]))
                    print("You are a good counter if it matches with your last number.")

        print()

    def box_5(self, start, end, base_number):

        print()

        b = []
        while True:
            while 1:
                r = random.randint(start, end)
                if r != base_number:
                    break
            if r not in b:
                b.append(r)
            if len(b) == 5:
                break

        randomnum1 = random.randint(0, 4)

        b[randomnum1] = base_number
        p47.pet5(b[0], b[1], b[2], b[3], b[4])

        i = b.index(base_number)
        c = t.clock(5, base_number, i)
        ac = t.anti_clock(5, base_number, i)
        print()


        des4 = input(" Does this circle contains your latest number? (y/n)")
        if des4 == "y" or des4 == "Y":
            print()
            print("for last time ...")
            randomnum2 = random.randint(1, 2)
            if randomnum2 == 1:

                print("Now plz rotate as CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                print()
                if des == 'y':
                    print(
                        "There is " + str(random.randint(91, 97)) + "% Possibility  that you are in number " + str(b[c]))
                    print("You are a good counter if it matches with your last number.")
            else:
                print("Now plz rotate as ANTI CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                if des == 'y':
                    print("There is " + str(random.randint(94, 98)) + "% Possibility  that your are in number " + str(
                        b[ac]))
                    print("You are a good counter if it matches with your last number.")

        print()

    def box_6(self, start, end, base_number):


        b = []
        while True:
            while 1:
                r = random.randint(start, end)
                if r != base_number:
                    break
            if r not in b:
                b.append(r)
            if len(b) == 6:
                break

        randomnum1 = random.randint(0, 5)

        b[randomnum1] = base_number
        p47.pet6(b[0], b[1], b[2], b[3], b[4], b[5])

        i = b.index(base_number)
        c = t.clock(6, base_number, i)
        ac = t.anti_clock(6, base_number, i)
        print()



        des4 = input(" Does this circle contains your latest number? (y/n)")
        if des4 == "y" or des4 == "Y":
            print()
            print("for last time ...")
            randomnum2 = random.randint(1, 2)
            if randomnum2 == 1:

                print("Now plz rotate as CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                print()
                if des == 'y':
                    print(
                        "There is " + str(random.randint(90, 97)) + "% Possibility  that you are in number " + str(b[c]))
                    print("You are a good counter if it matches with your last number.")
            else:
                print("Now plz rotate as ANTI CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                if des == 'y':
                    print("There is " + str(random.randint(93, 98)) + "% Possibility  that your are in number " + str(
                        b[ac]))
                    print("You are a good counter if it matches with your last number.")

        print()

        print()

    def box_7(self, start, end, base_number):

        print()

        b = []
        while True:
            while 1:
                r = random.randint(start, end)
                if r != base_number:
                    break
            if r not in b:
                b.append(r)
            if len(b) == 7:
                break

        randomnum1 = random.randint(0, 6)

        b[randomnum1] = base_number
        p47.pet7(b[0], b[1], b[2], b[3], b[4], b[5], b[6])

        i = b.index(base_number)
        c = t.clock(7, base_number, i)
        ac = t.anti_clock(7, base_number, i)

        print()


        des4 = input(" Does this circle contains your latest number? (y/n)")
        if des4 == "y" or des4 == "Y":
            print()
            print("for last time ...")
            randomnum2 = random.randint(1, 2)
            if randomnum2 == 1:

                print("Now plz rotate as CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                print()
                if des == 'y':
                    print(
                        "There is " + str(random.randint(93, 96)) + "% Possibility  that you are in number " + str(b[c]))
                    print("You are a good counter if it matches with your last number.")
            else:
                print("Now plz rotate as ANTI CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                if des == 'y':
                    print("There is " + str(random.randint(92, 95)) + "% Possibility  that your are in number " + str(
                        b[ac]))
                    print("You are a good counter if it matches with your last number.")

        print()

    def box_8(self, start, end, base_number):

        print()
        b = []
        while True:
            while 1:
                r = random.randint(start, end)
                if r != base_number:
                    break
            if r not in b:
                b.append(r)
            if len(b) == 8:
                break

        randomnum1 = random.randint(0, 7)

        b[randomnum1] = base_number
        p810.pet8(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7])

        i = b.index(base_number)
        c = t.clock(8, base_number, i)
        ac = t.anti_clock(8, base_number, i)

        print()


        des4 = input(" Does this circle contains your latest number? (y/n)")
        if des4 == "y" or des4 == "Y":
            print()
            print("for last time ...")
            randomnum2 = random.randint(1, 2)
            if randomnum2 == 1:

                print("Now plz rotate as CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                print()
                if des == 'y':
                    print(
                        "There is " + str(random.randint(90, 96)) + "% Possibility  that you are in number " + str(b[c]))
                    print("You are a good counter if it matches with your last number.")
            else:
                print("Now plz rotate as ANTI CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                if des == 'y':
                    print("There is " + str(random.randint(93, 95)) + "% Possibility  that your are in number " + str(
                        b[ac]))
                    print("You are a good counter if it matches with your last number.")

        print()

    def box_9(self, start, end, base_number):

        print()
        print("second circle")
        b = []
        while True:
            while 1:
                r = random.randint(start, end)
                if r != base_number:
                    break
            if r not in b:
                b.append(r)
            if len(b) == 9:
                break

        randomnum1 = random.randint(0, 8)

        b[randomnum1] = base_number

        p810.pet9(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8])

        i = b.index(base_number)
        c = t.clock(9, base_number, i)
        ac = t.anti_clock(9, base_number, i)

        print()


        des4 = input(" Does this circle contains your latest number? (y/n)")
        if des4 == "y" or des4 == "Y":
            print()
            print("for last time ...")
            randomnum2 = random.randint(1, 2)
            if randomnum2 == 1:

                print("Now plz rotate as CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                print()
                if des == 'y':
                    print(
                        "There is " + str(random.randint(92, 96)) + "% Possibility  that you are in number " + str(b[c]))
                    print("You are a good counter if it matches with your last number.")
            else:
                print("Now plz rotate as ANTI CLOCK WISE for the last time...")
                print()
                des = input("Have you done?(y/n)")
                if des == 'y':
                    print("There is " + str(random.randint(93, 95)) + "% Possibility  that your are in number " + str(
                        b[ac]))
                    print("You are a good counter if it matches with your last number.")

        print()
