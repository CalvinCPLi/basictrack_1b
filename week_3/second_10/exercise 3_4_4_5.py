import turtle
michael = turtle.Turtle()
screen = turtle.Screen()

for i in range(3):
    michael.forward(60)
    michael.left(120)

for i in range(4):
    michael.forward(60)
    michael.left(90)

for i in range(6):
    michael.forward(60)
    michael.left(60)

for i in range(8):
    michael.forward(60)
    michael.left(360/8)

screen.exitonclick()