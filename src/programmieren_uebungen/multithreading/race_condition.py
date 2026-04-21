import time 
from threading import Thread, Lock

counter = 0

def increment_counter():
    global counter
    for _ in range(1_000_000):
        counter+=1

thread1= Thread(target=increment_counter)
thread2= Thread(target=increment_counter)

print("Starte increment")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("increment beendet")
print(counter)
