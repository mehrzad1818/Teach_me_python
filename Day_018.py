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

forward_step = 100
degree = 90

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for i in range(0, 4):

    timmy_the_turtle.forward(forward_step)
    timmy_the_turtle.right(degree)

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

