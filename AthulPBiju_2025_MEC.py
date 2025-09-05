import turtle
screen = turtle.Screen()
screen.title('Pookalam 2025')
screen.colormode(255)
t = turtle.Turtle()
t.width(3)
t.speed(0)

def shape(radius, degree=None, steps=None, color=None):
    t.color(color)
    t.penup()
    t.lt(180)
    t.fd(radius)
    t.lt(90)
    t.pendown()
    t.begin_fill()
    t.circle(radius, degree, steps)
    t.end_fill()
    t.penup()
    t.lt(90)
    t.fd(radius)
    t.pendown()

def petal(length, color):
    t.color(color)
    t.begin_fill()
    for i in range(8):
        t.forward(length)
        t.circle(length/8, 208)
        t.forward(length)
        t.right(163)
    t.end_fill()

shape(355, color=(110, 0, 0))
shape(350, color=(220, 80, 20))

for _ in range(16):
    shape(radius=350, steps=4, color=(255, 200, 50))
    t.rt(5.625)
t.rt(2.8125)
for _ in range(16):
    shape(radius=333, steps=4, color=(180, 30, 30))
    t.rt(5.625)
t.rt(2.8125)
for _ in range(16):
    shape(radius=320, steps=4, color=(255, 220, 60))
    t.rt(5.625)
t.rt(2.8125)
for _ in range(16):
    shape(radius=306, steps=4, color=(245, 240, 220))
    t.rt(5.625)
t.rt(2.8125)
for _ in range(16):
    shape(radius=293, steps=4, color=(255, 215, 0))
    t.rt(5.625)

shape(270, color=(230, 70, 40))
shape(260, color=(255, 255, 0))

for _ in range(2):
    shape(radius=270, steps=4, color=(0, 150, 50))
    t.rt(45)

shape(205, color=(255, 165, 0))

t.penup()
t.rt(67.5)
t.bk(240)
t.lt(22.5)
t.pendown()
t.color((148, 0, 211))
t.begin_fill()
for _ in range(8):
    t.forward(440)
    t.right(135)
t.end_fill()
t.penup()
t.rt(22.5)
t.fd(240)
t.pendown()

shape(98, color=(255, 220, 50))

t.penup()
t.rt(180)
t.bk(30)
t.lt(90)
t.fd(5)
t.rt(90)
t.pendown()
petal(100, (255, 0, 0))

t.home()
shape(15, color=(255, 255, 255))

t.hideturtle()
turtle.done()
