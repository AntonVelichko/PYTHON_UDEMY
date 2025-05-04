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
