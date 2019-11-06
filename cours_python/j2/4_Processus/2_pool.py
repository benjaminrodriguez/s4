from multiprocessing import Pool
import sys

def adder(t):
    return str(t[0]+t[1])

def reader(source=sys.argv[1]):
    for line in open(source):
        a,b = line.split()
        yield (float(a), float(b))

#print(reader())

with Pool(5) as p:
    numbers = p.map(adder, reader())

#print(numbers)
