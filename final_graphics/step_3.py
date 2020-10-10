import turtle
from track import track
import random
import os

t = track()


class step_3:

    def stp3(self, randwall, randomnum4, b, last_box, base_number, base_index):

        raf = turtle.Turtle()
        rafwin = turtle.Screen()

        turtle.bgpic(randwall)

        c = t.clock(last_box, base_number, base_index)
        ac = t.anti_clock(last_box, base_number, base_index)
        speed = 0
        c_color = "#FEF1EA"

        def button_click(x, y):
            print(x, y)
            if (561.0 >= x >= 262.0) and (82.0 >= y >= 15.0):
                raf.clear()

                raf.pencolor("green")
                raf.goto(-315.0, -37.0)
                raf.pendown()
                raf.pensize(3.5)
                for i in range(2):  # button shape

                    raf.forward(700)
                    raf.left(90)
                    raf.forward(150)
                    raf.left(90)
                raf.penup()

                raf.goto(-140.0, 6.0)
                raf.pendown()
                raf.pencolor("blue")
                raf.write("Thank You", font=("Arial", 70, "normal"))
                raf.penup()

            elif (463.0 >= x >= 359.0) and (-40.0 >= y >= -134.0):
                raf.clear()

                raf.pencolor("green")
                raf.goto(-315.0, -37.0)
                raf.pendown()
                raf.pensize(3.5)
                for i in range(2):  # button shape

                    raf.forward(700)
                    raf.left(90)
                    raf.forward(150)
                    raf.left(90)
                raf.penup()

                raf.goto(-280, 6.0)
                raf.pendown()
                raf.pencolor("Red")
                raf.write("You are not Good in counting", font=("Arial", 48, "normal"))
                raf.penup()

                ##--- next call_____

        turtle.onscreenclick(button_click, 1)
        turtle.listen()

        raf.penup()

        raf.goto(-699.0, 338.0)
        raf.pendown()
        raf.pencolor("blue")
        raf.write("Is that on your mind?", font=("Arial", 45, "normal"))

        raf.speed(7)

        raf.penup()
        if randomnum4 == 1:
            if b[c] < c:
                raf.goto(-110.0, -97.0)
            else:
                raf.goto(-175.0, -97.0)
            raf.pendown()
            raf.pencolor("red")
            raf.write(b[c], font=("Arial", 300, "normal"))
            raf.penup()
        else:
            if b[c] < c:
                raf.goto(-110.0, -97.0)
            else:
                raf.goto(-175, -97.0)
            raf.pendown()
            raf.pencolor("Orange")
            raf.write(b[ac], font=("Arial", 300, "normal"))
            raf.penup()

        raf.pencolor("green")
        raf.goto(261.0, 15)
        raf.pensize(3.5)
        raf.pendown()
        for i in range(2):  # button shape

            raf.forward(300)
            raf.left(90)
            raf.forward(70)
            raf.left(90)
        raf.penup()

        raf.goto(411.0, -155.0)
        raf.pendown()
        raf.pensize(3.5)
        raf.pencolor("Red")
        raf.circle(70)
        raf.penup()

        raf.goto(362.0, 29.0)
        raf.pendown()
        raf.pencolor("blue")
        raf.write("Yes", font=("Arial", 45, "normal"))
        raf.penup()

        raf.goto(380.0, -111.0)
        raf.pendown()
        raf.pencolor("blue")
        raf.write("No", font=("Arial", 45, "normal"))
        raf.penup()


        turtle.done()
