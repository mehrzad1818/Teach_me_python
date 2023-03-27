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
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted. """
    print("Please insert coins.")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total = (quarters * 0.25) + (dimes * 0.10) + \
        (nickels * 0.05) + (pennies * 0.01)
    return total


def successful_transaction(money_received, drink_cost):
    """ Teturn True when the payment is accepted, or False if money is insufficient. """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} change.")
        global MONEY
        MONEY += drink_cost
        return True
    print("Sorry. That's not enough money. Money refunded.")
    return False


def make_coffee(drink_name, order_ingredient):
    """ Deduct the required ingredients from the resources. """
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}. ENJOY!")


IS_ON = True

while True:

    choice = input(
        str("What would you like? (espresso/latte/cappuccino)\n"))

    if choice == "off":
        IS_ON = False
    elif choice == "report":

        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${MONEY}")
    else:
        drink = MENU[choice]
        if resources_report(drink["ingredients"]):
            PAYMENT = process_coins()
            if successful_transaction(PAYMENT, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
