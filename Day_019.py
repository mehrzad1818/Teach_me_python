# This is the 19th day of 100 days of Python.


# This module uses event listener to trigger a funciton based on the given input (real-time input).
# %%
import random
from turtle import Turtle, Screen

# import random

tim = Turtle()
screen = Screen()


def move_forward():
    """Responsible for moving Tim on the screen."""
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()

# This part is like some sort of combining different functions together.
# We pass in the outcome of one function into income of the other function.

# %%
# def function_a(something):

#     # Do this with something
#     # Then do this
#     # Finally do this


# def function_b(function_a):
#     # Do this
# %%
import random
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    """Tim goes forwaaarrrddd."""
    tim.forward(10)


def move_backward():
    """Tim goes backwaaarrrddd."""
    tim.backward(10)


def yaw_clockwise():
    """Tim goes weeeeeee."""
    tim.right(5)


def yaw_c_clockwise():
    """Tim goes wooooooo."""
    tim.left(5)


def reset():
    """Tim goes baaaaaaaaack."""
    tim.reset()


screen.listen()
screen.exitonclick


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=yaw_clockwise)
screen.onkey(key="a", fun=yaw_c_clockwise)
screen.onkey(key="c", fun=reset)

# %%
# This is turtle race challenge:


screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(
    title="Make your bet!", prompt="Which turtle will win the race? Enter a color."
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, +20, +60, +100]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-225, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} is the winner!")
            else:
                print(f"You lost! The {winning_color} was the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
