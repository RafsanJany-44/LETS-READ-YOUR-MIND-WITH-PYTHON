import turtle
import time
from step_1 import step_1

class demo_2:

    def demo2(self, randwall):

        raf = turtle.Turtle()
        s1 = step_1()

        turtle.bgpic(randwall)
        turtle.title("Hypnos")

        raf.penup()
        raf.goto(-30, 250)
        raf.pendown()
        raf.pencolor("#EEA3D7")
        raf.write("*Let assume that you've selected 4 from the circle.", font=("Arial", 30, "normal"))
        raf.penup()

        c_color = "#ffdfe5"
        f_color = ("red")
        speed = 0

        i = -300
        j = -40
        raf.speed(speed)

        box = [2, 3, 4, 6, 8, 9, 10, 11, 12]

        raf.penup()
        raf.goto(-80 + i, 280 + j)
        for e in range(9):
            if e == 2:
                raf.penup()
                raf.forward(140)
                raf.pendown()
                raf.pensize(3.5)
                raf.begin_fill()
                raf.color('white', 'red')
                raf.circle(40)
                raf.right(360 / 9)
                raf.end_fill()

            else:
                raf.penup()
                raf.forward(140)
                raf.pendown()
                raf.pensize(3.5)
                raf.pencolor(c_color)
                raf.circle(40)
                raf.right(360 / 9)

        raf.pencolor(f_color)

        raf.penup()
        raf.goto(50 + i, 305 + j)
        raf.write(box[0], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(185 + i, 205 + j)
        raf.write(box[1], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(225 + i, 45 + j)
        raf.pencolor("blue")
        raf.write(box[2], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(150 + i, -100 + j)
        raf.pencolor("red")
        raf.write(box[3], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(-5 + i, -170 + j)
        raf.write(box[4], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(-165 + i, -120 + j)
        raf.write(box[5], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(-255 + i, 20 + j)
        raf.write(box[6], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(-240 + i, 185 + j)
        raf.write(box[7], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(-115 + i, 300 + j)
        raf.write(box[8], font=("Arial", 25, "normal"))

        time.sleep(4)

        raf.penup()
        raf.goto(-20, 100)
        raf.pendown()
        raf.pencolor("#EEA3D7")
        raf.write("And you are instructed to go ""ANTI_CLOCK_WISE"",",
                  font=("Arial", 30, "normal"))
        raf.penup()

        time.sleep(4)

        raf.penup()
        raf.goto(-20, 30)
        raf.pendown()
        raf.pencolor("#EEA3D7")
        raf.write("You have to go 4 cycle behind:.",
                  font=("Arial", 30, "normal"))
        raf.penup()

        time.sleep(3)

        raf.penup()
        raf.goto(-20 + 250, -10 - 50)
        raf.pendown()
        raf.pencolor("Yellow")
        raf.write("  3",
                  font=("Arial", 50, "normal"))
        raf.penup()

        raf.penup()
        raf.goto(185 + i, 205 + j)
        raf.pencolor("Yellow")
        raf.write(box[1], font=("Arial", 25, "normal"))

        time.sleep(2)

        raf.penup()
        raf.goto(-20 + 250, -50 - 50)
        raf.pendown()
        raf.pencolor("Yellow")
        raf.write("    2",
                  font=("Arial", 50, "normal"))
        raf.penup()

        raf.penup()
        raf.goto(50 + i, 305 + j)
        raf.pencolor("Yellow")
        raf.write(box[0], font=("Arial", 25, "normal"))

        time.sleep(2)

        raf.penup()
        raf.goto(-20 + 250, -90 - 50)
        raf.pendown()
        raf.pencolor("Yellow")
        raf.write("     12",
                  font=("Arial", 50, "normal"))
        raf.penup()

        raf.penup()
        raf.goto(-115 + i, 300 + j)
        raf.pencolor("Yellow")
        raf.write(box[8], font=("Arial", 25, "normal"))

        time.sleep(2)

        raf.penup()
        raf.goto(-20 + 250, -130 - 50)
        raf.pendown()
        raf.pencolor("Yellow")
        raf.write("       11",
                  font=("Arial", 50, "normal"))
        raf.penup()

        raf.penup()
        raf.goto(-240 + i, 185 + j)
        raf.pencolor("Yellow")
        raf.write(box[7], font=("Arial", 25, "normal"))

        raf.penup()
        raf.goto(-20, -240)
        raf.pendown()
        raf.pencolor("Yellow")
        raf.write("Your Final number is this...11",
                  font=("Arial", 30, "normal"))
        raf.penup()
        raf.goto(-20, -270)
        raf.pendown()
        raf.pencolor("Yellow")
        raf.write("Just follow the instructions",
                  font=("Arial", 25, "normal"))

        def button_click(x, y):  # button action

            if (107.0 <= x <= 405.0) and (-352.0 <= y <= -311.0):
                raf.clear()
                s1.stp1(randwall)


        raf.penup()
        raf.pencolor("#FF8232")
        raf.goto(106.0, -350.0)
        raf.pendown()
        for i in range(2):  # button shape

            raf.forward(300)
            raf.left(90)
            raf.forward(40)
            raf.left(90)
        raf.penup()

        raf.goto(200, -340.0)  # button tag
        raf.pendown()
        raf.pencolor("red")
        raf.write("Lets Start", font=("Arial", 25, "normal"))
        raf.penup()


        turtle.listen()
        turtle.onscreenclick(button_click, 1)

        turtle.done()
