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

# Now that we are done with the challenge, this part contains if/elif/else statements

# Multiple if conditions:

# "Take a look at this example

# if condition1:
#   do A
# if condition2:
#   do B
# if condition3:
#   do C
#
# "

print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photograph? Y or N. ")
    if wants_photo == "Y":
        bill += 3
else:
    print("Grow up!")

# " The code above although contained basic
# principles of formatting and multiple if, nested if, and elif else conditions
# I found it rather confusing due to its hierarchical nature."

# Code Challenge!
# This is code challenge 3.4 and its name is Python Pizza Order Program (PPOP)

print("Welcome to Python Pizza Order Program (PPOP).\n")

size = input("What size pizza do you want? S, M or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is ${bill}.")
    else:
        print(f"Your bill is ${bill}.")
if size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is ${bill}.")
    else:
        print(f"Your bill is ${bill}.")
if size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your bill is ${bill}.")
    else:
        print(f"Your bill is ${bill}.")
else:
    print("WRONG INPUT!")

# The above code that I wrote comes from a less efficient way of thinking about it.
# Instead of integrating functions (machines) inside each other, you can simply feed the product of one function (machine) into the next one.
# The code below I believe is more efficient in terms of maintenance and comprehensibility.

print("Welcome to Python Pizza Order Program (PPOP).\n")

size = input("What size pizza do you want? S, M or L\n")
add_pepperoni = input("Do you want pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")

# Logical Operators

# Now we are going to find about how to chain multiple conditions in the same line of code
# "
# A and B
# C or D
# not E
# "

# We're going to modify our previous code and add "free tickets for those dealing with
# middlelife crisis" into our code using logical operators.

print("Welcome to the rollercoaster!\n")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Carry on! You are half the way through. Your ticket is payed by the government.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photograph? Y or N. ")
    if wants_photo == "Y":
        bill += 3
else:
    print("Grow up!")

# Another code challenge!
# Day 3.5 Love Calculator Exercise

print("Welcome to the Love Calculator!\n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1lower = name1.lower()
name2lower = name2.lower()

T_counts = int(name1lower.count("t") + name2lower.count("t"))
R_counts = int(name1lower.count("r") + name2lower.count("r"))
U_counts = int(name1lower.count("u") + name2lower.count("u"))
E_counts = int(name1lower.count("e") + name2lower.count("e"))

L_counts = int(name1lower.count("l") + name2lower.count("l"))
O_counts = int(name1lower.count("o") + name2lower.count("o"))
V_counts = int(name1lower.count("v") + name2lower.count("v"))
E_counts = int(name1lower.count("e") + name2lower.count("e"))

first_digit = T_counts + R_counts + U_counts + E_counts
second_digit = L_counts + O_counts + V_counts + E_counts
whole_number = first_digit * 10 + second_digit

if whole_number < 10 or whole_number > 90:
    print(
        f"Your score is {whole_number}, you go together like coke and mentos.")
elif whole_number > 40 and whole_number < 50:
    print(f"Your score is {whole_number}, you are alright together.")
else:
    print(f"Your score is {whole_number}.")

# One more time with more efficiency

print("Welcome to the Love Calculator!\n")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

low_name_str_comb = (name1 + name2).lower

T = int(low_name_str_comb.count("t"))
R = int(low_name_str_comb.count("r"))
U = int(low_name_str_comb.count("u"))
E = int(low_name_str_comb.count("e"))
L = int(low_name_str_comb.count("l"))
O = int(low_name_str_comb.count("o"))
V = int(low_name_str_comb.count("v"))

truedigit = T + R + U + E
lovedigit = L + O + V + E

lovescore = int((str(truedigit) + str(lovedigit)))

if whole_number > 90:
    print(
        f"Your score is {whole_number}, you go together like coke and mentos.")
elif whole_number > 40 and whole_number < 50:
    print(f"Your score is {whole_number}, you are alright together.")
else:
    print(f"Your score is {whole_number}.")


# This is the final code challenge which is about making a story-driven code.
# This is somwhow the most basic form of video games.
# It reminded me of Fallout game.

print("Welcome to Treasure Island.\n Your mission is to find the treasure.\n")

left_or_right = input(
    "You'll arrive at a crossroad, you can either go right or left.\nThere's a thick forest on the right and a rocky cliff on the left.\n Which way do you go? Type 'left' or 'right'.\n")
if left_or_right == "right":
    print("You walk down the rainforest, as you are following the path, a snake bites your ankle and you have a horrible death.\n GAME OVER")
else:
    print("You climb the rocks. You fall down in the river while climbing a loose rock. You survive the fall but your head aches a lot.\n")

    swim_or_wait = input("You a are in the river. The water flows to north, where your plane was crashed. There's another worn path next to the river that might leads to a hut.\nWhich way do you go? Do you swim or walk to the worn path? Type 'swim' or 'walk'.\n")

    if swim_or_wait == "swim":
        print("You follow the run of the river. As you move forward, the stream gets more powerful.\n You are floating now and in front of you there's a waterfall.\nYour head explodes after falling down. Even carnivore fish are not interested in your mutilated corpse.\nGAME OVER")
    else:
        print("You arrive at the hut. It's old but it's strangely spacious.")

        red_blue_yellow = input(
            "There are three doors in front of you. Which one do you open? Type 'red', 'blue' or yellow.")
        if red_blue_yellow == "red":
            print(
                "A loaded shotgun was wiretrapped to the door. Your head explodes from the shot.\nGAME OVER")
        elif red_blue_yellow == "blue":
            print("You open the door, but what's there beyond it? A hungry tiger crushes your skull before you break a sweat.\nGAME OVER")
        else:
            print("There's a golden chest full of gold coins ahead you. The chest is as large as two king-sized beds put together.\nYOU WON!")
