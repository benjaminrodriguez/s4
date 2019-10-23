#!/usr/bin/env python3

nb = 2 ** 1000

somme = 0

for elem in str(nb):
    somme += int(elem)

print(somme)


## Ou en une ligne

sum([int(x) for x in str(2**1000)])
