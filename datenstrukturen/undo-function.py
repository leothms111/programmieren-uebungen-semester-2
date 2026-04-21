import keyboard
import time

class MyStack:
    def __init__(self):
        self.items = []

    def add_word(self, items):
        for item in items:
            self.items.append(item)

    def undo(self):
        if not self.items:
            return False
        self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display_stack(self):
        print(" ".join(self.items))

stack = MyStack(

)
while True:
    inp = input("Gib hier den Inhalt deines Dokuments ein:\n").split(" ")
    stack.add_word(inp)
    if keyboard.is_pressed('ctrl+m'):
        print("Kombination Strg + Z wurde erkannt!")
        time.sleep(0.5) 
    if keyboard.is_pressed('ctrl+s'):
        print("Kombination Strg + s wurde erkannt!")
        stack.display_stack()
        time.sleep(0.5) 
    
    if keyboard.is_pressed('esc'):
        print("Programm beendet.")
        break

