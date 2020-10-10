import turtle
import os
import random
from players_3 import players_3


class players_2:
    def play2(self, start, randwall):

        raf = turtle.Turtle()
        rafwin = turtle.Screen()
        p3 = players_3()

        turtle.bgpic(randwall)
        turtle.title("Hypnos")

        u = 150
        raf.penup()
        raf.goto(-450, 143.0)
        raf.speed(0)
        for x in range(3):
            for i in range(4):
                raf.penup()
                raf.forward(160)
                raf.pendown()
                raf.pensize(3)
                raf.pencolor("red")
                for j in range(2):  # button shape

                    raf.forward(100)
                    raf.left(90)
                    raf.forward(40)
                    raf.left(90)
            raf.penup()
            raf.goto(-450, 143 - u)
            u = u + 150

        v = 0
        z = 149
        for x in range(3):
            w = -249
            for i in range(4):
                v += 1
                raf.penup()
                raf.goto(w, z)
                raf.pendown()  # button tag
                raf.pencolor("Pink")
                raf.write(v, font=("Arial", 25, "normal"))
                raf.penup()
                w = w + 160

            z = z - 150
            raf.goto(w, z)

        def button_click(x, y):

            if 142 <= y <= 182:
                if -290 <= x <= -190:
                    raf.clear()
                    p3.play3(start, 1, randwall)

                elif -129 <= x <= -31:

                    raf.clear()
                    p3.play3(start, 2, randwall)

                elif 32 <= x <= 132:

                    raf.clear()
                    p3.play3(start, 3, randwall)

                elif 191 <= x <= 291:

                    raf.clear()
                    p3.play3(start, 4, randwall)

            if -9 <= y <= 30:
                if -290 <= x <= -190:

                    raf.clear()
                    p3.play3(start, 5, randwall)

                elif -129 <= x <= -31:

                    raf.clear()
                    p3.play3(start, 6, randwall)

                elif 32 <= x <= 132:

                    raf.clear()
                    p3.play3(start, 7, randwall)

                elif 191 <= x <= 291:

                    raf.clear()
                    p3.play3(start,8, randwall)

            if -160 <= y <= -120:
                if -290 <= x <= -190:

                    raf.clear()
                    p3.play3(start, 9, randwall)

                elif -129 <= x <= -31:

                    raf.clear()
                    p3.play3(start, 10, randwall)

                elif 32 <= x <= 132:

                    raf.clear()
                    p3.play3(start, 11, randwall)

                elif 191 <= x <= 291:

                    raf.clear()
                    p3.play3(start, 12, randwall)

        raf.goto(-343.0, 301.0)  # button tag
        raf.pendown()
        raf.pencolor("red")
        raf.write("Now select the end number of the circle.", font=("Arial", 40, "normal"))
        raf.penup()

        turtle.listen()
        turtle.onscreenclick(button_click, 1)

        turtle.done()
