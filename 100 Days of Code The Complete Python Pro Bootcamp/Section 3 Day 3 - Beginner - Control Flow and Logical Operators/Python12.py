# Treasure Island
print("WELCOME TO THE TREASURE ISLAND!")
left_or_right = str(input("Where do you want to go? left or right : "))
if left_or_right == "left":
    swim_or_wait = str(input("There is a river ahead of you! Do you want to swim or wait : "))
    if swim_or_wait == "wait":
        red_or_blue = str(input("Found two doors! Which door you want to go in? red or blue or yellow: "))
        if red_or_blue == "blue":
            print("Eaten by beasts!!!")
            print("Game Over")
        elif red_or_blue == "red":
            print("Burned by fire!!!")
            print("Game Over!")
        elif red_or_blue == "yellow":
            print("You Win!!!")
    else:
        print("Attacked by trout!!!")
        print("Game Over!")
else:
    print("Fall in to a hole!!!")
    print("Game Over!")