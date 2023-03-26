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

MONEY = 0


def resources_report(order_ingredients):
    """ Checks the coffee machine's resources."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")


IS_ON = True

while True:

    choice = input(
        str("What would you like? (espresso/latte/cappuccino)\n")).lower

    if choice == "off":
        IS_ON = False

    elif choice == "report":

        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${MONEY}")

    else:
        drink = MENU[choice]
        resources_report(drink["ingredients"])

# print("Please insert coins.")

# quarters = int(input("How many quarters? "))
# dimes = int(input("How many dimes? "))
# nickels = int(input("How many nickels? "))
# pennies = int(input("How many pennies? "))


# def coffee_process(choice):
#     MENU[choice]


# # print(f"Here is {remainder} in change.")
# # print(f"Here is your {choice}. Enjoy!")


# def report(choice):
#     print(resources)
#     print(deposit)


# def remainder(choice, quarters, dimes, nickels, pennies):
#     """Calculates to remainder money given by the customer."""

#     total_cost = (quarters * 0.25) + (dimes * 0.10) + \
#         (nickels * 0.05) + (pennies * 0.01)

#     choice_cost = MENU[choice:"cost"]

#     change = (total_cost - choice_cost)

#     print(f"Here is {change}$ in change.")
