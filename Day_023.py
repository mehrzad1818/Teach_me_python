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
