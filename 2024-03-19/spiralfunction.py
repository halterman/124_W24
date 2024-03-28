""" Draws a spiral.  """


import turtle


def spiral(x: float, y: float, color: str) -> None:
    """ Draws with turtle t a spiral centered at (x, y)
        with the specified color """
    distance = 0.2
    angle = 40
    turtle.pencolor(color) # Set pen color
    turtle.penup() # Left pen to move it
    turtle.setposition(x, y) # Position the pen at coordinates (x, y)
    turtle.pendown() # Set pen down to begin drawing
    for i in range(100):
        turtle.forward(distance)
        turtle.left(angle)
        distance += 0.5


if __name__ == '__main__':
    spiral(0, 0, 'red')
    turtle.done()

