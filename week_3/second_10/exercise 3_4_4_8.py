import turtle
tess = turtle.Turtle()
screen = turtle.Screen()

for i in range(5):
    tess.forward(100)
    tess.right((360 * 2) / 5) # two full rotations

screen.exitonclick()