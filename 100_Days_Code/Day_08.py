
##########################################################################################################################
###  exercise Love Calculator  ###

# my first solution
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
print(calculate_love_score('Demetron', "Paraphen"))


---


# my updated solution
def calculate_love_score(name1, name2):
    
    combined_name = name1 + name2
    
    word_true = "true"
    word_love = "love"   
    
    true_score = 0
    love_score = 0
    
    for i in combined_name.lower():
        if i in word_true:
            true_score += 1
        if i in word_love:
            love_score += 1
            
    return str(true_score) + str(love_score)
    
print(calculate_love_score('Demetron', "Paraphen"))


---


# by other user
def calculate_love_score(person, partner):
    true = sum([f"{person}{partner}".upper().count(letter) for letter in "TRUE"])
    love = sum([f"{person}{partner}".upper().count(letter) for letter in "LOVE"])
    print(f"{true}{love}")






##########################################################################################################################
###  PROJECT CAESAR CIPHER  ###

............................................................................................
../my_solution.py

# made code complicated with revirsing the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)





............................................................................................
../teacher_solution.py

import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

# if user input a sumbol that not exist in our alphabet
    for symbol in original_text:
        if symbol not in alphabet:
            output_text += symbol
        else:
            shifted_position = alphabet.index(symbol) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")





............................................................................................
../art.py

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""





..[end]
