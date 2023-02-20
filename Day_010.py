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
    first_case = first_name.title()
    last_case = last_name.title()
    return f"{first_case}, {last_case}"


print(format_name("JimMY", "CaRTEr"))


# This coding challenge deals with modifing the leap year calculator we did before, this is challenge 10.1:

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year")
    else:
        print("Now leap year.")


def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
