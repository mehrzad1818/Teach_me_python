# Welcome to Day 1 of 100 Days coding challenge

# This is the most basic type of code on can ever write.

print("Hello world!")

# Example of attaching an input function to an object
year = int(input("Which year do you want to check?"))

# Printing few arguments with each individual function operator

# Printing using \n inside the string to add new line
print("Hello world!\nWelcome to this world!\nOur Brave New World :)")

# This new method is used to optimize the below code
print("Hello world!")
print("Hello world!")
print("Hello world!")
# Now optimized: ...
print("Hello world!\nHello world!\nHello world!")

# String Concatenation

# Concatinating the strings in a given function
print("Hello" + "Mehrzad")
# There are three possible (known to my knowledge) that this problem can be solved:
#   1. Add space at the end of the first string "Hello "
#   2. Add space at the beginning of the second string " Mehrzad"
#   3 Add an individual space string that looks like this " "
print("Hello" + " " + "Mehrzad")

# This is an exercise from Day 1-2
print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello" + " " + "world")')
print("New lines can be created with a backslash and \n")


# Input function (plus some concatenation and nesting)
print("Hello" + ' ' + input("What to do you like to ba called?") + '!')

# This is exercise from Day 1-3
print(len(input("Write down you name please." )))
# The exercise above focuses on the lenght 'len()' function which is used for calculating the number of characters inside a string.


# Variables

name = input("What is your first name?")
last_name = input("What is your last name?")
nickname = input("What is your nickname?")
age = input("How old are you?")

# Another version of Day 1-3 exercise
name = input("Write your name.")
lenght = len(name)
print(lenght)

# This day's final code challenge, which is Day 1-4

a = input("a:")
b = input("b:")

x = a
y = b

a = y
b = x

print("a = " + a)
print("b = " + b)

# I did something very stupid with the code above,
# the thing is that you want to switch the content of 2 cups,
# in that case you need a third cup, but I used a fourth cup,
# I'm going to write this code down below using only one extra variable

a = input("a:")
b = input("b:")

x = a
a = b
b = x

print("a = " + a)
print("b = " + b)

# Another version, still using the same method
a = input("a:")
b = input("b:")

x = b
b = a
a = x

print("a = " + a)
print("b = " + b)

# This is the final project
# FINAL PROJECT
# Project Description:
# A "Band name generator" app is going to be built
# using new ideas learnt throughout this part of course module

print("Welcome to Band Name Generator app\nProduced by Mehrzad Barzegar")
city = input("Write the name of your city.\n")
pet = input("Write the name of your pet.\n")
print("Your band name could be " + city + " " + pet)
