# Exercise - Treasure Map
list1 = ["🔲", "🔲", "🔲"]
list2 = ["🔲", "🔲", "🔲"]
list3 = ["🔲", "🔲", "🔲"]
map = [list1, list2, list3]
position = input("Enter Position in the map : ")
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
map[row][column] = 'X'

print(f"{list1}\n{list2}\n{list3}")
