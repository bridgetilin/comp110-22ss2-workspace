import turtle
from turtle import Turtle, colormode, done

unc: Turtle = Turtle()

colormode(255)  #RGB

turtle.Screen()
turtle.bgcolor(240, 235, 250)
unc.speed(0)

unc.color("gray")
unc.penup()
unc.goto(-10, 90)
unc.pendown()


unc.color("grey")

# dome
unc.begin_fill()
unc.fillcolor(191,230,255)
unc.forward(100)
unc.left(90)
unc.circle(90, 180)
unc.end_fill()

unc.right(270)
unc.forward(100)


# panel thing
unc.penup()
unc.goto(-90, 90)
unc.pendown()
unc.right(50)
unc.forward(17)
unc.left(50)
unc.forward(159)
unc.left(50)
unc.forward(17)

unc.penup()
unc.left(180)
unc.forward(10)
unc.right(50)
unc.pendown()

unc.forward(168)


#  rectangles!
def rectangle(side_1: int, side_2: int):
    unc.forward(side_1) # Forward unc by side_1 units
    unc.right(90)

    unc.forward(side_2)
    unc.right(90)

    unc.forward(side_1) 
    unc.right(90)

    unc.forward(side_2)
    unc.right(90)

def rectangle_2(side_1: int, side_2: int):
    unc.forward(side_1) # Forward unc by side_1 units
    unc.left(90)

    unc.forward(side_2)
    unc.left(90)

    unc.forward(side_1) 
    unc.left(90)

    unc.forward(side_2)
    unc.left(90)

unc.penup()
unc.goto(-67, 74)
unc.pendown()

rectangle(13, 2)
rectangle_2(13, 170)

unc.penup()
unc.goto(-40, 74)
unc.pendown()

rectangle(13, 2)
rectangle_2(13, 170)

unc.penup()
unc.goto(52, 74)
unc.pendown()

rectangle(13, 2)
rectangle_2(13, 170)

unc.penup()
unc.goto(80, 74)
unc.pendown()

rectangle(13, 2)
rectangle_2(13, 170)

def bottoms():
    unc.backward(1)
    rectangle(14, 2)
    unc.penup()
    unc.backward(4)
    unc.pendown()
    rectangle_2(22, 4)

    
unc.penup()
unc.goto(-67, -98)
unc.pendown()
bottoms()


unc.penup()
unc.goto(-40, -98)
unc.pendown()
bottoms()


unc.penup()
unc.goto(52, -98)
unc.pendown()
bottoms()

unc.penup()
unc.goto(79, -98)
unc.pendown()
bottoms()

unc.penup()
unc.goto(99, -112)
unc.pendown()

rectangle(100, 9)

def go_to(x: int, y: int):
    unc.penup()
    unc.goto(x, y)
    unc.pendown()

rectangle(150, 9)
rectangle(200, 9)

go_to(114, -120)
rectangle(90, 9)
rectangle(180, 9)
rectangle(235, 9)


# unc.left(90)
# unc.circle(90, 180)


# def dome(rad):
     
#   # rad --> radius of arc
#   for i in range(2):
     
#     # two arcs
#     unc.circle(rad,90)
#     unc.circle(rad//2,90)
 
# Main section
# tilt the shape to negative 45

# unc.circle(100 ,90)
# unc.circle(100//2,90)
 
# # calling draw method
# # dome(100)


turtle.done()
