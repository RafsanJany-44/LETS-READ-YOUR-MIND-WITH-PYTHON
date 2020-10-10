import turtle
import os
import random
from players_4 import players_4


class players_3:
    def play3(self, start, end, randwall):

        p4=players_4()
        raf = turtle.Turtle()
        rafwin = turtle.Screen()

        turtle.bgpic(randwall)
        turtle.title("Hypnos")

        if 2 <= start <= 8 and 6 <= end <= 12:
            if start != 5 and end != 8:
                p4.play4(start,end,randwall)
            else:
                raf.goto(-671.0, 308.0)  # button tag
                raf.pendown()
                raf.pencolor("red")
                raf.write("not possible..you are not a pro...try again", font=("Arial", 25, "normal"))
                raf.penup()
                flag = 1
        else:
            raf.goto(-671.0, 308.0)  # button tag
            raf.pendown()
            raf.pencolor("red")
            raf.write("not possible..you are not a pro...try again", font=("Arial", 25, "normal"))
            raf.penup()
            flag = 1

        def button_click(x, y):  # button action
            print()

        turtle.listen()
        turtle.onscreenclick(button_click, 1)

        turtle.done()
