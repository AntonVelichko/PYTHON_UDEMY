##########################################################################################################################
###  PROJECT HANGMAN  ###

............................................................................................
../my_solution.py

# importing data
import random
import hangman_words
from hangman_art import stages, logo

lives  = 6

# creating Guessed Word
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

# creating a placeholder for Guessed Word
placeholder = ""
word_length = len(chosen_word)
for _ in range(word_length):
    placeholder += "_"
print(placeholder)

# creating list placeholder for calculation
list_placeholder = list(placeholder)
print(list_placeholder)

# printing the logo
print(logo)

# starting the loop
while "_" in list_placeholder and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1

    if guess in list_placeholder:
        print(f"You've already guessed a '{guess}'")

    for i in range(word_length):
        if chosen_word[i] == guess:
            list_placeholder[i] = guess

    print(''.join(list_placeholder))
    print(list_placeholder)
    print(lives)
    print(stages[lives])


else:
    if lives == 0:
        print("You lose")
    else:
        print("You win")







............................................................................................
../teacher_solution.py

import random

from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
  




............................................................................................
../hangman_words.py

word_list = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
]




............................................................................................
../art.py

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''







..[end]
