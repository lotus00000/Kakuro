import threading
import time

stop_event = threading.Event()
def timer():
    i = 0
    while not stop_event.is_set():
        i+=1
        print(i)
        time.sleep(1)

thread = threading.Thread(target=timer)
thread.start()
time.sleep(5)
print(thread.is_alive())
stop_event.set()
print(thread.is_alive())
thread.join()
print(thread.is_alive())