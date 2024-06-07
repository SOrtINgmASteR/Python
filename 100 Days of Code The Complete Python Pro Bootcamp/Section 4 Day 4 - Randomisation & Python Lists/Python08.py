# Exercise - Treasure Map

list1 = ["⬜️", "️⬜️", "️⬜️"]
list2 = ["⬜️", "⬜️", "️⬜️"]
list3 = ["⬜️️", "⬜️️", "⬜️️"]
treasure_map = [list1, list2, list3]
position = str(input("Enter Position : "))
letter = position[0].upper()
number = int(position[1])
column = int(0)
row = int(0)
if letter == 'A':
    column = 0
elif letter == 'B':
    column = 1
elif letter == 'C':
    column = 2
row = number - 1
treasure_map[row][column] = 'X'
print("Hiding your treasure! X marks the spot.")
print(f"{list1}\n{list2}\n{list3}")
