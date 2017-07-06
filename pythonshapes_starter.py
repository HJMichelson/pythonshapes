from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(700,700)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
""" square only
x_pos = 100
t.setposition(x_pos, y_pos)
y_pos = 100
t.setposition(x_pos, y_pos)
x_pos = 0
t.setposition(x_pos, y_pos)
y_pos = 0
t.setposition(x_pos, y_pos)
"""

prompt = input('How many sides? ')
sides = int(prompt)     ##change promt into an integer
IntAngle = 180 - ((sides * 180) - 360)/sides ## calculate turning angle

for i in range(sides): ##how many times it will run is dictated by sides
    t.left(IntAngle)
    t.forward(50)


# Close window on click.
exitonclick()
