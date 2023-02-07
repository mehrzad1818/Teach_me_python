# This file contains projects and new concepts from Day 8 of 100 Days of Python
# Day 8 is about function with capability of input, arguments and parameters
# The final project is about making a ceasar cipher program which deals
# encrypt and decrypt messages

# def my_function():
#     # Do this
#     # Do that
#     # Then do this and this
#     # Done

def greet():
    print("Hello,")
    print("Welcome to your program.")
    print("I hope you enjoy your stay.")


greet()

# So, to make functions with input capability, we need to add arguments into parantheses.
# Like this:

# def my_function(blah blah blah blah):
#     # Do this to blah blah blah
#     # Do that to the rest of blah blahs
#     # Then do this and this
#     # Done

# In this way, we can change the function based on the given input

# Here's an example that allows for input


def greet_with_given_name(name):
    print(f"Hello, {name}")
    print(f"How are you {name}?")


name = input("What is your name? ")

greet_with_given_name(name)


# In the example above, "name" is the parameter, and the for example "Jimmy" is the argument


# This part is about functions with more than one input.

def name_and_last(name, last):
    print(f"Your name is: {name}")
    print(f"Your last name is: {last}\n")

    print(f"Hello, {name} {last}")
    print(f"How are you {name} {last}")


name = input("What is your name? ")
location = input("Where are you from? ")


def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")
