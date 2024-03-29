# "This is Day 4,
# We are going to learn about Randomisation and Python Lists.
# This section deals with new, challenging codes."

# Random function import

import numpy as np
import random
a = random.randint(100, 1000)
print(a)

# Modules
# "Modules are made just like another file. For example, even this code that we are writing inside the file "Day_4.py" can be a module."
# You say how? Let me show you."

# "Imagine this is the module we've written on a separate file.
#
# pi = 3.14159265
#
# This is just the file.
#
# Here's our code in a separate file. We've saved its name as 'mymodule'.

# "import mymodule
#
# print(mymodule.pi)
#
# It would print: 3.141592"
# "

b = random.random()
print(b)


random_int = random.randint(0, 5)
random_flo = random.random()

print((str(random_int) + str(random_flo)))

# Random float gives you a float between 0.000000000....1 to 0.99999999999....

random_flo5 = random_flo * 5
print(random_flo5)

# One usage is that we can optimize our random love score calculator

random_love = random.randint(1, 100)
print(f"Your love score is {random_love}.")

# This is a code challenge, code challenge 4.1

# since the code editor will omit the imported module since it has already been imported, I'll comment it out.

# import random

random_digit = random.randint(1, 1000)
remainder = random_digit % 2
if remainder == 0:
    print("Tails")
else:
    print("Heads")

# A more efficient way is this:

random_side = random.randint(0, 1)
if random_side == 0:
    print("Tails")
else:
    print("Heads")

# This part of the tutorial deals with Lists in Python

# A basic example would be like this:

item1 = "banana"
item2 = "apple"

fruits = [item1, item2]

print(fruits)

# List always starts and ends with square brackets.

fruits = ["Cherry", "Apple", "Pear"]
print(fruits)

# In this project, we'll list the US states.

states_of_america = ["Delaware", "Pennsylvania",
                     "New Jersey", "Georgia", "Connecticut", "Hawaii"]
print(states_of_america[0])

# You can modify the things in the list too

states_of_america[3] = "Jorjia"
print(states_of_america)

# append function will add things to end of a list

states_of_america.append("Moroland")
print(states_of_america)

# Challenge 4.2 - This challenge's name is Bill Roulette
names_string = input(
    "Give me the name of people who are at the table. (Separate names by a comma.)\n")

actual_list = names_string.split(", ")
counted_list = len(actual_list)
randominteger = random.randint(0, counted_list - 1)
chosen_person = actual_list[randominteger]

print(f"{chosen_person} is going to pay the bill.")

# More efficient way is like this to do bill roulette

names_string = input(
    "Give me the name of people who are at the table. (Separate names by a comma.)\n")
actual_list = names_string.split(", ")
chosen_person = random.choice(actual_list)
print(f"{chosen_person} is going to pay the bill.")

# Here's a list of dirty dozen

dirty_dozen = "Strawberries, Spinach, Kale, Nectarines, Apples, Grapes, Peaches, Cherries, Pears, Tomatoes, Celery, Potatoes"

listed_dirty_dozen = dirty_dozen.split(", ")

fruitindex = [[0, 3, 4, 5, 6, 7, 8]]

listed_fruits = [listed_dirty_dozen[i] for i in fruitindex]

listed_vegetables = listed_dirty_dozen - listed_fruits

sortedlisted_dirty_dozen = [listed_fruits, listed_vegetables]
print(sortedlisted_dirty_dozen)

a = [-2, 1, 5, 3, 8, 5, 6]
b = [1, 2, 5]
c = [a[i] for i in b]
print(c)

# Code challenge 4.3 - Treasure Map Exercise

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

stringed_position = (str(position))
columndigit = int(stringed_position[0])
rowdigit = int(stringed_position[1])

if columndigit == 1 and rowdigit == 1:
    row1[0] = "X"
if columndigit == 2 and rowdigit == 1:
    row1[1] = "X"
if columndigit == 3 and rowdigit == 1:
    row1[2] = "X"

if columndigit == 1 and rowdigit == 2:
    row2[0] = "X"
if columndigit == 2 and rowdigit == 2:
    row2[1] = "X"
if columndigit == 3 and rowdigit == 2:
    row2[2] = "X"

if columndigit == 1 and rowdigit == 3:
    row3[0] = "X"
if columndigit == 2 and rowdigit == 3:
    row3[1] = "X"
if columndigit == 3 and rowdigit == 3:
    row3[2] = "X"

print(f"{row1}\n{row2}\n{row3}")

# The code that I typed above does not include the parts and parcels of using list manipulation tools provided by Python
# It employs codes from if statements and ends up having too much code.
# Instead of trying to map out every possible situation, think about it like choosing the corresponding spot and changing it with the desired value.
# The more clear form would be something like this:


row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

columndigit = int(position[0])
rowdigit = int(position[1])


selectedrow = map[rowdigit - 1]
selectedrow[columndigit - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")

# More efficient way (which the logic is simple if you think about it in mathematical terms)

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

columndigit = int(position[0])
rowdigit = int(position[1])

map[rowdigit - 1][columndigit - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# Rock Paper Scissors

# Rock

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print("Welcome to RPS game!")
initial_input = input(
    "To begin, type 0 for rock, 1 for paper, or 2 for scissors.\n")

human_input = int(initial_input)
pc_random_input = random.randint(0, 2)

choices_list = [human_input, pc_random_input]
shapes = [rock, paper, scissors]

if choices_list[0] == choices_list[1]:
    print(shapes[human_input])
    print("Computer chose: \n")
    print(shapes[pc_random_input])
    print("It's a draw.")
elif choices_list[0] > choices_list[1]:
    print(shapes[human_input])
    print("Computer chose: \n")
    print(shapes[pc_random_input])
    print("You win.")
elif choices_list[1] > choices_list[0]:
    print(shapes[human_input])
    print("Computer chose: \n")
    print(shapes[pc_random_input])
    print("You lose.")
else:
    print(shapes[human_input])
    print("Computer chose: \n")
    print(shapes[pc_random_input])
    print("You lost.")
