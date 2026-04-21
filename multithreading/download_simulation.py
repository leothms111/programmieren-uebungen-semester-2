import time 
from threading import Thread

def open(link:str):
    print(f"Starte Öffnen von: {link}")
    time.sleep(3)
    print(f"Abrufen von {link} abgeschlossen")

links = ["link1", "link2", "link3", "link4"]
threads = []


print("Starte Abrufen der Links")
for link in links:
    thread = Thread(target=open, args=(link,))
    threads.append(thread)
    thread.start()

for worker in threads:
    worker.join()

print("Abrufen abgeschlossen")

