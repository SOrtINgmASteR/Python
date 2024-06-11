# Hangman - 02

import random
import hangman

word_list = ["murderer", "executioner", "butcher", "slaughterer", "massacre", "assassin", "killer"]
chosen_word = random.choice(word_list)
guess_word = []

print(chosen_word)

for i in range(len(chosen_word)):
    guess_word += '_'

guess_letter = input("Guess a letter : ")
guess_letter = guess_letter.lower()

for i in range(len(chosen_word)):
    if chosen_word[i] == guess_letter:
        guess_word[i] = str(guess_letter)

for i in range(len(guess_word)):
    print(guess_word[i], end="")




