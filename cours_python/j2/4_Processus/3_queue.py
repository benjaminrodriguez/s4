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

def writer(qout):
    try:
        while True:
            item = qout.get(timeout=2)
            print(item)
    except Empty:
        pass


r = Process(target=reader, args=('data.txt', queue_in))
a = [Process(target=adder, args=(queue_in, queue_out)) for p in range(3)]
w = Process(target=writer, args=(queue_out,))

w.start()
[p.start() for p in a]
r.start()

