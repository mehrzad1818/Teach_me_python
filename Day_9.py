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

programming_dictionary["Parameter"] = "The values inside the actual implementation of the function."

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
# We can easily edit things in our dictionary.

programming_dictionary["Bug"] = "It's a very bad thing, you should avoid it."
print(programming_dictionary)


# This is how we 'loop through' a dictionary:

for key in programming_dictionary:
    print(key)

# The code above just gives us the keys and not the values
# We can have both with the code below:

for keysnvalues in programming_dictionary:
    print(keysnvalues)
    print(programming_dictionary[keysnvalues])


# This is Day 9.1 Grading Program Exercise - Our first code challenge of the day.

# "So, here's the rubric:

# from 91 to 100 -- outstanding
# from 81 to 90 -- exceeds expectation
# from 71 to 80 -- acceptable
# from 70 below -- fail


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,

}

student_grades = {}


for students in student_scores:
    grades = student_scores[students]
    if grades <= 70:
        student_grades[students] = "Fail"
    if 71 <= grades <= 80:
        student_grades[students] = "Acceptable"
    if 81 <= grades <= 90:
        student_grades[students] = "Exceeds Expectations"
    if 91 <= grades <= 100:
        student_grades[students] = "Outstanding"


print(student_grades)


# The new concept is called 'Nesting':
# If we think about a dictionaries as a list of things; in nesting, we can put a dictionary inside another dictionary.
# That's basically nesting.

# {
#     key1: [mylist]
#     key2: {mydic}
# }

# In the example above, we have a list and a dictionary nested inside another dictionary.

# Some examples are down below:

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Poland": "Warsaw",
    "Finland": "Helsinki",

}

travel_log = [

    {
        "country": "France",

        "cities_visited": ["Paris", "Lille", "Dijon"],
        "number_of_visits": 4,
        "overalltripscore": [67, 80, 75, 100]
    },
    {
        "country": "Germany",

        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "number_of_visits": 2,
        "overalltripscore": [50, 35]
    },
]

#  In the example above,
# We have a key above in the travel log dic which is france,
# but as value for the key we don't have a string, but a list,
# which has its own values.


# This is Day 2 Dictionary List Exercise

travel_log = [

    {
        "country": "France",

        "cities_visited": ["Paris", "Lille", "Dijon"],
        "number_of_visits": 4,
        "overalltripscore": [67, 80, 75, 100]
    },
    {
        "country": "Germany",

        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "number_of_visits": 2,
        "overalltripscore": [50, 35]
    },
]


def add_new_country(destination, visits, viscity):
    travel_logger = {"country": [destination],
                     "cities_visited": [viscity],
                     "number_of_visits": [visits]}
    travel_log.append(travel_logger)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg", "Dontesk"])
print(travel_log)

