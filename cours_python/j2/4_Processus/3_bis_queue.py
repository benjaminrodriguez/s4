import datetime
from multiprocessing import Process, Queue
from queue import Empty, Full

queue_in, queue_out = Queue(), Queue()

def reader(source, queue):
    for line in open(source):
        a,b = line.split()
        queue.put((float(a), float(b)))

def adder(qin, qout):
    try:
        while True:
            x,y = qin.get(timeout=2)
            qout.put(x+y)
    except Empty:
        pass

def writer(output, qout):
    with open(output, 'w') as fd:
        try:
            while True:
                item = qout.get(timeout=2)
                fd.write('{:f}\n'.format(item))
        except Empty:
            pass


r = Process(target=reader, args=('data3.txt', queue_in))
a = [Process(target=adder, args=(queue_in, queue_out)) for p in range(10)]
w = Process(target=writer, args=('output.txt', queue_out))

# Starting
timestamp1 = datetime.datetime.now()
w.start()
[p.start() for p in a]
r.start()

w.join()
[p.join() for p in a]
r.join()
timestamp2 = datetime.datetime.now()
print(timestamp2 - timestamp1)

