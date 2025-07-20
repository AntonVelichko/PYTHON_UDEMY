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
../teacher_solution.py








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

