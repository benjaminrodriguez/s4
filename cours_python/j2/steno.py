#!/usr/bin/env python3
from typing import List

IMG_PATH = "/home/user/python/secret_cat.bmp"

def get_lsb(octet: bytes) -> int:
    return octet & 0b1

def build_byte(lst_bits: List[int]) -> bytes:
    result = 0
    if len(lst_bits) != 8:
        print("Invalid argument")
        return bytes([0])
    # result = 1*2^0 + 0*2^1 + 1*2^2 + .... + 0*2^7
    for idx, val in enumerate(lst_bits):
        result += val * 2 ** idx
    return result

def find_hidden_bytes(payload: bytes) -> bytes:
    lst_bits = []
    result = b''
    for octet in payload:
        lsb = get_lsb(octet)
        lst_bits.append(lsb)
        if len(lst_bits) == 8:
            secret_byte = build_byte(lst_bits)
            result += bytes([secret_byte])
            lst_bits = []
    return result


def find_offset(raw_img: bytes) -> int:
    " Return first pixel of a BMP image "
    offset = raw_img[10:14] # See wikipedia doc https://fr.wikipedia.org/wiki/Windows_bitmap#Format_du_fichier
    return int.from_bytes(offset, byteorder="little")

# Question 3
#data = b'\x12\x94\xc8\xb5\xf2]\xb5@\xc9@.i\xa6\xed\xb50\x8f\\\x80nNK,x'
#find_hidden_bytes(data)

# Question 4
with open(IMG_PATH, "rb") as fd:
    raw_img = fd.read()
offset = find_offset(raw_img)
print("Offset: {}".format(offset))




