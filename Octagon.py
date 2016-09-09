# Assignment One_Octagon
# Ryan Ge
# Sep 6, 2016

import turtle
def drawoctagon():
    for x in range(8):
        turtle.forward(100)
        turtle.left(45)
# draw faster
turtle.speed(500)
def goto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.color('blue')
turtle.begin_fill()

turtle.end_fill()
# moves turtle to a new location
turtle.penup()
turtle.left(180)
turtle.forward(180)
turtle.pendown()

turtle.color('Gold')
turtle.begin_fill()
goto(100,-50)
drawoctagon()
turtle.end_fill()

turtle.penup()
turtle.forward(180)
turtle.right(180)
turtle.pendown()

turtle.color('Brown')
turtle.begin_fill()
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
drawoctagon()
turtle.end_fill()

turtle.penup()
turtle.goto(-300,-290)
turtle.pendown()
turtle.color('Grey')
turtle.begin_fill()
drawoctagon()
turtle.end_fill()

turtle.exitonclick()
