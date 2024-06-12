# Caesar Cipher - Encryption & Decryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Caesar Cipher - Encryption
def encryption(plain_text, shift_amount):
    encryption_text = ""
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        new_index = letter_index + shift_amount
        if new_index > 25:
            new_index -= 26
        encryption_text += alphabet[new_index]
    return encryption_text


# Caesar Cipher - Decryption
def decryption(encryption_text, shift_amount):
    decryption_text: str = ""
    for letter in encryption_text:
        letter_index = alphabet.index(letter)
        new_index = letter_index - shift_amount
        if new_index < 0:
            new_index += 26
        decryption_text += alphabet[new_index]
    return decryption_text


text = "uvwxyz"
shift = 5

encrypted_text = str(encryption(text, shift))
print(encrypted_text)

decryption_text = str(decryption(encrypted_text, shift))
print(decryption_text)
