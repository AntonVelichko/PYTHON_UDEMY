
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

