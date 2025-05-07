
##########################################################################################################################
###  DAY 6  ###


# https://reeborg.ca/reeborg.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_in_front() and not right_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
    else:
        turn_left()




def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
    else:
        turn_left()





##########################################################################################################################
###  DAY 7  ###

import random
import hangman_words
from hangman_art import stages, logo

lives  = 6

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

list_display = list(placeholder)
print(list_display)

# TODO-1: - Use a while loop to let the user guess again.

print(logo)

while "_" in list_display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1

    if guess in list_display:
        print(f"You've already guessed a '{guess}'")


    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for i in range(word_length):
        if chosen_word[i] == guess:
            list_display[i] = guess
        else:
            pass

    print(list_display)
    print(lives)

    print(stages[lives])



else:
    if lives == 0:
        print("You lose")
    else:
        print("You win")





##########################################################################################################################
###  DAY 8  ###


def calculate_love_score(name1, name2):
    true_check = "true"
    love_check = "love"   
    
    true_score = 0
    love_score = 0
    
    for i in range(0, len(name1)):
        if name1[i].lower() in true_check:
            true_score += 1
        if name1[i].lower() in love_check:
            love_score += 1
            
    for i in range(0, len(name2)):
        if name2[i].lower() in true_check:
            true_score += 1
        if name2[i].lower() in love_check:
            love_score += 1   
            
    return str(true_score) + str(love_score)
    

print(calculate_love_score("Angela Yu","Jack Bauer"))
print(calculate_love_score("Kanye West", "Kim Kardashian"))


---------------------------------------------------------------


def calculate_love_score(name1, name2):   
    combined_name = name1 + name2

    word_true = "TRUE"
    word_love = "LOVE"
    
    total_true = 0
    total_love = 0

    for letter in combined_name.upper():
        if letter in word_true:
            total_true +=1
        if letter in word_love:
            total_love +=1

    print(f"{total_true}{total_love}")
    

calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")




