"""Main file of Day 20 of 100 Days of Python."""
# List of dependencies

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setup

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Tricky Snake Game")
screen.tracer(0)

# Objects we've created from our classes

snake = Snake()
food = Food()
score = Scoreboard()

# This part listens for keystrokes

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# The actual game itself with its switches and ...

GAME_IS_ON = True
while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.food_regenerate()
        snake.extend()
        score.add_score()

    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        GAME_IS_ON = False
        score.game_over()

    for box in snake.box_list:
        if box == snake.box_list[1] and box == snake.box_list[2]:
            pass
        if snake.head.position() == box.position():
            GAME_IS_ON = False
            score.game_over

# Termination sequence

screen.exitonclick()



"""This module contains Scoreboard class."""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
COLOR = "white"


class Scoreboard(Turtle):
    """Generates food on the board."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.setposition(0, 260)

    def add_score(self):
        """Keeps the track of score."""

        self.score += 1
        self.clear()
        self.write(
            arg=f"Score: {self.score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        """Shows the player that the game is finished."""
        self.setposition(0, 0)
        self.write(
            arg="GAME OVER.",
            align=ALIGNMENT,
            font=FONT,
        )

"""This class contains the snake body and it's behavior."""

from turtle import Turtle

MOVE_DISTANCE = 20
PITCH = 20
HOME = (0, 0)
UP, DOWN, LEFT, RIGHT = (90, 270, 180, 0)


class Snake:
    """Snake: Body and Movement"""

    def __init__(self):
        """Triggers the snake."""

        self.box_list = []
        self.create_snake()
        self.head = self.box_list[0]

    def create_snake(self):
        """Creates the three inchoate parts of the snake."""

        for __ in range(3):
            new_box = Turtle(shape="square")
            new_box.color("white")
            new_box.penup()
            self.box_list.append(new_box)

        for index, turtle in enumerate(self.box_list):
            turtle.setx((-1 * PITCH * index))

        return

    def add_box(self, position):
        """Creates a piece for the snake."""

        new_box = Turtle(shape="square")
        new_box.color("white")
        new_box.penup()
        self.box_list.append(new_box)

    def extend(self):
        """Adds that piece to the snake."""

        self.add_box(self.box_list[-1].position())

    def move(self):
        """Places the boxes in their default position"""

        for box in range(len(self.box_list) - 1, 0, -1):
            new_x = self.box_list[box - 1].xcor()
            new_y = self.box_list[box - 1].ycor()
            self.box_list[box].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

        return self

    def up(self):
        """Turns the snake facing up."""

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turns the snake facing down."""

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turns the snake facing left."""

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turns the snake facing left."""

        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


"""This module contains Food class."""

from turtle import Turtle
import random


class Food(Turtle):

    """Generates food on the board."""

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.food_regenerate()

    def food_regenerate(self):
        """Randomly makes another food."""
        self.setposition(random.randint(-280, 280), random.randint(-280, 280))
