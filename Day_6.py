# "This is the beginning of Day 6
# We're going to learn about function, code blocks and while loop."

# 1. Functions

# Python has many buil-in functions, some basic examples are down below:

print("Hello")
print(len("Hello"))
print(len(str(2345698)))

# Now, we are going to learn how to "define" our own functions:


def here_is_my_first_function():
    print("Hey there!")
    2 + 2
    print("Are you fine?")
    input("Answer the question above.\n")


here_is_my_first_function()

# So, to call a function means that we want to use our function.


# Most of the tasks and challenges of this Day are carried out in reeborg.ca website

# This is for hurdle 1 challenge using for loop at the end

hurdles = input("How many hurdles are you jumping?")
numberofjumps = int(hurdles)


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for hurdle in range(0, numberofjumps):
    move()
    jump()

# This is for hurdle 1 challenge using while loop at the end

hurdles = input("How many hurdles are you jumping?")
numberofjumps = int(hurdles)


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while numberofjumps > 0:
    move()
    jump()
    numberofjumps -= 1

# This is for hurdle challenge 3, which walls are created randomly


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


# This is challenge for hurdle number 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while front_is_clear() and not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear() and not right_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
