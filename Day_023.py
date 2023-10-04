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
