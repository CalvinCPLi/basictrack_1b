import turtle

pairs = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

pirate = turtle.Turtle()
screen = turtle.Screen()
pirate.speed("slow")

for angle, distance in pairs:
    pirate.left(angle)
    pirate.forward(distance)

screen.exitonclick()

