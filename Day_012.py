# This is the 12th day of Learning Python
# We will learn about Global and Local Namespaces and also Scopes

# What is Scope?

# Scope is like planting an apple tree in your house.
# If it is planted inside your garden with fences around it,
# it is you and your family which can only access it.

# But it it's on the sidewalk, it is accessed by everyone.

# This example below will illustrate the points:

from random import randint
import random
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope:


def drink_potion():
    potion_strenght = 2
    print(potion_strenght)


drink_potion()
print(potion_strenght)

# When you create a new variable inside a FUNCTION, it is only available inside that function


# Global Scope

player_health = 10  # This is a global variable


def game():
    def drink_potion():
        potion_strenght = 2  # This is a local variable
        print(potion_strenght)
        print(player_health)


drink_potion()
print(player_health)

# In Python, there's no such thing as Block Scope:
if 3 > 2:
    a_variable = 10

game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[5]

    print(new_enemy)


print(enemies)


# How to modify a Global Variable?
# Modifiying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# So, the above method, which is changing global scope values is not recommended since it is prone to make mistakes and code breaks
# What do we do instead?

enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside functino: {enemies}")

# Global Scopes have their own usage, too

# Global Constants
# They are used for variable which are not going to be modified ever again in the code.
# The convention is to name them in all uppercase to recognize them in the code


PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "nameme"


def calc():
    PI


# Number Guessing Game
logo = """
   ___                       _____                  __                 _
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|

"""


answer = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.")
print(f"Psssst, the correct answer is {answer}")

HARD_MODE = 5
EASY_MODE = 10

guess = []
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "hard":
    print(f"You have {HARD_MODE} attempts remaining to guess the number.")
elif difficulty == "easy":
    print(f"You have {EASY_MODE} attempts remaining to guess the number.")


def compare(difficulty, answer, guess):
    """This function compares the input value with randomly generated one."""

    if difficulty == "hard":
        return HARD_MODE
    elif difficulty == "easy":
        return EASY_MODE

    while difficulty != 0:
        guess = int(input("What is your guess?\n"))

        if answer > guess:
            print("Too low.")
            HARD_MODE -= 1
        if guess > answer:
            print("Too high.")
        if guess == answer:
            print("You guessed right.")


compare(difficulty, answer, guess)

# Completed Version


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


set_difficulty()


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)
print(f"Pssst! The correct answer is {answer}.")

turns = set_difficulty
print(f"You have {turns} attempts remaining to guess the number.")


guess = int(input("Make a guess: "))
