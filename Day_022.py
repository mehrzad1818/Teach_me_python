"""This is Day 22 of 100 Days of Code. We're Going to Learn how to make a PONG game."""

# Dependencies

from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from score import Score

# Screen Settings

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


# Object Creation

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball((0, 0))
score = Score()


# Keystrokes

screen.listen()

screen.onkey(paddle_right.move_paddle_up, "Up")
screen.onkey(paddle_right.move_paddle_down, "Down")

screen.onkey(paddle_left.move_paddle_up, "w")
screen.onkey(paddle_left.move_paddle_down, "s")


# Game Start

GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.movement()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.xcor() > 320 and ball.distance(paddle_right) < 50) or (
        ball.xcor() < -320 and ball.distance(paddle_left) < 50
    ):
        ball.collision()

    if ball.xcor() > 380:
        ball.reset_position()
        score.add_score_left()

    if ball.xcor() < -380:
        ball.reset_position()
        score.add_score_right()

# Game Exit

screen.exitonclick()



"""This module contains the necessary code to make and control the ball in the Pong game."""
from turtle import Turtle


class Ball(Turtle):
    """Creates a ball and controls it."""

    def __init__(self, coordinates) -> None:
        super().__init__()
        self.create_ball(*coordinates)

    def create_ball(self, *coordinates):
        """Creates the ball for the game."""
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(coordinates[0], coordinates[1])
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def movement(self):
        """Moves the ball."""

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        """Makes the ball bounce!"""

        self.y_move *= -1

    def collision(self):
        """Makes the ball bounce from the paddle."""

        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """Resets the position of the ball to the center after it has passed through a paddle."""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.collision()



"""This class is about the paddles. Their creation, movement and ..."""
from turtle import Turtle


class Paddle(Turtle):
    """Paddle and stuff."""

    def __init__(self, coordinates) -> None:
        super().__init__()
        self.create_paddle(*coordinates)

    def create_paddle(self, *coordinates):
        """Creates a paddle."""
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates[0], coordinates[1])

    def move_paddle_up(self):
        """Moves the paddle up."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        """Moves the paddle down."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




"""This is the scoreboard class for the Pong game."""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 36, "normal")
COLOR = "white"


class Score(Turtle):
    """Keeps the score."""

    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update_score()

    def update_score(self):
        """Updates the scoreboard."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_left, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.score_right, align=ALIGNMENT, font=FONT)

    def add_score_left(self):
        """Adds a score."""
        self.score_left += 1
        self.update_score()

    def add_score_right(self):
        """Adds a score."""
        self.score_right += 1
        self.update_score()
