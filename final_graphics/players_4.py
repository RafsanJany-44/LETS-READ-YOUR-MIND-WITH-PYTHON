import turtle
from players_5 import players_5

import random


class players_4:

    def play4(self,start,end, randwall):

        raf = turtle.Turtle()

        p5=players_5()

        turtle.bgpic(randwall)
        turtle.title("Hypnos")



        randomnum3 = 0
        c_color = "#ffdfe5"
        f_color = "red"
        speed = 0
        pensize = 3.5
        randomNum1 = start
        randomNum2 = end


        i = randomNum1
        j = 0
        box = []
        baseNumber = 0
        while i <= randomNum2:
            box.append(i)
            i += 1
            j += 1
            baseNumber += 1

        if baseNumber == 5:

            raf.speed(speed)
            randomnum3 = 4

            raf.penup()
            raf.goto(-90, 190)
            for i in range(5):
                raf.penup()
                raf.forward(160)
                raf.pendown()
                raf.pensize(pensize)
                raf.pencolor(c_color)
                raf.circle(50)
                raf.right(360 / 5)

            raf.pencolor(f_color)
            raf.penup()
            if box[0] > 9:
                raf.goto(50, 220)
            else:
                raf.goto(60, 220)
            raf.write(box[0], font=("Arial", 35, "normal"))

            raf.penup()
            if box[1] > 9:
                raf.goto(145, 30)
            else:
                raf.goto(155, 30)
            raf.write(box[1], font=("Arial", 35, "normal"))

            raf.penup()
            if box[2] > 9:
                raf.goto(0, -115)
            else:
                raf.goto(10, -115)
            raf.write(box[2], font=("Arial", 35, "normal"))

            raf.penup()
            if box[3] > 9:
                raf.goto(-190, -20)
            else:
                raf.goto(-180, -20)
            raf.write(box[3], font=("Arial", 35, "normal"))

            raf.penup()
            if box[4] > 9:
                raf.goto(-160, 185)
            else:
                raf.goto(- 150, 185)
            raf.write(box[4], font=("Arial", 35, "normal"))

        elif baseNumber == 6:

            randomnum3 = random.randint(4, 5)
            raf.speed(speed)
            raf.penup()
            raf.goto(-90, 190)
            for i in range(6):
                raf.penup()
                raf.forward(160)
                raf.pendown()
                raf.pensize(pensize)
                raf.pencolor(c_color)
                raf.circle(50)
                raf.right(360 / 6)

            raf.pencolor(f_color)
            raf.penup()
            if box[0] > 9:
                raf.goto(50, 220)
            else:
                raf.goto(60, 220)
            raf.write(box[0], font=("Arial", 35, "normal"))

            raf.penup()
            if box[1] > 9:
                raf.goto(175, 60)
            else:
                raf.goto(185, 60)
            raf.write(box[1], font=("Arial", 35, "normal"))

            raf.penup()
            if box[2] > 9:
                raf.goto(95, -130)
            else:
                raf.goto(105, -130)
            raf.write(box[2], font=("Arial", 35, "normal"))

            raf.penup()
            if box[3] > 9:
                raf.goto(-110, -160)
            else:
                raf.goto(-100, -160)
            raf.write(box[3], font=("Arial", 35, "normal"))

            raf.penup()
            if box[4] > 9:
                raf.goto(-235, 10)
            else:
                raf.goto(-225, 10)
            raf.write(box[4], font=("Arial", 35, "normal"))

            raf.penup()
            if box[5] > 9:
                raf.goto(-155, 200)
            else:
                raf.goto(-145, 200)
            raf.write(box[5], font=("Arial", 35, "normal"))


        elif baseNumber == 7:
            randomnum3 = random.randint(4, 5)
            raf.speed(speed)

            raf.penup()
            raf.goto(-90, 190)
            for i in range(7):
                raf.penup()
                raf.forward(160)
                raf.pendown()
                raf.pencolor(c_color)
                raf.pensize(3.5)
                raf.circle(50)
                raf.right(360 / 7)

            raf.pencolor(f_color)
            raf.penup()
            if box[0] > 9:
                raf.goto(50, 222)
            else:
                raf.goto(60, 222)
            raf.write(box[0], font=("Arial", 35, "normal"))

            raf.penup()
            if box[1] > 9:
                raf.goto(190, 80)
            else:
                raf.goto(200, 80)
            raf.write(box[1], font=("Arial", 35, "normal"))

            raf.penup()
            if box[2] > 9:
                raf.goto(160, -120)
            else:
                raf.goto(170, -120)
            raf.write(box[2], font=("Arial", 35, "normal"))

            raf.penup()
            if box[3] > 9:
                raf.goto(-5, -225)
            else:
                raf.goto(5, -225)
            raf.write(box[3], font=("Arial", 35, "normal"))

            raf.penup()
            if box[4] > 9:
                raf.goto(-200, -155)
            else:
                raf.goto(-190, -155)
            raf.write(box[4], font=("Arial", 35, "normal"))

            raf.penup()
            if box[5] > 9:
                raf.goto(-260, 35)
            else:
                raf.goto(-250, 35)
            raf.write(box[5], font=("Arial", 35, "normal"))

            raf.penup()
            if box[6] > 9:
                raf.goto(-150, 200)
            else:
                raf.goto(-140, 200)
            raf.write(box[6], font=("Arial", 35, "normal"))



        elif baseNumber == 8:

            raf.speed(speed)
            randomnum3 = random.randint(4, 6)
            raf.penup()
            raf.goto(-90, 190)
            for i in range(8):
                raf.penup()
                raf.forward(160)
                raf.pendown()
                raf.pensize(3.5)
                raf.pencolor(c_color)
                raf.circle(50)
                raf.right(360 / 8)

            raf.pencolor(f_color)
            raf.penup()
            if box[0] > 9:
                raf.goto(50, 225)
            else:
                raf.goto(60, 225)
            raf.write(box[0], font=("Arial", 35, "normal"))

            raf.penup()
            if box[1] > 9:
                raf.goto(195, 95)
            else:
                raf.goto(205, 95)
            raf.write(box[1], font=("Arial", 35, "normal"))

            raf.penup()
            if box[2] > 9:
                raf.goto(215, -105)
            else:
                raf.goto(225, -105)
            raf.write(box[2], font=("Arial", 35, "normal"))

            raf.penup()
            if box[3] > 9:
                raf.goto(85, -255)
            else:
                raf.goto(95, -255)
            raf.write(box[3], font=("Arial", 35, "normal"))

            raf.penup()
            if box[4] > 9:
                raf.goto(-110, -265)
            else:
                raf.goto(-100, -265)
            raf.write(box[4], font=("Arial", 35, "normal"))

            raf.penup()
            if box[5] > 9:
                raf.goto(-260, -140)
            else:
                raf.goto(-250, -140)
            raf.write(box[5], font=("Arial", 35, "normal"))

            raf.penup()
            if box[6] > 9:
                raf.goto(-275, 60)
            else:
                raf.goto(-265, 60)
            raf.write(box[6], font=("Arial", 35, "normal"))

            raf.penup()
            if box[7] > 9:
                raf.goto(-145, 210)
            else:
                raf.goto(-135, 210)
            raf.write(box[7], font=("Arial", 35, "normal"))




        elif baseNumber == 9:
            raf.speed(speed)
            randomnum3 = random.randint(4, 6)

            raf.penup()
            raf.goto(-80, 280)
            for i in range(9):
                raf.penup()
                raf.forward(140)
                raf.pendown()
                raf.pensize(3.5)
                raf.pencolor(c_color)
                raf.circle(40)
                raf.right(360 / 9)

            raf.pencolor(f_color)

            raf.penup()
            if box[0] > 9:
                raf.goto(45, 305)
            else:
                raf.goto(50, 305)
            raf.write(box[0], font=("Arial", 25, "normal"))

            raf.penup()
            if box[1] > 9:
                raf.goto(180, 205)
            else:
                raf.goto(185, 205)
            raf.write(box[1], font=("Arial", 25, "normal"))

            raf.penup()
            if box[2] > 9:
                raf.goto(220, 45)
            else:
                raf.goto(225, 45)
            raf.write(box[2], font=("Arial", 25, "normal"))

            raf.penup()
            if box[3] > 9:
                raf.goto(145, -100)
            else:
                raf.goto(150, -100)
            raf.write(box[3], font=("Arial", 25, "normal"))

            raf.penup()
            if box[4] > 9:
                raf.goto(-10, -170)
            else:
                raf.goto(-5, -170)
            raf.write(box[4], font=("Arial", 25, "normal"))

            raf.penup()
            if box[5] > 9:
                raf.goto(-170, -120)
            else:
                raf.goto(-165, -120)
            raf.write(box[5], font=("Arial", 25, "normal"))

            raf.penup()
            if box[6] > 9:
                raf.goto(-260, 20)
            else:
                raf.goto(-255, 20)
            raf.write(box[6], font=("Arial", 25, "normal"))

            raf.penup()
            if box[7] > 9:
                raf.goto(-240, 185)
            else:
                raf.goto(-235, 185)
            raf.write(box[7], font=("Arial", 25, "normal"))

            raf.penup()
            if box[8] > 9:
                raf.goto(-115, 300)
            else:
                raf.goto(-110, 300)
            raf.write(box[8], font=("Arial", 25, "normal"))



        elif baseNumber == 10:

            raf.speed(speed)
            randomnum3 = random.randint(4, 6)

            raf.penup()
            raf.goto(-80, 280)
            for i in range(10):
                raf.penup()
                raf.forward(140)
                raf.pendown()
                raf.pensize(3.5)
                raf.pencolor(c_color)
                raf.circle(40)
                raf.right(360 / 10)

            raf.pencolor(f_color)
            raf.penup()
            if box[0] > 9:
                raf.goto(50, 305)
            else:
                raf.goto(55, 305)
            raf.write(box[0], font=("Arial", 25, "normal"))

            raf.penup()
            if box[1] > 9:
                raf.goto(185, 215)
            else:
                raf.goto(190, 215)
            raf.write(box[1], font=("Arial", 25, "normal"))

            raf.penup()
            if box[2] > 9:
                raf.goto(245, 60)
            else:
                raf.goto(250, 60)
            raf.write(box[2], font=("Arial", 25, "normal"))

            raf.penup()
            if box[3] > 9:
                raf.goto(200, -95)
            else:
                raf.goto(205, -95)
            raf.write(box[3], font=("Arial", 25, "normal"))

            raf.penup()
            if box[4] > 9:
                raf.goto(70, -200)
            else:
                raf.goto(75, -200)
            raf.write(box[4], font=("Arial", 25, "normal"))

            raf.penup()
            if box[5] > 9:
                raf.goto(-90, -205)
            else:
                raf.goto(-85, -205)
            raf.write(box[5], font=("Arial", 25, "normal"))

            raf.penup()
            if box[6] > 9:
                raf.goto(-230, -115)
            else:
                raf.goto(-225, -115)
            raf.write(box[6], font=("Arial", 25, "normal"))

            raf.penup()
            if box[7] > 9:
                raf.goto(-285, 40)
            else:
                raf.goto(-280, 40)
            raf.write(box[7], font=("Arial", 25, "normal"))

            raf.penup()
            if box[8] > 9:
                raf.goto(-245, 195)
            else:
                raf.goto(-240, 195)
            raf.write(box[8], font=("Arial", 25, "normal"))

            raf.penup()
            if box[9] > 9:
                raf.goto(-115, 300)
            else:
                raf.goto(-110, 300)
            raf.write(box[9], font=("Arial", 25, "normal"))


        elif baseNumber == 11:
            randomnum3 = random.randint(4, 7)

            raf.speed(speed)

            raf.penup()
            raf.goto(-80, 280)
            for i in range(11):
                raf.penup()
                raf.forward(140)
                raf.pendown()
                raf.pensize(3.5)
                raf.pencolor(c_color)
                raf.circle(40)
                raf.right(360 / 11)
            raf.pencolor(f_color)

            raf.penup()
            if box[0] > 9:
                raf.goto(50, 305)
            else:
                raf.goto(55, 305)
            raf.write(box[0], font=("Arial", 25, "normal"))

            raf.penup()
            if box[1] > 9:
                raf.goto(190, 225)
            else:
                raf.goto(195, 225)
            raf.write(box[1], font=("Arial", 25, "normal"))

            raf.penup()
            if box[2] > 9:
                raf.goto(260, 80)
            else:
                raf.goto(265, 80)
            raf.write(box[2], font=("Arial", 25, "normal"))

            raf.penup()
            if box[3] > 9:
                raf.goto(245, -80)
            else:
                raf.goto(250, -80)
            raf.write(box[3], font=("Arial", 25, "normal"))

            raf.penup()
            if box[4] > 9:
                raf.goto(145, -210)
            else:
                raf.goto(150, -210)
            raf.write(box[4], font=("Arial", 25, "normal"))

            raf.penup()
            if box[5] > 9:
                raf.goto(0, -260)
            else:
                raf.goto(-5, -260)
            raf.write(box[5], font=("Arial", 25, "normal"))

            raf.penup()
            if box[6] > 9:
                raf.goto(-170, -220)
            else:
                raf.goto(-165, -220)
            raf.write(box[6], font=("Arial", 25, "normal"))

            raf.penup()
            if box[7] > 9:
                raf.goto(-280, -100)
            else:
                raf.goto(-275, -100)
            raf.write(box[7], font=("Arial", 25, "normal"))

            raf.penup()
            if box[8] > 9:
                raf.goto(-310, 60)
            else:
                raf.goto(-305, 60)
            raf.write(box[8], font=("Arial", 25, "normal"))

            raf.penup()
            if box[9] > 9:
                raf.goto(-250, 210)
            else:
                raf.goto(-240, 210)
            raf.write(box[9], font=("Arial", 25, "normal"))

            raf.penup()
            if box[10] > 9:
                raf.goto(-115, 300)
            else:
                raf.goto(-110, 300)
            raf.write(box[10], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(-688.0, 276.0)
        raf.pendown()
        raf.pencolor("#EEA3D7")
        raf.write("Chose a number from the circle.", font=("Arial", 30, "normal"))
        raf.penup()

        randomnum4 = (random.randint(1, 2))
        if randomnum4 == 1:
            rotate = "Rotate as clock-wise"
        else:
            rotate = "Rotate as anti clock-wise"

        def button_click(x, y):


            if (-453.0 >= x >= -553.0) and (246.0 >= y >= 209.0):
                raf.penup()
                raf.goto(158.0, -301.0)
                raf.pendown()  # button tag
                raf.pencolor("green")
                raf.write(rotate, font=("Arial", 25, "normal"))
                raf.penup()

                raf.penup()
                raf.pencolor("red")
                raf.goto(455.0, -297.0)
                raf.pendown()
                for i in range(2):  # button shape

                    raf.forward(100)
                    raf.left(90)
                    raf.forward(40)
                    raf.left(90)
                raf.penup()
                raf.goto(475.0, -288.0)
                raf.pendown()  # button tag
                raf.pencolor("Pink")
                raf.write("done", font=("Arial", 25, "normal"))
                raf.penup()

            elif (555.0 >= x >= 456.0) and (-259.0 >= y >= -297.0):
                raf.penup()
                raf.goto(260.0, 299.0)
                raf.pendown()  # button tag
                raf.pencolor("green")
                raf.write("Rotate as anti clock-wise", font=("Arial", 25, "normal"))
                raf.penup()

                raf.penup()
                raf.pencolor("red")
                raf.goto(586.0, 304.0)
                raf.pendown()
                for i in range(2):  # button shape

                    raf.forward(100)
                    raf.left(90)
                    raf.forward(40)
                    raf.left(90)
                raf.penup()
                raf.goto(609.0, 312.0)
                raf.pendown()  # button tag
                raf.pencolor("Pink")
                raf.write("done", font=("Arial", 25, "normal"))
                raf.penup()

            elif (687.0 >= x >= 586.0) and (340.0 >= y >= 304.0):
                raf.clear()
                p5.play5(randwall,randomnum3, randomNum1, randomNum2, baseNumber)  # ___ linked has been done







        turtle.onscreenclick(button_click, 1)
        turtle.listen()

        raf.penup()
        raf.pencolor("red")
        raf.goto(-554.0, 209.0)
        raf.pendown()
        for i in range(2):  # button shape

            raf.forward(100)
            raf.left(90)
            raf.forward(40)
            raf.left(90)

        raf.penup()
        raf.goto(-520.0, 215.0)
        raf.pendown()  # button tag
        raf.pencolor("green")
        raf.write("ok", font=("Arial", 25, "normal"))
        raf.penup()
        turtle.onscreenclick(button_click, 1)
        turtle.listen()

        turtle.done()
