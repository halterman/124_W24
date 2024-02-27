from __future__ import annotations
import tkinter as tk
import math
import geometry

class GraphicalPoint:
    """ A geometric point consisting of an (x,y) coordinate pair. """
    def __init__(self, x: float, y: float) -> None:
        """ Constructor initializes the (x,y) coordinates of a point. """
        self.x, self.y = x, y

    def __equals__(self, other: GraphicalPoint) -> bool:
        """ Returns True if the (x,y) coordinates of 'other' equal to the
            (x,y) coordinates of this point object. """
        return (self.x == other.x and self.y == other.y) \
                or (math.isclose(self.x, other.x) and math.isclose(self.y, other.y))

    @classmethod
    def from_point(cls, pt: geometry.Point) -> GraphicalPoint:
        return cls(pt[0], pt[1])  




NO_POINT = GraphicalPoint(-10_000, -10_000)

def diff(a: float, b: float) -> float:
    """ Compute the absolute value of the difference of a and b """
    return a - b if a > b else b - a


def draw_point(canvas: tk.Canvas, pt: GraphicalPoint, color: str) -> None:
    """ Draw a point with a given color """
    canvas.create_oval((pt.x - 2, pt.y - 2, pt.x + 2, pt.y + 2), fill=color)


class VisualGeometry:
    #  Class variable
    #NO_POINT = Point(-1, -1)

    def __init__(self) -> None:
        """ Initializes the visual geometry window and points. """
        self.vertex1 = NO_POINT
        self.vertex2 = NO_POINT
        self.vertex3 = NO_POINT
        self.vertex4 = NO_POINT
        self.intersection = NO_POINT
        self.active_point = NO_POINT

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=600,
                             bg='white', cursor='arrow')

        #  The points managed by the program
        self.clear_points()
        
        #  Is the user currently dragging a point?
        self.dragging = False

        self.root.resizable(False, False)
        # self.root.wm_title('Visual Geometry: ' + str(self.points))
        self.root.wm_title('Visual Geometry')
        # root.protocol("WM_DELETE_WINDOW", None)

        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
        self.canvas.bind('<ButtonPress-1>', self.mouse_pressed)
        self.canvas.bind('<ButtonRelease-1>', self.mouse_released)
        self.canvas.bind('<Motion>', self.mouse_moved)
        self.canvas.bind('<B1-Motion>', self.mouse_moved)
        self.canvas.bind_all('<Key>', self.key_pressed)
        self.repaint()
        self.root.mainloop()

    def match_point(self, x: float, y: float) -> GraphicalPoint:
        """ Returns the point located within four pixels of the point
            (x,y).  If no point is within that distance to (x,y), the
            method return NO_POINT. """
        if diff(x, self.vertex1.x) < 4 and diff(y, self.vertex1.y) < 4:
            return self.vertex1
        elif diff(x, self.vertex2.x) < 4 and diff(y, self.vertex2.y) < 4:
            return self.vertex2
        elif diff(x, self.vertex3.x) < 4 and diff(y, self.vertex3.y) < 4:
            return self.vertex3
        elif diff(x, self.vertex4.x) < 4 and diff(y, self.vertex4.y) < 4:
            return self.vertex4
        else:
            return NO_POINT

    def draw_control_point(self, canvas: tk.Canvas, pt: GraphicalPoint, color: str) -> None:
        """ Draws one of the movable control points.  If the point is
            active (the cursor is over the point), the point is drawn
            larger than normal to provide visual feedback to the user
            that the point is active. """
        #  Draw a big box when mouse cursor is over the point
        if pt == self.active_point:
            canvas.create_oval((pt.x - 10, pt.y - 10,
                                pt.x + 10, pt.y + 10), outline=color)
            self.point_text(pt, color)
            # canvas.create_text(pt.x, pt.y + 20,
            #                   text=('(%2.2f,%2.2f)' % (pt.x, pt.y)))
        else:    # Draw little box when mouse cursor not over the point
            canvas.create_oval((pt.x - 4, pt.y - 4,
                                pt.x + 4, pt.y + 4), fill=color)

    @staticmethod
    def draw_line(canvas: tk.Canvas, p1: GraphicalPoint, p2: GraphicalPoint, color: str) -> None:
        """ Draw the line segment between the points p1 and p2 with 
            the color color.  """
        canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill=color)

    def draw_extended_line(self, canvas: tk.Canvas, p1: GraphicalPoint, p2: GraphicalPoint, color: str) -> None:
        """ Draw the line that passes through the points p1 and p2.
            The line extends to the border of the window. The line's
            color is color. """
        m = geometry.slope(p1.x, p1.y, p2.x, p2.y)
        b = geometry.intercept(p1.x, p1.y, p2.x, p2.y)
        if math.isinf(m):
            new_x1 = new_x2 = p1.x
            new_y1 = 0
            new_y2 = 600
        elif -1.0 <= m <= 1.0:
            pi1 = geometry.intersection(m, b, math.inf, 0)
            pi2 = geometry.intersection(m, b, math.inf, 600)
            (x1, y1) = pi1
            (x2, y2) = pi2
            new_x1 = x1
            new_y1 = y1
            new_x2 = x2
            new_y2 = y2
        else:
            pi1 = geometry.intersection(m, b, 0, 0)
            pi2 = geometry.intersection(m, b, 0, 600)
            (x1, y1) = pi1
            (x2, y2) = pi2
            new_x1 = x1
            new_y1 = y1
            new_x2 = x2
            new_y2 = y2
        canvas.create_line(new_x1, new_y1, new_x2, new_y2,
                           fill=color, width=2)

        # Line segment, for debugging
        # canvas.create_line(p1.x, p1.y, p2.x, p2.y,
        #
        #                    fill=color, width=2)


        self.draw_control_point(canvas, p1, color) 
        self.draw_control_point(canvas, p2, color) 

    def point_text(self, pt: GraphicalPoint, color: str) -> None:
        """ Draws the string containing the coordinates for point pt 
            in color color. """
        self.canvas.create_text(pt.x, pt.y + 20,
                                text=('(%2.1f,%2.1f)' %
                                      (pt.x - 300, 300 - pt.y)), fill=color)

    def line_text(self, x: float, y: float, p1: GraphicalPoint, p2: GraphicalPoint, 
                  color: str) -> None:
        """ Draws the string representing the equation of the line
            passing through points p1 and p2 in y = mx + b form.
            The color is color, and the string is displayed at (x,y). """
        eqn = geometry.line_equation(p1.x - 300, 300 - p1.y,
                                     p2.x - 300, 300 - p2.y)
        self.canvas.create_text(x, y, text=eqn, fill=color)

    @staticmethod
    def draw_axes(canvas: tk.Canvas) -> None:
        """ Draws the x- and y-axes and accessory grid lines at 20 
            unit intervals. """
        for x in range(0, 600, 50):
            canvas.create_line((x, 0, x, 600), fill='lightblue')
        for y in range(0, 600, 50):
            canvas.create_line((0, y, 600, y), fill='lightblue')
        canvas.create_line((0, 300, 600, 300), fill='black')
        canvas.create_line((300, 0, 300, 600), fill='black')

    def draw(self, canvas: tk.Canvas) -> None:
        """ Draws the contents of the window.  """
        #  Draw the axes
        self.draw_axes(canvas)
        #  Draw the control points
        if self.vertex1 != NO_POINT:
            self.draw_control_point(canvas, self.vertex1, 'blue')
            if self.vertex2 != NO_POINT:
                self.draw_control_point(canvas, self.vertex2, 'blue')
                self.draw_extended_line(canvas, self.vertex1, self.vertex2, 'blue')
                self.line_text(50, 500, self.vertex1, self.vertex2, 'blue')
                if self.vertex3 != NO_POINT:
                    self.draw_control_point(canvas, self.vertex3, 'green')
                    if self.vertex4 != NO_POINT:
                        self.draw_control_point(canvas, self.vertex4, 'green')
                        self.draw_extended_line(canvas, self.vertex3,
                                                self.vertex4, 'green')
                        self.line_text(50, 530, self.vertex3, self.vertex4, 'green')
                        v1 = (self.vertex1.x, self.vertex1.y)
                        v2 = (self.vertex2.x, self.vertex2.y)
                        v3 = (self.vertex3.x, self.vertex3.y)
                        v4 = (self.vertex4.x, self.vertex4.y)
                        inter = geometry.point_intersection(v1, v2, v3, v4)
                        if inter is not geometry.NO_POINT:    #None:
                            self.intersection = GraphicalPoint.from_point(inter)
                            self.draw_control_point(canvas, self.intersection, 
                                                    'red')
                            self.point_text(self.intersection, 'red')
                        else:
                            self.intersection = NO_POINT

    @staticmethod
    def do_quit() -> None:
        """ Quit the application """
        exit()  # Quit the application

    def mouse_released(self, event: tk.Event) -> None:
        if not self.dragging and self.vertex4 == NO_POINT \
                and self.active_point == NO_POINT:
            pt = GraphicalPoint(event.x, event.y)
            if self.vertex1 == NO_POINT:
                self.vertex1 = pt
            elif self.vertex2 == NO_POINT:
                self.vertex2 = pt
            elif self.vertex3 == NO_POINT:
                self.vertex3 = pt
            else:
                self.vertex4 = pt
            self.repaint()
        self.dragging = False
        # self.active_point = VisualGeometry.NO_POINT

    def mouse_moved(self, event: tk.Event) -> None:
        x = event.x
        y = event.y
        if self.dragging:
            self.active_point.x = x
            self.active_point.y = y
            self.repaint()
        else:
            # self.active_point = self.match_point(event.x, event.y)
            # if self.active_point != VisualGeometry.NO_POINT:
            #        self.repaint()
            prev = self.active_point
            self.active_point = self.match_point(x, y)
            if self.active_point != NO_POINT:
                self.canvas.config(cursor='fleur')
            else:
                self.canvas.config(cursor='arrow')
            if self.active_point == NO_POINT \
                    and prev != NO_POINT:
                self.repaint()
            elif self.active_point != NO_POINT:
                self.repaint()

    def mouse_pressed(self, event: tk.Event) -> None:
        x = event.x
        y = event.y
        self.active_point = self.match_point(x, y)
        if self.active_point != NO_POINT:
            self.active_point.x = x
            self.active_point.y = y
            self.dragging = True
        self.repaint()

    def clear_points(self) -> None:
        """ Removes all the points from the viewport to (re)start 
            the session. """
        self.vertex1 = NO_POINT
        self.vertex2 = NO_POINT
        self.vertex3 = NO_POINT
        self.vertex4 = NO_POINT
        self.intersection = NO_POINT
        self.active_point = NO_POINT

    # ---------------------------------------------------------------
    def repaint(self) -> None:
        """ Force the window to redraw itself.  Remove the current 
            graphical objects. """
        #  Remove current graphical objects
        self.canvas.delete(tk.ALL)
        self.draw(canvas=self.canvas)
        
    # -------------------------------------------------------------
    def key_pressed(self, event: tk.Event) -> None:
        """
        Respond to user key strokes.  The 'Z' key clears the
        points from the viewport.
        """
        x, y = event.x, event.y
        match event.keysym:
            case 'H' | 'h':
                # Make horizontal line
                if self.vertex1 == NO_POINT:
                    self.vertex1 = GraphicalPoint(x, y)
                    self.vertex2 = GraphicalPoint(0, y)
                elif self.vertex2 != NO_POINT and self.vertex3 == NO_POINT:
                    self.vertex3 = GraphicalPoint(x, y)
                    self.vertex4 = GraphicalPoint(0, y)
            case 'V' | 'v':
                # Make vertical line
                if self.vertex1 == NO_POINT:
                    self.vertex1 = GraphicalPoint(x, y)
                    self.vertex2 = GraphicalPoint(x, 0)
                elif self.vertex2 != NO_POINT and self.vertex3 == NO_POINT:
                    self.vertex3 = GraphicalPoint(x, y)
                    self.vertex4 = GraphicalPoint(x, 0)
            case 'Escape':
                self.clear_points()
            case _:
                print("Unrecognized key pressed")


        self.repaint()


def main() -> None:
    VisualGeometry()


if __name__ == '__main__':
    main()