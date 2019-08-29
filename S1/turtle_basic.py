# -*- coding : utf-8 -*-

import turtle

def square(length):
    "have the turtle draw a square of side <length>"
    for side in range(4): 
        turtle.forward(length) 
        turtle.left(90)

turtle.reset()
square(200)
turtle.exitonclick()