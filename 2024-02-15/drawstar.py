# Draw a stat using Turtle graphics
import turtle
import random

def draw_box():
    turtle.penup()
    turtle.setposition(50, -50)
    turtle.pendown()
    for i in range(4):
        turtle.left(90)
        turtle.forward(100)


def draw_star(size: float, x: float, y: float, color: str) -> None:
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color)
    turtle.left(108)
    for i in range(5):
        turtle.forward(size)
        turtle.left(144)

def draw_stars():
    for i in range(10):
        size = random.randrange(10, 101)
        x_pos = random.randrange(-200, 201)
        y_pos = random.randrange(-200, 201)
        draw_star(size, x_pos, y_pos, 'blue')


turtle.hideturtle()
draw_box()
draw_stars()
turtle.mainloop()