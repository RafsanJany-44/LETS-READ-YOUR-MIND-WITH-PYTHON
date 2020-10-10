import turtle
import os
import random
from players_7 import players_7

class players_6:
    def play6(self, randwall, randomnum4, b, last_box, base_number, base_index):

        raf = turtle.Turtle()
        rafwin = turtle.Screen()
        p7=players_7()

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

            print(randomnum4)




        def button_click(x, y):  # button action


            if 142 <= y <= 182:
                if -290 <= x <= -190:
                    raf.clear()
                    p7.play7(1, randwall, randomnum4, b, last_box, base_number, base_index)

                elif -129 <= x <= -31:

                    raf.clear()
                    p7.play7(2, randwall, randomnum4, b, last_box, base_number, base_index)

                elif 32 <= x <= 132:

                    raf.clear()
                    p7.play7(3, randwall, randomnum4, b, last_box, base_number, base_index)

                elif 191 <= x <= 291:

                    raf.clear()
                    p7.play7(4, randwall, randomnum4, b, last_box, base_number, base_index)

            if -9 <= y <= 30:
                if -290 <= x <= -190:

                    raf.clear()
                    p7.play7(5, randwall, randomnum4, b, last_box, base_number, base_index)

                elif -129 <= x <= -31:

                    raf.clear()
                    p7.play7(6, randwall, randomnum4, b, last_box, base_number, base_index)

                elif 32 <= x <= 132:

                    raf.clear()
                    p7.play7(7, randwall, randomnum4, b, last_box, base_number, base_index)

                elif 191 <= x <= 291:

                    raf.clear()
                    p7.play7(8, randwall, randomnum4, b, last_box, base_number, base_index)

            if -160 <= y <= -120 :
                if -290 <= x <= -190:

                    raf.clear()
                    p7.play7(9, randwall, randomnum4, b, last_box, base_number, base_index)

                elif -129 <= x <= -31:

                    raf.clear()
                    p7.play7(10, randwall, randomnum4, b, last_box, base_number, base_index)

                elif 32 <= x <= 132:

                    raf.clear()
                    p7.play7(11, randwall, randomnum4, b, last_box, base_number, base_index)

                elif 191 <= x <= 291:

                    raf.clear()
                    p7.play7(12, randwall, randomnum4, b, last_box, base_number, base_index)


        raf.goto(-370, 301.0)  # button tag
        raf.pendown()
        raf.pencolor("red")
        raf.write("Now select the number which will be inside your Audiences' mind.", font=("Arial", 25, "normal"))
        raf.penup()



        turtle.listen()
        turtle.onscreenclick(button_click, 1)

        turtle.done()
