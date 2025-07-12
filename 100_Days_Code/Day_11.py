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


        # Round starts
        # is_round_continue = True
        # while is_round_continue:

        # First initial round
        is_round_continue = True

        for i in range(2):
            user_cards.append(random.choice(cards))
            user_score += user_cards[i]
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
                print(f"\nYour cards: {user_cards}, current score: {user_score} ")
                print(f"Computer's first card: {computer_cards[0]}")

                # Result: Win, Blackjack
                if user_score == 21:
                    print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
                    print("🏆Win with a Blackjack🏆")
                    user_gets_cards = False
                    is_round_continue = False

                # Result: Lose, went over
                if user_score > 21:
                    print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
                    print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")
                    print("❌You went over. You lose❌")
                    user_gets_cards = False
                    is_round_continue = False
            else:
                user_gets_cards = False

        # if is_round_continue == False:
        #     break
        print(f"is_round_continue = {is_round_continue}")

        # Computer gets cards
        while is_round_continue and computer_score <= user_score and computer_score <= 21:
            computer_cards.append(random.choice(cards))
            computer_score += computer_cards[len(computer_cards) - 1]

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



            # print(f"\nYour final hand: {user_cards}, final score: {user_score} ")
            # print(f"Computer's final hand: {computer_cards}, final score: {computer_score} ")



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





--------------------------------------------------------------------------------------------



[end]
