##########################################################################################################################
###  BLACKJACK PROJECT  ###

............................................................................................
../my_solution.py

import random
from random import choice
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Game starter
game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

# Main Blackjack function
def blackjack():

    # Whole game start
    game_continue = True
    while game_continue:
        print(logo)

        # Data  for game
        user_cards = []
        user_score = 0
        computer_cards = []
        computer_score = 0

        # First initial round
        is_round_continue = True

        for i in range(2):
            user_cards.append(random.choice(cards))
            user_score += user_cards[i]
            # Changing Ace from 11 to 1 if it goes beyond 21 total
            if user_cards[len(user_cards) - 1] == 11 and user_score > 21:
                user_score -= 10
            if i < 1:
                computer_cards.append(random.choice(cards))
                computer_score += computer_cards[i]

        # Print first results
        print(f"Your cards: {user_cards}, current score: {user_score} ")
        print(f"Computer's first card: {computer_cards[0]}")


        # User gets cards
        user_gets_cards = True
        while user_gets_cards:
            get_more_cards = input("Type 'y' to get another card, type 'n' to pass: ")
            if  get_more_cards.lower() == 'y':
                user_cards.append(random.choice(cards))
                user_score += user_cards[len(user_cards) - 1]
                # Changing Ace from 11 to 1 if it goes beyond 21 total
                if user_cards[len(user_cards) - 1] == 11 and user_score > 21:
                    user_score -= 10
                print(f"\nYour cards: {user_cards}, current score: {user_score} ")
                print(f"Computer's first card: {computer_cards[0]}")

                # User Result: Lose, went over
                if user_score > 21:
                    print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
                    print("❌You went over. You lose❌")
                    user_gets_cards = False
                    is_round_continue = False

            else:
                user_gets_cards = False


        # User Result: Win, Blackjack
        if user_score == 21:
            print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
            print("🏆Win with a Blackjack🏆")
            user_gets_cards = False
            is_round_continue = False




        # Computer gets cards
        while is_round_continue and computer_score <= user_score and computer_score <= 21:
            computer_cards.append(random.choice(cards))
            computer_score += computer_cards[len(computer_cards) - 1]
            # Changing Ace from 11 to 1 if it goes beyond 21 total
            if computer_cards[len(computer_cards) - 1] == 11 and computer_score > 21:
                computer_score -= 10


        # Computer Results
        # Result: Win, Blackjack
        if is_round_continue:
            if computer_score == 21:
                print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
                print("❌❌❌Lose, opponent has Blackjack❌❌❌")

            # Result: Lose, went over
            elif computer_score > 21:
                print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
                print("✅Opponent went over. You win✅")

            # Result: Win
            elif computer_score > user_score:
                print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
                print("❌You lose❌")

            # Result: Lose
            elif computer_score > user_score:
                print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
                print("✅You win✅")

            # Result: Draw
            else:
                print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
                print("🟰Draw🟰")


        # Ask user to continue the game or not
        try_game_again = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
        if try_game_again.lower() == 'y':
            print("\n" * 20)
        else:
            game_continue = False


if game_start.lower() == 'y':
    blackjack()







............................................................................................
../teacher_solution.py

import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()






............................................................................................
../art.py

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


[end]
