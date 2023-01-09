# Welcome to Day 3 of 100 Days coding challenge

# "You'll learn about 'Conditional Statements', such as if, elif, else ...
# and 'Logical Operators', Code Blocks and Scope"
# "
# if condition:
#   do this
# else:
#   do that"

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You are good to go.")
else:
    print("Grow up, dude!")


# We have 'Comparison Operators' which are as follows:

# "  >  ----> Greater than
#   <  ----> Lesser than
#   >= ----> Greather than or equal to
#   <= ----> Lesser than or equal to"

# one equal sign is used for assigning something to something else, whereas two equal sings are used to check equality of something to something else

# == equals to
# != not equals to


# New Code Challenge: 3.1
# In this challenge, you are to build an odd/even checker using basic mathematical operations and common sense!


number = int(input("Which number do you want to check?\n"))

if ((number % 2) == (0)):
    print("Your number is even!")
else:
    print("Your number is odd!")

# Nested if/else
# Nesting basically means putting another if condition into another condition.


print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
age = int(input("How old are you? "))

if height >= 120:
    print("You are good to go.")
    if age = > 18:
        print("You should pay 20$.")
    else:
        print("You should pay 10$.")
else:
    print("Return when you grow up.")
