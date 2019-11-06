import sys
numbers = [str(sum(map(float, line.split()))) for line in open(sys.argv[1])]
open(sys.argv[2],'w').write('\n'.join(numbers))
