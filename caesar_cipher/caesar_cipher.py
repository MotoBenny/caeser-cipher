
abc = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(message, shift):
    encrypted = ""

    if shift < 0:
        shift = shift % 26
    for char in message:
        if not char.isalpha():
            encrypted += char
        else:
            index = abc.find(char.lower())
            index += shift
            if index >= len(abc):
                index -= len(abc)
            elif index < 0:
                index += len(abc)
            if char.isupper():
                letter = abc[index]
                encrypted += letter.upper()
            if char.islower():
                encrypted += abc[index]

    return encrypted


def decrypt(encrypted, shift):
    return encrypt(encrypted, -shift)


def crack(encrypted):
    pass
