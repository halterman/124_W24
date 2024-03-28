from tkinter import Tk, Canvas


root = Tk() # Create the main window
root.title("Traffic Light")
# Create a drawing surface within the root window
canvas = Canvas(root, width=400, height=300)
# Make the window size conform to this canvas object
canvas.pack()

# Set up the visual aspects of the traffic light

# Traffic light frame
canvas.create_rectangle(150, 20, 250, 280, fill='gray')

# Red lamp
red_lamp = canvas.create_oval(170, 40, 230, 100, fill='red')

# Yellow lamp
yellow_lamp = canvas.create_oval(170, 120, 230, 180, fill='yellow')

# Green lamp
green_lamp = canvas.create_oval(170, 200, 230, 260, fill='green2')

# Start the GUI event loop
root.mainloop()