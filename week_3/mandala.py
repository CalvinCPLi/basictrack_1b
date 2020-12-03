import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()
lucifer = turtle.Turtle()
maze = turtle.Turtle()


leonardo.shape("turtle")
leonardo.pensize(5)
leonardo.speed("fast")

lucifer.shape("turtle")
lucifer.pensize(2)


lucifer.speed("fast")
maze.setposition(0,190.2)
maze.shape("turtle")
maze.pensize(2)
maze.speed("fast")





colors = ["red", "orange", "green", "blue", "purple"]

colors[1]

for index in range(60):
    leonardo.color(colors[index % len(colors)])
    if index % 2 == 0:
        leonardo.forward(20)
    else:
        leonardo.forward(20)
    leonardo.left(6)

for index in range(60):
    lucifer.color(colors[index % len(colors)])
    if index % 2 == 0:
        lucifer.forward(20)
    else:
        lucifer.forward(10)
    lucifer.left(9)
print(lucifer.position())

for index in range(20):
    lucifer.color(colors[index % len(colors)])
    lucifer.left(189)
    lucifer.forward(30)


paper.exitonclick()
