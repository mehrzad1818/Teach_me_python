# This is the 11th day of 100 days of coding
# Your very first capstone project
import random

# lists  to show
playing_consent = input(
    str("Do you want to play a game of Blackjack? Type 'y' or 'n': "))

if playing_consent == "y":

    def picker():

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        playercard = cards[random.randint(0, 12)]
        cpucard = cards[random.randint(0, 12)]
        playercard2 = cards[random.randint(0, 12)]
        cpucard2 = cards[random.randint(0, 12)]

        playercardlist = []

        playercardlist.append(playercard)
        playercardlist.append(playercard2)

        print(
            f"The player's cards are {playercardlist}. The total is {playercard + playercard2}.")

        cpucardlist = []

        cpucardlist.append(cpucard)
        cpucardlist.append(cpucard2)

        print(
            f"The dealer's cards are {cpucardlist}. The total is {cpucard + cpucard2}.")


picker()
