"""Deals with handling the car for the turtle crossing game."""

import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """Manages the movement of the car and their creation."""

    def __init__(self):
        super().__init__()
        self.car_number = []
        self.turtle_generate()
        self.turtle_placement()

    def turtle_generate(self):
        """Generates a car shaped turtle."""

        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=1, stretch_wid=2)
        self.penup()
        self.car_number()

    def turtle_placement(self):
        """Places the turtle on the screen."""
        self.goto(300, random.randrange(-250, 250, 15))
        self.setheading(180)

    def car_movement(self):
        """Moves the car on the screen."""
        self.forward(MOVE_INCREMENT)
