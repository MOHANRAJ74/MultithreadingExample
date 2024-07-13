from threading import *
from time import *

def display(str1):
    for x in str1:
        print(x)

t1=Thread(target=display, args=('HELLO WORLD',))
t2=Thread(target=display, args=('you are wellcome',))

t1.start()
t2.start()

t1.join()
t2.join()
