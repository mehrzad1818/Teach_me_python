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


from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


screen.exitonclick()
