**Hurdel - 4 Using While Loop-**
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def go_up():
    turn_left()
    while right_is_clear() != True:
        move()
    turn_right()
    move()
def go_down():
    turn_right()
    move()
    while front_is_clear() == True:
        move()
    turn_left()
while at_goal() != True:
    if front_is_clear() == True:
        move()
    else:
        go_up()
        go_down()
```