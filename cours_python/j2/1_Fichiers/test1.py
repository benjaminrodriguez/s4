f = open('data.txt','r')
g = open('output.txt','w')
while True:
    line = f.readline()
    if line == '':
        break
    space = line.index(' ')
    a, b = line[:space], line[space+1:]
    c = float(a)+float(b)
    g.write(str(c)+'\n')
