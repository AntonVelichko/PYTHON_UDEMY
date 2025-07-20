##########################################################################################################################
###  HIGHER LOWER PROJECT  ###

............................................................................................
../my_solution.py

import random
from art import logo, vs
from game_data import data


# Functions to choose competetors
def competetor():
    return random.choice(data)

    
# Start of the game
def game():
    while True:
        
        # Data
        draw = False
        score = 0
        right_choice = f"You're right! Current score: {score}."
        account_a = competetor()
        account_b = competetor()

        while True:

            # Print logo
            print("\n" * 10)
            print(logo)

            if draw:
                print(f"Draw! Current score: {score}.")
                draw = False
            elif score > 0:
                print(f"You're right! Current score: {score}.")

            # Give options
            print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
            print(vs)
            print(f"Compare B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")
            user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            print("\n" * 10)

            # Compare scores
            if account_a['follower_count'] > account_b['follower_count'] and user_guess == 'a':
                score += 1
                account_b = competetor()          # change "comp_b", keep "comp_a"
            elif account_a['follower_count'] < account_b['follower_count'] and user_guess == 'b':
                score += 1
                account_a = account_b                # switch "comp_b" to "comp_a"
                account_b = competetor()          # change "comp_b", keep "comp_a"
            elif account_a['follower_count'] == account_b['follower_count']:
                account_b = competetor()  # change "comp_b", keep "comp_a"
                draw = True
            else:
                print(logo)
                print(f"Sorry, that's wrong. Final score: {score}")
                break


        play_again = input("Would like to play again? 'Y' or 'N': ").lower()
        if play_again != "y":
            break
        print("\n" * 10)

game()



# number = competetor()
# print(number)
# a = f"Compare A: {number['name']}, a {number['description']}, from {number['country']}."
# print(a)
# print(list(data[0]))

# Functions to choose competetors (other option)
# def competetor():
#     return random.randint(0, len(data)-1)
# a = f"Compare A: {data[number]['name']}, a {data[number]['description']}, from {data[number]['country']}."
# print(a)

#
# if a == b:
#     print(True)
# else:
#     print(False)








............................................................................................
../my_solutionUPDATED.py

import random
from art import logo, vs
from game_data import data


# Functions to choose competetors
def get_account():
    return random.choice(data)


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers == b_followers:
        return "draw"
    return "a" if a_followers > b_followers else "b"


def get_next_accounts(winner_account):
    """Sets up the next round with the previous winner as Account A."""
    return winner_account, get_account()



# Start of the game
def game():
    while True:

        # Data
        score = 0
        account_a = get_account()
        account_b = get_account()
        print(logo)

        while True:

            # Check if accounts are different
            while account_a == account_b:
                account_b = get_account()

            # Give options
            print(f"Compare A: {format_data(account_a)}.")
            print(vs)
            print(f"Compare B: {format_data(account_b)}.")

            # Ask user for a guess. User input validation
            while True:
                user_guess = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
                if user_guess not in ['a', 'b']:
                    print("Please type 'A' or 'B'.")
                    continue    # Go back to top and ask again
                break

            # Clear the screen
            print("\n" * 20)
            print(logo)

            # Get follower count of each account
            a_follower_count = account_a["follower_count"]
            b_follower_count = account_b["follower_count"]

            # Check if user is correct.
            result = check_answer(user_guess, a_follower_count, b_follower_count)

            # Give user feedback on their guess
            if result == "draw":
                print("It's a draw! Let's shuffle and continue.")
            elif result == user_guess:
                score += 1
                print(f"You're right! Current score {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                break

            if result in ["draw", user_guess]:
                account_a, account_b = get_next_accounts(account_b)


        play_again = input("Would like to play again? 'Y' or 'N': ").lower()
        if play_again != "y":
            break
        print("\n" * 20)


# Only run the game if this script is executed directly
if __name__ == "__main__":
    game()

'''
Why do this?
When your script is imported as a module in another Python file, everything outside a function 
will run immediately—which is usually not what you want. By wrapping your main logic like this, you ensure:
game() only runs when this file is executed directly (not when it's imported elsewhere).
Other scripts can safely import your helper functions without starting the game.
'''








............................................................................................
../teacher_solution.py

# Display art
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)
score = 0
game_should_continue = True
# Generate a random account from the game data
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False









............................................................................................
../art.py

logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""






[end]

