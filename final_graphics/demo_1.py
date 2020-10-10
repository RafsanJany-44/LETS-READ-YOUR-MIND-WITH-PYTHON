import turtle
import os
from demo_2 import demo_2

class demo_1:

    def demo1(self, randwall):

        raf = turtle.Turtle()
        rafwin = turtle.Screen()
        d1 = demo_2()

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
        raf.write("Here is a li'l demonstration of this program..", font=("Arial", 40, "normal"))
        raf.penup()

        raf.penup()
        raf.goto(48.0, 150)
        raf.pendown()
        raf.pencolor("#EEA3D7")
        raf.write("*You will be given a cycle of numbers.", font=("Arial", 30, "normal"))
        raf.penup()

        raf.penup()
        raf.goto(10, 50)
        raf.pendown()
        raf.pencolor("#EEA3D7")
        raf.write("*You have to assume a number from that circle.", font=("Arial", 30, "normal"))
        raf.penup()


        raf.penup()
        raf.goto(10, -10)
        raf.pendown()
        raf.pencolor("#EEA3D7")
        raf.write("*You just have to take decision.....Nothing else.", font=("Arial", 30, "normal"))
        raf.penup()



        raf.penup()
        raf.goto(0, -50)
        raf.pendown()
        raf.pencolor("#EEA3D7")
        raf.write("*Do not tell anything about what's going on your mind.", font=("Arial", 30, "normal"))
        raf.penup()



        def button_click(x, y):  # button action
            print(x, y)

            if (251.0 <= x <= 349.0) and (-166.0 <= y <= -130.0):
                #raf.clear()
                rafwin.clear()
                d1.demo2(randwall)  # __ linked has been done




        raf.penup()
        raf.pencolor("#FF8232")
        raf.goto(250.0, -166.0)
        raf.pendown()
        for i in range(2):  # button shape

            raf.forward(100)
            raf.left(90)
            raf.forward(40)
            raf.left(90)
        raf.penup()


        raf.goto(273.0, -158.0)  # button tag
        raf.pendown()
        raf.pencolor("red")
        raf.write("Next", font=("Arial", 25, "normal"))
        raf.penup()

        raf.goto(-340.0, -70)

        raf.penup()
        turtle.listen()
        turtle.onscreenclick(button_click, 1)

        while True:  # button shape

            raf.forward(150)
            raf.left(360 / 5)

        turtle.done()
