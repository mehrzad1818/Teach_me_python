# "This is Day 9 of 100 days of code, we will learn about dictionaries and nesting in programming."

# "so, dictionaries in python are just like dictionaries in real life with some key differences."

# Key -- Value
# Bug -- An error in a program that prevents the program from running as expected.

# " In python, the dictionary would look like this:"

key = "bug"
value = "An error in a program that prevents the program from running as expected"

mydic = {key: value}
print(mydic)

# This is the starting point:

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",

}

# The code below shows an example of retriving a piece of data from a dictionary

print(programming_dictionary["Bug"])


# Here's how we add items to the dictionary

programming_dictionary["Parameter"] = "The values inside the actual implementation of the function."]

print(programming_dictionary)


# We often start with empty dictionary, just like empty lists, strings ...
# Empty dictionaries are created with a set of empty curly braces
empty_list = []
empty_dictionary = {}

# This concept can be used for wiping a dictionary! Take a look here:
# This dictionary which had several entries, but after this argument, it's wiped out.

programming_dictionary = {}
print(programming_dictionary)

# The concept of tapping into a dictionary goes beyond just adding
# We can easily add many things to our dictionary

programming_dictionary["Bug"] = "It's a very bad thing, you should avoid it."
