"""Main file of Day 20 of 100 Days of Python."""

from turtle import Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Tricky Snake Game")
screen.tracer(0)


snake = Snake()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

GAME_IS_ON = True
while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()



"""This class contains the snake body and it's behavior."""

from turtle import Turtle

MOVE_DISTANCE = 20
PITCH = 20
HOME = (0, 0)


class Snake:
    """Snake: Body and Movement"""

    def __init__(self):
        """Triggers the snake."""

        self.box_list = []
        self.create_snake()

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

    def move(self):
        """Places the boxes in their default position"""

        for box in range(len(self.box_list) - 1, 0, -1):
            new_x = self.box_list[box - 1].xcor()
            new_y = self.box_list[box - 1].ycor()
            self.box_list[box].goto(new_x, new_y)
        self.box_list[0].forward(MOVE_DISTANCE)

        return self

    def up(self):
        """Turns the snake facing up."""
        for box in range(len(self.box_list) - 1, 0, -1):
            new_x = self.box_list[box - 1].xcor()
            new_y = self.box_list[box - 1].ycor()
            self.box_list[box].goto(new_x, new_y)

            if (
                self.box_list[0].pos()[0] > self.box_list[1].pos()[0]
            ):  # darhal harkat be samte raast
                self.box_list[0].left(90)
            elif (
                self.box_list[0].pos()[0] < self.box_list[1].pos()[0]
            ):  # darhal harkat be samte chap
                self.box_list[0].right(90)

    def down(self):
        """Turns the snake facing down."""
        for box in range(len(self.box_list) - 1, 0, -1):
            new_x = self.box_list[box - 1].xcor()
            new_y = self.box_list[box - 1].ycor()
            self.box_list[box].goto(new_x, new_y)

            if (
                self.box_list[0].pos()[0] > self.box_list[1].pos()[0]
            ):  # darhal harkat be samte raast
                self.box_list[0].right(90)
            elif (
                self.box_list[0].pos()[0] < self.box_list[1].pos()[0]
            ):  # darhal harkat be samte chap
                self.box_list[0].left(90)

    def left(self):
        """Turns the snake facing left."""
        for box in range(len(self.box_list) - 1, 0, -1):
            new_x = self.box_list[box - 1].xcor()
            new_y = self.box_list[box - 1].ycor()
            self.box_list[box].goto(new_x, new_y)

            if (
                self.box_list[0].pos()[1] > self.box_list[1].pos()[1]
            ):  # darhal harkat be samte raast
                self.box_list[0].left(90)
            elif (
                self.box_list[0].pos()[1] < self.box_list[1].pos()[1]
            ):  # darhal harkat be samte chap
                self.box_list[0].right(90)

    def right(self):
        """Turns the snake facing left."""
        for box in range(len(self.box_list) - 1, 0, -1):
            new_x = self.box_list[box - 1].xcor()
            new_y = self.box_list[box - 1].ycor()
            self.box_list[box].goto(new_x, new_y)

            if (
                self.box_list[0].pos()[1] > self.box_list[1].pos()[1]
            ):  # darhal harkat be samte raast
                self.box_list[0].right(90)
            elif (
                self.box_list[0].pos()[1] < self.box_list[1].pos()[1]
            ):  # darhal harkat be samte chap
                self.box_list[0].left(90)
