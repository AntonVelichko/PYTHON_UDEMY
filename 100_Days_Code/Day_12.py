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
../teacher_solution.py








............................................................................................
../art.py








[end]
