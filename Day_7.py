# Hello and good morning - This is Day 7 challenge of one hundred days of python and it deals with concepts we covered through the week
# like; for and while loops, if/elif/else, strings, lists, range and modules

# " So, the first step in making a working hangman is to
#


# 1. Randomly choose a word from the given list
# to a variable called something like chosen words."

# "2. Ask the user to guess a letter and assign their answer
# to a variable called guess. Make guess lowercase."

# "3. Check if the letter the user guessed is one of the
# letters in the chosen_word"


########################################################

# First, we import packages

import random

# Below is our initial list

word_list = ["ardvark", "baboon", "camel"]

# We randomly choose a word from the list

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
print(chosen_word)

# We ask the user to input a letter and we make it lowercase.

guess_letter = (str(input("Guess a letter: "))).lower()
print(guess_letter)

# here we want to find out whether the guessed letter is among the chosen word's letters

chosenword_letters = []

for each_letter in chosen_word:
    chosenword_letters.append(each_letter)

print(chosenword_letters)

# Here we want to make a loop to check one value (guessed letter) in the list (each letter).

for checkletter in chosenword_letters:
    if checkletter == guess_letter:
        print("True")
    else:
        print("False")

###########################

emptyspaces = []

for dash in chosen_word:
    emptyspaces.append("_")

print(emptyspaces)


for revealletter in range():
    if guess_letter == checkletter:
        emptyspaces += guess_letter
    else:
        emptyspaces += "_"

print(emptyspaces)

"This part of the code needs to be revised"
