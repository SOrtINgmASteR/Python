<h2 style="text-align:center">DAY - 4</h2>  

<h3 style="text-align:center;">Lesson 13 - Heads or Tails</h3>  

```python
import random
heads_or_tail = random.randint(0, 1)
if heads_or_tail == 1:
    print("Heads")
elif heads_or_tail == 0:
    print("Tails")
```  
<h3 style="text-align:center;">Lesson 14 - Banker Roulette</h3>  

```python
import random
names = input().split(", ")
length = int(len(names))
index = random.randint(0, length - 1)
print(f"{names[index]} is going to buy the meal today!")
```
<h3 style="text-align:center;">Lesson 15 - Treasure Map</h3>  

```python
list1 = ["⬜️", "️⬜️", "️⬜️"]
list2 = ["⬜️", "⬜️", "️⬜️"]
list3 = ["⬜️️", "⬜️️", "⬜️️"]
treasure_map = [list1, list2, list3]
position = str(input())
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
```
<h3 style="text-align:center;">Rock Paper Scissor</h3>  

**rock_paper_scissor** module  
```python
show_rock = str("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


show_paper = str("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")


show_scissor = str("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
```  
**Main Code**  
```python
import random
import rock_paper_scissor
your_choice = int(input("Enter 1 - for ROCK, 2 - for PAPER, 3 - for SCISSOR : "))
computer_choice = int(random.randint(1, 3))

print("You Choose : ")
if your_choice == 1:
    print(rock_paper_scissor.show_rock)
elif your_choice == 2:
    print(rock_paper_scissor.show_paper)
elif your_choice == 3:
    print(rock_paper_scissor.show_scissor)
print("Computer Chose : ")
if computer_choice == 1:
    print(rock_paper_scissor.show_rock)
elif computer_choice == 2:
    print(rock_paper_scissor.show_paper)
elif computer_choice == 3:
    print(rock_paper_scissor.show_scissor)

if computer_choice == your_choice:
    print("It's a Draw!!! ಠ_ಠ")
elif (computer_choice == 1 and your_choice == 2) or (computer_choice == 2 and your_choice == 3) or (computer_choice == 3 and your_choice == 1):
    print("YOU WIN!!! (◉‿◉)")
else:
    print("YOU LOOSE!!! (︶︹︶)")
```

