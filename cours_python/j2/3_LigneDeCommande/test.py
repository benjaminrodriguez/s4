#!/usr/bin/env python3
import argparse


parser = argparse.ArgumentParser(description="Super outil")
parser.add_argument("--machine", "-m", help="Nom de la machine")
parser.add_argument("--port", "-p", help="Port de la machine")
parser.add_argument("action", help="Scan|Connect")
args = parser.parse_args()


print("Je scan l'ip: {}".format(args.machine))

