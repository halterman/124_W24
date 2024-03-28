""" Draws in the window two spirals.  """

from typing import Generator, Any

import turtle


def spiral(t: turtle.Turtle, x: float, y: float, color: str)  \
        -> Generator[Any, Any, Any]:
    """ Draws with turtle t a spiral centered at (x, y)
        with the specified color """
    distance = 0.2
    angle = 40
    t.pencolor(color) # Set pen color
    t.penup() # Left pen to move it
    t.setposition(x, y) # Position the pen at coordinates (x, y)
    t.pendown() # Set pen down to begin drawing
    #for i in range(100):
    while True:
        t.forward(distance)
        t.left(angle)
        distance += 0.5
        yield

if __name__ == '__main__':
    t1 = turtle.Turtle() # Create a turtle object named t1
    t2 = turtle.Turtle() # Create a turtle object named t2
    g1 = spiral(t1, -100, 0, 'red')
    g2 = spiral(t2, 100, 0, 'blue')
    for i in range(80):
        next(g1)
        next(g2)
    #t1.hideturtle() # Make turtle t1 invisible
    #t2.hideturtle() # Make turtle t2 invisible
    turtle.done()

