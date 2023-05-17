import turtle

polygon = turtle.Turtle()
polygon.color('red', 'black')
numOfSides = 6

angle = 360/numOfSides
polygon.begin_fill()
for i in range(numOfSides):
    polygon.forward(100)
    polygon.right(angle)
polygon.end_fill()
turtle.done()
