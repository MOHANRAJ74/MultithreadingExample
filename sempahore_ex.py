from threading import Semaphore, Thread
import  time

sem=Semaphore(3)

def function(name):
    print(f"{name} is waiting acceess the resource.")
    sem.acquire()
    print(f"{name} has acquired the resource")
    time.sleep(0.5)
    print(f"{name} is releasing the reource.")
    sem.release()

threads=[]

for i in range(5):
    t=Thread(target=function, args=(f" Thread-{i+1}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()