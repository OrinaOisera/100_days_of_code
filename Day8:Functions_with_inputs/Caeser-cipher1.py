alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type  'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    cipher_text = " "
    # shift each letter of the text forwards by the shift number
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f'The encoded text is {cipher_text}')


def decrypt(cipher_text, shift_amount):
    decipher_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new1_position = position - shift_amount
        mew1_letter = alphabet[new1_position]
        decipher_text += mew1_letter
    print(f'The decoded text is {decipher_text}')


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)

# encrypt(plain_text=text, shift_amount=shift)
# decrypt ('khoor', 3)
