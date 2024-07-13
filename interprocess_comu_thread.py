import threading
import time

shared_data = []

lock = threading.Lock()

condition = threading.Condition(lock)

def producer():
    global shared_data
    for i in range(5):
        time.sleep(1)
        with condition:
            shared_data.append(i)
            print(f'Produced: {i}')
            condition.notify()
def consumer():
    global shared_data
    for i in range(5):
        with condition:
            condition.wait()
            item = shared_data.pop(0)
            print(f'Consumed: {item}')

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
