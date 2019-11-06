#!/usr/bin/env python3

import logging

from squareroot import squareroot

logging.basicConfig(
    format='%(filename)s:%(funcName)s[%(levelname)s]:%(message)s',
    level=logging.INFO
)

def func1(x: int):
    logging.info('Need more power !')
    return x**2

logging.info('starting')
power = func1(4)
root = squareroot.calculate_square_root(power)
print('La racine de {:d} est {:f}'.format(power, root))
logging.info('exiting')
