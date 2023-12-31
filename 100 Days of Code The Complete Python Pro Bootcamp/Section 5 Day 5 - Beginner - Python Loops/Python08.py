# Password Generator - Hard Version
import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
number_of_letters = int(input("How many letters : "))
number_of_numbers = int(input("How many number : "))
number_of_symbols = int(input("How many symbols : "))

for char in range(0, number_of_letters):
    random_char = random.choice(letters)
    password += random_char
    # print(f"{random_char}", end="")
for number in range(0, number_of_numbers):
    random_num = random.choice(numbers)
    password += str(random_num)
    # print(f"{random_num}", end="")
for symbol in range(0, number_of_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol
    # print(f"{random_symbol}", end="")
random.shuffle(password)

print(f"\nPassword = ", end="")
for i in range(0, len(password)):
    print(f"{password[i]}", end="")
