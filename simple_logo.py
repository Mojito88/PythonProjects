import turtle



t = turtle.Turtle()
t.speed(12)
turtle.Screen().bgcolor(0,0,0)
t.penup()

t.goto(-100, 200)
t.pendown()




#t.speed(1)
#t.circle(150)


def n_start():
    t.fillcolor("#FF0000")
    t.begin_fill()
    t.right(-180)
    t.forward(100)
    t.right(-90)
    t.forward(400)
    t.right(-90)

    t.forward(100)

    





    t.right(-90)
    t.forward(240)
    t.right(-90)
    t.end_fill()


n_start()

t.penup()
t.goto(-200, 200)
t.pendown()

def ret():
    t.speed(15)
    t.fillcolor("#FF0000")
    t.begin_fill()
    t.right(-120)
    t.forward(462)
    t.right(120)
    t.right(-180)
    t.forward(100)

    t.right(-90)
    t.right(-30)
    t.forward(462)
    t.right(-60)
    t.forward(100)
    t.end_fill()

ret()







def n_floor():
    t.speed(12)
    t.fillcolor("#FF0000")
    t.begin_fill()
    t.right(180)
    t.forward(100)
    t.right(-90)
    t.forward(400)
    t.right(-90)
    t.forward(100)
    t.right(-90)
    t.forward(228)
    t.penup()
    t.end_fill()
    t.pendown()
    t.right(-90)
    t.speed(18)
    t.right(120 - 90 + 30)
    t.forward(200)
    t.penup()
    t.forward(100)


t.goto(31, -200)


n_floor()
t.fillcolor("#000000")
t.end_fill()

ext = input()