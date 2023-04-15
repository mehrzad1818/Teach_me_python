# This is the 19th day of 100 days of Python.


# This module uses event listener to trigger a funciton based on the given input (real-time input).

from turtle import Turtle, Screen
# import random

tim = Turtle()
screen = Screen()


def move_forward():
    """ Responsible for moving Tim on the screen. """
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()
