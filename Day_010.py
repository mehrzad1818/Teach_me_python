# This is day 10, and it's about "Functions with Outputs"

# This was the simplest form of a function that we learnt how to make.

# def my_function():
#     Do this
#     Then do this
#     Then do that
#     Finally, do this

# This type of function actually took something is the input:

# def my_function(something):
#     Do this
#     then do this to something
#     then do that
#     dinally, do this

# This type actually has an output:

# def my_function():
#     result = 3 * 2
#     return result

# The code above can be written again like this:

# def my_function():
#     return = 3 * 2


# Here's the exercises for functions with outputs:

def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You didn't provide a valid input."
    first_case = first_name.title()
    last_case = last_name.title()
    return f"{first_case}, {last_case}"


print(format_name(input("What is your first name? "),
      input("What is your last name? ")))

# This coding challenge deals with modifing the leap year calculator we did before, this is challenge 10.1:


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """It shows the number of days in the given month."""
    if month > 12 or month < 1:
        return "Invalid month."
    if year == 0:
        return "Invalid year."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# This part talks about 'Docstrings'
# Docstrings are basically a small pieace of information given like some sort of information to help you use the function


# Already used functions with outputs.
length = len(formatted_name)

# Return as an early exit


def format_name(f_name, l_name):
    """Inputs are changed into type case letter."""

    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


# Print vs Return
# Which is which?

# Take a look at this example:
# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number? "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
