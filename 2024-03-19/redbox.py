from turtle import Turtle, mainloop

t = Turtle()      # Create a turtle object named t
t2 = Turtle()      # Create a turtle object named t2
t2.teleport(-250, 0)
t.pencolor('red') # t’s pen color is red
t2.pencolor('blue') # t’s pen color is red
t.forward(200)    # Move turtle t forward 200 units (bottom)
t2.forward(200)    # Move turtle t forward 200 units (bottom)
t.left(90)        # Turn turtle left by 90 degrees
t2.left(90)        # Turn turtle left by 90 degrees
t.forward(150)    # Move turtle t forward 150 units (right wall)
t2.forward(150)    # Move turtle t forward 150 units (right wall)
t.left(90)        # Turn turtle left by 90 degrees
t2.left(90)        # Turn turtle left by 90 degrees
t.forward(200)    # Move turtle t forward 200 units (top)
t2.forward(200)    # Move turtle t forward 200 units (top)
t.left(90)        # Turn turtle left by 90 degrees
t2.left(90)        # Turn turtle left by 90 degrees
t.forward(150)    # Move turtle t forward 150 units (left wall)
t2.forward(150)    # Move turtle t forward 150 units (left wall)
t.hideturtle()    # Make turtle t invisible
t2.hideturtle()    # Make turtle t invisible
mainloop()        # Await user input
