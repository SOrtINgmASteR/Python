# Hangman - 03

import random
import hangman


def print_man(life):
    if life == 6:
        print(hangman.life_six)
    elif life == 5:
        print(hangman.life_five)
    elif life == 4:
        print(hangman.life_four)
    elif life == 3:
        print(hangman.life_three)
    elif life == 2:
        print(hangman.life_two)
    elif life == 1:
        print(hangman.life_one)
    elif life == 0:
        print(hangman.life_zero)
        print("Man is HANGED!!!")


word_list = ["murderer", "executioner", "butcher", "slaughterer", "massacre", "assassin", "killer"]
chosen_word = random.choice(word_list)
guess_word = []
life_remaining = int(7)

print(chosen_word)

for i in range(len(chosen_word)):
    guess_word += '_'

guess_letter = input("Guess a letter : ")
guess_letter = guess_letter.lower()
match_letter = False

for i in range(len(chosen_word)):
    if chosen_word[i] == guess_letter:
        guess_word[i] = str(guess_letter)
        match_letter = True

for i in range(len(guess_word)):
    print(guess_word[i], end="")
print()

if not match_letter:
    life_remaining -= 1
    print_man(life_remaining)
