# Hangman - 01

import random
import hangman

word_list = ["murderer", "executioner", "butcher", "slaughterer", "massacre", "assassin", "killer"]
chosen_word = random.choice(word_list)

guess_letter = input("Guess a letter : ")
guess_letter = guess_letter.lower()

for i in range(len(chosen_word)):
    if chosen_word[i] == guess_letter:
        print("Right!")
    else:
        print("Wrong")


