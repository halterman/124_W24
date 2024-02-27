""" geometry.py
    Contains analytical geometry functions to compute line slope,
    distance between points, line intercepts, and line intersections. """

import math

# A convenient type alias
Point = tuple[float, float]

# A global value for a "non" point object
NO_POINT = (math.inf, math.inf)


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """ Computes the distance between the points (x1,y1) and (x2,y2),
        where x1, y1, x2, and y2 are numbers. """
    return 0.0    # Replace with your code


def slope(x1: float, y1: float, x2: float, y2: float) -> float:
    """ Computes the slope of the line that passes between the points
        (x1,y1) and (x2,y2).  The function returns infinity if the two
        points are identical.  x1, y1, x2, and y2 are numbers. """
    return 0.0    # Replace with your code


def intercept(x1: float, y1: float, x2: float, y2: float) -> float:
    """ Computes the y-intercept of the non-vertical line that
        passes through the points (x1,y1) and (x2,y2).  The
        function returns the x-intercept if the line is vertical.
        Two identical points are interpreted to be on a
        vertical line. """
    return 0.0    # Replace with your code

def line_equation_mb(m: float, b: float) -> str:
    """ Returns a string representation of a line with slope m and
        intercept b.  The result is in the form y = mx + b for
        non-vertical lines and x = b for vertical lines.  The representation
        is as simple as possible; e.g.,
         y = 3x - 2      not y = 3x + -2
         y = x + 3       not y = 1x + 3
         y = 5           not y = 0x + 5
         x = 4           a vertical line """
    return 'Line equation'    # Replace with your code

def line_equation(x1: float, y1: float, x2: float, y2: float) -> str:
    """ Returns a string representation of a line passing through the points
        (x1,y1) and (x2,y2).  The result is in the form y = mx + b for
        non-vertical lines and x = b for vertical lines.  The representation
        is as simple as possible; e.g.,
             y = 3x - 2      not y = 3x + -2
             y = x + 3       not y = 1x + 3
             y = 5           not y = 0x + 5
             x = 4           a vertical line """
    return line_equation_mb(slope(x1, y1, x2, y2), intercept(x1, y1, x2, y2))


def intersection(m1: float, b1: float, m2: float, b2: float) -> Point:
    """ Computes the (i_x,i_x) intersection point of the lines
        y = m1x + b1 and y = m2x + b1.  Returns None if the lines
        do not intersect in a single point. """
    return -1000.0, -1000.0   # Replace with your code
    # i_x = i_y = inf



def point_intersection(p1: Point, p2: Point, p3: Point, p4: Point) -> Point:
    """ Returns the point of intersection of the line p1-p2 and line
        p3-p4.  Returns None if the lines do not intersect in a single point. """
    (x1, y1) = p1
    (x2, y2) = p2
    (x3, y3) = p3
    (x4, y4) = p4
    return intersection(slope(x1, y1, x2, y2),
                        intercept(x1, y1, x2, y2),
                        slope(x3, y3, x4, y4),
                        intercept(x3, y3, x4, y4))


if __name__ == '__main__':
    pass
