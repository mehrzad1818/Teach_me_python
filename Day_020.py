# main.py

import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake_up, "Up")
screen.onkey(snake_down, "Down")
screen.onkey(snake_left, "Left")
screen.onkey(snake_right, "Right")


GAME_IS_ON = True

while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()


# snake.py


from turtle import Turtle
STARTING_POSITIONS = [(+20, +20),(+40, +20),(+60, +20)]
MOVE_PITCH = 20
YAW = 90

class Snake:
    """This is Buji's snake module."""

    def __init__(self):
        self.all_snakes_body = []
        self.create_snake()

    def create_snake(self):
        """This function creates the snake."""
        for turtle_index in STARTING_POSITIONS:
            snakes_body = Turtle(shape="square")
            snakes_body.penup()
            snakes_body.color("white")
            snakes_body.goto(turtle_index)
            self.all_snakes_body.append(snakes_body)

    def move(self):
        """This function moves the snake on the screen."""
        for snakes_part in range(len(self.all_snakes_body) - 1, 0, -1):
            new_x = self.all_snakes_body[snakes_part - 1].xcor()
            new_y = self.all_snakes_body[snakes_part - 1].ycor()
            self.all_snakes_body[snakes_part].goto(new_x, new_y)
        self.all_snakes_body[0].forward(MOVE_PITCH)
        self.all_snakes_body[0].left(YAW)

    def turn_left(self):
        """This function turns the snake to the left on the screen."""
        
