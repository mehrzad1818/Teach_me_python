# This is the 11th day of 100 days of coding
# Your very first capstone project
import random
from replit import clear

blackjacklogo = """

  ____  _            _        _            _
 |  _ \| |          | |      | |          | |
 | |_) | | __ _  ___| | __   | | __ _  ___| | __
 |  _ <| |/ _` |/ __| |/ /   | |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   < |__| | (_| | (__|   <
 |____/|_|\__,_|\___|_|\_\____/ \__,_|\___|_|\_\


"""

# lists  to show
playing_consent = input(
    str("Do you want to play a game of Blackjack? Type 'y' or 'n': "))

if playing_consent == "y":

    print(blackjacklogo)

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

        print(
            f"The dealer's first card is {cpucardlist}.")

        second_consent = input(
            str("Type 'y' to get another card, type 'n' to pass: "))

        if second_consent == "y":
            playercard3 = cards[random.randint(0, 12)]
            cpucard3 = cards[random.randint(0, 12)]
            playercardlist.append(playercard3)
            cpucardlist.append(cpucard2)
            cpucardlist.append(cpucard3)
            print(
                f"The dealer's total card is {cpucard + cpucard2 + cpucard3}.")
            print(
                f"Your total card is {playercard + playercard2 + playercard3}.")
        elif second_consent == "n":
            print("I don't know what to do at this point.")
        if (playercard + playercard2) > 21:
            print("You've lost.")
        elif (playercard + playercard2) == 21:
            print("You've won.")
        elif ((playercard + playercard2 + playercard3) > 21 and (playercard + playercard2 + playercard3) > (cpucard + cpucard2 + cpucard3)):
            print("You've lost.")
        else:
            print("You won.")
    picker()

elif playing_consent == "n":

    print(blackjacklogo)

    print("""
    Do you got the gots to play?
    Or you need more time to grow it?
    """)


else:
    print(blackjacklogo)
    print("Restart the program and check your input.")


# This is the more refined version of the Blackjack


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def play_game():

    print(blackjacklogo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):

        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)

        return sum(cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack."
        elif user_score == 0:
            return "Win, you have Blackjack."
        elif user_score > 21:
            return "You went over. You lost."
        elif computer_score > 21:
            return "Opponent went over. You won."
        elif user_score > computer_score:
            return "You win."
        else:
            return "You lose."

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play one more match? Type 'y' or 'n'.") == "y":
    clear()
    play_game()
