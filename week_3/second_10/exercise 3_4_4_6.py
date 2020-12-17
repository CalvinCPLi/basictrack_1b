import turtle

pirate = turtle.Turtle()
screen = turtle.Screen()

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for angle in angles:
    pirate.forward(100)
    pirate.left(angle)

screen.exitonclick()