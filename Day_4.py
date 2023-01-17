# "This is Day 4,
# We are going to learn about Randomisation and Python Lists.
# This section deals with new, challenging codes."

# Random function import

import random
a = random.randint(100, 1000)
print(a)

# Modules
# "Modules are made just like another file. For example, even this code that we are writing inside the file "Day_4.py" can be a module."
# You say how? Let me show you."

# "Imagine this is the module we've written on a separate file.
#
# pi = 3.14159265
#
# This is just the file.
#
# Here's our code in a separate file. We've saved its name as 'mymodule'.

# "import mymodule
#
# print(mymodule.pi)
#
# It would print: 3.141592"
# "

b = random.random()
print(b)


random_int = random.randint(0, 5)
random_flo = random.random()

print((str(random_int) + str(random_flo)))

# Random float gives you a float between 0.000000000....1 to 0.99999999999....

random_flo5 = random_flo * 5
print(random_flo5)

# One usage is that we can optimize our random love score calculator

random_love = random.randint(1, 100)
print(f"Your love score is {random_love}.")

# This is a code challenge, code challenge 4.1

# since the code editor will omit the imported module since it has already been imported, I'll comment it out.

# import random

random_digit = random.randint(1, 1000)
remainder = random_digit % 2
if remainder == 0:
    print("Tails")
else:
    print("Heads")

# A more efficient way is this:

random_side = random.randint(0, 1)
if random_side == 0:
    print("Tails")
else:
    print("Heads")