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


 # This challenge requires the turtle to do random walks in specified spaces and change color at the same time.
    
    
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(5)
tim.speed(0)


DIRECTION = [0, 90, 180, 270]
FORWARD_STEP = 35


def shape():
    """ Draws a shape. """

    tim.setheading(random.choice(DIRECTION))
    tim.forward(FORWARD_STEP)


def change_color():
    """ Changes the color of the turtle. """

    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


for y in range(50):
    shape()
    change_color()

screen = Screen()
screen.exitonclick()



# In this challenge, the turtle creates spirograph, rotating around its axis to make circles.


from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.pensize(1)
tim.speed(0)


FORWARD_STEP = 100
STEP = 44


def shape():
    """ Draws a shape. """

    tim.left(STEP)
    tim.circle(FORWARD_STEP)


def change_color():
    """ Changes the color of the turtle. """

    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)


for y in range(int(360 / STEP)):
    shape()
    change_color()

screen = Screen()
screen.exitonclick()


# In this final challenge, we're going to extract colors and make a pointed art with it.


# This part gives you the most frequent colors in a picture.

import colorgram

COLOR_NUMBER = 12
colors = colorgram.extract('image.jpg', COLOR_NUMBER)


rgb_list = []

for numer in range(0, COLOR_NUMBER):

    red = colors[numer].rgb.r
    green = colors[numer].rgb.g
    blue = colors[numer].rgb.b

    color_code = (red, green, blue)

    rgb_list.append(color_code)


print(rgb_list)


color_list = [(25, 108, 164),
              (194, 38, 81),
              (238, 161, 49),
              (234, 215, 85),
              (226, 237, 228),
              (223, 137, 176),
              (144, 108, 56),
              (102, 197, 219),
              (206, 166, 29)]


# This part creates the dotted painting:

from turtle import Turtle, Screen
import random


color_list = [
    (25, 108, 164),
    (194, 38, 81),
    (238, 161, 49),
    (234, 215, 85),
    (226, 237, 228),
    (223, 137, 176),
    (144, 108, 56),
    (102, 197, 219),
    (206, 166, 29)
]

tim = Turtle()
tim.shape("turtle")
tim.pensize(3)
tim.speed(0)

X_DISPLACEMENT = 50
Y_DISPLACEMENT = 50

X_ALIGN = -300
Y_ALIGN = -300


def shape():
    """ Draws a shape. """

    tim.dot(20, random.choice(color_list))


def position():
    """ Changes the position of the turtle. """
    tim.setposition(X_ALIGN, Y_ALIGN)


def change_color():
    """ Changes the color of the turtle. """

    R = color_list[0]
    B = color_list[1]
    G = color_list[2]
    tim.color(R, G, B)


for y in range(10):
    shape()

screen = Screen()
screen.exitonclick()

