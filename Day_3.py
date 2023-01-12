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
    if age >= 18:
        print("You should pay 20$.")
    else:
        print("You should pay 10$.")
else:
    print("Return when you grow up.")

# If you have more conditions, you can add more conditions by using elif, like this:

print("Welcome to the rollercoaster!\n")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You are good to you.")
    age = int(input("How old are you? "))
    if age <= 12:
        print("You should pay 10$.")
    elif age <= 18:
        print("You should pay 15$.")
    else:
        print("You should pay 20$.")
else:
    print("Get back here when you are taller!")

# This is somehow a little bit more complex

print("Welcome to the rollercoaster!\n")

height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("How old are you? "))
    print("You are good to you.")

    if age <= 12:

        print("You should pay 10$.")

        toys = int(input("How many toys do you have? "))

        if toys <= 5:
            print("You will get a free toy at the end of your ride!")

        else:
            print("There is no free toy for you!")

    elif age <= 18:
        print("You should pay 15$.")
        girlfriend = int(input("How many girlfriend do you have? "))

        if girlfriend == 0:
            print("Get a girlfriend before hopping on this rollercoaster!")
        elif girlfriend > 1:
            print(
                "You are a traitor and you are not welcommed here. Leave the area immediately!")
        else:
            print("You are a man of culture my friend.")
    else:
        print("You should pay 20$.")
        sex = int(input("How often do you have sex in a month? "))
        if sex >= 10:
            condom = int(input("Do you use condoms? (1 for Yes, 0 for No) "))
            if condom == 1:
                print("Nice job! Stay safe.")
            else:
                print("You should always wear one!")
        elif 0 < sex < 10:
            print("You should have more sexual activity.")
        else:
            print("Hire a dick.")

else:
    print("Get back here when you are taller!")

# Above, I basically went to far with if, elif and else (somehow too far,) and used nested code to have a multifaceted code.


# Code challenge 3.2 is BMI Calculator version 2.0


print("Welcome to BMI Calculator.\n")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(((weight // (height ** 2))))

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You are obese.")
else:
    print(f"Your BMI is {bmi}. You are clinically obese.")

# Code challenge 3.3 Leap year calculator

# To calculate leap years, it must meet these criteria:

# "on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400"

# The form I come up with is like this:

year = int(input("Which year do you want to check? "))

if (year % 4) == (0):
    if (year % 100) != (0):
        if (year % 400) != (0):
            print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Versus this one which was proposed in the video course.

year = int(input("WHich year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
