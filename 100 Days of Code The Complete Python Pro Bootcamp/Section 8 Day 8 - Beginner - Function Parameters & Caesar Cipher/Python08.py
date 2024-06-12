# Caesar Cipher - Reorganizing 2

import caesar_cipher

print(caesar_cipher.caesar_cipher)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(input_text, shift_amount, cipher_direction):
    output_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        if letter.isdigit() or letter.isspace() or not letter.isalnum():
            output_text += letter
            continue
        letter_index = alphabet.index(letter)
        new_index = letter_index + shift_amount
        if new_index > 25:
            new_index -= 26
        elif new_index < 0:
            new_index += 26
        output_text += alphabet[new_index]
    return output_text


ongoing = True
while ongoing:

    text = str(input("Enter text : "))
    shift = int(input("Enter shift : "))
    direction = str(input("Do you want to \"encode\" or \"decode\"??"))

    if direction == "encode":
        encrypted_text = str(caesar_cipher(text, shift, "encode"))
        print(encrypted_text)
    elif direction == "decode":
        decryption_text = str(caesar_cipher(encrypted_text, shift, "decode"))
        print(decryption_text)

    print("Do you want to continue? Y-yes or N-no")
    go = str(input())
    if go == 'N':
        ongoing = False
