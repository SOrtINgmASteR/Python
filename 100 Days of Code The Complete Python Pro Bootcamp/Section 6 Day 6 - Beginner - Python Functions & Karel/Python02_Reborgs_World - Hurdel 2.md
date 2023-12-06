**Hurdel - 2 Using While Loop-**  
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def go_up():
    turn_left()
    move()
    turn_right()
    move()
def go_down():
    turn_right()
    move()
    turn_left()
while at_goal() != True:
    move()
    go_up()
    go_down()
```