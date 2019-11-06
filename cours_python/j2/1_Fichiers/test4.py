#!/usr/bin/env python3
import sys

for line in sys.stdin:
    a,b = line.split()
    print(float(a)+float(b))
