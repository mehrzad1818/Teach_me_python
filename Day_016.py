# This is Day 16 of 100 Days of Code.
# "Today we are learning about "Object Oriented Programming.""

# In Procedure Programming which we've been doing so far,
# all of the components are connected together from disparate areas.

# OOP is like assigning a group of people to run a restaurant.
# In PRocedural programming, you are supposed to be the "ONE" person who
# does all of the things, but in OOP, you are just the manager looking at your staff
# without telling them what to do, because they are already trained for it.


# How to use OOP????
from turtle import Turtle, Screen

# A real life example of OOP implementation would be a virtual waiter.
# The two essential attributes of the waiter would be:

# 1. What it has (attributes):
IS_HOLDING_PLATE = True
tables_responsible = [4, 5, 6]

# 2. What it does (methods):


def take_order(table, order):
    """ Takes order """


def take_payment(amount):
    """ add money to the restaurant """


# In OOP, we have object and class. Object is the product and Class is the category in which the object is produced from.
# Take a look at this example:

# car = CarBlueprint()

# The piece of code above is an example of object/class.
# The class is always written in Pascal typecase (CapitalizingEachWordInTheName)

oscar = Turtle()
print(oscar)
oscar.shape("turtle")
oscar.color("blue")
oscar.goto(100, 100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Car has 100 kph and 45L fuel:
# Object/Attribute
# car.speed
# car is the object/speed is the attribute.

# Car is moving and is going at 80 kph
# Object/Method
# car.stop()
# car is the object/stop() is the method
