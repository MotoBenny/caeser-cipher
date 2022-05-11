import re
from caesar_cipher.corpus_loader import word_list, name_list


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

    key = 0
    percentage = 0
    for letter in abc:
        real_words = 0
        key += 1
        message = decrypt(encrypted, key)
        verified_message = message.split(' ')

        for word in verified_message:
            word = re.sub(r'[^A-Za-z]+', '', word)
            if word.lower() in word_list or word in name_list:
                real_words += 1
            else:
                pass
        percentage = int(real_words // len(verified_message) * 100)
        if percentage >= 50:
            return message
    if percentage < 50:
        return ""