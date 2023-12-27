# Exercise - Rock, Paper, Scissor game
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
