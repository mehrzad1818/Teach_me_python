
# This is alphabet

def split(alphabet):
    return list(alphabet)


alphabet = (split('abcdefghijklmnopqrstuvwxyz'))
print(alphabet)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    ciphered_text = []
    for letter in text:
        ciphered_text.append(alphabet[alphabet.index(letter) + shift])
    print(ciphered_text)


encrypt(text, shift)
