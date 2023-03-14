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
