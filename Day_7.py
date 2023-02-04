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

import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

########################################################


word_list = ["ardvark", "baboon", "camel"]

# We randomly choose a word from the list

chosen_word = word_list[random.randint(0, len(word_list) - 1)]
print(chosen_word)

guess_letter = (str(input("Guess a letter: "))).lower()


chosenword_letters = []

for each_letter in chosen_word:
    chosenword_letters.append(each_letter)


for checkletter in chosenword_letters:
    if checkletter == guess_letter:
        print("True")
    else:
        print("False")

emptyspaces = []

for dash in chosen_word:
    emptyspaces.append("_")

lives = 6

"*************************"
while not lives != 0:

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess_letter}")
        if letter == guess_letter:
            emptyspaces[position] = letter
        elif letter != guess_letter:
            lives -= 1
    print(emptyspaces)
guess_letter = (str(input("Guess a letter: "))).lower()

print("You lose")
