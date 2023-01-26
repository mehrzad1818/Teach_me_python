# "This is Day 5 of One hundred days of coding
# " For Loops, Range and Code Blocks"
# The project of this day is to make a password generator
# Its name is going to be PyPassword Generator


# First concept it

# For Loop

# for item in list_of_items:
# Do something to each item

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
# For is a loop, it goes over and assigns a variable name to your list, which
# that assigned letter or name comes between for and in

# Day 5.1 Average Height Exercise

# "This code will add up the given input in integer and then divide it
# by the number of given data to calculate its average."

student_heights = input("Input a list of student heights ").split(", ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)


# Modified


student_heights = input(
    "Write a list of numbers.\nDon't put comma between them, just a space\n").split()
summy = 0
dividi = 0
for number in range(0, len(student_heights)):
    student_heights[number] = int(student_heights[number])
    summy += student_heights[number]
    dividi += (student_heights[number] / student_heights[number])
print(summy)
print(dividi)

average = (round(summy) / round(dividi))
print(average)

# Day 5.2 Highest Score Exercise
# "As the name suggests, we should return the highest value in a given list using for loops
# unlike the previous code challenge which was about giving the average/mean of something, this one
# stretches beyond that concept."


student_scores = input("Input a list of students scores. \n").split()

value = 0
for student_score in range(0, len(student_scores)):
    student_scores[student_score] = int(student_scores[student_score])
    if value < student_scores[student_score]:
        value = student_scores[student_score]
print(f"The highest score in the class is: {value}")

# Above is the version I came up with, down below is the version proposed by the instructor

student_scores = input("Input a list of student scores. \n").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is: {highest_score}")

# Now we're going to learn about 'Range' function and using it inside the for loop

# "
# for number in range(a, b):
#   print(number)
# "

# Example
for number in range(1, 11):
    print(number)

# You can use steps to modify the slope of change

for number in range(1, 20, 2):
    print(number)


digit = 0
for number in range(1, 101):
    digit += number
print(digit)

# Day 5.3 Code challenge
#"Adding evens exercise"

# This is actually adding odds
odd_total = 0
for number in range(1, 101, 2):
    odd_total += number
print(odd_total)

# For even we use this

even_total = 0
for number in range(0, 101, 2):
    even_total += number
print(even_total)

# Without using step size option

even_total = 0
for number in range(1, 101):
    if ((number % 2) == (0)):
        even_total += number
print(even_total)

# Final project for Day 5 is to make a PyPassword Generatr
#"It's essentially a random number generator."

# "
# I'm going to ask the user for several inputs
#
# 1. How long do you want your password to be?
# 2. What characters do you want to include?
#
# "

passlength = input("Which letters do you want in your password?\n")


list1 = []
list1[:0] = passlength

print(list1)


# The code above shows how to do string slice


nr_letters = int(input("How many letters do you want?\n"))
nr_numbers = int(input("How many numbers do you wnat?\n"))
nr_icons = int(input("How many icons do you want?\n"))

letters_list = []
numbers_list = []
icons_list = []

password = ""

letters_list[:0] = "ZAQWSXCDERFVBGTYHNMJUIKLOPzaqwsxcderfvbgtyhnmjuiklop"
numbers_list[:0] = "0321654987"
icons_list[:0] = "!@#$%-+=&*()"

for letter in range(0, nr_letters):
    letters_list[letter] = str(letters_list[letter])
