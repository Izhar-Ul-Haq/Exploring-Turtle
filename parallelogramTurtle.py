import turtle

# Initialize the turtle
t = turtle.Turtle()
t.fillcolor("yellow")
# Set the turtle's speed
t.speed(1)
t.begin_fill()
# Draw the parallelogram
for i in range(2):
	t.forward(100)
	t.left(60)
	t.forward(50)
	t.left(120)
t.end_fill()
turtle.down()
