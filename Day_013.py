# This is the 13th Day of 100 Days of Code

# Debugging points

# Grace Hopper found the first bug.
# Everyone gets bugs.


# 1. Describe th Problem:
#       you should be able to make sense of what is wrong.


from random import randint


# Code with error

def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Fixed Code


def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()


# 2. Reproduce the Bug
#       when you come across a bug,
#       try to make it again and again since if it reoccures,
#       it means it has a pattern

# Code with reproduced error

dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = 6
print(dice_imgs[dice_num])

# Fixed code

dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# 3. Play Computer
#       Try to think like a computer,
#       going through each process one by one

# Code with error

year = int(input("What's your year of birth?\n"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# Fixed Code

year = int(input("What's your year of birth?\n"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

#  4. Fix the error
#       Errors are often shown by IDE, so fix them as soon as you see them.

# Broken Code

age = input("How old are you? ")
if age > 18:
print("You can drive at age {age}.")

# Fixed code

age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

# 5. Print is your friend
#       Printing a part of your code helps you trace where the problem lies.

# Code with bug

pages = 0
word_per_page = 0

pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))

total_words = pages * word_per_page

print(total_words)

# Fixed Code

pages = 0
word_per_page = 0

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))

total_words = pages * word_per_page

print(total_words)


# 6. Use a Debugger
#       Using debuggers helps you identify
# pythontutor.com and thonny are both great

# Code with error

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# Fixed Code


def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

# 7. Take a break
#       Taking a break makes your mind refreshed and you are able to recognize the problem after rest

# 8. Ask a friend
#       Asking your friend to find you the problem is the best.

# 9. Run often
#       Debug your code after writing a few lines so that you confirmed it

# 10. Ask StackOverflow
#       You can alwyas ask experts on websites to help you


# Day 13.1 - Debug Odd or Even Exercise

# Broken Code

number = int(input("Which number do you want to check?\n"))

if number % 2 = 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Fixed Code

number = int(input("Which number do you want to check?\n"))

if ((number % 2) == (0)):
    print("This is an even number.")
else:
    print("This is an odd number.")


# Day 13.2 - Debug Leap Year Exercise

# Broken Code

year = input("Which year do you want to check?\n")

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

# Fixed Code

year = int(input("Which year do you want to check?\n"))

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

# Day 13.3 - Debug Fizz Buzz Exercise

# Guides and rules:

# 1. Your program should print each number from 1 to 100 in turn.
# 2. When the number is divisible by 3, then instead of printing the number it should print "Fizz".
# 3. When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# 4. And if the number is divisible by both 3 and 5 e.g., 15 then instead of the number it should print "FizzBuzz".

# Broken Code

for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])

# Fixed Code

for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)
