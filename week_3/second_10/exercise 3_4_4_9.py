import turtle
tess = turtle.Turtle()
screen = turtle.Screen()
tess.shape("turtle")
tess.color("blue")
screen.bgcolor("black")
tess.penup()

for i in range(12):
    tess.forward(100)
    tess.pendown()
    tess.forward(20)
    tess.penup()
    tess.forward(20)
    tess.stamp()
    tess.goto(0,0)
    tess.right(360/12)

screen.exitonclick()

