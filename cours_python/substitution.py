#!/usr/bin/env python3

import string
import random

message_dechiffre = "Bonjour tout le monde, comment tu vas"

lettre = string.ascii_uppercase
random.shuffle(lettre)
key = print(''.join(lettre))

def chiffre_substitution(key: str, msg: str) -> str:
    i = 0
    j = 1 
    for i in str(lettre):
        lettre[i] = message_chiffre[j]
        j+=1
        i+=1
    pass
print(message_dechiffre)