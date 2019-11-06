#!/usr/bin/env python3
from argparse import ArgumentParser

parser = ArgumentParser(description='SuperOutil !')
parser.add_argument('entiers', metavar='N', type=int, nargs='+', help='mettre en réserve')
parser.add_argument('--sum', dest='traiter', action='store_const', const=sum, default=max, help='additionne les entiers au lieu du max')
args = parser.parse_args()

print(args.traiter(args.entiers))

