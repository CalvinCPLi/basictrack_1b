import turtle, math, random


def draw_polygon(drawing_turtle: turtle.Turtle, sides, radius, center_x = 0, center_y = 0):
    for side in range(sides):
        drawing_turtle.forward(size)
        drawing_turtle.left(360 / sides)


nick = turtle.Turtle()
maze = turtle.Turtle()
calvin = turtle.Turtle()
kids = turtle.Turtle()
screen = turtle.Screen()


screen.exitonclick()
