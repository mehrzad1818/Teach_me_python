# Welcome to Day 1 of 100 Days coding challenge

# '"This module is about Data types, which we're going to
# learn 4 types of them, that is: string, float,
# boolean, and interger"

# String data sets are accompanied by two quotation marks around them, like this:

print("This is a test, it can contain TRUE or 153 values.")

# '"Subscripting
# We can find the value of a given string by using subscription"

print("Hello World"[5])
print("This is a test message"[5+4])

# You can see above that we can simply do basic math here, the result in brackets is what it counts

# '"Integer
# In integer, we use whole numbers without any decimel"

# The following code is a string followed by an interger. Pay attention

print("123" + "321")
print(123 + 321)

# '"People split numbers into chunks of three to facilitate readability,
# the same logic applies to pieces of string values, too. Take a look at this example"

large_number = 234_345 + 654_234
print(large_number)

# Underscores are removed by the interpreter

# '"Next, we have Floats. They are numbers who have decimel values. Like Pi for example."

print(3.14 * 15.4)

# '"And finally, we have Booleans.
# They contain two values, either True or False.
# They should start with capital letter. true and false are not Boolean values. "

# Conversion

# Previously we encountered such piece of code:

number_of_characters = len(input("What is your pet's name?"))
print("You pet's name has" + number_of_characters + "characters.")

# type can be determined using type function, like below:

print(type("What is the type of this type?"))

# Conversion from int to str happens by using str() function

number_of_characters = str(len(input("What is your pet's name? ")))
print("You pet's name has " + number_of_characters + " characters.")

# I revised the code by adding necessary spaces in the text and also converting it from int to str

# Conversion is not limited to strings, we can do a whole bunch of conversions. Take a look at this:

a = 345
print(type(a))
print(a)

b = "65"
print(type(b))
print(b)

c = True
print(type(c))
print(c)

d = 123.543
print(type(d))
print(d)

# 'int' to other types

ab = int("65")
print(type(ab))
print(ab)

ac = int(True)
print(type(ac))
print(ac)

ad = int(123.543)
print(type(ad))
print(ad)

# 'str' to other types

ba = str(345)
print(type(ba))
print(ba)

bc = str(True)
print(type(bc))
print(bc)

bd = str(123.543)
print(type(bd))
print(bd)

# 'float' to other types

ca = bool(345)
print(type(ca))
print(ca)

cb = bool("65")
print(type(cb))
print(cb)

cd = bool(123.543)
print(type(cd))
print(cd)

# float to other types

da = float(345)
print(type(da))
print(da)

db = float("65")
print(type(db))
print(db)

dc = float(True)
print(type(dc))
print(dc)

# I guess all the examples above contributed to having a deep level of understanding how each data set works

# more exmaples:

print(str(23) + str(32) + str(98))
print(int(True) + int(False) + int(2 * True))

# Code Challenge 2.1

# You are asked to write a piece of code that adds up two digits of a two digit number (digit sum fucntion somehow)
# The mathematical approach can be found here: https://en.wikipedia.org/wiki/Digit_sum

print("Two digit sum digit sum calculator\n by Mehrzad Barzegar")

two_digit_number = int(
    input("Please type a two digit number (From 10 to 99) "))
if 10 <= two_digit_number <= 99:
    stringed_tdn = str(two_digit_number)
    result = (int(stringed_tdn[0])) + (int(stringed_tdn[1]))
    print(result)
else:
    print("Invalid Input: Please type a two digit number")

# "I put it into an if function which prompts you to give a two digit number only
# The version below doesn't have this function."

print("Two digit sum digit sum calculator\n by Mehrzad Barzegar")

two_digit_number = input("Please type a two digit number (From 10 to 99) ")
result = (int(two_digit_number[0])) + (int(two_digit_number[1]))
print(result)

# Mathematical Operations


35 + 532
23 - 45
34 * 45
654 / 345
234 ** 23

# They come into an order, which needs to be followed when solving

# '"PEMDAS
# It stands for:
# Paranthesis ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -"

# A quick demo to test the order of functions

print(2 * 4 / 15 - 12 + 5)
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

# Code Challenge 2.2
# This challenge requires you to make a BMI Calculator

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = ((weight)/(height ** 2))
print(int(bmi))

if bmi >= 30:
    print("Obese: Consult your physician immediately.")
elif 25 <= bmi < 30:
    print("Overwight: Consider going on a diet under supervision.")
elif 18.5 <= bmi < 25:
    print("Normal weight: Your body is in shape.")
else:
    print("Underwight: Consider visiting a nutrientist.")

# This part contains Number Manipulation and F strings

# Now we are learning how to round numbers with round()

single_slash = (round(8 / 3, 2))
print(type(single_slash))
print(single_slash)

# We can use floor division (part of floor and ceiling function)

double_slash = (8 // 5)
print(type(double_slash))
print(double_slash)

# "So, you might ask what's the point of using one over another?
# The answer is that you can continue manipulating values in different scenarios
# when dealing with the code."

result = 4 / 2
result /= 2
print(result)

# Basically these signs ( += *= -= /=) means that the follwing value will be applied to that variable
# Take a loot at these examples

score = 0
score += 1
score += 1
score += 1
print(score)


# Using single slash turns your result into float versus using double slash turns it in to interger
