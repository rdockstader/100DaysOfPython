def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

right_count = 0

while not at_goal():
    if right_is_clear():
        if right_count < 10:
            turn_right()
            move()
        else:
            turn_left()
            right_count = 0
        right_count += 1
    elif front_is_clear():
        move()
        right_count = 0
    else:
        turn_left()
        right_count = 0