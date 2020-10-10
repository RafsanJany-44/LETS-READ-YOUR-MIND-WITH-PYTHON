import turtle
import os
from step_1 import step_1
import random
from demo_1 import demo_1
from players_1 import players_1

raf = turtle.Turtle()
rafwin = turtle.Screen()
s1 = step_1()
d1 = demo_1()
p1 = players_1()

wall = ["10.gif"]
randwall = random.choice(wall)
turtle.bgpic(randwall)
turtle.title("Hypnos")

raf.penup()
raf.goto(620, 350)
rafwin.addshape(os.path.expanduser("croc1.gif"))
raf.shape(os.path.expanduser("croc1.gif"))

raf.penup()
raf.goto(-600, 320)
raf.pendown()
raf.pencolor("#EEA3D7")
raf.write("Hay There! Welcome to a clever program that can track your mind.", font=("Arial", 40, "normal"))
raf.penup()

raf.penup()
raf.goto(48.0, 210.0)
raf.pendown()
raf.pencolor("#EEA3D7")
raf.write("Have you seen this before??", font=("Arial", 30, "normal"))
raf.penup()


def button_click(x, y):  # button action

    if (97 <= x <= 196) and (144 <= y <= 181):
        # raf.clear()
        rafwin.clear()
        s1.stp1(randwall)  # __ linked has been donee
    elif (351 <= x <= 451) and (141 <= y <= 182):
        rafwin.clear()
        d1.demo1(randwall)
    elif (86 <= x <= 586) and (-275 <= y <= -195):
        rafwin.clear()
        p1.play1(randwall)


raf.penup()
raf.pencolor("#FF8232")
raf.goto(96.0, 144.0)
raf.pendown()
raf.pensize(3)
for i in range(2):  # button shape

    raf.forward(100)
    raf.left(90)
    raf.forward(40)
    raf.left(90)
raf.penup()

raf.penup()
raf.pencolor("#FF8232")
raf.goto(350, 144.0)
raf.pendown()
for i in range(2):  # button shape

    raf.forward(100)
    raf.left(90)
    raf.forward(40)
    raf.left(90)
raf.penup()

raf.goto(122.0, 150)  # button tag
raf.pendown()
raf.pencolor("#2DFF00")
raf.write("Yes", font=("Arial", 25, "normal"))
raf.penup()

raf.goto(376.0, 150)  # button tag
raf.pendown()
raf.pencolor("red")
raf.write("No", font=("Arial", 25, "normal"))
raf.penup()

raf.penup()
raf.pencolor("#FF8232")
raf.goto(85.0, -273.0)
raf.pendown()
for i in range(2):  # button shape

    raf.forward(500)
    raf.left(90)
    raf.forward(80)
    raf.left(90)
raf.penup()

raf.goto(265.0, -257.0)  # button tag
raf.pendown()
raf.pencolor("red")
raf.write("I'm PRO!", font=("Arial", 40, "normal"))
raf.penup()

raf.goto(-340.0, -70)

raf.penup()
turtle.listen()
turtle.onscreenclick(button_click, 1)

while True:
    raf.forward(150)
    raf.left(360 / 5)
turtle.done()
