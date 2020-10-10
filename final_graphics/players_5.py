import turtle
import random
from players_6 import players_6

class players_5:

    def play5(self,randwall, num, start, end, base_number):
        speed = 0
        c_color = "#FEF1EA"
        raf = turtle.Turtle()
        turtle.bgpic(randwall)
        p6=players_6()

        if num == 4:
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

            raf = turtle.Turtle()
            raf.speed(speed)
            raf.penup()
            raf.goto(-90, 190)
            for i in range(4):
                raf.penup()
                raf.forward(160)
                raf.pendown()
                raf.pensize(3.5)
                raf.pencolor(c_color)
                raf.circle(50)
                raf.right(360 / 4)

            raf.penup()
            if b[0] > 9:
                raf.goto(50, 225)
            else:
                raf.goto(60, 225)
            raf.pencolor("red")
            raf.write(b[0], font=("Arial", 35, "normal"))

            raf.penup()
            if b[1] > 9:
                raf.goto(100, 10)
            else:
                raf.goto(110, 10)
            raf.pencolor("red")
            raf.write(b[1], font=("Arial", 35, "normal"))

            raf.penup()
            if b[2] > 9:
                raf.goto(-110, -35)
            else:
                raf.goto(-100, -35)
            raf.pencolor("red")
            raf.write(b[2], font=("Arial", 35, "normal"))

            raf.penup()
            if b[3] > 9:
                raf.goto(-160, 175)
            else:
                raf.goto(- 150, 175)
            raf.pencolor("red")
            raf.write(b[3], font=("Arial", 35, "normal"))

        elif num == 5:
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

            raf = turtle.Turtle()

            raf.penup()
            raf.goto(-90, 190)
            for i in range(5):
                raf.penup()
                raf.forward(160)
                raf.pendown()
                raf.pensize(3.5)
                raf.pencolor(c_color)
                raf.circle(50)
                raf.right(360 / 5)

            raf.penup()
            if b[0] > 9:
                raf.goto(50, 220)
            else:
                raf.goto(60, 220)
            raf.write(b[0], font=("Arial", 35, "normal"))

            raf.penup()
            if b[1] > 9:
                raf.goto(145, 30)
            else:
                raf.goto(155, 30)
            raf.write(b[1], font=("Arial", 35, "normal"))

            raf.penup()
            if b[2] > 9:
                raf.goto(0, -115)
            else:
                raf.goto(10, -115)
            raf.write(b[2], font=("Arial", 35, "normal"))

            raf.penup()
            if b[3] > 9:
                raf.goto(-190, -20)
            else:
                raf.goto(-180, -20)
            raf.write(b[3], font=("Arial", 35, "normal"))

            raf.penup()
            if b[4] > 9:
                raf.goto(-160, 185)
            else:
                raf.goto(- 150, 185)
            raf.write(b[4], font=("Arial", 35, "normal"))

        elif num == 6:

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

            raf = turtle.Turtle()

            raf.speed(speed)

            raf.penup()
            raf.goto(-90, 190)
            for i in range(6):
                raf.penup()
                raf.forward(160)
                raf.pendown()
                raf.pensize(3.5)
                raf.pencolor(c_color)
                raf.circle(50)
                raf.right(360 / 6)

            raf.penup()
            if b[0] > 9:
                raf.goto(50, 220)
            else:
                raf.goto(60, 220)
            raf.write(b[0], font=("Arial", 35, "normal"))

            raf.penup()
            if b[1] > 9:
                raf.goto(175, 60)
            else:
                raf.goto(185, 60)
            raf.write(b[1], font=("Arial", 35, "normal"))

            raf.penup()
            if b[2] > 9:
                raf.goto(95, -130)
            else:
                raf.goto(105, -130)
            raf.write(b[2], font=("Arial", 35, "normal"))

            raf.penup()
            if b[3] > 9:
                raf.goto(-110, -160)
            else:
                raf.goto(-100, -160)
            raf.write(b[3], font=("Arial", 35, "normal"))

            raf.penup()
            if b[4] > 9:
                raf.goto(-235, 10)
            else:
                raf.goto(-225, 10)
            raf.write(b[4], font=("Arial", 35, "normal"))

            raf.penup()
            if b[5] > 9:
                raf.goto(-155, 200)
            else:
                raf.goto(-145, 200)
            raf.write(b[5], font=("Arial", 35, "normal"))

        elif num == 7:

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

            raf = turtle.Turtle()
            raf.speed(speed)

            raf.penup()
            raf.goto(-90, 190)
            for i in range(7):
                raf.penup()
                raf.forward(160)
                raf.pendown()
                raf.pensize(3.5)
                raf.pencolor(c_color)
                raf.circle(50)
                raf.right(360 / 7)

            raf.penup()
            if b[0] > 9:
                raf.goto(50, 222)
            else:
                raf.goto(60, 222)
            raf.write(b[0], font=("Arial", 35, "normal"))

            raf.penup()
            if b[1] > 9:
                raf.goto(190, 80)
            else:
                raf.goto(200, 80)
            raf.write(b[1], font=("Arial", 35, "normal"))

            raf.penup()
            if b[2] > 9:
                raf.goto(160, -120)
            else:
                raf.goto(170, -120)
            raf.write(b[2], font=("Arial", 35, "normal"))

            raf.penup()
            if b[3] > 9:
                raf.goto(-5, -225)
            else:
                raf.goto(5, -225)
            raf.write(b[3], font=("Arial", 35, "normal"))

            raf.penup()
            if b[4] > 9:
                raf.goto(-200, -155)
            else:
                raf.goto(-190, -155)
            raf.write(b[4], font=("Arial", 35, "normal"))

            raf.penup()
            if b[5] > 9:
                raf.goto(-260, 35)
            else:
                raf.goto(-250, 35)
            raf.write(b[5], font=("Arial", 35, "normal"))

            raf.penup()
            if b[6] > 9:
                raf.goto(-150, 200)
            else:
                raf.goto(-140, 200)
            raf.write(b[6], font=("Arial", 35, "normal"))

        elif num == 8:
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

            raf = turtle.Turtle()
            raf.speed(speed)

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

            raf.penup()
            if b[0] > 9:
                raf.goto(50, 225)
            else:
                raf.goto(60, 225)
            raf.write(b[0], font=("Arial", 35, "normal"))

            raf.penup()
            if b[1] > 9:
                raf.goto(195, 95)
            else:
                raf.goto(205, 95)
            raf.write(b[1], font=("Arial", 35, "normal"))

            raf.penup()
            if b[2] > 9:
                raf.goto(215, -105)
            else:
                raf.goto(225, -105)
            raf.write(b[2], font=("Arial", 35, "normal"))

            raf.penup()
            if b[3] > 9:
                raf.goto(85, -255)
            else:
                raf.goto(95, -255)
            raf.write(b[3], font=("Arial", 35, "normal"))

            raf.penup()
            if b[4] > 9:
                raf.goto(-110, -265)
            else:
                raf.goto(-100, -265)
            raf.write(b[4], font=("Arial", 35, "normal"))

            raf.penup()
            if b[5] > 9:
                raf.goto(-260, -140)
            else:
                raf.goto(-250, -140)
            raf.write(b[5], font=("Arial", 35, "normal"))

            raf.penup()
            if b[6] > 9:
                raf.goto(-275, 60)
            else:
                raf.goto(-265, 60)
            raf.write(b[6], font=("Arial", 35, "normal"))

            raf.penup()
            if b[7] > 9:
                raf.goto(-145, 210)
            else:
                raf.goto(-135, 210)
            raf.write(b[7], font=("Arial", 35, "normal"))


        elif num == 9:
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

            raf = turtle.Turtle()
            raf.speed(speed)

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

            raf.penup()
            if b[0] > 9:
                raf.goto(45, 305)
            else:
                raf.goto(50, 305)
            raf.write(b[0], font=("Arial", 25, "normal"))

            raf.penup()
            if b[1] > 9:
                raf.goto(180, 205)
            else:
                raf.goto(185, 205)
            raf.write(b[1], font=("Arial", 25, "normal"))

            raf.penup()
            if b[2] > 9:
                raf.goto(220, 45)
            else:
                raf.goto(225, 45)
            raf.write(b[2], font=("Arial", 25, "normal"))

            raf.penup()
            if b[3] > 9:
                raf.goto(145, -100)
            else:
                raf.goto(150, -100)
            raf.write(b[3], font=("Arial", 25, "normal"))

            raf.penup()
            if b[4] > 9:
                raf.goto(-10, -170)
            else:
                raf.goto(-5, -170)
            raf.write(b[4], font=("Arial", 25, "normal"))

            raf.penup()
            if b[5] > 9:
                raf.goto(-170, -120)
            else:
                raf.goto(-165, -120)
            raf.write(b[5], font=("Arial", 25, "normal"))

            raf.penup()
            if b[6] > 9:
                raf.goto(-260, 20)
            else:
                raf.goto(-255, 20)
            raf.write(b[6], font=("Arial", 25, "normal"))

            raf.penup()
            if b[7] > 9:
                raf.goto(-240, 185)
            else:
                raf.goto(-235, 185)
            raf.write(b[7], font=("Arial", 25, "normal"))

            raf.penup()
            if b[8] > 9:
                raf.goto(-115, 300)
            else:
                raf.goto(-110, 300)
            raf.write(b[8], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(-546.0, 267.0)
        raf.pendown()
        raf.pencolor("#EEA3D7")
        raf.write("Just one step", font=("Arial", 40, "normal"))
        raf.penup()

        randomnum4 = (random.randint(1, 2))
        if randomnum4 == 1:
            rotate = "Rotate as clock-wise"
        else:
            rotate = "Rotate as anti clock-wise"



        def button_click(x, y):


            if (-376.0 >= x >= -475.0) and (236.0 >= y >= 198.0):

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
                raf.clear()
                p6.play6(randwall, randomnum4, b, num, base_number, randomnum1)

        turtle.onscreenclick(button_click, 1)
        turtle.listen()
        raf.penup()
        raf.pencolor("red")
        raf.goto(-475.0, 200.0)
        raf.pendown()
        for i in range(2):  # button shape

            raf.forward(100)
            raf.left(90)
            raf.forward(40)
            raf.left(90)
        raf.penup()

        raf.goto(-442.0, 210.0)
        raf.pendown()
        raf.pencolor("Red")
        raf.write("ok", font=("Arial", 25, "normal"))
        raf.penup()
