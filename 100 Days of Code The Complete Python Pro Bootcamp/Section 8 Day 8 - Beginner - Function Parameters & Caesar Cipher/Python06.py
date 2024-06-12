# Caesar Cipher - Reorganizing 1

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(input_text, shift_amount, cipher_direction):
    output_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in input_text:
        letter_index = alphabet.index(letter)
        new_index = letter_index + shift_amount
        if new_index > 25:
            new_index -= 26
        elif new_index < 0:
            new_index += 26
        output_text += alphabet[new_index]
    return output_text


text = "uvwxyz"
shift = 5

encrypted_text = str(caesar_cipher(text, shift, "encode"))
print(encrypted_text)

decryption_text = str(caesar_cipher(encrypted_text, shift, "decode"))
print(decryption_text)
