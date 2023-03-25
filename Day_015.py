# It's day 15 and we're no longer a beginner. Welcome to being an intermediate python developer.

# This day we dealt with installing IDE's and getting used to new coding environment
# Today's project is about creating a coffee machine.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


choice = input(str("What would you like? (espresso/latte/cappuccino)\n")).lower

print()
