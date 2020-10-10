import turtle

class circle_1:
    c_color = "#ffdfe5"
    f_color = "#f0"
    speed = 0

    def print_4(self, a, b, c, d):

        raf = turtle.Turtle()

        raf.speed(self.speed)

        raf.penup()
        raf.goto(-90, 190)
        for i in range(4):
            raf.penup()
            raf.forward(160)
            raf.pendown()
            raf.pencolor(self.c_color)
            raf.circle(50)
            raf.right(360 / 4)

        raf.penup()
        if a > 9:
            raf.goto(50, 225)
        else:
            raf.goto(60, 225)
        raf.pencolor("red")
        raf.write(a, font=("Arial", 35, "normal"))

        raf.penup()
        if b > 9:
            raf.goto(110, -115)
        else:
            raf.goto(110, 10)
        raf.pencolor("red")
        raf.write(b, font=("Arial", 35, "normal"))

        raf.penup()
        if c > 9:
            raf.goto(-110, -35)
        else:
            raf.goto(-100, -35)
        raf.pencolor("red")
        raf.write(c, font=("Arial", 35, "normal"))

        raf.penup()
        if d > 9:
            raf.goto(-160, 175)
        else:
            raf.goto(- 150, 175)
        raf.pencolor("red")
        raf.write(d, font=("Arial", 35, "normal"))

    def print_5(self, a, b, c, d, e):

        raf = turtle.Turtle()

        raf.speed(self.speed)

        raf.penup()
        raf.goto(-90, 190)
        for i in range(5):
            raf.penup()
            raf.forward(160)
            raf.pendown()
            raf.pensize(3.5)
            raf.pencolor(self.c_color)
            raf.circle(50)
            raf.right(360 / 5)

        raf.penup()
        if a > 9:
            raf.goto(50, 220)
        else:
            raf.goto(60, 220)
        raf.write(a, font=("Arial", 35, "normal"))

        raf.penup()
        if b > 9:
            raf.goto(145, 30)
        else:
            raf.goto(155, 30)
        raf.write(b, font=("Arial", 35, "normal"))

        raf.penup()
        if c > 9:
            raf.goto(0, -115)
        else:
            raf.goto(10, -115)
        raf.write(c, font=("Arial", 35, "normal"))

        raf.penup()
        if d > 9:
            raf.goto(-190, -20)
        else:
            raf.goto(-180, -20)
        raf.write(d, font=("Arial", 35, "normal"))

        raf.penup()
        if e > 9:
            raf.goto(-160, 185)
        else:
            raf.goto(- 150, 185)
        raf.write(e, font=("Arial", 35, "normal"))

        raf.clear()

    def print_6(self, a, b, c, d, e, f):
        raf = turtle.Turtle()

        raf.speed(self.speed)

        raf.penup()
        raf.goto(-90, 190)
        for i in range(6):
            raf.penup()
            raf.forward(160)
            raf.pendown()
            raf.pencolor(self.c_color)
            raf.circle(50)
            raf.right(360 / 6)

        raf.penup()
        if a > 9:
            raf.goto(50, 220)
        else:
            raf.goto(60, 220)
        raf.write(a, font=("Arial", 35, "normal"))

        raf.penup()
        if b > 9:
            raf.goto(175, 60)
        else:
            raf.goto(185, 60)
        raf.write(b, font=("Arial", 35, "normal"))

        raf.penup()
        if c > 9:
            raf.goto(95, -130)
        else:
            raf.goto(105, -130)
        raf.write(c, font=("Arial", 35, "normal"))

        raf.penup()
        if d > 9:
            raf.goto(-110, -160)
        else:
            raf.goto(-100, -160)
        raf.write(d, font=("Arial", 35, "normal"))

        raf.penup()
        if e > 9:
            raf.goto(-235, 10)
        else:
            raf.goto(-225, 10)
        raf.write(e, font=("Arial", 35, "normal"))

        raf.penup()
        if f > 9:
            raf.goto(-155, 200)
        else:
            raf.goto(-145, 200)
        raf.write(f, font=("Arial", 35, "normal"))

    def print_7(self, a, b, c, d, e, f, g):

        raf = turtle.Turtle()
        raf.speed(self.speed)

        raf.penup()
        raf.goto(-90, 190)
        for i in range(7):
            raf.penup()
            raf.forward(160)
            raf.pendown()
            raf.pencolor(self.c_color)
            raf.pensize(3.5)
            raf.circle(50)
            raf.right(360 / 7)

        raf.penup()
        if a > 9:
            raf.goto(50, 222)
        else:
            raf.goto(60, 222)
        raf.write(a, font=("Arial", 35, "normal"))

        raf.penup()
        if b > 9:
            raf.goto(190, 80)
        else:
            raf.goto(200, 80)
        raf.write(b, font=("Arial", 35, "normal"))

        raf.penup()
        if c > 9:
            raf.goto(160, -120)
        else:
            raf.goto(170, -120)
        raf.write(c, font=("Arial", 35, "normal"))

        raf.penup()
        if d > 9:
            raf.goto(-5, -225)
        else:
            raf.goto(5, -225)
        raf.write(d, font=("Arial", 35, "normal"))

        raf.penup()
        if e > 9:
            raf.goto(-200, -155)
        else:
            raf.goto(-190, -155)
        raf.write(e, font=("Arial", 35, "normal"))

        raf.penup()
        if f > 9:
            raf.goto(-260, 35)
        else:
            raf.goto(-250, 35)
        raf.write(f, font=("Arial", 35, "normal"))

        raf.penup()
        if g > 9:
            raf.goto(-150, 200)
        else:
            raf.goto(-140, 200)
        raf.write(g, font=("Arial", 35, "normal"))

    def print_8(self, a, b, c, d, e, f, g, h):

        raf = turtle.Turtle()
        raf.speed(self.speed)

        raf.penup()
        raf.goto(-90, 190)
        for i in range(8):
            raf.penup()
            raf.forward(160)
            raf.pendown()
            raf.pensize(3.5)
            raf.pencolor(self.c_color)
            raf.circle(50)
            raf.right(360 / 8)

        raf.penup()
        if a > 9:
            raf.goto(50, 225)
        else:
            raf.goto(60, 225)
        raf.write(a, font=("Arial", 35, "normal"))

        raf.penup()
        if b > 9:
            raf.goto(195, 95)
        else:
            raf.goto(205, 95)
        raf.write(b, font=("Arial", 35, "normal"))

        raf.penup()
        if c > 9:
            raf.goto(215, -105)
        else:
            raf.goto(225, -105)
        raf.write(c, font=("Arial", 35, "normal"))

        raf.penup()
        if d > 9:
            raf.goto(85, -255)
        else:
            raf.goto(95, -255)
        raf.write(d, font=("Arial", 35, "normal"))

        raf.penup()
        if e > 9:
            raf.goto(-110, -265)
        else:
            raf.goto(-100, -265)
        raf.write(e, font=("Arial", 35, "normal"))

        raf.penup()
        if f > 9:
            raf.goto(-260, -140)
        else:
            raf.goto(-250, -140)
        raf.write(f, font=("Arial", 35, "normal"))

        raf.penup()
        if g > 9:
            raf.goto(-275, 60)
        else:
            raf.goto(-265, 60)
        raf.write(g, font=("Arial", 35, "normal"))

        raf.penup()
        if h > 9:
            raf.goto(-145, 210)
        else:
            raf.goto(-135, 210)
        raf.write(h, font=("Arial", 35, "normal"))

    def print_9(self, a, b, c, d, e, f, g, h, i):

        raf = turtle.Turtle()
        raf.speed(self.speed)

        raf.penup()
        raf.goto(-80, 280)
        for i in range(9):
            raf.penup()
            raf.forward(140)
            raf.pendown()
            raf.pensize(3.5)
            raf.pencolor(self.c_color)
            raf.circle(40)
            raf.right(360 / 9)

        raf.penup()
        if a > 9:
            raf.goto(45, 305)
        else:
            raf.goto(50, 305)
        raf.write(a, font=("Arial", 25, "normal"))

        raf.penup()
        if b > 9:
            raf.goto(180, 205)
        else:
            raf.goto(185, 205)
        raf.write(b, font=("Arial", 25, "normal"))

        raf.penup()
        if c > 9:
            raf.goto(220, 45)
        else:
            raf.goto(225, 45)
        raf.write(c, font=("Arial", 25, "normal"))

        raf.penup()
        if d > 9:
            raf.goto(145, -100)
        else:
            raf.goto(150, -100)
        raf.write(d, font=("Arial", 25, "normal"))

        raf.penup()
        if e > 9:
            raf.goto(-10, -170)
        else:
            raf.goto(-5, -170)
        raf.write(e, font=("Arial", 25, "normal"))

        raf.penup()
        if f > 9:
            raf.goto(-170, -120)
        else:
            raf.goto(-165, -120)
        raf.write(f, font=("Arial", 25, "normal"))

        raf.penup()
        if g > 9:
            raf.goto(-260, 20)
        else:
            raf.goto(-255, 20)
        raf.write(h, font=("Arial", 25, "normal"))

        raf.penup()
        if h > 9:
            raf.goto(-240, 185)
        else:
            raf.goto(-235, 185)
        raf.write(h, font=("Arial", 25, "normal"))

        raf.penup()
        if i > 9:
            raf.goto(-115, 300)
        else:
            raf.goto(-110, 300)
        raf.write(i, font=("Arial", 25, "normal"))

    def print_10(self, a, b, c, d, e, f, g, h, i, j):

        raf = turtle.Turtle()
        raf.speed(self.speed)

        raf.penup()
        raf.goto(-80, 280)
        for i in range(10):
            raf.penup()
            raf.forward(140)
            raf.pendown()
            raf.pensize(3.5)
            raf.pencolor(self.c_color)
            raf.circle(40)
            raf.right(360 / 10)

        raf.penup()
        if a > 9:
            raf.goto(50, 305)
        else:
            raf.goto(55, 305)
        raf.write(a, font=("Arial", 25, "normal"))

        raf.penup()
        if b > 9:
            raf.goto(185, 215)
        else:
            raf.goto(190, 215)
        raf.write(b, font=("Arial", 25, "normal"))

        raf.penup()
        if c > 9:
            raf.goto(245, 60)
        else:
            raf.goto(250, 60)
        raf.write(c, font=("Arial", 25, "normal"))

        raf.penup()
        if d > 9:
            raf.goto(200, -95)
        else:
            raf.goto(205, -95)
        raf.write(d, font=("Arial", 25, "normal"))

        raf.penup()
        if e > 9:
            raf.goto(70, -200)
        else:
            raf.goto(75, -200)
        raf.write(e, font=("Arial", 25, "normal"))

        raf.penup()
        if f > 9:
            raf.goto(-90, -205)
        else:
            raf.goto(-85, -205)
        raf.write(f, font=("Arial", 25, "normal"))

        raf.penup()
        if g > 9:
            raf.goto(-230, -115)
        else:
            raf.goto(-225, -115)
        raf.write(g, font=("Arial", 25, "normal"))

        raf.penup()
        if h > 9:
            raf.goto(-285, 40)
        else:
            raf.goto(-280, 40)
        raf.write(h, font=("Arial", 25, "normal"))

        raf.penup()
        if i > 9:
            raf.goto(-245, 195)
        else:
            raf.goto(-240, 195)
        raf.write(i, font=("Arial", 25, "normal"))

        raf.penup()
        if j > 9:
            raf.goto(-115, 300)
        else:
            raf.goto(-110, 300)
        raf.write(j, font=("Arial", 25, "normal"))

    def print_11(self, a, b, c, d, e, f, g, h, i, j, k):

        raf = turtle.Turtle()
        raf.speed(self.speed)

        raf.penup()
        raf.goto(-80, 280)
        for i in range(11):
            raf.penup()
            raf.forward(140)
            raf.pendown()
            raf.pensize(3.5)
            raf.pencolor(self.c_color)
            raf.circle(40)
            raf.right(360 / 11)

        raf.penup()
        if a > 9:
            raf.goto(50, 305)
        else:
            raf.goto(55, 305)
        raf.write(a, font=("Arial", 25, "normal"))

        raf.penup()
        if b > 9:
            raf.goto(190, 225)
        else:
            raf.goto(195, 225)
        raf.write(b, font=("Arial", 25, "normal"))

        raf.penup()
        if c > 9:
            raf.goto(260, 80)
        else:
            raf.goto(265, 80)
        raf.write(c, font=("Arial", 25, "normal"))

        raf.penup()
        if d > 9:
            raf.goto(245, -80)
        else:
            raf.goto(250, -80)
        raf.write(d, font=("Arial", 25, "normal"))

        raf.penup()
        if e > 9:
            raf.goto(145, -210)
        else:
            raf.goto(150, -210)
        raf.write(e, font=("Arial", 25, "normal"))

        raf.penup()
        if f > 9:
            raf.goto(0, -260)
        else:
            raf.goto(-5, -260)
        raf.write(f, font=("Arial", 25, "normal"))

        raf.penup()
        if g > 9:
            raf.goto(-170, -220)
        else:
            raf.goto(-165, -220)
        raf.write(g, font=("Arial", 25, "normal"))

        raf.penup()
        if h > 9:
            raf.goto(-280, -100)
        else:
            raf.goto(-275, -100)
        raf.write(h, font=("Arial", 25, "normal"))

        raf.penup()
        if i > 9:
            raf.goto(-310, 60)
        else:
            raf.goto(-305, 60)
        raf.write(i, font=("Arial", 25, "normal"))

        raf.penup()
        if j > 9:
            raf.goto(-250, 210)
        else:
            raf.goto(-240, 210)
        raf.write(j, font=("Arial", 25, "normal"))

        raf.penup()
        if k > 9:
            raf.goto(-115, 300)
        else:
            raf.goto(-110, 300)
        raf.write(k, font=("Arial", 25, "normal"))
