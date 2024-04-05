import time
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(1)

class hai(Thread):
    def run(self):
        for j in range(5):
            print('hai')


hel=hello()
ha=hai()
hel.start()
time.sleep(0.2)
ha.start()
hel.join()
ha.join()

print("bye")