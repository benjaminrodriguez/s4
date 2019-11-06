import sys

numbers = []
for line in open(sys.argv[1]):
    a, b = line.split()
    numbers.append(str(float(a) + float(b)))
open(sys.argv[2],'w').write('\n'.join(numbers))
