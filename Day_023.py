"""The next capstone is this. Turtle Crossing Game. Day 23"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

# Object Creation:

screen = Screen()
player = Player()
car = CarManager()
scoreboard = ScoreBoard()

# Screen Setting:

screen.setup(width=600, height=600)
screen.tracer(0)


# Keystrokes listening:

screen.listen()
screen.onkey(player.movement, "w")
screen.onkey(player.movement, "Up")


# Game Runner:

GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()

    car.car_generate()
    car.car_movement()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            GAME_IS_ON = False
            scoreboard.game_over()

    if player.is_finished():
        player.reset_position()
        car.level_up()


screen.exitonclick()


"""Contains the player code for the turtle crossing game."""

from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle, CarManager):
    """Contains the Player attributes."""

    def __init__(self):
        super().__init__()
        self.generate_player()

    def generate_player(self):
        """Makes a snake on the screen."""

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_position()
        self.setheading(90)

    def movement(self):
        """Moves the player along y axis."""

        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        """Realigns the turtle after it has hit with an obstacle or reached the other side."""

        self.setposition(STARTING_POSITION)
        # self.speeding *= 0.9

    def is_finished(self):
        """Detects whether the turtle has reached the other side or not."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


"""Deals with handling the car for the turtle crossing game."""

import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """Manages the movement of the car and their creation."""

    def __init__(self):
        self.all_cars = []
        self.speeding = STARTING_MOVE_DISTANCE

    def car_generate(self):
        """Generates a car-shaped turtle."""
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randrange(-240, 240, 20))
            self.all_cars.append(new_car)

    def car_movement(self):
        """Moves the car on the screen."""
        for car in self.all_cars:
            car.backward(self.speeding)

    def level_up(self):
        """Increases the speed after each crossing over."""
        self.speeding += MOVE_INCREMENT
