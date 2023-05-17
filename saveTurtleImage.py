import turtle
import tkinter as tk
from PIL import ImageGrab

# Create a Turtle screen and turtle object
screen = turtle.Screen()
turtle = turtle.Turtle()

# Your turtle graphics code goes here
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
# ...

# Hide the turtle and update the screen
turtle.hideturtle()
screen.update()

# Get the screen dimensions
screen_width = screen.window_width()
screen_height = screen.window_height()

# Get the coordinates of the turtle graphics on the screen
x, y = turtle.position()

# Create a blank image using PIL
image = ImageGrab.grab((x, -y, x + screen_width, -y + screen_height))

# Save the image as a PNG file
image.save("turtle_graphics.png", "PNG")

# Alternatively, save the image as a JPG file
image.save("turtle_graphics.jpg", "JPEG")

# Exit the Turtle program
turtle.done()
