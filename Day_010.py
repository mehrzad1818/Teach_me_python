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
