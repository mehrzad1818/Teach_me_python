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
