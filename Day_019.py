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

# This part is like some sort of combining different functions together.
# We pass in the outcome of one function into income of the other function.


# def function_a(something):

#     # Do this with something
#     # Then do this
#     # Finally do this


# def function_b(function_a):
#     # Do this



from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    """ Tim goes forwaaarrrddd. """
    tim.forward(10)


def move_backward():
    """ Tim goes backwaaarrrddd. """
    tim.backward(10)


def yaw_clockwise():
    """ Tim goes weeeeeee. """
    tim.right(5)


def yaw_c_clockwise():
    """ Tim goes wooooooo. """
    tim.left(5)


def reset():
    """ Tim goes baaaaaaaaack. """
    tim.reset()


screen.listen()
screen.exitonclick


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=yaw_clockwise)
screen.onkey(key="a", fun=yaw_c_clockwise)
screen.onkey(key="c", fun=reset)

