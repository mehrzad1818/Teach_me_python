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
from prettytable import PrettyTable

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


# Now we are going to use pretty table:

table = PrettyTable()

row_data = ["Pokemon Name", "Type"]
column_data = ["Pikachu", "Electric"], [
    "Squirtle", "Water"], ["Charmander", "Fire"]


table.field_names = row_data
table.add_rows(column_data)
table.align = "l"
table.valign = "c"
print(table)


class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

        
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

        
        
class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
