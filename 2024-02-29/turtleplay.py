import turtle
import random

circle_color = 'red'

def initialize() -> None:
    turtle.tracer(False)
    turtle.title('Turtle Play')
    turtle.onscreenclick(mouse_click)
    turtle.onkeyrelease(change_color, 'C')
    turtle.onkeyrelease(change_color, 'c')
    turtle.hideturtle()
    turtle.listen()


def mouse_click(x: float, y: float) -> None:
    print(f'x = {x}, y = {y}')
    draw_line(0, 0, x, y)
    turtle.teleport(x, y - 20)
    turtle.color(circle_color)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.update()

def change_color() -> None:
    global circle_color
    if circle_color == 'red':
        circle_color = 'yellow'
    else:
        circle_color = 'red'

def draw_line(x1: float, y1: float, 
          x2: float, y2: float) -> None:
    turtle.teleport(x1, y1)
    turtle.pensize(3)
    turtle.color('black')
    turtle.setpos(x2, y2)
    turtle.update()


initialize()
for i in range(20):
    x = random.randrange(-300, 300)
    y = random.randrange(-300, 300)
    mouse_click(x, y)
turtle.mainloop()