import turtle
import os
import random
from track import track
from step_3 import step_3


class players_7:
    def play7(self, assume, randwall, randomnum4, b, last_box, base_number, base_index):

        raf = turtle.Turtle()
        rafwin = turtle.Screen()

        t = track()
        s3 = step_3()

        turtle.bgpic(randwall)
        turtle.title("Hypnos")

        if randomnum4 == 1:
            track_num=t.clock(last_box, base_number, base_index)

        else:
            track_num=t.anti_clock(last_box, base_number, base_index)




        if assume == b[track_num]:
            s3.stp3(randwall, randomnum4, b, last_box, base_number, base_index)


        else:
            raf.penup()
            raf.pensize()
            raf.goto(-182.0, 19.0)  # button tag
            raf.pendown()
            raf.pencolor("red")
            raf.write("You are not a pro...Try again", font=("Arial", 35, "normal"))
            raf.penup()
            flag = 1

        def button_click(x, y):  # button action
            print(x, y)

        turtle.listen()
        turtle.onscreenclick(button_click, 1)

        turtle.done()
