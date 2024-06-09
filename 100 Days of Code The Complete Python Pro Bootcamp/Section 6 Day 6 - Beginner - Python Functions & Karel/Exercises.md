<h2 style="text-align:center">DAY - 6</h2>  

<h3 style="text-align:center;">Reborg's World - 1</h3>  

```
# Reborgs World
def turn_right():
    turn_left()
    turn_left()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
```

<h3 style="text-align:center;">Reborg's World - Hurdle 1</h3>  

```
# Hurdle - 1
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

for i in range(0, 6):
    move()
    go_up()
    go_down()
```

<h3 style="text-align:center;">Reborg's World - Hurdle 2</h3>  

```
# Hurdle - 2
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

while at_goal() == False:
    move()
    go_up()
    go_down()
```

<h3 style="text-align:center;">Reborg's World - Hurdle 3</h3>  

```
# Hurdle - 3
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

while at_goal() == False:
    while front_is_clear() == True:
        move()
    if front_is_clear() == False:
        go_up()
        go_down()
```

<h3 style="text-align:center;">Reborg's World - Hurdle 4</h3>  

```
# Hurdle - 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def go_up():
    turn_left()
    while right_is_clear() == False:
        move()
    turn_right()
    move()
    
def go_down():
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while at_goal() == False:
    if front_is_clear() == True:
        move()
    elif front_is_clear() == False:
        go_up()
        go_down()
```