class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return False
        self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0

inp_str ="(hallo))"
stack = MyStack()
is_correct = True

for char in inp_str:
    if char == "(":
        stack.push("(")
    elif char == ")":
        res = stack.pop()
        if res == False:
            is_correct = False
            break

if is_correct:
    is_correct = stack.is_empty()

print(is_correct)
