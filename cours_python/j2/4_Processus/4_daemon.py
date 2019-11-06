import os
import time

print("Daemon testing.")

def timer(t, output):
    t1 = time.time() + t
    while time.time() < t1:
        open(output,'a').write('ok! %s\n' % time.time())
        time.sleep(1)

if not os.fork():
    os.setsid()
    os.close(0)
    os.close(1)
    os.close(2)
    if not os.fork():
        timer(10, 'resultat.txt')

# autres choses...
 
