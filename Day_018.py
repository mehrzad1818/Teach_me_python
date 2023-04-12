# This is the beginning of the day 18 of 100 days of coding challenge. 



# This file contains a modular turtle that can rotate based on the given input.

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

forward_step = 2
degree = 1

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

while True:

    timmy_the_turtle.forward(forward_step)
    timmy_the_turtle.right(degree)
    timmy_the_turtle.forward(forward_step)
    degree -= 5
    forward_step += 1

screen = Screen()
screen.exitonclick()


# This code makes timmy create a simple square.

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

FORWARD_STEP = 100
STEP = 90

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for i in range(0, 4):

    timmy_the_turtle.forward(FORWARD_STEP)
    timmy_the_turtle.right(STEP)

screen = Screen()
screen.exitonclick()


# The most basic way of importing:

# import turtle
# tim = turtle.Turtle()


# A little bit more advanced:

# from turtle import Turtle
# tim = Turtle()


# The easiest way, but the most confusing one

# from turtle import *
# forward(100)


# You can draw a dashed line with the code below:

from turtle import Turtle, Screen

tim = Turtle()


for i in range(20):
    tim.down()
    tim.forward(10)
    tim.up()
    tim.forward(10)

screen = Screen()
screen.exitonclick()

# This code makes the turtle draw several shapes based on the number of given sides.

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("yellow")

FORWARD_STEP = 75


def shape(shape_side):
    """ Draws a shape. """

    shape_step = (360 / shape_side)

    for i in range(shape_side):

        tim.forward(FORWARD_STEP)
        tim.right(shape_step)


def change_color():
    """ Changes the color of the turtle. """

    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


for y in range(3, 8):
    shape(y)
    change_color()

screen = Screen()
screen.exitonclick()









