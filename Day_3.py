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

number = int(input("Which number do you want to check?\n"))

moduloed = (number % 2)

if moduloed == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")
