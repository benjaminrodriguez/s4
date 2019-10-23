#!/usr/bin/env python3

import random
import string

def chiffre_substitution(key: str, msg: str) -> str:
    crypt_msg = ''
    msg = msg.upper()
    for letter in msg:
        if letter.isalpha():
            pos = ord(letter) - ord('A')
            crypt_msg += key[pos]
        else:
            crypt_msg += letter
    return crypt_msg

def dechiffre_substitutioin(key: str, msg: str) -> str:
    cleartext = ''
    msg = msg.upper()
    for letter in msg:
        if letter.isalpha():
            pos = key.index(letter)
            cleartext += chr(pos + ord('A'))
        else:
            cleartext += letter
    return cleartext


# Generate 'unique' key:
alphabet = [l for l in string.ascii_uppercase]
random.shuffle(alphabet)
key = ''.join(alphabet)


msg_clair = "Coucou tout le monde"
msg_chiffre = chiffre_substitution(key, msg_clair)
print(msg_chiffre)
msg_clair = dechiffre_substitutioin(key, msg_chiffre)
print(msg_clair)
