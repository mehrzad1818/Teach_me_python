# This is the day 20 of 100 days of Python.
# We're going to make a snake game in two days.'

# The problems are as follow:

# 1. Create a snake body
# 2. Move the snake
# 3. Create snake food
# 4. Detect collision with food
# 5. create a scoreboard
# 6. detect collision with wall
# 7. detect collision with tail


from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

x_positions = [0, -20, -40]
all_snakes_body = []


for turtle_index in range(0, 3):
    snakes_body = Turtle(shape="square")
    snakes_body.penup()
    snakes_body.color("white")
    snakes_body.goto(x=x_positions[turtle_index], y=0)
    all_snakes_body.append(snakes_body)


GAME_IS_ON = True

while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)


    for snakes_part in range(len(all_snakes_body) - 1, 0, -1):
        new_x = all_snakes_body[snakes_part - 1].xcor()
        new_y = all_snakes_body[snakes_part - 1].ycor()
        all_snakes_body[snakes_part].goto(new_x, new_y)


    # for snakes in all_snakes_body:
    #     snakes.forward(20)
    # all_snakes_body[0].left(90)




screen.exitonclick()
