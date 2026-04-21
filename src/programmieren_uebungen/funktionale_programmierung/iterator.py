from time import sleep

class Countdown:
    def __init__(self, number):
        self.number = number + 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number <= 0:
            raise StopIteration
        self.number -= 1
        return self.number
    

class StepIterator:
    def __init__(self, liste: list, step: int):
        self.list = liste
        self.step = step
        self.i = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= len(self.list):
            raise StopIteration
        val = self.list[self.i]
        self.i += self.step
        return val
    
class DoubleCharIterator:
    def __init__(self, text:str):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            val =  self.text[self.index]*2
            self.index += 1
            return val
        except IndexError:
            raise StopIteration
    

def print_step_list():

    mylist = [number for number in range(30)]

    step_it = StepIterator(mylist, 3)


    while True:
        try:
            print(next(step_it))
            sleep(0.5)
        except StopIteration:
            break

def countdown():

    mycountdown = Countdown(5)
    while True:
        try:
            print(next(mycountdown))
            sleep(0.5)
        except StopIteration:
            break

def doublechar():
    iterator = DoubleCharIterator("abc")
    while True:
        try:
            print(next(iterator))
            sleep(0.5)
        except StopIteration:
            break


