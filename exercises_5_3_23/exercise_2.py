import turtle


screen = turtle.Screen()

tess = turtle.Turtle()      # creates a new Turtle object sets tess to refer to that object
alex = tess                 # copies the reference to tess

alex.color("hotpink")       # the turtle, referred to by both tess and alex becomes pink
tess.speed(1)

tess.forward(100)           # the turtle, referred to by both tess and alex moves forward
alex.backward(100)

screen.exitonclick()
