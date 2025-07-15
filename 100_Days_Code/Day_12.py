##########################################################################################################################
###  exercise Prime Number  ###

............................................................................................
../my_solution.py
import math

def is_prime(num):
    for i in range(1, math.floor(num ** 0.5)):
        if num % (i+1) == 0:
            return False
    return True

'''
🛑 Problem in Your Code
❌ You start your loop at i = 1 and check num % (i+1)
This means:
- You start dividing by 2, 3, 4, ... — but you never check 1, and you never skip it either.
- Also, you check num % 1 == 0 for every number, which is always true, so it wrongly returns False for every input.
'''



............................................................................................
../AI_solution.py
  
import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2):  # Only odd numbers
        if num % i == 0:
            return False
    return True








##########################################################################################################################
###  GUESS THE NAME PROJECT  ###

............................................................................................
../my_solution.py

import random
from art import logo


def random_number():
    number = random.randint(1, 100)
    return number


def game():

    # Initial game start print
    while True:
        print(logo)
        print("Welcome to the Number Guessing Game!\n"
              "I'm thinking of a number between 1 and 100.")


        # Guessing number is created
        user_number = ""
        hidden_number = random_number()
        print(f"Number to guess = {hidden_number}")


        # Difficulty level
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        attempts = 0
        if difficulty == "hard":
            attempts = 5
        else:
            attempts = 10


        # Guessing loop
        while hidden_number != user_number and attempts > 0:
            print(f"\nYou have {attempts} attempts remaining to guess the number.")
            emoji_up = "⬆️"
            emoji_down = "⬇️"

            user_number = int(input("Make a guess: "))

            # Conditions
            if user_number - hidden_number > 0:
                if abs(user_number - hidden_number) > 50:
                    print(f"{emoji_up}Super high")
                elif abs(user_number - hidden_number) > 25:
                    print(f"{emoji_up}Very high")
                elif abs(user_number - hidden_number) > 12:
                    print(f"{emoji_up}Too high")
                elif abs(user_number - hidden_number) > 6:
                    print(f"{emoji_up}A bit high")
                else:
                    print(f"{emoji_up}High, but very close")
            else:
                if user_number - hidden_number < 0:
                    if abs(user_number - hidden_number) > 50:
                        print(f"{emoji_down}Super low")
                    elif abs(user_number - hidden_number) > 25:
                        print(f"{emoji_down}Very low")
                    elif abs(user_number - hidden_number) > 12:
                        print(f"{emoji_down}Too low")
                    elif abs(user_number - hidden_number) > 6:
                        print(f"{emoji_down}A bit low")
                    else:
                        print(f"{emoji_down}Low, but very close")
            attempts -= 1


        if hidden_number == user_number:
            print(f"\n✅You got it! The answer was {hidden_number}.")
        else:
            print(f"\n❌You've run out of guesses! The answer was {hidden_number}.")


        # Ask to play again
        again = input("\nDo you want to play 'Guess the Number' again? Type 'y' or 'n': ").lower()
        if again != 'y':
            break
        print("\n" * 20)


game()





............................................................................................
../my_solution_UPDATED.py

import random
from art import logo


EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def random_number():
    number = random.randint(1, 100)
    return number


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return EASY_LEVEL_ATTEMPTS


def check_answer(u_guess, h_number):
    emoji_up = "⬆️"
    emoji_down = "⬇️"

    # Number is high
    if u_guess - h_number > 0:
        if abs(u_guess - h_number) > 50:
            print(f"{emoji_up}Super high")
        elif abs(u_guess - h_number) > 25:
            print(f"{emoji_up}Very high")
        elif abs(u_guess - h_number) > 12:
            print(f"{emoji_up}Too high")
        elif abs(u_guess - h_number) > 6:
            print(f"{emoji_up}A bit high")
        else:
            print(f"{emoji_up}High, but very close")

    # Number is low
    elif u_guess - h_number < 0:
            if abs(u_guess - h_number) > 50:
                print(f"{emoji_down}Super low")
            elif abs(u_guess - h_number) > 25:
                print(f"{emoji_down}Very low")
            elif abs(u_guess - h_number) > 12:
                print(f"{emoji_down}Too low")
            elif abs(u_guess - h_number) > 6:
                print(f"{emoji_down}A bit low")
            else:
                print(f"{emoji_down}Low, but very close")

    # Right number
    else:
        print(f"\n✅You got it! The answer was {h_number}.")


def game():
    # Initial game start print
    while True:
        print(logo)
        print("Welcome to the Number Guessing Game!\n"
              "I'm thinking of a number between 1 and 100.")

        # Guessing number is created
        hidden_number = random_number()
        print(f"Number to guess = {hidden_number}")

        # Guessing loop
        user_guess = 0
        attempts = set_difficulty()
        while hidden_number != user_guess and attempts > 0:
            print(f"\nYou have {attempts} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
            check_answer(user_guess, hidden_number)
            attempts -= 1
            if attempts == 0:
                print(f"\n❌You've run out of guesses! The answer was {hidden_number}.")

        # Ask to play again
        again = input("\nDo you want to play 'Guess the Number' again? Type 'y' or 'n': ").lower()
        if again != 'y':
            break
        print("\n" * 20)


game()





............................................................................................
../teacher_solution.py

from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()







............................................................................................
../art.py

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""






[end]
