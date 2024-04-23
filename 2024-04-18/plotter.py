import tkinter as tk


class PlotWindow(tk.Toplevel):
    """ Provides a window in which to render a data plot. """

    def __init__(self, title: str, data: list[float],  
                 left: int, top: int, width: int, height: int) -> None:
        """ Initializes a plotting window.
            data: a list of floating-point values to plot.
            title: a string title for the plot.
            left: the x position of the left edge of the window. 
            top: the y position of the top edge of the window.
            width: the width of the window.
            height: the height of the window. """
        # Initialize the Tkinter window
        super().__init__()
        self.title(title)
        self.geometry(f'{width + 10}x{height + 10}+{left - 5}+{top - 5}')
        print(f'width = {width}, height = {height}')
        canvas = tk.Canvas(self, width=width, height=height)
        canvas.pack()
       
        # Plot the data
        print(f'width = {width}, height = {height}')
        # Compute the vertical size of the data
        min_val = min(data) - 5
        max_val = max(data) + 5
        width_scale = width/(len(data) - 1)
        height_scale = height/(max_val - min_val)

        # Draw baseline at y = 0
        y_zero = height + min_val*height_scale
        canvas.create_line(0, y_zero, width, y_zero, fill='cyan')
    
        # Plot data
        for i in range(1, len(data)):
            x0 = (i - 1) * width_scale
            y0 = height - (data[i - 1] - min_val)*height_scale
            x1 = i * width_scale
            y1 = height - (data[i] - min_val)*height_scale
            canvas.create_line(x0, y0, x1, y1, fill='red')

        self.overrideredirect(True)  # Remove window frame and title bar



class Plotter:
    """ Manages multiple plotting windows. """

    def __init__(self) -> None:
        """ Initializes the root Tkinter window and 
            creates a list in which to add future plotting windows. """
        # Main element that oversees all the windows
        self.root = tk.Tk()
        self.root.geometry('200x1+1+1')
        self.plots = []

    def plot(self) -> None:
        """ Initiates the plots in all windows. 
            Call this one only time after adding all the plotting
            windows. """
        self.root.focus_set()
        self.root.mainloop()
    
    def new(self, name: str, data: list[float], 
            left: int, top: int, width: int, height: int) -> None:
        """ Creates and adds a new plotting window. 
            name: the title for the plotting window.
            data: the list of floating-point values to plot.
            left: the x position of the left edge of the new window. 
            top: the y position of the top edge of the new window.
            width: the width of the new window.
            height: the height of the new window. """
        self.plots.append(PlotWindow(name, data, left, top, width, height))



if __name__ == '__main__':
    import math
    plotter = Plotter()
    plotter.new('Sample plot', [10.0, -10.0, 5.0, -5.0], 100, 100, 300, 150)
    parabola = [x**2.0 for x in range(-800, 800)]
    plotter.new('Parabola', parabola, 100, 300, 600, 500)
    plotter.new('sin x', [20*math.sin(0.5*x) for x in range(-100, 100)], 700, 300, 600, 100)
    plotter.plot()
